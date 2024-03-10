"""SNMP MIB module (XEROX-HOST-RESOURCES-EXT-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-HOST-RESOURCES-EXT-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:13 2024
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

(hrDeviceStatus,
 hrSWRunIndex,
 hrSWInstalledIndex,
 hrStorageIndex,
 hrDeviceIndex,
 ProductID) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceStatus",
    "hrSWRunIndex",
    "hrSWInstalledIndex",
    "hrStorageIndex",
    "hrDeviceIndex",
    "ProductID")

(PresentOnOff,) = mibBuilder.importSymbols(
    "Printer-MIB",
    "PresentOnOff")

(NotificationGroup,
 ModuleCompliance,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance",
    "ObjectGroup")

(Bits,
 TimeTicks,
 ObjectIdentity,
 NotificationType,
 Counter64,
 Unsigned32,
 MibIdentifier,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 IpAddress,
 ModuleIdentity,
 Integer32,
 Gauge32,
 Counter32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "TimeTicks",
    "ObjectIdentity",
    "NotificationType",
    "Counter64",
    "Unsigned32",
    "MibIdentifier",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "IpAddress",
    "ModuleIdentity",
    "Integer32",
    "Gauge32",
    "Counter32",
    "iso")

(DisplayString,
 TruthValue,
 AutonomousType,
 TextualConvention,
 DateAndTime,
 RowStatus) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TruthValue",
    "AutonomousType",
    "TextualConvention",
    "DateAndTime",
    "RowStatus")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmGenSNMPv2ErrorStatus,
 zeroDotZero,
 Ordinal32,
 Cardinal32,
 XcmFixedLocaleDisplayString,
 XcmGenNotifyTrainingFilter,
 XcmGenNotifySeverityFilter) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "XcmGenSNMPv2ErrorStatus",
    "zeroDotZero",
    "Ordinal32",
    "Cardinal32",
    "XcmFixedLocaleDisplayString",
    "XcmGenNotifyTrainingFilter",
    "XcmGenNotifySeverityFilter")

(XcmHrStorageDetailType,
 XcmHrSuppliesClassTC,
 XcmHrDevDetailType,
 XcmHrDevMgmtCommandRequest,
 XcmHrDevInfoConditions,
 XcmHrConsoleDefaultService,
 XcmHrDevInfoRealization,
 XcmHrGroupSupport,
 XcmHrDevInfoXStatus,
 XcmHrDevDetailUnitClass,
 XcmHrDevMgmtCommandData,
 XcmHrDevCalendarTimeOfDay,
 XcmHrDevCalendarDayOfWeek,
 XcmHrDevTrafficUnit,
 XcmHrDevInfoXConditions,
 XcmHrSWRunXStatus,
 XcmHrStorageRealization,
 XcmHrDevPowerTimeUnit,
 XcmHrDetailTableEnumTC,
 XcmHrDevInfoStatus) = mibBuilder.importSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    "XcmHrStorageDetailType",
    "XcmHrSuppliesClassTC",
    "XcmHrDevDetailType",
    "XcmHrDevMgmtCommandRequest",
    "XcmHrDevInfoConditions",
    "XcmHrConsoleDefaultService",
    "XcmHrDevInfoRealization",
    "XcmHrGroupSupport",
    "XcmHrDevInfoXStatus",
    "XcmHrDevDetailUnitClass",
    "XcmHrDevMgmtCommandData",
    "XcmHrDevCalendarTimeOfDay",
    "XcmHrDevCalendarDayOfWeek",
    "XcmHrDevTrafficUnit",
    "XcmHrDevInfoXConditions",
    "XcmHrSWRunXStatus",
    "XcmHrStorageRealization",
    "XcmHrDevPowerTimeUnit",
    "XcmHrDetailTableEnumTC",
    "XcmHrDevInfoStatus")


# MODULE-IDENTITY

xcmHrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53)
)
xcmHrMIB.setLastUpdated("0708080000Z")
if mibBuilder.loadTexts:
    xcmHrMIB.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmHrMIB.setContactInfo("""\
 XCMI Editors Email: coherence@crt.xerox.com -- --
""")
if mibBuilder.loadTexts:
    xcmHrMIB.setDescription("""\
Version: 5.602.pub The MIB module for extended configuration and management of
various host resources for network accessible host systems. This module
augments and extends the original IETF Host Resources MIB (RFC 2790). Usage:
This MIB module introduces support for the 'realization' of both 'physical' and
'logical' devices, consistent with the Document Printing Application (DPA),
ISO/IEC 10175, as reflected in the object 'xcmHrDevInfoRealization'. Note:
Conforming implementations SHALL NOT 'bubble up' status from 'physical' devices
to associated 'logical' devices. All devices SHALL report their own status
ONLY. See: Section 9 'Supplement' in XCMI Extensions to IETF Host Resources TC,
for implementation guidance for this MIB module. Copyright (C) 1995-2006 Xerox
Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmHrZeroDummy_ObjectIdentity = ObjectIdentity
xcmHrZeroDummy = _XcmHrZeroDummy_ObjectIdentity(
    (0, 0, 53)
)
_XcmHrMIBConformance_ObjectIdentity = ObjectIdentity
xcmHrMIBConformance = _XcmHrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2)
)
_XcmHrMIBGroups_ObjectIdentity = ObjectIdentity
xcmHrMIBGroups = _XcmHrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2)
)
_XcmHrDevInfo_ObjectIdentity = ObjectIdentity
xcmHrDevInfo = _XcmHrDevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3)
)
_XcmHrDevInfoV1EventOID_ObjectIdentity = ObjectIdentity
xcmHrDevInfoV1EventOID = _XcmHrDevInfoV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 1)
)
if mibBuilder.loadTexts:
    xcmHrDevInfoV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever a
device status variable changes. See SNMPv2 trap definition
'xcmHrDevInfoV2Event' below for 'special semantics'.
""")
_XcmHrDevInfoV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmHrDevInfoV2EventPrefix = _XcmHrDevInfoV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 1, 0)
)
_XcmHrDevInfoTable_Object = MibTable
xcmHrDevInfoTable = _XcmHrDevInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevInfoTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoTable.setDescription("""\
A 'sparse' table containing device info objects for installed and (possibly)
active devices on this host system, augmenting the basic entries in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790). Usage: Although this
group is Mandatory in this MIB module, this table is 'sparse' because
conforming management agents need NOT implement an entry in 'xcmHrDevInfoTable'
for ALL of the installed (and instrumented) devices in 'hrDeviceTable'. Usage:
Conforming management agents SHALL implement an entry in 'xcmHrDevInfoTable'
for the following device types (if they are installed devices in
'hrDeviceTable'): 'hrDevicePrinter' (from IETF Host Resource MIB, RFC 2790);
and 'xcmHrDeviceHostSystem', 'xcmHrDeviceScanner', 'xcmHrDeviceCopier',
'xcmHrDeviceFax', and 'xcmHrDeviceMailbox' (from XCMI HRX TC).
""")
_XcmHrDevInfoEntry_Object = MibTableRow
xcmHrDevInfoEntry = _XcmHrDevInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1)
)
xcmHrDevInfoEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevInfoEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoEntry.setDescription("""\
A 'sparse' entry containing device info objects for an installed and (possibly)
active device on this host system, augmenting a basic entry in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevInfoRowStatus_Type = RowStatus
_XcmHrDevInfoRowStatus_Object = MibTableColumn
xcmHrDevInfoRowStatus = _XcmHrDevInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 1),
    _XcmHrDevInfoRowStatus_Type()
)
xcmHrDevInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrDevInfoTable' and ALSO manages the row status of the associated
conceptual row in the 'hrDeviceTable' of the IETF Host Resources MIB (RFC
2790). Usage: Conforming implementations which support static rows SHALL
support 'active' and 'notInService' writes to this 'xcmHrDevInfoRowStatus' row
status object; and SHALL clear the 'xcmHrDevInfoGroup' bit in
'xcmHrGeneralCreateSupport' in the 'xcmHrGeneralTable'. Usage: Conforming
implementations which support dynamic rows SHALL support 'createAndGo' and
'destroy' writes to this 'xcmHrDevInfoRowStatus' row status object; and SHALL
set the 'xcmHrDevInfoGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrDevInfoName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevInfoName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevInfoName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevInfoName_Object = MibTableColumn
xcmHrDevInfoName = _XcmHrDevInfoName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 2),
    _XcmHrDevInfoName_Type()
)
xcmHrDevInfoName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoName.setReference("""\
See: 'hrDeviceDescr' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoName.setDescription("""\
Human-readable device name, used by system administrators and end users to
identify this device for systems management. Usage: This device name SHALL be
the one normally used in a CLI/GUI/API for control of this system or device
(eg, 'showstopper.sample.com' or 'showstopper.sample.com/lpt1:') Usage:
Conforming management agents, which ALSO implement the the Printer MIB v2,
SHALL set 'xcmHrDevInfoName' to the SAME value as 'prtGeneralPrinterName' for
the SAME 'hrDevicePrinter' row (i.e., the values of these two objects SHALL be
interlocked).
""")


class _XcmHrDevInfoSerialNumber_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevInfoSerialNumber based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevInfoSerialNumber_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevInfoSerialNumber_Object = MibTableColumn
xcmHrDevInfoSerialNumber = _XcmHrDevInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 3),
    _XcmHrDevInfoSerialNumber_Type()
)
xcmHrDevInfoSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoSerialNumber.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoSerialNumber.setReference("""\
See: 'hrDeviceDescr' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoSerialNumber.setDescription("""\
Human-readable serial number, used by system administrators and end users to
identify this device for systems management. Usage: Conforming management
agents, which ALSO implement the the Printer MIB v2, SHALL set
'xcmHrDevInfoSerialNumber' to the SAME value as 'prtGeneralSerialNumber' for
the SAME 'hrDevicePrinter' row (i.e., the values of these two objects SHALL be
interlocked).
""")


class _XcmHrDevInfoRealization_Type(XcmHrDevInfoRealization):
    """Custom type xcmHrDevInfoRealization based on XcmHrDevInfoRealization"""


_XcmHrDevInfoRealization_Object = MibTableColumn
xcmHrDevInfoRealization = _XcmHrDevInfoRealization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 4),
    _XcmHrDevInfoRealization_Type()
)
xcmHrDevInfoRealization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoRealization.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoRealization.setReference("""\
See: 'hrDeviceType' in the Device group of the IETF Host Resources MIB (RFC
2790). See: Section 9.4 (pages 181 to 184) of DPA (Document Printing
Application) ISO/IEC 10175 (Final Text, March 1996) for a discussion of
'printer realizations' of 'physical', 'logical', and 'logical-and-physical'
types (the latter peculiar to DPA).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoRealization.setDescription("""\
An extended device type (or device 'realization'), used by system
administrators and end users of this device.
""")
_XcmHrDevInfoXStatus_Type = XcmHrDevInfoXStatus
_XcmHrDevInfoXStatus_Object = MibTableColumn
xcmHrDevInfoXStatus = _XcmHrDevInfoXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 5),
    _XcmHrDevInfoXStatus_Type()
)
xcmHrDevInfoXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevInfoXStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoXStatus.setReference("""\
See: Section 9.4.9 'Printer-state' (page 185) of DPA (Document Printing
Application) ISO/IEC 10175 (Final Text, March 1996) for a discussion of the
printer states used here. Note that the DPA state 'connecting-to-printer' has
no meaning in the context of a 'physical' printer device, but only in the
context of an intermediate DP-Server presenting a 'logical' printer device.
See: 'hrPrinterStatus' and 'hrPrinterDetectedErrorState' in IETF Host Resources
MIB (RFC 2790). See: 'hrDeviceStatus' in the Device group of the IETF Host
Resources MIB (RFC 2790). See: 'xcmHrDevInfoConditions' and
'xcmHrDevInfoXConditions' in the Host Resources Extensions MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoXStatus.setDescription("""\
An extended device status, used by system administrators and end users of this
device (here, read 'state' for 'status'). Usage: Conforming implementations
SHALL NOT 'bubble up' status from 'physical' devices to associated 'logical'
devices. All devices SHALL report their own status ONLY. Usage: Exactly one
enumeration of extended device status SHALL be defined, with ranges for each
basic device type (eg, 'hrDevicePrinter'). The legal range for extended device
status for a given device type (either defined by RFC 2790 or by this MIB) is
found by multiplying the final arc of the the device type OID by 100 - the
result is the device specific range base - the end of the device specific range
is 99 larger. These device specific extended device status values SHALL be
reissued periodically in the 'XcmHrDevInfoXStatus' textual convention.
""")
_XcmHrDevInfoConditions_Type = XcmHrDevInfoConditions
_XcmHrDevInfoConditions_Object = MibTableColumn
xcmHrDevInfoConditions = _XcmHrDevInfoConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 6),
    _XcmHrDevInfoConditions_Type()
)
xcmHrDevInfoConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevInfoConditions.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoConditions.setReference("""\
See: 'hrDeviceStatus' in the Device group of the IETF Host Resources MIB (RFC
2790). See: 'xcmHrDevInfoXStatus' and 'xcmHrDevInfoXConditions' in the Host
Resources Extensions MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoConditions.setDescription("""\
A relatively generic description of the current 'conditions' of this device,
specified in a bit-mask. Usage: It is desirable that the implementor report
'conditions' of all devices corresponding to conceptual rows in the
'hrDeviceTable' as accurately as feasible. 'Conditions' occur within or across
'states' in a finite state machine (FSM) implementation of a device. They
represent both short term and long term conditions.
""")
_XcmHrDevInfoXConditions_Type = XcmHrDevInfoXConditions
_XcmHrDevInfoXConditions_Object = MibTableColumn
xcmHrDevInfoXConditions = _XcmHrDevInfoXConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 7),
    _XcmHrDevInfoXConditions_Type()
)
xcmHrDevInfoXConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevInfoXConditions.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoXConditions.setReference("""\
See: 'hrDeviceStatus' in the Device group of the IETF Host Resources MIB (RFC
2790). See: 'xcmHrDevInfoXStatus' and 'xcmHrDevInfoConditions' in the Host
Resources Extensions MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoXConditions.setDescription("""\
A device specific description of the extended 'conditions' of this device,
specified in a bit-mask. Usage: For FUTURE expansion. Usage: Exactly one bit
mask of extended device conditions SHALL be defined for each basic device type
(eg, 'hrDevicePrinter'). These device specific extended device conditions
values SHALL be reissued periodically in the 'XcmHrDevInfoXConditions' textual
convention. These device specific extended device conditions are mutually
exclusive and 'overloaded' in the single reporting object
'xcmHrDevInfoXConditions'.
""")


class _XcmHrDevInfoInstallDate_Type(DateAndTime):
    """Custom type xcmHrDevInfoInstallDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrDevInfoInstallDate_Object = MibTableColumn
xcmHrDevInfoInstallDate = _XcmHrDevInfoInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 8),
    _XcmHrDevInfoInstallDate_Type()
)
xcmHrDevInfoInstallDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoInstallDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoInstallDate.setReference("""\
See: 'hrDeviceDescr' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoInstallDate.setDescription("""\
The date of the most recent install or upgrade of the device represented by
this conceptual row in the 'hrDeviceTable'.
""")


class _XcmHrDevInfoResetDate_Type(DateAndTime):
    """Custom type xcmHrDevInfoResetDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrDevInfoResetDate_Object = MibTableColumn
xcmHrDevInfoResetDate = _XcmHrDevInfoResetDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 9),
    _XcmHrDevInfoResetDate_Type()
)
xcmHrDevInfoResetDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevInfoResetDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoResetDate.setReference("""\
See: 'hrDeviceDescr' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoResetDate.setDescription("""\
The date of the most recent auto or managed reset of the device represented by
this conceptual row in the 'hrDeviceTable'.
""")
_XcmHrDevInfoNextDeviceIndex_Type = Cardinal32
_XcmHrDevInfoNextDeviceIndex_Object = MibTableColumn
xcmHrDevInfoNextDeviceIndex = _XcmHrDevInfoNextDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 10),
    _XcmHrDevInfoNextDeviceIndex_Type()
)
xcmHrDevInfoNextDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoNextDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoNextDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoNextDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to: a) the next associated row in
the 'hrDeviceTable'; or b) zero if this is the last associated conceptual row
in a given set; or c) zero if this conceptual row is NOT part of a set.
""")
_XcmHrDevInfoPreviousDeviceIndex_Type = Cardinal32
_XcmHrDevInfoPreviousDeviceIndex_Object = MibTableColumn
xcmHrDevInfoPreviousDeviceIndex = _XcmHrDevInfoPreviousDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 11),
    _XcmHrDevInfoPreviousDeviceIndex_Type()
)
xcmHrDevInfoPreviousDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPreviousDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoPreviousDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoPreviousDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to: a) the previous associated row
in the 'hrDeviceTable'; or b) zero if this is the first associated conceptual
row in a given set; or c) zero if this conceptual row is NOT part of a set.
""")
_XcmHrDevInfoPhysicalDeviceIndex_Type = Cardinal32
_XcmHrDevInfoPhysicalDeviceIndex_Object = MibTableColumn
xcmHrDevInfoPhysicalDeviceIndex = _XcmHrDevInfoPhysicalDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 12),
    _XcmHrDevInfoPhysicalDeviceIndex_Type()
)
xcmHrDevInfoPhysicalDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPhysicalDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoPhysicalDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoPhysicalDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the directly associated
conceptual row in the 'hrDeviceTable' representing: a) the first underlying
'physical' device (if any), if this row has 'xcmHrDevInfoRealization' of
'logical'; or b) the first subordinate 'physical' device (if any), if this row
has 'xcmHrDevInfoRealization' of 'physical' or 'logicalAndPhysical'; or c) zero
if there is no underlying or subordinate 'physical' device associated with this
row (ie, this device).
""")


class _XcmHrDevInfoPriority_Type(Integer32):
    """Custom type xcmHrDevInfoPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmHrDevInfoPriority_Type.__name__ = "Integer32"
_XcmHrDevInfoPriority_Object = MibTableColumn
xcmHrDevInfoPriority = _XcmHrDevInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 13),
    _XcmHrDevInfoPriority_Type()
)
xcmHrDevInfoPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPriority.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoPriority.setReference("""\
See: 'xcmSvcMonServicePriority' in XCMI Service Monitoring MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoPriority.setDescription("""\
The current priority of this device. Usage: The scheduling priority of this
device, where '0' is unspecified (default), '1' is lowest, and '100' is
highest.
""")


class _XcmHrDevInfoXeroxAssetTagNumber_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevInfoXeroxAssetTagNumber based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XcmHrDevInfoXeroxAssetTagNumber_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevInfoXeroxAssetTagNumber_Object = MibTableColumn
xcmHrDevInfoXeroxAssetTagNumber = _XcmHrDevInfoXeroxAssetTagNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 14),
    _XcmHrDevInfoXeroxAssetTagNumber_Type()
)
xcmHrDevInfoXeroxAssetTagNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoXeroxAssetTagNumber.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoXeroxAssetTagNumber.setReference("""\
See: 'hrDeviceDescr' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoXeroxAssetTagNumber.setDescription("""\
Human-readable, alpha-numeric ID used by Xerox and Xerox managed service
providers to uniquely identify a device ACROSS back-end financial, printer
management, asset management, and help desk system applications. The Asset Tag
Number is an infra- structure management de facto standard for asset
identification for use by Xerox and Xerox managed service providers. Usage:
Conforming management agents SHALL set 'xcmHrDevInfoXeroxAssetTagNumber' to the
SAME value as entered at a device's local UI, at a device's web UI interface,
and as shown on the device's configuration sheet.
""")


class _XcmHrDevInfoCustomerAssetNumber_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevInfoCustomerAssetNumber based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XcmHrDevInfoCustomerAssetNumber_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevInfoCustomerAssetNumber_Object = MibTableColumn
xcmHrDevInfoCustomerAssetNumber = _XcmHrDevInfoCustomerAssetNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 15),
    _XcmHrDevInfoCustomerAssetNumber_Type()
)
xcmHrDevInfoCustomerAssetNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoCustomerAssetNumber.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoCustomerAssetNumber.setReference("""\
See: 'hrDeviceDescr' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoCustomerAssetNumber.setDescription("""\
Human-readable, alpha-numeric ID used by customers of Xerox. This ID is used
system administrators and their designated managed service providers to
uniquely identify a device for customers' internal financial management,
printer management, asset management, and help desk system applications. Usage:
Conforming management agents SHALL set 'xcmHrDevInfoCustomerAssetNumber' to the
SAME value as entered at a device's local UI, at a device's web UI interface,
and as shown on the device's configuration sheet.
""")


class _XcmHrDevInfoPagePackPIN_Type(OctetString):
    """Custom type xcmHrDevInfoPagePackPIN based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XcmHrDevInfoPagePackPIN_Type.__name__ = "OctetString"
_XcmHrDevInfoPagePackPIN_Object = MibTableColumn
xcmHrDevInfoPagePackPIN = _XcmHrDevInfoPagePackPIN_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 16),
    _XcmHrDevInfoPagePackPIN_Type()
)
xcmHrDevInfoPagePackPIN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackPIN.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackPIN.setReference("""\
See: 'XcmSvcMonServiceType' in 'Service Monitoring TC'.
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackPIN.setDescription("""\
An alpha-numeric ID used by Xerox and Xerox authorized resellers to enable
devices to use a PagePack model of device distribution. PagePack is a cost per
page contract model - which includes consumables, supplies and service - on
both printer and multifunction systems The PIN number is used to change a
device from purchased consumables device to a PagePack device. Usage: The
device may return a NULL string or the word 'authorized' if the PIN value has
been sent and the device does not want to expose the value to the PIN to
unauthorized viewing. If no PIN has been sent or this functionality is not
supported then a NULL string is returned
""")


class _XcmHrDevInfoPagePackReset_Type(Integer32):
    """Custom type xcmHrDevInfoPagePackReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XcmHrDevInfoPagePackReset_Type.__name__ = "Integer32"
_XcmHrDevInfoPagePackReset_Object = MibTableColumn
xcmHrDevInfoPagePackReset = _XcmHrDevInfoPagePackReset_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 17),
    _XcmHrDevInfoPagePackReset_Type()
)
xcmHrDevInfoPagePackReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackReset.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackReset.setReference("""\
See: 'xcmHrDevInfoPagePackPIN' in this mib.
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackReset.setDescription("""\
An enumeration used to get and set the page pack settings. Usage: The device
will return enabled when page pack has been enabled and return disabled when
page pack has been disabled. enabled (1) disabled (2)
""")


class _XcmHrDevInfoPagePackTimer_Type(Integer32):
    """Custom type xcmHrDevInfoPagePackTimer based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_XcmHrDevInfoPagePackTimer_Type.__name__ = "Integer32"
_XcmHrDevInfoPagePackTimer_Object = MibTableColumn
xcmHrDevInfoPagePackTimer = _XcmHrDevInfoPagePackTimer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 2, 1, 18),
    _XcmHrDevInfoPagePackTimer_Type()
)
xcmHrDevInfoPagePackTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackTimer.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackTimer.setReference("""\
See: 'xcmHrDevInfoPagePackPIN' in this mib.
""")
if mibBuilder.loadTexts:
    xcmHrDevInfoPagePackTimer.setDescription("""\
An timer value for page pack. Usage: The value (-1) means timer not enabled and
a value 0..2147483647 means the timer has been enabled
""")
_XcmHrDevHelp_ObjectIdentity = ObjectIdentity
xcmHrDevHelp = _XcmHrDevHelp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4)
)
_XcmHrDevHelpTable_Object = MibTable
xcmHrDevHelpTable = _XcmHrDevHelpTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevHelpTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevHelpTable.setReference("""\
See: 'hrProcessorTable', 'hrNetworkTable', 'hrPrinterTable' in the IETF Host
Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevHelpTable.setDescription("""\
A 'sparse' table containing device help objects for installed and (possibly)
active devices on this host system, augmenting the basic entries in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevHelpEntry_Object = MibTableRow
xcmHrDevHelpEntry = _XcmHrDevHelpEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1)
)
xcmHrDevHelpEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevHelpEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevHelpEntry.setDescription("""\
A 'sparse' entry containing device help objects for an installed and (possibly)
active device on this host system, augmenting a basic entry in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevHelpRowStatus_Type = RowStatus
_XcmHrDevHelpRowStatus_Object = MibTableColumn
xcmHrDevHelpRowStatus = _XcmHrDevHelpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1, 1),
    _XcmHrDevHelpRowStatus_Type()
)
xcmHrDevHelpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevHelpRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevHelpRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevHelpRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrDevHelpTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmHrDevHelpRowStatus' row status object; and SHALL clear the
'xcmHrDevHelpGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrDevHelpRowStatus' row status object; and SHALL set the
'xcmHrDevHelpGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrDevHelpOperatorMessage_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevHelpOperatorMessage based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevHelpOperatorMessage_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevHelpOperatorMessage_Object = MibTableColumn
xcmHrDevHelpOperatorMessage = _XcmHrDevHelpOperatorMessage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1, 2),
    _XcmHrDevHelpOperatorMessage_Type()
)
xcmHrDevHelpOperatorMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevHelpOperatorMessage.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevHelpOperatorMessage.setReference("""\
See: 'hrDeviceDescr' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevHelpOperatorMessage.setDescription("""\
Human-readable operator message, used by system operators and system
administrators to display an operator message for end users of this device. For
example, 'Out to lunch - back at 1pm'.
""")


class _XcmHrDevHelpProblemMessage_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevHelpProblemMessage based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevHelpProblemMessage_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevHelpProblemMessage_Object = MibTableColumn
xcmHrDevHelpProblemMessage = _XcmHrDevHelpProblemMessage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1, 3),
    _XcmHrDevHelpProblemMessage_Type()
)
xcmHrDevHelpProblemMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevHelpProblemMessage.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevHelpProblemMessage.setReference("""\
See: 'hrDeviceDescr' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevHelpProblemMessage.setDescription("""\
Human-readable problem message, used by system operators and system
administrators to display a problem message for end users of this device. For
example, 'Toner low - only small jobs accepted'.
""")
_XcmHrDevHelpCommsAddressIndex_Type = Cardinal32
_XcmHrDevHelpCommsAddressIndex_Object = MibTableColumn
xcmHrDevHelpCommsAddressIndex = _XcmHrDevHelpCommsAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 4, 2, 1, 4),
    _XcmHrDevHelpCommsAddressIndex_Type()
)
xcmHrDevHelpCommsAddressIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevHelpCommsAddressIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevHelpCommsAddressIndex.setReference("""\
See: Comms Address group of the XCMI Comms Engine MIB, for details of
specification of device help contact info. See: 'XcmSecUserRole' in XCMI
Security TC, for appropriate values for 'xcmCommsAddressUserRole'. See:
'sysContact' in the IETF MIB-II (RFC 1213), for details of specification of
'simple' host system contact info.
""")
if mibBuilder.loadTexts:
    xcmHrDevHelpCommsAddressIndex.setDescription("""\
The value of 'xcmCommsAddressIndex' corresponding to the first associated
conceptual row in the 'xcmCommsAddressTable', or zero if this
'xcmHrDevHelpEntry' does NOT require such information. This 'chain' of address
entries provides device help contact info for end users of this device. For
example, 'system operator' or 'supplies' contact info.
""")
_XcmHrDevMgmt_ObjectIdentity = ObjectIdentity
xcmHrDevMgmt = _XcmHrDevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5)
)
_XcmHrDevMgmtV1EventOID_ObjectIdentity = ObjectIdentity
xcmHrDevMgmtV1EventOID = _XcmHrDevMgmtV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 1)
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever an
'xcmHrDevMgmtCommandRequest' completes. See SNMPv2 trap definition
'xcmHrDevMgmtV2Event' below for 'special semantics'.
""")
_XcmHrDevMgmtV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmHrDevMgmtV2EventPrefix = _XcmHrDevMgmtV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 1, 0)
)
_XcmHrDevMgmtTable_Object = MibTable
xcmHrDevMgmtTable = _XcmHrDevMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtTable.setReference("""\
See: 'hrProcessorTable', 'hrNetworkTable', 'hrPrinterTable' in the IETF Host
Resources MIB (RFC 2790). See: 'xcmSysAdminRequestTable' in XCMI System Admin
MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtTable.setDescription("""\
A 'sparse' table containing management control objects for installed and
(possibly) active devices on this host system, augmenting the basic entries in
the 'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevMgmtEntry_Object = MibTableRow
xcmHrDevMgmtEntry = _XcmHrDevMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1)
)
xcmHrDevMgmtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtEntry.setDescription("""\
A 'sparse' entry containing management control objects for an installed and
(possibly) active device on this host system, augmenting a basic entry in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevMgmtRowStatus_Type = RowStatus
_XcmHrDevMgmtRowStatus_Object = MibTableColumn
xcmHrDevMgmtRowStatus = _XcmHrDevMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 1),
    _XcmHrDevMgmtRowStatus_Type()
)
xcmHrDevMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrDevMgmtTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmHrDevMgmtRowStatus' row status object; and SHALL clear the
'xcmHrDevMgmtGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrDevMgmtRowStatus' row status object; and SHALL set the
'xcmHrDevMgmtGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrDevMgmtCommandRequest_Type(XcmHrDevMgmtCommandRequest):
    """Custom type xcmHrDevMgmtCommandRequest based on XcmHrDevMgmtCommandRequest"""


_XcmHrDevMgmtCommandRequest_Object = MibTableColumn
xcmHrDevMgmtCommandRequest = _XcmHrDevMgmtCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 2),
    _XcmHrDevMgmtCommandRequest_Type()
)
xcmHrDevMgmtCommandRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandRequest.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandRequest.setReference("""\
See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE
1387.4 / Draft 8, October 1994). See: 'hrDeviceStatus' in the Device group of
the IETF Host Resources MIB (RFC 2790). See: OBJECT clause in MODULE-COMPLIANCE
macro of XCMI Ext to Host Resources MIB, for compliance info. See:
'XcmHrDevMgmtCommandDataTag' textual convention, Section 3.4 'XCMI Standard
Tagged Management Data', and Section 3.5 'Simple Device Management Requests' in
XCMI Ext to Host Resources TC. See: Section 3.5.3 'Secure Simple Device Mgmt
Requests' in XCMI Security TC. See:
'xcmHrDevMgmtCommand[Data|Status|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandRequest.setDescription("""\
The most recent device management command request specified for this conceptual
row in the 'xcmHrDevMgmtTable'. Usage: Conforming management agents SHALL
'reject' any SNMP Set-Request to 'xcmHrDevMgmtCommand[Request|Data]' while
another management operation is already in progress (ie, while
'xcmHrDevMgmtCommandInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: Conforming management stations SHALL
set 'xcmHrDevMgmtCommandRequest' (mgmt operation) and 'xcmHrDevMgmtCommandData'
(mgmt arguments) SIMULTANEOUSLY (in the same SNMP Set-Request PDU).
""")


class _XcmHrDevMgmtCommandData_Type(XcmHrDevMgmtCommandData):
    """Custom type xcmHrDevMgmtCommandData based on XcmHrDevMgmtCommandData"""
    defaultHexValue = ""

    subtypeSpec = XcmHrDevMgmtCommandData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtCommandData_Type.__name__ = "XcmHrDevMgmtCommandData"
_XcmHrDevMgmtCommandData_Object = MibTableColumn
xcmHrDevMgmtCommandData = _XcmHrDevMgmtCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 3),
    _XcmHrDevMgmtCommandData_Type()
)
xcmHrDevMgmtCommandData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandData.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandData.setReference("""\
See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE
1387.4 / Draft 8, October 1994). See: 'hrDeviceStatus' in the Device group of
the IETF Host Resources MIB (RFC 2790). See: 'XcmHrDevMgmtCommandDataTag'
textual convention, Section 3.4 'XCMI Standard Tagged Management Data', and
Section 3.5 'Simple Device Management Requests' in XCMI Ext to Host Resources
TC. See: Section 3.5.3 'Secure Simple Device Mgmt Requests' in XCMI Security
TC. See: 'xcmHrDevMgmtCommand[Request|Status|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandData.setDescription("""\
The most recent device management command data (if any) specified for this
conceptual row in the 'xcmHrDevMgmtTable'. Usage: Conforming management agents
SHALL 'reject' any SNMP Set-Request to 'xcmHrDevMgmtCommand[Request|Data]'
while another management operation is already in progress (ie, while
'xcmHrDevMgmtCommandInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: Conforming management stations SHALL
set 'xcmHrDevMgmtCommandRequest' (mgmt operation) and 'xcmHrDevMgmtCommandData'
(mgmt arguments) SIMULTANEOUSLY (in the same SNMP Set-Request PDU). Usage:
Conformant implementations MUST encrypt passwords, keys, and other security
information stored in this string object.
""")
_XcmHrDevMgmtCommandStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmHrDevMgmtCommandStatus_Object = MibTableColumn
xcmHrDevMgmtCommandStatus = _XcmHrDevMgmtCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 4),
    _XcmHrDevMgmtCommandStatus_Type()
)
xcmHrDevMgmtCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandStatus.setReference("""\
See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE
1387.4 / Draft 8, October 1994). See: 'hrDeviceStatus' in the Device group of
the IETF Host Resources MIB (RFC 2790). See: 'XcmHrDevMgmtCommandDataTag'
textual convention, Section 3.4 'XCMI Standard Tagged Management Data', and
Section 3.5 'Simple Device Management Requests' in XCMI Ext to Host Resources
TC. See: Section 3.5.3 'Secure Simple Device Mgmt Requests' in XCMI Security
TC. See: 'xcmHrDevMgmtCommand[Operation|Data|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandStatus.setDescription("""\
The simple device management error status associated with this conceptual row
in 'xcmHrDevMgmtTable'. Usage: Conforming management agents SHALL set this
object to the value returned in an SNMP Set-Response PDU when a simple device
management operation is 'accepted', ie, when 'xcmHrDevMgmtCommandInProgress'
goes from 'false' to 'true'. Usage: Conforming management agents SHALL set this
object to the value of the completion status of the (possibly deferred) simple
device management operation, when 'xcmHrDevMgmtCommandInProgress' goes from
'true' to 'false'.
""")


class _XcmHrDevMgmtUserPassword_Type(OctetString):
    """Custom type xcmHrDevMgmtUserPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtUserPassword_Type.__name__ = "OctetString"
