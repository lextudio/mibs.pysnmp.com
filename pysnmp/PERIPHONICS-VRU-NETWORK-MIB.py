# SNMP MIB module (PERIPHONICS-VRU-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PERIPHONICS-VRU-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:28 2024
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

(periphonics,) = mibBuilder.importSymbols(
    "PERIPHONICS-MIB",
    "periphonics")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vruNetwork = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1)
)
vruNetwork.setRevisions(
        ("1998-08-05 00:00",
         "1998-01-05 00:00",
         "1997-07-29 00:00",
         "1997-05-06 00:00",
         "1997-04-08 00:00",
         "1997-03-26 00:00",
         "1997-02-24 00:00",
         "1997-01-18 00:00",
         "1997-01-15 00:00",
         "1996-12-17 00:00",
         "1996-12-04 00:00",
         "1996-07-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VruNetworkMIBConformance_ObjectIdentity = ObjectIdentity
vruNetworkMIBConformance = _VruNetworkMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1)
)
_VruNetworkMIBCompliances_ObjectIdentity = ObjectIdentity
vruNetworkMIBCompliances = _VruNetworkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 1)
)
_VruNetworkMIBGroups_ObjectIdentity = ObjectIdentity
vruNetworkMIBGroups = _VruNetworkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2)
)
_VruEvents_ObjectIdentity = ObjectIdentity
vruEvents = _VruEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2)
)
_VruEventVars_ObjectIdentity = ObjectIdentity
vruEventVars = _VruEventVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 1)
)
_EvObjectId_Type = ObjectIdentifier
_EvObjectId_Object = MibScalar
evObjectId = _EvObjectId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 1, 1),
    _EvObjectId_Type()
)
evObjectId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    evObjectId.setStatus("current")


class _EvChange_Type(Integer32):
    """Custom type evChange based on Integer32"""
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
        *(("add", 2),
          ("del", 3),
          ("mod", 4),
          ("other", 1))
    )


_EvChange_Type.__name__ = "Integer32"
_EvChange_Object = MibScalar
evChange = _EvChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 1, 2),
    _EvChange_Type()
)
evChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    evChange.setStatus("current")
_VruNotifications_ObjectIdentity = ObjectIdentity
vruNotifications = _VruNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2)
)
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3)
)


class _AlrmLogMax_Type(Integer32):
    """Custom type alrmLogMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlrmLogMax_Type.__name__ = "Integer32"
_AlrmLogMax_Object = MibScalar
alrmLogMax = _AlrmLogMax_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 4),
    _AlrmLogMax_Type()
)
alrmLogMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogMax.setStatus("current")


class _AlrmLogNumber_Type(Integer32):
    """Custom type alrmLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlrmLogNumber_Type.__name__ = "Integer32"
_AlrmLogNumber_Object = MibScalar
alrmLogNumber = _AlrmLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 5),
    _AlrmLogNumber_Type()
)
alrmLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogNumber.setStatus("current")
_AlrmLogTable_Object = MibTable
alrmLogTable = _AlrmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    alrmLogTable.setStatus("current")
_AlrmLogTableEntry_Object = MibTableRow
alrmLogTableEntry = _AlrmLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1)
)
alrmLogTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "alrmLogIdx"),
)
if mibBuilder.loadTexts:
    alrmLogTableEntry.setStatus("current")


class _AlrmLogIdx_Type(Integer32):
    """Custom type alrmLogIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlrmLogIdx_Type.__name__ = "Integer32"
_AlrmLogIdx_Object = MibTableColumn
alrmLogIdx = _AlrmLogIdx_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 1),
    _AlrmLogIdx_Type()
)
alrmLogIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alrmLogIdx.setStatus("current")


class _AlrmLogSeverity_Type(Integer32):
    """Custom type alrmLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AlrmLogSeverity_Type.__name__ = "Integer32"
_AlrmLogSeverity_Object = MibTableColumn
alrmLogSeverity = _AlrmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 2),
    _AlrmLogSeverity_Type()
)
alrmLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogSeverity.setStatus("current")


class _AlrmLogCode_Type(Integer32):
    """Custom type alrmLogCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlrmLogCode_Type.__name__ = "Integer32"
_AlrmLogCode_Object = MibTableColumn
alrmLogCode = _AlrmLogCode_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 3),
    _AlrmLogCode_Type()
)
alrmLogCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogCode.setStatus("current")


class _AlrmLogVruId_Type(Integer32):
    """Custom type alrmLogVruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlrmLogVruId_Type.__name__ = "Integer32"
_AlrmLogVruId_Object = MibTableColumn
alrmLogVruId = _AlrmLogVruId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 4),
    _AlrmLogVruId_Type()
)
alrmLogVruId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogVruId.setStatus("deprecated")


class _AlrmLogLineId_Type(Integer32):
    """Custom type alrmLogLineId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlrmLogLineId_Type.__name__ = "Integer32"
_AlrmLogLineId_Object = MibTableColumn
alrmLogLineId = _AlrmLogLineId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 5),
    _AlrmLogLineId_Type()
)
alrmLogLineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogLineId.setStatus("current")


class _AlrmLogHostId_Type(Integer32):
    """Custom type alrmLogHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlrmLogHostId_Type.__name__ = "Integer32"
