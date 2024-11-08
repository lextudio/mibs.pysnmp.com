"""SNMP MIB module (XEROX-JOB-MONITORING-TC) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-JOB-MONITORING-TC
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:17 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Counter32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Integer32,
 Gauge32,
 Bits,
 MibIdentifier,
 TimeTicks,
 Counter64,
 ModuleIdentity,
 ObjectIdentity,
 iso,
 NotificationType,
 Unsigned32,
 IpAddress) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Integer32",
    "Gauge32",
    "Bits",
    "MibIdentifier",
    "TimeTicks",
    "Counter64",
    "ModuleIdentity",
    "ObjectIdentity",
    "iso",
    "NotificationType",
    "Unsigned32",
    "IpAddress")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmJobMonTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58)
)
xcmJobMonTC.setLastUpdated("0209170000Z")
if mibBuilder.loadTexts:
    xcmJobMonTC.setOrganization("""\
Xerox Corporation - Common MIB Working Group
""")
xcmJobMonTC.setContactInfo("""\
 XCMI Editors E-Mail: coherence@crt.xerox.com -- --
""")
if mibBuilder.loadTexts:
    xcmJobMonTC.setDescription("""\
 File: 40jobtc.dfm, .mib, .pdf, .txt Version: 5.11.pub This textual-convention
module defines textual- conventions for use with the Job Monitoring MIB,
module: XEROX-JOB-MONITORING-MIB. Also the explanatory material with this
module explains the Job Monitoring MIB. These textual-conventions and
explanations are in a separate module from the Job Monitoring MIB, so that they
may be republished when additional enums are added or more explanatory material
is added without needing to republish the Job Monitoring MIB, thus increasing
the stability of the Job Monitoring MIB. Copyright 1996-2002 Xerox Corporation.
All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmJMJobServiceTypeOID(TextualConvention, ObjectIdentifier):
    status = "current"
    if mibBuilder.loadTexts:
        description = """\
Specifies the type of service to which the job has been submitted. The service
type is represented as a single OID, rather than as an OID for a source-type
and an OID for a destination-type, so that more general and arbitrary service
types can be created, such as services with more than one destination type, or
ones with only a source or only a destination.
"""


class XcmJMJobState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              11,
              12,
              13,
              14,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("completed", 17),
          ("created", 3),
          ("held", 12),
          ("interrupted", 8),
          ("other", 1),
          ("paused", 13),
          ("pending", 6),
          ("printing", 18),
          ("processing", 7),
          ("retained", 11),
          ("terminating", 14),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
