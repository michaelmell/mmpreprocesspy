import os
import shutil
from unittest import TestCase


class TestPreproc_fun(TestCase):
    test_data_base_path = '/home/micha/Documents/01_work/git/MM_Testing'

    def test__dataset_19_no_flatfield(self):
        from mmpreprocesspy import preproc_fun
        import tifffile as tff

        data_directory = self.test_data_base_path + '/19__dany__20201123_comlac_3conds_5/MMStack/'
        directory_to_save = self.test_data_base_path + '/19__dany__20201123_comlac_3conds_5/MMStack/result_no_flatfield/'
        positions = [0]
        maxframe = 1
        dark_noise = 90
        gaussian_sigma = 5
        main_channel_angle = 0
        # main_channel_angle = None
        growthlane_length_threshold = 200

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, maxframe=maxframe, dark_noise=dark_noise,
                                growthlane_length_threshold=growthlane_length_threshold, gaussian_sigma=gaussian_sigma, main_channel_angle=main_channel_angle)

        image_with_rois = tff.imread(os.path.join(directory_to_save, "Pos0_GL_index_initial.tiff"))
        self.show_image(image_with_rois)


    def test__dataset_17_no_flatfield(self):
        from mmpreprocesspy import preproc_fun
        import tifffile as tff

        data_directory = self.test_data_base_path + '/17_lis_20201218_VNG40_AB6min_2h_1_1/MMStack/'
        directory_to_save = self.test_data_base_path + '/17_lis_20201218_VNG40_AB6min_2h_1_1/MMStack/result_no_flatfield/'
        positions = [0]
        maxframe = 1
        dark_noise = 90
        gaussian_sigma = 5
        main_channel_angle = 90
        # main_channel_angle = None
        growthlane_length_threshold = 200

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, maxframe=maxframe, dark_noise=dark_noise,
                                growthlane_length_threshold=growthlane_length_threshold, gaussian_sigma=gaussian_sigma, main_channel_angle=main_channel_angle)

        image_with_rois = tff.imread(os.path.join(directory_to_save, "Pos0_GL_index_initial.tiff"))
        self.show_image(image_with_rois)

    def test__dataset_16_no_flatfield(self):
        from mmpreprocesspy import preproc_fun
        import tifffile as tff

        data_directory = self.test_data_base_path + '/16_thomas_20201229_glc_lac_1/MMStack/'
        directory_to_save = self.test_data_base_path + '/16_thomas_20201229_glc_lac_1/MMStack/result_no_flatfield/'
        positions = [0]
        maxframe = 20
        dark_noise = 90
        gaussian_sigma = 5
        growthlane_length_threshold = 300

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, maxframe=maxframe, dark_noise=dark_noise,
                                growthlane_length_threshold=growthlane_length_threshold, gaussian_sigma=gaussian_sigma)

        image_with_rois = tff.imread(os.path.join(directory_to_save, "Pos0_GL_index_initial.tiff"))
        self.show_image(image_with_rois)

    def test__dataset_15_no_flatfield(self):
        from mmpreprocesspy import preproc_fun
        import tifffile as tff

        data_directory = self.test_data_base_path + '/15_lis_20201119_VNG1040_AB2h_2h_1/MMStack/'
        directory_to_save = self.test_data_base_path + '/15_lis_20201119_VNG1040_AB2h_2h_1/MMStack/result_no_flatfield/'
        positions = [1]
        maxframe = 1
        dark_noise = 90
        gaussian_sigma = 5
        main_channel_angle = 90
        # main_channel_angle = None
        growthlane_length_threshold = 300

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, maxframe=maxframe, dark_noise=dark_noise,
                                growthlane_length_threshold=growthlane_length_threshold, gaussian_sigma=gaussian_sigma,
                                main_channel_angle=main_channel_angle)

        image_with_rois = tff.imread(os.path.join(directory_to_save, "Pos1_GL_index_initial.tiff"))
        self.show_image(image_with_rois)

    def test__dataset_14_no_flatfield(self):
        from mmpreprocesspy import preproc_fun
        import tifffile as tff

        data_directory = self.test_data_base_path + '/14_thomas_20201228_glc_ara_1/MMStack/'
        directory_to_save = self.test_data_base_path + '/14_thomas_20201228_glc_ara_1/MMStack/result_no_flatfield/'
        positions = [0]
        maxframe = 1
        dark_noise = 90
        gaussian_sigma = 5
        growthlane_length_threshold = 300

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, maxframe=maxframe, dark_noise=dark_noise,
                                growthlane_length_threshold=growthlane_length_threshold, gaussian_sigma=gaussian_sigma)

        image_with_rois = tff.imread(os.path.join(directory_to_save, "Pos0_GL_index_initial.tiff"))
        self.show_image(image_with_rois)

    def test__dataset_13_with_flatfield(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/13_20200128_glcIPTG_glc_1/MMStack/RawData/measurement'
        flatfield_directory = self.test_data_base_path + '/13_20200128_glcIPTG_glc_1/MMStack/RawData/flatfield'
        directory_to_save = self.test_data_base_path + '/13_20200128_glcIPTG_glc_1/MMStack/result_with_flatfield/'
        positions = [1]

        minframe = 1
        maxframe = 8
        dark_noise = None
        gaussian_sigma = None
        growthlane_length_threshold = 300

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, minframe=minframe, maxframe=maxframe,
                                growthlane_length_threshold=growthlane_length_threshold, flatfield_directory=flatfield_directory,
                                dark_noise=dark_noise, gaussian_sigma=gaussian_sigma)

    def test__dataset_10_with_flatfield(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack/RawData/measurement'
        flatfield_directory = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack/RawData/flatfield'
        directory_to_save = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack/result_with_flatfield/'
        positions = [0]
        minframe = None
        maxframe = 8
        dark_noise = None
        gaussian_sigma = None

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, minframe=minframe, maxframe=maxframe,
                                growthlane_length_threshold=300, flatfield_directory=flatfield_directory,
                                dark_noise=dark_noise, gaussian_sigma=gaussian_sigma)

    def test__dataset_11_with_flatfield(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/11_20190910_glc_spcm_1/MMStack'
        flatfield_directory = self.test_data_base_path + '/11_20190910_glc_spcm_1/MMStack/flatfield'
        directory_to_save = self.test_data_base_path + '/11_20190910_glc_spcm_1/MMStack/result_with_flatfield/'
        positions = [0]
        minframe = None
        maxframe = 8
        dark_noise = None
        gaussian_sigma = None

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, minframe=minframe, maxframe=maxframe,
                                growthlane_length_threshold=300, flatfield_directory=flatfield_directory,
                                dark_noise=dark_noise, gaussian_sigma=gaussian_sigma)

    def test__dataset_11_no_flatfield(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/11_20190910_glc_spcm_1/MMStack'
        directory_to_save = self.test_data_base_path + '/11_20190910_glc_spcm_1/MMStack/result_no_flatfield/'
        positions = [0]
        minframe = None
        maxframe = 8
        dark_noise = 90
        gaussian_sigma = 5

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, maxframe=maxframe,
                                growthlane_length_threshold=300, dark_noise=dark_noise, gaussian_sigma=gaussian_sigma)

        # preproc_fun.preproc_fun(data_directory, directory_to_save, positions, maxframe=maxframe, dark_noise=dark_noise,
        #                         gaussian_sigma=gaussian_sigma)

    def test__dataset_12_with_flatfield(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/12_20190816_Theo/MMStack/'
        flatfield_directory = self.test_data_base_path + '/12_20190816_Theo/MMStack/flatfield'
        directory_to_save = self.test_data_base_path + '/12_20190816_Theo/MMStack/result_with_flatfield/'
        positions = [0]
        minframe = None
        maxframe = 8
        dark_noise = 90
        gaussian_sigma = 5

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, minframe=minframe, maxframe=maxframe, flatfield_directory=flatfield_directory, dark_noise=dark_noise,
                                gaussian_sigma=gaussian_sigma)

    def test__dataset_12_no_flatfield(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/12_20190816_Theo/MMStack/'
        directory_to_save = self.test_data_base_path + '/12_20190816_Theo/MMStack/result_no_flatfield/'
        positions = [0]
        maxframe = 8
        dark_noise = 90
        gaussian_sigma = 5

        if os.path.isdir(directory_to_save):
            shutil.rmtree(directory_to_save)

        preproc_fun.preproc_fun(data_directory, directory_to_save, positions, maxframe=maxframe, dark_noise=dark_noise,
                                gaussian_sigma=gaussian_sigma)

    def test__dataset_11(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/11_20190910_glc_spcm_1/MMStack'
        directory_to_save = data_directory
        positions = [0]
        maxframe = 5

        results_directory = directory_to_save + '/result/'
        if os.path.isdir(results_directory):
            shutil.rmtree(results_directory)

        preproc_fun.preproc_fun(data_directory, results_directory, positions=positions, maxframe=maxframe, growthlane_length_threshold=300)

    def test__dataset_04(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/04_20180531_gluIPTG5uM_lac_1/MMStack'
        directory_to_save = data_directory
        positions = [0]
        maxframe = 10

        results_directory = directory_to_save + '/result/'
        if os.path.isdir(results_directory):
            shutil.rmtree(results_directory)

        preproc_fun.preproc_fun(data_directory, results_directory, positions=positions, maxframe=maxframe)

    def test__dataset_08(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/08_20190222_LB_SpentLB_TrisEDTA_LB_1/MMStack'
        directory_to_save = data_directory
        positions = [0]
        maxframe = 10

        results_directory = directory_to_save + '/result/'
        if os.path.isdir(results_directory):
            shutil.rmtree(results_directory)

        preproc_fun.preproc_fun(data_directory, results_directory, positions=positions, maxframe=maxframe)

    def test__dataset_10(self):
        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack/RawData/measurement'
        flatfield_directory = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack/RawData/flatfield'
        directory_to_save = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack'
        positions = [0]
        minframe = None
        maxframe = 8
        dark_noise = 90
        gaussian_sigma = 5

        results_directory = directory_to_save + '/result/'
        if os.path.isdir(results_directory):
            shutil.rmtree(results_directory)

        preproc_fun.preproc_fun(data_directory, results_directory, positions, minframe=minframe, maxframe=maxframe, flatfield_directory=flatfield_directory, dark_noise=dark_noise,
                                gaussian_sigma=gaussian_sigma)

    def test__dataset_10__shift_is_determined_correctly(self):
        # There is jump of the image position in dataset 10 going from frame 603 to 604. This trips up the current
        # current implementation. This test was created for debugging this issue.

        from mmpreprocesspy import preproc_fun

        data_directory = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack/RawData/measurement'
        flatfield_directory = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack/RawData/flatfield'
        directory_to_save = self.test_data_base_path + '/10_20190424_hi2_hi3_med2_rplN_glu_gly/MMStack/result'
        positions = [0]
        minframe = 590
        maxframe = 610
        dark_noise = 90
        gaussian_sigma = 5

        results_directory = directory_to_save + '/result/'
        if os.path.isdir(results_directory):
            shutil.rmtree(results_directory)

        preproc_fun.preproc_fun(data_directory, results_directory, positions, minframe=minframe, maxframe=maxframe, flatfield_directory=flatfield_directory, dark_noise=dark_noise,
                                gaussian_sigma=gaussian_sigma)

    def test__get_gl_tiff_path(self):
        from mmpreprocesspy import preproc_fun

        gl_file_path = preproc_fun.get_gl_tiff_path('/path/to/file', 'experiment_name', '1', '5')
        print(gl_file_path)
        print(os.path.dirname(gl_file_path))

    def show_image(self, imdata):
        import matplotlib.pyplot as plt

        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        # axes.plot(xs, ys)
        axes.imshow(imdata, cmap='gray')
        axes.get_xaxis().set_visible(False)
        fig.tight_layout(pad=0)
        plt.axis('off')
        plt.show()