_AlrmLogHostId_Object = MibTableColumn
alrmLogHostId = _AlrmLogHostId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 6),
    _AlrmLogHostId_Type()
)
alrmLogHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogHostId.setStatus("current")
_AlrmLogProcName_Type = DisplayString
_AlrmLogProcName_Object = MibTableColumn
alrmLogProcName = _AlrmLogProcName_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 7),
    _AlrmLogProcName_Type()
)
alrmLogProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogProcName.setStatus("current")
_AlrmLogMessage_Type = DisplayString
_AlrmLogMessage_Object = MibTableColumn
alrmLogMessage = _AlrmLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 8),
    _AlrmLogMessage_Type()
)
alrmLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogMessage.setStatus("current")
_AlrmLogTime_Type = DateAndTime
_AlrmLogTime_Object = MibTableColumn
alrmLogTime = _AlrmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 9),
    _AlrmLogTime_Type()
)
alrmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogTime.setStatus("current")


class _AlrmLogComponentType_Type(Integer32):
    """Custom type alrmLogComponentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlrmLogComponentType_Type.__name__ = "Integer32"
_AlrmLogComponentType_Object = MibTableColumn
alrmLogComponentType = _AlrmLogComponentType_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 10),
    _AlrmLogComponentType_Type()
)
alrmLogComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogComponentType.setStatus("current")


class _AlrmLogComponentId_Type(Integer32):
    """Custom type alrmLogComponentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlrmLogComponentId_Type.__name__ = "Integer32"
_AlrmLogComponentId_Object = MibTableColumn
alrmLogComponentId = _AlrmLogComponentId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 11),
    _AlrmLogComponentId_Type()
)
alrmLogComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogComponentId.setStatus("current")
_AlrmLogComponentIpAddress_Type = IpAddress
_AlrmLogComponentIpAddress_Object = MibTableColumn
alrmLogComponentIpAddress = _AlrmLogComponentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 3, 6, 1, 12),
    _AlrmLogComponentIpAddress_Type()
)
alrmLogComponentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrmLogComponentIpAddress.setStatus("current")
_VruTable_Object = MibTable
vruTable = _VruTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3)
)
if mibBuilder.loadTexts:
    vruTable.setStatus("current")
_VruTableEntry_Object = MibTableRow
vruTableEntry = _VruTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1)
)
vruTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "vruId"),
)
if mibBuilder.loadTexts:
    vruTableEntry.setStatus("current")


class _VruId_Type(Integer32):
    """Custom type vruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VruId_Type.__name__ = "Integer32"
_VruId_Object = MibTableColumn
vruId = _VruId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 1),
    _VruId_Type()
)
vruId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vruId.setStatus("current")
_VruIpAddress_Type = IpAddress
_VruIpAddress_Object = MibTableColumn
vruIpAddress = _VruIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 2),
    _VruIpAddress_Type()
)
vruIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vruIpAddress.setStatus("current")
_VruDescr_Type = DisplayString
_VruDescr_Object = MibTableColumn
vruDescr = _VruDescr_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 3),
    _VruDescr_Type()
)
vruDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vruDescr.setStatus("current")


class _VruLineCnt_Type(Integer32):
    """Custom type vruLineCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VruLineCnt_Type.__name__ = "Integer32"
_VruLineCnt_Object = MibTableColumn
vruLineCnt = _VruLineCnt_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 4),
    _VruLineCnt_Type()
)
vruLineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vruLineCnt.setStatus("current")


class _VruSpanCnt_Type(Integer32):
    """Custom type vruSpanCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VruSpanCnt_Type.__name__ = "Integer32"
_VruSpanCnt_Object = MibTableColumn
vruSpanCnt = _VruSpanCnt_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 5),
    _VruSpanCnt_Type()
)
vruSpanCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vruSpanCnt.setStatus("current")


class _VruHostCnt_Type(Integer32):
    """Custom type vruHostCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VruHostCnt_Type.__name__ = "Integer32"
_VruHostCnt_Object = MibTableColumn
vruHostCnt = _VruHostCnt_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 6),
    _VruHostCnt_Type()
)
vruHostCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vruHostCnt.setStatus("current")


class _VruAdminState_Type(Integer32):
    """Custom type vruAdminState based on Integer32"""
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
        *(("checkpoint", 6),
          ("other", 1),
          ("recycle", 4),
          ("selftest", 5),
          ("shutdown", 3),
          ("startup", 2))
    )


_VruAdminState_Type.__name__ = "Integer32"
_VruAdminState_Object = MibTableColumn
vruAdminState = _VruAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 7),
    _VruAdminState_Type()
)
vruAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vruAdminState.setStatus("current")


class _VruState_Type(Integer32):
    """Custom type vruState based on Integer32"""
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
        *(("down", 5),
          ("init", 3),
          ("other", 1),
          ("selftest", 6),
          ("unknown", 2),
          ("up", 4))
    )


_VruState_Type.__name__ = "Integer32"
_VruState_Object = MibTableColumn
vruState = _VruState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 8),
    _VruState_Type()
)
vruState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vruState.setStatus("current")
_VruStateLastChange_Type = DateAndTime
_VruStateLastChange_Object = MibTableColumn
vruStateLastChange = _VruStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 3, 1, 9),
    _VruStateLastChange_Type()
)
vruStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vruStateLastChange.setStatus("current")
_LineTable_Object = MibTable
lineTable = _LineTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4)
)
if mibBuilder.loadTexts:
    lineTable.setStatus("current")
