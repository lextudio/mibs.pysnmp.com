# SNMP MIB module (CISCO-ZS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ZS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:13 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

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

(FcGs3RejectReasonCode,) = mibBuilder.importSymbols(
    "CISCO-NS-MIB",
    "FcGs3RejectReasonCode")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(DomainIdOrZero,
 FcAddressId,
 FcNameId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainIdOrZero",
    "FcAddressId",
    "FcNameId",
    "VsanIndex")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoZsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294)
)
ciscoZsMIB.setRevisions(
        ("2005-11-10 00:00",
         "2005-04-07 00:00",
         "2004-09-01 00:00",
         "2004-01-27 00:00",
         "2003-12-12 00:00",
         "2003-08-25 00:00",
         "2003-08-01 00:00",
         "2003-03-26 00:00",
         "2003-01-17 00:00",
         "2002-11-08 00:00",
         "2002-10-28 00:00",
         "2002-10-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZoneMemberType(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("deviceAlias", 10),
          ("domainIntf", 7),
          ("domainPort", 2),
          ("fcAddr", 3),
          ("fwwn", 4),
          ("intf", 6),
          ("ipAddr", 8),
          ("ipAddrv6", 9),
          ("symNodeName", 5),
          ("wwn", 1))
    )



class FcZoneServerRejReasonExpl(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("capabilityNotSupported", 11),
          ("deactivateZoneSetFailed", 9),
          ("incorrectPayloadLen", 7),
          ("invalidZoneSetDefinition", 13),
          ("noAdditionalExplanation", 1),
          ("noZoneSetActive", 4),
          ("reqNotSupported", 10),
          ("tooLargeZoneSet", 8),
          ("zoneMemberIDTypeNotSupp", 12),
          ("zoneNameUnknown", 5),
          ("zoneSetNameUnknown", 3),
          ("zoneStateUnknown", 6),
          ("zonesNotSupported", 2))
    )



class FcList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class FcChangeProtoFailCause(Integer32, TextualConvention):
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("acaRetryExceed", 4),
          ("dbUpdateInProgress", 16),
          ("fabricChange", 9),
          ("fabricUnstable", 22),
          ("fc2SendFailed", 20),
          ("fc2SeqSizeExceed", 19),
          ("hwOperFailed", 18),
          ("invalidZsetFormat", 11),
          ("lcUpgradeInProgress", 24),
          ("nonInteropMember", 23),
          ("none", 1),
          ("notAuth", 8),
          ("rcvdSfcBusy", 2),
          ("rcvdUfcBusy", 3),
          ("sfcRetryExceed", 5),
          ("systemErr", 12),
          ("ufcRetryExceed", 6),
          ("unsuppCmd", 7),
          ("updateNotStaged", 10),
          ("vsanInactive", 14),
          ("vsanNotPresent", 13),
          ("zsetNotActive", 17),
          ("zsetNotPresent", 15),
          ("zsetUnchangedAndActive", 21))
    )



class ZoneCopyProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("scp", 4),
          ("sftp", 3),
          ("tftp", 1))
    )



class ZoneFileType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localFile", 2),
          ("networkFile", 1))
    )



class ZoneQosPriorityLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("none", 1))
    )



class ZoneMergeFailCause(Integer32, TextualConvention):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("bcastAttrMissing", 9),
          ("bcastNotEnabled", 5),
          ("defZoneMismatch", 7),
          ("invPayloadFormat", 12),
          ("memberMismatch", 11),
          ("mergeCtrlMismatch", 6),
          ("nonInteropZoneset", 15),
          ("other", 1),
          ("qosAttrMissing", 8),
          ("qosConflict", 4),
          ("qosNotEnabled", 3),
          ("rdonlyAttrMissing", 10),
          ("sizeExceeded", 13),
          ("unlicensedMember", 14),
          ("zoningModeMismatch", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoZoningMIBObjects_ObjectIdentity = ObjectIdentity
ciscoZoningMIBObjects = _CiscoZoningMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1)
)
_ZoneConfiguration_ObjectIdentity = ObjectIdentity
zoneConfiguration = _ZoneConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1)
)
_ZoneDefaultZoneTable_Object = MibTable
zoneDefaultZoneTable = _ZoneDefaultZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zoneDefaultZoneTable.setStatus("current")
_ZoneDefaultZoneEntry_Object = MibTableRow
zoneDefaultZoneEntry = _ZoneDefaultZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 1, 1)
)
zoneDefaultZoneEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    zoneDefaultZoneEntry.setStatus("current")


class _ZoneDefaultZoneBehaviour_Type(Integer32):
    """Custom type zoneDefaultZoneBehaviour based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_ZoneDefaultZoneBehaviour_Type.__name__ = "Integer32"
_ZoneDefaultZoneBehaviour_Object = MibTableColumn
zoneDefaultZoneBehaviour = _ZoneDefaultZoneBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 1, 1, 1),
    _ZoneDefaultZoneBehaviour_Type()
)
zoneDefaultZoneBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneDefaultZoneBehaviour.setStatus("current")


class _ZoneDefaultZoneReadOnly_Type(TruthValue):
    """Custom type zoneDefaultZoneReadOnly based on TruthValue"""


_ZoneDefaultZoneReadOnly_Object = MibTableColumn
zoneDefaultZoneReadOnly = _ZoneDefaultZoneReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 1, 1, 2),
    _ZoneDefaultZoneReadOnly_Type()
)
zoneDefaultZoneReadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneDefaultZoneReadOnly.setStatus("current")
_ZoneDefaultZoneQos_Type = TruthValue
_ZoneDefaultZoneQos_Object = MibTableColumn
zoneDefaultZoneQos = _ZoneDefaultZoneQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 1, 1, 3),
    _ZoneDefaultZoneQos_Type()
)
zoneDefaultZoneQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneDefaultZoneQos.setStatus("current")


class _ZoneDefaultZoneQosPriority_Type(ZoneQosPriorityLevel):
    """Custom type zoneDefaultZoneQosPriority based on ZoneQosPriorityLevel"""


_ZoneDefaultZoneQosPriority_Object = MibTableColumn
zoneDefaultZoneQosPriority = _ZoneDefaultZoneQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 1, 1, 4),
    _ZoneDefaultZoneQosPriority_Type()
)
zoneDefaultZoneQosPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneDefaultZoneQosPriority.setStatus("current")
_ZoneDefaultZoneBroadcast_Type = TruthValue
_ZoneDefaultZoneBroadcast_Object = MibTableColumn
zoneDefaultZoneBroadcast = _ZoneDefaultZoneBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 1, 1, 5),
    _ZoneDefaultZoneBroadcast_Type()
)
zoneDefaultZoneBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneDefaultZoneBroadcast.setStatus("current")
_ZoneSetPropagationTable_Object = MibTable
zoneSetPropagationTable = _ZoneSetPropagationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zoneSetPropagationTable.setStatus("current")
_ZoneSetPropagationEntry_Object = MibTableRow
zoneSetPropagationEntry = _ZoneSetPropagationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 2, 1)
)
zoneSetPropagationEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    zoneSetPropagationEntry.setStatus("current")


class _ZoneSetPropagationMode_Type(Integer32):
    """Custom type zoneSetPropagationMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeZoneSet", 2),
          ("fullZoneSet", 1))
    )


_ZoneSetPropagationMode_Type.__name__ = "Integer32"
_ZoneSetPropagationMode_Object = MibTableColumn
zoneSetPropagationMode = _ZoneSetPropagationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 2, 1, 1),
    _ZoneSetPropagationMode_Type()
)
zoneSetPropagationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneSetPropagationMode.setStatus("current")


class _ZoneSetNumber_Type(Integer32):
    """Custom type zoneSetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_ZoneSetNumber_Type.__name__ = "Integer32"
_ZoneSetNumber_Object = MibScalar
zoneSetNumber = _ZoneSetNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 3),
    _ZoneSetNumber_Type()
)
zoneSetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneSetNumber.setStatus("current")
_ZoneSetTable_Object = MibTable
zoneSetTable = _ZoneSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 4)
)
if mibBuilder.loadTexts:
    zoneSetTable.setStatus("current")
_ZoneSetEntry_Object = MibTableRow
zoneSetEntry = _ZoneSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 4, 1)
)
zoneSetEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneSetIndex"),
)
if mibBuilder.loadTexts:
    zoneSetEntry.setStatus("current")


class _ZoneSetIndex_Type(Unsigned32):
    """Custom type zoneSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ZoneSetIndex_Type.__name__ = "Unsigned32"
_ZoneSetIndex_Object = MibTableColumn
zoneSetIndex = _ZoneSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 4, 1, 1),
    _ZoneSetIndex_Type()
)
zoneSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneSetIndex.setStatus("current")


class _ZoneSetName_Type(SnmpAdminString):
    """Custom type zoneSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneSetName_Type.__name__ = "SnmpAdminString"
_ZoneSetName_Object = MibTableColumn
zoneSetName = _ZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 4, 1, 2),
    _ZoneSetName_Type()
)
zoneSetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetName.setStatus("current")


class _ZoneSetZoneList_Type(FcList):
    """Custom type zoneSetZoneList based on FcList"""
    defaultHexValue = ""


_ZoneSetZoneList_Object = MibTableColumn
zoneSetZoneList = _ZoneSetZoneList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 4, 1, 3),
    _ZoneSetZoneList_Type()
)
zoneSetZoneList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetZoneList.setStatus("current")
_ZoneSetLastChange_Type = TimeStamp
_ZoneSetLastChange_Object = MibTableColumn
zoneSetLastChange = _ZoneSetLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 4, 1, 4),
    _ZoneSetLastChange_Type()
)
zoneSetLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneSetLastChange.setStatus("current")
_ZoneSetRowStatus_Type = RowStatus
_ZoneSetRowStatus_Object = MibTableColumn
zoneSetRowStatus = _ZoneSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 4, 1, 5),
    _ZoneSetRowStatus_Type()
)
zoneSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetRowStatus.setStatus("current")


class _ZoneSetClone_Type(SnmpAdminString):
    """Custom type zoneSetClone based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneSetClone_Type.__name__ = "SnmpAdminString"
_ZoneSetClone_Object = MibTableColumn
zoneSetClone = _ZoneSetClone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 4, 1, 6),
    _ZoneSetClone_Type()
)
zoneSetClone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetClone.setStatus("current")
_ZoneSetActivateTable_Object = MibTable
zoneSetActivateTable = _ZoneSetActivateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 5)
)
if mibBuilder.loadTexts:
    zoneSetActivateTable.setStatus("current")
_ZoneSetActivateEntry_Object = MibTableRow
zoneSetActivateEntry = _ZoneSetActivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 5, 1)
)
zoneSetActivateEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    zoneSetActivateEntry.setStatus("current")


class _ZoneSetActivate_Type(Unsigned32):
    """Custom type zoneSetActivate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ZoneSetActivate_Type.__name__ = "Unsigned32"
_ZoneSetActivate_Object = MibTableColumn
zoneSetActivate = _ZoneSetActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 5, 1, 1),
    _ZoneSetActivate_Type()
)
zoneSetActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetActivate.setStatus("current")


class _ZoneSetActivateResult_Type(Integer32):
    """Custom type zoneSetActivateResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("activateFailure", 2),
          ("activateSuccess", 1),
          ("deactivateFailure", 4),
          ("deactivateSuccess", 3),
          ("inProgress", 5),
          ("newEntry", 6))
    )


_ZoneSetActivateResult_Type.__name__ = "Integer32"
_ZoneSetActivateResult_Object = MibTableColumn
zoneSetActivateResult = _ZoneSetActivateResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 5, 1, 2),
    _ZoneSetActivateResult_Type()
)
zoneSetActivateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneSetActivateResult.setStatus("current")


class _ZoneSetDeActivate_Type(Integer32):
    """Custom type zoneSetDeActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deactivate", 1),
          ("noop", 2))
    )


_ZoneSetDeActivate_Type.__name__ = "Integer32"
_ZoneSetDeActivate_Object = MibTableColumn
zoneSetDeActivate = _ZoneSetDeActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 5, 1, 3),
    _ZoneSetDeActivate_Type()
)
zoneSetDeActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetDeActivate.setStatus("current")
_ZoneSetActivateRowStatus_Type = RowStatus
_ZoneSetActivateRowStatus_Object = MibTableColumn
zoneSetActivateRowStatus = _ZoneSetActivateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 5, 1, 4),
    _ZoneSetActivateRowStatus_Type()
)
zoneSetActivateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetActivateRowStatus.setStatus("current")
_ZoneSetFailCause_Type = FcChangeProtoFailCause
_ZoneSetFailCause_Object = MibTableColumn
zoneSetFailCause = _ZoneSetFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 5, 1, 5),
    _ZoneSetFailCause_Type()
)
zoneSetFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneSetFailCause.setStatus("current")
_ZoneSetFailDomId_Type = DomainIdOrZero
_ZoneSetFailDomId_Object = MibTableColumn
zoneSetFailDomId = _ZoneSetFailDomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 5, 1, 6),
    _ZoneSetFailDomId_Type()
)
zoneSetFailDomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneSetFailDomId.setStatus("current")


class _ZoneNumber_Type(Integer32):
    """Custom type zoneNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_ZoneNumber_Type.__name__ = "Integer32"
_ZoneNumber_Object = MibScalar
zoneNumber = _ZoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 6),
    _ZoneNumber_Type()
)
zoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneNumber.setStatus("current")
_ZoneTable_Object = MibTable
zoneTable = _ZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7)
)
if mibBuilder.loadTexts:
    zoneTable.setStatus("current")