_XcmHrDevMgmtUserPassword_Object = MibTableColumn
xcmHrDevMgmtUserPassword = _XcmHrDevMgmtUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 5),
    _XcmHrDevMgmtUserPassword_Type()
)
xcmHrDevMgmtUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtUserPassword.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtUserPassword.setReference("""\
See: 'xcmHrDevMgmt[Operator|Admin]Password' See: Section 3.5.2 'Secure Password
Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable' in XCMI
System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB. See: Both the
X/Open PSIS (Printing Systems Interoperability Specification) and the new Part
3 'Systems Management' of DPA (ISO/IEC 10175) use the simple three-role scheme
specified here. In Appendix D 'Roles of Users' (pages 108 to 109) of Printer
MIB v1 (RFC 1759), Jay Martin provided an excellent discussion of a number of
user 'role models', including the following ones: User (USER) - A person or
application that submits print jobs to the printer; typically viewed as the
'end user' within the overall printing environment. Operator (OP) - A person
responsible for maintaining a printer on a day-to-day basis, including such
tasks as filling empty media trays, emptying full output trays, replacing toner
cartridges, etc. System Manager (MGR) - A person responsible for configuration
and troubleshooting of components involved in the overall printing environment,
including printers, print queues and network connectivity issues. This person
is typically responsible for ensuring the overall operational integrity of the
print system components, and is typically viewed as the central point of
coordination among all other Role Models.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtUserPassword.setDescription("""\
A protected end user password for this device. Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information
stored in this string object. Usage: All XCMI conforming management agents: a)
SHOULD always return a zero length string in response to an SNMP GetRequest of
this object; b) SHALL NOT return the contents of this object in cleartext (ie,
unencrypted) in response to an SNMP GetRequest; c) SHOULD support (ie, accept)
an authenticated SNMP SetRequest changing the system 'end user password' in
this object. Usage: Conforming management stations and management agents SHOULD
support authentication of SNMP SetRequests via values of
'xcmHrDevMgmt[User|Operator|Admin]Password' in ciphertext (ie, encrypted)
written in 'xcmHrDevMgmtCommandData'. Usage: Conforming management stations MAY
support client-side authentication of user roles and rights via checking values
of 'xcmHrDevMgmt[User|Operator|Admin]Password' presented in client applications
(eg, install tools). WARNING: Such authentication mechanisms do NOT protect
managed systems from attack by other SNMP client applications that do NOT
perform such client-side authentication and are thus inherently weak.
""")


class _XcmHrDevMgmtOperatorPassword_Type(OctetString):
    """Custom type xcmHrDevMgmtOperatorPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtOperatorPassword_Type.__name__ = "OctetString"
_XcmHrDevMgmtOperatorPassword_Object = MibTableColumn
xcmHrDevMgmtOperatorPassword = _XcmHrDevMgmtOperatorPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 6),
    _XcmHrDevMgmtOperatorPassword_Type()
)
xcmHrDevMgmtOperatorPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtOperatorPassword.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtOperatorPassword.setReference("""\
See: 'xcmHrDevMgmt[User|Admin]Password' See: Section 3.5.2 'Secure Password
Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable' in XCMI
System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtOperatorPassword.setDescription("""\
A protected system operator password for this device. Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information
stored in this string object. Usage: All XCMI conforming management agents: a)
SHOULD always return a zero length string in response to an SNMP GetRequest of
this object; b) SHALL NOT return the contents of this object in cleartext (ie,
unencrypted) in response to an SNMP GetRequest; c) SHOULD support (ie, accept)
an authenticated SNMP SetRequest changing the system 'operator password' in
this object. Usage: Conforming management stations and management agents SHOULD
support authentication of SNMP SetRequests via values of
'xcmHrDevMgmt[User|Operator|Admin]Password' in ciphertext (ie, encrypted)
written in 'xcmHrDevMgmtCommandData'. Usage: Conforming management stations MAY
support client-side authentication of user roles and rights via checking values
of 'xcmHrDevMgmt[User|Operator|Admin]Password' presented in client applications
(eg, install tools). WARNING: Such authentication mechanisms do NOT protect
managed systems from attack by other SNMP client applications that do NOT
perform such client-side authentication and are thus inherently weak.
""")


class _XcmHrDevMgmtAdminPassword_Type(OctetString):
    """Custom type xcmHrDevMgmtAdminPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtAdminPassword_Type.__name__ = "OctetString"
_XcmHrDevMgmtAdminPassword_Object = MibTableColumn
xcmHrDevMgmtAdminPassword = _XcmHrDevMgmtAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 7),
    _XcmHrDevMgmtAdminPassword_Type()
)
xcmHrDevMgmtAdminPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtAdminPassword.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtAdminPassword.setReference("""\
See: 'xcmHrDevMgmt[User|Operator]Password' See: Section 3.5.2 'Secure Password
Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable' in XCMI
System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtAdminPassword.setDescription("""\
A protected system administrator password for this device. Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information
stored in this string object. Usage: All XCMI conforming management agents: a)
SHOULD always return a zero length string in response to an SNMP GetRequest of
this object; b) SHALL NOT return the contents of this object in cleartext (ie,
unencrypted) in response to an SNMP GetRequest; c) SHOULD support (ie, accept)
an authenticated SNMP SetRequest changing the system 'administrator password'
in this object. Usage: Conforming management stations and management agents
SHOULD support authentication of SNMP SetRequests via values of
'xcmHrDevMgmt[User|Operator|Admin]Password' in ciphertext (ie, encrypted)
written in 'xcmHrDevMgmtCommandData'. Usage: Conforming management stations MAY
support client-side authentication of user roles and rights via checking values
of 'xcmHrDevMgmt[User|Operator|Admin]Password' presented in client applications
(eg, install tools). WARNING: Such authentication mechanisms do NOT protect
managed systems from attack by other SNMP client applications that do NOT
perform such client-side authentication and are thus inherently weak.
""")


class _XcmHrDevMgmtCommandInProgress_Type(TruthValue):
    """Custom type xcmHrDevMgmtCommandInProgress based on TruthValue"""


_XcmHrDevMgmtCommandInProgress_Object = MibTableColumn
xcmHrDevMgmtCommandInProgress = _XcmHrDevMgmtCommandInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 8),
    _XcmHrDevMgmtCommandInProgress_Type()
)
xcmHrDevMgmtCommandInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandInProgress.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandInProgress.setReference("""\
See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE
1387.4 / Draft 8, October 1994). See: 'hrDeviceStatus' in the Device group of
the IETF Host Resources MIB (RFC 2790). See: 'XcmHrDevMgmtCommandDataTag'
textual convention, Section 3.4 'XCMI Standard Tagged Management Data', and
Section 3.5 'Simple Device Management Requests' in XCMI Ext to Host Resources
TC. See: Section 3.5.3 'Secure Simple Device Mgmt Requests' in XCMI Security
TC. See: 'xcmHrDevMgmtCommand[Request|Data|Status]'
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCommandInProgress.setDescription("""\
The device management in progress status associated with this conceptual row in
'xcmHrDevMgmtTable'. Usage: Conforming management agents SHALL 'reject' any
SNMP Set-Request to 'xcmHrDevMgmtCommand[Request|Data]' while another
management operation is already in progress (ie, while
'xcmHrDevMgmtCommandInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3).
""")


class _XcmHrDevMgmtUserName_Type(OctetString):
    """Custom type xcmHrDevMgmtUserName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtUserName_Type.__name__ = "OctetString"
_XcmHrDevMgmtUserName_Object = MibTableColumn
xcmHrDevMgmtUserName = _XcmHrDevMgmtUserName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 9),
    _XcmHrDevMgmtUserName_Type()
)
xcmHrDevMgmtUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtUserName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtUserName.setReference("""\
See: 'xcmHrDevMgmt[Operator|Admin]Name' See: Section 3.5.2 'Secure Password
Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable' in XCMI
System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB. See: Both the
X/Open PSIS (Printing Systems Interoperability Specification) and the new Part
3 'Systems Management' of DPA (ISO/IEC 10175) use the simple three-role scheme
specified here In Appendix D 'Roles of Users' (pages 108 to 109) of Printer MI
v1 (RFC 1759), Jay Martin provided an excellent discussion of a number of user
'role models', including the following ones: User (USER) - A person or
application that submits print jobs to the printer; typically viewed as the
'end user' within the overall printing environment. Operator (OP) - A person
responsible for maintaining a printer on a day-to-day basis, including such
tasks as filling empty media trays, emptying full output trays, replacing toner
cartridges, etc. System Manager (MGR) - A person responsible for configuration
and troubleshooting of components involved in the overall printing environment,
including printers, print queues and network connectivity issues. This person
is typically responsible for ensuring the overall operational integrity of the
print system components, and is typically viewed as the central point of
coordination among all other Role Models.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtUserName.setDescription("""\
A protected end user Name for this device. Usage: Conformant implementations
MUST encrypt passwords, keys, and other security information stored in this
string object. Usage: All XCMI conforming management agents: a) SHOULD always
return a zero length string in response to an SNMP GetRequest of this object;
b) SHALL NOT return the contents of this object in cleartext (ie, unencrypted)
in response to an SNMP GetRequest; c) SHOULD support (ie, accept) an
authenticated SNMP SetRequest changing the system 'end user Name' in this
object. Usage: Conforming management stations and management agents SHOULD
support authentication of SNMP SetRequests via values of
'xcmHrDevMgmt[User|Operator|Admin]Name' in ciphertext (ie, encrypted) written
in 'xcmHrDevMgmtCommandData'. Usage: Conforming management stations MAY support
client-side authentication of user roles and rights via checking values of
'xcmHrDevMgmt[User|Operator|Admin]Name' presented in client applications (eg,
install tools). WARNING: Such authentication mechanisms do NOT protect managed
systems from attack by other SNMP client applications that do NOT perform such
client-side authentication and are thus inherently weak.
""")


class _XcmHrDevMgmtOperatorName_Type(OctetString):
    """Custom type xcmHrDevMgmtOperatorName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtOperatorName_Type.__name__ = "OctetString"
_XcmHrDevMgmtOperatorName_Object = MibTableColumn
xcmHrDevMgmtOperatorName = _XcmHrDevMgmtOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 10),
    _XcmHrDevMgmtOperatorName_Type()
)
xcmHrDevMgmtOperatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtOperatorName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtOperatorName.setReference("""\
See: 'xcmHrDevMgmt[User|Admin]Name' See: Section 3.5.2 'Secure Password Change
Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable' in XCMI System
Admin MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtOperatorName.setDescription("""\
A protected system operator Name for this device. Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information
stored in this string object. Usage: All XCMI conforming management agents: a)
SHOULD always return a zero length string in response to an SNMP GetRequest of
this object; b) SHALL NOT return the contents of this object in cleartext (ie,
unencrypted) in response to an SNMP GetRequest; c) SHOULD support (ie, accept)
an authenticated SNMP SetRequest changing the system 'operator Name' in this
object. Usage: Conforming management stations and management agents SHOULD
support authentication of SNMP SetRequests via values of
'xcmHrDevMgmt[User|Operator|Admin]Name' in ciphertext (ie, encrypted) written
in 'xcmHrDevMgmtCommandData'. Usage: Conforming management stations MAY support
client-side authentication of user roles and rights via checking values of
'xcmHrDevMgmt[User|Operator|Admin]Name' presented in client applications (eg,
install tools). WARNING: Such authentication mechanisms do NOT protect managed
systems from attack by other SNMP client applications that do NOT perform such
client-side authentication and are thus inherently weak.
""")


class _XcmHrDevMgmtAdminName_Type(OctetString):
    """Custom type xcmHrDevMgmtAdminName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtAdminName_Type.__name__ = "OctetString"
_XcmHrDevMgmtAdminName_Object = MibTableColumn
xcmHrDevMgmtAdminName = _XcmHrDevMgmtAdminName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 11),
    _XcmHrDevMgmtAdminName_Type()
)
xcmHrDevMgmtAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtAdminName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtAdminName.setReference("""\
See: 'xcmHrDevMgmt[User|Operator]Name' See: Section 3.5.2 'Secure Password
Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable' in XCMI
System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtAdminName.setDescription("""\
A protected system administrator Name for this device. Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information
stored in this string object. Usage: All XCMI conforming management agents: a)
SHOULD always return a zero length string in response to an SNMP GetRequest of
this object; b) SHALL NOT return the contents of this object in cleartext (ie,
unencrypted) in response to an SNMP GetRequest; c) SHOULD support (ie, accept)
an authenticated SNMP SetRequest changing the system 'administrator Name' in
this object. Usage: Conforming management stations and management agents SHOULD
support authentication of SNMP SetRequests via values of
'xcmHrDevMgmt[User|Operator|Admin]Name' in ciphertext (ie, encrypted) written
in 'xcmHrDevMgmtCommandData'. Usage: Conforming management stations MAY support
client-side authentication of user roles and rights via checking values of
'xcmHrDevMgmt[User|Operator|Admin]Name' presented in client applications (eg,
install tools). WARNING: Such authentication mechanisms do NOT protect managed
systems from attack by other SNMP client applications that do NOT perform such
client-side authentication and are thus inherently weak.
""")


class _XcmHrDevMgmtCustomPassword_Type(OctetString):
    """Custom type xcmHrDevMgmtCustomPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevMgmtCustomPassword_Type.__name__ = "OctetString"
_XcmHrDevMgmtCustomPassword_Object = MibTableColumn
xcmHrDevMgmtCustomPassword = _XcmHrDevMgmtCustomPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 2, 1, 12),
    _XcmHrDevMgmtCustomPassword_Type()
)
xcmHrDevMgmtCustomPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCustomPassword.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCustomPassword.setReference("""\
See: 'xcmHrDevMgmt[User|Operator|Admin]Password' See: Section 3.5.2 'Secure
Password Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable'
in XCMI System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevMgmtCustomPassword.setDescription("""\
A protected PDL password for this device. Usage: Conformant implementations
MUST encrypt passwords, keys, and other security information stored in this
string object. Usage: All XCMI conforming management agents: a) SHOULD always
return an encoded string in response to an SNMP GetRequest of this object; b)
SHALL NOT return the contents of this object in cleartext (ie, unencrypted) in
response to an SNMP GetRequest; c) SHOULD support (ie, accept) an unencoded
SNMP SetRequest changing the system 'custom password' in this object. Usage:
Conforming management stations and management agents SHOULD support
authentication of SNMP SetRequests via values of
'xcmHrDevMgmt[User|Operator|Admin|Custom]Password' in written cleartext in
'xcmHrDevMgmtCommandData'. Usage: Conforming management stations MAY support
client-side authentication of user roles and rights via checking values of
'xcmHrDevMgmt[User|Operator|Admin|Custom]Password' presented in client
applications (eg, install tools). WARNING: Such mechanisms do NOT protect
managed systems from attack by other authentication SNMP client applications
that do NOT perform such client-side authentication and are thus inherently
weak.
""")
_XcmHrDevPower_ObjectIdentity = ObjectIdentity
xcmHrDevPower = _XcmHrDevPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6)
)
_XcmHrDevPowerTable_Object = MibTable
xcmHrDevPowerTable = _XcmHrDevPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevPowerTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerTable.setReference("""\
See: 'hrProcessorTable', 'hrNetworkTable', 'hrPrinterTable' in the IETF Host
Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerTable.setDescription("""\
A 'sparse' table containing power management cycle objects for installed and
(possibly) active devices on this host system, augmenting the basic entries in
the 'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevPowerEntry_Object = MibTableRow
xcmHrDevPowerEntry = _XcmHrDevPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1)
)
xcmHrDevPowerEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevPowerEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerEntry.setDescription("""\
A 'sparse' entry containing power management cycle objects for an installed and
(possibly) active device on this host system, augmenting a basic entry in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevPowerRowStatus_Type = RowStatus
_XcmHrDevPowerRowStatus_Object = MibTableColumn
xcmHrDevPowerRowStatus = _XcmHrDevPowerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 1),
    _XcmHrDevPowerRowStatus_Type()
)
xcmHrDevPowerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrDevPowerTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmHrDevPowerRowStatus' row status object; and SHALL clear the
'xcmHrDevPowerGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrDevPowerRowStatus' row status object; and SHALL set the
'xcmHrDevPowerGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrDevPowerWarmUpSupport_Type(PresentOnOff):
    """Custom type xcmHrDevPowerWarmUpSupport based on PresentOnOff"""


_XcmHrDevPowerWarmUpSupport_Object = MibTableColumn
xcmHrDevPowerWarmUpSupport = _XcmHrDevPowerWarmUpSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 2),
    _XcmHrDevPowerWarmUpSupport_Type()
)
xcmHrDevPowerWarmUpSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpSupport.setReference("""\
See: 'xcmHrDevPowerWarmUp[Delay|Duration]'
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpSupport.setDescription("""\
A device 'warm up' feature support management object, used by system
administrators of this device. Usage: This object specifies the support present
(if any) for a device 'warm up' feature ('standbyMode' to 'readyMode'). For
example, a photocopier might want to 'warm up' (as a system) (to 'readyMode')
some time after a user presses a button. * 'other(1)' - DEPRECATED - SHALL NOT
be used by conforming implementations * 'on(3)' - device 'warm up' feature is
present and enabled both '...WarmUpDelay' and '...WarmUpDuration' are used - if
'...WarmUpDelay' is zero, then 'warm up' cycle begins immediately after trigger
event - if '...WarmUpDelay' is non-zero, then 'warm up' cycle is delayed for
specified time - if '...WarmUpDuration' is zero, then 'warm up' cycle completes
immediately after initiation - if '...WarmUpDuration' is non-zero, then 'warm
up' cycle requires specified time to complete * 'off(4)' - device 'warm up'
feature is present but disabled both '...WarmUpDelay' and '...WarmUpDuration'
NOT used * 'notPresent(5)' - device 'warm up' feature NOT present on this host
system both '...WarmUpDelay' and '...WarmUpDuration' NOT used
""")


class _XcmHrDevPowerCoolDownSupport_Type(PresentOnOff):
    """Custom type xcmHrDevPowerCoolDownSupport based on PresentOnOff"""


_XcmHrDevPowerCoolDownSupport_Object = MibTableColumn
xcmHrDevPowerCoolDownSupport = _XcmHrDevPowerCoolDownSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 3),
    _XcmHrDevPowerCoolDownSupport_Type()
)
xcmHrDevPowerCoolDownSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownSupport.setReference("""\
See: 'xcmHrDevPowerCoolDown[Delay|Duration]'
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownSupport.setDescription("""\
A device 'cool down' feature support management object, used by system
administrators of this device. Usage: This object specifies the support present
(if any) for a device 'cool down' feature ('readyMode' to 'standbyMode'). For
example, a printer might want to 'cool down' a motor (to 'standbyMode') some
time after the last page printed. * 'other(1)' - DEPRECATED - SHALL NOT be used
by conforming implementations * 'on(3)' - device 'cool down' feature is present
and enabled both '...CoolDownDelay' and '...CoolDownDuration' are used - if
'...CoolDownDelay' is zero, then 'cool down' cycle begins immediately after
trigger event - if '...CoolDownDelay' is non-zero, then 'cool down' cycle is
delayed for specified time - if '...CoolDownDuration' is zero, then 'cool down'
cycle completes immediately after initiation - if '...CoolDownDuration' is non-
zero, then 'cool down' cycle requires specified time to complete * 'off(4)' -
device 'cool down' feature is present but disabled both '...CoolDownDelay' and
'...CoolDownDuration' NOT used * 'notPresent(5)' - device 'cool down' feature
NOT present on this host system both '...CoolDownDelay' and
'...CoolDownDuration' NOT used
""")


class _XcmHrDevPowerEnergySaveSupport_Type(PresentOnOff):
    """Custom type xcmHrDevPowerEnergySaveSupport based on PresentOnOff"""


_XcmHrDevPowerEnergySaveSupport_Object = MibTableColumn
xcmHrDevPowerEnergySaveSupport = _XcmHrDevPowerEnergySaveSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 4),
    _XcmHrDevPowerEnergySaveSupport_Type()
)
xcmHrDevPowerEnergySaveSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveSupport.setReference("""\
See: 'xcmHrDevPowerEnergySave[Delay|Duration]'
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveSupport.setDescription("""\
A device 'energy save' feature support management object, used by system
administrators of this device. Usage: This object specifies the support present
(if any) for a device 'energy save' feature ('standbyMode' to 'sleepMode'). For
example, a printer might want to 'energy save' transition (to 'sleepMode') some
time after the last 'cool down' (to 'standbyMode') completion. * 'other(1)' -
DEPRECATED - SHALL NOT be used by conforming implementations * 'on(3)' - device
'energy save' feature is present and enabled both '...EnergySaveDelay' and
'...EnergySaveDuration' are used - if '...EnergySaveDelay' is zero, then
'energy save' cycle begins immediately after trigger event - if
'...EnergySaveDelay' is non-zero, then 'energy save' cycle is delayed for
specified time - if '...EnergySaveDuration' is zero, then 'energy save' cycle
completes immediately after initiation - if '...EnergySaveDuration' is non-
zero, then 'energy save' cycle requires specified time to complete * 'off(4)' -
device 'energy save' feature is present but disabled both '...EnergySaveDelay'
and '...EnergySaveDuration' NOT used * 'notPresent(5)' - device 'energy save'
feature NOT present on this host system both '...EnergySaveDelay' and
'...EnergySaveDuration' NOT used
""")


class _XcmHrDevPowerTimeUnit_Type(XcmHrDevPowerTimeUnit):
    """Custom type xcmHrDevPowerTimeUnit based on XcmHrDevPowerTimeUnit"""


_XcmHrDevPowerTimeUnit_Object = MibTableColumn
xcmHrDevPowerTimeUnit = _XcmHrDevPowerTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 5),
    _XcmHrDevPowerTimeUnit_Type()
)
xcmHrDevPowerTimeUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerTimeUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerTimeUnit.setDescription("""\
A device power cycle time unit, used by system administrators of this device
for power management cycle times. Usage: Used to scale the values in the Device
Power group, for convenience and (optional) high resolution.
""")
_XcmHrDevPowerWarmUpDelay_Type = Integer32
_XcmHrDevPowerWarmUpDelay_Object = MibTableColumn
xcmHrDevPowerWarmUpDelay = _XcmHrDevPowerWarmUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 6),
    _XcmHrDevPowerWarmUpDelay_Type()
)
xcmHrDevPowerWarmUpDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpDelay.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpDelay.setReference("""\
See: 'xcmHrDevPowerWarmUpSupport' for feature details and
'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for device
'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpDelay.setDescription("""\
A device 'warm up' feature delay time, or zero if none, used by system
administrators of this device. Usage: The time delay after last 'warm up'
trigger event (eg, arrival of a job, some local user action, etc) before the
'warm up' cycle will begin (to power 'readyMode' in 'xcmHrDevInfoConditions').
""")
_XcmHrDevPowerWarmUpDuration_Type = Integer32
_XcmHrDevPowerWarmUpDuration_Object = MibTableColumn
xcmHrDevPowerWarmUpDuration = _XcmHrDevPowerWarmUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 7),
    _XcmHrDevPowerWarmUpDuration_Type()
)
xcmHrDevPowerWarmUpDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpDuration.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpDuration.setReference("""\
See: 'xcmHrDevPowerWarmUpSupport' for feature details and
'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for device
'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerWarmUpDuration.setDescription("""\
A device 'warm up' feature duration, or zero if none, used by system
administrators of this device. Usage: The time after last 'warm up' initiation
before the 'warm up' will complete (to power 'readyMode' in
'xcmHrDevInfoConditions').
""")
_XcmHrDevPowerCoolDownDelay_Type = Integer32
_XcmHrDevPowerCoolDownDelay_Object = MibTableColumn
xcmHrDevPowerCoolDownDelay = _XcmHrDevPowerCoolDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 8),
    _XcmHrDevPowerCoolDownDelay_Type()
)
xcmHrDevPowerCoolDownDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownDelay.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownDelay.setReference("""\
See: 'xcmHrDevPowerCoolDownSupport' for feature details and
'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for device
'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownDelay.setDescription("""\
A device 'cool down' feature delay time, or zero if none, used by system
administrators of this device. Usage: The time delay after last 'cool down'
trigger event (eg, completion of a job, some local user action, etc) before the
'cool down' cycle will begin (to power 'standbyMode' in
'xcmHrDevInfoConditions').
""")
_XcmHrDevPowerCoolDownDuration_Type = Integer32
_XcmHrDevPowerCoolDownDuration_Object = MibTableColumn
xcmHrDevPowerCoolDownDuration = _XcmHrDevPowerCoolDownDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 9),
    _XcmHrDevPowerCoolDownDuration_Type()
)
xcmHrDevPowerCoolDownDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownDuration.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownDuration.setReference("""\
See: 'xcmHrDevPowerCoolDownSupport' for feature details and
'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for device
'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerCoolDownDuration.setDescription("""\
A device 'cool down' feature duration, or zero if none, used by system
administrators of this device. Usage: The time after last 'cool down'
initiation before the 'cool down' will complete (to power 'standbyMode' in
'xcmHrDevInfoConditions').
""")
_XcmHrDevPowerEnergySaveDelay_Type = Integer32
_XcmHrDevPowerEnergySaveDelay_Object = MibTableColumn
xcmHrDevPowerEnergySaveDelay = _XcmHrDevPowerEnergySaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 10),
    _XcmHrDevPowerEnergySaveDelay_Type()
)
xcmHrDevPowerEnergySaveDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveDelay.setReference("""\
See: 'xcmHrDevPowerEnergySaveSupport' for feature details and
'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for device
'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveDelay.setDescription("""\
A device 'energy save' feature delay time, or zero if none, used by system
administrators of this device. Usage: The time delay after last 'energy save'
trigger event (eg, completion of the last 'cool down' cycle to 'standbyMode')
before the 'energy save' cycle will begin (to power 'sleepMode' in
'xcmHrDevInfoConditions').
""")
_XcmHrDevPowerEnergySaveDuration_Type = Integer32
_XcmHrDevPowerEnergySaveDuration_Object = MibTableColumn
xcmHrDevPowerEnergySaveDuration = _XcmHrDevPowerEnergySaveDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 11),
    _XcmHrDevPowerEnergySaveDuration_Type()
)
xcmHrDevPowerEnergySaveDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveDuration.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveDuration.setReference("""\
See: 'xcmHrDevPowerEnergySaveSupport' for feature details and
'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for device
'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerEnergySaveDuration.setDescription("""\
A device 'energy save' feature duration, or zero if none, used by system
administrators of this device. Usage: The time after last 'energy save'
initiation before the 'energy save' will complete (to power 'sleepMode' in
'xcmHrDevInfoConditions').
""")


class _XcmHrDevPowerWakeUpSupport_Type(PresentOnOff):
    """Custom type xcmHrDevPowerWakeUpSupport based on PresentOnOff"""


_XcmHrDevPowerWakeUpSupport_Object = MibTableColumn
xcmHrDevPowerWakeUpSupport = _XcmHrDevPowerWakeUpSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 12),
    _XcmHrDevPowerWakeUpSupport_Type()
)
xcmHrDevPowerWakeUpSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpSupport.setReference("""\
See: 'xcmHrDevPowerWakeUp[Delay|Duration]'
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpSupport.setDescription("""\
A device 'wake up' feature support management object, used by system
administrators of this device. Usage: This object specifies the support present
(if any) for a device 'wake up' feature ('sleepMode' to 'standbyMode'). For
example, a photocopier might want to 'wake up' (as a system) (to 'standbyMode')
some time after a user presses a button. * 'other(1)' - DEPRECATED - SHALL NOT
be used by conforming implementations * 'on(3)' - device 'wake up' feature is
present and enabled both '...WakeUpDelay' and '...WakeUpDuration' are used - if
'...WakeUpDelay' is zero, then 'wake up' cycle begins immediately after trigger
event - if '...WakeUpDelay' is non-zero, then 'wake up' cycle is delayed for
specified time - if '...WakeUpDuration' is zero, then 'wake up' cycle completes
immediately after initiation - if '...WakeUpDuration' is non-zero, then 'wake
up' cycle requires specified time to complete * 'off(4)' - device 'wake up'
feature is present but disabled both '...WakeUpDelay' and '...WakeUpDuration'
NOT used * 'notPresent(5)' - device 'wake up' feature NOT present on this host
system both '...WakeUpDelay' and '...WakeUpDuration' NOT used
""")
_XcmHrDevPowerWakeUpDelay_Type = Integer32
_XcmHrDevPowerWakeUpDelay_Object = MibTableColumn
xcmHrDevPowerWakeUpDelay = _XcmHrDevPowerWakeUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 13),
    _XcmHrDevPowerWakeUpDelay_Type()
)
xcmHrDevPowerWakeUpDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpDelay.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpDelay.setReference("""\
See: 'xcmHrDevPowerWakeUpSupport' for feature details and
'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for device
'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpDelay.setDescription("""\
A device 'wake up' feature delay time, or zero if none, used by system
administrators of this device. Usage: The time delay after last 'wake up'
trigger event (eg, arrival of a job, some local user action, etc) before the
'wake up' cycle will begin (to power 'standbyMode' in
'xcmHrDevInfoConditions').
""")
_XcmHrDevPowerWakeUpDuration_Type = Integer32
_XcmHrDevPowerWakeUpDuration_Object = MibTableColumn
xcmHrDevPowerWakeUpDuration = _XcmHrDevPowerWakeUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 14),
    _XcmHrDevPowerWakeUpDuration_Type()
)
xcmHrDevPowerWakeUpDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpDuration.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpDuration.setReference("""\
See: 'xcmHrDevPowerWakeUpSupport' for feature details and
'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for device
'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerWakeUpDuration.setDescription("""\
A device 'wake up' feature duration, or zero if none, used by system
administrators of this device. Usage: The time after last 'wake up' initiation
before the 'wake up' will complete (to power 'standbyMode' in
'xcmHrDevInfoConditions').
""")
_XcmHrDevPowerShutdownDelay_Type = Integer32
_XcmHrDevPowerShutdownDelay_Object = MibTableColumn
xcmHrDevPowerShutdownDelay = _XcmHrDevPowerShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 15),
    _XcmHrDevPowerShutdownDelay_Type()
)
xcmHrDevPowerShutdownDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerShutdownDelay.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerShutdownDelay.setReference("""\
See: 'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for
device 'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerShutdownDelay.setDescription("""\
A device 'shutdown' feature delay time, or zero if none, used by system
administrators of this device. Usage: The time delay after last 'shutdown'
trigger event (eg, completion of the last 'energy save' cycle to 'sleepMode')
before the 'shutdown' cycle will begin (to power 'offMode' in
'xcmHrDevInfoConditions' and 'down' in 'hrDeviceStatus').
""")
_XcmHrDevPowerShutdownDuration_Type = Integer32
_XcmHrDevPowerShutdownDuration_Object = MibTableColumn
xcmHrDevPowerShutdownDuration = _XcmHrDevPowerShutdownDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 16),
    _XcmHrDevPowerShutdownDuration_Type()
)
xcmHrDevPowerShutdownDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerShutdownDuration.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerShutdownDuration.setReference("""\
See: 'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for
device 'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerShutdownDuration.setDescription("""\
A device 'shutdown' feature duration, or zero if none, used by system
administrators of this device. Usage: The time after last 'shutdown' initiation
before the 'shutdown' cycle will complete (to power 'offMode' in
'xcmHrDevInfoConditions' and 'down' in 'hrDeviceStatus').
""")
_XcmHrDevPowerStartupDelay_Type = Integer32
_XcmHrDevPowerStartupDelay_Object = MibTableColumn
xcmHrDevPowerStartupDelay = _XcmHrDevPowerStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 17),
    _XcmHrDevPowerStartupDelay_Type()
)
xcmHrDevPowerStartupDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerStartupDelay.setReference("""\
See: 'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for
device 'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerStartupDelay.setDescription("""\
A device 'startup' feature delay time, or zero if none, used by system
administrators of this device. Usage: The time delay after last 'startup'
trigger event (eg, 'xcmHrDevCalendarCommandRequest' or local user action)
before the 'startup' cycle will begin (to power 'readyMode' in
'xcmHrDevInfoConditions' and 'running' in 'hrDeviceStatus').
""")
_XcmHrDevPowerStartupDuration_Type = Integer32
_XcmHrDevPowerStartupDuration_Object = MibTableColumn
xcmHrDevPowerStartupDuration = _XcmHrDevPowerStartupDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 6, 2, 1, 18),
    _XcmHrDevPowerStartupDuration_Type()
)
xcmHrDevPowerStartupDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevPowerStartupDuration.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerStartupDuration.setReference("""\
See: 'xcmHrDevPowerTimeUnit' for time unit and 'xcmHrDevInfoConditions' for
device 'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevPowerStartupDuration.setDescription("""\
A device 'startup' feature duration, or zero if none, used by system
administrators of this device. Usage: The time after last 'startup' initiation
before the 'startup' cycle will complete (to power 'readyMode' in
'xcmHrDevInfoConditions' and 'running' in 'hrDeviceStatus').
""")
_XcmHrDevTraffic_ObjectIdentity = ObjectIdentity
xcmHrDevTraffic = _XcmHrDevTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7)
)
_XcmHrDevTrafficTable_Object = MibTable
xcmHrDevTrafficTable = _XcmHrDevTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevTrafficTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficTable.setReference("""\
See: 'hrProcessorTable', 'hrNetworkTable', 'hrPrinterTable' in the IETF Host
Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevTrafficTable.setDescription("""\
A 'sparse' table containing traffic information objects for installed and
(possibly) active devices on this host system, augmenting the basic entries in
the 'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevTrafficEntry_Object = MibTableRow
xcmHrDevTrafficEntry = _XcmHrDevTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1)
)
xcmHrDevTrafficEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevTrafficEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficEntry.setDescription("""\
A 'sparse' entry containing traffic information objects for an installed and
(possibly) active device on this host system, augmenting a basic entry in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevTrafficRowStatus_Type = RowStatus
_XcmHrDevTrafficRowStatus_Object = MibTableColumn
xcmHrDevTrafficRowStatus = _XcmHrDevTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 1),
    _XcmHrDevTrafficRowStatus_Type()
)
xcmHrDevTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevTrafficRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrDevTrafficTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmHrDevTrafficRowStatus' row status object; and SHALL clear the
'xcmHrDevTrafficGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrDevTrafficRowStatus' row status object; and SHALL set the
'xcmHrDevTrafficGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrDevTrafficInputSupport_Type(PresentOnOff):
    """Custom type xcmHrDevTrafficInputSupport based on PresentOnOff"""