_LineTableEntry_Object = MibTableRow
lineTableEntry = _LineTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1)
)
lineTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "lineVruId"),
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "lineId"),
)
if mibBuilder.loadTexts:
    lineTableEntry.setStatus("current")


class _LineVruId_Type(Integer32):
    """Custom type lineVruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LineVruId_Type.__name__ = "Integer32"
_LineVruId_Object = MibTableColumn
lineVruId = _LineVruId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 1),
    _LineVruId_Type()
)
lineVruId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineVruId.setStatus("current")


class _LineId_Type(Integer32):
    """Custom type lineId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LineId_Type.__name__ = "Integer32"
_LineId_Object = MibTableColumn
lineId = _LineId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 2),
    _LineId_Type()
)
lineId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineId.setStatus("current")


class _LineType_Type(Integer32):
    """Custom type lineType based on Integer32"""
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
        *(("analog", 4),
          ("digital", 5),
          ("other", 1),
          ("unknown", 2),
          ("virtual", 3))
    )


_LineType_Type.__name__ = "Integer32"
_LineType_Object = MibTableColumn
lineType = _LineType_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 3),
    _LineType_Type()
)
lineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineType.setStatus("current")


class _LineProtocol_Type(Integer32):
    """Custom type lineProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LineProtocol_Type.__name__ = "Integer32"
_LineProtocol_Object = MibTableColumn
lineProtocol = _LineProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 4),
    _LineProtocol_Type()
)
lineProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineProtocol.setStatus("current")


class _LineState_Type(Integer32):
    """Custom type lineState based on Integer32"""
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
        *(("busy", 5),
          ("connected", 3),
          ("down", 7),
          ("idle", 4),
          ("other", 1),
          ("referral", 6),
          ("unknown", 2))
    )


_LineState_Type.__name__ = "Integer32"
_LineState_Object = MibTableColumn
lineState = _LineState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 5),
    _LineState_Type()
)
lineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineState.setStatus("current")
_LineAppName_Type = DisplayString
_LineAppName_Object = MibTableColumn
lineAppName = _LineAppName_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 6),
    _LineAppName_Type()
)
lineAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineAppName.setStatus("current")
_LineAppOverlay_Type = DisplayString
_LineAppOverlay_Object = MibTableColumn
lineAppOverlay = _LineAppOverlay_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 7),
    _LineAppOverlay_Type()
)
lineAppOverlay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineAppOverlay.setStatus("current")


class _LineAppAdminState_Type(Integer32):
    """Custom type lineAppAdminState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("assign", 5),
          ("hardrestart", 7),
          ("hardterm", 4),
          ("other", 1),
          ("softrestart", 8),
          ("softterm", 3),
          ("startapp", 2),
          ("unassign", 6))
    )


_LineAppAdminState_Type.__name__ = "Integer32"
_LineAppAdminState_Object = MibTableColumn
lineAppAdminState = _LineAppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 8),
    _LineAppAdminState_Type()
)
lineAppAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineAppAdminState.setStatus("current")


class _LineAppState_Type(Integer32):
    """Custom type lineAppState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("config", 7),
          ("down", 6),
          ("exit", 8),
          ("init", 4),
          ("noapp", 3),
          ("other", 1),
          ("unknown", 2),
          ("up", 5))
    )


_LineAppState_Type.__name__ = "Integer32"
_LineAppState_Object = MibTableColumn
lineAppState = _LineAppState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 9),
    _LineAppState_Type()
)
lineAppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineAppState.setStatus("current")
_LineAppStateLastChange_Type = DateAndTime
_LineAppStateLastChange_Object = MibTableColumn
lineAppStateLastChange = _LineAppStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 10),
    _LineAppStateLastChange_Type()
)
lineAppStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineAppStateLastChange.setStatus("current")
_LineAppCfgLastChange_Type = DateAndTime
_LineAppCfgLastChange_Object = MibTableColumn
lineAppCfgLastChange = _LineAppCfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 4, 1, 11),
    _LineAppCfgLastChange_Type()
)
lineAppCfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineAppCfgLastChange.setStatus("current")
_SpanTable_Object = MibTable
spanTable = _SpanTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5)
)
if mibBuilder.loadTexts:
    spanTable.setStatus("current")
_SpanTableEntry_Object = MibTableRow
spanTableEntry = _SpanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5, 1)
)
spanTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "spanVruId"),
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "spanId"),
)
if mibBuilder.loadTexts:
    spanTableEntry.setStatus("current")


class _SpanVruId_Type(Integer32):
    """Custom type spanVruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SpanVruId_Type.__name__ = "Integer32"
_SpanVruId_Object = MibTableColumn
spanVruId = _SpanVruId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5, 1, 1),
    _SpanVruId_Type()
)
spanVruId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spanVruId.setStatus("current")


class _SpanId_Type(Integer32):
    """Custom type spanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SpanId_Type.__name__ = "Integer32"
_SpanId_Object = MibTableColumn
spanId = _SpanId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5, 1, 2),
    _SpanId_Type()
)
spanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spanId.setStatus("current")


class _SpanLineIdStart_Type(Integer32):
    """Custom type spanLineIdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SpanLineIdStart_Type.__name__ = "Integer32"