_ZoneEntry_Object = MibTableRow
zoneEntry = _ZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1)
)
zoneEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneIndex"),
)
if mibBuilder.loadTexts:
    zoneEntry.setStatus("current")


class _ZoneIndex_Type(Unsigned32):
    """Custom type zoneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_ZoneIndex_Type.__name__ = "Unsigned32"
_ZoneIndex_Object = MibTableColumn
zoneIndex = _ZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 1),
    _ZoneIndex_Type()
)
zoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneIndex.setStatus("current")


class _ZoneName_Type(SnmpAdminString):
    """Custom type zoneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneName_Type.__name__ = "SnmpAdminString"
_ZoneName_Object = MibTableColumn
zoneName = _ZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 2),
    _ZoneName_Type()
)
zoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneName.setStatus("current")


class _ZoneMemberList_Type(FcList):
    """Custom type zoneMemberList based on FcList"""
    defaultHexValue = ""


_ZoneMemberList_Object = MibTableColumn
zoneMemberList = _ZoneMemberList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 3),
    _ZoneMemberList_Type()
)
zoneMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneMemberList.setStatus("current")


class _ZoneAliasList_Type(FcList):
    """Custom type zoneAliasList based on FcList"""
    defaultHexValue = ""


_ZoneAliasList_Object = MibTableColumn
zoneAliasList = _ZoneAliasList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 4),
    _ZoneAliasList_Type()
)
zoneAliasList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneAliasList.setStatus("current")
_ZoneLastChange_Type = TimeStamp
_ZoneLastChange_Object = MibTableColumn
zoneLastChange = _ZoneLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 5),
    _ZoneLastChange_Type()
)
zoneLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneLastChange.setStatus("current")
_ZoneRowStatus_Type = RowStatus
_ZoneRowStatus_Object = MibTableColumn
zoneRowStatus = _ZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 6),
    _ZoneRowStatus_Type()
)
zoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneRowStatus.setStatus("current")


class _ZoneReadOnly_Type(TruthValue):
    """Custom type zoneReadOnly based on TruthValue"""


_ZoneReadOnly_Object = MibTableColumn
zoneReadOnly = _ZoneReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 7),
    _ZoneReadOnly_Type()
)
zoneReadOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneReadOnly.setStatus("current")


class _ZoneQos_Type(TruthValue):
    """Custom type zoneQos based on TruthValue"""


_ZoneQos_Object = MibTableColumn
zoneQos = _ZoneQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 8),
    _ZoneQos_Type()
)
zoneQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneQos.setStatus("current")


class _ZoneQosPriority_Type(ZoneQosPriorityLevel):
    """Custom type zoneQosPriority based on ZoneQosPriorityLevel"""


_ZoneQosPriority_Object = MibTableColumn
zoneQosPriority = _ZoneQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 9),
    _ZoneQosPriority_Type()
)
zoneQosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneQosPriority.setStatus("current")


class _ZoneBroadcast_Type(TruthValue):
    """Custom type zoneBroadcast based on TruthValue"""


_ZoneBroadcast_Object = MibTableColumn
zoneBroadcast = _ZoneBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 10),
    _ZoneBroadcast_Type()
)
zoneBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneBroadcast.setStatus("current")


class _ZoneClone_Type(SnmpAdminString):
    """Custom type zoneClone based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneClone_Type.__name__ = "SnmpAdminString"
_ZoneClone_Object = MibTableColumn
zoneClone = _ZoneClone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 7, 1, 11),
    _ZoneClone_Type()
)
zoneClone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneClone.setStatus("current")


class _ZoneAliasNumber_Type(Integer32):
    """Custom type zoneAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_ZoneAliasNumber_Type.__name__ = "Integer32"
_ZoneAliasNumber_Object = MibScalar
zoneAliasNumber = _ZoneAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 8),
    _ZoneAliasNumber_Type()
)
zoneAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneAliasNumber.setStatus("current")
_ZoneAliasTable_Object = MibTable
zoneAliasTable = _ZoneAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 9)
)
if mibBuilder.loadTexts:
    zoneAliasTable.setStatus("current")
_ZoneAliasEntry_Object = MibTableRow
zoneAliasEntry = _ZoneAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 9, 1)
)
zoneAliasEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneAliasIndex"),
)
if mibBuilder.loadTexts:
    zoneAliasEntry.setStatus("current")


class _ZoneAliasIndex_Type(Unsigned32):
    """Custom type zoneAliasIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ZoneAliasIndex_Type.__name__ = "Unsigned32"
_ZoneAliasIndex_Object = MibTableColumn
zoneAliasIndex = _ZoneAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 9, 1, 1),
    _ZoneAliasIndex_Type()
)
zoneAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneAliasIndex.setStatus("current")


class _ZoneAliasName_Type(SnmpAdminString):
    """Custom type zoneAliasName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneAliasName_Type.__name__ = "SnmpAdminString"
_ZoneAliasName_Object = MibTableColumn
zoneAliasName = _ZoneAliasName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 9, 1, 2),
    _ZoneAliasName_Type()
)
zoneAliasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneAliasName.setStatus("current")


class _ZoneAliasMemberList_Type(FcList):
    """Custom type zoneAliasMemberList based on FcList"""
    defaultHexValue = ""


_ZoneAliasMemberList_Object = MibTableColumn
zoneAliasMemberList = _ZoneAliasMemberList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 9, 1, 3),
    _ZoneAliasMemberList_Type()
)
zoneAliasMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneAliasMemberList.setStatus("current")
_ZoneAliasRowStatus_Type = RowStatus
_ZoneAliasRowStatus_Object = MibTableColumn
zoneAliasRowStatus = _ZoneAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 9, 1, 4),
    _ZoneAliasRowStatus_Type()
)
zoneAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneAliasRowStatus.setStatus("current")
_ZoneAliasLastChange_Type = TimeStamp
_ZoneAliasLastChange_Object = MibTableColumn
zoneAliasLastChange = _ZoneAliasLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 9, 1, 5),
    _ZoneAliasLastChange_Type()
)
zoneAliasLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneAliasLastChange.setStatus("current")


class _ZoneAliasClone_Type(SnmpAdminString):
    """Custom type zoneAliasClone based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneAliasClone_Type.__name__ = "SnmpAdminString"
_ZoneAliasClone_Object = MibTableColumn
zoneAliasClone = _ZoneAliasClone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 9, 1, 6),
    _ZoneAliasClone_Type()
)
zoneAliasClone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneAliasClone.setStatus("current")


class _ZoneMemberNumber_Type(Integer32):
    """Custom type zoneMemberNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )


_ZoneMemberNumber_Type.__name__ = "Integer32"
_ZoneMemberNumber_Object = MibScalar
zoneMemberNumber = _ZoneMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 10),
    _ZoneMemberNumber_Type()
)
zoneMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneMemberNumber.setStatus("current")
_ZoneMemberTable_Object = MibTable
zoneMemberTable = _ZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11)
)
if mibBuilder.loadTexts:
    zoneMemberTable.setStatus("current")
_ZoneMemberEntry_Object = MibTableRow
zoneMemberEntry = _ZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11, 1)
)
zoneMemberEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneMemberTypeIndex"),
    (0, "CISCO-ZS-MIB", "zoneMemberParentIndex"),
    (0, "CISCO-ZS-MIB", "zoneMemberIndex"),
)
if mibBuilder.loadTexts:
    zoneMemberEntry.setStatus("current")


class _ZoneMemberTypeIndex_Type(Integer32):
    """Custom type zoneMemberTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alias", 2),
          ("zone", 1))
    )


_ZoneMemberTypeIndex_Type.__name__ = "Integer32"
_ZoneMemberTypeIndex_Object = MibTableColumn
zoneMemberTypeIndex = _ZoneMemberTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11, 1, 1),
    _ZoneMemberTypeIndex_Type()
)
zoneMemberTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneMemberTypeIndex.setStatus("current")


class _ZoneMemberParentIndex_Type(Unsigned32):
    """Custom type zoneMemberParentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_ZoneMemberParentIndex_Type.__name__ = "Unsigned32"
_ZoneMemberParentIndex_Object = MibTableColumn
zoneMemberParentIndex = _ZoneMemberParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11, 1, 2),
    _ZoneMemberParentIndex_Type()
)
zoneMemberParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneMemberParentIndex.setStatus("current")


class _ZoneMemberIndex_Type(Unsigned32):
    """Custom type zoneMemberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ZoneMemberIndex_Type.__name__ = "Unsigned32"
_ZoneMemberIndex_Object = MibTableColumn
zoneMemberIndex = _ZoneMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11, 1, 3),
    _ZoneMemberIndex_Type()
)
zoneMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneMemberIndex.setStatus("current")
_ZoneMemberFormat_Type = ZoneMemberType
_ZoneMemberFormat_Object = MibTableColumn
zoneMemberFormat = _ZoneMemberFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11, 1, 4),
    _ZoneMemberFormat_Type()
)
zoneMemberFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneMemberFormat.setStatus("current")


class _ZoneMemberID_Type(OctetString):
    """Custom type zoneMemberID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZoneMemberID_Type.__name__ = "OctetString"
_ZoneMemberID_Object = MibTableColumn
zoneMemberID = _ZoneMemberID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11, 1, 5),
    _ZoneMemberID_Type()
)
zoneMemberID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneMemberID.setStatus("current")


class _ZoneMemberLunID_Type(OctetString):
    """Custom type zoneMemberLunID based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_ZoneMemberLunID_Type.__name__ = "OctetString"
_ZoneMemberLunID_Object = MibTableColumn
zoneMemberLunID = _ZoneMemberLunID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11, 1, 6),
    _ZoneMemberLunID_Type()
)
zoneMemberLunID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneMemberLunID.setStatus("current")
_ZoneMemberRowStatus_Type = RowStatus
_ZoneMemberRowStatus_Object = MibTableColumn
zoneMemberRowStatus = _ZoneMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 11, 1, 7),
    _ZoneMemberRowStatus_Type()
)
zoneMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneMemberRowStatus.setStatus("current")


class _ZoneEnforcedZoneSetNumber_Type(Integer32):
    """Custom type zoneEnforcedZoneSetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ZoneEnforcedZoneSetNumber_Type.__name__ = "Integer32"
_ZoneEnforcedZoneSetNumber_Object = MibScalar
zoneEnforcedZoneSetNumber = _ZoneEnforcedZoneSetNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 12),
    _ZoneEnforcedZoneSetNumber_Type()
)
zoneEnforcedZoneSetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneSetNumber.setStatus("current")
_ZoneEnforcedZoneSetTable_Object = MibTable
zoneEnforcedZoneSetTable = _ZoneEnforcedZoneSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 13)
)
if mibBuilder.loadTexts:
    zoneEnforcedZoneSetTable.setStatus("current")
_ZoneEnforcedZoneSetEntry_Object = MibTableRow
zoneEnforcedZoneSetEntry = _ZoneEnforcedZoneSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 13, 1)
)
zoneEnforcedZoneSetEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    zoneEnforcedZoneSetEntry.setStatus("current")


class _ZoneEnforcedZoneSetName_Type(SnmpAdminString):
    """Custom type zoneEnforcedZoneSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneEnforcedZoneSetName_Type.__name__ = "SnmpAdminString"
_ZoneEnforcedZoneSetName_Object = MibTableColumn
zoneEnforcedZoneSetName = _ZoneEnforcedZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 13, 1, 1),
    _ZoneEnforcedZoneSetName_Type()
)
zoneEnforcedZoneSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneSetName.setStatus("current")
_ZoneEnforcedZoneSetZoneList_Type = FcList
_ZoneEnforcedZoneSetZoneList_Object = MibTableColumn
zoneEnforcedZoneSetZoneList = _ZoneEnforcedZoneSetZoneList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 13, 1, 2),
    _ZoneEnforcedZoneSetZoneList_Type()
)
zoneEnforcedZoneSetZoneList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneSetZoneList.setStatus("current")
_ZoneEnforcedZoneSetActivateTime_Type = TimeStamp
_ZoneEnforcedZoneSetActivateTime_Object = MibTableColumn
zoneEnforcedZoneSetActivateTime = _ZoneEnforcedZoneSetActivateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 13, 1, 3),
    _ZoneEnforcedZoneSetActivateTime_Type()
)
zoneEnforcedZoneSetActivateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneSetActivateTime.setStatus("current")


class _ZoneEnforcedZoneNumber_Type(Integer32):
    """Custom type zoneEnforcedZoneNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_ZoneEnforcedZoneNumber_Type.__name__ = "Integer32"
_ZoneEnforcedZoneNumber_Object = MibScalar
zoneEnforcedZoneNumber = _ZoneEnforcedZoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 14),
    _ZoneEnforcedZoneNumber_Type()
)
zoneEnforcedZoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneNumber.setStatus("current")
_ZoneEnforcedZoneTable_Object = MibTable
zoneEnforcedZoneTable = _ZoneEnforcedZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15)
)
if mibBuilder.loadTexts:
    zoneEnforcedZoneTable.setStatus("current")
_ZoneEnforcedZoneEntry_Object = MibTableRow
zoneEnforcedZoneEntry = _ZoneEnforcedZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1)
)
zoneEnforcedZoneEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneIndex"),
)
if mibBuilder.loadTexts:
    zoneEnforcedZoneEntry.setStatus("current")