_XcmHrDevTrafficInputSupport_Object = MibTableColumn
xcmHrDevTrafficInputSupport = _XcmHrDevTrafficInputSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 2),
    _XcmHrDevTrafficInputSupport_Type()
)
xcmHrDevTrafficInputSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputSupport.setReference("""\
See: 'xcmHrDevTrafficInputTimeout'.
""")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputSupport.setDescription("""\
A device input traffic support management object, used by system administrators
of this device. Usage: This object specifies the support present (if any) for
device input traffic (I/O). For example, a ROM only supports input traffic (ie,
reads). * 'other(1)' - DEPRECATED - SHALL NOT be used by conforming
implementations * 'on(3)' - device 'input I/O' feature is present and enabled
and '...InputTimeout' is meaningful - if '...InputTimeout' is zero, then 'input
I/O' cycle MAY proceed for an infinite time - if '...InputTimeout' is non-zero,
then 'input I/O' cycle is limited to the specified time * 'off(4)' - device
'input I/O' feature is present but disabled and '...InputTimeout' is ignored *
'notPresent(5)' - device 'input I/O' feature NOT present on this host system
and '...InputTimeout' is ignored
""")


class _XcmHrDevTrafficOutputSupport_Type(PresentOnOff):
    """Custom type xcmHrDevTrafficOutputSupport based on PresentOnOff"""


_XcmHrDevTrafficOutputSupport_Object = MibTableColumn
xcmHrDevTrafficOutputSupport = _XcmHrDevTrafficOutputSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 3),
    _XcmHrDevTrafficOutputSupport_Type()
)
xcmHrDevTrafficOutputSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputSupport.setReference("""\
See: 'xcmHrDevTrafficOutputTimeout'.
""")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputSupport.setDescription("""\
A device output traffic support management object, used by system
administrators of this device. Usage: This object specifies the support present
(if any) for device output traffic (I/O). For example, a ROM does NOT support
output traffic (ie, writes). * 'other(1)' - DEPRECATED - SHALL NOT be used by
conforming implementations * 'on(3)' - device 'output I/O' feature is present
and enabled and '...OutputTimeout' is meaningful - if '...OutputTimeout' is
zero, then 'output I/O' cycle MAY proceed for an infinite time - if
'...OutputTimeout' is non-zero, then 'output I/O' cycle is limited to the
specified time * 'off(4)' - device 'output I/O' feature is present but disabled
and '...OutputTimeout' is ignored * 'notPresent(5)' - device 'output I/O'
feature NOT present on this host system and '...OutputTimeout' is ignored
""")


class _XcmHrDevTrafficInputUnit_Type(XcmHrDevTrafficUnit):
    """Custom type xcmHrDevTrafficInputUnit based on XcmHrDevTrafficUnit"""


_XcmHrDevTrafficInputUnit_Object = MibTableColumn
xcmHrDevTrafficInputUnit = _XcmHrDevTrafficInputUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 4),
    _XcmHrDevTrafficInputUnit_Type()
)
xcmHrDevTrafficInputUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputUnit.setDescription("""\
A device input unit, used by system administrators of this device for input
traffic counters. Usage: For example, a disk drive might use 'mediaBlock'.
Usage: Thanks to XCMI WG members for stimulating the following discussion.
There are three reasonable ways for using the
'xcmHrDevTraffic[Input|Output]Unit' objects: a) 'read-only' and set up by the
management agent according to the sole appropriate (fixed) units at time of row
creation; b) 'write-once' by the management station, at time of row creation
(possibly selecting from among several possible valid units); and c) 'write-
many' by the management station (to dynamically request the management agent to
'convert' the 'xcmHrDevTraffic[Input|Output]Count' objects into the appropriate
units). Conforming implementations need NOT support more than one of the above
three scenarios. Usage: 'mediaImage' - SHOULD be used ONLY for softcopy INPUT
page images (scan, copy, fax, etc.). 'mediaImpression' - SHOULD be used ONLY
for hardcopy OUTPUT page impressions (print, copy, fax, etc.) 'mediaSheet' -
SHOULD be used ONLY for hardcopy OUTPUT and does NOT always equal output pages
(e.g., duplex or N-up printing).
""")


class _XcmHrDevTrafficOutputUnit_Type(XcmHrDevTrafficUnit):
    """Custom type xcmHrDevTrafficOutputUnit based on XcmHrDevTrafficUnit"""


_XcmHrDevTrafficOutputUnit_Object = MibTableColumn
xcmHrDevTrafficOutputUnit = _XcmHrDevTrafficOutputUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 5),
    _XcmHrDevTrafficOutputUnit_Type()
)
xcmHrDevTrafficOutputUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputUnit.setDescription("""\
A device output unit, used by system administrators of this device for output
traffic counters. Usage: For example, a terminal might use 'textLine'. Usage:
'mediaImage' - SHOULD be used ONLY for softcopy INPUT page images (scan, copy,
fax, etc.). 'mediaImpression' - SHOULD be used ONLY for hardcopy OUTPUT page
impressions (print, copy, fax, etc.) 'mediaSheet' - SHOULD be used ONLY for
hardcopy OUTPUT and does NOT always equal output pages (e.g., duplex or N-up
printing).
""")
_XcmHrDevTrafficInputCount_Type = Counter32
_XcmHrDevTrafficInputCount_Object = MibTableColumn
xcmHrDevTrafficInputCount = _XcmHrDevTrafficInputCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 6),
    _XcmHrDevTrafficInputCount_Type()
)
xcmHrDevTrafficInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputCount.setReference("""\
See: 'hrDeviceErrors' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputCount.setDescription("""\
A device input traffic count, used by system administrators and end users of
this device. Usage: Although no default value ('DEFVAL' clause) is permitted
(by IETF SMIv2) for this counter, conforming host systems SHALL zero this
counter upon conceptual row creation.
""")
_XcmHrDevTrafficOutputCount_Type = Counter32
_XcmHrDevTrafficOutputCount_Object = MibTableColumn
xcmHrDevTrafficOutputCount = _XcmHrDevTrafficOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 7),
    _XcmHrDevTrafficOutputCount_Type()
)
xcmHrDevTrafficOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputCount.setReference("""\
See: 'hrDeviceErrors' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputCount.setDescription("""\
A device output traffic count, used by system administrators and end users of
this device. Usage: Although no default value ('DEFVAL' clause) is permitted
(by IETF SMIv2) for this counter, conforming host systems SHALL zero this
counter upon conceptual row creation.
""")
_XcmHrDevTrafficInputMaxSize_Type = Cardinal32
_XcmHrDevTrafficInputMaxSize_Object = MibTableColumn
xcmHrDevTrafficInputMaxSize = _XcmHrDevTrafficInputMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 8),
    _XcmHrDevTrafficInputMaxSize_Type()
)
xcmHrDevTrafficInputMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputMaxSize.setDescription("""\
A device input maximum size, or zero if infinite, used by system administrators
and end users of this device. Usage: It is device specific how (or if) this
limit object is used (eg, disk with 'xcmHrDevTrafficInputUnit' of 'mediaBlock'
might limit block count of a single disk read to '50').
""")
_XcmHrDevTrafficOutputMaxSize_Type = Cardinal32
_XcmHrDevTrafficOutputMaxSize_Object = MibTableColumn
xcmHrDevTrafficOutputMaxSize = _XcmHrDevTrafficOutputMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 9),
    _XcmHrDevTrafficOutputMaxSize_Type()
)
xcmHrDevTrafficOutputMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputMaxSize.setDescription("""\
A device output maximum size, or zero if infinite, used by system
administrators and end users of this device. Usage: It is device specific how
(or if) this limit object is used (eg, disk with 'xcmHrDevTrafficOutputUnit' of
'mediaBlock' might limit block count of a single disk write to '50').
""")
_XcmHrDevTrafficInputTimeout_Type = Integer32
_XcmHrDevTrafficInputTimeout_Object = MibTableColumn
xcmHrDevTrafficInputTimeout = _XcmHrDevTrafficInputTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 10),
    _XcmHrDevTrafficInputTimeout_Type()
)
xcmHrDevTrafficInputTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputTimeout.setUnits("seconds")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputTimeout.setReference("""\
See: 'xcmHrDevTrafficInputSupport' for feature details and
'xcmHrDevInfoConditions' for device 'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevTrafficInputTimeout.setDescription("""\
A device input traffic timeout (in seconds), or zero if none, used by system
administrators of this device. Usage: This object specifies the timeout to be
used (if any) for device input traffic (I/O). For example, a disk drive might
want to timeout disk reads.
""")
_XcmHrDevTrafficOutputTimeout_Type = Integer32
_XcmHrDevTrafficOutputTimeout_Object = MibTableColumn
xcmHrDevTrafficOutputTimeout = _XcmHrDevTrafficOutputTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 7, 2, 1, 11),
    _XcmHrDevTrafficOutputTimeout_Type()
)
xcmHrDevTrafficOutputTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputTimeout.setUnits("seconds")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputTimeout.setReference("""\
See: 'xcmHrDevTrafficOutputSupport' for feature details and
'xcmHrDevInfoConditions' for device 'mode' conditions
""")
if mibBuilder.loadTexts:
    xcmHrDevTrafficOutputTimeout.setDescription("""\
A device output traffic timeout (in seconds), or zero if none, used by system
administrators of this device. Usage: This object specifies the timeout to be
used (if any) for device output traffic (I/O). For example, a terminal might
want to timeout screen writes.
""")
_XcmHrSystemFault_ObjectIdentity = ObjectIdentity
xcmHrSystemFault = _XcmHrSystemFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8)
)
_XcmHrSystemFaultTable_Object = MibTable
xcmHrSystemFaultTable = _XcmHrSystemFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2)
)
if mibBuilder.loadTexts:
    xcmHrSystemFaultTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultTable.setDescription("""\
A table of the system faults which have been recorded (logged) on this host
system. Usage: Conforming implementations SHALL ensure that this table contains
(up to) a product specific number of the most 'recent' faults on this host
system. Usage: Conforming implementations which also implement Device Alert
group, SHALL record in 'xcmHrDevAlertTable' each persistent system fault when
it occurs and is recorded in 'xcmHrSystemFaultTable'. Usage: Conforming
implementations MAY 'age' older entries out of 'xcmHrSystemFaultTable' (by an
algorithm outside the scope of XCMI specifications).
""")
_XcmHrSystemFaultEntry_Object = MibTableRow
xcmHrSystemFaultEntry = _XcmHrSystemFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1)
)
xcmHrSystemFaultEntry.setIndexNames(
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultIndex"),
)
if mibBuilder.loadTexts:
    xcmHrSystemFaultEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultEntry.setDescription("""\
An entry for a system fault which has been recorded (logged) on this host
system.
""")
_XcmHrSystemFaultIndex_Type = Ordinal32
_XcmHrSystemFaultIndex_Object = MibTableColumn
xcmHrSystemFaultIndex = _XcmHrSystemFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 1),
    _XcmHrSystemFaultIndex_Type()
)
xcmHrSystemFaultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrSystemFaultIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrSystemFaultTable'. Usage: Conforming implementations SHALL NOT 'reuse'
values of 'xcmHrSystemFaultIndex' until its' 32-bit value wraps. Even in the
case of eventual wrap, the entries SHALL be strictly sequenced by the
associated value of 'xcmHrSystemFaultDate'. Usage: Conforming implementations
are strongly encouraged to preserve the last used value of
'xcmHrSystemFaultIndex' across system power cycles.
""")
_XcmHrSystemFaultRowStatus_Type = RowStatus
_XcmHrSystemFaultRowStatus_Object = MibTableColumn
xcmHrSystemFaultRowStatus = _XcmHrSystemFaultRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 2),
    _XcmHrSystemFaultRowStatus_Type()
)
xcmHrSystemFaultRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSystemFaultRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrSystemFaultRowStatus.setDescription("""\
This object is used to create (by management agent) and delete (by management
station and/or management agent) individual conceptual rows in the
'xcmHrSystemFaultTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmHrSystemFaultRowStatus' row status object; and SHALL clear the
'xcmHrSystemFaultGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrSystemFaultRowStatus' row status object; and SHALL set the
'xcmHrSystemFaultGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")
_XcmHrSystemFaultCode_Type = Integer32
_XcmHrSystemFaultCode_Object = MibTableColumn
xcmHrSystemFaultCode = _XcmHrSystemFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 3),
    _XcmHrSystemFaultCode_Type()
)
xcmHrSystemFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultCode.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultCode.setDescription("""\
Encoded fault code of the system fault which is recorded in this conceptual row
in the 'xcmHrSystemFaultTable'.
""")


class _XcmHrSystemFaultString_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrSystemFaultString based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrSystemFaultString_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrSystemFaultString_Object = MibTableColumn
xcmHrSystemFaultString = _XcmHrSystemFaultString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 4),
    _XcmHrSystemFaultString_Type()
)
xcmHrSystemFaultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultString.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultString.setDescription("""\
Human-readable fault string of the system fault which is recorded in this
conceptual row in the 'xcmHrSystemFaultTable'.
""")


class _XcmHrSystemFaultReferenceOID_Type(ObjectIdentifier):
    """Custom type xcmHrSystemFaultReferenceOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmHrSystemFaultReferenceOID_Object = MibTableColumn
xcmHrSystemFaultReferenceOID = _XcmHrSystemFaultReferenceOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 5),
    _XcmHrSystemFaultReferenceOID_Type()
)
xcmHrSystemFaultReferenceOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultReferenceOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultReferenceOID.setDescription("""\
An (optional) unambiguous system object reference (which MAY include instance
suffix information), used by system administrators and end users to qualify
this system fault. Usage: Since this system object reference is specified as an
object identifier, it MAY be taken from any IETF, Xerox, third- party, or
product-specific MIB, or it MAY simply be any IETF SMIv2-style 'autonomous
type'.
""")
_XcmHrSystemFaultHrDeviceIndex_Type = Cardinal32
_XcmHrSystemFaultHrDeviceIndex_Object = MibTableColumn
xcmHrSystemFaultHrDeviceIndex = _XcmHrSystemFaultHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 6),
    _XcmHrSystemFaultHrDeviceIndex_Type()
)
xcmHrSystemFaultHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultHrDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultHrDeviceIndex.setReference("""\
See: 'hrDeviceIndex' and 'hrDeviceType' objects in the IETF Host Resources MIB
(RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrSystemFaultHrDeviceIndex.setDescription("""\
An (optional) device index (ie, value of 'hrDeviceIndex'), used by system
administrators and end users to qualify this system fault.
""")


class _XcmHrSystemFaultDate_Type(DateAndTime):
    """Custom type xcmHrSystemFaultDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrSystemFaultDate_Object = MibTableColumn
xcmHrSystemFaultDate = _XcmHrSystemFaultDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 8, 2, 1, 7),
    _XcmHrSystemFaultDate_Type()
)
xcmHrSystemFaultDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSystemFaultDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultDate.setDescription("""\
The time stamp for the system fault which is recorded in this conceptual row in
the 'xcmHrSystemFaultTable'.
""")
_XcmHrGeneral_ObjectIdentity = ObjectIdentity
xcmHrGeneral = _XcmHrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9)
)
_XcmHrGeneralTable_Object = MibTable
xcmHrGeneralTable = _XcmHrGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2)
)
if mibBuilder.loadTexts:
    xcmHrGeneralTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralTable.setDescription("""\
A table of general counters and information for ease of use of the XCMI Ext to
IETF Host Resources MIB and the IETF Host Resources MIB (RFC 2790) on this host
system. Usage: The ONLY valid row in the 'xcmHrGeneralTable' SHALL have an
'xcmHrGeneralIndex' of one ('1').
""")
_XcmHrGeneralEntry_Object = MibTableRow
xcmHrGeneralEntry = _XcmHrGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1)
)
xcmHrGeneralEntry.setIndexNames(
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralIndex"),
)
if mibBuilder.loadTexts:
    xcmHrGeneralEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralEntry.setDescription("""\
An entry of general counters and information for ease of use of the XCMI Ext to
IETF Host Resources MIB and the IETF Host Resources MIB (RFC 2790) on this host
system. Usage: The ONLY valid row in the 'xcmHrGeneralTable' SHALL have an
'xcmHrGeneralIndex' of one ('1').
""")
_XcmHrGeneralIndex_Type = Ordinal32
_XcmHrGeneralIndex_Object = MibTableColumn
xcmHrGeneralIndex = _XcmHrGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 1),
    _XcmHrGeneralIndex_Type()
)
xcmHrGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrGeneralIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrGeneralTable'. Usage: The ONLY valid row in the 'xcmHrGeneralTable' SHALL
have an 'xcmHrGeneralIndex' of one ('1').
""")
_XcmHrGeneralRowStatus_Type = RowStatus
_XcmHrGeneralRowStatus_Object = MibTableColumn
xcmHrGeneralRowStatus = _XcmHrGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 2),
    _XcmHrGeneralRowStatus_Type()
)
xcmHrGeneralRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralRowStatus.setDescription("""\
This object is used to display status of the ONLY valid conceptual row in the
'xcmHrGeneralTable'. Usage: 'xcmHrGeneralRowStatus' is 'read-only' because the
ONLY valid conceptual row SHALL NOT be deleted.
""")


class _XcmHrGeneralVersionID_Type(ProductID):
    """Custom type xcmHrGeneralVersionID based on ProductID"""
    defaultValue = "(0, 0)"


_XcmHrGeneralVersionID_Object = MibTableColumn
xcmHrGeneralVersionID = _XcmHrGeneralVersionID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 3),
    _XcmHrGeneralVersionID_Type()
)
xcmHrGeneralVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralVersionID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralVersionID.setReference("""\
See: 'hrSW[Installed|Run]ID' in the Software Installed and Software Running
groups of the IETF HR MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrGeneralVersionID.setDescription("""\
The software product ID of the SNMP sub-agent which implements the IETF Host
Resources MIB (RFC 2790) and XCMI Extensions to Host Resources MIB on this host
system. Usage: This object SHALL specify the software product ID of an SNMP
sub-agent (possibly also found in a conceptual row in the 'hrSWRunTable' and/or
'hrSWInstalledTable' in the IETF HR MIB). This object SHALL NOT specify a
particular release of the IETF HR MIB, the XCMI HRX MIB, or the whole host
system product. Note: Contrast with 'sysObjectID' for the whole SNMP agent in
the IETF MIB-II (RFC 1213) and 'hrDeviceID' for the whole device (or whole
product, in the case of 'xcmHrDevice...') in the IETF Host Resources MIB (RFC
2790).
""")


class _XcmHrGeneralVersionDate_Type(DateAndTime):
    """Custom type xcmHrGeneralVersionDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrGeneralVersionDate_Object = MibTableColumn
xcmHrGeneralVersionDate = _XcmHrGeneralVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 4),
    _XcmHrGeneralVersionDate_Type()
)
xcmHrGeneralVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralVersionDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralVersionDate.setReference("""\
See: 'hrSW[Installed|Run]ID' in the Software Installed and Software Running
groups of the IETF HR MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrGeneralVersionDate.setDescription("""\
The software build date of the SNMP sub-agent which implements the IETF Host
Resources MIB (RFC 2790) and XCMI Extensions to Host Resources MIB on this host
system. Usage: This object SHALL specify the BUILD date of the SNMP sub-agent
software (not available elsewhere in IETF/XCMI MIBs). This object SHALL NOT
specify the INSTALL date of the SNMP sub-agent software on this host system,
nor the RESET date. Note: Contrast with 'hrSWInstalledDate' in the Software
Installed group of the IETF Host Resources MIB (RFC 2790), and
'xcmHrDevInfoResetDate' in the Device Info group of the XCMI Host Resources
Extensions MIB.
""")