_SpanLineIdStart_Object = MibTableColumn
spanLineIdStart = _SpanLineIdStart_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5, 1, 3),
    _SpanLineIdStart_Type()
)
spanLineIdStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanLineIdStart.setStatus("current")


class _SpanLineNumber_Type(Integer32):
    """Custom type spanLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(24,
              30)
        )
    )
    namedValues = NamedValues(
        *(("europaLineNumber", 30),
          ("usaLineNumber", 24))
    )


_SpanLineNumber_Type.__name__ = "Integer32"
_SpanLineNumber_Object = MibTableColumn
spanLineNumber = _SpanLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5, 1, 4),
    _SpanLineNumber_Type()
)
spanLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanLineNumber.setStatus("current")
_SpanEnabled_Type = TruthValue
_SpanEnabled_Object = MibTableColumn
spanEnabled = _SpanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5, 1, 5),
    _SpanEnabled_Type()
)
spanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanEnabled.setStatus("current")


class _SpanState_Type(Integer32):
    """Custom type spanState based on Integer32"""
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
        *(("fatal", 5),
          ("green", 4),
          ("init", 3),
          ("other", 1),
          ("red", 7),
          ("unknown", 2),
          ("yellow", 6))
    )


_SpanState_Type.__name__ = "Integer32"
_SpanState_Object = MibTableColumn
spanState = _SpanState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5, 1, 6),
    _SpanState_Type()
)
spanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanState.setStatus("current")
_SpanStateLastChange_Type = DateAndTime
_SpanStateLastChange_Object = MibTableColumn
spanStateLastChange = _SpanStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 5, 1, 7),
    _SpanStateLastChange_Type()
)
spanStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanStateLastChange.setStatus("current")
_AppTable_Object = MibTable
appTable = _AppTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 6)
)
if mibBuilder.loadTexts:
    appTable.setStatus("current")
_AppTableEntry_Object = MibTableRow
appTableEntry = _AppTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 6, 1)
)
appTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "appVruId"),
    (1, "PERIPHONICS-VRU-NETWORK-MIB", "appName"),
)
if mibBuilder.loadTexts:
    appTableEntry.setStatus("current")


class _AppVruId_Type(Integer32):
    """Custom type appVruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AppVruId_Type.__name__ = "Integer32"
_AppVruId_Object = MibTableColumn
appVruId = _AppVruId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 6, 1, 1),
    _AppVruId_Type()
)
appVruId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appVruId.setStatus("current")


class _AppName_Type(DisplayString):
    """Custom type appName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AppName_Type.__name__ = "DisplayString"
_AppName_Object = MibTableColumn
appName = _AppName_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 6, 1, 2),
    _AppName_Type()
)
appName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appName.setStatus("current")
_AppDescr_Type = DisplayString
_AppDescr_Object = MibTableColumn
appDescr = _AppDescr_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 6, 1, 3),
    _AppDescr_Type()
)
appDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appDescr.setStatus("current")
_AppOptions_Type = DisplayString
_AppOptions_Object = MibTableColumn
appOptions = _AppOptions_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 6, 1, 4),
    _AppOptions_Type()
)
appOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appOptions.setStatus("current")


class _AppLineCnt_Type(Integer32):
    """Custom type appLineCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AppLineCnt_Type.__name__ = "Integer32"
_AppLineCnt_Object = MibTableColumn
appLineCnt = _AppLineCnt_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 6, 1, 5),
    _AppLineCnt_Type()
)
appLineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLineCnt.setStatus("current")
_AppStatsTable_Object = MibTable
appStatsTable = _AppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 7)
)
if mibBuilder.loadTexts:
    appStatsTable.setStatus("current")
_AppStatsTableEntry_Object = MibTableRow
appStatsTableEntry = _AppStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 7, 1)
)
appStatsTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "appStatsVruId"),
    (1, "PERIPHONICS-VRU-NETWORK-MIB", "appStatsName"),
)
if mibBuilder.loadTexts:
    appStatsTableEntry.setStatus("current")


class _AppStatsVruId_Type(Integer32):
    """Custom type appStatsVruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AppStatsVruId_Type.__name__ = "Integer32"
_AppStatsVruId_Object = MibTableColumn
appStatsVruId = _AppStatsVruId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 7, 1, 1),
    _AppStatsVruId_Type()
)
appStatsVruId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appStatsVruId.setStatus("current")


class _AppStatsName_Type(DisplayString):
    """Custom type appStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AppStatsName_Type.__name__ = "DisplayString"
_AppStatsName_Object = MibTableColumn
appStatsName = _AppStatsName_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 7, 1, 2),
    _AppStatsName_Type()
)
appStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appStatsName.setStatus("current")


class _AppStatsValue_Type(Integer32):
    """Custom type appStatsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AppStatsValue_Type.__name__ = "Integer32"
_AppStatsValue_Object = MibTableColumn
appStatsValue = _AppStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 7, 1, 3),
    _AppStatsValue_Type()
)
appStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appStatsValue.setStatus("current")
_AppStatsLastChange_Type = DateAndTime
_AppStatsLastChange_Object = MibTableColumn
appStatsLastChange = _AppStatsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 7, 1, 4),
    _AppStatsLastChange_Type()
)
appStatsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appStatsLastChange.setStatus("current")
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("current")
_HostTableEntry_Object = MibTableRow
hostTableEntry = _HostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1)
)
hostTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "hostVruId"),
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "hostId"),
)
if mibBuilder.loadTexts:
    hostTableEntry.setStatus("current")


class _HostVruId_Type(Integer32):
    """Custom type hostVruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HostVruId_Type.__name__ = "Integer32"