class _ZoneEnforcedZoneName_Type(SnmpAdminString):
    """Custom type zoneEnforcedZoneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneEnforcedZoneName_Type.__name__ = "SnmpAdminString"
_ZoneEnforcedZoneName_Object = MibTableColumn
zoneEnforcedZoneName = _ZoneEnforcedZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1, 1),
    _ZoneEnforcedZoneName_Type()
)
zoneEnforcedZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneName.setStatus("current")
_ZoneEnforcedZoneMemberList_Type = FcList
_ZoneEnforcedZoneMemberList_Object = MibTableColumn
zoneEnforcedZoneMemberList = _ZoneEnforcedZoneMemberList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1, 2),
    _ZoneEnforcedZoneMemberList_Type()
)
zoneEnforcedZoneMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneMemberList.setStatus("current")
_ZoneEnforcedZoneAliasList_Type = FcList
_ZoneEnforcedZoneAliasList_Object = MibTableColumn
zoneEnforcedZoneAliasList = _ZoneEnforcedZoneAliasList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1, 3),
    _ZoneEnforcedZoneAliasList_Type()
)
zoneEnforcedZoneAliasList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneAliasList.setStatus("current")
_ZoneEnforcedZoneActivateTime_Type = TimeStamp
_ZoneEnforcedZoneActivateTime_Object = MibTableColumn
zoneEnforcedZoneActivateTime = _ZoneEnforcedZoneActivateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1, 4),
    _ZoneEnforcedZoneActivateTime_Type()
)
zoneEnforcedZoneActivateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneActivateTime.setStatus("current")
_ZoneEnforcedZoneReadOnly_Type = TruthValue
_ZoneEnforcedZoneReadOnly_Object = MibTableColumn
zoneEnforcedZoneReadOnly = _ZoneEnforcedZoneReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1, 5),
    _ZoneEnforcedZoneReadOnly_Type()
)
zoneEnforcedZoneReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneReadOnly.setStatus("current")
_ZoneEnforcedZoneQos_Type = TruthValue
_ZoneEnforcedZoneQos_Object = MibTableColumn
zoneEnforcedZoneQos = _ZoneEnforcedZoneQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1, 6),
    _ZoneEnforcedZoneQos_Type()
)
zoneEnforcedZoneQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneQos.setStatus("current")
_ZoneEnforcedZoneQosPriority_Type = ZoneQosPriorityLevel
_ZoneEnforcedZoneQosPriority_Object = MibTableColumn
zoneEnforcedZoneQosPriority = _ZoneEnforcedZoneQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1, 7),
    _ZoneEnforcedZoneQosPriority_Type()
)
zoneEnforcedZoneQosPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneQosPriority.setStatus("current")
_ZoneEnforcedZoneBroadcast_Type = TruthValue
_ZoneEnforcedZoneBroadcast_Object = MibTableColumn
zoneEnforcedZoneBroadcast = _ZoneEnforcedZoneBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 15, 1, 8),
    _ZoneEnforcedZoneBroadcast_Type()
)
zoneEnforcedZoneBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneBroadcast.setStatus("current")


class _ZoneEnforcedZoneAliasNumber_Type(Integer32):
    """Custom type zoneEnforcedZoneAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8488608),
    )


_ZoneEnforcedZoneAliasNumber_Type.__name__ = "Integer32"
_ZoneEnforcedZoneAliasNumber_Object = MibScalar
zoneEnforcedZoneAliasNumber = _ZoneEnforcedZoneAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 16),
    _ZoneEnforcedZoneAliasNumber_Type()
)
zoneEnforcedZoneAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneAliasNumber.setStatus("deprecated")
_ZoneEnforcedZoneAliasTable_Object = MibTable
zoneEnforcedZoneAliasTable = _ZoneEnforcedZoneAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 17)
)
if mibBuilder.loadTexts:
    zoneEnforcedZoneAliasTable.setStatus("deprecated")
_ZoneEnforcedZoneAliasEntry_Object = MibTableRow
zoneEnforcedZoneAliasEntry = _ZoneEnforcedZoneAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 17, 1)
)
zoneEnforcedZoneAliasEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneAliasIndex"),
)
if mibBuilder.loadTexts:
    zoneEnforcedZoneAliasEntry.setStatus("deprecated")


class _ZoneEnforcedZoneAliasName_Type(SnmpAdminString):
    """Custom type zoneEnforcedZoneAliasName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZoneEnforcedZoneAliasName_Type.__name__ = "SnmpAdminString"
_ZoneEnforcedZoneAliasName_Object = MibTableColumn
zoneEnforcedZoneAliasName = _ZoneEnforcedZoneAliasName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 17, 1, 1),
    _ZoneEnforcedZoneAliasName_Type()
)
zoneEnforcedZoneAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneAliasName.setStatus("deprecated")
_ZoneEnforcedZoneAliasMemberList_Type = FcList
_ZoneEnforcedZoneAliasMemberList_Object = MibTableColumn
zoneEnforcedZoneAliasMemberList = _ZoneEnforcedZoneAliasMemberList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 17, 1, 2),
    _ZoneEnforcedZoneAliasMemberList_Type()
)
zoneEnforcedZoneAliasMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneAliasMemberList.setStatus("deprecated")


class _ZoneEnforcedZoneMemberNumber_Type(Integer32):
    """Custom type zoneEnforcedZoneMemberNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )


_ZoneEnforcedZoneMemberNumber_Type.__name__ = "Integer32"
_ZoneEnforcedZoneMemberNumber_Object = MibScalar
zoneEnforcedZoneMemberNumber = _ZoneEnforcedZoneMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 18),
    _ZoneEnforcedZoneMemberNumber_Type()
)
zoneEnforcedZoneMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneMemberNumber.setStatus("current")
_ZoneEnforcedZoneMemberTable_Object = MibTable
zoneEnforcedZoneMemberTable = _ZoneEnforcedZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 19)
)
if mibBuilder.loadTexts:
    zoneEnforcedZoneMemberTable.setStatus("current")
_ZoneEnforcedZoneMemberEntry_Object = MibTableRow
zoneEnforcedZoneMemberEntry = _ZoneEnforcedZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 19, 1)
)
zoneEnforcedZoneMemberEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneMemberTypeIndex"),
    (0, "CISCO-ZS-MIB", "zoneMemberParentIndex"),
    (0, "CISCO-ZS-MIB", "zoneMemberIndex"),
)
if mibBuilder.loadTexts:
    zoneEnforcedZoneMemberEntry.setStatus("current")
_ZoneEnforcedZoneMemberFormat_Type = ZoneMemberType
_ZoneEnforcedZoneMemberFormat_Object = MibTableColumn
zoneEnforcedZoneMemberFormat = _ZoneEnforcedZoneMemberFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 19, 1, 1),
    _ZoneEnforcedZoneMemberFormat_Type()
)
zoneEnforcedZoneMemberFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneMemberFormat.setStatus("current")


class _ZoneEnforcedZoneMemberID_Type(OctetString):
    """Custom type zoneEnforcedZoneMemberID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZoneEnforcedZoneMemberID_Type.__name__ = "OctetString"
_ZoneEnforcedZoneMemberID_Object = MibTableColumn
zoneEnforcedZoneMemberID = _ZoneEnforcedZoneMemberID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 19, 1, 2),
    _ZoneEnforcedZoneMemberID_Type()
)
zoneEnforcedZoneMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneMemberID.setStatus("current")


class _ZoneEnforcedZoneMemberLunID_Type(OctetString):
    """Custom type zoneEnforcedZoneMemberLunID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_ZoneEnforcedZoneMemberLunID_Type.__name__ = "OctetString"
_ZoneEnforcedZoneMemberLunID_Object = MibTableColumn
zoneEnforcedZoneMemberLunID = _ZoneEnforcedZoneMemberLunID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 19, 1, 3),
    _ZoneEnforcedZoneMemberLunID_Type()
)
zoneEnforcedZoneMemberLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneEnforcedZoneMemberLunID.setStatus("current")
_ZoneMergeFailRecoverSpinLock_Type = TestAndIncr
_ZoneMergeFailRecoverSpinLock_Object = MibScalar
zoneMergeFailRecoverSpinLock = _ZoneMergeFailRecoverSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 20),
    _ZoneMergeFailRecoverSpinLock_Type()
)
zoneMergeFailRecoverSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneMergeFailRecoverSpinLock.setStatus("current")
_ZoneMergeFailRecoverInterface_Type = InterfaceIndexOrZero
_ZoneMergeFailRecoverInterface_Object = MibScalar
zoneMergeFailRecoverInterface = _ZoneMergeFailRecoverInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 21),
    _ZoneMergeFailRecoverInterface_Type()
)
zoneMergeFailRecoverInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneMergeFailRecoverInterface.setStatus("current")


class _ZoneMergeFailRecoverVsan_Type(VsanIndex):
    """Custom type zoneMergeFailRecoverVsan based on VsanIndex"""
    defaultValue = 1


_ZoneMergeFailRecoverVsan_Object = MibScalar
zoneMergeFailRecoverVsan = _ZoneMergeFailRecoverVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 22),
    _ZoneMergeFailRecoverVsan_Type()
)
zoneMergeFailRecoverVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneMergeFailRecoverVsan.setStatus("current")


class _ZoneMergeFailRecoverOper_Type(Integer32):
    """Custom type zoneMergeFailRecoverOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("import", 1),
          ("noop", 3))
    )


_ZoneMergeFailRecoverOper_Type.__name__ = "Integer32"
_ZoneMergeFailRecoverOper_Object = MibScalar
zoneMergeFailRecoverOper = _ZoneMergeFailRecoverOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 23),
    _ZoneMergeFailRecoverOper_Type()
)
zoneMergeFailRecoverOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneMergeFailRecoverOper.setStatus("current")


class _ZoneMergeFailRecoverResult_Type(Integer32):
    """Custom type zoneMergeFailRecoverResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("inProgress", 3),
          ("success", 1))
    )


_ZoneMergeFailRecoverResult_Type.__name__ = "Integer32"
_ZoneMergeFailRecoverResult_Object = MibScalar
zoneMergeFailRecoverResult = _ZoneMergeFailRecoverResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 24),
    _ZoneMergeFailRecoverResult_Type()
)
zoneMergeFailRecoverResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneMergeFailRecoverResult.setStatus("current")
_ZoneCopyActiveToFullOnVsan_Type = VsanIndex
_ZoneCopyActiveToFullOnVsan_Object = MibScalar
zoneCopyActiveToFullOnVsan = _ZoneCopyActiveToFullOnVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 25),
    _ZoneCopyActiveToFullOnVsan_Type()
)
zoneCopyActiveToFullOnVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneCopyActiveToFullOnVsan.setStatus("deprecated")
_ZoneServiceReqRejNotifyEnable_Type = TruthValue
_ZoneServiceReqRejNotifyEnable_Object = MibScalar
zoneServiceReqRejNotifyEnable = _ZoneServiceReqRejNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 26),
    _ZoneServiceReqRejNotifyEnable_Type()
)
zoneServiceReqRejNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneServiceReqRejNotifyEnable.setStatus("current")
_ZoneMergeFailureNotifyEnable_Type = TruthValue
_ZoneMergeFailureNotifyEnable_Object = MibScalar
zoneMergeFailureNotifyEnable = _ZoneMergeFailureNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 27),
    _ZoneMergeFailureNotifyEnable_Type()
)
zoneMergeFailureNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneMergeFailureNotifyEnable.setStatus("current")
_ZoneMergeSuccessNotifyEnable_Type = TruthValue
_ZoneMergeSuccessNotifyEnable_Object = MibScalar
zoneMergeSuccessNotifyEnable = _ZoneMergeSuccessNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 28),
    _ZoneMergeSuccessNotifyEnable_Type()
)
zoneMergeSuccessNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneMergeSuccessNotifyEnable.setStatus("current")
_ZoneDefZoneBehvrChngNotifyEnable_Type = TruthValue
_ZoneDefZoneBehvrChngNotifyEnable_Object = MibScalar
zoneDefZoneBehvrChngNotifyEnable = _ZoneDefZoneBehvrChngNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 29),
    _ZoneDefZoneBehvrChngNotifyEnable_Type()
)
zoneDefZoneBehvrChngNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneDefZoneBehvrChngNotifyEnable.setStatus("current")
_ZoneDbTable_Object = MibTable
zoneDbTable = _ZoneDbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 30)
)
if mibBuilder.loadTexts:
    zoneDbTable.setStatus("current")
_ZoneDbEntry_Object = MibTableRow
zoneDbEntry = _ZoneDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 30, 1)
)
zoneDbEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    zoneDbEntry.setStatus("current")