class _XcmHrGeneralGroupSupport_Type(XcmHrGroupSupport):
    """Custom type xcmHrGeneralGroupSupport based on XcmHrGroupSupport"""
    defaultValue = 71


_XcmHrGeneralGroupSupport_Object = MibTableColumn
xcmHrGeneralGroupSupport = _XcmHrGeneralGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 5),
    _XcmHrGeneralGroupSupport_Type()
)
xcmHrGeneralGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralGroupSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional IETF Host Resources MIB (RFC 2790) and XCMI Ext to IETF Host Resources
MIB objects which are supported by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. Usage: Conforming
management agents SHALL accurately report their support for IETF Host Resources
MIB (RFC 2790) and XCMI Ext to IETF Host Resources MIB object groups.
""")
_XcmHrGeneralStorageLast_Type = Cardinal32
_XcmHrGeneralStorageLast_Object = MibTableColumn
xcmHrGeneralStorageLast = _XcmHrGeneralStorageLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 6),
    _XcmHrGeneralStorageLast_Type()
)
xcmHrGeneralStorageLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralStorageLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralStorageLast.setDescription("""\
The last entry index (regardless of its current state) in the 'hrStorageTable'
of the IETF Host Resources MIB, on this host system. Usage: The last entry
index explicitly bounds the valid range of 'hrStorageIndex'.
""")
_XcmHrGeneralDeviceLast_Type = Cardinal32
_XcmHrGeneralDeviceLast_Object = MibTableColumn
xcmHrGeneralDeviceLast = _XcmHrGeneralDeviceLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 7),
    _XcmHrGeneralDeviceLast_Type()
)
xcmHrGeneralDeviceLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralDeviceLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralDeviceLast.setDescription("""\
The last entry index (regardless of its current state) in the 'hrDeviceTable'
of the IETF Host Resources MIB, on this host system. Usage: The last entry
index explicitly bounds the valid range of 'hrDeviceIndex'.
""")
_XcmHrGeneralFSLast_Type = Cardinal32
_XcmHrGeneralFSLast_Object = MibTableColumn
xcmHrGeneralFSLast = _XcmHrGeneralFSLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 8),
    _XcmHrGeneralFSLast_Type()
)
xcmHrGeneralFSLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralFSLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralFSLast.setDescription("""\
The last entry index (regardless of its current state) in the 'hrFSTable' of
the IETF Host Resources MIB, on this host system. Usage: The last entry index
explicitly bounds the valid range of 'hrFSIndex'.
""")
_XcmHrGeneralSWRunLast_Type = Cardinal32
_XcmHrGeneralSWRunLast_Object = MibTableColumn
xcmHrGeneralSWRunLast = _XcmHrGeneralSWRunLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 9),
    _XcmHrGeneralSWRunLast_Type()
)
xcmHrGeneralSWRunLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralSWRunLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralSWRunLast.setDescription("""\
The last entry index (regardless of its current state) in the 'hrSWRunTable' of
the IETF Host Resources MIB, on this host system. Usage: The last entry index
explicitly bounds the valid range of 'hrSWRunIndex'.
""")
_XcmHrGeneralSWInstalledLast_Type = Cardinal32
_XcmHrGeneralSWInstalledLast_Object = MibTableColumn
xcmHrGeneralSWInstalledLast = _XcmHrGeneralSWInstalledLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 10),
    _XcmHrGeneralSWInstalledLast_Type()
)
xcmHrGeneralSWInstalledLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralSWInstalledLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralSWInstalledLast.setDescription("""\
The last entry index (regardless of its current state) in the
'hrSWInstalledTable' of the IETF Host Resources MIB, on this host system.
Usage: The last entry index explicitly bounds the valid range of
'hrSWInstalledIndex'.
""")
_XcmHrGeneralSystemFaultLast_Type = Cardinal32
_XcmHrGeneralSystemFaultLast_Object = MibTableColumn
xcmHrGeneralSystemFaultLast = _XcmHrGeneralSystemFaultLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 11),
    _XcmHrGeneralSystemFaultLast_Type()
)
xcmHrGeneralSystemFaultLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralSystemFaultLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralSystemFaultLast.setDescription("""\
The last entry index (regardless of its current state) in the
'xcmHrSystemFaultTable' of this XCMI Ext to Host Resources MIB, on this host
system. Usage: The last entry index explicitly bounds the valid range of
'xcmHrSystemFaultIndex'.
""")
_XcmHrGeneralCreateSupport_Type = XcmHrGroupSupport
_XcmHrGeneralCreateSupport_Object = MibTableColumn
xcmHrGeneralCreateSupport = _XcmHrGeneralCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 12),
    _XcmHrGeneralCreateSupport_Type()
)
xcmHrGeneralCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralCreateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional IETF Host Resources MIB (RFC 2790) and XCMI Ext to IETF Host Resources
MIB objects which are supported for dynamic row creation (via '...RowStatus')
by this management agent implementation (ie, version) on this host system,
specified in a bit-mask. Usage: Conforming management agents SHALL accurately
report their support for IETF Host Resources MIB (RFC 2790) and XCMI Ext to
IETF Host Resources MIB object groups.
""")
_XcmHrGeneralUpdateSupport_Type = XcmHrGroupSupport
_XcmHrGeneralUpdateSupport_Object = MibTableColumn
xcmHrGeneralUpdateSupport = _XcmHrGeneralUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 9, 2, 1, 13),
    _XcmHrGeneralUpdateSupport_Type()
)
xcmHrGeneralUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrGeneralUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralUpdateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional IETF Host Resources MIB (RFC 2790) and XCMI Ext to IETF Host Resources
MIB objects which are supported for existing row update (via SNMP Set-Request
PDUs) by this management agent implementation (ie, version) on this host
system, specified in a bit-mask. Usage: Conforming management agents SHALL
accurately report their support for IETF Host Resources MIB (RFC 2790) and XCMI
Ext to IETF Host Resources MIB object groups.
""")
_XcmHrDevCalendar_ObjectIdentity = ObjectIdentity
xcmHrDevCalendar = _XcmHrDevCalendar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10)
)
_XcmHrDevCalendarTable_Object = MibTable
xcmHrDevCalendarTable = _XcmHrDevCalendarTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevCalendarTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarTable.setDescription("""\
A 'sparse' table containing calendar management objects for installed and
(possibly) active devices on this host system, augmenting the basic entries in
the 'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevCalendarEntry_Object = MibTableRow
xcmHrDevCalendarEntry = _XcmHrDevCalendarEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1)
)
xcmHrDevCalendarEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarDayOfWeek"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarTimeOfDay"),
)
if mibBuilder.loadTexts:
    xcmHrDevCalendarEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarEntry.setDescription("""\
A 'sparse' entry containing calendar management objects for an installed and
(possibly) active device on this host system, augmenting a basic entry in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevCalendarDayOfWeek_Type = XcmHrDevCalendarDayOfWeek
_XcmHrDevCalendarDayOfWeek_Object = MibTableColumn
xcmHrDevCalendarDayOfWeek = _XcmHrDevCalendarDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 1),
    _XcmHrDevCalendarDayOfWeek_Type()
)
xcmHrDevCalendarDayOfWeek.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDevCalendarDayOfWeek.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarDayOfWeek.setDescription("""\
The day of week when the command specified in this conceptual row in the
'xcmHrDevCalendarTable' SHALL be invoked.
""")
_XcmHrDevCalendarTimeOfDay_Type = XcmHrDevCalendarTimeOfDay
_XcmHrDevCalendarTimeOfDay_Object = MibTableColumn
xcmHrDevCalendarTimeOfDay = _XcmHrDevCalendarTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 2),
    _XcmHrDevCalendarTimeOfDay_Type()
)
xcmHrDevCalendarTimeOfDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDevCalendarTimeOfDay.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarTimeOfDay.setDescription("""\
The time of day when the command specified in this conceptual row in the
'xcmHrDevCalendarTable' SHALL be invoked, specified as hours (0..23) multiplied
by 100, added to minutes (0..59), added to a constant bias of 10000 (avoids an
index value of zero in 'xcmHrDevCalendarTimeOfDay').
""")
_XcmHrDevCalendarRowStatus_Type = RowStatus
_XcmHrDevCalendarRowStatus_Object = MibTableColumn
xcmHrDevCalendarRowStatus = _XcmHrDevCalendarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 3),
    _XcmHrDevCalendarRowStatus_Type()
)
xcmHrDevCalendarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCalendarRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevCalendarRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrDevCalendarTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmHrDevCalendarRowStatus' row status object; and SHALL clear the
'xcmHrDevCalendarGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrDevCalendarRowStatus' row status object; and SHALL set the
'xcmHrDevCalendarGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrDevCalendarExplicitDate_Type(DateAndTime):
    """Custom type xcmHrDevCalendarExplicitDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrDevCalendarExplicitDate_Object = MibTableColumn
xcmHrDevCalendarExplicitDate = _XcmHrDevCalendarExplicitDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 4),
    _XcmHrDevCalendarExplicitDate_Type()
)
xcmHrDevCalendarExplicitDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCalendarExplicitDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarExplicitDate.setDescription("""\
The explicit date when the command specified in this conceptual row in the
'xcmHrDevCalendarTable' SHALL be invoked. Usage: When
'xcmHrDevCalendarExplicitDate' is used, the value of
'xcmHrDevCalendarDayOfWeek' SHALL be 'everyDay' and the value of
'xcmHrDevCalendarTimeOfDay' SHALL be arbitrary (to provide uniqueness for this
conceptual row).
""")


class _XcmHrDevCalendarCommandRequest_Type(XcmHrDevMgmtCommandRequest):
    """Custom type xcmHrDevCalendarCommandRequest based on XcmHrDevMgmtCommandRequest"""


_XcmHrDevCalendarCommandRequest_Object = MibTableColumn
xcmHrDevCalendarCommandRequest = _XcmHrDevCalendarCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 5),
    _XcmHrDevCalendarCommandRequest_Type()
)
xcmHrDevCalendarCommandRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCalendarCommandRequest.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarCommandRequest.setReference("""\
See: 'hrDeviceStatus' in the Device group of the IETF Host Resources MIB (RFC
2790). See: 'xcmHrDevCalendarCommandData'
""")
if mibBuilder.loadTexts:
    xcmHrDevCalendarCommandRequest.setDescription("""\
The management command request specified in this conceptual row in the
'xcmHrDevCalendarTable', which SHALL be invoked based on
'xcmHrDevCalendarDayOfWeek', 'xcmHrDevCalendarTimeOfDay', and (optionally)
'xcmHrDevCalendarExplicitDate'.
""")


class _XcmHrDevCalendarCommandData_Type(XcmHrDevMgmtCommandData):
    """Custom type xcmHrDevCalendarCommandData based on XcmHrDevMgmtCommandData"""
    defaultHexValue = ""


_XcmHrDevCalendarCommandData_Object = MibTableColumn
xcmHrDevCalendarCommandData = _XcmHrDevCalendarCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 10, 2, 1, 6),
    _XcmHrDevCalendarCommandData_Type()
)
xcmHrDevCalendarCommandData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCalendarCommandData.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarCommandData.setReference("""\
See: Security Config, Account, and User groups in XCMI Security MIB. See:
Section 6.6 'Security in DPA' (pages 38 to 39) of DPA (ISO 10175-1 / Final
Text, March 1996). See: 'hrDeviceStatus' in the Device group of the IETF Host
Resources MIB (RFC 2790). See: 'xcmHrDevCalendarCommandRequest'
""")
if mibBuilder.loadTexts:
    xcmHrDevCalendarCommandData.setDescription("""\
The management command data specified in this conceptual row in the
'xcmHrDevCalendarTable', which SHALL be invoked based on
'xcmHrDevCalendarDayOfWeek', 'xcmHrDevCalendarTimeOfDay', and (optionally)
'xcmHrDevCalendarExplicitDate'. Usage: Conformant implementations MUST encrypt
passwords, keys, and other security information stored in this string object.
""")
_XcmHrSWRun_ObjectIdentity = ObjectIdentity
xcmHrSWRun = _XcmHrSWRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11)
)
_XcmHrSWRunTable_Object = MibTable
xcmHrSWRunTable = _XcmHrSWRunTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2)
)
if mibBuilder.loadTexts:
    xcmHrSWRunTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunTable.setDescription("""\
A 'sparse' table containing software info objects for loaded and (possibly)
active software on this host system, augmenting the basic entries in the
'hrSWRunTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrSWRunEntry_Object = MibTableRow
xcmHrSWRunEntry = _XcmHrSWRunEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1)
)
xcmHrSWRunEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrSWRunIndex"),
)
if mibBuilder.loadTexts:
    xcmHrSWRunEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunEntry.setDescription("""\
A 'sparse' entry containing software info objects for loaded and (possibly)
active software on this host system, augmenting a basic entry in the
'hrSWRunTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrSWRunRowStatus_Type = RowStatus
_XcmHrSWRunRowStatus_Object = MibTableColumn
xcmHrSWRunRowStatus = _XcmHrSWRunRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 1),
    _XcmHrSWRunRowStatus_Type()
)
xcmHrSWRunRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrSWRunRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrSWRunTable' and ALSO manages the row status of the associated conceptual
row in the 'hrSWRunTable' of the IETF Host Resources MIB. Usage: Conforming
implementations which support static rows SHALL support 'active' and
'notInService' writes to this 'xcmHrSWRunRowStatus' row status object; and
SHALL clear the 'xcmHrSWRunGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrSWRunRowStatus' row status object; and SHALL set the 'xcmHrSWRunGroup'
bit in 'xcmHrGeneralCreateSupport' in the 'xcmHrGeneralTable'. Usage:
Conforming implementations need NOT support dynamic row creation (via
'createAndGo(4)') nor dynamic row deletion (via 'destroy(6)'). Usage: See
section 3.4 'Secure Modes of Operation' and section 3.5 'Secure SNMP Get/Set
Requests' in XCMI Security TC, for details of secure modes of access to this
row status object.
""")


class _XcmHrSWRunAdminName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrSWRunAdminName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrSWRunAdminName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrSWRunAdminName_Object = MibTableColumn
xcmHrSWRunAdminName = _XcmHrSWRunAdminName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 2),
    _XcmHrSWRunAdminName_Type()
)
xcmHrSWRunAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunAdminName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunAdminName.setReference("""\
See: 'hrSWRunName' in the Software Running Group of the IETF Host Resources MIB
(RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrSWRunAdminName.setDescription("""\
Human-readable software name, used by system administrators and end users to
identify this software for systems management. Usage: This software name SHALL
be the one normally used in a CLI/GUI/API for control of this software. Note:
The 'hrSWRunName' object in 'hrSWRunTable' of the IETF Host Resources MIB (RFC
2790) has MANDATORY content of 'manufacturer, revision, and the name by which
[the software] is commonly known'. Thus, conforming implementations SHALL NOT
set a 'simple name' into 'hrSWRunName'. Therefore, this 'xcmHrSWRunAdminName'
object is needed for management.
""")
_XcmHrSWRunXStatus_Type = XcmHrSWRunXStatus
_XcmHrSWRunXStatus_Object = MibTableColumn
xcmHrSWRunXStatus = _XcmHrSWRunXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 3),
    _XcmHrSWRunXStatus_Type()
)
xcmHrSWRunXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSWRunXStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunXStatus.setReference("""\
See: 'hrSWRunStatus' in the Software Running Group of the IETF Host Resources
MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrSWRunXStatus.setDescription("""\
An extended software status, used by system administrators and end users of
this software (here, read 'state' for 'status'). Note: This extended software
status is present for future extensions.
""")


class _XcmHrSWRunRowCreateDate_Type(DateAndTime):
    """Custom type xcmHrSWRunRowCreateDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrSWRunRowCreateDate_Object = MibTableColumn
xcmHrSWRunRowCreateDate = _XcmHrSWRunRowCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 4),
    _XcmHrSWRunRowCreateDate_Type()
)
xcmHrSWRunRowCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSWRunRowCreateDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunRowCreateDate.setDescription("""\
The date and time when this conceptual row was created.
""")
_XcmHrSWRunPhysicalDeviceIndex_Type = Cardinal32
_XcmHrSWRunPhysicalDeviceIndex_Object = MibTableColumn
xcmHrSWRunPhysicalDeviceIndex = _XcmHrSWRunPhysicalDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 5),
    _XcmHrSWRunPhysicalDeviceIndex_Type()
)
xcmHrSWRunPhysicalDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunPhysicalDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunPhysicalDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790). See: Section 9.5.6 'Physical-printers-supported' of DPA (ISO 10175-1,
Final Text, March 1996).
""")
if mibBuilder.loadTexts:
    xcmHrSWRunPhysicalDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the first associated conceptual
row in the 'hrDeviceTable' representing a supported and (possibly) ready
'physical' device, which has 'xcmHrDevInfoRealization' of 'physical' or
'logicalAndPhysical', or zero, if there is no supported and subordinate
'physical' device associated with this row (ie, this running software).
""")
_XcmHrSWRunLogicalDeviceIndex_Type = Cardinal32
_XcmHrSWRunLogicalDeviceIndex_Object = MibTableColumn
xcmHrSWRunLogicalDeviceIndex = _XcmHrSWRunLogicalDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 6),
    _XcmHrSWRunLogicalDeviceIndex_Type()
)
xcmHrSWRunLogicalDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunLogicalDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunLogicalDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790). See: Section 9.5.8 'Logical-printers-supported' of DPA (ISO 10175-1,
Final Text, March 1996).
""")
if mibBuilder.loadTexts:
    xcmHrSWRunLogicalDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the first associated conceptual
row in the 'hrDeviceTable' representing a supported and (possibly) ready
'logical' device, which has 'xcmHrDevInfoRealization' of 'logical' or
'logicalAndPhysical', or zero, if there is no supported and subordinate
'logical' device associated with this row (ie, this running software).
""")
_XcmHrSWRunNextIndex_Type = Cardinal32
_XcmHrSWRunNextIndex_Object = MibTableColumn
xcmHrSWRunNextIndex = _XcmHrSWRunNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 7),
    _XcmHrSWRunNextIndex_Type()
)
xcmHrSWRunNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunNextIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunNextIndex.setDescription("""\
The value of 'hrSWRunIndex' corresponding to the next associated row in the
'hrSWRunTable', or zero if this is the last associated conceptual row in a
given set.
""")
_XcmHrSWRunPreviousIndex_Type = Cardinal32
_XcmHrSWRunPreviousIndex_Object = MibTableColumn
xcmHrSWRunPreviousIndex = _XcmHrSWRunPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 11, 2, 1, 8),
    _XcmHrSWRunPreviousIndex_Type()
)
xcmHrSWRunPreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWRunPreviousIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunPreviousIndex.setDescription("""\
The value of 'hrSWRunIndex' corresponding to the previous associated row in the
'hrSWRunTable', or zero if this is the first associated conceptual row in a
given set.
""")
_XcmHrSWInstalled_ObjectIdentity = ObjectIdentity
xcmHrSWInstalled = _XcmHrSWInstalled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12)
)
_XcmHrSWInstalledTable_Object = MibTable
xcmHrSWInstalledTable = _XcmHrSWInstalledTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2)
)
if mibBuilder.loadTexts:
    xcmHrSWInstalledTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledTable.setDescription("""\
A 'sparse' table containing software info objects for installed and (possibly)
active software on this host system, augmenting the basic entries in the
'hrSWInstalledTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrSWInstalledEntry_Object = MibTableRow
xcmHrSWInstalledEntry = _XcmHrSWInstalledEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1)
)
xcmHrSWInstalledEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrSWInstalledIndex"),
)
if mibBuilder.loadTexts:
    xcmHrSWInstalledEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledEntry.setDescription("""\
A 'sparse' entry containing software info objects for installed and (possibly)
active software on this host system, augmenting a basic entry in the
'hrSWInstalledTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrSWInstalledRowStatus_Type = RowStatus
_XcmHrSWInstalledRowStatus_Object = MibTableColumn
xcmHrSWInstalledRowStatus = _XcmHrSWInstalledRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 1),
    _XcmHrSWInstalledRowStatus_Type()
)
xcmHrSWInstalledRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrSWInstalledRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrSWInstalledTable' and ALSO manages the row status of the associated
conceptual row in the 'hrSWInstalledTable' of the IETF Host Resources MIB (RFC
2790). Usage: Conforming implementations which support static rows SHALL
support 'active' and 'notInService' writes to this 'xcmHrSWInstalledRowStatus'
row status object; and SHALL clear the 'xcmHrSWInstalledGroup' bit in
'xcmHrGeneralCreateSupport' in the 'xcmHrGeneralTable'. Usage: Conforming
implementations which support dynamic rows SHALL support 'createAndGo' and
'destroy' writes to this 'xcmHrSWInstalledRowStatus' row status object; and
SHALL set the 'xcmHrSWInstalledGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrSWInstalledAdminName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrSWInstalledAdminName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrSWInstalledAdminName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrSWInstalledAdminName_Object = MibTableColumn
xcmHrSWInstalledAdminName = _XcmHrSWInstalledAdminName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 2),
    _XcmHrSWInstalledAdminName_Type()
)
xcmHrSWInstalledAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledAdminName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledAdminName.setReference("""\
See: 'hrSWInstalledName' in the Software Installed Group of the IETF Host
Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrSWInstalledAdminName.setDescription("""\
Human-readable software name, used by system administrators and end users to
identify this software for systems management. Usage: This software name SHALL
be the one normally used in a CLI/GUI/API for control of this software. Note:
The 'hrSWInstalledName' object in 'hrSWInstalledTable' of the IETF Host
Resources MIB (RFC 2790) has MANDATORY content of 'manufacturer, revision, and
the name by which [the software] is commonly known'. Thus, conforming
implementations SHALL NOT set a 'simple name' into 'hrSWInstalledName'.
Therefore, this 'xcmHrSWInstalledAdminName' object is needed for management.
""")
_XcmHrSWInstalledXStatus_Type = XcmHrSWRunXStatus
_XcmHrSWInstalledXStatus_Object = MibTableColumn
xcmHrSWInstalledXStatus = _XcmHrSWInstalledXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 3),
    _XcmHrSWInstalledXStatus_Type()
)
xcmHrSWInstalledXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSWInstalledXStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledXStatus.setReference("""\
See: 'hrSWRunStatus' in the Software Running Group of the IETF Host Resources
MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrSWInstalledXStatus.setDescription("""\
An extended software status, used by system administrators and end users of
this software (here, read 'state' for 'status'). Note: This extended software
status is present for future extensions.
""")


class _XcmHrSWInstalledRowCreateDate_Type(DateAndTime):
    """Custom type xcmHrSWInstalledRowCreateDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrSWInstalledRowCreateDate_Object = MibTableColumn
xcmHrSWInstalledRowCreateDate = _XcmHrSWInstalledRowCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 4),
    _XcmHrSWInstalledRowCreateDate_Type()
)
xcmHrSWInstalledRowCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSWInstalledRowCreateDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledRowCreateDate.setDescription("""\
The date and time when this conceptual row was created.
""")
_XcmHrSWInstalledPhysicalIndex_Type = Cardinal32
_XcmHrSWInstalledPhysicalIndex_Object = MibTableColumn
xcmHrSWInstalledPhysicalIndex = _XcmHrSWInstalledPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 5),
    _XcmHrSWInstalledPhysicalIndex_Type()
)
xcmHrSWInstalledPhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledPhysicalIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledPhysicalIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790). See: Section 9.5.6 'Physical-printers-supported' of DPA (ISO 10175-1,
Final Text, March 1996).
""")
if mibBuilder.loadTexts:
    xcmHrSWInstalledPhysicalIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the first associated conceptual
row in the 'hrDeviceTable' representing a supported and (possibly) ready
'physical' device, which has 'xcmHrDevInfoRealization' of 'physical' or
'logicalAndPhysical', or zero, if there is no supported and subordinate
'physical' device associated with this row (ie, this installed software).
""")
_XcmHrSWInstalledLogicalIndex_Type = Cardinal32
_XcmHrSWInstalledLogicalIndex_Object = MibTableColumn
xcmHrSWInstalledLogicalIndex = _XcmHrSWInstalledLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 6),
    _XcmHrSWInstalledLogicalIndex_Type()
)
xcmHrSWInstalledLogicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledLogicalIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledLogicalIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790). See: Section 9.5.8 'Logical-printers-supported' of DPA (ISO 10175-1,
Final Text, March 1996).
""")
if mibBuilder.loadTexts:
    xcmHrSWInstalledLogicalIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the first associated conceptual
row in the 'hrDeviceTable' representing a supported and (possibly) ready
'logical' device, which has 'xcmHrDevInfoRealization' of 'logical' or
'logicalAndPhysical', or zero, if there is no supported and subordinate
'logical' device associated with this row (ie, this installed software).
""")
_XcmHrSWInstalledNextIndex_Type = Cardinal32
_XcmHrSWInstalledNextIndex_Object = MibTableColumn
xcmHrSWInstalledNextIndex = _XcmHrSWInstalledNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 7),
    _XcmHrSWInstalledNextIndex_Type()
)
xcmHrSWInstalledNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledNextIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledNextIndex.setDescription("""\
The value of 'hrSWInstalledIndex' corresponding to the next associated row in
the 'hrSWInstalledTable', or zero if this is the last associated conceptual row
in a given set.
""")
_XcmHrSWInstalledPreviousIndex_Type = Cardinal32
_XcmHrSWInstalledPreviousIndex_Object = MibTableColumn
xcmHrSWInstalledPreviousIndex = _XcmHrSWInstalledPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 12, 2, 1, 8),
    _XcmHrSWInstalledPreviousIndex_Type()
)
xcmHrSWInstalledPreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrSWInstalledPreviousIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledPreviousIndex.setDescription("""\
The value of 'hrSWInstalledIndex' corresponding to the previous associated row
in the 'hrSWInstalledTable', or zero if this is the first associated conceptual
row in a given set.
""")
_XcmHrDevDetail_ObjectIdentity = ObjectIdentity
xcmHrDevDetail = _XcmHrDevDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13)
)
_XcmHrDevDetailV1EventOID_ObjectIdentity = ObjectIdentity
xcmHrDevDetailV1EventOID = _XcmHrDevDetailV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 1)
)
if mibBuilder.loadTexts:
    xcmHrDevDetailV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever a
device detail usage or time limit is reached. See SNMPv2 trap definition
'xcmHrDevDetailV2Event' below for 'special semantics'.
""")
_XcmHrDevDetailV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmHrDevDetailV2EventPrefix = _XcmHrDevDetailV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 1, 0)
)
_XcmHrDevDetailTable_Object = MibTable
xcmHrDevDetailTable = _XcmHrDevDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevDetailTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailTable.setReference("""\
See: 'hrProcessorTable', 'hrNetworkTable', 'hrPrinterTable' in the IETF Host
Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevDetailTable.setDescription("""\
A 'sparse' table containing device detail information for installed and
(possibly) active devices on this host system, augmenting the basic entries in
the 'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790). Usage: UNLIKE
the 'xcmGenOptionTable' in the XCMI General MIB (which is a unique exception),
this table of 'dictionary-based' device details is used with DIRECT
create/update operations.
""")
_XcmHrDevDetailEntry_Object = MibTableRow
xcmHrDevDetailEntry = _XcmHrDevDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1)
)
xcmHrDevDetailEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailType"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevDetailEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailEntry.setDescription("""\
A 'sparse' entry containing device detail information for an installed and
(possibly) active device on this host system, augmenting a basic entry in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790). Usage: An entry in
this table MAY be used to store specialized information for a device, such as
'lifetime' information for a CRU ('customer replaceable unit'), eg, a paper
tray feed head.
""")
_XcmHrDevDetailType_Type = XcmHrDevDetailType
_XcmHrDevDetailType_Object = MibTableColumn
xcmHrDevDetailType = _XcmHrDevDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 1),
    _XcmHrDevDetailType_Type()
)
xcmHrDevDetailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevDetailType.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailType.setDescription("""\
The type of the device detail information specified in this conceptual row in
the 'xcmHrDevDetailTable'.
""")
_XcmHrDevDetailIndex_Type = Ordinal32
_XcmHrDevDetailIndex_Object = MibTableColumn
xcmHrDevDetailIndex = _XcmHrDevDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 2),
    _XcmHrDevDetailIndex_Type()
)
xcmHrDevDetailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevDetailIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrDevDetailTable', OR a common value shared across a set of related
conceptual rows (with different values of 'xcmHrDevDetailType'. Usage: For
device detail types which are single-valued, this index SHALL be used to
correlate related single-valued details. Usage: For device detail types which
are multi-valued, this index SHALL be used to enumerate lists of multi-valued
details.
""")
_XcmHrDevDetailRowStatus_Type = RowStatus
_XcmHrDevDetailRowStatus_Object = MibTableColumn
xcmHrDevDetailRowStatus = _XcmHrDevDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 3),
    _XcmHrDevDetailRowStatus_Type()
)
xcmHrDevDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevDetailRowStatus.setDescription("""\
This object manages the row status of this conceptual row in in the
'xcmHrDevDetailTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmHrDevDetailRowStatus' row status object; and SHALL clear the
'xcmHrDevDetailGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrDevDetailRowStatus' row status object; and SHALL set the
'xcmHrDevDetailGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrDevDetailUnitClass_Type(XcmHrDevDetailUnitClass):
    """Custom type xcmHrDevDetailUnitClass based on XcmHrDevDetailUnitClass"""


_XcmHrDevDetailUnitClass_Object = MibTableColumn
xcmHrDevDetailUnitClass = _XcmHrDevDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 4),
    _XcmHrDevDetailUnitClass_Type()
)
xcmHrDevDetailUnitClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailUnitClass.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailUnitClass.setReference("""\
See: 'xcmHrDevDetailUnit'
""")
if mibBuilder.loadTexts:
    xcmHrDevDetailUnitClass.setDescription("""\
The value unit class of the detail information specified in this conceptual row
in the 'xcmHrDevDetailTable'. Usage: Used to select a textual convention for
specifying the value unit of this device detail. Usage: The
'xcmHrDevDetail[UnitClass|Class]' objects are used to specify the value syntax
AND the value unit of the 'xcmHrDevDetail[Integer|OID|String]' value objects.
""")
_XcmHrDevDetailUnit_Type = Cardinal32
_XcmHrDevDetailUnit_Object = MibTableColumn
xcmHrDevDetailUnit = _XcmHrDevDetailUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 5),
    _XcmHrDevDetailUnit_Type()
)
xcmHrDevDetailUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailUnit.setReference("""\
See: 'xcmHrDevDetailUnitClass'
""")
if mibBuilder.loadTexts:
    xcmHrDevDetailUnit.setDescription("""\
The value unit of the detail information specified in this conceptual row in
the 'xcmHrDevDetailTable'. Usage: Used to select an enumerated choice from a
textual convention to specify the value unit of this device detail. Usage: The
'xcmHrDevDetail[UnitClass|Class]' objects are used to specify the value syntax
AND the value unit of the 'xcmHrDevDetail[Integer|OID|String]' value objects.
""")
_XcmHrDevDetailValueInteger_Type = Integer32
_XcmHrDevDetailValueInteger_Object = MibTableColumn
xcmHrDevDetailValueInteger = _XcmHrDevDetailValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 6),
    _XcmHrDevDetailValueInteger_Type()
)
xcmHrDevDetailValueInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueInteger.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueInteger.setReference("""\
See: 'xcmHrDevDetailValueOID' and 'xcmHrDevDetailValueString' See:
'xcmHrDevDetailUnitClass' and 'xcmHrDevDetailUnit' for syntax of detail value
""")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueInteger.setDescription("""\
A device detail value integer, used by system administrators and end users to
specify the current value for a device detail with a base value syntax of
'INTEGER'.
""")


class _XcmHrDevDetailValueOID_Type(ObjectIdentifier):
    """Custom type xcmHrDevDetailValueOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmHrDevDetailValueOID_Object = MibTableColumn
xcmHrDevDetailValueOID = _XcmHrDevDetailValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 7),
    _XcmHrDevDetailValueOID_Type()
)
xcmHrDevDetailValueOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueOID.setReference("""\
See: 'xcmHrDevDetailValueInteger' and 'xcmHrDevDetailValueString' See:
'xcmHrDevDetailUnitClass' and 'xcmHrDevDetailUnit' for syntax of detail value
""")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueOID.setDescription("""\
A device detail value OID (object identifier), used by system administrators
and end users to specify the current value for a device detail with a base
value syntax of 'OBJECT IDENTIFIER'.
""")