_HostVruId_Object = MibTableColumn
hostVruId = _HostVruId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 1),
    _HostVruId_Type()
)
hostVruId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostVruId.setStatus("current")


class _HostId_Type(Integer32):
    """Custom type hostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HostId_Type.__name__ = "Integer32"
_HostId_Object = MibTableColumn
hostId = _HostId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 2),
    _HostId_Type()
)
hostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostId.setStatus("current")
_HostDescr_Type = DisplayString
_HostDescr_Object = MibTableColumn
hostDescr = _HostDescr_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 3),
    _HostDescr_Type()
)
hostDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostDescr.setStatus("current")


class _HostLuCnt_Type(Integer32):
    """Custom type hostLuCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HostLuCnt_Type.__name__ = "Integer32"
_HostLuCnt_Object = MibTableColumn
hostLuCnt = _HostLuCnt_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 4),
    _HostLuCnt_Type()
)
hostLuCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostLuCnt.setStatus("current")


class _HostProtocol_Type(Integer32):
    """Custom type hostProtocol based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("async", 4),
          ("atte", 3),
          ("lu62", 5),
          ("other", 1),
          ("sdlcexp", 7),
          ("sna3270", 6),
          ("unknown", 2),
          ("vpstn3270", 8))
    )


_HostProtocol_Type.__name__ = "Integer32"
_HostProtocol_Object = MibTableColumn
hostProtocol = _HostProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 5),
    _HostProtocol_Type()
)
hostProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostProtocol.setStatus("current")


class _HostMedia_Type(Integer32):
    """Custom type hostMedia based on Integer32"""
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
        *(("hardwarebased", 3),
          ("other", 1),
          ("softwarebased", 4),
          ("unknown", 2))
    )


_HostMedia_Type.__name__ = "Integer32"
_HostMedia_Object = MibTableColumn
hostMedia = _HostMedia_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 6),
    _HostMedia_Type()
)
hostMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMedia.setStatus("current")


class _HostAdminState_Type(Integer32):
    """Custom type hostAdminState based on Integer32"""
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
        *(("down", 4),
          ("init", 2),
          ("other", 1),
          ("recycle", 5),
          ("selftest", 6),
          ("up", 3))
    )


_HostAdminState_Type.__name__ = "Integer32"
_HostAdminState_Object = MibTableColumn
hostAdminState = _HostAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 8),
    _HostAdminState_Type()
)
hostAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostAdminState.setStatus("current")


class _HostState_Type(Integer32):
    """Custom type hostState based on Integer32"""
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
        *(("down", 5),
          ("init", 3),
          ("other", 1),
          ("selftest", 6),
          ("unknown", 2),
          ("up", 4))
    )


_HostState_Type.__name__ = "Integer32"
_HostState_Object = MibTableColumn
hostState = _HostState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 9),
    _HostState_Type()
)
hostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostState.setStatus("current")
_HostStateLastChange_Type = DateAndTime
_HostStateLastChange_Object = MibTableColumn
hostStateLastChange = _HostStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 8, 1, 10),
    _HostStateLastChange_Type()
)
hostStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStateLastChange.setStatus("current")
_LuTable_Object = MibTable
luTable = _LuTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9)
)
if mibBuilder.loadTexts:
    luTable.setStatus("current")
_LuTableEntry_Object = MibTableRow
luTableEntry = _LuTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9, 1)
)
luTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "luVruId"),
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "luHostId"),
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "luId"),
)
if mibBuilder.loadTexts:
    luTableEntry.setStatus("current")


class _LuVruId_Type(Integer32):
    """Custom type luVruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LuVruId_Type.__name__ = "Integer32"
_LuVruId_Object = MibTableColumn
luVruId = _LuVruId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9, 1, 1),
    _LuVruId_Type()
)
luVruId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    luVruId.setStatus("current")


class _LuHostId_Type(Integer32):
    """Custom type luHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LuHostId_Type.__name__ = "Integer32"
_LuHostId_Object = MibTableColumn
luHostId = _LuHostId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9, 1, 2),
    _LuHostId_Type()
)
luHostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    luHostId.setStatus("current")


class _LuId_Type(Integer32):
    """Custom type luId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LuId_Type.__name__ = "Integer32"
_LuId_Object = MibTableColumn
luId = _LuId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9, 1, 3),
    _LuId_Type()
)
luId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    luId.setStatus("current")
_LuDescr_Type = DisplayString
_LuDescr_Object = MibTableColumn
luDescr = _LuDescr_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9, 1, 4),
    _LuDescr_Type()
)
luDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDescr.setStatus("current")
_LuPoolName_Type = DisplayString
_LuPoolName_Object = MibTableColumn
luPoolName = _LuPoolName_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9, 1, 5),
    _LuPoolName_Type()
)
luPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luPoolName.setStatus("current")


class _LuState_Type(Integer32):
    """Custom type luState based on Integer32"""
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
        *(("down", 5),
          ("init", 3),
          ("other", 1),
          ("unknown", 2),
          ("up", 4))
    )