A job may be in any of the states defined by this textual- convention. The
Xerox Job model is a refinement of the ISO DPA standard and generalizes to non-
printing devices. The textual definitions given here are an abbreviation of the
full specification of the semantics of the job states given in the Xerox Job
Model specification. Agent implementers of this MIB need to refer to the Xerox
Job Model specification in addition to this textual convention. Traps shall be
generated when a job performs a job state transition. In order to reduce
network traffic, it is recommended, but not required, that an implementation
suppress traps for self-loops. The xcmJobPreviousState can be used to detect
self-loops and suppress self-loop traps by not sending traps when the value of
the xcmJobPreviousState is the same as the value of the xcmJobCurrentState.
When a job is in the processing state, the state of the assigned device(s) is
needed to fully represent the state of the job. In addition, the job-state-
reasons attributes provides additional, more abstract, user feedback about what
is happening to the job when the job is in many of its states. See the Xerox
Job Model Specification, Phase 1 or later for the specification of which job-
state-reasons values may be used with which job states.. ISO DPA: Job-current-
state Standard values are defined for the current-job-state and previous-job-
state attributes of the DPA job object, as follows: unknown The job state is
not known, or is indeterminate, or is not returned by the operation. (id-val-
job-state-unknown) creating The job has been created on the server by the
create-job sub-operation of the Submit request, but a Submit request with
neither (1) a TRUE value for the job-submission-complete component of the
SubmitArgument nor (2) a TRUE value for the job-process-before-completely-
specified (long jobs) job attribute has not yet been received and no document
has started processing. The job maybe in the process of being checked by the
server for attributes, defaults being applied, a device being selected, etc.
[Renamed from ISO DPA pre-processing state, but kept the same enum code, since
the semantics are identical.] (id-val-job- state-pre-processing) NOTE: The
Xerox Job Model transitory state: evaluate-hold shall not be visible to
requesters, and therefore is not in the Job Monitoring MIB. held The job is
waiting to be released for scheduling for any number of reasons as specified by
the value of the job's job- state-reasons attribute. (id-val-job- state-held)
See the Xerox Job Model Specification, Phase 1 or later for the specification
of which job-state-reasons values may be used when the job is in the held
state. pending The job is waiting to start processing on a device and has no
shared system resources assigned to it yet. (id-val-job-state-pending) [The ISO
DPA processing and printing states have been combined into a single job state,
called processing, which includes any device activity, so that the job life
cycle can be used for all kinds of jobs, not just printing jobs, and have the
same life cycle. The printing state is DEPRECATED. In addition, the difference
between the ISO DPA processing state and printing state was one of user feed
back only. The standard specified no differences in job state transitions
between the processing and printing states. Therefore, ISO DPA should have used
the device- state-of-devices-assigned mechanism to provide the user feedback
distinction between the processing and printing states. In fact, neither
Novell's NDPS nor IBM's PSM DPA products implement the printing state, only the
processing state. Only Printxchange implements the printing state (as well as
the processing state). So we will propose to ISO DPA that the DPA printing
state be deprecated. [For convenience in understanding the difference between
ISO DPA and the Job Monitoring MIB (and the Xerox Job Model), the ISO DPA
processing and printing specifications are given here first, followed by the
new (Xerox) definition of processing which incorporates the semantics of the
ISO DPA processing and printing states, and extends these semantics to sub-
jobs.] [ISO DPA processing specification: The server is processing the job, or
has made the job ready for printing, but the output device is not yet printing
it, either because the job hasn't reached the output device or because the job
is queued in the output device or some other spooler, awaiting the output
device to print it.] [ISO DPA printing state specification which is DEPRECATED
by the Job Monitoring MIB: The server has completed processing the job and the
output device is currently printing the job on at least one printer. That is, a
print engine is either printing pages of the job, or failing in its attempt to
print pages of the job because of some wait state, such as, start-wait, end-
wait, needs-attention, etc. The complete job state includes the detailed status
represented in the printers' printer- state attribute(s).] [The following Xerox
definition of the 'processing' job state combines the ISO DPA processing and
printing states into a single state, called 'processing', which can be used
with any kind of device: processing The server is: (1) processing the job, or
(2) has made the job ready for processing, but the device is not yet processing
it, either: (a) because the job hasn't reached the device or (b) because the
job is queued in the device or some other spooler, awaiting the device to
process it or (3) has completed processing the job and the device is currently
processing (printing, scanning, sending-fax, receiving-fax, sending-e-mail,
filing, or retrieving) the job on at least one device. That is, a device is
either performing input-output of the job, or failing in its attempt to perform
input-output of the job because of some wait state, such as, start-wait, end-
wait, needs-attention, etc. Additional information about the job's current
state is also given in the job's job-state-reasons attribute for when the job
is in any of its states, including processing. See the Xerox Job Model for
which values of the job's job-state-reasons attribute may be used when the job
is in the processing state. NOTE: DPA does not yet have any job-state-reasons
defined for the processing/printing states. (id-val-job-state-processing)]
paused The job has been paused as a result of a PauseJob request. NOTE: The
Xerox Job Model has renamed the PauseJob and ResumeJob operations to HoldJob
and ReleaseJob and has changed the semantics to put the job back into the held
state, with the job-hold attribute set to TRUE and the job-hold-set value added
to the job-state-reasons attribute instead of putting into the paused state. So
the paused state remains only for use with ISO DPA systems that have
implemented the paused state. (id-val-job-state-paused) interrupted The job was
interrupted by the InterruptJob request for an intervening job, and shall
resume processing automatically once the intervening job has completed. The
interrupted job may relinquish shared resources and devices to the interrupting
job, but not to other jobs. (id-val-job-state-interrupted) terminating The job
has been cancelled by a CancelJob request or aborted by the server and is in
the process of terminating. The job's job- state-reasons attribute contains the
reasons that the job is being terminated. (id-val-job-state-terminating)
retained The job is being retained at the server as a result of the job's job-
retention-period being non-zero. The job has (1) completed successfully or with
warnings or errors, (2) been aborted while [processing] printing by the server,
or (3) been cancelled by the CancelJob request before or during processing. The
job's job-state-reasons attribute contains the reasons that the job has been
retained. While in the retained state, all of the job's document data (and
resources, if any) shall be retained by the server; thus a job in the retained
state [could be resubmitted using the Resubmit request in ISO DPA Part 3.].
ResubmitJob shall create a new job object instance and assign a new job-
identifier. See the Xerox Job Model spec. (id-val-job-state-retained) completed
The job has either: (1) completed successfully or with warnings or errors, (2)
been aborted by the server while processing, or (3) been cancelled by the
CancelJob request, AND the job's: (1) job-retention-period was zero or has
expired, or (2) job-discard-time has arrived. OR a ResubmitJob operation has
been issued which forces the old job to the completed state and makes a new job
object instance with a new job identifier. See the Xerox Job Model
specification. The job's job-state-reasons attribute contains the reason(s)
that the job has been completed. While in the completed state, a job's document
data (and resources if any) need not be retained by the server; thus a job in
the completed state could not be resubmitted. The length of time that a job may
be in this state, before transitioning to unknown, is implementation-dependent.
However, servers that implement the completed job-state shall retain, as a
minimum, the following attributes for any job in the completed state: job-
identifier, job-owner, job-name, current-job-state, devices-assigned, and job-
state-reasons, plus as a Xerox extension, the accounting attributes:
xcmJobAccountingUserName, xcmJobAccountingInformation,
xcmJobStartedProcessingTime, xcmJobImpressionsCompleted,
xcmJobMediaSheetsCompleted, xcmJobCompletionTime, xcmJobWorkUnitType
XcmHrDevTrafficUnit, and xcmJobUnitsOfWorkCompleted so that an accounting
management application can copy the accounting data from the MIB before the job
is deleted from the MIB. Jobs that have been moved to the OPTIONAL 'Job
History' device SHALL be in the 'completed' state (or 'aborted' or 'canceled'
states with the PWG Job Mon MIB). (id-val-job-state-completed) This is a type 2
enum.
"""


class XcmJMJobStateReasons(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
This representation is bit-encoded, so that multiple reasons can occur at once.
Each bit corresponds to an ISO DPA OID for the same reason. The MIB enum value
is given by: value = 2 ** (last arc of DPA id-val-reasons-xxx OID -1) id-val-
reasons-documents-needed = 1.0.10175.1.6.19.1 See the Xerox Job Model
Specification, Phase 1 or later for the specification of which job-state-
reasons values may be used with which job states. ISO DPA: Job-state-reasons
This attribute identifies the reason or reasons that the job is in the held,
[processing,] terminating, retained, or completed state. The server shall
indicate the particular reason(s) by setting the value of the job-state-reasons
attribute. When the job is not in any of these states, the server shall set the
value of the job-state-reasons attribute to the empty set. The following
standard values are defined: jobIncoming 0x1 The job has been accepted by the
server or device, but the server or device is expecting (1) additional
operations from the client to finish creating the job and/or (2) is
accessing/accepting document data. NOTE - this reason has been renamed from the
ISO DPA 'documents-needed' to the IPP 'job-incoming' which has been generalized
to include the condition before the job has been closed by the client. (id-val-
reasons-documents-needed) jobHoldSet 0x2 The value of the job's job-hold
attribute is TRUE. (id-val- reasons-job-hold-set) jobProcessAfterSpecified 0x4
The value of the job's job-process-after attribute has specified a time
specification that has not yet occurred. Renamed from ISO DPA job-print-after-
specified. (id-val- reasons-job-process-after-specified)
requiredResourcesNotReady 0x8 At least one of the resources needed by the job,
such as media, fonts, resource objects, etc., is not ready on any of the
physical device's for which the job is a candidate. (id-val-reasons-required-
resources-not-ready) successfulCompletion 0x10 The job completed successfully.
(id-val-reasons-successful completion) completedWithWarnings 0x20 The job
completed with warnings. (id-val-reasons-completed- with-warnings)
completedWithErrors 0x40 The job completed with errors (and possibly warnings
too). (id-val-reasons-completed-with-errors) cancelledByUser 0x80 The job was
cancelled by the user using the CancelJob request. (id-val-reasons-cancelled-
by-user) cancelledByOperator 0x100 The job was cancelled by the operator using
the CancelJob request. (id-val-reasons-cancelled-by-operator) abortedBySystem
0x200 The job was aborted by the system. (id-val-reasons-aborted- by-system)
logfilePending 0x400 The job's logfile is pending file transfer. (id-val-
reasons-logfile-pending) logfileTransferring 0x800 The job's logfile is being
transferred. (id-val-reasons- logfile-transferring) The following bits are from
IPP (and start at the high end of the bits definitions): jobOutgoing 0x40000000
Configuration 2 only: The server is transmitting the job to the device. The
remaining bits are reserved for future standardization and shall not be used by
conforming implementations. This is the equivalent of a type 2 enum.
"""