class _XcmHrDevDetailValueString_Type(OctetString):
    """Custom type xcmHrDevDetailValueString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevDetailValueString_Type.__name__ = "OctetString"
_XcmHrDevDetailValueString_Object = MibTableColumn
xcmHrDevDetailValueString = _XcmHrDevDetailValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 8),
    _XcmHrDevDetailValueString_Type()
)
xcmHrDevDetailValueString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueString.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueString.setReference("""\
See: 'xcmHrDevDetailValueInteger' and 'xcmHrDevDetailValueOID' See:
'xcmHrDevDetailUnitClass' and 'xcmHrDevDetailUnit' for syntax of detail value
""")
if mibBuilder.loadTexts:
    xcmHrDevDetailValueString.setDescription("""\
A device detail value string, used by system administrators and end users to
specify the current value for a device detail with a base value syntax of
'OCTET STRING'. Usage: This object is of type 'XcmFixedLocaleDisplayString'.
Usage: Conformant implementations MUST encrypt passwords, keys, and other
security information stored in this string object.
""")


class _XcmHrDevDetailDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevDetailDescription based on XcmFixedLocaleDisplayString"""
    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevDetailDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevDetailDescription_Object = MibTableColumn
xcmHrDevDetailDescription = _XcmHrDevDetailDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 2, 1, 9),
    _XcmHrDevDetailDescription_Type()
)
xcmHrDevDetailDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevDetailDescription.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailDescription.setDescription("""\
This object is used to provide a description of the detail. It is NOT expected
to be parsed by the management application.
""")
_XcmHrStorage_ObjectIdentity = ObjectIdentity
xcmHrStorage = _XcmHrStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14)
)
_XcmHrStorageTable_Object = MibTable
xcmHrStorageTable = _XcmHrStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2)
)
if mibBuilder.loadTexts:
    xcmHrStorageTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageTable.setDescription("""\
A 'sparse' table containing storage info objects for 'logical' or 'physical'
storage elements on this host system, augmenting the basic entries in the
'hrStorageTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrStorageEntry_Object = MibTableRow
xcmHrStorageEntry = _XcmHrStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1)
)
xcmHrStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrStorageIndex"),
)
if mibBuilder.loadTexts:
    xcmHrStorageEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageEntry.setDescription("""\
A 'sparse' entry containing storage info objects for a 'logical' or 'physical'
storage element on this host system, augmenting a basic entry in the
'hrStorageTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrStorageRowStatus_Type = RowStatus
_XcmHrStorageRowStatus_Object = MibTableColumn
xcmHrStorageRowStatus = _XcmHrStorageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 1),
    _XcmHrStorageRowStatus_Type()
)
xcmHrStorageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrStorageRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrStorageTable' and ALSO manages the row status of the associated
conceptual row in the 'hrStorageTable' of the IETF Host Resources MIB (RFC
2790). Usage: Conforming implementations which support static rows SHALL
support 'active' and 'notInService' writes to this 'xcmHrStorageRowStatus' row
status object; and SHALL clear the 'xcmHrStorageGroup' bit in
'xcmHrGeneralCreateSupport' in the 'xcmHrGeneralTable'. Usage: Conforming
implementations which support dynamic rows SHALL support 'createAndGo' and
'destroy' writes to this 'xcmHrStorageRowStatus' row status object; and SHALL
set the 'xcmHrStorageGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrStorageRealization_Type(XcmHrStorageRealization):
    """Custom type xcmHrStorageRealization based on XcmHrStorageRealization"""


_XcmHrStorageRealization_Object = MibTableColumn
xcmHrStorageRealization = _XcmHrStorageRealization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 2),
    _XcmHrStorageRealization_Type()
)
xcmHrStorageRealization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageRealization.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageRealization.setReference("""\
See: 'XcmHrDevInfoRealization' textual convention in the XCMI Ext to Host
Resources TC. See: 'xcmHrDevInfoRealization' in the Device Info group of the
XCMI Ext to Host Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmHrStorageRealization.setDescription("""\
An extended storage type (or storage 'realization'), used by system
administrators and end users of this storage. Usage: The use of either 'other'
or 'unknown' is uninformative and SHOULD be avoided by conforming
implementations.
""")


class _XcmHrStorageStatus_Type(XcmHrDevInfoStatus):
    """Custom type xcmHrStorageStatus based on XcmHrDevInfoStatus"""


_XcmHrStorageStatus_Object = MibTableColumn
xcmHrStorageStatus = _XcmHrStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 3),
    _XcmHrStorageStatus_Type()
)
xcmHrStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrStorageStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageStatus.setReference("""\
See: 'XcmHrDevInfoStatus' textual convention in the XCMI Ext to Host Resources
TC. See: 'hrDeviceStatus' in the Device group of the IETF Host Resources MIB
(RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrStorageStatus.setDescription("""\
A storage status, used by system administrators and end users of this storage
(here, read 'state' for 'status'). Usage: Conforming implementations SHALL NOT
'bubble up' status from 'physical' storage to associated 'logical' storage. All
storage SHALL report its own status ONLY.
""")
_XcmHrStorageProductDeviceIndex_Type = Cardinal32
_XcmHrStorageProductDeviceIndex_Object = MibTableColumn
xcmHrStorageProductDeviceIndex = _XcmHrStorageProductDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 4),
    _XcmHrStorageProductDeviceIndex_Type()
)
xcmHrStorageProductDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageProductDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageProductDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrStorageProductDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the product associated conceptual
row in the 'hrDeviceTable' representing the product (container) device (eg, of
type 'hrDevicePrinter'), which uses this storage.
""")
_XcmHrStoragePlatformDeviceIndex_Type = Cardinal32
_XcmHrStoragePlatformDeviceIndex_Object = MibTableColumn
xcmHrStoragePlatformDeviceIndex = _XcmHrStoragePlatformDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 5),
    _XcmHrStoragePlatformDeviceIndex_Type()
)
xcmHrStoragePlatformDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStoragePlatformDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStoragePlatformDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrStoragePlatformDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the platform associated
conceptual row in the 'hrDeviceTable' representing the CPU device (of type
'hrDeviceProcessor'), which manages this storage.
""")
_XcmHrStoragePagingDeviceIndex_Type = Cardinal32
_XcmHrStoragePagingDeviceIndex_Object = MibTableColumn
xcmHrStoragePagingDeviceIndex = _XcmHrStoragePagingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 6),
    _XcmHrStoragePagingDeviceIndex_Type()
)
xcmHrStoragePagingDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStoragePagingDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStoragePagingDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790). See: 'storagePageSize' in the 'XcmHrStorageDetailType' textual
convention in the XCMI Ext to Host Resources TC.
""")
if mibBuilder.loadTexts:
    xcmHrStoragePagingDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the paging associated conceptual
row in the 'hrDeviceTable' representing the paging device (usually of type
'hrDeviceDiskStorage'), which provides secondary storage for swapping of this
storage.
""")
_XcmHrStorageMatchingDeviceIndex_Type = Cardinal32
_XcmHrStorageMatchingDeviceIndex_Object = MibTableColumn
xcmHrStorageMatchingDeviceIndex = _XcmHrStorageMatchingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 7),
    _XcmHrStorageMatchingDeviceIndex_Type()
)
xcmHrStorageMatchingDeviceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageMatchingDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageMatchingDeviceIndex.setReference("""\
See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrStorageMatchingDeviceIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the matching associated
conceptual row in the 'hrDeviceTable' representing the matching device (eg, of
type 'hrDeviceDiskStorage'), which corresponds to this storage.
""")
_XcmHrStorageSWRunIndex_Type = Cardinal32
_XcmHrStorageSWRunIndex_Object = MibTableColumn
xcmHrStorageSWRunIndex = _XcmHrStorageSWRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 8),
    _XcmHrStorageSWRunIndex_Type()
)
xcmHrStorageSWRunIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageSWRunIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageSWRunIndex.setReference("""\
See: 'hrSWRunIndex' in the Software Running group of the IETF Host Resources
MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrStorageSWRunIndex.setDescription("""\
The value of 'hrSWRunIndex' corresponding to the superior associated conceptual
row in the 'hrSWRunTable' representing the running software which manages this
storage.
""")
_XcmHrStorageSWInstalledIndex_Type = Cardinal32
_XcmHrStorageSWInstalledIndex_Object = MibTableColumn
xcmHrStorageSWInstalledIndex = _XcmHrStorageSWInstalledIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 9),
    _XcmHrStorageSWInstalledIndex_Type()
)
xcmHrStorageSWInstalledIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageSWInstalledIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageSWInstalledIndex.setReference("""\
See: 'hrSWInstalledIndex' in the Software Installed group of the IETF Host
Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrStorageSWInstalledIndex.setDescription("""\
The value of 'hrSWInstalledIndex' corresponding to the superior associated
conceptual row in the 'hrSWInstalledTable' representing the installed software
which manages this storage.
""")
_XcmHrStorageNextIndex_Type = Cardinal32
_XcmHrStorageNextIndex_Object = MibTableColumn
xcmHrStorageNextIndex = _XcmHrStorageNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 10),
    _XcmHrStorageNextIndex_Type()
)
xcmHrStorageNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageNextIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageNextIndex.setReference("""\
See: 'hrStorageIndex' in the Storage group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrStorageNextIndex.setDescription("""\
The value of 'hrStorageIndex' corresponding to: a) the next associated row in
the 'hrStorageTable'; or b) zero if this is the last associated conceptual row
in a given set; or c) zero if this conceptual row is NOT part of a set.
""")
_XcmHrStoragePreviousIndex_Type = Cardinal32
_XcmHrStoragePreviousIndex_Object = MibTableColumn
xcmHrStoragePreviousIndex = _XcmHrStoragePreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 11),
    _XcmHrStoragePreviousIndex_Type()
)
xcmHrStoragePreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStoragePreviousIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStoragePreviousIndex.setReference("""\
See: 'hrStorageIndex' in the Storage group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrStoragePreviousIndex.setDescription("""\
The value of 'hrStorageIndex' corresponding to: a) the previous associated row
in the 'hrStorageTable'; or b) zero if this is the first associated conceptual
row in a given set; or c) zero if this conceptual row is NOT part of a set.
""")
_XcmHrStoragePhysicalIndex_Type = Cardinal32
_XcmHrStoragePhysicalIndex_Object = MibTableColumn
xcmHrStoragePhysicalIndex = _XcmHrStoragePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 14, 2, 1, 12),
    _XcmHrStoragePhysicalIndex_Type()
)
xcmHrStoragePhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStoragePhysicalIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStoragePhysicalIndex.setReference("""\
See: 'hrStorageIndex' in the Storage group of the IETF Host Resources MIB (RFC
2790).
""")
if mibBuilder.loadTexts:
    xcmHrStoragePhysicalIndex.setDescription("""\
The value of 'hrStorageIndex' corresponding to the directly associated
conceptual row in the 'hrStorageTable' representing: a) the first underlying
'physical' storage (if any), if this row has 'xcmHrStorageRealization' of
'logical...'; or b) the first subordinate 'physical' storage (if any), if this
row has 'xcmHrStorageRealization' of 'physical...'; or c) zero if there is no
underlying or subordinate 'physical' storage associated with this row (ie, this
storage).
""")
_XcmHrStorageDetail_ObjectIdentity = ObjectIdentity
xcmHrStorageDetail = _XcmHrStorageDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15)
)
_XcmHrStorageDetailTable_Object = MibTable
xcmHrStorageDetailTable = _XcmHrStorageDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2)
)
if mibBuilder.loadTexts:
    xcmHrStorageDetailTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailTable.setDescription("""\
A 'sparse' table containing storage detail information for 'logical' or
'physical' storage elements on this host system, augmenting a basic entry in
the 'hrStorageTable' of the IETF Host Resources MIB (RFC 2790). Usage: UNLIKE
the 'xcmGenOptionTable' in the XCMI General MIB (which is a unique exception),
this table of 'dictionary-based' storage details is used with DIRECT
create/update operations.
""")
_XcmHrStorageDetailEntry_Object = MibTableRow
xcmHrStorageDetailEntry = _XcmHrStorageDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1)
)
xcmHrStorageDetailEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrStorageIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailType"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmHrStorageDetailEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailEntry.setDescription("""\
A 'sparse' entry containing storage detail information for a 'logical' or
'physical' storage element on this host system, augmenting a basic entry in the
'hrStorageTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrStorageDetailType_Type = XcmHrStorageDetailType
_XcmHrStorageDetailType_Object = MibTableColumn
xcmHrStorageDetailType = _XcmHrStorageDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 1),
    _XcmHrStorageDetailType_Type()
)
xcmHrStorageDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrStorageDetailType.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailType.setDescription("""\
The type of the storage detail information specified in this conceptual row in
the 'xcmHrStorageDetailTable'.
""")
_XcmHrStorageDetailIndex_Type = Ordinal32
_XcmHrStorageDetailIndex_Object = MibTableColumn
xcmHrStorageDetailIndex = _XcmHrStorageDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 2),
    _XcmHrStorageDetailIndex_Type()
)
xcmHrStorageDetailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrStorageDetailIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrStorageDetailTable', OR a common value shared across a set of related
conceptual rows (with different values of 'xcmHrStorageDetailType'. Usage: For
storage detail types which are single-valued, this index SHALL be used to
correlate related single-valued details. Usage: For storage detail types which
are multi-valued, this index SHALL be used to enumerate lists of multi-valued
details.
""")
_XcmHrStorageDetailRowStatus_Type = RowStatus
_XcmHrStorageDetailRowStatus_Object = MibTableColumn
xcmHrStorageDetailRowStatus = _XcmHrStorageDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 3),
    _XcmHrStorageDetailRowStatus_Type()
)
xcmHrStorageDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrStorageDetailRowStatus.setDescription("""\
This object manages the row status of this conceptual row in in the
'xcmHrStorageDetailTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmHrStorageDetailRowStatus' row status object; and SHALL clear the
'xcmHrStorageDetailGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrStorageDetailRowStatus' row status object; and SHALL set the
'xcmHrStorageDetailGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrStorageDetailUnitClass_Type(XcmHrDevDetailUnitClass):
    """Custom type xcmHrStorageDetailUnitClass based on XcmHrDevDetailUnitClass"""


_XcmHrStorageDetailUnitClass_Object = MibTableColumn
xcmHrStorageDetailUnitClass = _XcmHrStorageDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 4),
    _XcmHrStorageDetailUnitClass_Type()
)
xcmHrStorageDetailUnitClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailUnitClass.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailUnitClass.setReference("""\
See: 'xcmHrStorageDetailUnit'
""")
if mibBuilder.loadTexts:
    xcmHrStorageDetailUnitClass.setDescription("""\
The value unit class of the detail information specified in this conceptual row
in the 'xcmHrStorageDetailTable'. Usage: Used to select a textual convention
for specifying the value unit of this storage detail. Usage: The
'xcmHrStorageDetail[UnitClass|Class]' objects are used to specify the value
syntax AND the value unit of the 'xcmHrStorageDetail[Integer|OID|String]' value
objects.
""")
_XcmHrStorageDetailUnit_Type = Cardinal32
_XcmHrStorageDetailUnit_Object = MibTableColumn
xcmHrStorageDetailUnit = _XcmHrStorageDetailUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 5),
    _XcmHrStorageDetailUnit_Type()
)
xcmHrStorageDetailUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailUnit.setReference("""\
See: 'xcmHrStorageDetailUnitClass'
""")
if mibBuilder.loadTexts:
    xcmHrStorageDetailUnit.setDescription("""\
The value unit of the detail information specified in this conceptual row in
the 'xcmHrStorageDetailTable'. Usage: Used to select an enumerated choice from
a textual convention to specify the value unit of this storage detail. Usage:
The 'xcmHrStorageDetail[UnitClass|Class]' objects are used to specify the value
syntax AND the value unit of the 'xcmHrStorageDetail[Integer|OID|String]' value
objects.
""")
_XcmHrStorageDetailValueInteger_Type = Integer32
_XcmHrStorageDetailValueInteger_Object = MibTableColumn
xcmHrStorageDetailValueInteger = _XcmHrStorageDetailValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 6),
    _XcmHrStorageDetailValueInteger_Type()
)
xcmHrStorageDetailValueInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueInteger.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueInteger.setReference("""\
See: 'xcmHrStorageDetailValueOID' and 'xcmHrStorageDetailValueString' See:
'xcmHrStorageDetailUnitClass' and 'xcmHrStorageDetailUnit' for syntax of detail
value
""")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueInteger.setDescription("""\
A storage detail value integer, used by system administrators and end users to
specify the current value for a storage detail with a base value syntax of
'INTEGER'.
""")


class _XcmHrStorageDetailValueOID_Type(ObjectIdentifier):
    """Custom type xcmHrStorageDetailValueOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmHrStorageDetailValueOID_Object = MibTableColumn
xcmHrStorageDetailValueOID = _XcmHrStorageDetailValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 7),
    _XcmHrStorageDetailValueOID_Type()
)
xcmHrStorageDetailValueOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueOID.setReference("""\
See: 'xcmHrStorageDetailValueInteger' and 'xcmHrStorageDetailValueString' See:
'xcmHrStorageDetailUnitClass' and 'xcmHrStorageDetailUnit' for syntax of detail
value
""")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueOID.setDescription("""\
A storage detail value OID (object identifier), used by system administrators
and end users to specify the current value for a storage detail with a base
value syntax of 'OBJECT IDENTIFIER'.
""")


class _XcmHrStorageDetailValueString_Type(OctetString):
    """Custom type xcmHrStorageDetailValueString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrStorageDetailValueString_Type.__name__ = "OctetString"
_XcmHrStorageDetailValueString_Object = MibTableColumn
xcmHrStorageDetailValueString = _XcmHrStorageDetailValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 15, 2, 1, 8),
    _XcmHrStorageDetailValueString_Type()
)
xcmHrStorageDetailValueString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueString.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueString.setReference("""\
See: 'xcmHrStorageDetailValueInteger' and 'xcmHrStorageDetailValueOID' See:
'xcmHrStorageDetailUnitClass' and 'xcmHrStorageDetailUnit' for syntax of detail
value
""")
if mibBuilder.loadTexts:
    xcmHrStorageDetailValueString.setDescription("""\
A storage detail value string, used by system administrators and end users to
specify the current value for a storage detail with a base value syntax of
'OCTET STRING'. Usage: This object is of type 'XcmFixedLocaleDisplayString'.
Usage: Conformant implementations MUST encrypt passwords, keys, and other
security information stored in this string object.
""")
_XcmHrDevCover_ObjectIdentity = ObjectIdentity
xcmHrDevCover = _XcmHrDevCover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16)
)
_XcmHrDevCoverTable_Object = MibTable
xcmHrDevCoverTable = _XcmHrDevCoverTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevCoverTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverTable.setReference("""\
See: 'prtCoverTable' in the Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevCoverTable.setDescription("""\
A 'sparse' table containing cover and/or interlock info for installed and
(possibly) active devices on this host system, augmenting the basic entries in
the 'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevCoverEntry_Object = MibTableRow
xcmHrDevCoverEntry = _XcmHrDevCoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1)
)
xcmHrDevCoverEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevCoverEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverEntry.setDescription("""\
A 'sparse' entry containing cover and/or interlock info for an installed and
(possibly) active device on this host system, augmenting a basic entry in the
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790).
""")
_XcmHrDevCoverIndex_Type = Ordinal32
_XcmHrDevCoverIndex_Object = MibTableColumn
xcmHrDevCoverIndex = _XcmHrDevCoverIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 1),
    _XcmHrDevCoverIndex_Type()
)
xcmHrDevCoverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDevCoverIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrDevCoverTable'.
""")
_XcmHrDevCoverRowStatus_Type = RowStatus
_XcmHrDevCoverRowStatus_Object = MibTableColumn
xcmHrDevCoverRowStatus = _XcmHrDevCoverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 2),
    _XcmHrDevCoverRowStatus_Type()
)
xcmHrDevCoverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevCoverRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmHrDevCoverTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmHrDevCoverRowStatus' row status object; and SHALL clear the
'xcmHrDevCoverGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmHrDevCoverRowStatus' row status object; and SHALL set the
'xcmHrDevCoverGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations need NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmHrDevCoverName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevCoverName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevCoverName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevCoverName_Object = MibTableColumn
xcmHrDevCoverName = _XcmHrDevCoverName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 3),
    _XcmHrDevCoverName_Type()
)
xcmHrDevCoverName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverName.setReference("""\
See: 'xcmHrDevCoverDescription' (below). See: 'prtCoverDescription' in the
Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevCoverName.setDescription("""\
Human-readable name of this device cover or interlock specified in this
conceptual row in the 'xcmHrDevCoverTable'. Usage: This name SHALL be locally
unambiguous (if specified) on this managed host system and SHALL be the one
normally used in a CLI/GUI/API for identification of this device cover or
interlock (eg, 'Cover1'). Usage: The the Printer MIB combines the name of a
device cover or device interlock with the description, in one object -
'xcmHrDevCover[Name|Description]' add clarity.
""")