class _ZoneDbClearDb_Type(Integer32):
    """Custom type zoneDbClearDb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noop", 2))
    )


_ZoneDbClearDb_Type.__name__ = "Integer32"
_ZoneDbClearDb_Object = MibTableColumn
zoneDbClearDb = _ZoneDbClearDb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 30, 1, 1),
    _ZoneDbClearDb_Type()
)
zoneDbClearDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneDbClearDb.setStatus("current")
_ZoneDbEnforcedEqualsLocal_Type = TruthValue
_ZoneDbEnforcedEqualsLocal_Object = MibTableColumn
zoneDbEnforcedEqualsLocal = _ZoneDbEnforcedEqualsLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 30, 1, 2),
    _ZoneDbEnforcedEqualsLocal_Type()
)
zoneDbEnforcedEqualsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneDbEnforcedEqualsLocal.setStatus("current")
_ZoneDbHardZoningEnabled_Type = TruthValue
_ZoneDbHardZoningEnabled_Object = MibTableColumn
zoneDbHardZoningEnabled = _ZoneDbHardZoningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 30, 1, 3),
    _ZoneDbHardZoningEnabled_Type()
)
zoneDbHardZoningEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneDbHardZoningEnabled.setStatus("current")
_ZoneCopyTable_Object = MibTable
zoneCopyTable = _ZoneCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31)
)
if mibBuilder.loadTexts:
    zoneCopyTable.setStatus("current")
_ZoneCopyEntry_Object = MibTableRow
zoneCopyEntry = _ZoneCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1)
)
zoneCopyEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    zoneCopyEntry.setStatus("current")


class _ZoneCopyProto_Type(ZoneCopyProtocol):
    """Custom type zoneCopyProto based on ZoneCopyProtocol"""


_ZoneCopyProto_Object = MibTableColumn
zoneCopyProto = _ZoneCopyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 1),
    _ZoneCopyProto_Type()
)
zoneCopyProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyProto.setStatus("current")


class _ZoneCopyDestFileType_Type(ZoneFileType):
    """Custom type zoneCopyDestFileType based on ZoneFileType"""


_ZoneCopyDestFileType_Object = MibTableColumn
zoneCopyDestFileType = _ZoneCopyDestFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 2),
    _ZoneCopyDestFileType_Type()
)
zoneCopyDestFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyDestFileType.setStatus("current")


class _ZoneCopyServerAddrType_Type(InetAddressType):
    """Custom type zoneCopyServerAddrType based on InetAddressType"""


_ZoneCopyServerAddrType_Object = MibTableColumn
zoneCopyServerAddrType = _ZoneCopyServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 3),
    _ZoneCopyServerAddrType_Type()
)
zoneCopyServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyServerAddrType.setStatus("current")
_ZoneCopyServerAddr_Type = InetAddress
_ZoneCopyServerAddr_Object = MibTableColumn
zoneCopyServerAddr = _ZoneCopyServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 4),
    _ZoneCopyServerAddr_Type()
)
zoneCopyServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyServerAddr.setStatus("current")


class _ZoneCopyDestFileName_Type(SnmpAdminString):
    """Custom type zoneCopyDestFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZoneCopyDestFileName_Type.__name__ = "SnmpAdminString"
_ZoneCopyDestFileName_Object = MibTableColumn
zoneCopyDestFileName = _ZoneCopyDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 5),
    _ZoneCopyDestFileName_Type()
)
zoneCopyDestFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyDestFileName.setStatus("current")


class _ZoneCopyUserName_Type(SnmpAdminString):
    """Custom type zoneCopyUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZoneCopyUserName_Type.__name__ = "SnmpAdminString"
_ZoneCopyUserName_Object = MibTableColumn
zoneCopyUserName = _ZoneCopyUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 6),
    _ZoneCopyUserName_Type()
)
zoneCopyUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyUserName.setStatus("current")


class _ZoneCopyUserPassword_Type(SnmpAdminString):
    """Custom type zoneCopyUserPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZoneCopyUserPassword_Type.__name__ = "SnmpAdminString"
_ZoneCopyUserPassword_Object = MibTableColumn
zoneCopyUserPassword = _ZoneCopyUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 7),
    _ZoneCopyUserPassword_Type()
)
zoneCopyUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyUserPassword.setStatus("current")


class _ZoneCopyStartCopy_Type(Integer32):
    """Custom type zoneCopyStartCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("noop", 2))
    )


_ZoneCopyStartCopy_Type.__name__ = "Integer32"
_ZoneCopyStartCopy_Object = MibTableColumn
zoneCopyStartCopy = _ZoneCopyStartCopy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 8),
    _ZoneCopyStartCopy_Type()
)
zoneCopyStartCopy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyStartCopy.setStatus("current")


class _ZoneCopyState_Type(Integer32):
    """Custom type zoneCopyState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("anotherCopyInProgress", 9),
          ("badFileName", 3),
          ("badUserNamePasswd", 5),
          ("inProgress", 4),
          ("incompleteConfig", 6),
          ("success", 1),
          ("sysErr", 8),
          ("timeout", 2),
          ("unknown", 7))
    )


_ZoneCopyState_Type.__name__ = "Integer32"
_ZoneCopyState_Object = MibTableColumn
zoneCopyState = _ZoneCopyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 9),
    _ZoneCopyState_Type()
)
zoneCopyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneCopyState.setStatus("current")
_ZoneCopyRowStatus_Type = RowStatus
_ZoneCopyRowStatus_Object = MibTableColumn
zoneCopyRowStatus = _ZoneCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 31, 1, 10),
    _ZoneCopyRowStatus_Type()
)
zoneCopyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneCopyRowStatus.setStatus("current")


class _ZoneUnsuppMemInIntOpNotifyEnable_Type(TruthValue):
    """Custom type zoneUnsuppMemInIntOpNotifyEnable based on TruthValue"""


_ZoneUnsuppMemInIntOpNotifyEnable_Object = MibScalar
zoneUnsuppMemInIntOpNotifyEnable = _ZoneUnsuppMemInIntOpNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 32),
    _ZoneUnsuppMemInIntOpNotifyEnable_Type()
)
zoneUnsuppMemInIntOpNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneUnsuppMemInIntOpNotifyEnable.setStatus("current")
_ZoneVsanId_Type = VsanIndex
_ZoneVsanId_Object = MibScalar
zoneVsanId = _ZoneVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 33),
    _ZoneVsanId_Type()
)
zoneVsanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zoneVsanId.setStatus("current")
_ZoneZoneSetDistributeVsan_Type = VsanIndex
_ZoneZoneSetDistributeVsan_Object = MibScalar
zoneZoneSetDistributeVsan = _ZoneZoneSetDistributeVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 34),
    _ZoneZoneSetDistributeVsan_Type()
)
zoneZoneSetDistributeVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneZoneSetDistributeVsan.setStatus("current")


class _ZoneZoneSetDistributeResult_Type(Integer32):
    """Custom type zoneZoneSetDistributeResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("inProgress", 3),
          ("success", 1))
    )


_ZoneZoneSetDistributeResult_Type.__name__ = "Integer32"
_ZoneZoneSetDistributeResult_Object = MibScalar
zoneZoneSetDistributeResult = _ZoneZoneSetDistributeResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 35),
    _ZoneZoneSetDistributeResult_Type()
)
zoneZoneSetDistributeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneZoneSetDistributeResult.setStatus("current")
_ZoneZoneSetDistributeFailReason_Type = FcChangeProtoFailCause
_ZoneZoneSetDistributeFailReason_Object = MibScalar
zoneZoneSetDistributeFailReason = _ZoneZoneSetDistributeFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 36),
    _ZoneZoneSetDistributeFailReason_Type()
)
zoneZoneSetDistributeFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneZoneSetDistributeFailReason.setStatus("current")
_ZoneSwitchWwn_Type = FcNameId
_ZoneSwitchWwn_Object = MibScalar
zoneSwitchWwn = _ZoneSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 37),
    _ZoneSwitchWwn_Type()
)
zoneSwitchWwn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zoneSwitchWwn.setStatus("current")
_ZoneSetZoneListTable_Object = MibTable
zoneSetZoneListTable = _ZoneSetZoneListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 38)
)
if mibBuilder.loadTexts:
    zoneSetZoneListTable.setStatus("current")
_ZoneSetZoneListEntry_Object = MibTableRow
zoneSetZoneListEntry = _ZoneSetZoneListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 38, 1)
)
if mibBuilder.loadTexts:
    zoneSetZoneListEntry.setStatus("current")


class _ZoneSetZoneListBmap4k_Type(FcList):
    """Custom type zoneSetZoneListBmap4k based on FcList"""
    defaultHexValue = ""


_ZoneSetZoneListBmap4k_Object = MibTableColumn
zoneSetZoneListBmap4k = _ZoneSetZoneListBmap4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 38, 1, 1),
    _ZoneSetZoneListBmap4k_Type()
)
zoneSetZoneListBmap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetZoneListBmap4k.setStatus("current")


class _ZoneSetZoneListBmap6k_Type(FcList):
    """Custom type zoneSetZoneListBmap6k based on FcList"""
    defaultHexValue = ""


_ZoneSetZoneListBmap6k_Object = MibTableColumn
zoneSetZoneListBmap6k = _ZoneSetZoneListBmap6k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 38, 1, 2),
    _ZoneSetZoneListBmap6k_Type()
)
zoneSetZoneListBmap6k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetZoneListBmap6k.setStatus("current")


class _ZoneSetZoneListBmap8k_Type(FcList):
    """Custom type zoneSetZoneListBmap8k based on FcList"""
    defaultHexValue = ""


_ZoneSetZoneListBmap8k_Object = MibTableColumn
zoneSetZoneListBmap8k = _ZoneSetZoneListBmap8k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 38, 1, 3),
    _ZoneSetZoneListBmap8k_Type()
)
zoneSetZoneListBmap8k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zoneSetZoneListBmap8k.setStatus("current")
_ZoneSetEnforcedZoneListTable_Object = MibTable
zoneSetEnforcedZoneListTable = _ZoneSetEnforcedZoneListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 39)
)
if mibBuilder.loadTexts:
    zoneSetEnforcedZoneListTable.setStatus("current")
_ZoneSetEnforcedZoneListEntry_Object = MibTableRow
zoneSetEnforcedZoneListEntry = _ZoneSetEnforcedZoneListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 39, 1)
)
if mibBuilder.loadTexts:
    zoneSetEnforcedZoneListEntry.setStatus("current")
_ZoneSetEnforcedZoneListBmap4k_Type = FcList
_ZoneSetEnforcedZoneListBmap4k_Object = MibTableColumn
zoneSetEnforcedZoneListBmap4k = _ZoneSetEnforcedZoneListBmap4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 39, 1, 1),
    _ZoneSetEnforcedZoneListBmap4k_Type()
)
zoneSetEnforcedZoneListBmap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneSetEnforcedZoneListBmap4k.setStatus("current")
_ZoneSetEnforcedZoneListBmap6k_Type = FcList
_ZoneSetEnforcedZoneListBmap6k_Object = MibTableColumn
zoneSetEnforcedZoneListBmap6k = _ZoneSetEnforcedZoneListBmap6k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 39, 1, 2),
    _ZoneSetEnforcedZoneListBmap6k_Type()
)
zoneSetEnforcedZoneListBmap6k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneSetEnforcedZoneListBmap6k.setStatus("current")
_ZoneSetEnforcedZoneListBmap8k_Type = FcList
_ZoneSetEnforcedZoneListBmap8k_Object = MibTableColumn
zoneSetEnforcedZoneListBmap8k = _ZoneSetEnforcedZoneListBmap8k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 39, 1, 3),
    _ZoneSetEnforcedZoneListBmap8k_Type()
)
zoneSetEnforcedZoneListBmap8k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneSetEnforcedZoneListBmap8k.setStatus("current")
_ZoneCompactTable_Object = MibTable
zoneCompactTable = _ZoneCompactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 40)
)
if mibBuilder.loadTexts:
    zoneCompactTable.setStatus("current")
_ZoneCompactEntry_Object = MibTableRow
zoneCompactEntry = _ZoneCompactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 40, 1)
)
zoneCompactEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    zoneCompactEntry.setStatus("current")


class _ZoneCompactFirst2k_Type(Integer32):
    """Custom type zoneCompactFirst2k based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compact", 1),
          ("noop", 2))
    )


_ZoneCompactFirst2k_Type.__name__ = "Integer32"
_ZoneCompactFirst2k_Object = MibTableColumn
zoneCompactFirst2k = _ZoneCompactFirst2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 40, 1, 1),
    _ZoneCompactFirst2k_Type()
)
zoneCompactFirst2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneCompactFirst2k.setStatus("current")
_ZoneCompactVsan_Type = VsanIndex
_ZoneCompactVsan_Object = MibScalar
zoneCompactVsan = _ZoneCompactVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 41),
    _ZoneCompactVsan_Type()
)
zoneCompactVsan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zoneCompactVsan.setStatus("current")
_ZoneCopyActToFullSpinLock_Type = TestAndIncr
_ZoneCopyActToFullSpinLock_Object = MibScalar
zoneCopyActToFullSpinLock = _ZoneCopyActToFullSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 42),
    _ZoneCopyActToFullSpinLock_Type()
)
zoneCopyActToFullSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneCopyActToFullSpinLock.setStatus("current")