class XcmJMJobXStateReasons(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
This representation is bit-encoded, so that multiple reasons can occur at once.
Each bit corresponds to a Xerox OID for the same Xerox extension to the ISO DPA
job state reason. In a DPA protocol, the DPA and Xerox OID can be intermixed.
But in a bit encoded SNMP information object, we need to keep the bit encodings
separate. The MIB enum value is given by: value = 2 ** (last arc of Xerox xid-
val-reasons-xxx OID) xid-val-reasons-cascaded = 1.2.840.113550.1.6.19.0 The
last arc is shown in parens in the description. ISO DPA: Job-state-reasons This
attribute identifies the reason or reasons that the job is in the held,
[processing] terminating, retained, or completed state. The server shall
indicate the particular reason(s) by setting the value of the job-state-reasons
[xcmJobStateReasons, xcmJobXStateReasons, and xcmX2StateReasons objects]
attribute. When the job is not in any of these states, the server shall set the
value of the job-state-reasons attribute to the empty set. The following values
are defined as Xerox extensions. The specification is copied from the Xerox Job
Model, Phase 1, updated to version 0.67, 12/20/96. NOTE: In the Xerox Job
Model, the acronym JSP stands for Job Service Provider. In ISO DPA and this MIB
the term server is used equivalently to JSP. The extensions defined by
Printxchange: cascaded 0x1 (0) After the outbound gateway retrieves all job and
document attributes and data, it stores the information into a spool directory.
Once it has done this, it sends the supervisor a job-processing event with this
job-state-reason which tells the supervisor to transition to a new job state.
deletedByAdministrator 0x2 (1) The administrator has issued a Delete operation
on the job or a Clean operation on the server or queue containing the job;
therefore the job may have been cancelled before or during processing, and will
have no retention-period or completion-period. discardTimeArrived 0x4 (2) The
job has been deleted (cancelled with the job- retention-period set to 0) due to
the fact that the time specified by the job's job-discard-time has arrived [if
the job had already completed, the only action that would have occurred is that
the job-retention-period would be set to 0 and the job is deleted].
postprintFailed 0x8 (3) The post-processing agent failed while trying to log
accounting attributes for the job; therefore the job has been placed into
retained state for a system-defined period of time (Printxchange, 5 minutes),
so the administrator can examine it, resubmit it, etc. The post-processing
agent is a plug-and-play mechanism which the system and the customer uses to
add functionality that is executed after a job has finished processing.
submissionInterrupted 0x10 (4) Indicates that the job was not completely
submitted for the following reasons: (1) the server has crashed before the job
was closed by the client. The server shall put the job into the completed state
(and shall not process the job). (2) the server or the document transfer method
has crashed in some non-recoverable way before the document data was entirely
transferred to the server. The server shall put the job into the completed
state (and shall not process the job). (3) the client crashed or failed to
close the job before the time-out period (Printxchange, 20 minutes). The server
shall close the job and put the job into the held state with job-state-reasons
of submission-interrupted and job-hold-set and with the job's job-hold
attribute set to TRUE. The user may release the job for scheduling by issuing
the ReleaseJob operation. maxJobFaultCountExceeded 0x20 (5) The job has been
faulted and returned by the server several times and that the job-fault-count
exceeded the device's (or server's, if not defined for the device) cfg- max-
job-fault-count. The job is automatically put into the held state regardless of
the hold-jobs-interrupted-by- device-failure attribute. This job-state-reasons
value is used in conjunction with the job-interrupted-by-device- failure value.
Job timed-out while processing (optional): Implementation option: The following
values of job-state- reasons are derived from ISO DPA printer states for use
when the system moves a processing job to the held state because a site-
settable time-out condition was exceeded while the job was in the processing
state: devicesNeedAttentionTimeOut 0x40 (6) One or more document transforms
that the job is using needs human intervention in order for the job to make
progress, but the human intervention did not occur within the site-settable
time-out value and the JSP has transitioned the job to the held state.
needsKeyOperatorTimeOut 0x80 (7) One or more devices or document transforms
that the job is using need a specially trained operator (who may need a key to
unlock the device and gain access) in order for the job to make progress, but
the key operator intervention did not occur within the site-settable time-out
value and the JSP has transitioned the job to the held state.
jobStartWaitTimeOut 0x100 (8) The JSP has stopped the job at the beginning of
processing to await human action, such as installing a special cartridge or
special non-standard media, but the job was not resumed within the site-
settable time-out value and the JSP has transitioned the job to the held state.
Normally, the job is resumed by means outside the job model, such as some local
function on the device. jobEndWaitTimeOut 0x200 (9) The JSP has stopped the job
at the end of processing to await human action, such as removing a special
cartridge or restoring standard media, but the job was not resumed within the
site-settable time-out value and the JSP has transitioned the job to the
retained state. Normally, the job is resumed by means outside the job model,
such as some local function on the device, whereupon the job shall transition
immediately to the terminating state. jobPasswordWaitTimeOut 0x400 DEPRECATED:
(10) The JSP has stopped the job at the beginning of processing to await input
of the job's password, but the human intervention did not occur within the
site-settable time-out value and the JSP has transitioned the job to the held
state. Normally, the password is input and the job is resumed by means outside
the job model, such as some local function on the device. This value is
DEPRECATED because the JSP shall move Secure Jobs from processing to held when
they are the next to run and set the jobPasswordWait job-state-reason, so that
the device is not blocked. deviceTimedOut 0x800 (11) A device that the job was
using has not responded in a period specified by the device's site-settable
device- timeout-period attribute (In ISO DPA the printer's printer- timeout-
period attribute). connectingToDeviceTimeOut 0x1000 (12) The JSP is attempting
to connect to one or more devices which may be dial-up, polled, or queued, and
so may be busy with traffic from other systems, but JSP was unable to connect
to the device within the site-settable time-out value and the JSP has
transitioned the job to the held state Reasons used when the job is in
processing state: The following values for the job-state-reasons attribute have
been added by the Job Model team to give requesters feedback about the job when
the job is in the processing state: transferring 0x2000 (13) The job is being
transferred to a down stream server or device. queueInDevice 0x4000 (14) The
job has been queued in a down stream server or device. jobCleanup 0x8000 (15)
The JSP is performing cleanup activity as part of ending normal processing.
processingToStopPoint 0x10000 (16) The requester has issued an InterruptJob
operation and the JSP is processing up until the specified stop point occurs.
Other reasons added by the Xerox Job Model: The following values for the job's
job-state-reasons attribute have been added by the Xerox Job Model team:
jobPasswordWait 0x20000 (17) Either: (1) The JSP has selected the Secure Job to
be next to process, but instead of assigning resources and starting the job
processing, the JSP has transitioned the job to the held state to await entry
of a password (and dispatched another job, if there is one) OR (2) the JSP has
interpreted (ripped) the Secure Job and the marker is scheduled separately, so
that the JSP transitions the job to the held state to await entry of a password
(and dispatched another job, if there is one). The user resumes the job either
locally or by issuing a ReleaseJob supplying a job-password=secret-code input
parameter that SHALL match the job's job-password attribute. validating 0x40000
(18) The job is validating the job after a CreateJob operation. The job state
may be creating, held, pending, or processing. queueHeld 0x80000 (19) The
operator has held the entire queue by means outside the scope of the Job model.
jobProofWait 0x100000 (20) The job has produced a single proof copy and is in
the held state waiting for the requester to issue the ReleaseJob operation to
release the job to print normally, obeying the job-copies and copy-count job
and document attributes that were originally submitted. heldForDiagnostics
0x200000 (21) The system is running intrusive diagnostics, so the all jobs are
being held. serviceOffLine 0x400000 (22) The service/document transform is off-
line and accepting no jobs. All pending jobs are put into the held state. This
could be true if its input is impaired or broken. noSpaceOnServer 0x800000 (23)
The job is held because there is no room on the server to store all of the job.
For example, there is no room for the document data or a scan-to-file job.
pinRequired 0x1000000 (24) The device requires that a pin be entered in order
to proceed, because the PIN was not supplied with the document or job.
exceededAccountLimit 0x2000000 (25) The account for which this job is drawn has
exceeded its limit. This condition should be detected before the job is
scheduled so that the user does not wait until his/her job is scheduled only to
find that the account is overdrawn. This condition may also occur while the job
is processing either as processing begins or part way through processing. An
overdraft mechanism should be included to be user- friendly, so as to minimize
the chances that the job cannot finish or that media is wasted. For example,
the JSP should finish the current copy for a job with collated document copies,
rather than stopping in the middle of the current document copy.
jobHeldForRetry 0x4000000 (26) The job encountered some errors that the JSP
could not recover from with its normal retry procedures, but the error is worth
trying the job later, such as phone number busy or remote file system in-
accessible. For such a situation, the JSP shall add the held-for-retry value to
the job's job- state-reasons attribute and transition the job from the
processing to the held (via the evaluate-hold internal momentary state), rather
than to the retained state. The remaining bits are reserved for future
standardization and shall not be used by conforming implementations. This is
the equivalent of a type 2 enum.
"""


class XcmJMJobX2StateReasons(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
This representation is bit-encoded, so that multiple reasons can occur at once.
Each bit corresponds to a Xerox OID for the same Xerox extension to the ISO DPA
job state reason. In a DPA protocol, the DPA and Xerox OID can be intermixed.
But in a bit encoded SNMP information object, we need to keep the bit encodings
separate. XcmJMJobX2StateReasons provides an additional 31 bits for Xerox
extensions in addition to the 31 bits provided for by XcmJMJobXStateReasons.
The MIB enum value is given by: value = 2 ** (last arc of Xerox xid-val-
reasons-xxx OID -30) xid-val-reasons-xxx = 1.2.840.113550.1.6.19.30 jobPrinting
0x1 (30) At least one of the output device to which the job is assigned is
marking media. This value is useful for servers and output devices which spend
a great deal of time processing (1) when no marking is happening and then want
to show that marking is now happening or (2) when the job is in the process of
being canceled or aborted while the job remains in the 'processing' state, but
the marking has not yet stopped so that impression or sheet counts are still
increasing for the job. This job-state-reason value is defined in the PWG Job
Monitoring MIB and IPP. It has been generalized here for jobs that use more
than one device. This job-state-reason value should be used instead of the
'printing' which has been deprecated in this MIB (and is recommended against in
ISO DPA in a corrigenda). jobInterpreting 0x2 (31) The job is interpreting
document data. This job-state-reason value is defined in the PWG Job Monitoring
MIB and IPP. It has been generalized here for jobs that use more than one
device and for devices that can be interpreting more than one job at a time.
jobScanning 0x4 (32) At least one of the input devices to which the job is
assigned is scanning document data. jobFaxReceiving 0x8 (33) At least one of
the FAX devices to which the job is assigned is receiving FAX document data.
jobFaxSending 0x10 (34) At least one of the FAX devices to which the job is
assigned is sending FAX document data. jobFileReceiving 0x20 (35) The job is
receiving files or document data. jobFileSending 0x40 (36) The job is sending
files or document data. jobMailReceiving 0x80 (37) The job is receiving
electronic mail document data. jobMailSending 0x100 (38) The job is sending
electronic mail document data. value = 2 ** (30 - last arc of PSIS pid-val-
reasons-xxx OID) pid-val-reasons-cancelled-by-shutdown =
1.2.826.0.1050.8.1.6.19.0 NOTE: the Xerox extensions to DPA work from right to
left and X/Open PSIS extensions work from left to right, avoiding the sign bit.
The remaining bits (in the middle) are reserved for future standardization and
shall not be used by conforming implementations. The following PSIS bits are
defined using the PSIS extensions to ISO DPA starting with the left-most bit,
not counting the sign bit. These definitions are taken from the August 28,
1995, version 5.0 of the X/Open PSIS specification. [Text in brackets indicates
additions and clarifications made for the Job Monitoring MIB.]
cancelledByShutdown 0x40000000 the job was cancelled because the server or
device was shutdown before completing the job. The job shall be placed in the
pending state [if the job was not started, else the job shall be placed in the
terminating state]. deviceUnavailable 0x20000000 This job was aborted by the
system because the device is currently unable to accept jobs. This reason
[shall be] used in conjunction with the reason aborted-by-system. The job shall
be placed in the pending state. wrongDevice 0x10000000 This job was aborted by
the system because the device is unable to handle this particular job; the
spooler should try another device. This reason [shall be] used in conjunction
with the reason aborted-by-system. The job shall be pending if the queue
contains other physical devices that the job could process on, and the spooler
is capable of not sending the job back to a physical device that has rejected
the job for this job-state-reasons value. Otherwise, [the job] shall be
retained. badJob 0x8000000 This job was aborted by the system because this job
has a major problem[, such as an ill-formed PDL]; the spooler should not even
try another printer. This reason [shall be] used in conjunction with the reason
aborted-by-system. The job shall be placed in the [terminating] state.
jobInterruptedByDeviceFailure 0x4000000 The device or supervisor failed while
the job was [processing/]printing. The spooler is keeping the job in the held
state until an operator can determine what to do with the job. This is the
equivalent of a type 2 enum.
"""