class _XcmHrDevCoverDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevCoverDescription based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevCoverDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevCoverDescription_Object = MibTableColumn
xcmHrDevCoverDescription = _XcmHrDevCoverDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 4),
    _XcmHrDevCoverDescription_Type()
)
xcmHrDevCoverDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverDescription.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverDescription.setReference("""\
See: 'xcmHrDevCoverName' (above). See: 'prtCoverDescription' in the Printer
MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevCoverDescription.setDescription("""\
Human-readable description of this device cover or interlock specified in this
conceptual row in the 'xcmHrDevCoverTable'. Usage: This description MAY contain
the manufacturer's name, the color, the physical location, etc, of this device
cover or interlock (eg, 'Top front blue cover'). Usage: The the Printer MIB
combines the name of a device cover or device interlock with the description,
in one object - 'xcmHrDevCover[Name|Description]' add clarity.
""")


class _XcmHrDevCoverTypeCover_Type(TruthValue):
    """Custom type xcmHrDevCoverTypeCover based on TruthValue"""


_XcmHrDevCoverTypeCover_Object = MibTableColumn
xcmHrDevCoverTypeCover = _XcmHrDevCoverTypeCover_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 5),
    _XcmHrDevCoverTypeCover_Type()
)
xcmHrDevCoverTypeCover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverTypeCover.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverTypeCover.setReference("""\
See: 'xcmHrDevCoverStatusOpen' (below). See: 'prtCoverStatus' in the Printer
MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevCoverTypeCover.setDescription("""\
The type of the device cover or interlock specified in this conceptual row in
the 'xcmHrDevCoverTable'. * 'true' - this is a device cover conceptual row; *
'false' - this is a device interlock conceptual row. Usage: The the Printer MIB
combines the identity of cover versus interlock with the status of open versus
closed, in one object - 'xcmHrDevCover[TypeCover|StatusOpen]' add clarity.
""")


class _XcmHrDevCoverStatusOpen_Type(TruthValue):
    """Custom type xcmHrDevCoverStatusOpen based on TruthValue"""


_XcmHrDevCoverStatusOpen_Object = MibTableColumn
xcmHrDevCoverStatusOpen = _XcmHrDevCoverStatusOpen_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 16, 2, 1, 6),
    _XcmHrDevCoverStatusOpen_Type()
)
xcmHrDevCoverStatusOpen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevCoverStatusOpen.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverStatusOpen.setReference("""\
See: 'xcmHrDevCoverTypeCover' (above). See: 'prtCoverStatus' in the Printer
MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevCoverStatusOpen.setDescription("""\
The status of the device cover or interlock specified in this conceptual row in
the 'xcmHrDevCoverTable'. * 'true' - this cover/interlock is currently open; *
'false' - this cover/interlock is currently closed. Usage: The the Printer MIB
combines the choice of cover versus interlock with the status of open versus
closed, in one object - 'xcmHrDevCover[TypeCover|StatusOpen]' add clarity.
""")
_XcmHrDevAlert_ObjectIdentity = ObjectIdentity
xcmHrDevAlert = _XcmHrDevAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17)
)
_XcmHrDevAlertV1EventOID_ObjectIdentity = ObjectIdentity
xcmHrDevAlertV1EventOID = _XcmHrDevAlertV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 1)
)
if mibBuilder.loadTexts:
    xcmHrDevAlertV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever a
device alert row transitions to 'active' row status or (optionally) transitions
to 'notInService' row status in 'xcmHrDevAlertTable'. See SNMPv2 trap
definition 'xcmHrDevAlertV2Event' below for 'special semantics'.
""")
_XcmHrDevAlertV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmHrDevAlertV2EventPrefix = _XcmHrDevAlertV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 1, 0)
)
_XcmHrDevAlertTable_Object = MibTable
xcmHrDevAlertTable = _XcmHrDevAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2)
)
if mibBuilder.loadTexts:
    xcmHrDevAlertTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertTable.setReference("""\
See: 'prtAlertTable' in the Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertTable.setDescription("""\
A table of the device alerts which have been generated and recorded on this
host system. Certain devices can be associated with specific alert tables
defined industry wide for the specific device. This general alert table is
designed to work with these other alert tables. At this time, the only device
specific alert table is prtAlertTable in the printer MIB. See
xcmHrDevAlertCodeInteger and xcmHrDevAlertDevAlertIndex for connections to the
device specific alert table. Usage: Conforming implementations SHALL ensure
that this table contains (up to) a product-specific number of the most 'recent'
device alerts on this host system. Usage: When an event occurs that should be
reported through the Alert table, the implementation SHALL create an alert for
each device impacted by the event. This SHOULD include all logical devices
containing the impacted device. All such alerts SHALL have the same index
'xcmHrDevAlertIndex.' Usage: If the hrDeviceIndex is an hrDevicePrinter, then
the product SHALL also generate an alert in the IETF 'prtAlertTable.' The index
'prtAlertIndex' for the associated printer alert table entry SHALL be returned
in 'xcmHrDevAlertDevAlertIndex' for the 'hrDevicePrinter' index. Management
tools can use the value of 'xcmHrDevAlertDevAlertIndex' to associate printer
alerts with alerts in this table. Usage: Conforming implementations which also
implement the System Fault group SHALL record in 'xcmHrSystemFaultTable' each
persistent system fault when it occurs and is recorded in 'xcmHrDevAlertTable'.
Usage: Conforming implementations MAY 'age' older entries out of
'xcmHrDevAlertTable' based on algorithms which depend on the age of the entry
and the particular alert. When the number of alerts in the table exceeds the
product-specific maximum number of alerts, the oldest non-critical alert SHALL
be removed. If there are no non-critical alerts, then the oldest critical alert
SHALL be removed.
""")
_XcmHrDevAlertEntry_Object = MibTableRow
xcmHrDevAlertEntry = _XcmHrDevAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1)
)
xcmHrDevAlertEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDevAlertEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertEntry.setReference("""\
See: 'prtAlertEntry' in the Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertEntry.setDescription("""\
An entry for a device alert which has been generated and recorded on this host
system.
""")
_XcmHrDevAlertIndex_Type = Ordinal32
_XcmHrDevAlertIndex_Object = MibTableColumn
xcmHrDevAlertIndex = _XcmHrDevAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 1),
    _XcmHrDevAlertIndex_Type()
)
xcmHrDevAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDevAlertIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrDevAlertTable'. Usage: Conforming implementations SHALL NOT 'reuse'
values of 'xcmHrDevAlertIndex' until its' 32-bit value wraps. Even in the case
of eventual wrap, the entries SHALL be strictly sequenced by the associated
value of 'xcmHrDevAlertDateAndTime.' Usage: When an event causes an alert on
several devices, all such alerts SHALL have the same 'xcmHrDevAlertIndex.'
Usage: Conforming implementations are strongly encouraged to preserve the last
used value of 'xcmHrDevAlertIndex' across system power cycles.
""")
_XcmHrDevAlertRowStatus_Type = RowStatus
_XcmHrDevAlertRowStatus_Object = MibTableColumn
xcmHrDevAlertRowStatus = _XcmHrDevAlertRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 2),
    _XcmHrDevAlertRowStatus_Type()
)
xcmHrDevAlertRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertRowStatus.setReference("""\
See: 'xcmHrGeneralCreateSupport' in 'xcmHrGeneralTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertRowStatus.setDescription("""\
This object is used to create (by management agent) and delete (by management
station and/or management agent) individual conceptual rows in the
'xcmHrDevAlertTable'. Usage: Management stations can not create rows in the
alert table. Conforming implementations SHALL support 'active' and
'notInService' writes to this 'xcmHrDevAlertRowStatus' row status object; and
SHALL clear the 'xcmHrDevAlertGroup' bit in 'xcmHrGeneralCreateSupport' in the
'xcmHrGeneralTable'. Usage: Conforming implementations MAY support dynamic row
deletion via 'destroy(6)'. This allows management stations to delete any any
obsolete unary non-critical alerts.
""")
_XcmHrDevAlertSeverityLevel_Type = XcmGenNotifySeverityFilter
_XcmHrDevAlertSeverityLevel_Object = MibTableColumn
xcmHrDevAlertSeverityLevel = _XcmHrDevAlertSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 3),
    _XcmHrDevAlertSeverityLevel_Type()
)
xcmHrDevAlertSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertSeverityLevel.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertSeverityLevel.setReference("""\
See: 'prtAlertSeverityLevel' in the Printer MIB. See:
'XcmGenNotifySeverityFilter' in XCMI General TC and
'xcmGenTrapViewNotifySeverity' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertSeverityLevel.setDescription("""\
Device-specific severity level for the device alert which is recorded in this
conceptual row in the 'xcmHrDevAlertTable'. Usage: Conforming management agents
SHALL set one bit (specific severity level) or zero bits (no severity level
reported) in this object.
""")
_XcmHrDevAlertTrainingLevel_Type = XcmGenNotifyTrainingFilter
_XcmHrDevAlertTrainingLevel_Object = MibTableColumn
xcmHrDevAlertTrainingLevel = _XcmHrDevAlertTrainingLevel_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 4),
    _XcmHrDevAlertTrainingLevel_Type()
)
xcmHrDevAlertTrainingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertTrainingLevel.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertTrainingLevel.setReference("""\
See: 'prtAlertTrainingLevel' in the Printer MIB. See:
'XcmGenNotifyTrainingFilter' in XCMI General TC and
'xcmGenTrapViewNotifyTraining' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertTrainingLevel.setDescription("""\
Device-specific training level for the device alert which is recorded in this
conceptual row in the 'xcmHrDevAlertTable'. Usage: Conforming management agents
SHALL set one bit (specific training level) or zero bits (no training level
reported) in this object.
""")
_XcmHrDevAlertCodeInteger_Type = Integer32
_XcmHrDevAlertCodeInteger_Object = MibTableColumn
xcmHrDevAlertCodeInteger = _XcmHrDevAlertCodeInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 5),
    _XcmHrDevAlertCodeInteger_Type()
)
xcmHrDevAlertCodeInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertCodeInteger.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertCodeInteger.setReference("""\
See: 'prtAlertCode' in the Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertCodeInteger.setDescription("""\
Device-specific code for the device alert which is recorded in this conceptual
row in the 'xcmHrDevAlertTable'. Usage: Conforming implementations SHALL use
the values specified in any device-specific alert table. For devices of type
'hrDevicePrinter', this value SHALL be the same as the 'PrtAlertCodeTC'
returned in 'prtAlertCode.' The value of 0 means that no code has been assigned
to this alert. This value is intended for internal use by management
applications rather than for human display. It should not be confused with
'xcmHrDevAlertCodeString;' the two values are generally NOT the same and there
is no assumed mapping from one to the other. All values in the range 1..99999
are reserved for definition within a device specific MIB. Values 100000..199999
will be defined within this MIB in future versions. Individual products may
define values 200000 and larger.
""")


class _XcmHrDevAlertCodeString_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevAlertCodeString based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevAlertCodeString_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevAlertCodeString_Object = MibTableColumn
xcmHrDevAlertCodeString = _XcmHrDevAlertCodeString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 6),
    _XcmHrDevAlertCodeString_Type()
)
xcmHrDevAlertCodeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertCodeString.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertCodeString.setDescription("""\
Product-specific 'reportable alert code' string for the device alert which is
recorded in this conceptual row in the 'xcmHrDevAlertTable'. This is a product-
specific value used in documentation when describing this alert. Usage: This
value is intended for human display, and typically contains an alphanumeric
code or keyword phrase. It should not be confused with
'xcmHrDevAlertCodeInteger;' the two values are generally NOT the same and there
is no assumed mapping from one to the other. Usage: Often this string is not
translated since it has no specific meaning.
""")


class _XcmHrDevAlertDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevAlertDescription based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevAlertDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevAlertDescription_Object = MibTableColumn
xcmHrDevAlertDescription = _XcmHrDevAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 7),
    _XcmHrDevAlertDescription_Type()
)
xcmHrDevAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertDescription.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertDescription.setReference("""\
See: 'prtAlertDescription' in the Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertDescription.setDescription("""\
Human-readable alert description for the device alert which is recorded in this
conceptual row in the 'xcmHrDevAlertTable'. Usage: This is a human-readable
string, not intended for machine parsing. Management stations SHOULD obtain the
alert-specific fault code and severity level from the 'xcmHrDevAlertCodeString'
and 'xcmHrDevAlertSeverityLevel' and the current status from 'hrDeviceStatus'
objects rather than trying to interpret this string. Implementators are
strongly encouraged to include in this description: - a description of the
problem, - a description of the corrective action or a statement that no
corrective action is required, - a description of the impact on device
operations. Implementors SHOULD NOT include in this description a statement of
the current operating state of the device, since the device state may be
changed by some other event unrelated to this alert, making any such statement
invalid. A statement such as 'Device operation may continue' or 'This problem
must be corrected before the device can resume operation' is acceptable. Usage:
Conforming implementations SHALL provide BOTH detailed
'xcmHrDevAlertDescription' AND terse 'xcmHrDevAlertTitle' descriptions for each
critical alert and for each alert which requires human intervention.
Implementations MAY provide the same text for both strings. Usage:
Implementations SHALL provide localized translations of this string via the
'xcmGenMessageTextTable.' Usage: For devices of type 'hrDevicePrinter', this
SHOULD be the same description provided in 'prtAlertDescription' in the IETF
Printer MIB alert table. Implementations MAY choose to make these descriptions
different in order to differentiate between IETF-only and XCMI-aware management
applications.
""")


class _XcmHrDevAlertReferenceOID_Type(ObjectIdentifier):
    """Custom type xcmHrDevAlertReferenceOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmHrDevAlertReferenceOID_Object = MibTableColumn
xcmHrDevAlertReferenceOID = _XcmHrDevAlertReferenceOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 8),
    _XcmHrDevAlertReferenceOID_Type()
)
xcmHrDevAlertReferenceOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceOID.setReference("""\
See: 'prtAlertGroup', 'prtAlertGroupIndex' and 'prtAlertLocation' in the
Printer MIB. See: 'xcmHrSystemFaultReferenceOID' in XCMI HRX MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceOID.setDescription("""\
An (optional) unambiguous system object reference (which MAY include an object
instance qualifier suffix), used to specify supplemental information for this
device alert. Usage: Since this system object reference is specified as an
ASN.1 object identifier, it MAY be taken from any IETF, Xerox, third-party, or
product-specific MIB, or it MAY simply be any IETF SMIv2-style 'autonomous
type'. Usage: If 'xcmHrDevAlertReferenceIndex' is greater than 0, then it is an
index into a table referenced by 'xcmHrDevAlertReferenceOID.' Usage: Devices of
type 'hrDevicePrinter' SHALL set 'xcmHrDevAlertReferenceOID' to the OID of the
table or group referred to by 'prtAlertGroup' in the IETF printer alert table.
(This may be a table or group in the host resources MIB, printer MIB, finisher
MIB, or other MIB as enumerated by 'PrtAlertGroupTC'.) Note: Given the
flexibility this object provides, the information is only valuable to the
Management Station if the OID is a well known OID.
""")


class _XcmHrDevAlertDateAndTime_Type(DateAndTime):
    """Custom type xcmHrDevAlertDateAndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmHrDevAlertDateAndTime_Object = MibTableColumn
xcmHrDevAlertDateAndTime = _XcmHrDevAlertDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 9),
    _XcmHrDevAlertDateAndTime_Type()
)
xcmHrDevAlertDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertDateAndTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertDateAndTime.setReference("""\
See: 'prtAlertTime' in the Printer MIB. See: 'hrSystemDate' in IETF Host
Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertDateAndTime.setDescription("""\
The date and time stamp for the device alert which is recorded in this
conceptual row in the 'xcmHrDevAlertTable'.
""")


class _XcmHrDevAlertTitle_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDevAlertTitle based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_XcmHrDevAlertTitle_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDevAlertTitle_Object = MibTableColumn
xcmHrDevAlertTitle = _XcmHrDevAlertTitle_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 10),
    _XcmHrDevAlertTitle_Type()
)
xcmHrDevAlertTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertTitle.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertTitle.setReference("""\
See: 'xcmHrDevAlertDescription' which contains both a description of the alert
and the repair plan. See: 'xcmHrDevAlertCodeString' which contains an alert
code used in product documentation. See: 'xcmHrDevAlertHelpReference' which
contains an alert code used by a management station to locate help.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertTitle.setDescription("""\
A terse description of the problem or corrective action associated with the
device alert which is recorded in this conceptual row in the
'xcmHrDevAlertTable'. Usage: This is a human-readable string, not intended for
machine parsing. This message should be constructed for display in a navigation
tree or other contexts where the management station's user interface may have
strict limits on message length and complexity. The message should identify the
general type and area of the alert but omit most details in the interest of
brevity, e.g. 'tray empty' or 'replace toner' but not 'load A4 Transparency in
top tray' or 'replace cyan toner cartridge.' Implementations are strongly
encouraged to supply more detailed information in 'xcmHrDevAlertDescription'
but may simply supply the same text for both strings. Usage: Conforming
implementations SHALL provide both detailed 'xcmHrDevAlertDescription' and
terse 'xcmHrDevAlertTitle' descriptions for each critical alert and for each
alert which requires human intervention. Usage: Implementations SHALL provide
localized translations of this string via the 'xcmGenMessageTextTable.'
""")


class _XcmHrDevAlertHelpReference_Type(OctetString):
    """Custom type xcmHrDevAlertHelpReference based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDevAlertHelpReference_Type.__name__ = "OctetString"
_XcmHrDevAlertHelpReference_Object = MibTableColumn
xcmHrDevAlertHelpReference = _XcmHrDevAlertHelpReference_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 11),
    _XcmHrDevAlertHelpReference_Type()
)
xcmHrDevAlertHelpReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertHelpReference.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertHelpReference.setReference("""\
See: 'xcmHrDevAlertDescription' which contains both a description of the alert
and the repair plan. See: 'xcmHrDevAlertCodeString' which contains an alert
code used in product documentation. See: 'xcmHrDevAlertDescription' which
contains a description and repair actions.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertHelpReference.setDescription("""\
A key into a help reference. This key is intended for machine usage as either a
key into a database or as part of a path name to additional information. Usage:
This string may be used by a management station to construct the complete URL
or pathname of a file which may be stored on the management station, the
managed device, a customer's server or a Xerox web server. The mechanism by
which the URL or pathname should be constructed, including any requested
localization, is product- and application- dependent. For example, if the
device returns a string containing two path components <product-name>/<info-
path>, a host-based management application might construct either the pathname
'<install-dir>/<product-name>/<info-path>.<locale>' or '<install-
dir>/<locale>/<product-name>/<info-path>' depending on how the author wanted to
organize and distribute help files for various products and locales. A web-
based application with knowledge of the managed device's embedded web server
might be able to construct the URL 'http://<device-address>/alert-
info/<product-name>/<info-path>' and request a specific localization via the
HTTP 'accept- language' and 'accept-charset' headers. Usage: Implementors SHALL
use only the US-ASCII alphanumeric characters 'A'-'Z', 'a'-'z', '0'-'9' and the
punctuation marks underscore ('_'), hyphen ('-'), and forward slash ('/'). The
first and last characters must be alphanumeric. Implementors should note that
some hosts distinguish between upper- and lower-case letters in pathnames and
others don't. Therefore, different help paths should differ by more than just
letter case, and product documentation MUST accurately reflect the strings
returned in 'xcmHrDevAlertHelpReference', including letter case. Rationale:
Limiting the character set in this way ensures that the string can be used to
construct a valid pathname or URL on the widest variety of host systems. Note
that the file name is not localized (although the contents may be) and not
generally displayed for users, so there is little need to support characters
outside of this basic US-ASCII set.
""")


class _XcmHrDevAlertReferenceIndex_Type(Integer32):
    """Custom type xcmHrDevAlertReferenceIndex based on Integer32"""
    defaultValue = -1


_XcmHrDevAlertReferenceIndex_Object = MibTableColumn
xcmHrDevAlertReferenceIndex = _XcmHrDevAlertReferenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 12),
    _XcmHrDevAlertReferenceIndex_Type()
)
xcmHrDevAlertReferenceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceIndex.setReference("""\
See: 'prtAlertGroupIndex' in the Printer MIB. See: 'xcmHrDevAlertReferenceOID'.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceIndex.setDescription("""\
An (optional) index into a system table used to specify supplemental
information for this device alert. Usage: When xcmHrDevAlertReferenceOID is a
table, xcmHrDevAlertReferenceIndex can be an index into that table. Note: If
the ReferenceOID table has multiple indices, the management table must
recognize the table and must know which index is given by this ReferenceIndex.
Usage: Use -1 if no index is required.
""")


class _XcmHrDevAlertReferenceLocation_Type(Integer32):
    """Custom type xcmHrDevAlertReferenceLocation based on Integer32"""
    defaultValue = -2


_XcmHrDevAlertReferenceLocation_Object = MibTableColumn
xcmHrDevAlertReferenceLocation = _XcmHrDevAlertReferenceLocation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 13),
    _XcmHrDevAlertReferenceLocation_Type()
)
xcmHrDevAlertReferenceLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceLocation.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceLocation.setReference("""\
See: 'prtAlertGroupLocation' in the Printer MIB. See:
'xcmHrDevAlertReferenceOID'. See: 'xcmHrDevAlertReferenceIndex'.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertReferenceLocation.setDescription("""\
A product-specific refinement of the source of an alert. The value
'unknown(-2)' indicates that the device has no additional information to
provide.
""")
_XcmHrDevAlertDevAlertIndex_Type = Integer32
_XcmHrDevAlertDevAlertIndex_Object = MibTableColumn
xcmHrDevAlertDevAlertIndex = _XcmHrDevAlertDevAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 14),
    _XcmHrDevAlertDevAlertIndex_Type()
)
xcmHrDevAlertDevAlertIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertDevAlertIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertDevAlertIndex.setReference("""\
See: 'prtAlertIndex' in the Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertDevAlertIndex.setDescription("""\
An index into a device-specific alert table. When 'hrDeviceIndex' is of type
'hrDevicePrinter', then this field SHALL be the value of 'prtAlertIndex' for
the same alert.
""")
_XcmHrDevAlertPriority_Type = Integer32
_XcmHrDevAlertPriority_Object = MibTableColumn
xcmHrDevAlertPriority = _XcmHrDevAlertPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 2, 1, 15),
    _XcmHrDevAlertPriority_Type()
)
xcmHrDevAlertPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrDevAlertPriority.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertPriority.setReference("""\
See: 'prtAlertIndex' in the Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevAlertPriority.setDescription("""\
A sorting hint for user interfaces displaying device alerts. Usage: this field
allows a device to suggest, for instance, that the 'replace fuser' alert should
be displayed before the 'close door' alert in a list or navigation tree. Alert
priorities are ordinal numbers, with 1 indicating the highest priority for
display. A value of zero means 'no priority hint available'.
""")
_XcmHrDevAlertLastAlertIndex_Type = Cardinal32
_XcmHrDevAlertLastAlertIndex_Object = MibScalar
xcmHrDevAlertLastAlertIndex = _XcmHrDevAlertLastAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 3),
    _XcmHrDevAlertLastAlertIndex_Type()
)
xcmHrDevAlertLastAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertLastAlertIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertLastAlertIndex.setDescription("""\
The value of 'xcmHrDevAlertIndex' for the most recently-added alert (critical
or non-critical) in the alert table. This value only reflects the most recently
added alert; if the alert is subsequently cleared, the value of
'xcmHrDevAlertAllEvents' SHALL NOT be changed as a result. Compliant
implementations SHALL report zero if no alerts have been added to the table. A
management tool may use the fact that this value has not changed to avoid
checking for new alerts. Note that the value of this object will 'wrap' when
the first alert is added to the table after 'xcmHrDevAlertIndex' has reached
2**32 - 1 and 'wrapped' to 1.
""")
_XcmHrDevAlertLastCriticalAlertIndex_Type = Cardinal32
_XcmHrDevAlertLastCriticalAlertIndex_Object = MibScalar
xcmHrDevAlertLastCriticalAlertIndex = _XcmHrDevAlertLastCriticalAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 4),
    _XcmHrDevAlertLastCriticalAlertIndex_Type()
)
xcmHrDevAlertLastCriticalAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDevAlertLastCriticalAlertIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertLastCriticalAlertIndex.setDescription("""\
The value of 'xcmHrDevAlertIndex' for the most recently-added critical alert in
the alert table. This value only reflects the most recently added alert; if the
alert is subsequently cleared, the value of
'xcmHrDevAlertLastCriticalAlertIndex' SHALL NOT be changed as a result.
Compliant implementations SHALL report zero if no critical alerts have been
added to the table. A management tool may use the fact that this value has not
changed to avoid checking for new critical alerts. Note that the value of this
object will 'wrap' when the first critical alert is added to the table after
'xcmHrDevAlertIndex' has reached 2**32 - 1 and 'wrapped' to 1.
""")
_XcmHrConsoleScreen_ObjectIdentity = ObjectIdentity
xcmHrConsoleScreen = _XcmHrConsoleScreen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18)
)
_XcmHrConsoleScreenTable_Object = MibTable
xcmHrConsoleScreenTable = _XcmHrConsoleScreenTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2)
)
if mibBuilder.loadTexts:
    xcmHrConsoleScreenTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenTable.setReference("""\
See: 'prtConsoleDisplayBufferTable' and 'prtConsoleLightTable' in the Printer
MIB.
""")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenTable.setDescription("""\
A table containing system local console screen (page) info for an installed
local user interface console on this host system.
""")
_XcmHrConsoleScreenEntry_Object = MibTableRow
xcmHrConsoleScreenEntry = _XcmHrConsoleScreenEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1)
)
xcmHrConsoleScreenEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenIndex"),
)
if mibBuilder.loadTexts:
    xcmHrConsoleScreenEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenEntry.setDescription("""\
An entry containing system local console screen (page) info for an installed
local user interface console on this host system. Usage: Conforming management
agents SHOULD report local console info via 'hrDeviceIndex' for
'hrDevicePrinter' - consistent with 'prtConsoleDisplayBufferTable' in the
Printer MIB - or 'hrDeviceIndex' for 'xcmHrDeviceHostSystem' in XCMI HRX TC.
""")
_XcmHrConsoleScreenIndex_Type = Ordinal32
_XcmHrConsoleScreenIndex_Object = MibTableColumn
xcmHrConsoleScreenIndex = _XcmHrConsoleScreenIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 1),
    _XcmHrConsoleScreenIndex_Type()
)
xcmHrConsoleScreenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrConsoleScreenTable'.
""")


class _XcmHrConsoleScreenName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrConsoleScreenName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrConsoleScreenName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrConsoleScreenName_Object = MibTableColumn
xcmHrConsoleScreenName = _XcmHrConsoleScreenName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 2),
    _XcmHrConsoleScreenName_Type()
)
xcmHrConsoleScreenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenName.setDescription("""\
Human-readable name of this local console screen (page), used by system
administrators and end users to identify this screen for systems management.
Usage: Conforming management agents SHOULD NOT report the same value of
'xcmHrConsoleScreenName' for different screens (pages). Screens (pages) are
always uniquely labelled by their indices of 'xcmHrDeviceIndex' and
'xcmHrConsoleScreenIndex'.
""")


class _XcmHrConsoleScreenDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrConsoleScreenDescription based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrConsoleScreenDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrConsoleScreenDescription_Object = MibTableColumn
xcmHrConsoleScreenDescription = _XcmHrConsoleScreenDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 3),
    _XcmHrConsoleScreenDescription_Type()
)
xcmHrConsoleScreenDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenDescription.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenDescription.setDescription("""\
Human-readable description of this local console screen.
""")
_XcmHrConsoleScreenParentIndex_Type = Cardinal32
_XcmHrConsoleScreenParentIndex_Object = MibTableColumn
xcmHrConsoleScreenParentIndex = _XcmHrConsoleScreenParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 4),
    _XcmHrConsoleScreenParentIndex_Type()
)
xcmHrConsoleScreenParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenParentIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenParentIndex.setDescription("""\
Parent console screen index associated with this local console screen (page),
or zero (if none). Usage: Value of 'xcmHrConsoleScreenIndex' for parent screen.
This object MAY be used to report tree or forest relationships between local
console screens. Trees have a single root screen. Forests have two or more root
screens (w/ no parent screen).
""")


class _XcmHrConsoleScreenPriority_Type(Integer32):
    """Custom type xcmHrConsoleScreenPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmHrConsoleScreenPriority_Type.__name__ = "Integer32"
_XcmHrConsoleScreenPriority_Object = MibTableColumn
xcmHrConsoleScreenPriority = _XcmHrConsoleScreenPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 5),
    _XcmHrConsoleScreenPriority_Type()
)
xcmHrConsoleScreenPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenPriority.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenPriority.setReference("""\
See: 'xcmHrDevInfoPriority' in XCMI Ext to Host Resources MIB 'xcmJobPriority'
in XCMI Job Mon MIB. 'xcmSvcMonServicePriority' in XCMI Svc Mon MIB.
""")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenPriority.setDescription("""\
The display priority of this local console screen (page). Usage: The display
priority of this screen (page), where '0' is unspecified (default), '1' is
lowest, and '100' is highest. When two screens (pages) have equal priority, the
first (lowest) value of 'xcmHrConsoleScreenIndex' (lexicographical order) SHALL
have the highest display priority.
""")
_XcmHrConsoleScreenTabCount_Type = Cardinal32
_XcmHrConsoleScreenTabCount_Object = MibTableColumn
xcmHrConsoleScreenTabCount = _XcmHrConsoleScreenTabCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 18, 2, 1, 6),
    _XcmHrConsoleScreenTabCount_Type()
)
xcmHrConsoleScreenTabCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenTabCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenTabCount.setDescription("""\
Number of tabs (buttons) on this local console screen (page). Usage: Conforming
management agents SHALL report values of 'xcmHrConsoleTabIndex' that are less
than or equal to the value of 'xcmHrConsoleScreenTabCount' for the SAME value
of 'xcmHrConsoleScreenIndex' (enclosing screen).
""")
_XcmHrConsoleTab_ObjectIdentity = ObjectIdentity
xcmHrConsoleTab = _XcmHrConsoleTab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19)
)
_XcmHrConsoleTabTable_Object = MibTable
xcmHrConsoleTabTable = _XcmHrConsoleTabTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2)
)
if mibBuilder.loadTexts:
    xcmHrConsoleTabTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTabTable.setReference("""\
See: 'prtConsoleDisplayBufferTable' and 'prtConsoleLightTable' in the Printer
MIB.
""")
if mibBuilder.loadTexts:
    xcmHrConsoleTabTable.setDescription("""\
A table containing system local console tab (button) info for an installed
local user interface console on this host system.
""")
_XcmHrConsoleTabEntry_Object = MibTableRow
xcmHrConsoleTabEntry = _XcmHrConsoleTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1)
)
xcmHrConsoleTabEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabIndex"),
)
if mibBuilder.loadTexts:
    xcmHrConsoleTabEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTabEntry.setDescription("""\
An entry containing system local console tab (button) info for an installed
local user interface console on this host system. Usage: Conforming management
agents SHOULD report local console info via 'hrDeviceIndex' for
'hrDevicePrinter' - consistent with 'prtConsoleDisplayBufferTable' in the
Printer MIB - or 'hrDeviceIndex' for 'xcmHrDeviceHostSystem' in XCMI HRX TC.
""")
_XcmHrConsoleTabIndex_Type = Ordinal32
_XcmHrConsoleTabIndex_Object = MibTableColumn
xcmHrConsoleTabIndex = _XcmHrConsoleTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 1),
    _XcmHrConsoleTabIndex_Type()
)
xcmHrConsoleTabIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrConsoleTabIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTabIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrConsoleTabTable'.
""")


class _XcmHrConsoleTabName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrConsoleTabName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrConsoleTabName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrConsoleTabName_Object = MibTableColumn
xcmHrConsoleTabName = _XcmHrConsoleTabName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 2),
    _XcmHrConsoleTabName_Type()
)
xcmHrConsoleTabName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleTabName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTabName.setDescription("""\
Human-readable name of this local console tab (button), within the enclosing
local console screen (page), used by system administrators and end users to
identify this tab for systems management. Usage: Conforming management agents
MAY report the same value of 'xcmHrConsoleTabName' for different tabs
(buttons). Tabs (buttons) are always uniquely labelled by their indices of
'xcmHrDeviceIndex', 'xcmHrConsoleScreenIndex', and 'xcmHrConsoleTabIndex'.
""")


class _XcmHrConsoleTabDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrConsoleTabDescription based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrConsoleTabDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrConsoleTabDescription_Object = MibTableColumn
xcmHrConsoleTabDescription = _XcmHrConsoleTabDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 3),
    _XcmHrConsoleTabDescription_Type()
)
xcmHrConsoleTabDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleTabDescription.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTabDescription.setDescription("""\
Human-readable description of this local console tab (button), within the
enclosing local console screen (page).
""")
_XcmHrConsoleTabScreenIndex_Type = Cardinal32
_XcmHrConsoleTabScreenIndex_Object = MibTableColumn
xcmHrConsoleTabScreenIndex = _XcmHrConsoleTabScreenIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 4),
    _XcmHrConsoleTabScreenIndex_Type()
)
xcmHrConsoleTabScreenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrConsoleTabScreenIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTabScreenIndex.setDescription("""\
New local console screen selected by this local console tab (button). Usage:
Value of 'xcmHrConsoleScreenIndex' for the new screen.
""")


class _XcmHrConsoleTabPriority_Type(Integer32):
    """Custom type xcmHrConsoleTabPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmHrConsoleTabPriority_Type.__name__ = "Integer32"
_XcmHrConsoleTabPriority_Object = MibTableColumn
xcmHrConsoleTabPriority = _XcmHrConsoleTabPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 19, 2, 1, 5),
    _XcmHrConsoleTabPriority_Type()
)
xcmHrConsoleTabPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrConsoleTabPriority.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTabPriority.setReference("""\
See: 'xcmHrDevInfoPriority' in XCMI Ext to Host Resources MIB 'xcmJobPriority'
in XCMI Job Mon MIB. 'xcmSvcMonServicePriority' in XCMI Svc Mon MIB.
""")
if mibBuilder.loadTexts:
    xcmHrConsoleTabPriority.setDescription("""\
The display priority of this local console tab (button) within the enclosing
local console screen (page). Usage: The display priority of this tab (button),
where '0' is unspecified (default), '1' is lowest, and '100' is highest. When
two tabs (buttons) have equal priority, the first (lowest) value of
'xcmHrConsoleTabIndex' (lexicographical order), for the SAME value of
'xcmHrConsoleScreenIndex' (enclosing screen), SHALL have the highest display
priority.
""")
_XcmHrSupplies_ObjectIdentity = ObjectIdentity
xcmHrSupplies = _XcmHrSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20)
)
_XcmHrSuppliesTable_Object = MibTable
xcmHrSuppliesTable = _XcmHrSuppliesTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1)
)
if mibBuilder.loadTexts:
    xcmHrSuppliesTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesTable.setDescription("""\
A table containing information on all supplies for the managed system. Usage:
Rows of the table are created by the agent. Certain values in the rows can be
set by a management tool.
""")
_XcmHrSuppliesEntry_Object = MibTableRow
xcmHrSuppliesEntry = _XcmHrSuppliesEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1)
)
xcmHrSuppliesEntry.setIndexNames(
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesIndex"),
)
if mibBuilder.loadTexts:
    xcmHrSuppliesEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesEntry.setDescription("""\
See xcmHrSuppliesTable
""")