class _ZoneCopyActToFullMode_Type(Integer32):
    """Custom type zoneCopyActToFullMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("excludeAutoZones", 2),
          ("includeAutoZones", 1),
          ("noop", 3))
    )


_ZoneCopyActToFullMode_Type.__name__ = "Integer32"
_ZoneCopyActToFullMode_Object = MibScalar
zoneCopyActToFullMode = _ZoneCopyActToFullMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 43),
    _ZoneCopyActToFullMode_Type()
)
zoneCopyActToFullMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneCopyActToFullMode.setStatus("current")
_ZoneCopyActToFullVsan_Type = VsanIndex
_ZoneCopyActToFullVsan_Object = MibScalar
zoneCopyActToFullVsan = _ZoneCopyActToFullVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 1, 44),
    _ZoneCopyActToFullVsan_Type()
)
zoneCopyActToFullVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneCopyActToFullVsan.setStatus("current")
_ZoneStats_ObjectIdentity = ObjectIdentity
zoneStats = _ZoneStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2)
)
_ZoneTotalGS3Rejects_Type = Counter32
_ZoneTotalGS3Rejects_Object = MibScalar
zoneTotalGS3Rejects = _ZoneTotalGS3Rejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 1),
    _ZoneTotalGS3Rejects_Type()
)
zoneTotalGS3Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneTotalGS3Rejects.setStatus("current")
_ZoneStatsTable_Object = MibTable
zoneStatsTable = _ZoneStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zoneStatsTable.setStatus("current")
_ZoneStatsEntry_Object = MibTableRow
zoneStatsEntry = _ZoneStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1)
)
zoneStatsEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    zoneStatsEntry.setStatus("current")
_ZoneTxMergeReqs_Type = Counter32
_ZoneTxMergeReqs_Object = MibTableColumn
zoneTxMergeReqs = _ZoneTxMergeReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 1),
    _ZoneTxMergeReqs_Type()
)
zoneTxMergeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneTxMergeReqs.setStatus("current")
_ZoneRxMergeAccepts_Type = Counter32
_ZoneRxMergeAccepts_Object = MibTableColumn
zoneRxMergeAccepts = _ZoneRxMergeAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 2),
    _ZoneRxMergeAccepts_Type()
)
zoneRxMergeAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneRxMergeAccepts.setStatus("current")
_ZoneRxMergeReqs_Type = Counter32
_ZoneRxMergeReqs_Object = MibTableColumn
zoneRxMergeReqs = _ZoneRxMergeReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 3),
    _ZoneRxMergeReqs_Type()
)
zoneRxMergeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneRxMergeReqs.setStatus("current")
_ZoneTxMergeAccepts_Type = Counter32
_ZoneTxMergeAccepts_Object = MibTableColumn
zoneTxMergeAccepts = _ZoneTxMergeAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 4),
    _ZoneTxMergeAccepts_Type()
)
zoneTxMergeAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneTxMergeAccepts.setStatus("current")
_ZoneTxChangeReqs_Type = Counter32
_ZoneTxChangeReqs_Object = MibTableColumn
zoneTxChangeReqs = _ZoneTxChangeReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 5),
    _ZoneTxChangeReqs_Type()
)
zoneTxChangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneTxChangeReqs.setStatus("current")
_ZoneRxChangeAccepts_Type = Counter32
_ZoneRxChangeAccepts_Object = MibTableColumn
zoneRxChangeAccepts = _ZoneRxChangeAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 6),
    _ZoneRxChangeAccepts_Type()
)
zoneRxChangeAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneRxChangeAccepts.setStatus("current")
_ZoneRxChangeReqs_Type = Counter32
_ZoneRxChangeReqs_Object = MibTableColumn
zoneRxChangeReqs = _ZoneRxChangeReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 7),
    _ZoneRxChangeReqs_Type()
)
zoneRxChangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneRxChangeReqs.setStatus("current")
_ZoneTxChangeAccepts_Type = Counter32
_ZoneTxChangeAccepts_Object = MibTableColumn
zoneTxChangeAccepts = _ZoneTxChangeAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 8),
    _ZoneTxChangeAccepts_Type()
)
zoneTxChangeAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneTxChangeAccepts.setStatus("current")
_ZoneRxGS3Reqs_Type = Counter32
_ZoneRxGS3Reqs_Object = MibTableColumn
zoneRxGS3Reqs = _ZoneRxGS3Reqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 9),
    _ZoneRxGS3Reqs_Type()
)
zoneRxGS3Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneRxGS3Reqs.setStatus("current")
_ZoneTxGS3Rejects_Type = Counter32
_ZoneTxGS3Rejects_Object = MibTableColumn
zoneTxGS3Rejects = _ZoneTxGS3Rejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 2, 1, 10),
    _ZoneTxGS3Rejects_Type()
)
zoneTxGS3Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneTxGS3Rejects.setStatus("current")
_ZoneLunStatsTable_Object = MibTable
zoneLunStatsTable = _ZoneLunStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zoneLunStatsTable.setStatus("current")
_ZoneLunStatsEntry_Object = MibTableRow
zoneLunStatsEntry = _ZoneLunStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1)
)
zoneLunStatsEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneLunSrcFcId"),
    (0, "CISCO-ZS-MIB", "zoneLunDstFcId"),
    (0, "CISCO-ZS-MIB", "zoneLunNum"),
)
if mibBuilder.loadTexts:
    zoneLunStatsEntry.setStatus("current")
_ZoneLunSrcFcId_Type = FcAddressId
_ZoneLunSrcFcId_Object = MibTableColumn
zoneLunSrcFcId = _ZoneLunSrcFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 1),
    _ZoneLunSrcFcId_Type()
)
zoneLunSrcFcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneLunSrcFcId.setStatus("current")
_ZoneLunDstFcId_Type = FcAddressId
_ZoneLunDstFcId_Object = MibTableColumn
zoneLunDstFcId = _ZoneLunDstFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 2),
    _ZoneLunDstFcId_Type()
)
zoneLunDstFcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneLunDstFcId.setStatus("current")


class _ZoneLunNum_Type(OctetString):
    """Custom type zoneLunNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ZoneLunNum_Type.__name__ = "OctetString"
_ZoneLunNum_Object = MibTableColumn
zoneLunNum = _ZoneLunNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 3),
    _ZoneLunNum_Type()
)
zoneLunNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneLunNum.setStatus("current")
_ZoneLunRxInqReqs_Type = Counter32
_ZoneLunRxInqReqs_Object = MibTableColumn
zoneLunRxInqReqs = _ZoneLunRxInqReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 4),
    _ZoneLunRxInqReqs_Type()
)
zoneLunRxInqReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneLunRxInqReqs.setStatus("current")
_ZoneLunRxRepLunReqs_Type = Counter32
_ZoneLunRxRepLunReqs_Object = MibTableColumn
zoneLunRxRepLunReqs = _ZoneLunRxRepLunReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 5),
    _ZoneLunRxRepLunReqs_Type()
)
zoneLunRxRepLunReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneLunRxRepLunReqs.setStatus("current")
_ZoneLunRxSenseReqs_Type = Counter32
_ZoneLunRxSenseReqs_Object = MibTableColumn
zoneLunRxSenseReqs = _ZoneLunRxSenseReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 6),
    _ZoneLunRxSenseReqs_Type()
)
zoneLunRxSenseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneLunRxSenseReqs.setStatus("current")
_ZoneLunRxOtherCmds_Type = Counter32
_ZoneLunRxOtherCmds_Object = MibTableColumn
zoneLunRxOtherCmds = _ZoneLunRxOtherCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 7),
    _ZoneLunRxOtherCmds_Type()
)
zoneLunRxOtherCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneLunRxOtherCmds.setStatus("current")
_ZoneLunTxInqDataNoLus_Type = Counter32
_ZoneLunTxInqDataNoLus_Object = MibTableColumn
zoneLunTxInqDataNoLus = _ZoneLunTxInqDataNoLus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 8),
    _ZoneLunTxInqDataNoLus_Type()
)
zoneLunTxInqDataNoLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneLunTxInqDataNoLus.setStatus("current")
_ZoneLunTxIllegalReqs_Type = Counter32
_ZoneLunTxIllegalReqs_Object = MibTableColumn
zoneLunTxIllegalReqs = _ZoneLunTxIllegalReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 3, 1, 9),
    _ZoneLunTxIllegalReqs_Type()
)
zoneLunTxIllegalReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneLunTxIllegalReqs.setStatus("current")
_ZoneRoZoneStatsTable_Object = MibTable
zoneRoZoneStatsTable = _ZoneRoZoneStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zoneRoZoneStatsTable.setStatus("current")
_ZoneRoZoneStatsEntry_Object = MibTableRow
zoneRoZoneStatsEntry = _ZoneRoZoneStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 4, 1)
)
zoneRoZoneStatsEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-ZS-MIB", "zoneRoZoneSrcFcId"),
    (0, "CISCO-ZS-MIB", "zoneRoZoneDstFcId"),
    (0, "CISCO-ZS-MIB", "zoneRoZoneLunNum"),
)
if mibBuilder.loadTexts:
    zoneRoZoneStatsEntry.setStatus("current")
_ZoneRoZoneSrcFcId_Type = FcAddressId
_ZoneRoZoneSrcFcId_Object = MibTableColumn
zoneRoZoneSrcFcId = _ZoneRoZoneSrcFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 4, 1, 1),
    _ZoneRoZoneSrcFcId_Type()
)
zoneRoZoneSrcFcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneRoZoneSrcFcId.setStatus("current")
_ZoneRoZoneDstFcId_Type = FcAddressId
_ZoneRoZoneDstFcId_Object = MibTableColumn
zoneRoZoneDstFcId = _ZoneRoZoneDstFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 4, 1, 2),
    _ZoneRoZoneDstFcId_Type()
)
zoneRoZoneDstFcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneRoZoneDstFcId.setStatus("current")


class _ZoneRoZoneLunNum_Type(OctetString):
    """Custom type zoneRoZoneLunNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ZoneRoZoneLunNum_Type.__name__ = "OctetString"
_ZoneRoZoneLunNum_Object = MibTableColumn
zoneRoZoneLunNum = _ZoneRoZoneLunNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 4, 1, 3),
    _ZoneRoZoneLunNum_Type()
)
zoneRoZoneLunNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zoneRoZoneLunNum.setStatus("current")
_ZoneRoZoneTxDataProts_Type = Counter32
_ZoneRoZoneTxDataProts_Object = MibTableColumn
zoneRoZoneTxDataProts = _ZoneRoZoneTxDataProts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 2, 4, 1, 4),
    _ZoneRoZoneTxDataProts_Type()
)
zoneRoZoneTxDataProts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneRoZoneTxDataProts.setStatus("current")
_ZoneInformation_ObjectIdentity = ObjectIdentity
zoneInformation = _ZoneInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 3)
)
_ZoneServiceRejReasonCode_Type = FcGs3RejectReasonCode
_ZoneServiceRejReasonCode_Object = MibScalar
zoneServiceRejReasonCode = _ZoneServiceRejReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 3, 1),
    _ZoneServiceRejReasonCode_Type()
)
zoneServiceRejReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneServiceRejReasonCode.setStatus("current")
_ZoneServiceRejReasonCodeExp_Type = FcZoneServerRejReasonExpl
_ZoneServiceRejReasonCodeExp_Object = MibScalar
zoneServiceRejReasonCodeExp = _ZoneServiceRejReasonCodeExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 3, 2),
    _ZoneServiceRejReasonCodeExp_Type()
)
zoneServiceRejReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneServiceRejReasonCodeExp.setStatus("current")


class _ZoneMergeFailureVSANNum_Type(Unsigned32):
    """Custom type zoneMergeFailureVSANNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZoneMergeFailureVSANNum_Type.__name__ = "Unsigned32"
_ZoneMergeFailureVSANNum_Object = MibScalar
zoneMergeFailureVSANNum = _ZoneMergeFailureVSANNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 3, 3),
    _ZoneMergeFailureVSANNum_Type()
)
zoneMergeFailureVSANNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneMergeFailureVSANNum.setStatus("current")