_LuState_Type.__name__ = "Integer32"
_LuState_Object = MibTableColumn
luState = _LuState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9, 1, 6),
    _LuState_Type()
)
luState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luState.setStatus("current")
_LuStateLastChange_Type = DateAndTime
_LuStateLastChange_Object = MibTableColumn
luStateLastChange = _LuStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 9, 1, 7),
    _LuStateLastChange_Type()
)
luStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luStateLastChange.setStatus("current")
_Components_ObjectIdentity = ObjectIdentity
components = _Components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10)
)
_ComponentTypeTable_Object = MibTable
componentTypeTable = _ComponentTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 1)
)
if mibBuilder.loadTexts:
    componentTypeTable.setStatus("current")
_ComponentTypeTableEntry_Object = MibTableRow
componentTypeTableEntry = _ComponentTypeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 1, 1)
)
componentTypeTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "componentTypeId"),
)
if mibBuilder.loadTexts:
    componentTypeTableEntry.setStatus("current")


class _ComponentTypeId_Type(Integer32):
    """Custom type componentTypeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ComponentTypeId_Type.__name__ = "Integer32"
_ComponentTypeId_Object = MibTableColumn
componentTypeId = _ComponentTypeId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 1, 1, 1),
    _ComponentTypeId_Type()
)
componentTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentTypeId.setStatus("current")
_ComponentTypeName_Type = DisplayString
_ComponentTypeName_Object = MibTableColumn
componentTypeName = _ComponentTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 1, 1, 2),
    _ComponentTypeName_Type()
)
componentTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentTypeName.setStatus("current")
_ComponentTable_Object = MibTable
componentTable = _ComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 3)
)
if mibBuilder.loadTexts:
    componentTable.setStatus("current")
_ComponentTableEntry_Object = MibTableRow
componentTableEntry = _ComponentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 3, 1)
)
componentTableEntry.setIndexNames(
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "componentType"),
    (0, "PERIPHONICS-VRU-NETWORK-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    componentTableEntry.setStatus("current")


class _ComponentType_Type(Integer32):
    """Custom type componentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ComponentType_Type.__name__ = "Integer32"
_ComponentType_Object = MibTableColumn
componentType = _ComponentType_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 3, 1, 1),
    _ComponentType_Type()
)
componentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentType.setStatus("current")