class XcmJMDocType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("font", 4),
          ("other", 1),
          ("printable", 3),
          ("resource", 5),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
Jobs contain contained-documents. Contained-documents may be printable, font,
or resource objects. This had been deleted due to object deletions from
41jobmon.mib, but has been restored along with those objects. ISO DPA:
Document-type The following standard values are defined: printable Specifies
that this document is to be printed on the assigned printer. (id-val-document-
type- printable) font Specifies that this document is a font resource which may
be required by one or more of the printable documents associated with the
print- job. See the font object class. (id-val- document-type-font) resource
Specifies that this document contains resource data, of some type other than
font, which may be required to print one or more of the printable documents
associated with the print-job. See the resource object class. (id-val-document-
type-resource) This is a type 2 enum.
"""


class XcmJMDocFileNameType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("fntAutomatic", 3),
          ("fntBindery", 13),
          ("fntCDS", 7),
          ("fntDCE", 6),
          ("fntDECNS", 10),
          ("fntDNS", 9),
          ("fntInternetMail", 11),
          ("fntMVS", 28),
          ("fntNDS", 14),
          ("fntNIS", 8),
          ("fntNT", 27),
          ("fntNetWare", 33),
          ("fntOS2", 25),
          ("fntOS400", 30),
          ("fntPCDOS", 26),
          ("fntPOSIX", 23),
          ("fntUNC", 32),
          ("fntUNIX", 24),
          ("fntURL", 15),
          ("fntVM", 29),
          ("fntVMS", 31),
          ("fntX500", 4),
          ("fntXFN", 5),
          ("fntXNS", 12),
          ("other", 1),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The type of file name syntax from which a document is obtained for an output
job, such as print, or for which a document is produced for an input job, such
as scan- to-file. The file name syntax types are taken from ISO DPA for the
DistinguishedNameStringSyntax data type. This had been deleted due to object
deletions from 41jobmon.mib, but has been restored along with those objects.
ISO DPA: distinguished-name-syntax The following standard values are defined:
automatic server recognizes the syntax X-500 ISO 9594 Directory Service XFN
X/OPEN Federated Names DCE Distributed Computing Environment includes X.500 and
CDS CDS Cell Directory Service - part of DCE NIS Network Information Service
DNS Domain Name Service DEC-NS Digital Name Service Internet-mail Internet Mail
address XNS Xerox Network System Bindery Bindery example:
FILE_SERVER_NAME\OBJECT_NAME NDS Novell Directory Service example:
.objectName.container.organization or
.cn=objectName.ou=container.o=organization URL HTTP Universal Resource Locator
examples: http://www.organization-name.org/homepage.htm ftp://ftp-
out.external.hp.com/snmpmib/dpa/dpa-00.doc POSIX POSIX file name (ISO 9945-1)
-- file name types UNIX UNIX(TM) file name OS/2 OS/2 file name PC-DOS PC DOS
file name NT NT file name MVS MVS file name VM VM file name OS/400 OS/400 file
name VMS VMS file name UNC Microsoft Universal Name Convention example:
\\fileservername\volume\filepath\filename.ext NetWare NetWare file path name
example: servername\volume\filepath\filename.ext This is a type 2 enum.
"""


