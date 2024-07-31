def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for pred, gr_tr in zip(prediction, ground_truth):
        if pred == gr_tr & gr_tr == True:
            TP += 1
        if pred == gr_tr & gr_tr == False:
            TN += 1
        if pred != gr_tr & gr_tr == True:
            FN += 1
        if pred != gr_tr & gr_tr == False:
            FP += 1
            
    
    if TP + FP != 0:
        precision = TP / (TP + FP)
    if TP + FN != 0:
        recall = TP / (TP + FN)
    if precision + recall:
        f1 = 2 * precision * recall / (precision + recall)
    if TP + TN + FP + FN != 0:
        accuracy = TP + TN / (TP + TN + FP + FN)
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    accuracy = 0
    for pred, gt_tr in zip(prediction, ground_truth):
        if pred == gt_tr:
            accuracy += 1
    return accuracy / len(prediction)