class _XcmHrSuppliesIndex_Type(Ordinal32):
    """Custom type xcmHrSuppliesIndex based on Ordinal32"""
    subtypeSpec = Ordinal32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XcmHrSuppliesIndex_Type.__name__ = "Ordinal32"
_XcmHrSuppliesIndex_Object = MibTableColumn
xcmHrSuppliesIndex = _XcmHrSuppliesIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 1),
    _XcmHrSuppliesIndex_Type()
)
xcmHrSuppliesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrSuppliesIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesIndex.setDescription("""\
A unique value used by the agent to identify this supply. Although these values
may change due to a major reconfiguration of the device (e.g. the addition of
new finishing module to the printer), values SHOULD remain stable across
successive printer power cycles.
""")
_XcmHrSuppliesReferenceOID_Type = ObjectIdentifier
_XcmHrSuppliesReferenceOID_Object = MibTableColumn
xcmHrSuppliesReferenceOID = _XcmHrSuppliesReferenceOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 2),
    _XcmHrSuppliesReferenceOID_Type()
)
xcmHrSuppliesReferenceOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesReferenceOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesReferenceOID.setDescription("""\
A system object reference (which SHALL include an object instance qualifier
suffix), used to specify an object in another table related to this supply.
Usage: If the supply also appears in the prtMarkerSuppliesTable, then this
referenceOID SHALL be the OID for the prtMarkerSuppliesDescription for this
supply. Usage: If the supply also appears in the finSupplyTable, then this
referenceOID SHALL be the OID for the finSupplyDescription for this supply.
Usage: If the supply also appears in some other table (such as a scanner
supplies table), then this referenceOID SHALL be the OID for the description
column for this supply if a description column exists. Otherwise it SHALL be
the first column of the other table as the reference OID. Usage: If the supply
does not appear in any other table, then this referenceOID SHALL be the OID for
hrDeviceDescr for the physical device requiring or using this supply. Usage: If
no physical device in the hrDeviceTable requires the supply, then the
hrDeviceTable is not complete. Note: Given the flexibility this object
provides, the information is only valuable to the Management Station if the OID
is a well-known OID. Note: This object has no default value since it must be
filled in.
""")
_XcmHrSuppliesType_Type = AutonomousType
_XcmHrSuppliesType_Object = MibTableColumn
xcmHrSuppliesType = _XcmHrSuppliesType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 3),
    _XcmHrSuppliesType_Type()
)
xcmHrSuppliesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesType.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesType.setDescription("""\
An indication of the type of device. Use device type OIDs.
""")
_XcmHrSuppliesClass_Type = XcmHrSuppliesClassTC
_XcmHrSuppliesClass_Object = MibTableColumn
xcmHrSuppliesClass = _XcmHrSuppliesClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 4),
    _XcmHrSuppliesClass_Type()
)
xcmHrSuppliesClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesClass.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesClass.setDescription("""\
This object describes how this type is replaced. Values range from 'it never
breaks' to 'untrained user'. A value of 'Unknown(2)' should never be used. Use
the least restrictive type if it is not clear. For example, if a part is
usually replaced by service, but a customer can order it and replace it on
their own, then the supply would be 'CustomerReplaceable(4)'.
""")
_XcmHrSuppliesDescr_Type = OctetString
_XcmHrSuppliesDescr_Object = MibTableColumn
xcmHrSuppliesDescr = _XcmHrSuppliesDescr_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 5),
    _XcmHrSuppliesDescr_Type()
)
xcmHrSuppliesDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesDescr.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesDescr.setDescription("""\
A description of this supply. This name MUST match the name of the supply as it
will be exposed on www.xerox.com, within the printer's web UI, within the
printer's local UI and within all configuration pages that can be generated by
the printer.
""")
_XcmHrSuppliesPartNumber_Type = OctetString
_XcmHrSuppliesPartNumber_Object = MibTableColumn
xcmHrSuppliesPartNumber = _XcmHrSuppliesPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 1, 1, 6),
    _XcmHrSuppliesPartNumber_Type()
)
xcmHrSuppliesPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrSuppliesPartNumber.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesPartNumber.setDescription("""\
The part number used to order this supply. This part number may depend on the
location of the machine. If no part number is associated with this supply, then
the value will be blank (null).
""")
_XcmHrDetailTable_Object = MibTable
xcmHrDetailTable = _XcmHrDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2)
)
if mibBuilder.loadTexts:
    xcmHrDetailTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailTable.setDescription("""\
A 'sparse' table containing detail information for rows of other SNMP tables'
Usage: Rows of the table are created by the agent. Certain values in the rows
can be set by a management tool. Usage: OSI ASN.1 encoding rules (ISO 8825) and
IETF SNMP rules REQUIRE that when object identifiers (OIDs) are used as table
indices, the first arc (sub- identifier) of each object identifier MUST be
preceded by the count of arcs (sub- identifiers) in the object identifier (see
'Mapping of the INDEX clause' in SNMPv2-SMI, RFC 2578), unless the index is
rightmost (low-order) and specified with the IMPLIED keyword. Thus, the
xcmHrDetailTableIndex index of xcmHrDetailEntry MUST be preceded by an arcs
count in SNMP request/response PDUs. So, if we wanted the Total Black
Impressions using the third xcmHrSupplies row (lets assume that is the toner
cartridge) we would do an SNMP Get on the object
1.3.6.1.4.1.253.8.51.1.3.1.7.1.1.3.20.34 Because 1.3.6.1.4.1.253.8.51.1.3.1.7
is the OID of xcmHrDetailValueInteger. 1 is the enumeration for the
xcmHrSuppliesTable. 3 is the index into the xcmHrSupplies table for this
cartridge (and there is 1 arcs there). 20 is the detail type for lifetime
usage. And 34 is the index from table 22 of the XMIG for 'Total Black
Impressions'.
""")
_XcmHrDetailEntry_Object = MibTableRow
xcmHrDetailEntry = _XcmHrDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1)
)
xcmHrDetailEntry.setIndexNames(
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailTableRef"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailTableIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailType"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmHrDetailEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailEntry.setDescription("""\
See xcmHrDetailTable
""")
_XcmHrDetailTableRef_Type = XcmHrDetailTableEnumTC
_XcmHrDetailTableRef_Object = MibTableColumn
xcmHrDetailTableRef = _XcmHrDetailTableRef_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 1),
    _XcmHrDetailTableRef_Type()
)
xcmHrDetailTableRef.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDetailTableRef.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailTableRef.setDescription("""\
This object is used to identify the table that this detail is qualifying.
Usage: To provide additional information on supplies that are defined in the
xcmHrSuppliesTable, prtMarkerSuppliesTable or finSupplyTable.
""")
_XcmHrDetailTableIndex_Type = ObjectIdentifier
_XcmHrDetailTableIndex_Object = MibTableColumn
xcmHrDetailTableIndex = _XcmHrDetailTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 2),
    _XcmHrDetailTableIndex_Type()
)
xcmHrDetailTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDetailTableIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailTableIndex.setDescription("""\
This object is used to provide the index of the specific row in the table
referenced by xcmHrDetailTableRef. Usage: To identify a supply in the
xcmHrSuppliesTable, use the single octet xcmHrSuppliesIndex. Usage: To identify
a supply in the prtMarkerSuppliesTable, use the single octet
prtMarkerSuppliesIndex. Usage: To identify a supply in the finSupplyTable, use
the single octet finSupplyIndex.
""")
_XcmHrDetailType_Type = XcmHrDevDetailType
_XcmHrDetailType_Object = MibTableColumn
xcmHrDetailType = _XcmHrDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 3),
    _XcmHrDetailType_Type()
)
xcmHrDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDetailType.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailType.setDescription("""\
The type of the detail information specified in this row of the table.
""")
_XcmHrDetailIndex_Type = Ordinal32
_XcmHrDetailIndex_Object = MibTableColumn
xcmHrDetailIndex = _XcmHrDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 4),
    _XcmHrDetailIndex_Type()
)
xcmHrDetailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrDetailIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailIndex.setDescription("""\
This object supports details which have multiple values and can also be used to
correlate related values of different types. Usage: For distinct detail types
which are related, this index SHALL be equal for related detail values. Usage:
For detail types which are multi-valued, this index SHALL be used to enumerate
the list of details.
""")


class _XcmHrDetailUnitClass_Type(XcmHrDevDetailUnitClass):
    """Custom type xcmHrDetailUnitClass based on XcmHrDevDetailUnitClass"""


_XcmHrDetailUnitClass_Object = MibTableColumn
xcmHrDetailUnitClass = _XcmHrDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 5),
    _XcmHrDetailUnitClass_Type()
)
xcmHrDetailUnitClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmHrDetailUnitClass.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailUnitClass.setDescription("""\
The value/unit class of the detail information specified in this row of the
table. Usage: Used to select a textual convention for specifying the value unit
of this device detail. Usage: Also used to specify which of
xcmHrDetailValue[Integer|OID|String] are used to contain the detail value.
Usage: Typically the value of xcmHrDetailUnitClass is listed explicitly in the
description of the XcmHrDevDetailType enumeration. In that case, the agent
SHALL populate this object with the listed enumeration and a management tool
does not have to check this object to determine the unit class.
""")
_XcmHrDetailUnit_Type = Cardinal32
_XcmHrDetailUnit_Object = MibTableColumn
xcmHrDetailUnit = _XcmHrDetailUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 6),
    _XcmHrDetailUnit_Type()
)
xcmHrDetailUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailUnit.setDescription("""\
This object makes explicit the units in which this detail value is being
specified. Usage: Used to select an enumerated choice from a textual convention
to specify the value unit of this device detail. The specific textual
convention is identified by xcmHrDetailUnitClass.
""")
_XcmHrDetailValueInteger_Type = Integer32
_XcmHrDetailValueInteger_Object = MibTableColumn
xcmHrDetailValueInteger = _XcmHrDetailValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 7),
    _XcmHrDetailValueInteger_Type()
)
xcmHrDetailValueInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailValueInteger.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailValueInteger.setDescription("""\
The current value for a device detail with a base value syntax 'INTEGER'.
""")
_XcmHrDetailValueOID_Type = ObjectIdentifier
_XcmHrDetailValueOID_Object = MibTableColumn
xcmHrDetailValueOID = _XcmHrDetailValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 8),
    _XcmHrDetailValueOID_Type()
)
xcmHrDetailValueOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailValueOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailValueOID.setDescription("""\
The current value for a device detail with a base value syntax 'OID'.
""")
_XcmHrDetailValueString_Type = OctetString
_XcmHrDetailValueString_Object = MibTableColumn
xcmHrDetailValueString = _XcmHrDetailValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 9),
    _XcmHrDetailValueString_Type()
)
xcmHrDetailValueString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailValueString.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailValueString.setDescription("""\
The current value for a device detail with a base value syntax 'STRING'. This
object is also used to provide secondary information when the base value syntax
is 'INTEGER' or 'OID'. Typically this is a string version of the value of the
detail.
""")


class _XcmHrDetailDescription_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmHrDetailDescription based on XcmFixedLocaleDisplayString"""
    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrDetailDescription_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmHrDetailDescription_Object = MibTableColumn
xcmHrDetailDescription = _XcmHrDetailDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 20, 2, 1, 10),
    _XcmHrDetailDescription_Type()
)
xcmHrDetailDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmHrDetailDescription.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailDescription.setDescription("""\
This object is used to provide a description of the detail.
""")
_XcmHrConsole_ObjectIdentity = ObjectIdentity
xcmHrConsole = _XcmHrConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21)
)
_XcmHrConsoleTable_Object = MibTable
xcmHrConsoleTable = _XcmHrConsoleTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2)
)
if mibBuilder.loadTexts:
    xcmHrConsoleTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTable.setReference("""\
See: 'prtConsoleDisplayBufferTable' and 'prtConsoleLightTable' in the Printer
MIB.
""")
if mibBuilder.loadTexts:
    xcmHrConsoleTable.setDescription("""\
A table containing system local console information for an installed local user
interface console on this host system.
""")
_XcmHrConsoleEntry_Object = MibTableRow
xcmHrConsoleEntry = _XcmHrConsoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1)
)
xcmHrConsoleEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleIndex"),
)
if mibBuilder.loadTexts:
    xcmHrConsoleEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleEntry.setDescription("""\
An entry containing system local console information for an installed local
user interface console on this host system. Usage: Conforming management agents
SHOULD report local console info via 'hrDeviceIndex' for 'hrDevicePrinter' -
consistent with 'prtConsoleDisplayBufferTable' in the Printer MIB - or
'hrDeviceIndex' for 'xcmHrDeviceHostSystem' in XCMI HRX TC.
""")
_XcmHrConsoleIndex_Type = Ordinal32
_XcmHrConsoleIndex_Object = MibTableColumn
xcmHrConsoleIndex = _XcmHrConsoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 1),
    _XcmHrConsoleIndex_Type()
)
xcmHrConsoleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmHrConsoleIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmHrConsoleTable'.
""")


class _XcmHrConsoleDefaultService_Type(XcmHrConsoleDefaultService):
    """Custom type xcmHrConsoleDefaultService based on XcmHrConsoleDefaultService"""


_XcmHrConsoleDefaultService_Object = MibTableColumn
xcmHrConsoleDefaultService = _XcmHrConsoleDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 2),
    _XcmHrConsoleDefaultService_Type()
)
xcmHrConsoleDefaultService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleDefaultService.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleDefaultService.setDescription("""\
The default service shown on the console user interface. This is used to change
the meaning of the Green Button on the front panel of many devices.
""")


class _XcmHrConsoleBrightness_Type(Integer32):
    """Custom type xcmHrConsoleBrightness based on Integer32"""
    defaultValue = 5


_XcmHrConsoleBrightness_Object = MibTableColumn
xcmHrConsoleBrightness = _XcmHrConsoleBrightness_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 3),
    _XcmHrConsoleBrightness_Type()
)
xcmHrConsoleBrightness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleBrightness.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleBrightness.setDescription("""\
The console brightness level. Often this a number from 1 to 10 where 1 is
dimmest and 10 is brightest.
""")


class _XcmHrConsoleContrast_Type(Integer32):
    """Custom type xcmHrConsoleContrast based on Integer32"""
    defaultValue = 5


_XcmHrConsoleContrast_Object = MibTableColumn
xcmHrConsoleContrast = _XcmHrConsoleContrast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 4),
    _XcmHrConsoleContrast_Type()
)
xcmHrConsoleContrast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleContrast.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleContrast.setDescription("""\
The console contrast level. Often this a number from 1 to 10 where 1 is least
contrast and 10 is most contrast.
""")


class _XcmHrConsoleAccessibility_Type(TruthValue):
    """Custom type xcmHrConsoleAccessibility based on TruthValue"""


_XcmHrConsoleAccessibility_Object = MibTableColumn
xcmHrConsoleAccessibility = _XcmHrConsoleAccessibility_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 5),
    _XcmHrConsoleAccessibility_Type()
)
xcmHrConsoleAccessibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleAccessibility.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleAccessibility.setDescription("""\
Turns On/off control panel accessibility mode. When On, value=true, the console
does not timeout and key repeating is off. When Off, value=false, the console
panel times out after specified period of no activity and key repeating is on.
""")


class _XcmHrConsoleAutoClearTime_Type(Integer32):
    """Custom type xcmHrConsoleAutoClearTime based on Integer32"""
    defaultValue = 60


_XcmHrConsoleAutoClearTime_Object = MibTableColumn
xcmHrConsoleAutoClearTime = _XcmHrConsoleAutoClearTime_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 6),
    _XcmHrConsoleAutoClearTime_Type()
)
xcmHrConsoleAutoClearTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleAutoClearTime.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleAutoClearTime.setDescription("""\
The automatic clear timeout for the console. Often this a numbe 0 to 120 where
0 is console never times out and 120 means the console times out after 120
seconds of no activity.
""")


class _XcmHrConsoleInsertTimeout_Type(Integer32):
    """Custom type xcmHrConsoleInsertTimeout based on Integer32"""
    defaultValue = 60


_XcmHrConsoleInsertTimeout_Object = MibTableColumn
xcmHrConsoleInsertTimeout = _XcmHrConsoleInsertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 7),
    _XcmHrConsoleInsertTimeout_Type()
)
xcmHrConsoleInsertTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleInsertTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleInsertTimeout.setDescription("""\
The insertion timeout for console prompts. Often this a number 0, 60 or -1
where 0 is console never prompts, 60 means the console prompts the user for 60
seconds than stops and -1 means the console prompt is displayed for an infinite
amount of time.
""")


class _XcmHrConsoleTray1Timeout_Type(Integer32):
    """Custom type xcmHrConsoleTray1Timeout based on Integer32"""
    defaultValue = 60


_XcmHrConsoleTray1Timeout_Object = MibTableColumn
xcmHrConsoleTray1Timeout = _XcmHrConsoleTray1Timeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 8),
    _XcmHrConsoleTray1Timeout_Type()
)
xcmHrConsoleTray1Timeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleTray1Timeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTray1Timeout.setDescription("""\
The insertion timeout for console prompts for tray 1 events. Often this a
number 0, 60 or -1 where 0 is console never prompts, 60 means the console
prompts the user for 60 seconds than stops and -1 means the console prompt is
displayed for an infinite amount of time.
""")


class _XcmHrConsoleTray2nTimeout_Type(Integer32):
    """Custom type xcmHrConsoleTray2nTimeout based on Integer32"""
    defaultValue = 60


_XcmHrConsoleTray2nTimeout_Object = MibTableColumn
xcmHrConsoleTray2nTimeout = _XcmHrConsoleTray2nTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 9),
    _XcmHrConsoleTray2nTimeout_Type()
)
xcmHrConsoleTray2nTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleTray2nTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTray2nTimeout.setDescription("""\
The insertion timeout in seconds for console prompts for trays 2 through n
events. Often this a number 0, 60 or -1 where 0 is console never prompts, 60
means the console prompts the user for 1 minute than stops and -1 means the
console prompt is displayed for an infinite amount of time.
""")


class _XcmHrConsoleLoadTimeout_Type(Integer32):
    """Custom type xcmHrConsoleLoadTimeout based on Integer32"""
    defaultValue = 60


_XcmHrConsoleLoadTimeout_Object = MibTableColumn
xcmHrConsoleLoadTimeout = _XcmHrConsoleLoadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 10),
    _XcmHrConsoleLoadTimeout_Type()
)
xcmHrConsoleLoadTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleLoadTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleLoadTimeout.setDescription("""\
The amount of time in minutes the system waits for before using the default
media source for the device.
""")


class _XcmHrConsoleSoundVolume_Type(Integer32):
    """Custom type xcmHrConsoleSoundVolume based on Integer32"""
    defaultValue = 2


_XcmHrConsoleSoundVolume_Object = MibTableColumn
xcmHrConsoleSoundVolume = _XcmHrConsoleSoundVolume_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 11),
    _XcmHrConsoleSoundVolume_Type()
)
xcmHrConsoleSoundVolume.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleSoundVolume.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleSoundVolume.setDescription("""\
The console sound volume control. This is often used to control how loud the
fax modem telephone line sound is. This is often a number 0 through 10 where 0
is console sounds are off, 1 is the lowest volume and 10 is the highest volume.
""")


class _XcmHrConsoleSoundDuration_Type(Integer32):
    """Custom type xcmHrConsoleSoundDuration based on Integer32"""
    defaultValue = 15


_XcmHrConsoleSoundDuration_Object = MibTableColumn
xcmHrConsoleSoundDuration = _XcmHrConsoleSoundDuration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 21, 2, 1, 12),
    _XcmHrConsoleSoundDuration_Type()
)
xcmHrConsoleSoundDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrConsoleSoundDuration.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleSoundDuration.setDescription("""\
The console sound duration. This is often used to control how long the sound
will last when the fax modem telephone line soun is on. This is often a number
1 through 255 where 1 means the console sounds are on for 1 second and 255
means the console sounds are on for 255 seconds.
""")
_XcmHrGenericParamGroup_ObjectIdentity = ObjectIdentity
xcmHrGenericParamGroup = _XcmHrGenericParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 22)
)


class _XcmHrGenericParamName_Type(OctetString):
    """Custom type xcmHrGenericParamName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrGenericParamName_Type.__name__ = "OctetString"
_XcmHrGenericParamName_Object = MibScalar
xcmHrGenericParamName = _XcmHrGenericParamName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 22, 1),
    _XcmHrGenericParamName_Type()
)
xcmHrGenericParamName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrGenericParamName.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGenericParamName.setDescription("""\
 This object provides a name of a parameter that can be returned and modified
by SNMP. Usage: Conforming management agents SHALL 'reject' any SNMP Set-
request to xcmHrGenericParamName if the parameter name is invalid, with 'bad
Value' error. Usage: Conforming management stations can set
'xcmHrGenericParamName', i.e. the parameter name and 'xcmHrGenericParamValue',
i.e. the parameter value SIMULTANEOUSLY in the same SNMP Set-Request PDU using
a BULK-SET request. The order in the BULK-SET must be 'xcmHrGenericParamName',
followed by 'xcmHrGenericParamValue'
""")


class _XcmHrGenericParamValue_Type(OctetString):
    """Custom type xcmHrGenericParamValue based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmHrGenericParamValue_Type.__name__ = "OctetString"
_XcmHrGenericParamValue_Object = MibScalar
xcmHrGenericParamValue = _XcmHrGenericParamValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 22, 2),
    _XcmHrGenericParamValue_Type()
)
xcmHrGenericParamValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmHrGenericParamValue.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGenericParamValue.setDescription("""\
 This object provides a value for a parameter that can be returned and modified
by SNMP. To get a parameter value the manager will need to SET
'xcmHrGenericParamName' to inform the agent what parameter value is desired.
Then a GET request on this object will return the value for the parameter
requested. Usage: Conformant implementations MUST encrypt passwords, keys, and
other security information in SET requests made to this object. Usage:
Conformant implementations MUST NOT return passwords, keys, and other security
information in response to GET requests made to this object. Usage: Conforming
management stations can set 'xcmHrGenericParamValue', i.e. the parameter value
and 'xcmHrGenericParamName', i.e. the parameter name SIMULTANEOUSLY in the same
SNMP Set-Request PDU using a BULK-SET request. The order in the BULK-SET must
be 'xcmHrGenericParamName', followed by 'xcmHrGenericParamValue'
""")

# Managed Objects groups

xcmHrDevInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 3)
)
xcmHrDevInfoGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoSerialNumber"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoRealization"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoInstallDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoResetDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoNextDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoPreviousDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoPhysicalDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoPriority"))
)
if mibBuilder.loadTexts:
    xcmHrDevInfoGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevInfoGroup.setDescription("""\
The Host Resources Extensions MIB Device Info Group
""")

xcmHrDevHelpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 4)
)
xcmHrDevHelpGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevHelpRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevHelpOperatorMessage"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevHelpProblemMessage"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevHelpCommsAddressIndex"))
)
if mibBuilder.loadTexts:
    xcmHrDevHelpGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevHelpGroup.setDescription("""\
The Host Resources Extensions MIB Device Help Group Implementation of this
group is DEPRECATED (as of XCMI v4.1) and conforming implementations SHOULD use
'deviceHelp...' details in 'xcmHrDevDetailTable' instead.
""")

xcmHrDevMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 5)
)
xcmHrDevMgmtGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandRequest"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandData"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtUserPassword"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtOperatorPassword"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtAdminPassword"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandInProgress"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtUserName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtOperatorName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtAdminName"))
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevMgmtGroup.setDescription("""\
The Host Resources Extensions MIB Device Mgmt Group
""")

xcmHrDevPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 6)
)
xcmHrDevPowerGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWarmUpSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerCoolDownSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerEnergySaveSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerTimeUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWarmUpDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWarmUpDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerCoolDownDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerCoolDownDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerEnergySaveDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerEnergySaveDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWakeUpSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWakeUpDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerWakeUpDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerShutdownDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerShutdownDuration"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerStartupDelay"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevPowerStartupDuration"))
)
if mibBuilder.loadTexts:
    xcmHrDevPowerGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevPowerGroup.setDescription("""\
The Host Resources Extensions MIB Device Power Group
""")

xcmHrDevTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 7)
)
xcmHrDevTrafficGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputCount"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputCount"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputMaxSize"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputMaxSize"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficInputTimeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevTrafficOutputTimeout"))
)
if mibBuilder.loadTexts:
    xcmHrDevTrafficGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevTrafficGroup.setDescription("""\
The Host Resources Extensions MIB Device Traffic Group
""")

xcmHrSystemFaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 8)
)
xcmHrSystemFaultGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultCode"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultString"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultReferenceOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultHrDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSystemFaultDate"))
)
if mibBuilder.loadTexts:
    xcmHrSystemFaultGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSystemFaultGroup.setDescription("""\
The Host Resources Extensions MIB System Fault Group
""")

xcmHrGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 9)
)
xcmHrGeneralGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralVersionID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralVersionDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralGroupSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralStorageLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralDeviceLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralFSLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralSWRunLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralSWInstalledLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralSystemFaultLast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralCreateSupport"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrGeneralUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmHrGeneralGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrGeneralGroup.setDescription("""\
The Host Resources Extensions MIB General Group
""")

xcmHrDevCalendarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 10)
)
xcmHrDevCalendarGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarExplicitDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarCommandRequest"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCalendarCommandData"))
)
if mibBuilder.loadTexts:
    xcmHrDevCalendarGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCalendarGroup.setDescription("""\
The Host Resources Extensions MIB Device Calendar Group
""")

xcmHrSWRunGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 11)
)
xcmHrSWRunGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunAdminName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunRowCreateDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunPhysicalDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunLogicalDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunNextIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWRunPreviousIndex"))
)
if mibBuilder.loadTexts:
    xcmHrSWRunGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWRunGroup.setDescription("""\
The Host Resources Extensions MIB Software Running Ext Group
""")

xcmHrSWInstalledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 12)
)
xcmHrSWInstalledGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledAdminName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledRowCreateDate"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledPhysicalIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledLogicalIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledNextIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSWInstalledPreviousIndex"))
)
if mibBuilder.loadTexts:
    xcmHrSWInstalledGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSWInstalledGroup.setDescription("""\
The Host Resources Extensions MIB Software Installed Ext Group
""")

xcmHrDevDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 13)
)
xcmHrDevDetailGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailType"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailUnitClass"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailValueInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailValueOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailValueString"))
)
if mibBuilder.loadTexts:
    xcmHrDevDetailGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevDetailGroup.setDescription("""\
The Host Resources Extensions MIB Device Detail Group
""")

xcmHrStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 14)
)
xcmHrStorageGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageRealization"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageProductDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStoragePlatformDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStoragePagingDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageMatchingDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageSWRunIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageSWInstalledIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageNextIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStoragePreviousIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStoragePhysicalIndex"))
)
if mibBuilder.loadTexts:
    xcmHrStorageGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageGroup.setDescription("""\
The Host Resources Extensions MIB Storage Ext Group
""")

xcmHrStorageDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 15)
)
xcmHrStorageDetailGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailUnitClass"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailValueInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailValueOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrStorageDetailValueString"))
)
if mibBuilder.loadTexts:
    xcmHrStorageDetailGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrStorageDetailGroup.setDescription("""\
The Host Resources Extensions MIB Storage Detail Group
""")

xcmHrDevCoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 16)
)
xcmHrDevCoverGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverDescription"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverTypeCover"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevCoverStatusOpen"))
)
if mibBuilder.loadTexts:
    xcmHrDevCoverGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevCoverGroup.setDescription("""\
The Host Resources Extensions MIB Device Cover Group
""")

xcmHrDevAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 17)
)
xcmHrDevAlertGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertSeverityLevel"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertTrainingLevel"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertCodeInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertCodeString"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertDescription"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertReferenceOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertDateAndTime"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertTitle"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertHelpReference"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertReferenceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertReferenceLocation"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertDevAlertIndex"))
)
if mibBuilder.loadTexts:
    xcmHrDevAlertGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevAlertGroup.setDescription("""\
The Host Resources Extensions MIB Device Alert Group
""")

xcmHrConsoleScreenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 18)
)
xcmHrConsoleScreenGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenDescription"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenParentIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenPriority"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleScreenTabCount"))
)
if mibBuilder.loadTexts:
    xcmHrConsoleScreenGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleScreenGroup.setDescription("""\
The Host Resources Extensions MIB Console Screen Group
""")

xcmHrConsoleTabGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 19)
)
xcmHrConsoleTabGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabName"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabDescription"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabScreenIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTabPriority"))
)
if mibBuilder.loadTexts:
    xcmHrConsoleTabGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleTabGroup.setDescription("""\
The Host Resources Extensions MIB Console Tab Group
""")

xcmHrSuppliesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 20)
)
xcmHrSuppliesGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesReferenceOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesType"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesClass"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesDescr"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrSuppliesPartNumber"))
)
if mibBuilder.loadTexts:
    xcmHrSuppliesGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrSuppliesGroup.setDescription("""\