class XcmJMDocState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("completed", 6),
          ("other", 1),
          ("pending", 4),
          ("printing", 7),
          ("processing", 5),
          ("transferPending", 3),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The following standard values are defined for the state of contained-documents:
transferPending The server has created the document object, but the data
transfer of the document data has not started or completed (id-val-document-
state-transfer-pending) pending The server has received the document data and
the document is waiting for processing to begin. The job may already be in the
processing state, if the job's job-scheduling attribute is not after-complete
(see the current-job-state and job-scheduling job attributes. (id-val-document-
state- pending) processing The server has started processing this document, or
has made the document ready for processing by a device, but the device is not
yet processing it, either because the document hasn't reached the device or
because the document is queued in the device or some other spooler, awaiting
the device to process it, or the device has finished processingthe document and
some additional processing is needed, such as image processing after scanning.
(id-val-document-state- processing) printing The server has completed
processing the document and the output device is currently printing the
document on at least one printer. That is, a print engine is either printing
pages of the document, or failing in its attempt to print pages of the document
because of some wait state, such as, start-wait, end-wait, needs-attention,
etc. The complete document state includes the detailed status represented in
the devices' device-state attribute(s). NOTE: Other job-service-type-specific
states will be added in the future, such as scanning. completed The server has
completed this document. The job may still be in the processing state, or may
be in the retained state. The job shall move to the retained state when all
documents are completed (id-val-document-state-completed) This is a type 2
enum.
"""


class XcmJMDocOutputMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )

    if mibBuilder.loadTexts:
        description = """\
This object is bit coded, so that multiple document output requests may be made
for the document. Each bit corresponds to one of the ISO DPA output OIDs. ISO
DPA: Output This attribute identifies the output processing for the media on
which the document is to be printed. The following standard values are defined.
The value of the bit is given by the formula: bit value = 2 ** (last OID arc)
id-val-output-page-collate = 1.0.10175.1.6.115.0 pageCollate 0x1 This value
specifies that the pages of a document are to be in sequence, when multiple
copies of the document are specified by the copy-count attribute (possibly up
to some implementation-defined maximum number of copies). Whether this effect
is achieved by placing copies of the document in multiple output bins or in the
same output bin with implementation-defined document separation is
implementation-dependent. Also whether it is achieved by making multiple passes
over the document or by using an output sorter is implementation-dependent.
Either pageCollate or noPageCollate shall be set, but not both. If both
pageCollate and noPageCollate are set, the noPageCollate value shall be
ignored. (id-val-output-page- collate) noPageCollate 0x2 This value specifies
that the copies of the pages of a document are to follow one another when
multiple copies are specified by the copy-count attribute. That is, if 3 copies
are specified, three copies of page 1 are printed then three copies of page 2,
etc., and no collating of these pages is desired. This may be useful in some
implementations where multiple copies requires re-interpretation of the
document format and the document contains some compute intensive pages (such as
images) (id-val-output-no page-collate) decollate 0x10 The parts of a multi-
part form are to be separated and sorted into stacks for each part. Either
decollate or noDecollate shall be set, but not both. If both decollate and
noDecollate are set, the noDecollate value shall be ignored. (id-val-output-
decollate) noDecollate 0x20 The parts of a multi-part form are to remain intact
(id- val-output-no decollate) burst 0x40 Continuous media is to be separated
into individual sheets, generally by bursting along perforations. Either burst
or noBurst shall be set, but not both. If both burst and noBurst are set, the
noBurst value shall be ignored. (id-val-output-burst) noBurst 0x80 Continuous
media is to remain continuous, no bursting is desired (id-val-output-no burst)
stackingDefault 0x400 A site-defined output-stacking operation is to be applied
(id-val-output-stacking-default) This is the equivalent of a type 2 enum.
"""


class XcmJMGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Job Monitoring MIB groups supported by this management agent
implementation (i.e., version) on this host system, specified in a bit-mask.
The current set of values (which may be extended in the future) is given below:
1 : xcmJMBaseGroup -- 2**0 conditional 2 : xcmJMJobGenBasicGroup -- 2**1
conditional 4 : xcmJMDevicesAssignedGroup -- 2**2 deprecated 8 :
xcmJMClientIdMapGroup -- 2**3 optional 32 : xcmJMJobGenExtGroup -- 2**5
conditional 128 : xcmJMDocGenBasicGroup -- 2**7 conditional 256 :
xcmJMDocPrintExtGroup -- 2**8 conditional 512 : xcmJMJobGenSpoolingBasicGroup
-- 2**9 conditional 1024 : xcmJMJobGenSpoolingExtGroup -- 2**10 conditional
2048 : xcmJMJobGenAccountingBasicGroup -- 2**11 conditional 4096 :
xcmJMMediaConsumedGroup -- 2**12 conditional 8192 : xcmJMColorImpsConsumedGroup
-- 2**13 conditional 16384 : xcmJMJobAlertGroup -- 2**14 conditional 32768 :
xcmJMDocAlertGroup -- 2**15 conditional 65536 : xcmJMJobImpsByMediumSizeGroup
-- 2**16 conditional Note: The following had been deprecated, but have been
made current starting with version 4.00: xcmJMJobGenExtGroup,
xcmJMJobGenSpoolingBasicGroup, xcmJMJobGenAccountingBasicGroup,
xcmJMMediaConsumedGroup, and xcmJMJobImpsByMediumSizeGroup. The following had
been deleted, but are restored as of version 4.01: xcmJMDocGenBasicGroup,
xcmJMDocPrintExtGroup, xcmJMJobGenSpoolingExtGroup,
xcmJMColorImpsConsumedGroup, and xcmJMDocAlertGroup. The following were deleted
in v2.51: xcmJMJobStateMsgGroup and xcmJMJobTreeBasicGroup. Usage: Conforming
management agents shall ALWAYS accurately report their support for XCMI Job
Monitoring MIB groups.
"""


class XcmJMImpsCountType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              11,
              19,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("blackAndWhiteCount", 5),
          ("fourColorantCount", 24),
          ("fullColorCount", 7),
          ("highlightColorCount", 6),
          ("limitedVisibleColorCount", 19),
          ("oneColorantCount", 21),
          ("oneVisibleColorCount", 11),
          ("other", 1),
          ("threeColorantCount", 23),
          ("totalCount", 4),
          ("twoColorantCount", 22))
    )

    if mibBuilder.loadTexts:
        description = """\
 The recognized impression counting types for impressions produced by the jobs.
The following standard values are defined for the count-type. total count Count
all impressions. black and white count Count impressions requiring only black
colorant. highlight color count Count impressions requiring black plus one
other colorant. full color count Count impressions requiring 3 or more
colorants. one visible color count Count impressions for which one visible
color is printed. This is determined when a printer driver converts a document
to PDL formatted data. This is related in a specific accounting method rather
than consumed colorants. The differentiation between a 'one visible color'
impression from an impression of another type is device dependent, i.e., a
device might consider 'one visible', 'black and white', and 'highlight' to be
three different types. limited visible color count Count impressions for which
multiple visible colors are printed, but when the impression should not be
considered 'full color'. This is determined when a printer driver converts a
document to PDL formatted data. This is related in a specific accounting method
rather than consumed colorants. The choice of a number of colors that
differentiates a 'limited color' impression from a 'full color' (or other type
of) impression is device dependent. one colorant count Count impressions on
which any one colorant is used, whether black or any other color. two colorant
count Count impressions on which any two colorants are used, whether or not
black is used. three colorant count Count impressions on which any three
colorants are used, whether or not black is used. four colorant count Count
impressions on which any four colorants are used, whether or not black is used.
NOTE: Other count-type may be added in the future according to the requirements
of accounting services.
"""