class _ComponentId_Type(Integer32):
    """Custom type componentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ComponentId_Type.__name__ = "Integer32"
_ComponentId_Object = MibTableColumn
componentId = _ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 3, 1, 2),
    _ComponentId_Type()
)
componentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentId.setStatus("current")
_ComponentIpAddress_Type = IpAddress
_ComponentIpAddress_Object = MibTableColumn
componentIpAddress = _ComponentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 3, 1, 3),
    _ComponentIpAddress_Type()
)
componentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentIpAddress.setStatus("current")


class _ComponentState_Type(Integer32):
    """Custom type componentState based on Integer32"""
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
        *(("down", 5),
          ("init", 3),
          ("other", 1),
          ("unknown", 2),
          ("up", 4))
    )


_ComponentState_Type.__name__ = "Integer32"
_ComponentState_Object = MibTableColumn
componentState = _ComponentState_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 3, 1, 4),
    _ComponentState_Type()
)
componentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentState.setStatus("current")
_ComponentStateLastChange_Type = DateAndTime
_ComponentStateLastChange_Object = MibTableColumn
componentStateLastChange = _ComponentStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1357, 1, 10, 3, 1, 5),
    _ComponentStateLastChange_Type()
)
componentStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStateLastChange.setStatus("current")

# Managed Objects groups

vruEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 2)
)
vruEventsGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "evObjectId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "evChange"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMax"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogNumber"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogSeverity"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogCode"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogVruId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogLineId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogHostId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogProcName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMessage"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogTime"))
)
if mibBuilder.loadTexts:
    vruEventsGroup.setStatus("deprecated")

vruGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 3)
)
vruGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "vruIpAddress"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "vruDescr"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "vruLineCnt"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "vruSpanCnt"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "vruHostCnt"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "vruAdminState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "vruState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "vruStateLastChange"))
)
if mibBuilder.loadTexts:
    vruGroup.setStatus("current")

lineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 4)
)
lineGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "lineType"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineProtocol"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineAppName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineAppOverlay"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineAppAdminState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineAppState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineAppStateLastChange"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineAppCfgLastChange"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "spanLineIdStart"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "spanLineNumber"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "spanEnabled"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "spanState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "spanStateLastChange"))
)
if mibBuilder.loadTexts:
    lineGroup.setStatus("current")

applicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 5)
)
applicationGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "appDescr"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "appOptions"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "appLineCnt"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "appStatsValue"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "appStatsLastChange"))
)
if mibBuilder.loadTexts:
    applicationGroup.setStatus("current")

hostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 6)
)
hostGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "hostDescr"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "hostLuCnt"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "hostProtocol"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "hostMedia"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "hostAdminState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "hostState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "hostStateLastChange"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "luDescr"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "luPoolName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "luState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "luStateLastChange"))
)
if mibBuilder.loadTexts:
    hostGroup.setStatus("current")

componentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 7)
)
componentGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "componentTypeName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "componentIpAddress"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "componentState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "componentStateLastChange"))
)
if mibBuilder.loadTexts:
    componentGroup.setStatus("current")

componentEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 9)
)
componentEventsGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "evObjectId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "evChange"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMax"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogNumber"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogSeverity"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogCode"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogLineId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogHostId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogProcName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMessage"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogTime"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentType"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentId"))
)
if mibBuilder.loadTexts:
    componentEventsGroup.setStatus("deprecated")

componentEventsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 11)
)
componentEventsGroup2.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "evObjectId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "evChange"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMax"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogNumber"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogSeverity"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogCode"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogLineId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogHostId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogProcName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMessage"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogTime"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentType"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentIpAddress"))
)
if mibBuilder.loadTexts:
    componentEventsGroup2.setStatus("current")


# Notification objects

notifyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 1)
)
notifyAlarm.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogSeverity"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogCode"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogVruId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogLineId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogHostId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogProcName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMessage"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogTime"))
)
if mibBuilder.loadTexts:
    notifyAlarm.setStatus(
        "deprecated"
    )

notifyVruStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 2)
)
notifyVruStateChg.setObjects(
    ("PERIPHONICS-VRU-NETWORK-MIB", "vruState")
)
if mibBuilder.loadTexts:
    notifyVruStateChg.setStatus(
        "deprecated"
    )

notifyLineAppStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 3)
)
notifyLineAppStateChg.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "lineAppState"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineAppName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "lineAppOverlay"))
)
if mibBuilder.loadTexts:
    notifyLineAppStateChg.setStatus(
        "current"
    )

notifySpanStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 4)
)
notifySpanStateChg.setObjects(
    ("PERIPHONICS-VRU-NETWORK-MIB", "spanState")
)
if mibBuilder.loadTexts:
    notifySpanStateChg.setStatus(
        "current"
    )

notifyHostStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 5)
)
notifyHostStateChg.setObjects(
    ("PERIPHONICS-VRU-NETWORK-MIB", "hostState")
)
if mibBuilder.loadTexts:
    notifyHostStateChg.setStatus(
        "current"
    )

notifyLuStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 6)
)
notifyLuStateChg.setObjects(
    ("PERIPHONICS-VRU-NETWORK-MIB", "luState")
)
if mibBuilder.loadTexts:
    notifyLuStateChg.setStatus(
        "current"
    )

notifyTopologyChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 7)
)
notifyTopologyChg.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "evObjectId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "evChange"))
)
if mibBuilder.loadTexts:
    notifyTopologyChg.setStatus(
        "current"
    )

notifyComponentStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 8)
)
notifyComponentStateChg.setObjects(
    ("PERIPHONICS-VRU-NETWORK-MIB", "componentState")
)
if mibBuilder.loadTexts:
    notifyComponentStateChg.setStatus(
        "current"
    )

notifyAlarmByComponent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 9)
)
notifyAlarmByComponent.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentType"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogSeverity"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogCode"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogLineId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogHostId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogProcName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMessage"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogTime"))
)
if mibBuilder.loadTexts:
    notifyAlarmByComponent.setStatus(
        "deprecated"
    )

notifyAlarmByComponentEx = NotificationType(
    (1, 3, 6, 1, 4, 1, 1357, 1, 2, 2, 10)
)
notifyAlarmByComponentEx.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentType"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogSeverity"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogCode"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogLineId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogHostId"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogProcName"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogMessage"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogTime"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "alrmLogComponentIpAddress"))
)
if mibBuilder.loadTexts:
    notifyAlarmByComponentEx.setStatus(
        "current"
    )


# Notifications groups

vruNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 1)
)
vruNotificationsGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "notifyAlarm"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyVruStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyLineAppStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifySpanStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyHostStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyLuStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyTopologyChg"))
)
if mibBuilder.loadTexts:
    vruNotificationsGroup.setStatus(
        "deprecated"
    )

componentNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 8)
)
componentNotificationsGroup.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "notifyLineAppStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifySpanStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyHostStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyLuStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyTopologyChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyComponentStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyAlarmByComponent"))
)
if mibBuilder.loadTexts:
    componentNotificationsGroup.setStatus(
        "deprecated"
    )

componentNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 2, 10)
)
componentNotificationsGroup2.setObjects(
      *(("PERIPHONICS-VRU-NETWORK-MIB", "notifyLineAppStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifySpanStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyHostStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyLuStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyTopologyChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyComponentStateChg"),
        ("PERIPHONICS-VRU-NETWORK-MIB", "notifyAlarmByComponentEx"))
)
if mibBuilder.loadTexts:
    componentNotificationsGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vruNetworkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vruNetworkMIBCompliance.setStatus(
        "deprecated"
    )

vruNetworkMIBComplianceByComponent = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vruNetworkMIBComplianceByComponent.setStatus(
        "deprecated"
    )

vruNetworkMIBComplianceByComponent2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1357, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vruNetworkMIBComplianceByComponent2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PERIPHONICS-VRU-NETWORK-MIB",
    **{"vruNetwork": vruNetwork,
       "vruNetworkMIBConformance": vruNetworkMIBConformance,
       "vruNetworkMIBCompliances": vruNetworkMIBCompliances,
       "vruNetworkMIBCompliance": vruNetworkMIBCompliance,
       "vruNetworkMIBComplianceByComponent": vruNetworkMIBComplianceByComponent,
       "vruNetworkMIBComplianceByComponent2": vruNetworkMIBComplianceByComponent2,
       "vruNetworkMIBGroups": vruNetworkMIBGroups,
       "vruNotificationsGroup": vruNotificationsGroup,
       "vruEventsGroup": vruEventsGroup,
       "vruGroup": vruGroup,
       "lineGroup": lineGroup,
       "applicationGroup": applicationGroup,
       "hostGroup": hostGroup,
       "componentGroup": componentGroup,
       "componentNotificationsGroup": componentNotificationsGroup,
       "componentEventsGroup": componentEventsGroup,
       "componentNotificationsGroup2": componentNotificationsGroup2,
       "componentEventsGroup2": componentEventsGroup2,
       "vruEvents": vruEvents,
       "vruEventVars": vruEventVars,
       "evObjectId": evObjectId,
       "evChange": evChange,
       "vruNotifications": vruNotifications,
       "notifyAlarm": notifyAlarm,
       "notifyVruStateChg": notifyVruStateChg,
       "notifyLineAppStateChg": notifyLineAppStateChg,
       "notifySpanStateChg": notifySpanStateChg,
       "notifyHostStateChg": notifyHostStateChg,
       "notifyLuStateChg": notifyLuStateChg,
       "notifyTopologyChg": notifyTopologyChg,
       "notifyComponentStateChg": notifyComponentStateChg,
       "notifyAlarmByComponent": notifyAlarmByComponent,
       "notifyAlarmByComponentEx": notifyAlarmByComponentEx,
       "alarms": alarms,
       "alrmLogMax": alrmLogMax,
       "alrmLogNumber": alrmLogNumber,
       "alrmLogTable": alrmLogTable,
       "alrmLogTableEntry": alrmLogTableEntry,
       "alrmLogIdx": alrmLogIdx,
       "alrmLogSeverity": alrmLogSeverity,
       "alrmLogCode": alrmLogCode,
       "alrmLogVruId": alrmLogVruId,
       "alrmLogLineId": alrmLogLineId,
       "alrmLogHostId": alrmLogHostId,
       "alrmLogProcName": alrmLogProcName,
       "alrmLogMessage": alrmLogMessage,
       "alrmLogTime": alrmLogTime,
       "alrmLogComponentType": alrmLogComponentType,
       "alrmLogComponentId": alrmLogComponentId,
       "alrmLogComponentIpAddress": alrmLogComponentIpAddress,
       "vruTable": vruTable,
       "vruTableEntry": vruTableEntry,
       "vruId": vruId,
       "vruIpAddress": vruIpAddress,
       "vruDescr": vruDescr,
       "vruLineCnt": vruLineCnt,
       "vruSpanCnt": vruSpanCnt,
       "vruHostCnt": vruHostCnt,
       "vruAdminState": vruAdminState,
       "vruState": vruState,
       "vruStateLastChange": vruStateLastChange,
       "lineTable": lineTable,
       "lineTableEntry": lineTableEntry,
       "lineVruId": lineVruId,
       "lineId": lineId,
       "lineType": lineType,
       "lineProtocol": lineProtocol,
       "lineState": lineState,
       "lineAppName": lineAppName,
       "lineAppOverlay": lineAppOverlay,
       "lineAppAdminState": lineAppAdminState,
       "lineAppState": lineAppState,
       "lineAppStateLastChange": lineAppStateLastChange,
       "lineAppCfgLastChange": lineAppCfgLastChange,
       "spanTable": spanTable,
       "spanTableEntry": spanTableEntry,
       "spanVruId": spanVruId,
       "spanId": spanId,
       "spanLineIdStart": spanLineIdStart,
       "spanLineNumber": spanLineNumber,
       "spanEnabled": spanEnabled,
       "spanState": spanState,
       "spanStateLastChange": spanStateLastChange,
       "appTable": appTable,
       "appTableEntry": appTableEntry,
       "appVruId": appVruId,
       "appName": appName,
       "appDescr": appDescr,
       "appOptions": appOptions,
       "appLineCnt": appLineCnt,
       "appStatsTable": appStatsTable,
       "appStatsTableEntry": appStatsTableEntry,
       "appStatsVruId": appStatsVruId,
       "appStatsName": appStatsName,
       "appStatsValue": appStatsValue,
       "appStatsLastChange": appStatsLastChange,
       "hostTable": hostTable,
       "hostTableEntry": hostTableEntry,
       "hostVruId": hostVruId,
       "hostId": hostId,
       "hostDescr": hostDescr,
       "hostLuCnt": hostLuCnt,
       "hostProtocol": hostProtocol,
       "hostMedia": hostMedia,
       "hostAdminState": hostAdminState,
       "hostState": hostState,
       "hostStateLastChange": hostStateLastChange,
       "luTable": luTable,
       "luTableEntry": luTableEntry,
       "luVruId": luVruId,
       "luHostId": luHostId,
       "luId": luId,
       "luDescr": luDescr,
       "luPoolName": luPoolName,
       "luState": luState,
       "luStateLastChange": luStateLastChange,
       "components": components,
       "componentTypeTable": componentTypeTable,
       "componentTypeTableEntry": componentTypeTableEntry,
       "componentTypeId": componentTypeId,
       "componentTypeName": componentTypeName,
       "componentTable": componentTable,
       "componentTableEntry": componentTableEntry,
       "componentType": componentType,
       "componentId": componentId,
       "componentIpAddress": componentIpAddress,
       "componentState": componentState,
       "componentStateLastChange": componentStateLastChange}
)