The Host Resources Extensions MIB Supplies Group
""")

xcmHrDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 21)
)
xcmHrDetailGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailUnitClass"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailUnit"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailValueInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailValueOID"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailValueString"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDetailDescription"))
)
if mibBuilder.loadTexts:
    xcmHrDetailGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDetailGroup.setDescription("""\
The Host Resources Extensions MIB Detail Group
""")

xcmHrConsoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 2, 22)
)
xcmHrConsoleGroup.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleDefaultService"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleBrightness"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleContrast"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleAccessibility"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleAutoClearTime"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleInsertTimeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTray1Timeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleTray2nTimeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleLoadTimeout"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleSoundVolume"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrConsoleSoundDuration"))
)
if mibBuilder.loadTexts:
    xcmHrConsoleGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrConsoleGroup.setDescription("""\
The Host Resources Extensions MIB Console Group
""")


# Notification objects

xcmHrDevInfoV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 3, 1, 0, 1)
)
xcmHrDevInfoV2Event.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("HOST-RESOURCES-MIB", "hrDeviceStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXConditions"))
)
if mibBuilder.loadTexts:
    xcmHrDevInfoV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmHrDevInfoV2Event.setDescription("""\
This trap is sent whenever 'hrDeviceStatus' and/or
'xcmHrDevInfo[XStatus|Conditions|XConditions]' changes. Note: The variable-
bindings of this trap have been chosen to specify a complete device status
change while keeping trap messages reasonably concise (generally a few hundred
octets at most). This notification has the following special semantics: o The
device's 'hrDeviceIndex' field value SHALL be appended to this trap object ID,
as a BER binary OID suffix. This trap OID qualifier allows device
management/monitoring applications to limit the alerts they receive to ones
generated by devices of interest.
""")

xcmHrDevMgmtV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 5, 1, 0, 1)
)
xcmHrDevMgmtV2Event.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("HOST-RESOURCES-MIB", "hrDeviceStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevInfoXConditions"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandRequest"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevMgmtCommandStatus"))
)
if mibBuilder.loadTexts:
    xcmHrDevMgmtV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmHrDevMgmtV2Event.setDescription("""\
This trap is sent whenever an 'XcmHrDevMgmtCommandRequest' completes, ie, when
'xcmHrDevMgmtCommandStatus' becomes the completed operation status and
'XcmHrDevMgmtCommandInProgress' goes from 'true' to 'false'. Note: The
variable-bindings of this trap have been chosen to specify a complete
management operation result while keeping trap messages reasonably concise
(generally a few hundred octets at most). This notification has the following
special semantics: o The device's 'hrDeviceIndex' field value SHALL be appended
to this trap object ID, as a BER binary OID suffix. This trap OID qualifier
allows device management/monitoring applications to limit the alerts they
receive to ones generated by requests they have submitted.
""")

xcmHrDevDetailV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 13, 1, 0, 1)
)
xcmHrDevDetailV2Event.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailType"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevDetailIndex"))
)
if mibBuilder.loadTexts:
    xcmHrDevDetailV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmHrDevDetailV2Event.setDescription("""\
This trap is sent when 'xcmHrDevDetailIndex' is shared between a counter detail
and a limit detail which are specified in 'xcmHrDevDetailValueInteger', OR when
'xcmHrDevDetailValueString' specifies a trigger date. Note: The variable-
bindings of this trap have been chosen to specify a complete device status
change while keeping trap messages reasonably concise (generally a few hundred
octets at most). This notification has the following special semantics: o The
detail's 'hrDeviceIndex' value, the detail's 'xcmHrDevDetailType' value, and
the detail's 'xcmHrDevDetailIndex' value SHALL be appended to this trap object
ID, as a BER binary OID suffix. This trap OID qualifier allows device
management/monitoring applications to limit the alerts they receive to ones
generated by device details of interest.
""")

xcmHrDevAlertV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 17, 1, 0, 1)
)
xcmHrDevAlertV2Event.setObjects(
      *(("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertRowStatus"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertSeverityLevel"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertTrainingLevel"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertCodeInteger"),
        ("XEROX-HOST-RESOURCES-EXT-MIB", "xcmHrDevAlertCodeString"))
)
if mibBuilder.loadTexts:
    xcmHrDevAlertV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmHrDevAlertV2Event.setDescription("""\
This trap is sent whenever a device alert row transitions to 'active' row
status or (optionally) transitions to 'notInService' row status in
'xcmHrDevAlertTable'. This trap is sent when requested by a prior subscription.
Note: The variable-bindings of this trap have been chosen to specify a complete
device alert event while keeping trap messages reasonably concise (generally a
few hundred octets at most). This notification has the following special
semantics: o The device's 'hrDeviceIndex' field value SHALL be appended to this
trap object ID, as a BER binary OID suffix. This trap OID qualifier allows
device management/monitoring applications to limit the alerts they receive to
ones generated by devices of interest. Systems MAY add other variable-bindings
from any MIB.
""")


# Notifications groups


# Agent capabilities


# Module compliance

xcmHrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 53, 2, 3)
)
if mibBuilder.loadTexts:
    xcmHrMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmHrMIBCompliance.setDescription("""\
The compliance statements for SNMP management agents that implement the Host
Resources Extensions MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-HOST-RESOURCES-EXT-MIB",
    **{"xcmHrZeroDummy": xcmHrZeroDummy,
       "xcmHrMIB": xcmHrMIB,
       "xcmHrMIBConformance": xcmHrMIBConformance,
       "xcmHrMIBGroups": xcmHrMIBGroups,
       "xcmHrDevInfoGroup": xcmHrDevInfoGroup,
       "xcmHrDevHelpGroup": xcmHrDevHelpGroup,
       "xcmHrDevMgmtGroup": xcmHrDevMgmtGroup,
       "xcmHrDevPowerGroup": xcmHrDevPowerGroup,
       "xcmHrDevTrafficGroup": xcmHrDevTrafficGroup,
       "xcmHrSystemFaultGroup": xcmHrSystemFaultGroup,
       "xcmHrGeneralGroup": xcmHrGeneralGroup,
       "xcmHrDevCalendarGroup": xcmHrDevCalendarGroup,
       "xcmHrSWRunGroup": xcmHrSWRunGroup,
       "xcmHrSWInstalledGroup": xcmHrSWInstalledGroup,
       "xcmHrDevDetailGroup": xcmHrDevDetailGroup,
       "xcmHrStorageGroup": xcmHrStorageGroup,
       "xcmHrStorageDetailGroup": xcmHrStorageDetailGroup,
       "xcmHrDevCoverGroup": xcmHrDevCoverGroup,
       "xcmHrDevAlertGroup": xcmHrDevAlertGroup,
       "xcmHrConsoleScreenGroup": xcmHrConsoleScreenGroup,
       "xcmHrConsoleTabGroup": xcmHrConsoleTabGroup,
       "xcmHrSuppliesGroup": xcmHrSuppliesGroup,
       "xcmHrDetailGroup": xcmHrDetailGroup,
       "xcmHrConsoleGroup": xcmHrConsoleGroup,
       "xcmHrMIBCompliance": xcmHrMIBCompliance,
       "xcmHrDevInfo": xcmHrDevInfo,
       "xcmHrDevInfoV1EventOID": xcmHrDevInfoV1EventOID,
       "xcmHrDevInfoV2EventPrefix": xcmHrDevInfoV2EventPrefix,
       "xcmHrDevInfoV2Event": xcmHrDevInfoV2Event,
       "xcmHrDevInfoTable": xcmHrDevInfoTable,
       "xcmHrDevInfoEntry": xcmHrDevInfoEntry,
       "xcmHrDevInfoRowStatus": xcmHrDevInfoRowStatus,
       "xcmHrDevInfoName": xcmHrDevInfoName,
       "xcmHrDevInfoSerialNumber": xcmHrDevInfoSerialNumber,
       "xcmHrDevInfoRealization": xcmHrDevInfoRealization,
       "xcmHrDevInfoXStatus": xcmHrDevInfoXStatus,
       "xcmHrDevInfoConditions": xcmHrDevInfoConditions,
       "xcmHrDevInfoXConditions": xcmHrDevInfoXConditions,
       "xcmHrDevInfoInstallDate": xcmHrDevInfoInstallDate,
       "xcmHrDevInfoResetDate": xcmHrDevInfoResetDate,
       "xcmHrDevInfoNextDeviceIndex": xcmHrDevInfoNextDeviceIndex,
       "xcmHrDevInfoPreviousDeviceIndex": xcmHrDevInfoPreviousDeviceIndex,
       "xcmHrDevInfoPhysicalDeviceIndex": xcmHrDevInfoPhysicalDeviceIndex,
       "xcmHrDevInfoPriority": xcmHrDevInfoPriority,
       "xcmHrDevInfoXeroxAssetTagNumber": xcmHrDevInfoXeroxAssetTagNumber,
       "xcmHrDevInfoCustomerAssetNumber": xcmHrDevInfoCustomerAssetNumber,
       "xcmHrDevInfoPagePackPIN": xcmHrDevInfoPagePackPIN,
       "xcmHrDevInfoPagePackReset": xcmHrDevInfoPagePackReset,
       "xcmHrDevInfoPagePackTimer": xcmHrDevInfoPagePackTimer,
       "xcmHrDevHelp": xcmHrDevHelp,
       "xcmHrDevHelpTable": xcmHrDevHelpTable,
       "xcmHrDevHelpEntry": xcmHrDevHelpEntry,
       "xcmHrDevHelpRowStatus": xcmHrDevHelpRowStatus,
       "xcmHrDevHelpOperatorMessage": xcmHrDevHelpOperatorMessage,
       "xcmHrDevHelpProblemMessage": xcmHrDevHelpProblemMessage,
       "xcmHrDevHelpCommsAddressIndex": xcmHrDevHelpCommsAddressIndex,
       "xcmHrDevMgmt": xcmHrDevMgmt,
       "xcmHrDevMgmtV1EventOID": xcmHrDevMgmtV1EventOID,
       "xcmHrDevMgmtV2EventPrefix": xcmHrDevMgmtV2EventPrefix,
       "xcmHrDevMgmtV2Event": xcmHrDevMgmtV2Event,
       "xcmHrDevMgmtTable": xcmHrDevMgmtTable,
       "xcmHrDevMgmtEntry": xcmHrDevMgmtEntry,
       "xcmHrDevMgmtRowStatus": xcmHrDevMgmtRowStatus,
       "xcmHrDevMgmtCommandRequest": xcmHrDevMgmtCommandRequest,
       "xcmHrDevMgmtCommandData": xcmHrDevMgmtCommandData,
       "xcmHrDevMgmtCommandStatus": xcmHrDevMgmtCommandStatus,
       "xcmHrDevMgmtUserPassword": xcmHrDevMgmtUserPassword,
       "xcmHrDevMgmtOperatorPassword": xcmHrDevMgmtOperatorPassword,
       "xcmHrDevMgmtAdminPassword": xcmHrDevMgmtAdminPassword,
       "xcmHrDevMgmtCommandInProgress": xcmHrDevMgmtCommandInProgress,
       "xcmHrDevMgmtUserName": xcmHrDevMgmtUserName,
       "xcmHrDevMgmtOperatorName": xcmHrDevMgmtOperatorName,
       "xcmHrDevMgmtAdminName": xcmHrDevMgmtAdminName,
       "xcmHrDevMgmtCustomPassword": xcmHrDevMgmtCustomPassword,
       "xcmHrDevPower": xcmHrDevPower,
       "xcmHrDevPowerTable": xcmHrDevPowerTable,
       "xcmHrDevPowerEntry": xcmHrDevPowerEntry,
       "xcmHrDevPowerRowStatus": xcmHrDevPowerRowStatus,
       "xcmHrDevPowerWarmUpSupport": xcmHrDevPowerWarmUpSupport,
       "xcmHrDevPowerCoolDownSupport": xcmHrDevPowerCoolDownSupport,
       "xcmHrDevPowerEnergySaveSupport": xcmHrDevPowerEnergySaveSupport,
       "xcmHrDevPowerTimeUnit": xcmHrDevPowerTimeUnit,
       "xcmHrDevPowerWarmUpDelay": xcmHrDevPowerWarmUpDelay,
       "xcmHrDevPowerWarmUpDuration": xcmHrDevPowerWarmUpDuration,
       "xcmHrDevPowerCoolDownDelay": xcmHrDevPowerCoolDownDelay,
       "xcmHrDevPowerCoolDownDuration": xcmHrDevPowerCoolDownDuration,
       "xcmHrDevPowerEnergySaveDelay": xcmHrDevPowerEnergySaveDelay,
       "xcmHrDevPowerEnergySaveDuration": xcmHrDevPowerEnergySaveDuration,
       "xcmHrDevPowerWakeUpSupport": xcmHrDevPowerWakeUpSupport,
       "xcmHrDevPowerWakeUpDelay": xcmHrDevPowerWakeUpDelay,
       "xcmHrDevPowerWakeUpDuration": xcmHrDevPowerWakeUpDuration,
       "xcmHrDevPowerShutdownDelay": xcmHrDevPowerShutdownDelay,
       "xcmHrDevPowerShutdownDuration": xcmHrDevPowerShutdownDuration,
       "xcmHrDevPowerStartupDelay": xcmHrDevPowerStartupDelay,
       "xcmHrDevPowerStartupDuration": xcmHrDevPowerStartupDuration,
       "xcmHrDevTraffic": xcmHrDevTraffic,
       "xcmHrDevTrafficTable": xcmHrDevTrafficTable,
       "xcmHrDevTrafficEntry": xcmHrDevTrafficEntry,
       "xcmHrDevTrafficRowStatus": xcmHrDevTrafficRowStatus,
       "xcmHrDevTrafficInputSupport": xcmHrDevTrafficInputSupport,
       "xcmHrDevTrafficOutputSupport": xcmHrDevTrafficOutputSupport,
       "xcmHrDevTrafficInputUnit": xcmHrDevTrafficInputUnit,
       "xcmHrDevTrafficOutputUnit": xcmHrDevTrafficOutputUnit,
       "xcmHrDevTrafficInputCount": xcmHrDevTrafficInputCount,
       "xcmHrDevTrafficOutputCount": xcmHrDevTrafficOutputCount,
       "xcmHrDevTrafficInputMaxSize": xcmHrDevTrafficInputMaxSize,
       "xcmHrDevTrafficOutputMaxSize": xcmHrDevTrafficOutputMaxSize,
       "xcmHrDevTrafficInputTimeout": xcmHrDevTrafficInputTimeout,
       "xcmHrDevTrafficOutputTimeout": xcmHrDevTrafficOutputTimeout,
       "xcmHrSystemFault": xcmHrSystemFault,
       "xcmHrSystemFaultTable": xcmHrSystemFaultTable,
       "xcmHrSystemFaultEntry": xcmHrSystemFaultEntry,
       "xcmHrSystemFaultIndex": xcmHrSystemFaultIndex,
       "xcmHrSystemFaultRowStatus": xcmHrSystemFaultRowStatus,
       "xcmHrSystemFaultCode": xcmHrSystemFaultCode,
       "xcmHrSystemFaultString": xcmHrSystemFaultString,
       "xcmHrSystemFaultReferenceOID": xcmHrSystemFaultReferenceOID,
       "xcmHrSystemFaultHrDeviceIndex": xcmHrSystemFaultHrDeviceIndex,
       "xcmHrSystemFaultDate": xcmHrSystemFaultDate,
       "xcmHrGeneral": xcmHrGeneral,
       "xcmHrGeneralTable": xcmHrGeneralTable,
       "xcmHrGeneralEntry": xcmHrGeneralEntry,
       "xcmHrGeneralIndex": xcmHrGeneralIndex,
       "xcmHrGeneralRowStatus": xcmHrGeneralRowStatus,
       "xcmHrGeneralVersionID": xcmHrGeneralVersionID,
       "xcmHrGeneralVersionDate": xcmHrGeneralVersionDate,
       "xcmHrGeneralGroupSupport": xcmHrGeneralGroupSupport,
       "xcmHrGeneralStorageLast": xcmHrGeneralStorageLast,
       "xcmHrGeneralDeviceLast": xcmHrGeneralDeviceLast,
       "xcmHrGeneralFSLast": xcmHrGeneralFSLast,
       "xcmHrGeneralSWRunLast": xcmHrGeneralSWRunLast,
       "xcmHrGeneralSWInstalledLast": xcmHrGeneralSWInstalledLast,
       "xcmHrGeneralSystemFaultLast": xcmHrGeneralSystemFaultLast,
       "xcmHrGeneralCreateSupport": xcmHrGeneralCreateSupport,
       "xcmHrGeneralUpdateSupport": xcmHrGeneralUpdateSupport,
       "xcmHrDevCalendar": xcmHrDevCalendar,
       "xcmHrDevCalendarTable": xcmHrDevCalendarTable,
       "xcmHrDevCalendarEntry": xcmHrDevCalendarEntry,
       "xcmHrDevCalendarDayOfWeek": xcmHrDevCalendarDayOfWeek,
       "xcmHrDevCalendarTimeOfDay": xcmHrDevCalendarTimeOfDay,
       "xcmHrDevCalendarRowStatus": xcmHrDevCalendarRowStatus,
       "xcmHrDevCalendarExplicitDate": xcmHrDevCalendarExplicitDate,
       "xcmHrDevCalendarCommandRequest": xcmHrDevCalendarCommandRequest,
       "xcmHrDevCalendarCommandData": xcmHrDevCalendarCommandData,
       "xcmHrSWRun": xcmHrSWRun,
       "xcmHrSWRunTable": xcmHrSWRunTable,
       "xcmHrSWRunEntry": xcmHrSWRunEntry,
       "xcmHrSWRunRowStatus": xcmHrSWRunRowStatus,
       "xcmHrSWRunAdminName": xcmHrSWRunAdminName,
       "xcmHrSWRunXStatus": xcmHrSWRunXStatus,
       "xcmHrSWRunRowCreateDate": xcmHrSWRunRowCreateDate,
       "xcmHrSWRunPhysicalDeviceIndex": xcmHrSWRunPhysicalDeviceIndex,
       "xcmHrSWRunLogicalDeviceIndex": xcmHrSWRunLogicalDeviceIndex,
       "xcmHrSWRunNextIndex": xcmHrSWRunNextIndex,
       "xcmHrSWRunPreviousIndex": xcmHrSWRunPreviousIndex,
       "xcmHrSWInstalled": xcmHrSWInstalled,
       "xcmHrSWInstalledTable": xcmHrSWInstalledTable,
       "xcmHrSWInstalledEntry": xcmHrSWInstalledEntry,
       "xcmHrSWInstalledRowStatus": xcmHrSWInstalledRowStatus,
       "xcmHrSWInstalledAdminName": xcmHrSWInstalledAdminName,
       "xcmHrSWInstalledXStatus": xcmHrSWInstalledXStatus,
       "xcmHrSWInstalledRowCreateDate": xcmHrSWInstalledRowCreateDate,
       "xcmHrSWInstalledPhysicalIndex": xcmHrSWInstalledPhysicalIndex,
       "xcmHrSWInstalledLogicalIndex": xcmHrSWInstalledLogicalIndex,
       "xcmHrSWInstalledNextIndex": xcmHrSWInstalledNextIndex,
       "xcmHrSWInstalledPreviousIndex": xcmHrSWInstalledPreviousIndex,
       "xcmHrDevDetail": xcmHrDevDetail,
       "xcmHrDevDetailV1EventOID": xcmHrDevDetailV1EventOID,
       "xcmHrDevDetailV2EventPrefix": xcmHrDevDetailV2EventPrefix,
       "xcmHrDevDetailV2Event": xcmHrDevDetailV2Event,
       "xcmHrDevDetailTable": xcmHrDevDetailTable,
       "xcmHrDevDetailEntry": xcmHrDevDetailEntry,
       "xcmHrDevDetailType": xcmHrDevDetailType,
       "xcmHrDevDetailIndex": xcmHrDevDetailIndex,
       "xcmHrDevDetailRowStatus": xcmHrDevDetailRowStatus,
       "xcmHrDevDetailUnitClass": xcmHrDevDetailUnitClass,
       "xcmHrDevDetailUnit": xcmHrDevDetailUnit,
       "xcmHrDevDetailValueInteger": xcmHrDevDetailValueInteger,
       "xcmHrDevDetailValueOID": xcmHrDevDetailValueOID,
       "xcmHrDevDetailValueString": xcmHrDevDetailValueString,
       "xcmHrDevDetailDescription": xcmHrDevDetailDescription,
       "xcmHrStorage": xcmHrStorage,
       "xcmHrStorageTable": xcmHrStorageTable,
       "xcmHrStorageEntry": xcmHrStorageEntry,
       "xcmHrStorageRowStatus": xcmHrStorageRowStatus,
       "xcmHrStorageRealization": xcmHrStorageRealization,
       "xcmHrStorageStatus": xcmHrStorageStatus,
       "xcmHrStorageProductDeviceIndex": xcmHrStorageProductDeviceIndex,
       "xcmHrStoragePlatformDeviceIndex": xcmHrStoragePlatformDeviceIndex,
       "xcmHrStoragePagingDeviceIndex": xcmHrStoragePagingDeviceIndex,
       "xcmHrStorageMatchingDeviceIndex": xcmHrStorageMatchingDeviceIndex,
       "xcmHrStorageSWRunIndex": xcmHrStorageSWRunIndex,
       "xcmHrStorageSWInstalledIndex": xcmHrStorageSWInstalledIndex,
       "xcmHrStorageNextIndex": xcmHrStorageNextIndex,
       "xcmHrStoragePreviousIndex": xcmHrStoragePreviousIndex,
       "xcmHrStoragePhysicalIndex": xcmHrStoragePhysicalIndex,
       "xcmHrStorageDetail": xcmHrStorageDetail,
       "xcmHrStorageDetailTable": xcmHrStorageDetailTable,
       "xcmHrStorageDetailEntry": xcmHrStorageDetailEntry,
       "xcmHrStorageDetailType": xcmHrStorageDetailType,
       "xcmHrStorageDetailIndex": xcmHrStorageDetailIndex,
       "xcmHrStorageDetailRowStatus": xcmHrStorageDetailRowStatus,
       "xcmHrStorageDetailUnitClass": xcmHrStorageDetailUnitClass,
       "xcmHrStorageDetailUnit": xcmHrStorageDetailUnit,
       "xcmHrStorageDetailValueInteger": xcmHrStorageDetailValueInteger,
       "xcmHrStorageDetailValueOID": xcmHrStorageDetailValueOID,
       "xcmHrStorageDetailValueString": xcmHrStorageDetailValueString,
       "xcmHrDevCover": xcmHrDevCover,
       "xcmHrDevCoverTable": xcmHrDevCoverTable,
       "xcmHrDevCoverEntry": xcmHrDevCoverEntry,
       "xcmHrDevCoverIndex": xcmHrDevCoverIndex,
       "xcmHrDevCoverRowStatus": xcmHrDevCoverRowStatus,
       "xcmHrDevCoverName": xcmHrDevCoverName,
       "xcmHrDevCoverDescription": xcmHrDevCoverDescription,
       "xcmHrDevCoverTypeCover": xcmHrDevCoverTypeCover,
       "xcmHrDevCoverStatusOpen": xcmHrDevCoverStatusOpen,
       "xcmHrDevAlert": xcmHrDevAlert,
       "xcmHrDevAlertV1EventOID": xcmHrDevAlertV1EventOID,
       "xcmHrDevAlertV2EventPrefix": xcmHrDevAlertV2EventPrefix,
       "xcmHrDevAlertV2Event": xcmHrDevAlertV2Event,
       "xcmHrDevAlertTable": xcmHrDevAlertTable,
       "xcmHrDevAlertEntry": xcmHrDevAlertEntry,
       "xcmHrDevAlertIndex": xcmHrDevAlertIndex,
       "xcmHrDevAlertRowStatus": xcmHrDevAlertRowStatus,
       "xcmHrDevAlertSeverityLevel": xcmHrDevAlertSeverityLevel,
       "xcmHrDevAlertTrainingLevel": xcmHrDevAlertTrainingLevel,
       "xcmHrDevAlertCodeInteger": xcmHrDevAlertCodeInteger,
       "xcmHrDevAlertCodeString": xcmHrDevAlertCodeString,
       "xcmHrDevAlertDescription": xcmHrDevAlertDescription,
       "xcmHrDevAlertReferenceOID": xcmHrDevAlertReferenceOID,
       "xcmHrDevAlertDateAndTime": xcmHrDevAlertDateAndTime,
       "xcmHrDevAlertTitle": xcmHrDevAlertTitle,
       "xcmHrDevAlertHelpReference": xcmHrDevAlertHelpReference,
       "xcmHrDevAlertReferenceIndex": xcmHrDevAlertReferenceIndex,
       "xcmHrDevAlertReferenceLocation": xcmHrDevAlertReferenceLocation,
       "xcmHrDevAlertDevAlertIndex": xcmHrDevAlertDevAlertIndex,
       "xcmHrDevAlertPriority": xcmHrDevAlertPriority,
       "xcmHrDevAlertLastAlertIndex": xcmHrDevAlertLastAlertIndex,
       "xcmHrDevAlertLastCriticalAlertIndex": xcmHrDevAlertLastCriticalAlertIndex,
       "xcmHrConsoleScreen": xcmHrConsoleScreen,
       "xcmHrConsoleScreenTable": xcmHrConsoleScreenTable,
       "xcmHrConsoleScreenEntry": xcmHrConsoleScreenEntry,
       "xcmHrConsoleScreenIndex": xcmHrConsoleScreenIndex,
       "xcmHrConsoleScreenName": xcmHrConsoleScreenName,
       "xcmHrConsoleScreenDescription": xcmHrConsoleScreenDescription,
       "xcmHrConsoleScreenParentIndex": xcmHrConsoleScreenParentIndex,
       "xcmHrConsoleScreenPriority": xcmHrConsoleScreenPriority,
       "xcmHrConsoleScreenTabCount": xcmHrConsoleScreenTabCount,
       "xcmHrConsoleTab": xcmHrConsoleTab,
       "xcmHrConsoleTabTable": xcmHrConsoleTabTable,
       "xcmHrConsoleTabEntry": xcmHrConsoleTabEntry,
       "xcmHrConsoleTabIndex": xcmHrConsoleTabIndex,
       "xcmHrConsoleTabName": xcmHrConsoleTabName,
       "xcmHrConsoleTabDescription": xcmHrConsoleTabDescription,
       "xcmHrConsoleTabScreenIndex": xcmHrConsoleTabScreenIndex,
       "xcmHrConsoleTabPriority": xcmHrConsoleTabPriority,
       "xcmHrSupplies": xcmHrSupplies,
       "xcmHrSuppliesTable": xcmHrSuppliesTable,
       "xcmHrSuppliesEntry": xcmHrSuppliesEntry,
       "xcmHrSuppliesIndex": xcmHrSuppliesIndex,
       "xcmHrSuppliesReferenceOID": xcmHrSuppliesReferenceOID,
       "xcmHrSuppliesType": xcmHrSuppliesType,
       "xcmHrSuppliesClass": xcmHrSuppliesClass,
       "xcmHrSuppliesDescr": xcmHrSuppliesDescr,
       "xcmHrSuppliesPartNumber": xcmHrSuppliesPartNumber,
       "xcmHrDetailTable": xcmHrDetailTable,
       "xcmHrDetailEntry": xcmHrDetailEntry,
       "xcmHrDetailTableRef": xcmHrDetailTableRef,
       "xcmHrDetailTableIndex": xcmHrDetailTableIndex,
       "xcmHrDetailType": xcmHrDetailType,
       "xcmHrDetailIndex": xcmHrDetailIndex,
       "xcmHrDetailUnitClass": xcmHrDetailUnitClass,
       "xcmHrDetailUnit": xcmHrDetailUnit,
       "xcmHrDetailValueInteger": xcmHrDetailValueInteger,
       "xcmHrDetailValueOID": xcmHrDetailValueOID,
       "xcmHrDetailValueString": xcmHrDetailValueString,
       "xcmHrDetailDescription": xcmHrDetailDescription,
       "xcmHrConsole": xcmHrConsole,
       "xcmHrConsoleTable": xcmHrConsoleTable,
       "xcmHrConsoleEntry": xcmHrConsoleEntry,
       "xcmHrConsoleIndex": xcmHrConsoleIndex,
       "xcmHrConsoleDefaultService": xcmHrConsoleDefaultService,
       "xcmHrConsoleBrightness": xcmHrConsoleBrightness,
       "xcmHrConsoleContrast": xcmHrConsoleContrast,
       "xcmHrConsoleAccessibility": xcmHrConsoleAccessibility,
       "xcmHrConsoleAutoClearTime": xcmHrConsoleAutoClearTime,
       "xcmHrConsoleInsertTimeout": xcmHrConsoleInsertTimeout,
       "xcmHrConsoleTray1Timeout": xcmHrConsoleTray1Timeout,
       "xcmHrConsoleTray2nTimeout": xcmHrConsoleTray2nTimeout,
       "xcmHrConsoleLoadTimeout": xcmHrConsoleLoadTimeout,
       "xcmHrConsoleSoundVolume": xcmHrConsoleSoundVolume,
       "xcmHrConsoleSoundDuration": xcmHrConsoleSoundDuration,
       "xcmHrGenericParamGroup": xcmHrGenericParamGroup,
       "xcmHrGenericParamName": xcmHrGenericParamName,
       "xcmHrGenericParamValue": xcmHrGenericParamValue}
)