class XcmJMMediumType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              100,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("coated", 101),
          ("continuousLong", 7),
          ("continuousShort", 8),
          ("coverStock", 16),
          ("drilled", 100),
          ("envelope", 5),
          ("envelopePlain", 6),
          ("envelopeWindow", 12),
          ("heavyWeight", 103),
          ("labels", 11),
          ("letterhead", 15),
          ("multiLayer", 13),
          ("multiPartForm", 10),
          ("other", 1),
          ("prePrinted", 14),
          ("recycled", 102),
          ("stationery", 3),
          ("tabStock", 9),
          ("transparency", 4),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The recognized types of media. NOTE: For this MIB, these values are enums,
instead of strings. This departure from the IETF Printer MIB where medium-types
are strings is so that the medium types can be more easily localized. Also the
xcmJMMediaConsumedGroup accounting group also has the media names as string
values so that accounting systems can use either the enum type or the medium
name. ISO DPA: Medium-type This attribute identifies the type of this medium.
(e.g. stationery, envelope, transparency, etc.) The following standard values
are defined: stationery Separately cut sheets of an opaque material (id-val-
medium- type-stationery)Sometimes called 'standard'. transparency Separately
cut sheets of a transparent material (id-val- medium-type-transparency)
envelope Envelopes that can be used for conventional mailing purposes (id-val-
medium-type-envelope) envelopePlain Envelopes that are not pre-printed and have
no windows (id- val-medium-type-envelope-plain) envelopeWindow Envelopes that
have windows for addressing purposes (id- val-medium-type-envelope-window)
continuousLong Continuously connected sheets of an opaque material connected
along the long edge (id-val-medium-type- continuous-long) continuousShort
Continuously connected sheets of an opaque material connected along the short
edge (id-val-medium-type- continuous-short) tabStock Media with tabs (id-val-
medium-type-tab) multiPartForm Form medium composed of multiple layers not pre-
attached to one another; each sheet may be drawn separately from an input
source (id-val-medium-multi-part-form) labels Label-stock (id-val-medium-
labels) multiLayer Form medium composed of multiple layers which are pre-
attached to one another, e.g. for use with impact printers (id-val-medium-type-
multi-layer). The following are additional types that are being proposed to ISO
DPA and so continue with the same enum and OID assignments: prePrinted pre-
printed medium, other than letterhead letterhead pre-printed letterhead
coverStock cover medium The following are additional types that are orthogonal
to media- type and so will not be proposed to ISO DPA as additional media-
type. Instead, these will be proposed as separate attributes of the medium
object. Therefore, they will be assigned as Xerox extension bits for use in the
Job Monitoring MIB: drilled Medium with holes. (Corresponds to the existing ISO
DPA medium-holes attribute) coated Medium with some coating. (Will be proposed
to ISO DPA as a separate medium object attribute, possibly Boolean). recycled
recycled medium. (Will be proposed to ISO DPA as a separate medium object
attribute, possibly Boolean). heavyWeight heavy-weight medium. (Corresponds to
the existing ISO DPA medium-weight attribute). This is a type 2 enum.
"""


# MIB Managed Objects in the order of their OIDs

_XcmJobServiceTypesOID_ObjectIdentity = ObjectIdentity
xcmJobServiceTypesOID = _XcmJobServiceTypesOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2)
)
if mibBuilder.loadTexts:
    xcmJobServiceTypesOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceTypesOID.setDescription("""\
The root of all job service type OIDs defined in the Job Monitoring MIB TC.
Also use these same OIDs for Xerox extensions to ISO DPA.
""")
_XcmJobServiceScanToFileOID_ObjectIdentity = ObjectIdentity
xcmJobServiceScanToFileOID = _XcmJobServiceScanToFileOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 1)
)
if mibBuilder.loadTexts:
    xcmJobServiceScanToFileOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceScanToFileOID.setDescription("""\
Scan-to-file The scan-to-file job service scans one or more documents and
stores the result in one or more (1) local files, (2) files in a distributed
file system or (3) files in a document repository, depending on the
prescriptive instructions submitted with the job service request.
""")
_XcmJobServiceScanToPrintOID_ObjectIdentity = ObjectIdentity
xcmJobServiceScanToPrintOID = _XcmJobServiceScanToPrintOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 2)
)
if mibBuilder.loadTexts:
    xcmJobServiceScanToPrintOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceScanToPrintOID.setReference("""\
See: 'xcmJobServiceCopyOID' below
""")
if mibBuilder.loadTexts:
    xcmJobServiceScanToPrintOID.setDescription("""\
Scan-to-print The scan-to-print job service scans one or more documents and
prints the results on a local printer or on a network printer, depending on the
prescriptive instructions submitted with the job service request.
""")
_XcmJobServiceScanToFaxOID_ObjectIdentity = ObjectIdentity
xcmJobServiceScanToFaxOID = _XcmJobServiceScanToFaxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 3)
)
if mibBuilder.loadTexts:
    xcmJobServiceScanToFaxOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceScanToFaxOID.setDescription("""\