class _ZoneMergeSuccessVSANNum_Type(Unsigned32):
    """Custom type zoneMergeSuccessVSANNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZoneMergeSuccessVSANNum_Type.__name__ = "Unsigned32"
_ZoneMergeSuccessVSANNum_Object = MibScalar
zoneMergeSuccessVSANNum = _ZoneMergeSuccessVSANNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 3, 4),
    _ZoneMergeSuccessVSANNum_Type()
)
zoneMergeSuccessVSANNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneMergeSuccessVSANNum.setStatus("current")
_ZoneMergeFailureObject_Type = SnmpAdminString
_ZoneMergeFailureObject_Object = MibScalar
zoneMergeFailureObject = _ZoneMergeFailureObject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 3, 5),
    _ZoneMergeFailureObject_Type()
)
zoneMergeFailureObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zoneMergeFailureObject.setStatus("current")
_ZoneMergeFailureReason_Type = ZoneMergeFailCause
_ZoneMergeFailureReason_Object = MibScalar
zoneMergeFailureReason = _ZoneMergeFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 3, 6),
    _ZoneMergeFailureReason_Type()
)
zoneMergeFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zoneMergeFailureReason.setStatus("current")
_ZoneNotification_ObjectIdentity = ObjectIdentity
zoneNotification = _ZoneNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4)
)
_ZoneNotifications_ObjectIdentity = ObjectIdentity
zoneNotifications = _ZoneNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4, 0)
)
_ZoneServerMIBConformance_ObjectIdentity = ObjectIdentity
zoneServerMIBConformance = _ZoneServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2)
)
_ZoneServerMIBCompliances_ObjectIdentity = ObjectIdentity
zoneServerMIBCompliances = _ZoneServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1)
)
_ZoneServerMIBGroups_ObjectIdentity = ObjectIdentity
zoneServerMIBGroups = _ZoneServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2)
)
zoneSetEntry.registerAugmentions(
    ("CISCO-ZS-MIB",
     "zoneSetZoneListEntry")
)
zoneSetZoneListEntry.setIndexNames(*zoneSetEntry.getIndexNames())
zoneEnforcedZoneSetEntry.registerAugmentions(
    ("CISCO-ZS-MIB",
     "zoneSetEnforcedZoneListEntry")
)
zoneSetEnforcedZoneListEntry.setIndexNames(*zoneEnforcedZoneSetEntry.getIndexNames())

# Managed Objects groups

zoneConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 1)
)
zoneConfigurationGroup.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetPropagationMode"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour"),
        ("CISCO-ZS-MIB", "zoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneSetName"),
        ("CISCO-ZS-MIB", "zoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneSetLastChange"),
        ("CISCO-ZS-MIB", "zoneSetRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSetDeActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateRowStatus"),
        ("CISCO-ZS-MIB", "zoneNumber"),
        ("CISCO-ZS-MIB", "zoneName"),
        ("CISCO-ZS-MIB", "zoneMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasList"),
        ("CISCO-ZS-MIB", "zoneLastChange"),
        ("CISCO-ZS-MIB", "zoneRowStatus"),
        ("CISCO-ZS-MIB", "zoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneAliasName"),
        ("CISCO-ZS-MIB", "zoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasRowStatus"),
        ("CISCO-ZS-MIB", "zoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMemberRowStatus"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberID"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverSpinLock"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverInterface"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverOper"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverResult"),
        ("CISCO-ZS-MIB", "zoneCopyActiveToFullOnVsan"))
)
if mibBuilder.loadTexts:
    zoneConfigurationGroup.setStatus("deprecated")

zoneStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 2)
)
zoneStatisticsGroup.setObjects(
      *(("CISCO-ZS-MIB", "zoneTotalGS3Rejects"),
        ("CISCO-ZS-MIB", "zoneTxMergeReqs"),
        ("CISCO-ZS-MIB", "zoneRxMergeAccepts"),
        ("CISCO-ZS-MIB", "zoneRxMergeReqs"),
        ("CISCO-ZS-MIB", "zoneTxMergeAccepts"),
        ("CISCO-ZS-MIB", "zoneTxChangeReqs"),
        ("CISCO-ZS-MIB", "zoneRxChangeAccepts"),
        ("CISCO-ZS-MIB", "zoneRxChangeReqs"),
        ("CISCO-ZS-MIB", "zoneTxChangeAccepts"),
        ("CISCO-ZS-MIB", "zoneRxGS3Reqs"),
        ("CISCO-ZS-MIB", "zoneTxGS3Rejects"))
)
if mibBuilder.loadTexts:
    zoneStatisticsGroup.setStatus("current")

zoneNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 3)
)
zoneNotificationControlGroup.setObjects(
      *(("CISCO-ZS-MIB", "zoneServiceReqRejNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneMergeFailureNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneMergeSuccessNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneDefZoneBehvrChngNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneServiceRejReasonCode"),
        ("CISCO-ZS-MIB", "zoneServiceRejReasonCodeExp"),
        ("CISCO-ZS-MIB", "zoneMergeFailureVSANNum"),
        ("CISCO-ZS-MIB", "zoneMergeSuccessVSANNum"))
)
if mibBuilder.loadTexts:
    zoneNotificationControlGroup.setStatus("deprecated")

zoneConfigurationGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 5)
)
zoneConfigurationGroup1.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetPropagationMode"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour"),
        ("CISCO-ZS-MIB", "zoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneSetName"),
        ("CISCO-ZS-MIB", "zoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneSetLastChange"),
        ("CISCO-ZS-MIB", "zoneSetRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSetDeActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetFailCause"),
        ("CISCO-ZS-MIB", "zoneSetFailDomId"),
        ("CISCO-ZS-MIB", "zoneNumber"),
        ("CISCO-ZS-MIB", "zoneName"),
        ("CISCO-ZS-MIB", "zoneMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasList"),
        ("CISCO-ZS-MIB", "zoneLastChange"),
        ("CISCO-ZS-MIB", "zoneRowStatus"),
        ("CISCO-ZS-MIB", "zoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneAliasName"),
        ("CISCO-ZS-MIB", "zoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasRowStatus"),
        ("CISCO-ZS-MIB", "zoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMemberRowStatus"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberID"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverSpinLock"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverInterface"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverOper"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverResult"),
        ("CISCO-ZS-MIB", "zoneCopyActiveToFullOnVsan"),
        ("CISCO-ZS-MIB", "zoneDbClearDb"),
        ("CISCO-ZS-MIB", "zoneDbEnforcedEqualsLocal"))
)
if mibBuilder.loadTexts:
    zoneConfigurationGroup1.setStatus("deprecated")

zoneConfigurationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 6)
)
zoneConfigurationGroup2.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetPropagationMode"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneSetName"),
        ("CISCO-ZS-MIB", "zoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneSetLastChange"),
        ("CISCO-ZS-MIB", "zoneSetRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSetDeActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetFailCause"),
        ("CISCO-ZS-MIB", "zoneSetFailDomId"),
        ("CISCO-ZS-MIB", "zoneNumber"),
        ("CISCO-ZS-MIB", "zoneName"),
        ("CISCO-ZS-MIB", "zoneMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasList"),
        ("CISCO-ZS-MIB", "zoneLastChange"),
        ("CISCO-ZS-MIB", "zoneRowStatus"),
        ("CISCO-ZS-MIB", "zoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneAliasName"),
        ("CISCO-ZS-MIB", "zoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasRowStatus"),
        ("CISCO-ZS-MIB", "zoneAliasLastChange"),
        ("CISCO-ZS-MIB", "zoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMemberRowStatus"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberID"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverSpinLock"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverInterface"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverOper"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverResult"),
        ("CISCO-ZS-MIB", "zoneCopyActiveToFullOnVsan"),
        ("CISCO-ZS-MIB", "zoneDbClearDb"),
        ("CISCO-ZS-MIB", "zoneDbEnforcedEqualsLocal"))
)
if mibBuilder.loadTexts:
    zoneConfigurationGroup2.setStatus("deprecated")

zoneLunStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 7)
)
zoneLunStatsGroup.setObjects(
      *(("CISCO-ZS-MIB", "zoneLunRxInqReqs"),
        ("CISCO-ZS-MIB", "zoneLunRxRepLunReqs"),
        ("CISCO-ZS-MIB", "zoneLunRxSenseReqs"),
        ("CISCO-ZS-MIB", "zoneLunRxOtherCmds"),
        ("CISCO-ZS-MIB", "zoneLunTxInqDataNoLus"),
        ("CISCO-ZS-MIB", "zoneLunTxIllegalReqs"),
        ("CISCO-ZS-MIB", "zoneRoZoneTxDataProts"))
)
if mibBuilder.loadTexts:
    zoneLunStatsGroup.setStatus("current")

zoneConfigurationGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 8)
)
zoneConfigurationGroup3.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetPropagationMode"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneSetName"),
        ("CISCO-ZS-MIB", "zoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneSetLastChange"),
        ("CISCO-ZS-MIB", "zoneSetRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSetDeActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetFailCause"),
        ("CISCO-ZS-MIB", "zoneSetFailDomId"),
        ("CISCO-ZS-MIB", "zoneNumber"),
        ("CISCO-ZS-MIB", "zoneName"),
        ("CISCO-ZS-MIB", "zoneMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasList"),
        ("CISCO-ZS-MIB", "zoneLastChange"),
        ("CISCO-ZS-MIB", "zoneRowStatus"),
        ("CISCO-ZS-MIB", "zoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneAliasName"),
        ("CISCO-ZS-MIB", "zoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasRowStatus"),
        ("CISCO-ZS-MIB", "zoneAliasLastChange"),
        ("CISCO-ZS-MIB", "zoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMemberRowStatus"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberID"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverSpinLock"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverInterface"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverOper"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverResult"),
        ("CISCO-ZS-MIB", "zoneCopyActiveToFullOnVsan"),
        ("CISCO-ZS-MIB", "zoneDbClearDb"),
        ("CISCO-ZS-MIB", "zoneDbEnforcedEqualsLocal"),
        ("CISCO-ZS-MIB", "zoneCopyProto"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddrType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddr"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileName"),
        ("CISCO-ZS-MIB", "zoneCopyUserName"),
        ("CISCO-ZS-MIB", "zoneCopyUserPassword"),
        ("CISCO-ZS-MIB", "zoneCopyStartCopy"),
        ("CISCO-ZS-MIB", "zoneCopyState"),
        ("CISCO-ZS-MIB", "zoneCopyRowStatus"))
)
if mibBuilder.loadTexts:
    zoneConfigurationGroup3.setStatus("deprecated")

zoneNotificationControlGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 9)
)
zoneNotificationControlGroup1.setObjects(
      *(("CISCO-ZS-MIB", "zoneServiceReqRejNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneMergeFailureNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneMergeSuccessNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneDefZoneBehvrChngNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneUnsuppMemInIntOpNotifyEnable"),
        ("CISCO-ZS-MIB", "zoneServiceRejReasonCode"),
        ("CISCO-ZS-MIB", "zoneServiceRejReasonCodeExp"),
        ("CISCO-ZS-MIB", "zoneMergeFailureVSANNum"),
        ("CISCO-ZS-MIB", "zoneMergeSuccessVSANNum"),
        ("CISCO-ZS-MIB", "zoneVsanId"))
)
if mibBuilder.loadTexts:
    zoneNotificationControlGroup1.setStatus("current")

zoneConfigurationGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 11)
)
zoneConfigurationGroup4.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetPropagationMode"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneSetName"),
        ("CISCO-ZS-MIB", "zoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneSetLastChange"),
        ("CISCO-ZS-MIB", "zoneSetRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSetDeActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetFailCause"),
        ("CISCO-ZS-MIB", "zoneSetFailDomId"),
        ("CISCO-ZS-MIB", "zoneNumber"),
        ("CISCO-ZS-MIB", "zoneName"),
        ("CISCO-ZS-MIB", "zoneMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasList"),
        ("CISCO-ZS-MIB", "zoneLastChange"),
        ("CISCO-ZS-MIB", "zoneRowStatus"),
        ("CISCO-ZS-MIB", "zoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneAliasName"),
        ("CISCO-ZS-MIB", "zoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasRowStatus"),
        ("CISCO-ZS-MIB", "zoneAliasLastChange"),
        ("CISCO-ZS-MIB", "zoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMemberRowStatus"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberID"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverSpinLock"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverInterface"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverOper"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverResult"),
        ("CISCO-ZS-MIB", "zoneCopyActiveToFullOnVsan"),
        ("CISCO-ZS-MIB", "zoneDbClearDb"),
        ("CISCO-ZS-MIB", "zoneDbEnforcedEqualsLocal"),
        ("CISCO-ZS-MIB", "zoneCopyProto"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddrType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddr"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileName"),
        ("CISCO-ZS-MIB", "zoneCopyUserName"),
        ("CISCO-ZS-MIB", "zoneCopyUserPassword"),
        ("CISCO-ZS-MIB", "zoneCopyStartCopy"),
        ("CISCO-ZS-MIB", "zoneCopyState"),
        ("CISCO-ZS-MIB", "zoneCopyRowStatus"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeVsan"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeResult"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeFailReason"))
)
if mibBuilder.loadTexts:
    zoneConfigurationGroup4.setStatus("deprecated")

zoneConfigurationGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 12)
)
zoneConfigurationGroup5.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetPropagationMode"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneQos"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneSetName"),
        ("CISCO-ZS-MIB", "zoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneSetLastChange"),
        ("CISCO-ZS-MIB", "zoneSetRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSetDeActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetFailCause"),
        ("CISCO-ZS-MIB", "zoneSetFailDomId"),
        ("CISCO-ZS-MIB", "zoneNumber"),
        ("CISCO-ZS-MIB", "zoneName"),
        ("CISCO-ZS-MIB", "zoneMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasList"),
        ("CISCO-ZS-MIB", "zoneLastChange"),
        ("CISCO-ZS-MIB", "zoneRowStatus"),
        ("CISCO-ZS-MIB", "zoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneQos"),
        ("CISCO-ZS-MIB", "zoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneAliasName"),
        ("CISCO-ZS-MIB", "zoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasRowStatus"),
        ("CISCO-ZS-MIB", "zoneAliasLastChange"),
        ("CISCO-ZS-MIB", "zoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMemberRowStatus"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneQos"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberID"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverSpinLock"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverInterface"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverOper"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverResult"),
        ("CISCO-ZS-MIB", "zoneCopyActiveToFullOnVsan"),
        ("CISCO-ZS-MIB", "zoneDbClearDb"),
        ("CISCO-ZS-MIB", "zoneDbEnforcedEqualsLocal"),
        ("CISCO-ZS-MIB", "zoneCopyProto"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddrType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddr"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileName"),
        ("CISCO-ZS-MIB", "zoneCopyUserName"),
        ("CISCO-ZS-MIB", "zoneCopyUserPassword"),
        ("CISCO-ZS-MIB", "zoneCopyStartCopy"),
        ("CISCO-ZS-MIB", "zoneCopyState"),
        ("CISCO-ZS-MIB", "zoneCopyRowStatus"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeVsan"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeResult"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeFailReason"))
)
if mibBuilder.loadTexts:
    zoneConfigurationGroup5.setStatus("deprecated")

zoneConfigurationGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 13)
)
zoneConfigurationGroup6.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetPropagationMode"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneQos"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneSetName"),
        ("CISCO-ZS-MIB", "zoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneSetLastChange"),
        ("CISCO-ZS-MIB", "zoneSetRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetClone"),
        ("CISCO-ZS-MIB", "zoneSetActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSetDeActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetFailCause"),
        ("CISCO-ZS-MIB", "zoneSetFailDomId"),
        ("CISCO-ZS-MIB", "zoneNumber"),
        ("CISCO-ZS-MIB", "zoneName"),
        ("CISCO-ZS-MIB", "zoneMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasList"),
        ("CISCO-ZS-MIB", "zoneLastChange"),
        ("CISCO-ZS-MIB", "zoneRowStatus"),
        ("CISCO-ZS-MIB", "zoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneQos"),
        ("CISCO-ZS-MIB", "zoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneClone"),
        ("CISCO-ZS-MIB", "zoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneAliasName"),
        ("CISCO-ZS-MIB", "zoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasRowStatus"),
        ("CISCO-ZS-MIB", "zoneAliasLastChange"),
        ("CISCO-ZS-MIB", "zoneAliasClone"),
        ("CISCO-ZS-MIB", "zoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMemberRowStatus"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneQos"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberID"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverSpinLock"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverInterface"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverOper"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverResult"),
        ("CISCO-ZS-MIB", "zoneCopyActiveToFullOnVsan"),
        ("CISCO-ZS-MIB", "zoneDbClearDb"),
        ("CISCO-ZS-MIB", "zoneDbEnforcedEqualsLocal"),
        ("CISCO-ZS-MIB", "zoneDbHardZoningEnabled"),
        ("CISCO-ZS-MIB", "zoneCopyProto"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddrType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddr"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileName"),
        ("CISCO-ZS-MIB", "zoneCopyUserName"),
        ("CISCO-ZS-MIB", "zoneCopyUserPassword"),
        ("CISCO-ZS-MIB", "zoneCopyStartCopy"),
        ("CISCO-ZS-MIB", "zoneCopyState"),
        ("CISCO-ZS-MIB", "zoneCopyRowStatus"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeVsan"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeResult"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeFailReason"))
)
if mibBuilder.loadTexts:
    zoneConfigurationGroup6.setStatus("deprecated")

zoneNotificationControlGroup1Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 15)
)
zoneNotificationControlGroup1Sup1.setObjects(
    ("CISCO-ZS-MIB", "zoneSwitchWwn")
)
if mibBuilder.loadTexts:
    zoneNotificationControlGroup1Sup1.setStatus("current")

zoneConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 16)
)
zoneConfigGroupSup1.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetZoneListBmap4k"),
        ("CISCO-ZS-MIB", "zoneSetZoneListBmap6k"),
        ("CISCO-ZS-MIB", "zoneSetZoneListBmap8k"),
        ("CISCO-ZS-MIB", "zoneSetEnforcedZoneListBmap4k"),
        ("CISCO-ZS-MIB", "zoneSetEnforcedZoneListBmap6k"),
        ("CISCO-ZS-MIB", "zoneSetEnforcedZoneListBmap8k"),
        ("CISCO-ZS-MIB", "zoneCompactFirst2k"))
)
if mibBuilder.loadTexts:
    zoneConfigGroupSup1.setStatus("current")

zoneNotificationControlGroup1Sup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 17)
)
zoneNotificationControlGroup1Sup2.setObjects(
      *(("CISCO-ZS-MIB", "zoneCompactVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailureObject"),
        ("CISCO-ZS-MIB", "zoneMergeFailureReason"))
)
if mibBuilder.loadTexts:
    zoneNotificationControlGroup1Sup2.setStatus("current")

zoneConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 19)
)
zoneConfigGroupSup2.setObjects(
      *(("CISCO-ZS-MIB", "zoneCopyActToFullSpinLock"),
        ("CISCO-ZS-MIB", "zoneCopyActToFullMode"),
        ("CISCO-ZS-MIB", "zoneCopyActToFullVsan"))
)
if mibBuilder.loadTexts:
    zoneConfigGroupSup2.setStatus("current")

zoneConfigurationGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 20)
)
zoneConfigurationGroup7.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetPropagationMode"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneQos"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneDefaultZoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneSetName"),
        ("CISCO-ZS-MIB", "zoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneSetLastChange"),
        ("CISCO-ZS-MIB", "zoneSetRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetClone"),
        ("CISCO-ZS-MIB", "zoneSetActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSetDeActivate"),
        ("CISCO-ZS-MIB", "zoneSetActivateRowStatus"),
        ("CISCO-ZS-MIB", "zoneSetFailCause"),
        ("CISCO-ZS-MIB", "zoneSetFailDomId"),
        ("CISCO-ZS-MIB", "zoneNumber"),
        ("CISCO-ZS-MIB", "zoneName"),
        ("CISCO-ZS-MIB", "zoneMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasList"),
        ("CISCO-ZS-MIB", "zoneLastChange"),
        ("CISCO-ZS-MIB", "zoneRowStatus"),
        ("CISCO-ZS-MIB", "zoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneQos"),
        ("CISCO-ZS-MIB", "zoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneClone"),
        ("CISCO-ZS-MIB", "zoneAliasNumber"),
        ("CISCO-ZS-MIB", "zoneAliasName"),
        ("CISCO-ZS-MIB", "zoneAliasMemberList"),
        ("CISCO-ZS-MIB", "zoneAliasRowStatus"),
        ("CISCO-ZS-MIB", "zoneAliasLastChange"),
        ("CISCO-ZS-MIB", "zoneAliasClone"),
        ("CISCO-ZS-MIB", "zoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMemberRowStatus"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetZoneList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneSetActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneName"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneAliasList"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneActivateTime"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneReadOnly"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneQos"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneQosPriority"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneBroadcast"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberNumber"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberID"),
        ("CISCO-ZS-MIB", "zoneEnforcedZoneMemberLunID"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverSpinLock"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverInterface"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverVsan"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverOper"),
        ("CISCO-ZS-MIB", "zoneMergeFailRecoverResult"),
        ("CISCO-ZS-MIB", "zoneDbClearDb"),
        ("CISCO-ZS-MIB", "zoneDbEnforcedEqualsLocal"),
        ("CISCO-ZS-MIB", "zoneDbHardZoningEnabled"),
        ("CISCO-ZS-MIB", "zoneCopyProto"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddrType"),
        ("CISCO-ZS-MIB", "zoneCopyServerAddr"),
        ("CISCO-ZS-MIB", "zoneCopyDestFileName"),
        ("CISCO-ZS-MIB", "zoneCopyUserName"),
        ("CISCO-ZS-MIB", "zoneCopyUserPassword"),
        ("CISCO-ZS-MIB", "zoneCopyStartCopy"),
        ("CISCO-ZS-MIB", "zoneCopyState"),
        ("CISCO-ZS-MIB", "zoneCopyRowStatus"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeVsan"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeResult"),
        ("CISCO-ZS-MIB", "zoneZoneSetDistributeFailReason"))
)
if mibBuilder.loadTexts:
    zoneConfigurationGroup7.setStatus("current")


# Notification objects

zoneServiceReqRejNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4, 0, 1)
)
zoneServiceReqRejNotify.setObjects(
      *(("CISCO-ZS-MIB", "zoneMemberFormat"),
        ("CISCO-ZS-MIB", "zoneMemberID"),
        ("CISCO-ZS-MIB", "zoneServiceRejReasonCode"),
        ("CISCO-ZS-MIB", "zoneServiceRejReasonCodeExp"))
)
if mibBuilder.loadTexts:
    zoneServiceReqRejNotify.setStatus(
        "current"
    )

zoneMergeFailureNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4, 0, 2)
)
zoneMergeFailureNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ZS-MIB", "zoneMergeFailureVSANNum"),
        ("CISCO-ZS-MIB", "zoneMergeFailureObject"),
        ("CISCO-ZS-MIB", "zoneMergeFailureReason"))
)
if mibBuilder.loadTexts:
    zoneMergeFailureNotify.setStatus(
        "current"
    )

zoneMergeSuccessNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4, 0, 3)
)
zoneMergeSuccessNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ZS-MIB", "zoneMergeSuccessVSANNum"))
)
if mibBuilder.loadTexts:
    zoneMergeSuccessNotify.setStatus(
        "current"
    )

zoneDefZoneBehaviourChngNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4, 0, 4)
)
zoneDefZoneBehaviourChngNotify.setObjects(
    ("CISCO-ZS-MIB", "zoneDefaultZoneBehaviour")
)
if mibBuilder.loadTexts:
    zoneDefZoneBehaviourChngNotify.setStatus(
        "current"
    )

zoneUnsuppMemInIntOpModeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4, 0, 5)
)
zoneUnsuppMemInIntOpModeNotify.setObjects(
    ("CISCO-ZS-MIB", "zoneVsanId")
)
if mibBuilder.loadTexts:
    zoneUnsuppMemInIntOpModeNotify.setStatus(
        "current"
    )

zoneActivateNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4, 0, 6)
)
zoneActivateNotify.setObjects(
      *(("CISCO-ZS-MIB", "zoneSetActivateResult"),
        ("CISCO-ZS-MIB", "zoneSwitchWwn"))
)
if mibBuilder.loadTexts:
    zoneActivateNotify.setStatus(
        "current"
    )

zoneCompactNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 1, 4, 0, 7)
)
zoneCompactNotify.setObjects(
    ("CISCO-ZS-MIB", "zoneCompactVsan")
)
if mibBuilder.loadTexts:
    zoneCompactNotify.setStatus(
        "current"
    )


# Notifications groups

zoneNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 4)
)
zoneNotificationGroup.setObjects(
      *(("CISCO-ZS-MIB", "zoneServiceReqRejNotify"),
        ("CISCO-ZS-MIB", "zoneMergeFailureNotify"),
        ("CISCO-ZS-MIB", "zoneMergeSuccessNotify"),
        ("CISCO-ZS-MIB", "zoneDefZoneBehaviourChngNotify"))
)
if mibBuilder.loadTexts:
    zoneNotificationGroup.setStatus(
        "deprecated"
    )

zoneNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 10)
)
zoneNotificationGroup1.setObjects(
      *(("CISCO-ZS-MIB", "zoneServiceReqRejNotify"),
        ("CISCO-ZS-MIB", "zoneMergeFailureNotify"),
        ("CISCO-ZS-MIB", "zoneMergeSuccessNotify"),
        ("CISCO-ZS-MIB", "zoneDefZoneBehaviourChngNotify"),
        ("CISCO-ZS-MIB", "zoneUnsuppMemInIntOpModeNotify"))
)
if mibBuilder.loadTexts:
    zoneNotificationGroup1.setStatus(
        "deprecated"
    )

zoneNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 14)
)
zoneNotificationGroup2.setObjects(
      *(("CISCO-ZS-MIB", "zoneServiceReqRejNotify"),
        ("CISCO-ZS-MIB", "zoneMergeFailureNotify"),
        ("CISCO-ZS-MIB", "zoneMergeSuccessNotify"),
        ("CISCO-ZS-MIB", "zoneDefZoneBehaviourChngNotify"),
        ("CISCO-ZS-MIB", "zoneUnsuppMemInIntOpModeNotify"),
        ("CISCO-ZS-MIB", "zoneActivateNotify"))
)
if mibBuilder.loadTexts:
    zoneNotificationGroup2.setStatus(
        "current"
    )

zoneNotificationGroup2Sup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 2, 18)
)
zoneNotificationGroup2Sup1.setObjects(
    ("CISCO-ZS-MIB", "zoneCompactNotify")
)
if mibBuilder.loadTexts:
    zoneNotificationGroup2Sup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

zoneServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 1)
)
if mibBuilder.loadTexts:
    zoneServerMIBCompliance.setStatus(
        "deprecated"
    )

zoneServerMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 2)
)
if mibBuilder.loadTexts:
    zoneServerMIBCompliance1.setStatus(
        "deprecated"
    )

zoneServerMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 3)
)
if mibBuilder.loadTexts:
    zoneServerMIBComplianceRev2.setStatus(
        "deprecated"
    )

zoneServerMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 4)
)
if mibBuilder.loadTexts:
    zoneServerMIBComplianceRev3.setStatus(
        "deprecated"
    )

zoneServerMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 5)
)
if mibBuilder.loadTexts:
    zoneServerMIBComplianceRev4.setStatus(
        "deprecated"
    )

zoneServerMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 6)
)
if mibBuilder.loadTexts:
    zoneServerMIBComplianceRev5.setStatus(
        "deprecated"
    )

zoneServerMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 7)
)
if mibBuilder.loadTexts:
    zoneServerMIBComplianceRev6.setStatus(
        "deprecated"
    )

zoneServerMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 8)
)
if mibBuilder.loadTexts:
    zoneServerMIBComplianceRev7.setStatus(
        "deprecated"
    )

zoneServerMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 294, 2, 1, 9)
)
if mibBuilder.loadTexts:
    zoneServerMIBComplianceRev8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ZS-MIB",
    **{"ZoneMemberType": ZoneMemberType,
       "FcZoneServerRejReasonExpl": FcZoneServerRejReasonExpl,
       "FcList": FcList,
       "FcChangeProtoFailCause": FcChangeProtoFailCause,
       "ZoneCopyProtocol": ZoneCopyProtocol,
       "ZoneFileType": ZoneFileType,
       "ZoneQosPriorityLevel": ZoneQosPriorityLevel,
       "ZoneMergeFailCause": ZoneMergeFailCause,
       "ciscoZsMIB": ciscoZsMIB,
       "ciscoZoningMIBObjects": ciscoZoningMIBObjects,
       "zoneConfiguration": zoneConfiguration,
       "zoneDefaultZoneTable": zoneDefaultZoneTable,
       "zoneDefaultZoneEntry": zoneDefaultZoneEntry,
       "zoneDefaultZoneBehaviour": zoneDefaultZoneBehaviour,
       "zoneDefaultZoneReadOnly": zoneDefaultZoneReadOnly,
       "zoneDefaultZoneQos": zoneDefaultZoneQos,
       "zoneDefaultZoneQosPriority": zoneDefaultZoneQosPriority,
       "zoneDefaultZoneBroadcast": zoneDefaultZoneBroadcast,
       "zoneSetPropagationTable": zoneSetPropagationTable,
       "zoneSetPropagationEntry": zoneSetPropagationEntry,
       "zoneSetPropagationMode": zoneSetPropagationMode,
       "zoneSetNumber": zoneSetNumber,
       "zoneSetTable": zoneSetTable,
       "zoneSetEntry": zoneSetEntry,
       "zoneSetIndex": zoneSetIndex,
       "zoneSetName": zoneSetName,
       "zoneSetZoneList": zoneSetZoneList,
       "zoneSetLastChange": zoneSetLastChange,
       "zoneSetRowStatus": zoneSetRowStatus,
       "zoneSetClone": zoneSetClone,
       "zoneSetActivateTable": zoneSetActivateTable,
       "zoneSetActivateEntry": zoneSetActivateEntry,
       "zoneSetActivate": zoneSetActivate,
       "zoneSetActivateResult": zoneSetActivateResult,
       "zoneSetDeActivate": zoneSetDeActivate,
       "zoneSetActivateRowStatus": zoneSetActivateRowStatus,
       "zoneSetFailCause": zoneSetFailCause,
       "zoneSetFailDomId": zoneSetFailDomId,
       "zoneNumber": zoneNumber,
       "zoneTable": zoneTable,
       "zoneEntry": zoneEntry,
       "zoneIndex": zoneIndex,
       "zoneName": zoneName,
       "zoneMemberList": zoneMemberList,
       "zoneAliasList": zoneAliasList,
       "zoneLastChange": zoneLastChange,
       "zoneRowStatus": zoneRowStatus,
       "zoneReadOnly": zoneReadOnly,
       "zoneQos": zoneQos,
       "zoneQosPriority": zoneQosPriority,
       "zoneBroadcast": zoneBroadcast,
       "zoneClone": zoneClone,
       "zoneAliasNumber": zoneAliasNumber,
       "zoneAliasTable": zoneAliasTable,
       "zoneAliasEntry": zoneAliasEntry,
       "zoneAliasIndex": zoneAliasIndex,
       "zoneAliasName": zoneAliasName,
       "zoneAliasMemberList": zoneAliasMemberList,
       "zoneAliasRowStatus": zoneAliasRowStatus,
       "zoneAliasLastChange": zoneAliasLastChange,
       "zoneAliasClone": zoneAliasClone,
       "zoneMemberNumber": zoneMemberNumber,
       "zoneMemberTable": zoneMemberTable,
       "zoneMemberEntry": zoneMemberEntry,
       "zoneMemberTypeIndex": zoneMemberTypeIndex,
       "zoneMemberParentIndex": zoneMemberParentIndex,
       "zoneMemberIndex": zoneMemberIndex,
       "zoneMemberFormat": zoneMemberFormat,
       "zoneMemberID": zoneMemberID,
       "zoneMemberLunID": zoneMemberLunID,
       "zoneMemberRowStatus": zoneMemberRowStatus,
       "zoneEnforcedZoneSetNumber": zoneEnforcedZoneSetNumber,
       "zoneEnforcedZoneSetTable": zoneEnforcedZoneSetTable,
       "zoneEnforcedZoneSetEntry": zoneEnforcedZoneSetEntry,
       "zoneEnforcedZoneSetName": zoneEnforcedZoneSetName,
       "zoneEnforcedZoneSetZoneList": zoneEnforcedZoneSetZoneList,
       "zoneEnforcedZoneSetActivateTime": zoneEnforcedZoneSetActivateTime,
       "zoneEnforcedZoneNumber": zoneEnforcedZoneNumber,
       "zoneEnforcedZoneTable": zoneEnforcedZoneTable,
       "zoneEnforcedZoneEntry": zoneEnforcedZoneEntry,
       "zoneEnforcedZoneName": zoneEnforcedZoneName,
       "zoneEnforcedZoneMemberList": zoneEnforcedZoneMemberList,
       "zoneEnforcedZoneAliasList": zoneEnforcedZoneAliasList,
       "zoneEnforcedZoneActivateTime": zoneEnforcedZoneActivateTime,
       "zoneEnforcedZoneReadOnly": zoneEnforcedZoneReadOnly,
       "zoneEnforcedZoneQos": zoneEnforcedZoneQos,
       "zoneEnforcedZoneQosPriority": zoneEnforcedZoneQosPriority,
       "zoneEnforcedZoneBroadcast": zoneEnforcedZoneBroadcast,
       "zoneEnforcedZoneAliasNumber": zoneEnforcedZoneAliasNumber,
       "zoneEnforcedZoneAliasTable": zoneEnforcedZoneAliasTable,
       "zoneEnforcedZoneAliasEntry": zoneEnforcedZoneAliasEntry,
       "zoneEnforcedZoneAliasName": zoneEnforcedZoneAliasName,
       "zoneEnforcedZoneAliasMemberList": zoneEnforcedZoneAliasMemberList,
       "zoneEnforcedZoneMemberNumber": zoneEnforcedZoneMemberNumber,
       "zoneEnforcedZoneMemberTable": zoneEnforcedZoneMemberTable,
       "zoneEnforcedZoneMemberEntry": zoneEnforcedZoneMemberEntry,
       "zoneEnforcedZoneMemberFormat": zoneEnforcedZoneMemberFormat,
       "zoneEnforcedZoneMemberID": zoneEnforcedZoneMemberID,
       "zoneEnforcedZoneMemberLunID": zoneEnforcedZoneMemberLunID,
       "zoneMergeFailRecoverSpinLock": zoneMergeFailRecoverSpinLock,
       "zoneMergeFailRecoverInterface": zoneMergeFailRecoverInterface,
       "zoneMergeFailRecoverVsan": zoneMergeFailRecoverVsan,
       "zoneMergeFailRecoverOper": zoneMergeFailRecoverOper,
       "zoneMergeFailRecoverResult": zoneMergeFailRecoverResult,
       "zoneCopyActiveToFullOnVsan": zoneCopyActiveToFullOnVsan,
       "zoneServiceReqRejNotifyEnable": zoneServiceReqRejNotifyEnable,
       "zoneMergeFailureNotifyEnable": zoneMergeFailureNotifyEnable,
       "zoneMergeSuccessNotifyEnable": zoneMergeSuccessNotifyEnable,
       "zoneDefZoneBehvrChngNotifyEnable": zoneDefZoneBehvrChngNotifyEnable,
       "zoneDbTable": zoneDbTable,
       "zoneDbEntry": zoneDbEntry,
       "zoneDbClearDb": zoneDbClearDb,
       "zoneDbEnforcedEqualsLocal": zoneDbEnforcedEqualsLocal,
       "zoneDbHardZoningEnabled": zoneDbHardZoningEnabled,
       "zoneCopyTable": zoneCopyTable,
       "zoneCopyEntry": zoneCopyEntry,
       "zoneCopyProto": zoneCopyProto,
       "zoneCopyDestFileType": zoneCopyDestFileType,
       "zoneCopyServerAddrType": zoneCopyServerAddrType,
       "zoneCopyServerAddr": zoneCopyServerAddr,
       "zoneCopyDestFileName": zoneCopyDestFileName,
       "zoneCopyUserName": zoneCopyUserName,
       "zoneCopyUserPassword": zoneCopyUserPassword,
       "zoneCopyStartCopy": zoneCopyStartCopy,
       "zoneCopyState": zoneCopyState,
       "zoneCopyRowStatus": zoneCopyRowStatus,
       "zoneUnsuppMemInIntOpNotifyEnable": zoneUnsuppMemInIntOpNotifyEnable,
       "zoneVsanId": zoneVsanId,
       "zoneZoneSetDistributeVsan": zoneZoneSetDistributeVsan,
       "zoneZoneSetDistributeResult": zoneZoneSetDistributeResult,
       "zoneZoneSetDistributeFailReason": zoneZoneSetDistributeFailReason,
       "zoneSwitchWwn": zoneSwitchWwn,
       "zoneSetZoneListTable": zoneSetZoneListTable,
       "zoneSetZoneListEntry": zoneSetZoneListEntry,
       "zoneSetZoneListBmap4k": zoneSetZoneListBmap4k,
       "zoneSetZoneListBmap6k": zoneSetZoneListBmap6k,
       "zoneSetZoneListBmap8k": zoneSetZoneListBmap8k,
       "zoneSetEnforcedZoneListTable": zoneSetEnforcedZoneListTable,
       "zoneSetEnforcedZoneListEntry": zoneSetEnforcedZoneListEntry,
       "zoneSetEnforcedZoneListBmap4k": zoneSetEnforcedZoneListBmap4k,
       "zoneSetEnforcedZoneListBmap6k": zoneSetEnforcedZoneListBmap6k,
       "zoneSetEnforcedZoneListBmap8k": zoneSetEnforcedZoneListBmap8k,
       "zoneCompactTable": zoneCompactTable,
       "zoneCompactEntry": zoneCompactEntry,
       "zoneCompactFirst2k": zoneCompactFirst2k,
       "zoneCompactVsan": zoneCompactVsan,
       "zoneCopyActToFullSpinLock": zoneCopyActToFullSpinLock,
       "zoneCopyActToFullMode": zoneCopyActToFullMode,
       "zoneCopyActToFullVsan": zoneCopyActToFullVsan,
       "zoneStats": zoneStats,
       "zoneTotalGS3Rejects": zoneTotalGS3Rejects,
       "zoneStatsTable": zoneStatsTable,
       "zoneStatsEntry": zoneStatsEntry,
       "zoneTxMergeReqs": zoneTxMergeReqs,
       "zoneRxMergeAccepts": zoneRxMergeAccepts,
       "zoneRxMergeReqs": zoneRxMergeReqs,
       "zoneTxMergeAccepts": zoneTxMergeAccepts,
       "zoneTxChangeReqs": zoneTxChangeReqs,
       "zoneRxChangeAccepts": zoneRxChangeAccepts,
       "zoneRxChangeReqs": zoneRxChangeReqs,
       "zoneTxChangeAccepts": zoneTxChangeAccepts,
       "zoneRxGS3Reqs": zoneRxGS3Reqs,
       "zoneTxGS3Rejects": zoneTxGS3Rejects,
       "zoneLunStatsTable": zoneLunStatsTable,
       "zoneLunStatsEntry": zoneLunStatsEntry,
       "zoneLunSrcFcId": zoneLunSrcFcId,
       "zoneLunDstFcId": zoneLunDstFcId,
       "zoneLunNum": zoneLunNum,
       "zoneLunRxInqReqs": zoneLunRxInqReqs,
       "zoneLunRxRepLunReqs": zoneLunRxRepLunReqs,
       "zoneLunRxSenseReqs": zoneLunRxSenseReqs,
       "zoneLunRxOtherCmds": zoneLunRxOtherCmds,
       "zoneLunTxInqDataNoLus": zoneLunTxInqDataNoLus,
       "zoneLunTxIllegalReqs": zoneLunTxIllegalReqs,
       "zoneRoZoneStatsTable": zoneRoZoneStatsTable,
       "zoneRoZoneStatsEntry": zoneRoZoneStatsEntry,
       "zoneRoZoneSrcFcId": zoneRoZoneSrcFcId,
       "zoneRoZoneDstFcId": zoneRoZoneDstFcId,
       "zoneRoZoneLunNum": zoneRoZoneLunNum,
       "zoneRoZoneTxDataProts": zoneRoZoneTxDataProts,
       "zoneInformation": zoneInformation,
       "zoneServiceRejReasonCode": zoneServiceRejReasonCode,
       "zoneServiceRejReasonCodeExp": zoneServiceRejReasonCodeExp,
       "zoneMergeFailureVSANNum": zoneMergeFailureVSANNum,
       "zoneMergeSuccessVSANNum": zoneMergeSuccessVSANNum,
       "zoneMergeFailureObject": zoneMergeFailureObject,
       "zoneMergeFailureReason": zoneMergeFailureReason,
       "zoneNotification": zoneNotification,
       "zoneNotifications": zoneNotifications,
       "zoneServiceReqRejNotify": zoneServiceReqRejNotify,
       "zoneMergeFailureNotify": zoneMergeFailureNotify,
       "zoneMergeSuccessNotify": zoneMergeSuccessNotify,
       "zoneDefZoneBehaviourChngNotify": zoneDefZoneBehaviourChngNotify,
       "zoneUnsuppMemInIntOpModeNotify": zoneUnsuppMemInIntOpModeNotify,
       "zoneActivateNotify": zoneActivateNotify,
       "zoneCompactNotify": zoneCompactNotify,
       "zoneServerMIBConformance": zoneServerMIBConformance,
       "zoneServerMIBCompliances": zoneServerMIBCompliances,
       "zoneServerMIBCompliance": zoneServerMIBCompliance,
       "zoneServerMIBCompliance1": zoneServerMIBCompliance1,
       "zoneServerMIBComplianceRev2": zoneServerMIBComplianceRev2,
       "zoneServerMIBComplianceRev3": zoneServerMIBComplianceRev3,
       "zoneServerMIBComplianceRev4": zoneServerMIBComplianceRev4,
       "zoneServerMIBComplianceRev5": zoneServerMIBComplianceRev5,
       "zoneServerMIBComplianceRev6": zoneServerMIBComplianceRev6,
       "zoneServerMIBComplianceRev7": zoneServerMIBComplianceRev7,
       "zoneServerMIBComplianceRev8": zoneServerMIBComplianceRev8,
       "zoneServerMIBGroups": zoneServerMIBGroups,
       "zoneConfigurationGroup": zoneConfigurationGroup,
       "zoneStatisticsGroup": zoneStatisticsGroup,
       "zoneNotificationControlGroup": zoneNotificationControlGroup,
       "zoneNotificationGroup": zoneNotificationGroup,
       "zoneConfigurationGroup1": zoneConfigurationGroup1,
       "zoneConfigurationGroup2": zoneConfigurationGroup2,
       "zoneLunStatsGroup": zoneLunStatsGroup,
       "zoneConfigurationGroup3": zoneConfigurationGroup3,
       "zoneNotificationControlGroup1": zoneNotificationControlGroup1,
       "zoneNotificationGroup1": zoneNotificationGroup1,
       "zoneConfigurationGroup4": zoneConfigurationGroup4,
       "zoneConfigurationGroup5": zoneConfigurationGroup5,
       "zoneConfigurationGroup6": zoneConfigurationGroup6,
       "zoneNotificationGroup2": zoneNotificationGroup2,
       "zoneNotificationControlGroup1Sup1": zoneNotificationControlGroup1Sup1,
       "zoneConfigGroupSup1": zoneConfigGroupSup1,
       "zoneNotificationControlGroup1Sup2": zoneNotificationControlGroup1Sup2,
       "zoneNotificationGroup2Sup1": zoneNotificationGroup2Sup1,
       "zoneConfigGroupSup2": zoneConfigGroupSup2,
       "zoneConfigurationGroup7": zoneConfigurationGroup7}
)