Scan-to-fax The scan-to-fax job service scans one or more documents and faxes
the results using a local fax or on a network fax, depending on the
prescriptive instructions submitted with the job service request.
""")
_XcmJobServiceScanToMailListOID_ObjectIdentity = ObjectIdentity
xcmJobServiceScanToMailListOID = _XcmJobServiceScanToMailListOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 4)
)
if mibBuilder.loadTexts:
    xcmJobServiceScanToMailListOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceScanToMailListOID.setDescription("""\
Scan-to-mail-list The scan-to-mail-list job service scans one or more documents
and distributes the results using the distribution list specified by the
prescriptive instructions submitted with the job service request.
""")
_XcmJobServiceFaxToFileOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFaxToFileOID = _XcmJobServiceFaxToFileOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 5)
)
if mibBuilder.loadTexts:
    xcmJobServiceFaxToFileOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceFaxToFileOID.setDescription("""\
Fax-to-file The fax-to-file job service accepts one or more documents via
inbound fax and stores the result in one or more: (1) local files, (2) files in
a distributed file system or (3) files in a document repository, depending on
the prescriptive instructions submitted with the job service request.
""")
_XcmJobServiceFaxToPrintOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFaxToPrintOID = _XcmJobServiceFaxToPrintOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 6)
)
if mibBuilder.loadTexts:
    xcmJobServiceFaxToPrintOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceFaxToPrintOID.setDescription("""\
Fax-to-print The fax-to-print job service accepts one or more documents via
inbound fax and prints the results on a local printer or on a network printer,
depending on the prescriptive instructions submitted with the job service
request.
""")
_XcmJobServiceFaxToMailListOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFaxToMailListOID = _XcmJobServiceFaxToMailListOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 7)
)
if mibBuilder.loadTexts:
    xcmJobServiceFaxToMailListOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceFaxToMailListOID.setDescription("""\
Fax-to-mail-list The fax-to-mail-list job service accepts one or more documents
via inbound fax and distributes the results using the distribution list
specified by the prescriptive instructions submitted with the job service
request.
""")
_XcmJobServicePrintOID_ObjectIdentity = ObjectIdentity
xcmJobServicePrintOID = _XcmJobServicePrintOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 8)
)
if mibBuilder.loadTexts:
    xcmJobServicePrintOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServicePrintOID.setDescription("""\
Print The print job service accepts one or more documents submitted with the
job print service request, referenced from the job request in a distributed
file system or document repository and prints on a network printer, depending
on the prescriptive instructions submitted with the job service request.
""")
_XcmJobServiceFileToFaxOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFileToFaxOID = _XcmJobServiceFileToFaxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 9)
)
if mibBuilder.loadTexts:
    xcmJobServiceFileToFaxOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceFileToFaxOID.setDescription("""\
File-to-fax The file-to-fax job service accepts one or more documents submitted
with the job print service request, referenced from the job request in a
distributed file system or document repository and faxes the results using a
local fax or on a network fax, depending on the prescriptive instructions
submitted with the job service request.
""")
_XcmJobServiceFileToMailListOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFileToMailListOID = _XcmJobServiceFileToMailListOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 10)
)
if mibBuilder.loadTexts:
    xcmJobServiceFileToMailListOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceFileToMailListOID.setDescription("""\
File-to-mail-list The file-to-mail-list job service accepts one or more
documents submitted with the job service request, referenced from the job
request in a distributed file system or document repository and distributes the
results using the distribution list specified by the prescriptive instructions
submitted with the job service request. The file-to-mail-list service permits a
user to compose a compound job whose sub-job produces a file, such as a scan-
to-file, and whose subsequent sub-jobs use the file as input, such as a sub-job
to file-to-mail-list and a second (parallel) sub-job to print from the same
file.
""")
_XcmJobServiceCopyOID_ObjectIdentity = ObjectIdentity
xcmJobServiceCopyOID = _XcmJobServiceCopyOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 11)
)
if mibBuilder.loadTexts:
    xcmJobServiceCopyOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceCopyOID.setReference("""\
See: 'xcmJobServiceScanToPrintOID' above
""")
if mibBuilder.loadTexts:
    xcmJobServiceCopyOID.setDescription("""\
Copy The copy job service reads images (via xerography, scanner, etc.) and
writes (prints) those images (with a pipeline delay of zero or more images) on
a local marker sub-unit (copy service need NOT write a disk or other secondary
storage file of the copy images). Compare with 'xcmJobServiceScanToPrint'
(strictly used for digital scanners - scan to print service shall ALWAYS write
a disk or other secondary storage file of the whole document, i.e., the set of
copy images). The key distinction, from an Image Processing point of is that,
for a copy (or local copy) job the IIT (input - scan) and IOT (output - marker)
are WELL-TUNED with respect to each other to produce the best quality and the
best performance. Whereas for ScantoPrint the target IOT (or the its
capabilities) are not assumed to be known at the time scanning and in order to
achieve best quality, there is often an additional step of image processing
that the systems needs to go through (often called Image Interoperability
Services). Usage: A copy job service shall ALWAYS expose an 'xcmHrDeviceCopier'
(scanner and marker are invisible) in the IETF HR MIB, XCMI HRX MIB, and XCMI
Job Monitoring MIB. Usage: A scan to print job service shall ALWAYS expose an
'xcmHrDeviceScanner' and an 'hrDevicePrinter' (marker) in the IETF HR MIB, XCMI
HRX MIB, and XCMI Job Monitoring MIB.
""")
_XcmJobServiceFileToFileOID_ObjectIdentity = ObjectIdentity
xcmJobServiceFileToFileOID = _XcmJobServiceFileToFileOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 2, 12)
)
if mibBuilder.loadTexts:
    xcmJobServiceFileToFileOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmJobServiceFileToFileOID.setDescription("""\
File-to-file The file-to-file job service accepts one or more documents
submitted with the job print service request, referenced from the job request
in a distributed file system or document repository and stores the result in
one or more: (1) local files, (2) files in a distributed file system or (3)
files in a document repository, depending on the prescriptive instructions
submitted with the job service request. The initial intent of this job service
is support the transfer of a file to a device's hard drive. When the file
transfer is complete, the file-to-file job is complete. It is expected that a
user will eventually process the file from the device hard drive, but that
action starts a new job. This service might be used in the processing of a
secure-print action.
""")
_XCmJobMonTCDummy_ObjectIdentity = ObjectIdentity
xCmJobMonTCDummy = _XCmJobMonTCDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999)
)
_XCmJobMonTCJobServiceTypeOID_Type = XcmJMJobServiceTypeOID
_XCmJobMonTCJobServiceTypeOID_Object = MibScalar
xCmJobMonTCJobServiceTypeOID = _XCmJobMonTCJobServiceTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 1),
    _XCmJobMonTCJobServiceTypeOID_Type()
)
xCmJobMonTCJobServiceTypeOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobServiceTypeOID.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCJobServiceTypeOID.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCJobState_Type = XcmJMJobState
_XCmJobMonTCJobState_Object = MibScalar
xCmJobMonTCJobState = _XCmJobMonTCJobState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 2),
    _XCmJobMonTCJobState_Type()
)
xCmJobMonTCJobState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobState.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCJobState.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCJobStateReasons_Type = XcmJMJobStateReasons
_XCmJobMonTCJobStateReasons_Object = MibScalar
xCmJobMonTCJobStateReasons = _XCmJobMonTCJobStateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 3),
    _XCmJobMonTCJobStateReasons_Type()
)
xCmJobMonTCJobStateReasons.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobStateReasons.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCJobStateReasons.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCJobXStateReasons_Type = XcmJMJobXStateReasons
_XCmJobMonTCJobXStateReasons_Object = MibScalar
xCmJobMonTCJobXStateReasons = _XCmJobMonTCJobXStateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 4),
    _XCmJobMonTCJobXStateReasons_Type()
)
xCmJobMonTCJobXStateReasons.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobXStateReasons.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCJobXStateReasons.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCJobX2StateReasons_Type = XcmJMJobX2StateReasons
_XCmJobMonTCJobX2StateReasons_Object = MibScalar
xCmJobMonTCJobX2StateReasons = _XCmJobMonTCJobX2StateReasons_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 5),
    _XCmJobMonTCJobX2StateReasons_Type()
)
xCmJobMonTCJobX2StateReasons.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCJobX2StateReasons.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCJobX2StateReasons.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCDocType_Type = XcmJMDocType
_XCmJobMonTCDocType_Object = MibScalar
xCmJobMonTCDocType = _XCmJobMonTCDocType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 6),
    _XCmJobMonTCDocType_Type()
)
xCmJobMonTCDocType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCDocType.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCDocType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCDocFileNameType_Type = XcmJMDocFileNameType
_XCmJobMonTCDocFileNameType_Object = MibScalar
xCmJobMonTCDocFileNameType = _XCmJobMonTCDocFileNameType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 7),
    _XCmJobMonTCDocFileNameType_Type()
)
xCmJobMonTCDocFileNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCDocFileNameType.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCDocFileNameType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCDocState_Type = XcmJMDocState
_XCmJobMonTCDocState_Object = MibScalar
xCmJobMonTCDocState = _XCmJobMonTCDocState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 8),
    _XCmJobMonTCDocState_Type()
)
xCmJobMonTCDocState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCDocState.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCDocState.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCDocOutputMethod_Type = XcmJMDocOutputMethod
_XCmJobMonTCDocOutputMethod_Object = MibScalar
xCmJobMonTCDocOutputMethod = _XCmJobMonTCDocOutputMethod_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 9),
    _XCmJobMonTCDocOutputMethod_Type()
)
xCmJobMonTCDocOutputMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCDocOutputMethod.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCDocOutputMethod.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCGroupSupport_Type = XcmJMGroupSupport
_XCmJobMonTCGroupSupport_Object = MibScalar
xCmJobMonTCGroupSupport = _XCmJobMonTCGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 10),
    _XCmJobMonTCGroupSupport_Type()
)
xCmJobMonTCGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCGroupSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCImpsCountType_Type = XcmJMImpsCountType
_XCmJobMonTCImpsCountType_Object = MibScalar
xCmJobMonTCImpsCountType = _XCmJobMonTCImpsCountType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 11),
    _XCmJobMonTCImpsCountType_Type()
)
xCmJobMonTCImpsCountType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCImpsCountType.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCImpsCountType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmJobMonTCMediumType_Type = XcmJMMediumType
_XCmJobMonTCMediumType_Object = MibScalar
xCmJobMonTCMediumType = _XCmJobMonTCMediumType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 58, 999, 12),
    _XCmJobMonTCMediumType_Type()
)
xCmJobMonTCMediumType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmJobMonTCMediumType.setStatus("current")
if mibBuilder.loadTexts:
    xCmJobMonTCMediumType.setDescription("""\
Dummy - DO NOT USE
""")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-JOB-MONITORING-TC",
    **{"XcmJMJobServiceTypeOID": XcmJMJobServiceTypeOID,
       "XcmJMJobState": XcmJMJobState,
       "XcmJMJobStateReasons": XcmJMJobStateReasons,
       "XcmJMJobXStateReasons": XcmJMJobXStateReasons,
       "XcmJMJobX2StateReasons": XcmJMJobX2StateReasons,
       "XcmJMDocType": XcmJMDocType,
       "XcmJMDocFileNameType": XcmJMDocFileNameType,
       "XcmJMDocState": XcmJMDocState,
       "XcmJMDocOutputMethod": XcmJMDocOutputMethod,
       "XcmJMGroupSupport": XcmJMGroupSupport,
       "XcmJMImpsCountType": XcmJMImpsCountType,
       "XcmJMMediumType": XcmJMMediumType,
       "xcmJobMonTC": xcmJobMonTC,
       "xcmJobServiceTypesOID": xcmJobServiceTypesOID,
       "xcmJobServiceScanToFileOID": xcmJobServiceScanToFileOID,
       "xcmJobServiceScanToPrintOID": xcmJobServiceScanToPrintOID,
       "xcmJobServiceScanToFaxOID": xcmJobServiceScanToFaxOID,
       "xcmJobServiceScanToMailListOID": xcmJobServiceScanToMailListOID,
       "xcmJobServiceFaxToFileOID": xcmJobServiceFaxToFileOID,
       "xcmJobServiceFaxToPrintOID": xcmJobServiceFaxToPrintOID,
       "xcmJobServiceFaxToMailListOID": xcmJobServiceFaxToMailListOID,
       "xcmJobServicePrintOID": xcmJobServicePrintOID,
       "xcmJobServiceFileToFaxOID": xcmJobServiceFileToFaxOID,
       "xcmJobServiceFileToMailListOID": xcmJobServiceFileToMailListOID,
       "xcmJobServiceCopyOID": xcmJobServiceCopyOID,
       "xcmJobServiceFileToFileOID": xcmJobServiceFileToFileOID,
       "xCmJobMonTCDummy": xCmJobMonTCDummy,
       "xCmJobMonTCJobServiceTypeOID": xCmJobMonTCJobServiceTypeOID,
       "xCmJobMonTCJobState": xCmJobMonTCJobState,
       "xCmJobMonTCJobStateReasons": xCmJobMonTCJobStateReasons,
       "xCmJobMonTCJobXStateReasons": xCmJobMonTCJobXStateReasons,
       "xCmJobMonTCJobX2StateReasons": xCmJobMonTCJobX2StateReasons,
       "xCmJobMonTCDocType": xCmJobMonTCDocType,
       "xCmJobMonTCDocFileNameType": xCmJobMonTCDocFileNameType,
       "xCmJobMonTCDocState": xCmJobMonTCDocState,
       "xCmJobMonTCDocOutputMethod": xCmJobMonTCDocOutputMethod,
       "xCmJobMonTCGroupSupport": xCmJobMonTCGroupSupport,
       "xCmJobMonTCImpsCountType": xCmJobMonTCImpsCountType,
       "xCmJobMonTCMediumType": xCmJobMonTCMediumType}
)
