# SNMP MIB module (CISCO-PSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:15 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(DomainId,
 DomainIdOrZero,
 FcNameId,
 FcNameIdOrZero,
 PortMemberList) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainId",
    "DomainIdOrZero",
    "FcNameId",
    "FcNameIdOrZero",
    "PortMemberList")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoPsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 364)
)
ciscoPsmMIB.setRevisions(
        ("2004-10-15 00:00",
         "2004-03-16 00:00",
         "2003-11-27 00:00",
         "2003-11-10 00:00",
         "2003-10-17 00:00",
         "2003-10-06 00:00",
         "2003-08-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CpsmVirtNwType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 2),
          ("vsan", 1))
    )



class CpsmPortBindDevType(Integer32, TextualConvention):
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
        *(("mac", 1),
          ("nWwn", 2),
          ("pWwn", 3),
          ("sWwn", 4),
          ("wildCard", 5))
    )



class CpsmPortBindSwPortType(Integer32, TextualConvention):
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
        *(("fwwn", 1),
          ("intfIndex", 2),
          ("swwn", 4),
          ("wildCard", 3))
    )



class CpsmDbActivate(Integer32, TextualConvention):
    status = "current"
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
        *(("activate", 1),
          ("activateWithAutoLearnOff", 2),
          ("deactivate", 5),
          ("forceActivate", 3),
          ("forceActivateWithAutoLearnOff", 4),
          ("noop", 6))
    )



class CpsmActivateResult(Integer32, TextualConvention):
    status = "current"
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
        *(("actFailAutoLearnOn", 5),
          ("actFailConflictDb", 3),
          ("actFailNullDb", 2),
          ("actFailSystemErr", 4),
          ("deactFailNoActive", 6),
          ("success", 1))
    )



class CpsmAutoLearnEnable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )



class CpsmClearStats(Integer32, TextualConvention):
    status = "current"
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



class CpsmClearAutoLearnDb(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearOnIntf", 2),
          ("clearOnVsan", 1),
          ("noop", 3))
    )



class CpsmDiffDb(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeDb", 2),
          ("configDb", 1),
          ("noop", 3))
    )



class CpsmDiffReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("conflict", 3),
          ("extra", 1),
          ("missing", 2))
    )



class CpsmStatsCounter(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CpsmViolationReasonCode(Integer32, TextualConvention):
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
        *(("domIdMismatch", 3),
          ("efmdDbMismatch", 4),
          ("noRespFromRemote", 5),
          ("noSwwn", 2),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPsmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPsmMIBNotifs = _CiscoPsmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 0)
)
_CiscoPsmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPsmMIBObjects = _CiscoPsmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1)
)
_CpsmConfiguration_ObjectIdentity = ObjectIdentity
cpsmConfiguration = _CpsmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1)
)
_CpsmPortBindTable_Object = MibTable
cpsmPortBindTable = _CpsmPortBindTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpsmPortBindTable.setStatus("current")
_CpsmPortBindEntry_Object = MibTableRow
cpsmPortBindEntry = _CpsmPortBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1)
)
cpsmPortBindEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindNwIndex"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindEntry.setStatus("current")
_CpsmPortBindNwType_Type = CpsmVirtNwType
_CpsmPortBindNwType_Object = MibTableColumn
cpsmPortBindNwType = _CpsmPortBindNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1, 1),
    _CpsmPortBindNwType_Type()
)
cpsmPortBindNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindNwType.setStatus("current")


class _CpsmPortBindNwIndex_Type(Unsigned32):
    """Custom type cpsmPortBindNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindNwIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindNwIndex_Object = MibTableColumn
cpsmPortBindNwIndex = _CpsmPortBindNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1, 2),
    _CpsmPortBindNwIndex_Type()
)
cpsmPortBindNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindNwIndex.setStatus("current")


class _CpsmPortBindIndex_Type(Unsigned32):
    """Custom type cpsmPortBindIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CpsmPortBindIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindIndex_Object = MibTableColumn
cpsmPortBindIndex = _CpsmPortBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1, 3),
    _CpsmPortBindIndex_Type()
)
cpsmPortBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindIndex.setStatus("current")


class _CpsmPortBindLoginDevType_Type(CpsmPortBindDevType):
    """Custom type cpsmPortBindLoginDevType based on CpsmPortBindDevType"""


_CpsmPortBindLoginDevType_Object = MibTableColumn
cpsmPortBindLoginDevType = _CpsmPortBindLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1, 4),
    _CpsmPortBindLoginDevType_Type()
)
cpsmPortBindLoginDevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsmPortBindLoginDevType.setStatus("current")


class _CpsmPortBindLoginDev_Type(OctetString):
    """Custom type cpsmPortBindLoginDev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_CpsmPortBindLoginDev_Type.__name__ = "OctetString"
_CpsmPortBindLoginDev_Object = MibTableColumn
cpsmPortBindLoginDev = _CpsmPortBindLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1, 5),
    _CpsmPortBindLoginDev_Type()
)
cpsmPortBindLoginDev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsmPortBindLoginDev.setStatus("current")


class _CpsmPortBindLoginPointType_Type(CpsmPortBindSwPortType):
    """Custom type cpsmPortBindLoginPointType based on CpsmPortBindSwPortType"""


_CpsmPortBindLoginPointType_Object = MibTableColumn
cpsmPortBindLoginPointType = _CpsmPortBindLoginPointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1, 6),
    _CpsmPortBindLoginPointType_Type()
)
cpsmPortBindLoginPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsmPortBindLoginPointType.setStatus("current")


class _CpsmPortBindLoginPoint_Type(OctetString):
    """Custom type cpsmPortBindLoginPoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
    )


_CpsmPortBindLoginPoint_Type.__name__ = "OctetString"
_CpsmPortBindLoginPoint_Object = MibTableColumn
cpsmPortBindLoginPoint = _CpsmPortBindLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1, 7),
    _CpsmPortBindLoginPoint_Type()
)
cpsmPortBindLoginPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsmPortBindLoginPoint.setStatus("current")
_CpsmPortBindRowStatus_Type = RowStatus
_CpsmPortBindRowStatus_Object = MibTableColumn
cpsmPortBindRowStatus = _CpsmPortBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 1, 1, 8),
    _CpsmPortBindRowStatus_Type()
)
cpsmPortBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsmPortBindRowStatus.setStatus("current")
_CpsmPortBindActivateTable_Object = MibTable
cpsmPortBindActivateTable = _CpsmPortBindActivateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpsmPortBindActivateTable.setStatus("current")
_CpsmPortBindActivateEntry_Object = MibTableRow
cpsmPortBindActivateEntry = _CpsmPortBindActivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 2, 1)
)
cpsmPortBindActivateEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindActivateEntry.setStatus("current")
_CpsmPortBindActivate_Type = CpsmDbActivate
_CpsmPortBindActivate_Object = MibTableColumn
cpsmPortBindActivate = _CpsmPortBindActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 2, 1, 1),
    _CpsmPortBindActivate_Type()
)
cpsmPortBindActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmPortBindActivate.setStatus("current")
_CpsmPortBindResult_Type = CpsmActivateResult
_CpsmPortBindResult_Object = MibTableColumn
cpsmPortBindResult = _CpsmPortBindResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 2, 1, 2),
    _CpsmPortBindResult_Type()
)
cpsmPortBindResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindResult.setStatus("current")
_CpsmPortBindLastActTime_Type = TimeStamp
_CpsmPortBindLastActTime_Object = MibTableColumn
cpsmPortBindLastActTime = _CpsmPortBindLastActTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 2, 1, 3),
    _CpsmPortBindLastActTime_Type()
)
cpsmPortBindLastActTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLastActTime.setStatus("current")
_CpsmPortBindActState_Type = TruthValue
_CpsmPortBindActState_Object = MibTableColumn
cpsmPortBindActState = _CpsmPortBindActState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 2, 1, 4),
    _CpsmPortBindActState_Type()
)
cpsmPortBindActState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindActState.setStatus("current")
_CpsmFabricBindTable_Object = MibTable
cpsmFabricBindTable = _CpsmFabricBindTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cpsmFabricBindTable.setStatus("current")
_CpsmFabricBindEntry_Object = MibTableRow
cpsmFabricBindEntry = _CpsmFabricBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 3, 1)
)
cpsmFabricBindEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindNwType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindNwIndex"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindEntry.setStatus("current")
_CpsmFabricBindNwType_Type = CpsmVirtNwType
_CpsmFabricBindNwType_Object = MibTableColumn
cpsmFabricBindNwType = _CpsmFabricBindNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 3, 1, 1),
    _CpsmFabricBindNwType_Type()
)
cpsmFabricBindNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindNwType.setStatus("current")


class _CpsmFabricBindNwIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindNwIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindNwIndex_Object = MibTableColumn
cpsmFabricBindNwIndex = _CpsmFabricBindNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 3, 1, 2),
    _CpsmFabricBindNwIndex_Type()
)
cpsmFabricBindNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindNwIndex.setStatus("current")


class _CpsmFabricBindIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CpsmFabricBindIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindIndex_Object = MibTableColumn
cpsmFabricBindIndex = _CpsmFabricBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 3, 1, 3),
    _CpsmFabricBindIndex_Type()
)
cpsmFabricBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindIndex.setStatus("current")


class _CpsmFabricBindSwitchWwn_Type(OctetString):
    """Custom type cpsmFabricBindSwitchWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CpsmFabricBindSwitchWwn_Type.__name__ = "OctetString"
_CpsmFabricBindSwitchWwn_Object = MibTableColumn
cpsmFabricBindSwitchWwn = _CpsmFabricBindSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 3, 1, 4),
    _CpsmFabricBindSwitchWwn_Type()
)
cpsmFabricBindSwitchWwn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsmFabricBindSwitchWwn.setStatus("current")
_CpsmFabricBindDomId_Type = DomainId
_CpsmFabricBindDomId_Object = MibTableColumn
cpsmFabricBindDomId = _CpsmFabricBindDomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 3, 1, 5),
    _CpsmFabricBindDomId_Type()
)
cpsmFabricBindDomId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsmFabricBindDomId.setStatus("current")
_CpsmFabricBindRowStatus_Type = RowStatus
_CpsmFabricBindRowStatus_Object = MibTableColumn
cpsmFabricBindRowStatus = _CpsmFabricBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 3, 1, 6),
    _CpsmFabricBindRowStatus_Type()
)
cpsmFabricBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsmFabricBindRowStatus.setStatus("current")
_CpsmFabricBindActivateTable_Object = MibTable
cpsmFabricBindActivateTable = _CpsmFabricBindActivateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cpsmFabricBindActivateTable.setStatus("current")
_CpsmFabricBindActivateEntry_Object = MibTableRow
cpsmFabricBindActivateEntry = _CpsmFabricBindActivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 4, 1)
)
cpsmFabricBindActivateEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindNwType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindActivateEntry.setStatus("current")
_CpsmFabricBindActivate_Type = CpsmDbActivate
_CpsmFabricBindActivate_Object = MibTableColumn
cpsmFabricBindActivate = _CpsmFabricBindActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 4, 1, 1),
    _CpsmFabricBindActivate_Type()
)
cpsmFabricBindActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmFabricBindActivate.setStatus("current")
_CpsmFabricBindResult_Type = CpsmActivateResult
_CpsmFabricBindResult_Object = MibTableColumn
cpsmFabricBindResult = _CpsmFabricBindResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 4, 1, 2),
    _CpsmFabricBindResult_Type()
)
cpsmFabricBindResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindResult.setStatus("current")
_CpsmFabricBindLastActTime_Type = TimeStamp
_CpsmFabricBindLastActTime_Object = MibTableColumn
cpsmFabricBindLastActTime = _CpsmFabricBindLastActTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 4, 1, 3),
    _CpsmFabricBindLastActTime_Type()
)
cpsmFabricBindLastActTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindLastActTime.setStatus("current")
_CpsmFabricBindActState_Type = TruthValue
_CpsmFabricBindActState_Object = MibTableColumn
cpsmFabricBindActState = _CpsmFabricBindActState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 4, 1, 4),
    _CpsmFabricBindActState_Type()
)
cpsmFabricBindActState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindActState.setStatus("current")
_CpsmPortBindCopyTable_Object = MibTable
cpsmPortBindCopyTable = _CpsmPortBindCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cpsmPortBindCopyTable.setStatus("current")
_CpsmPortBindCopyEntry_Object = MibTableRow
cpsmPortBindCopyEntry = _CpsmPortBindCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 5, 1)
)
cpsmPortBindCopyEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindCopyEntry.setStatus("current")


class _CpsmPortBindCopyActToConfig_Type(Integer32):
    """Custom type cpsmPortBindCopyActToConfig based on Integer32"""
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


_CpsmPortBindCopyActToConfig_Type.__name__ = "Integer32"
_CpsmPortBindCopyActToConfig_Object = MibTableColumn
cpsmPortBindCopyActToConfig = _CpsmPortBindCopyActToConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 5, 1, 1),
    _CpsmPortBindCopyActToConfig_Type()
)
cpsmPortBindCopyActToConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmPortBindCopyActToConfig.setStatus("current")
_CpsmPortBindLastChangeTime_Type = TimeStamp
_CpsmPortBindLastChangeTime_Object = MibTableColumn
cpsmPortBindLastChangeTime = _CpsmPortBindLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 5, 1, 2),
    _CpsmPortBindLastChangeTime_Type()
)
cpsmPortBindLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLastChangeTime.setStatus("current")
_CpsmFabricBindCopyTable_Object = MibTable
cpsmFabricBindCopyTable = _CpsmFabricBindCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cpsmFabricBindCopyTable.setStatus("current")
_CpsmFabricBindCopyEntry_Object = MibTableRow
cpsmFabricBindCopyEntry = _CpsmFabricBindCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 6, 1)
)
cpsmFabricBindCopyEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindNwType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindCopyEntry.setStatus("current")


class _CpsmFabricBindCopyActToConfig_Type(Integer32):
    """Custom type cpsmFabricBindCopyActToConfig based on Integer32"""
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


_CpsmFabricBindCopyActToConfig_Type.__name__ = "Integer32"
_CpsmFabricBindCopyActToConfig_Object = MibTableColumn
cpsmFabricBindCopyActToConfig = _CpsmFabricBindCopyActToConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 6, 1, 1),
    _CpsmFabricBindCopyActToConfig_Type()
)
cpsmFabricBindCopyActToConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmFabricBindCopyActToConfig.setStatus("current")
_CpsmFabricBindLastChangeTime_Type = TimeStamp
_CpsmFabricBindLastChangeTime_Object = MibTableColumn
cpsmFabricBindLastChangeTime = _CpsmFabricBindLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 6, 1, 2),
    _CpsmFabricBindLastChangeTime_Type()
)
cpsmFabricBindLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindLastChangeTime.setStatus("current")
_CpsmPortBindEnfTable_Object = MibTable
cpsmPortBindEnfTable = _CpsmPortBindEnfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cpsmPortBindEnfTable.setStatus("current")
_CpsmPortBindEnfEntry_Object = MibTableRow
cpsmPortBindEnfEntry = _CpsmPortBindEnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1)
)
cpsmPortBindEnfEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindEnfNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindEnfNwIndex"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindEnfIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindEnfEntry.setStatus("current")
_CpsmPortBindEnfNwType_Type = CpsmVirtNwType
_CpsmPortBindEnfNwType_Object = MibTableColumn
cpsmPortBindEnfNwType = _CpsmPortBindEnfNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1, 1),
    _CpsmPortBindEnfNwType_Type()
)
cpsmPortBindEnfNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindEnfNwType.setStatus("current")


class _CpsmPortBindEnfNwIndex_Type(Unsigned32):
    """Custom type cpsmPortBindEnfNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindEnfNwIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindEnfNwIndex_Object = MibTableColumn
cpsmPortBindEnfNwIndex = _CpsmPortBindEnfNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1, 2),
    _CpsmPortBindEnfNwIndex_Type()
)
cpsmPortBindEnfNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindEnfNwIndex.setStatus("current")


class _CpsmPortBindEnfIndex_Type(Unsigned32):
    """Custom type cpsmPortBindEnfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CpsmPortBindEnfIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindEnfIndex_Object = MibTableColumn
cpsmPortBindEnfIndex = _CpsmPortBindEnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1, 3),
    _CpsmPortBindEnfIndex_Type()
)
cpsmPortBindEnfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindEnfIndex.setStatus("current")
_CpsmPortBindEnfLoginDevType_Type = CpsmPortBindDevType
_CpsmPortBindEnfLoginDevType_Object = MibTableColumn
cpsmPortBindEnfLoginDevType = _CpsmPortBindEnfLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1, 4),
    _CpsmPortBindEnfLoginDevType_Type()
)
cpsmPortBindEnfLoginDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindEnfLoginDevType.setStatus("current")


class _CpsmPortBindEnfLoginDev_Type(OctetString):
    """Custom type cpsmPortBindEnfLoginDev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_CpsmPortBindEnfLoginDev_Type.__name__ = "OctetString"
_CpsmPortBindEnfLoginDev_Object = MibTableColumn
cpsmPortBindEnfLoginDev = _CpsmPortBindEnfLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1, 5),
    _CpsmPortBindEnfLoginDev_Type()
)
cpsmPortBindEnfLoginDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindEnfLoginDev.setStatus("current")
_CpsmPortBindEnfLoginPointType_Type = CpsmPortBindSwPortType
_CpsmPortBindEnfLoginPointType_Object = MibTableColumn
cpsmPortBindEnfLoginPointType = _CpsmPortBindEnfLoginPointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1, 6),
    _CpsmPortBindEnfLoginPointType_Type()
)
cpsmPortBindEnfLoginPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindEnfLoginPointType.setStatus("current")


class _CpsmPortBindEnfLoginPoint_Type(OctetString):
    """Custom type cpsmPortBindEnfLoginPoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
    )


_CpsmPortBindEnfLoginPoint_Type.__name__ = "OctetString"
_CpsmPortBindEnfLoginPoint_Object = MibTableColumn
cpsmPortBindEnfLoginPoint = _CpsmPortBindEnfLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1, 7),
    _CpsmPortBindEnfLoginPoint_Type()
)
cpsmPortBindEnfLoginPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindEnfLoginPoint.setStatus("current")
_CpsmPortBindEnfIsLearnt_Type = TruthValue
_CpsmPortBindEnfIsLearnt_Object = MibTableColumn
cpsmPortBindEnfIsLearnt = _CpsmPortBindEnfIsLearnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 7, 1, 8),
    _CpsmPortBindEnfIsLearnt_Type()
)
cpsmPortBindEnfIsLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindEnfIsLearnt.setStatus("current")
_CpsmFabricBindEnfTable_Object = MibTable
cpsmFabricBindEnfTable = _CpsmFabricBindEnfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cpsmFabricBindEnfTable.setStatus("current")
_CpsmFabricBindEnfEntry_Object = MibTableRow
cpsmFabricBindEnfEntry = _CpsmFabricBindEnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 8, 1)
)
cpsmFabricBindEnfEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindEnfNwType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindEnfNwIndex"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindEnfIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindEnfEntry.setStatus("current")
_CpsmFabricBindEnfNwType_Type = CpsmVirtNwType
_CpsmFabricBindEnfNwType_Object = MibTableColumn
cpsmFabricBindEnfNwType = _CpsmFabricBindEnfNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 8, 1, 1),
    _CpsmFabricBindEnfNwType_Type()
)
cpsmFabricBindEnfNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindEnfNwType.setStatus("current")


class _CpsmFabricBindEnfNwIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindEnfNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindEnfNwIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindEnfNwIndex_Object = MibTableColumn
cpsmFabricBindEnfNwIndex = _CpsmFabricBindEnfNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 8, 1, 2),
    _CpsmFabricBindEnfNwIndex_Type()
)
cpsmFabricBindEnfNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindEnfNwIndex.setStatus("current")


class _CpsmFabricBindEnfIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindEnfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CpsmFabricBindEnfIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindEnfIndex_Object = MibTableColumn
cpsmFabricBindEnfIndex = _CpsmFabricBindEnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 8, 1, 3),
    _CpsmFabricBindEnfIndex_Type()
)
cpsmFabricBindEnfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindEnfIndex.setStatus("current")


class _CpsmFabricBindEnfSwitchWwn_Type(OctetString):
    """Custom type cpsmFabricBindEnfSwitchWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CpsmFabricBindEnfSwitchWwn_Type.__name__ = "OctetString"
_CpsmFabricBindEnfSwitchWwn_Object = MibTableColumn
cpsmFabricBindEnfSwitchWwn = _CpsmFabricBindEnfSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 8, 1, 4),
    _CpsmFabricBindEnfSwitchWwn_Type()
)
cpsmFabricBindEnfSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindEnfSwitchWwn.setStatus("current")
_CpsmFabricBindEnfDomId_Type = DomainId
_CpsmFabricBindEnfDomId_Object = MibTableColumn
cpsmFabricBindEnfDomId = _CpsmFabricBindEnfDomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 8, 1, 5),
    _CpsmFabricBindEnfDomId_Type()
)
cpsmFabricBindEnfDomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindEnfDomId.setStatus("current")
_CpsmFabricBindEnfIsLearnt_Type = TruthValue
_CpsmFabricBindEnfIsLearnt_Object = MibTableColumn
cpsmFabricBindEnfIsLearnt = _CpsmFabricBindEnfIsLearnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 8, 1, 6),
    _CpsmFabricBindEnfIsLearnt_Type()
)
cpsmFabricBindEnfIsLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindEnfIsLearnt.setStatus("current")
_CpsmPortBindAutoLearnTable_Object = MibTable
cpsmPortBindAutoLearnTable = _CpsmPortBindAutoLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cpsmPortBindAutoLearnTable.setStatus("current")
_CpsmPortBindAutoLearnEntry_Object = MibTableRow
cpsmPortBindAutoLearnEntry = _CpsmPortBindAutoLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 9, 1)
)
cpsmPortBindAutoLearnEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindAutoLearnIndexType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindAutoLearnIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindAutoLearnEntry.setStatus("current")
_CpsmPortBindAutoLearnIndexType_Type = CpsmVirtNwType
_CpsmPortBindAutoLearnIndexType_Object = MibTableColumn
cpsmPortBindAutoLearnIndexType = _CpsmPortBindAutoLearnIndexType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 9, 1, 1),
    _CpsmPortBindAutoLearnIndexType_Type()
)
cpsmPortBindAutoLearnIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindAutoLearnIndexType.setStatus("current")


class _CpsmPortBindAutoLearnIndex_Type(Unsigned32):
    """Custom type cpsmPortBindAutoLearnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindAutoLearnIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindAutoLearnIndex_Object = MibTableColumn
cpsmPortBindAutoLearnIndex = _CpsmPortBindAutoLearnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 9, 1, 2),
    _CpsmPortBindAutoLearnIndex_Type()
)
cpsmPortBindAutoLearnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindAutoLearnIndex.setStatus("current")


class _CpsmPortBindAutoLearnEnable_Type(CpsmAutoLearnEnable):
    """Custom type cpsmPortBindAutoLearnEnable based on CpsmAutoLearnEnable"""


_CpsmPortBindAutoLearnEnable_Object = MibTableColumn
cpsmPortBindAutoLearnEnable = _CpsmPortBindAutoLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 9, 1, 3),
    _CpsmPortBindAutoLearnEnable_Type()
)
cpsmPortBindAutoLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmPortBindAutoLearnEnable.setStatus("current")
_CpsmFabricBindAutoLearnTable_Object = MibTable
cpsmFabricBindAutoLearnTable = _CpsmFabricBindAutoLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cpsmFabricBindAutoLearnTable.setStatus("deprecated")
_CpsmFabricBindAutoLearnEntry_Object = MibTableRow
cpsmFabricBindAutoLearnEntry = _CpsmFabricBindAutoLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 10, 1)
)
cpsmFabricBindAutoLearnEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindAutoLearnIndexType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindAutoLearnIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindAutoLearnEntry.setStatus("deprecated")
_CpsmFabricBindAutoLearnIndexType_Type = CpsmVirtNwType
_CpsmFabricBindAutoLearnIndexType_Object = MibTableColumn
cpsmFabricBindAutoLearnIndexType = _CpsmFabricBindAutoLearnIndexType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 10, 1, 1),
    _CpsmFabricBindAutoLearnIndexType_Type()
)
cpsmFabricBindAutoLearnIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindAutoLearnIndexType.setStatus("deprecated")


class _CpsmFabricBindAutoLearnIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindAutoLearnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindAutoLearnIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindAutoLearnIndex_Object = MibTableColumn
cpsmFabricBindAutoLearnIndex = _CpsmFabricBindAutoLearnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 10, 1, 2),
    _CpsmFabricBindAutoLearnIndex_Type()
)
cpsmFabricBindAutoLearnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindAutoLearnIndex.setStatus("deprecated")


class _CpsmFabricBindAutoLearnEnable_Type(CpsmAutoLearnEnable):
    """Custom type cpsmFabricBindAutoLearnEnable based on CpsmAutoLearnEnable"""


_CpsmFabricBindAutoLearnEnable_Object = MibTableColumn
cpsmFabricBindAutoLearnEnable = _CpsmFabricBindAutoLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 10, 1, 3),
    _CpsmFabricBindAutoLearnEnable_Type()
)
cpsmFabricBindAutoLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmFabricBindAutoLearnEnable.setStatus("deprecated")
_CpsmPortBindClearTable_Object = MibTable
cpsmPortBindClearTable = _CpsmPortBindClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cpsmPortBindClearTable.setStatus("current")
_CpsmPortBindClearEntry_Object = MibTableRow
cpsmPortBindClearEntry = _CpsmPortBindClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 11, 1)
)
cpsmPortBindClearEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindClearNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindClearNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindClearEntry.setStatus("current")
_CpsmPortBindClearNwType_Type = CpsmVirtNwType
_CpsmPortBindClearNwType_Object = MibTableColumn
cpsmPortBindClearNwType = _CpsmPortBindClearNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 11, 1, 1),
    _CpsmPortBindClearNwType_Type()
)
cpsmPortBindClearNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindClearNwType.setStatus("current")


class _CpsmPortBindClearNwIndex_Type(Unsigned32):
    """Custom type cpsmPortBindClearNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindClearNwIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindClearNwIndex_Object = MibTableColumn
cpsmPortBindClearNwIndex = _CpsmPortBindClearNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 11, 1, 2),
    _CpsmPortBindClearNwIndex_Type()
)
cpsmPortBindClearNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindClearNwIndex.setStatus("current")
_CpsmPortBindClearStats_Type = CpsmClearStats
_CpsmPortBindClearStats_Object = MibTableColumn
cpsmPortBindClearStats = _CpsmPortBindClearStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 11, 1, 3),
    _CpsmPortBindClearStats_Type()
)
cpsmPortBindClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmPortBindClearStats.setStatus("current")
_CpsmPortBindClearAutoLearnDb_Type = CpsmClearAutoLearnDb
_CpsmPortBindClearAutoLearnDb_Object = MibTableColumn
cpsmPortBindClearAutoLearnDb = _CpsmPortBindClearAutoLearnDb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 11, 1, 4),
    _CpsmPortBindClearAutoLearnDb_Type()
)
cpsmPortBindClearAutoLearnDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmPortBindClearAutoLearnDb.setStatus("current")


class _CpsmPortBindClearAutoLearnIntf_Type(PortMemberList):
    """Custom type cpsmPortBindClearAutoLearnIntf based on PortMemberList"""
    defaultHexValue = ""


_CpsmPortBindClearAutoLearnIntf_Object = MibTableColumn
cpsmPortBindClearAutoLearnIntf = _CpsmPortBindClearAutoLearnIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 11, 1, 5),
    _CpsmPortBindClearAutoLearnIntf_Type()
)
cpsmPortBindClearAutoLearnIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmPortBindClearAutoLearnIntf.setStatus("current")
_CpsmFabricBindClearTable_Object = MibTable
cpsmFabricBindClearTable = _CpsmFabricBindClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cpsmFabricBindClearTable.setStatus("current")
_CpsmFabricBindClearEntry_Object = MibTableRow
cpsmFabricBindClearEntry = _CpsmFabricBindClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 12, 1)
)
cpsmFabricBindClearEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindClearNwType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindClearNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindClearEntry.setStatus("current")
_CpsmFabricBindClearNwType_Type = CpsmVirtNwType
_CpsmFabricBindClearNwType_Object = MibTableColumn
cpsmFabricBindClearNwType = _CpsmFabricBindClearNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 12, 1, 1),
    _CpsmFabricBindClearNwType_Type()
)
cpsmFabricBindClearNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindClearNwType.setStatus("current")


class _CpsmFabricBindClearNwIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindClearNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindClearNwIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindClearNwIndex_Object = MibTableColumn
cpsmFabricBindClearNwIndex = _CpsmFabricBindClearNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 12, 1, 2),
    _CpsmFabricBindClearNwIndex_Type()
)
cpsmFabricBindClearNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindClearNwIndex.setStatus("current")
_CpsmFabricBindClearStats_Type = CpsmClearStats
_CpsmFabricBindClearStats_Object = MibTableColumn
cpsmFabricBindClearStats = _CpsmFabricBindClearStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 12, 1, 3),
    _CpsmFabricBindClearStats_Type()
)
cpsmFabricBindClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmFabricBindClearStats.setStatus("current")
_CpsmFabricBindClearAutoLearnDb_Type = CpsmClearAutoLearnDb
_CpsmFabricBindClearAutoLearnDb_Object = MibTableColumn
cpsmFabricBindClearAutoLearnDb = _CpsmFabricBindClearAutoLearnDb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 12, 1, 4),
    _CpsmFabricBindClearAutoLearnDb_Type()
)
cpsmFabricBindClearAutoLearnDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmFabricBindClearAutoLearnDb.setStatus("current")


class _CpsmFabricBindClearAutoLearnIntf_Type(InterfaceIndexOrZero):
    """Custom type cpsmFabricBindClearAutoLearnIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_CpsmFabricBindClearAutoLearnIntf_Object = MibTableColumn
cpsmFabricBindClearAutoLearnIntf = _CpsmFabricBindClearAutoLearnIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 12, 1, 5),
    _CpsmFabricBindClearAutoLearnIntf_Type()
)
cpsmFabricBindClearAutoLearnIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmFabricBindClearAutoLearnIntf.setStatus("deprecated")
_CpsmPortBindDiffConfigTable_Object = MibTable
cpsmPortBindDiffConfigTable = _CpsmPortBindDiffConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cpsmPortBindDiffConfigTable.setStatus("current")
_CpsmPortBindDiffConfigEntry_Object = MibTableRow
cpsmPortBindDiffConfigEntry = _CpsmPortBindDiffConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 13, 1)
)
cpsmPortBindDiffConfigEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindDiffConfigNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindDiffConfigNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindDiffConfigEntry.setStatus("current")
_CpsmPortBindDiffConfigNwType_Type = CpsmVirtNwType
_CpsmPortBindDiffConfigNwType_Object = MibTableColumn
cpsmPortBindDiffConfigNwType = _CpsmPortBindDiffConfigNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 13, 1, 1),
    _CpsmPortBindDiffConfigNwType_Type()
)
cpsmPortBindDiffConfigNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindDiffConfigNwType.setStatus("current")


class _CpsmPortBindDiffConfigNwIndex_Type(Unsigned32):
    """Custom type cpsmPortBindDiffConfigNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindDiffConfigNwIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindDiffConfigNwIndex_Object = MibTableColumn
cpsmPortBindDiffConfigNwIndex = _CpsmPortBindDiffConfigNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 13, 1, 2),
    _CpsmPortBindDiffConfigNwIndex_Type()
)
cpsmPortBindDiffConfigNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindDiffConfigNwIndex.setStatus("current")
_CpsmPortBindDiffConfigDb_Type = CpsmDiffDb
_CpsmPortBindDiffConfigDb_Object = MibTableColumn
cpsmPortBindDiffConfigDb = _CpsmPortBindDiffConfigDb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 13, 1, 3),
    _CpsmPortBindDiffConfigDb_Type()
)
cpsmPortBindDiffConfigDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmPortBindDiffConfigDb.setStatus("current")
_CpsmPortBindDiffTable_Object = MibTable
cpsmPortBindDiffTable = _CpsmPortBindDiffTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cpsmPortBindDiffTable.setStatus("current")
_CpsmPortBindDiffEntry_Object = MibTableRow
cpsmPortBindDiffEntry = _CpsmPortBindDiffEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1)
)
cpsmPortBindDiffEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindDiffNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindDiffNwIndex"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindDiffIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindDiffEntry.setStatus("current")
_CpsmPortBindDiffNwType_Type = CpsmVirtNwType
_CpsmPortBindDiffNwType_Object = MibTableColumn
cpsmPortBindDiffNwType = _CpsmPortBindDiffNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1, 1),
    _CpsmPortBindDiffNwType_Type()
)
cpsmPortBindDiffNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindDiffNwType.setStatus("current")


class _CpsmPortBindDiffNwIndex_Type(Unsigned32):
    """Custom type cpsmPortBindDiffNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindDiffNwIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindDiffNwIndex_Object = MibTableColumn
cpsmPortBindDiffNwIndex = _CpsmPortBindDiffNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1, 2),
    _CpsmPortBindDiffNwIndex_Type()
)
cpsmPortBindDiffNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindDiffNwIndex.setStatus("current")


class _CpsmPortBindDiffIndex_Type(Unsigned32):
    """Custom type cpsmPortBindDiffIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CpsmPortBindDiffIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindDiffIndex_Object = MibTableColumn
cpsmPortBindDiffIndex = _CpsmPortBindDiffIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1, 3),
    _CpsmPortBindDiffIndex_Type()
)
cpsmPortBindDiffIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindDiffIndex.setStatus("current")
_CpsmPortBindDiffReason_Type = CpsmDiffReason
_CpsmPortBindDiffReason_Object = MibTableColumn
cpsmPortBindDiffReason = _CpsmPortBindDiffReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1, 4),
    _CpsmPortBindDiffReason_Type()
)
cpsmPortBindDiffReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindDiffReason.setStatus("current")
_CpsmPortBindDiffLoginDevType_Type = CpsmPortBindDevType
_CpsmPortBindDiffLoginDevType_Object = MibTableColumn
cpsmPortBindDiffLoginDevType = _CpsmPortBindDiffLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1, 5),
    _CpsmPortBindDiffLoginDevType_Type()
)
cpsmPortBindDiffLoginDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindDiffLoginDevType.setStatus("current")


class _CpsmPortBindDiffLoginDev_Type(OctetString):
    """Custom type cpsmPortBindDiffLoginDev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_CpsmPortBindDiffLoginDev_Type.__name__ = "OctetString"
_CpsmPortBindDiffLoginDev_Object = MibTableColumn
cpsmPortBindDiffLoginDev = _CpsmPortBindDiffLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1, 6),
    _CpsmPortBindDiffLoginDev_Type()
)
cpsmPortBindDiffLoginDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindDiffLoginDev.setStatus("current")
_CpsmPortBindDiffLoginPointType_Type = CpsmPortBindSwPortType
_CpsmPortBindDiffLoginPointType_Object = MibTableColumn
cpsmPortBindDiffLoginPointType = _CpsmPortBindDiffLoginPointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1, 7),
    _CpsmPortBindDiffLoginPointType_Type()
)
cpsmPortBindDiffLoginPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindDiffLoginPointType.setStatus("current")


class _CpsmPortBindDiffLoginPoint_Type(OctetString):
    """Custom type cpsmPortBindDiffLoginPoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
    )


_CpsmPortBindDiffLoginPoint_Type.__name__ = "OctetString"
_CpsmPortBindDiffLoginPoint_Object = MibTableColumn
cpsmPortBindDiffLoginPoint = _CpsmPortBindDiffLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 14, 1, 8),
    _CpsmPortBindDiffLoginPoint_Type()
)
cpsmPortBindDiffLoginPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindDiffLoginPoint.setStatus("current")
_CpsmFabricBindDiffConfigTable_Object = MibTable
cpsmFabricBindDiffConfigTable = _CpsmFabricBindDiffConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cpsmFabricBindDiffConfigTable.setStatus("current")
_CpsmFabricBindDiffConfigEntry_Object = MibTableRow
cpsmFabricBindDiffConfigEntry = _CpsmFabricBindDiffConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 15, 1)
)
cpsmFabricBindDiffConfigEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindDiffConfigNwType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindDiffConfigNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindDiffConfigEntry.setStatus("current")
_CpsmFabricBindDiffConfigNwType_Type = CpsmVirtNwType
_CpsmFabricBindDiffConfigNwType_Object = MibTableColumn
cpsmFabricBindDiffConfigNwType = _CpsmFabricBindDiffConfigNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 15, 1, 1),
    _CpsmFabricBindDiffConfigNwType_Type()
)
cpsmFabricBindDiffConfigNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffConfigNwType.setStatus("current")


class _CpsmFabricBindDiffConfigNwIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindDiffConfigNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindDiffConfigNwIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindDiffConfigNwIndex_Object = MibTableColumn
cpsmFabricBindDiffConfigNwIndex = _CpsmFabricBindDiffConfigNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 15, 1, 2),
    _CpsmFabricBindDiffConfigNwIndex_Type()
)
cpsmFabricBindDiffConfigNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffConfigNwIndex.setStatus("current")
_CpsmFabricBindDiffConfigDb_Type = CpsmDiffDb
_CpsmFabricBindDiffConfigDb_Object = MibTableColumn
cpsmFabricBindDiffConfigDb = _CpsmFabricBindDiffConfigDb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 15, 1, 3),
    _CpsmFabricBindDiffConfigDb_Type()
)
cpsmFabricBindDiffConfigDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffConfigDb.setStatus("current")
_CpsmFabricBindDiffTable_Object = MibTable
cpsmFabricBindDiffTable = _CpsmFabricBindDiffTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cpsmFabricBindDiffTable.setStatus("current")
_CpsmFabricBindDiffEntry_Object = MibTableRow
cpsmFabricBindDiffEntry = _CpsmFabricBindDiffEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 16, 1)
)
cpsmFabricBindDiffEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindDiffNwType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindDiffNwIndex"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindDiffIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindDiffEntry.setStatus("current")
_CpsmFabricBindDiffNwType_Type = CpsmVirtNwType
_CpsmFabricBindDiffNwType_Object = MibTableColumn
cpsmFabricBindDiffNwType = _CpsmFabricBindDiffNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 16, 1, 1),
    _CpsmFabricBindDiffNwType_Type()
)
cpsmFabricBindDiffNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffNwType.setStatus("current")


class _CpsmFabricBindDiffNwIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindDiffNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindDiffNwIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindDiffNwIndex_Object = MibTableColumn
cpsmFabricBindDiffNwIndex = _CpsmFabricBindDiffNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 16, 1, 2),
    _CpsmFabricBindDiffNwIndex_Type()
)
cpsmFabricBindDiffNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffNwIndex.setStatus("current")


class _CpsmFabricBindDiffIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindDiffIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CpsmFabricBindDiffIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindDiffIndex_Object = MibTableColumn
cpsmFabricBindDiffIndex = _CpsmFabricBindDiffIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 16, 1, 3),
    _CpsmFabricBindDiffIndex_Type()
)
cpsmFabricBindDiffIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffIndex.setStatus("current")
_CpsmFabricBindDiffReason_Type = CpsmDiffReason
_CpsmFabricBindDiffReason_Object = MibTableColumn
cpsmFabricBindDiffReason = _CpsmFabricBindDiffReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 16, 1, 4),
    _CpsmFabricBindDiffReason_Type()
)
cpsmFabricBindDiffReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffReason.setStatus("current")


class _CpsmFabricBindDiffSwitchWwn_Type(OctetString):
    """Custom type cpsmFabricBindDiffSwitchWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CpsmFabricBindDiffSwitchWwn_Type.__name__ = "OctetString"
_CpsmFabricBindDiffSwitchWwn_Object = MibTableColumn
cpsmFabricBindDiffSwitchWwn = _CpsmFabricBindDiffSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 16, 1, 5),
    _CpsmFabricBindDiffSwitchWwn_Type()
)
cpsmFabricBindDiffSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffSwitchWwn.setStatus("current")
_CpsmFabricBindDiffDomId_Type = DomainId
_CpsmFabricBindDiffDomId_Object = MibTableColumn
cpsmFabricBindDiffDomId = _CpsmFabricBindDiffDomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 16, 1, 6),
    _CpsmFabricBindDiffDomId_Type()
)
cpsmFabricBindDiffDomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDiffDomId.setStatus("current")


class _CpsmNotifyEnable_Type(TruthValue):
    """Custom type cpsmNotifyEnable based on TruthValue"""


_CpsmNotifyEnable_Object = MibScalar
cpsmNotifyEnable = _CpsmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 17),
    _CpsmNotifyEnable_Type()
)
cpsmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmNotifyEnable.setStatus("current")
_CpsmEfmdConfigTable_Object = MibTable
cpsmEfmdConfigTable = _CpsmEfmdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cpsmEfmdConfigTable.setStatus("current")
_CpsmEfmdConfigEntry_Object = MibTableRow
cpsmEfmdConfigEntry = _CpsmEfmdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 18, 1)
)
cpsmEfmdConfigEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    cpsmEfmdConfigEntry.setStatus("current")


class _CpsmEfmdConfigEnforce_Type(TruthValue):
    """Custom type cpsmEfmdConfigEnforce based on TruthValue"""


_CpsmEfmdConfigEnforce_Object = MibTableColumn
cpsmEfmdConfigEnforce = _CpsmEfmdConfigEnforce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 18, 1, 1),
    _CpsmEfmdConfigEnforce_Type()
)
cpsmEfmdConfigEnforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmEfmdConfigEnforce.setStatus("current")
_CpsmPortBindNextFreeTable_Object = MibTable
cpsmPortBindNextFreeTable = _CpsmPortBindNextFreeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 19)
)
if mibBuilder.loadTexts:
    cpsmPortBindNextFreeTable.setStatus("current")
_CpsmPortBindNextFreeEntry_Object = MibTableRow
cpsmPortBindNextFreeEntry = _CpsmPortBindNextFreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 19, 1)
)
cpsmPortBindNextFreeEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindNextFreeNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindNextFreeNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindNextFreeEntry.setStatus("current")
_CpsmPortBindNextFreeNwType_Type = CpsmVirtNwType
_CpsmPortBindNextFreeNwType_Object = MibTableColumn
cpsmPortBindNextFreeNwType = _CpsmPortBindNextFreeNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 19, 1, 1),
    _CpsmPortBindNextFreeNwType_Type()
)
cpsmPortBindNextFreeNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindNextFreeNwType.setStatus("current")


class _CpsmPortBindNextFreeNwIndex_Type(Unsigned32):
    """Custom type cpsmPortBindNextFreeNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindNextFreeNwIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindNextFreeNwIndex_Object = MibTableColumn
cpsmPortBindNextFreeNwIndex = _CpsmPortBindNextFreeNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 19, 1, 2),
    _CpsmPortBindNextFreeNwIndex_Type()
)
cpsmPortBindNextFreeNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindNextFreeNwIndex.setStatus("current")


class _CpsmPortBindNextFreeIndex_Type(Unsigned32):
    """Custom type cpsmPortBindNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CpsmPortBindNextFreeIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindNextFreeIndex_Object = MibTableColumn
cpsmPortBindNextFreeIndex = _CpsmPortBindNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 19, 1, 3),
    _CpsmPortBindNextFreeIndex_Type()
)
cpsmPortBindNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindNextFreeIndex.setStatus("current")
_CpsmFabricBindNextFreeTable_Object = MibTable
cpsmFabricBindNextFreeTable = _CpsmFabricBindNextFreeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 20)
)
if mibBuilder.loadTexts:
    cpsmFabricBindNextFreeTable.setStatus("current")
_CpsmFabricBindNextFreeEntry_Object = MibTableRow
cpsmFabricBindNextFreeEntry = _CpsmFabricBindNextFreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 20, 1)
)
cpsmFabricBindNextFreeEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindNextFreeNwType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindNextFreeNwIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindNextFreeEntry.setStatus("current")
_CpsmFabricBindNextFreeNwType_Type = CpsmVirtNwType
_CpsmFabricBindNextFreeNwType_Object = MibTableColumn
cpsmFabricBindNextFreeNwType = _CpsmFabricBindNextFreeNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 20, 1, 1),
    _CpsmFabricBindNextFreeNwType_Type()
)
cpsmFabricBindNextFreeNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindNextFreeNwType.setStatus("current")


class _CpsmFabricBindNextFreeNwIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindNextFreeNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindNextFreeNwIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindNextFreeNwIndex_Object = MibTableColumn
cpsmFabricBindNextFreeNwIndex = _CpsmFabricBindNextFreeNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 20, 1, 2),
    _CpsmFabricBindNextFreeNwIndex_Type()
)
cpsmFabricBindNextFreeNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindNextFreeNwIndex.setStatus("current")


class _CpsmFabricBindNextFreeIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CpsmFabricBindNextFreeIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindNextFreeIndex_Object = MibTableColumn
cpsmFabricBindNextFreeIndex = _CpsmFabricBindNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 1, 20, 1, 3),
    _CpsmFabricBindNextFreeIndex_Type()
)
cpsmFabricBindNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindNextFreeIndex.setStatus("current")
_CpsmStats_ObjectIdentity = ObjectIdentity
cpsmStats = _CpsmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2)
)
_CpsmPortBindStatsTable_Object = MibTable
cpsmPortBindStatsTable = _CpsmPortBindStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpsmPortBindStatsTable.setStatus("current")
_CpsmPortBindStatsEntry_Object = MibTableRow
cpsmPortBindStatsEntry = _CpsmPortBindStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 1, 1)
)
cpsmPortBindStatsEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindVsanVlanType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindVsanVlanIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindStatsEntry.setStatus("current")
_CpsmPortBindVsanVlanType_Type = CpsmVirtNwType
_CpsmPortBindVsanVlanType_Object = MibTableColumn
cpsmPortBindVsanVlanType = _CpsmPortBindVsanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 1, 1, 1),
    _CpsmPortBindVsanVlanType_Type()
)
cpsmPortBindVsanVlanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindVsanVlanType.setStatus("current")


class _CpsmPortBindVsanVlanIndex_Type(Unsigned32):
    """Custom type cpsmPortBindVsanVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindVsanVlanIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindVsanVlanIndex_Object = MibTableColumn
cpsmPortBindVsanVlanIndex = _CpsmPortBindVsanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 1, 1, 2),
    _CpsmPortBindVsanVlanIndex_Type()
)
cpsmPortBindVsanVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindVsanVlanIndex.setStatus("current")
_CpsmPortBindAllowedLogins_Type = CpsmStatsCounter
_CpsmPortBindAllowedLogins_Object = MibTableColumn
cpsmPortBindAllowedLogins = _CpsmPortBindAllowedLogins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 1, 1, 3),
    _CpsmPortBindAllowedLogins_Type()
)
cpsmPortBindAllowedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindAllowedLogins.setStatus("current")
_CpsmPortBindDeniedLogins_Type = CpsmStatsCounter
_CpsmPortBindDeniedLogins_Object = MibTableColumn
cpsmPortBindDeniedLogins = _CpsmPortBindDeniedLogins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 1, 1, 4),
    _CpsmPortBindDeniedLogins_Type()
)
cpsmPortBindDeniedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindDeniedLogins.setStatus("current")
_CpsmFabricBindStatsTable_Object = MibTable
cpsmFabricBindStatsTable = _CpsmFabricBindStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpsmFabricBindStatsTable.setStatus("current")
_CpsmFabricBindStatsEntry_Object = MibTableRow
cpsmFabricBindStatsEntry = _CpsmFabricBindStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 2, 1)
)
cpsmFabricBindStatsEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindVsanVlanType"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindVsanVlanIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindStatsEntry.setStatus("current")
_CpsmFabricBindVsanVlanType_Type = CpsmVirtNwType
_CpsmFabricBindVsanVlanType_Object = MibTableColumn
cpsmFabricBindVsanVlanType = _CpsmFabricBindVsanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 2, 1, 1),
    _CpsmFabricBindVsanVlanType_Type()
)
cpsmFabricBindVsanVlanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindVsanVlanType.setStatus("current")


class _CpsmFabricBindVsanVlanIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindVsanVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindVsanVlanIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindVsanVlanIndex_Object = MibTableColumn
cpsmFabricBindVsanVlanIndex = _CpsmFabricBindVsanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 2, 1, 2),
    _CpsmFabricBindVsanVlanIndex_Type()
)
cpsmFabricBindVsanVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindVsanVlanIndex.setStatus("current")
_CpsmFabricBindAllowedReqs_Type = CpsmStatsCounter
_CpsmFabricBindAllowedReqs_Object = MibTableColumn
cpsmFabricBindAllowedReqs = _CpsmFabricBindAllowedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 2, 1, 3),
    _CpsmFabricBindAllowedReqs_Type()
)
cpsmFabricBindAllowedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindAllowedReqs.setStatus("current")
_CpsmFabricBindDeniedReqs_Type = CpsmStatsCounter
_CpsmFabricBindDeniedReqs_Object = MibTableColumn
cpsmFabricBindDeniedReqs = _CpsmFabricBindDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 2, 1, 4),
    _CpsmFabricBindDeniedReqs_Type()
)
cpsmFabricBindDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDeniedReqs.setStatus("current")
_CpsmPortBindViolationTable_Object = MibTable
cpsmPortBindViolationTable = _CpsmPortBindViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cpsmPortBindViolationTable.setStatus("current")
_CpsmPortBindViolationEntry_Object = MibTableRow
cpsmPortBindViolationEntry = _CpsmPortBindViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1)
)
cpsmPortBindViolationEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmPortBindViolationNwType"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindViolationNwIndex"),
    (0, "CISCO-PSM-MIB", "cpsmPortBindViolationIndex"),
)
if mibBuilder.loadTexts:
    cpsmPortBindViolationEntry.setStatus("current")
_CpsmPortBindViolationNwType_Type = CpsmVirtNwType
_CpsmPortBindViolationNwType_Object = MibTableColumn
cpsmPortBindViolationNwType = _CpsmPortBindViolationNwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 1),
    _CpsmPortBindViolationNwType_Type()
)
cpsmPortBindViolationNwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindViolationNwType.setStatus("current")


class _CpsmPortBindViolationNwIndex_Type(Unsigned32):
    """Custom type cpsmPortBindViolationNwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmPortBindViolationNwIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindViolationNwIndex_Object = MibTableColumn
cpsmPortBindViolationNwIndex = _CpsmPortBindViolationNwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 2),
    _CpsmPortBindViolationNwIndex_Type()
)
cpsmPortBindViolationNwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindViolationNwIndex.setStatus("current")


class _CpsmPortBindViolationIndex_Type(Unsigned32):
    """Custom type cpsmPortBindViolationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpsmPortBindViolationIndex_Type.__name__ = "Unsigned32"
_CpsmPortBindViolationIndex_Object = MibTableColumn
cpsmPortBindViolationIndex = _CpsmPortBindViolationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 3),
    _CpsmPortBindViolationIndex_Type()
)
cpsmPortBindViolationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmPortBindViolationIndex.setStatus("current")
_CpsmPortBindLoginPwwn_Type = FcNameIdOrZero
_CpsmPortBindLoginPwwn_Object = MibTableColumn
cpsmPortBindLoginPwwn = _CpsmPortBindLoginPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 4),
    _CpsmPortBindLoginPwwn_Type()
)
cpsmPortBindLoginPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLoginPwwn.setStatus("current")
_CpsmPortBindLoginNwwn_Type = FcNameIdOrZero
_CpsmPortBindLoginNwwn_Object = MibTableColumn
cpsmPortBindLoginNwwn = _CpsmPortBindLoginNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 5),
    _CpsmPortBindLoginNwwn_Type()
)
cpsmPortBindLoginNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLoginNwwn.setStatus("current")
_CpsmPortBindLoginSwwn_Type = FcNameIdOrZero
_CpsmPortBindLoginSwwn_Object = MibTableColumn
cpsmPortBindLoginSwwn = _CpsmPortBindLoginSwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 6),
    _CpsmPortBindLoginSwwn_Type()
)
cpsmPortBindLoginSwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLoginSwwn.setStatus("current")
_CpsmPortBindLoginPort_Type = FcNameId
_CpsmPortBindLoginPort_Object = MibTableColumn
cpsmPortBindLoginPort = _CpsmPortBindLoginPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 7),
    _CpsmPortBindLoginPort_Type()
)
cpsmPortBindLoginPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLoginPort.setStatus("current")
_CpsmPortBindLoginTime_Type = TimeStamp
_CpsmPortBindLoginTime_Object = MibTableColumn
cpsmPortBindLoginTime = _CpsmPortBindLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 8),
    _CpsmPortBindLoginTime_Type()
)
cpsmPortBindLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLoginTime.setStatus("current")
_CpsmPortBindLoginCount_Type = Counter32
_CpsmPortBindLoginCount_Object = MibTableColumn
cpsmPortBindLoginCount = _CpsmPortBindLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 9),
    _CpsmPortBindLoginCount_Type()
)
cpsmPortBindLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLoginCount.setStatus("current")
_CpsmPortBindLoginIntf_Type = InterfaceIndex
_CpsmPortBindLoginIntf_Object = MibTableColumn
cpsmPortBindLoginIntf = _CpsmPortBindLoginIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 3, 1, 10),
    _CpsmPortBindLoginIntf_Type()
)
cpsmPortBindLoginIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmPortBindLoginIntf.setStatus("current")
_CpsmFabricBindViolationTable_Object = MibTable
cpsmFabricBindViolationTable = _CpsmFabricBindViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cpsmFabricBindViolationTable.setStatus("deprecated")
_CpsmFabricBindViolationEntry_Object = MibTableRow
cpsmFabricBindViolationEntry = _CpsmFabricBindViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 4, 1)
)
cpsmFabricBindViolationEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindViolationIndex"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindViolationEntry.setStatus("deprecated")


class _CpsmFabricBindViolationIndex_Type(Unsigned32):
    """Custom type cpsmFabricBindViolationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpsmFabricBindViolationIndex_Type.__name__ = "Unsigned32"
_CpsmFabricBindViolationIndex_Object = MibTableColumn
cpsmFabricBindViolationIndex = _CpsmFabricBindViolationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 4, 1, 1),
    _CpsmFabricBindViolationIndex_Type()
)
cpsmFabricBindViolationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindViolationIndex.setStatus("deprecated")
_CpsmFabricBindSwwn_Type = FcNameId
_CpsmFabricBindSwwn_Object = MibTableColumn
cpsmFabricBindSwwn = _CpsmFabricBindSwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 4, 1, 2),
    _CpsmFabricBindSwwn_Type()
)
cpsmFabricBindSwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindSwwn.setStatus("deprecated")
_CpsmFabricBindLocalPort_Type = FcNameId
_CpsmFabricBindLocalPort_Object = MibTableColumn
cpsmFabricBindLocalPort = _CpsmFabricBindLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 4, 1, 3),
    _CpsmFabricBindLocalPort_Type()
)
cpsmFabricBindLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindLocalPort.setStatus("deprecated")
_CpsmFabricBindDenialTime_Type = TimeStamp
_CpsmFabricBindDenialTime_Object = MibTableColumn
cpsmFabricBindDenialTime = _CpsmFabricBindDenialTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 4, 1, 4),
    _CpsmFabricBindDenialTime_Type()
)
cpsmFabricBindDenialTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDenialTime.setStatus("deprecated")
_CpsmFabricBindLocalIntf_Type = InterfaceIndex
_CpsmFabricBindLocalIntf_Object = MibTableColumn
cpsmFabricBindLocalIntf = _CpsmFabricBindLocalIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 4, 1, 5),
    _CpsmFabricBindLocalIntf_Type()
)
cpsmFabricBindLocalIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindLocalIntf.setStatus("deprecated")
_CpsmFabricBindViolationNewTable_Object = MibTable
cpsmFabricBindViolationNewTable = _CpsmFabricBindViolationNewTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cpsmFabricBindViolationNewTable.setStatus("current")
_CpsmFabricBindViolationNewEntry_Object = MibTableRow
cpsmFabricBindViolationNewEntry = _CpsmFabricBindViolationNewEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1)
)
cpsmFabricBindViolationNewEntry.setIndexNames(
    (0, "CISCO-PSM-MIB", "cpsmFabricBindViolationNwTypeR1"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindViolationNwIndexR1"),
    (0, "CISCO-PSM-MIB", "cpsmFabricBindViolationIndexR1"),
)
if mibBuilder.loadTexts:
    cpsmFabricBindViolationNewEntry.setStatus("current")
_CpsmFabricBindViolationNwTypeR1_Type = CpsmVirtNwType
_CpsmFabricBindViolationNwTypeR1_Object = MibTableColumn
cpsmFabricBindViolationNwTypeR1 = _CpsmFabricBindViolationNwTypeR1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1, 1),
    _CpsmFabricBindViolationNwTypeR1_Type()
)
cpsmFabricBindViolationNwTypeR1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindViolationNwTypeR1.setStatus("current")


class _CpsmFabricBindViolationNwIndexR1_Type(Unsigned32):
    """Custom type cpsmFabricBindViolationNwIndexR1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_CpsmFabricBindViolationNwIndexR1_Type.__name__ = "Unsigned32"
_CpsmFabricBindViolationNwIndexR1_Object = MibTableColumn
cpsmFabricBindViolationNwIndexR1 = _CpsmFabricBindViolationNwIndexR1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1, 2),
    _CpsmFabricBindViolationNwIndexR1_Type()
)
cpsmFabricBindViolationNwIndexR1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindViolationNwIndexR1.setStatus("current")


class _CpsmFabricBindViolationIndexR1_Type(Unsigned32):
    """Custom type cpsmFabricBindViolationIndexR1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpsmFabricBindViolationIndexR1_Type.__name__ = "Unsigned32"
_CpsmFabricBindViolationIndexR1_Object = MibTableColumn
cpsmFabricBindViolationIndexR1 = _CpsmFabricBindViolationIndexR1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1, 3),
    _CpsmFabricBindViolationIndexR1_Type()
)
cpsmFabricBindViolationIndexR1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsmFabricBindViolationIndexR1.setStatus("current")
_CpsmFabricBindSwwnR1_Type = FcNameId
_CpsmFabricBindSwwnR1_Object = MibTableColumn
cpsmFabricBindSwwnR1 = _CpsmFabricBindSwwnR1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1, 4),
    _CpsmFabricBindSwwnR1_Type()
)
cpsmFabricBindSwwnR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindSwwnR1.setStatus("current")
_CpsmFabricBindDenialTimeR1_Type = TimeStamp
_CpsmFabricBindDenialTimeR1_Object = MibTableColumn
cpsmFabricBindDenialTimeR1 = _CpsmFabricBindDenialTimeR1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1, 5),
    _CpsmFabricBindDenialTimeR1_Type()
)
cpsmFabricBindDenialTimeR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDenialTimeR1.setStatus("current")
_CpsmFabricBindDenialCountR1_Type = Counter32
_CpsmFabricBindDenialCountR1_Object = MibTableColumn
cpsmFabricBindDenialCountR1 = _CpsmFabricBindDenialCountR1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1, 6),
    _CpsmFabricBindDenialCountR1_Type()
)
cpsmFabricBindDenialCountR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDenialCountR1.setStatus("current")
_CpsmFabricBindDenialDomId_Type = DomainIdOrZero
_CpsmFabricBindDenialDomId_Object = MibTableColumn
cpsmFabricBindDenialDomId = _CpsmFabricBindDenialDomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1, 7),
    _CpsmFabricBindDenialDomId_Type()
)
cpsmFabricBindDenialDomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDenialDomId.setStatus("current")
_CpsmFabricBindDenialReasonCode_Type = CpsmViolationReasonCode
_CpsmFabricBindDenialReasonCode_Object = MibTableColumn
cpsmFabricBindDenialReasonCode = _CpsmFabricBindDenialReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 5, 1, 8),
    _CpsmFabricBindDenialReasonCode_Type()
)
cpsmFabricBindDenialReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmFabricBindDenialReasonCode.setStatus("current")
_CpsmEfmdStatsTable_Object = MibTable
cpsmEfmdStatsTable = _CpsmEfmdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cpsmEfmdStatsTable.setStatus("current")
_CpsmEfmdStatsEntry_Object = MibTableRow
cpsmEfmdStatsEntry = _CpsmEfmdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1)
)
cpsmEfmdStatsEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    cpsmEfmdStatsEntry.setStatus("current")
_CpsmEfmdTxMergeReqs_Type = Counter32
_CpsmEfmdTxMergeReqs_Object = MibTableColumn
cpsmEfmdTxMergeReqs = _CpsmEfmdTxMergeReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 1),
    _CpsmEfmdTxMergeReqs_Type()
)
cpsmEfmdTxMergeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdTxMergeReqs.setStatus("current")
_CpsmEfmdRxMergeReqs_Type = Counter32
_CpsmEfmdRxMergeReqs_Object = MibTableColumn
cpsmEfmdRxMergeReqs = _CpsmEfmdRxMergeReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 2),
    _CpsmEfmdRxMergeReqs_Type()
)
cpsmEfmdRxMergeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdRxMergeReqs.setStatus("current")
_CpsmEfmdTxMergeAccs_Type = Counter32
_CpsmEfmdTxMergeAccs_Object = MibTableColumn
cpsmEfmdTxMergeAccs = _CpsmEfmdTxMergeAccs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 3),
    _CpsmEfmdTxMergeAccs_Type()
)
cpsmEfmdTxMergeAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdTxMergeAccs.setStatus("current")
_CpsmEfmdRxMergeAccs_Type = Counter32
_CpsmEfmdRxMergeAccs_Object = MibTableColumn
cpsmEfmdRxMergeAccs = _CpsmEfmdRxMergeAccs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 4),
    _CpsmEfmdRxMergeAccs_Type()
)
cpsmEfmdRxMergeAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdRxMergeAccs.setStatus("current")
_CpsmEfmdTxMergeRejs_Type = Counter32
_CpsmEfmdTxMergeRejs_Object = MibTableColumn
cpsmEfmdTxMergeRejs = _CpsmEfmdTxMergeRejs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 5),
    _CpsmEfmdTxMergeRejs_Type()
)
cpsmEfmdTxMergeRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdTxMergeRejs.setStatus("current")
_CpsmEfmdRxMergeRejs_Type = Counter32
_CpsmEfmdRxMergeRejs_Object = MibTableColumn
cpsmEfmdRxMergeRejs = _CpsmEfmdRxMergeRejs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 6),
    _CpsmEfmdRxMergeRejs_Type()
)
cpsmEfmdRxMergeRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdRxMergeRejs.setStatus("current")
_CpsmEfmdTxMergeBusys_Type = Counter32
_CpsmEfmdTxMergeBusys_Object = MibTableColumn
cpsmEfmdTxMergeBusys = _CpsmEfmdTxMergeBusys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 7),
    _CpsmEfmdTxMergeBusys_Type()
)
cpsmEfmdTxMergeBusys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdTxMergeBusys.setStatus("current")
_CpsmEfmdRxMergeBusys_Type = Counter32
_CpsmEfmdRxMergeBusys_Object = MibTableColumn
cpsmEfmdRxMergeBusys = _CpsmEfmdRxMergeBusys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 8),
    _CpsmEfmdRxMergeBusys_Type()
)
cpsmEfmdRxMergeBusys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdRxMergeBusys.setStatus("current")
_CpsmEfmdTxMergeErrs_Type = Counter32
_CpsmEfmdTxMergeErrs_Object = MibTableColumn
cpsmEfmdTxMergeErrs = _CpsmEfmdTxMergeErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 9),
    _CpsmEfmdTxMergeErrs_Type()
)
cpsmEfmdTxMergeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdTxMergeErrs.setStatus("current")
_CpsmEfmdRxMergeErrs_Type = Counter32
_CpsmEfmdRxMergeErrs_Object = MibTableColumn
cpsmEfmdRxMergeErrs = _CpsmEfmdRxMergeErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 1, 2, 6, 1, 10),
    _CpsmEfmdRxMergeErrs_Type()
)
cpsmEfmdRxMergeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmEfmdRxMergeErrs.setStatus("current")
_CiscoPsmMIBConform_ObjectIdentity = ObjectIdentity
ciscoPsmMIBConform = _CiscoPsmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2)
)
_CiscoPsmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPsmMIBCompliances = _CiscoPsmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 1)
)
_CiscoPsmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPsmMIBGroups = _CiscoPsmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2)
)

# Managed Objects groups

ciscoPsmPortBindConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 1)
)
ciscoPsmPortBindConfigGroup.setObjects(
      *(("CISCO-PSM-MIB", "cpsmPortBindLoginDevType"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginDev"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginPointType"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginPoint"),
        ("CISCO-PSM-MIB", "cpsmPortBindRowStatus"),
        ("CISCO-PSM-MIB", "cpsmPortBindActivate"),
        ("CISCO-PSM-MIB", "cpsmPortBindResult"),
        ("CISCO-PSM-MIB", "cpsmPortBindLastActTime"),
        ("CISCO-PSM-MIB", "cpsmPortBindActState"),
        ("CISCO-PSM-MIB", "cpsmPortBindCopyActToConfig"),
        ("CISCO-PSM-MIB", "cpsmPortBindLastChangeTime"),
        ("CISCO-PSM-MIB", "cpsmPortBindClearStats"),
        ("CISCO-PSM-MIB", "cpsmPortBindClearAutoLearnDb"),
        ("CISCO-PSM-MIB", "cpsmPortBindClearAutoLearnIntf"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffConfigDb"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffReason"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffLoginDevType"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffLoginDev"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffLoginPointType"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffLoginPoint"))
)
if mibBuilder.loadTexts:
    ciscoPsmPortBindConfigGroup.setStatus("deprecated")

ciscoPsmFabricBindConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 2)
)
ciscoPsmFabricBindConfigGroup.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindSwitchWwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDomId"),
        ("CISCO-PSM-MIB", "cpsmFabricBindRowStatus"),
        ("CISCO-PSM-MIB", "cpsmFabricBindActivate"),
        ("CISCO-PSM-MIB", "cpsmFabricBindResult"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLastActTime"),
        ("CISCO-PSM-MIB", "cpsmFabricBindActState"),
        ("CISCO-PSM-MIB", "cpsmFabricBindCopyActToConfig"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLastChangeTime"),
        ("CISCO-PSM-MIB", "cpsmFabricBindClearStats"),
        ("CISCO-PSM-MIB", "cpsmFabricBindClearAutoLearnDb"),
        ("CISCO-PSM-MIB", "cpsmFabricBindClearAutoLearnIntf"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffConfigDb"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffReason"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffSwitchWwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffDomId"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindConfigGroup.setStatus("deprecated")

ciscoPsmPortBindEnforcedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 3)
)
ciscoPsmPortBindEnforcedGroup.setObjects(
      *(("CISCO-PSM-MIB", "cpsmPortBindEnfLoginDevType"),
        ("CISCO-PSM-MIB", "cpsmPortBindEnfLoginDev"),
        ("CISCO-PSM-MIB", "cpsmPortBindEnfLoginPointType"),
        ("CISCO-PSM-MIB", "cpsmPortBindEnfLoginPoint"),
        ("CISCO-PSM-MIB", "cpsmPortBindEnfIsLearnt"))
)
if mibBuilder.loadTexts:
    ciscoPsmPortBindEnforcedGroup.setStatus("current")

ciscoPsmFabricBindEnforcedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 4)
)
ciscoPsmFabricBindEnforcedGroup.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindEnfSwitchWwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindEnfDomId"),
        ("CISCO-PSM-MIB", "cpsmFabricBindEnfIsLearnt"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindEnforcedGroup.setStatus("current")

ciscoPsmPortBindStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 5)
)
ciscoPsmPortBindStatsGroup.setObjects(
      *(("CISCO-PSM-MIB", "cpsmPortBindAllowedLogins"),
        ("CISCO-PSM-MIB", "cpsmPortBindDeniedLogins"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginPwwn"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginNwwn"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginSwwn"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginPort"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginTime"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginCount"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginIntf"))
)
if mibBuilder.loadTexts:
    ciscoPsmPortBindStatsGroup.setStatus("current")

ciscoPsmFabricBindStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 6)
)
ciscoPsmFabricBindStatsGroup.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindAllowedReqs"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDeniedReqs"),
        ("CISCO-PSM-MIB", "cpsmFabricBindSwwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLocalPort"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialTime"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLocalIntf"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindStatsGroup.setStatus("deprecated")

ciscoPsmPortBindAutoLearnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 9)
)
ciscoPsmPortBindAutoLearnGroup.setObjects(
    ("CISCO-PSM-MIB", "cpsmPortBindAutoLearnEnable")
)
if mibBuilder.loadTexts:
    ciscoPsmPortBindAutoLearnGroup.setStatus("current")

ciscoPsmFabricBindAutoLearnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 10)
)
ciscoPsmFabricBindAutoLearnGroup.setObjects(
    ("CISCO-PSM-MIB", "cpsmFabricBindAutoLearnEnable")
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindAutoLearnGroup.setStatus("deprecated")

ciscoPsmNotifyEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 11)
)
ciscoPsmNotifyEnableGroup.setObjects(
    ("CISCO-PSM-MIB", "cpsmNotifyEnable")
)
if mibBuilder.loadTexts:
    ciscoPsmNotifyEnableGroup.setStatus("current")

ciscoPsmFabricBindConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 12)
)
ciscoPsmFabricBindConfigGroup1.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindSwitchWwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDomId"),
        ("CISCO-PSM-MIB", "cpsmFabricBindRowStatus"),
        ("CISCO-PSM-MIB", "cpsmFabricBindActivate"),
        ("CISCO-PSM-MIB", "cpsmFabricBindResult"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLastActTime"),
        ("CISCO-PSM-MIB", "cpsmFabricBindActState"),
        ("CISCO-PSM-MIB", "cpsmFabricBindCopyActToConfig"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLastChangeTime"),
        ("CISCO-PSM-MIB", "cpsmFabricBindClearStats"),
        ("CISCO-PSM-MIB", "cpsmFabricBindClearAutoLearnDb"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffConfigDb"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffReason"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffSwitchWwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffDomId"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindConfigGroup1.setStatus("deprecated")

ciscoPsmFabricBindStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 13)
)
ciscoPsmFabricBindStatsGroup1.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindAllowedReqs"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDeniedReqs"),
        ("CISCO-PSM-MIB", "cpsmFabricBindSwwnR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialTimeR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialCountR1"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindStatsGroup1.setStatus("deprecated")

ciscoPsmEfmdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 15)
)
ciscoPsmEfmdConfigGroup.setObjects(
    ("CISCO-PSM-MIB", "cpsmEfmdConfigEnforce")
)
if mibBuilder.loadTexts:
    ciscoPsmEfmdConfigGroup.setStatus("current")

ciscoPsmEfmdStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 16)
)
ciscoPsmEfmdStatsGroup.setObjects(
      *(("CISCO-PSM-MIB", "cpsmEfmdTxMergeReqs"),
        ("CISCO-PSM-MIB", "cpsmEfmdRxMergeReqs"),
        ("CISCO-PSM-MIB", "cpsmEfmdTxMergeAccs"),
        ("CISCO-PSM-MIB", "cpsmEfmdRxMergeAccs"),
        ("CISCO-PSM-MIB", "cpsmEfmdTxMergeRejs"),
        ("CISCO-PSM-MIB", "cpsmEfmdRxMergeRejs"),
        ("CISCO-PSM-MIB", "cpsmEfmdTxMergeBusys"),
        ("CISCO-PSM-MIB", "cpsmEfmdRxMergeBusys"),
        ("CISCO-PSM-MIB", "cpsmEfmdTxMergeErrs"),
        ("CISCO-PSM-MIB", "cpsmEfmdRxMergeErrs"))
)
if mibBuilder.loadTexts:
    ciscoPsmEfmdStatsGroup.setStatus("current")

ciscoPsmFabricBindStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 17)
)
ciscoPsmFabricBindStatsGroup2.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindAllowedReqs"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDeniedReqs"),
        ("CISCO-PSM-MIB", "cpsmFabricBindSwwnR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialTimeR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialCountR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialDomId"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindStatsGroup2.setStatus("deprecated")

ciscoPsmFabricBindStatsGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 18)
)
ciscoPsmFabricBindStatsGroup3.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindAllowedReqs"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDeniedReqs"),
        ("CISCO-PSM-MIB", "cpsmFabricBindSwwnR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialTimeR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialCountR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialDomId"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindStatsGroup3.setStatus("current")

ciscoPsmPortBindConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 19)
)
ciscoPsmPortBindConfigGroup1.setObjects(
      *(("CISCO-PSM-MIB", "cpsmPortBindLoginDevType"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginDev"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginPointType"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginPoint"),
        ("CISCO-PSM-MIB", "cpsmPortBindRowStatus"),
        ("CISCO-PSM-MIB", "cpsmPortBindActivate"),
        ("CISCO-PSM-MIB", "cpsmPortBindResult"),
        ("CISCO-PSM-MIB", "cpsmPortBindLastActTime"),
        ("CISCO-PSM-MIB", "cpsmPortBindActState"),
        ("CISCO-PSM-MIB", "cpsmPortBindCopyActToConfig"),
        ("CISCO-PSM-MIB", "cpsmPortBindLastChangeTime"),
        ("CISCO-PSM-MIB", "cpsmPortBindClearStats"),
        ("CISCO-PSM-MIB", "cpsmPortBindClearAutoLearnDb"),
        ("CISCO-PSM-MIB", "cpsmPortBindClearAutoLearnIntf"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffConfigDb"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffReason"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffLoginDevType"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffLoginDev"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffLoginPointType"),
        ("CISCO-PSM-MIB", "cpsmPortBindDiffLoginPoint"),
        ("CISCO-PSM-MIB", "cpsmPortBindNextFreeIndex"))
)
if mibBuilder.loadTexts:
    ciscoPsmPortBindConfigGroup1.setStatus("current")

ciscoPsmFabricBindConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 20)
)
ciscoPsmFabricBindConfigGroup2.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindSwitchWwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDomId"),
        ("CISCO-PSM-MIB", "cpsmFabricBindRowStatus"),
        ("CISCO-PSM-MIB", "cpsmFabricBindActivate"),
        ("CISCO-PSM-MIB", "cpsmFabricBindResult"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLastActTime"),
        ("CISCO-PSM-MIB", "cpsmFabricBindActState"),
        ("CISCO-PSM-MIB", "cpsmFabricBindCopyActToConfig"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLastChangeTime"),
        ("CISCO-PSM-MIB", "cpsmFabricBindClearStats"),
        ("CISCO-PSM-MIB", "cpsmFabricBindClearAutoLearnDb"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffConfigDb"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffReason"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffSwitchWwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDiffDomId"),
        ("CISCO-PSM-MIB", "cpsmFabricBindNextFreeIndex"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindConfigGroup2.setStatus("current")


# Notification objects

ciscoPsmPortBindFPortDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 0, 1)
)
ciscoPsmPortBindFPortDenyNotify.setObjects(
      *(("CISCO-PSM-MIB", "cpsmPortBindLoginPwwn"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginPort"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginTime"))
)
if mibBuilder.loadTexts:
    ciscoPsmPortBindFPortDenyNotify.setStatus(
        "current"
    )

ciscoPsmPortBindEPortDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 0, 2)
)
ciscoPsmPortBindEPortDenyNotify.setObjects(
      *(("CISCO-PSM-MIB", "cpsmPortBindLoginSwwn"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginPort"),
        ("CISCO-PSM-MIB", "cpsmPortBindLoginTime"))
)
if mibBuilder.loadTexts:
    ciscoPsmPortBindEPortDenyNotify.setStatus(
        "current"
    )

ciscoPsmFabricBindDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 0, 3)
)
ciscoPsmFabricBindDenyNotify.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindSwwn"),
        ("CISCO-PSM-MIB", "cpsmFabricBindLocalPort"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialTime"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindDenyNotify.setStatus(
        "deprecated"
    )

ciscoPsmFabricBindDenyNotifyNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 0, 4)
)
ciscoPsmFabricBindDenyNotifyNew.setObjects(
      *(("CISCO-PSM-MIB", "cpsmFabricBindSwwnR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialTimeR1"),
        ("CISCO-PSM-MIB", "cpsmFabricBindDenialReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindDenyNotifyNew.setStatus(
        "current"
    )


# Notifications groups

ciscoPsmPortBindNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 7)
)
ciscoPsmPortBindNotifyGroup.setObjects(
      *(("CISCO-PSM-MIB", "ciscoPsmPortBindFPortDenyNotify"),
        ("CISCO-PSM-MIB", "ciscoPsmPortBindEPortDenyNotify"))
)
if mibBuilder.loadTexts:
    ciscoPsmPortBindNotifyGroup.setStatus(
        "current"
    )

ciscoPsmFabricBindNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 8)
)
ciscoPsmFabricBindNotifyGroup.setObjects(
    ("CISCO-PSM-MIB", "ciscoPsmFabricBindDenyNotify")
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindNotifyGroup.setStatus(
        "deprecated"
    )

ciscoPsmFabricBindNotifyGroupR1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 2, 14)
)
ciscoPsmFabricBindNotifyGroupR1.setObjects(
    ("CISCO-PSM-MIB", "ciscoPsmFabricBindDenyNotifyNew")
)
if mibBuilder.loadTexts:
    ciscoPsmFabricBindNotifyGroupR1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPsmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPsmMIBCompliance.setStatus(
        "deprecated"
    )

ciscoPsmMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPsmMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoPsmMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoPsmMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoPsmMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoPsmMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoPsmMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoPsmMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoPsmMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 364, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoPsmMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PSM-MIB",
    **{"CpsmVirtNwType": CpsmVirtNwType,
       "CpsmPortBindDevType": CpsmPortBindDevType,
       "CpsmPortBindSwPortType": CpsmPortBindSwPortType,
       "CpsmDbActivate": CpsmDbActivate,
       "CpsmActivateResult": CpsmActivateResult,
       "CpsmAutoLearnEnable": CpsmAutoLearnEnable,
       "CpsmClearStats": CpsmClearStats,
       "CpsmClearAutoLearnDb": CpsmClearAutoLearnDb,
       "CpsmDiffDb": CpsmDiffDb,
       "CpsmDiffReason": CpsmDiffReason,
       "CpsmStatsCounter": CpsmStatsCounter,
       "CpsmViolationReasonCode": CpsmViolationReasonCode,
       "ciscoPsmMIB": ciscoPsmMIB,
       "ciscoPsmMIBNotifs": ciscoPsmMIBNotifs,
       "ciscoPsmPortBindFPortDenyNotify": ciscoPsmPortBindFPortDenyNotify,
       "ciscoPsmPortBindEPortDenyNotify": ciscoPsmPortBindEPortDenyNotify,
       "ciscoPsmFabricBindDenyNotify": ciscoPsmFabricBindDenyNotify,
       "ciscoPsmFabricBindDenyNotifyNew": ciscoPsmFabricBindDenyNotifyNew,
       "ciscoPsmMIBObjects": ciscoPsmMIBObjects,
       "cpsmConfiguration": cpsmConfiguration,
       "cpsmPortBindTable": cpsmPortBindTable,
       "cpsmPortBindEntry": cpsmPortBindEntry,
       "cpsmPortBindNwType": cpsmPortBindNwType,
       "cpsmPortBindNwIndex": cpsmPortBindNwIndex,
       "cpsmPortBindIndex": cpsmPortBindIndex,
       "cpsmPortBindLoginDevType": cpsmPortBindLoginDevType,
       "cpsmPortBindLoginDev": cpsmPortBindLoginDev,
       "cpsmPortBindLoginPointType": cpsmPortBindLoginPointType,
       "cpsmPortBindLoginPoint": cpsmPortBindLoginPoint,
       "cpsmPortBindRowStatus": cpsmPortBindRowStatus,
       "cpsmPortBindActivateTable": cpsmPortBindActivateTable,
       "cpsmPortBindActivateEntry": cpsmPortBindActivateEntry,
       "cpsmPortBindActivate": cpsmPortBindActivate,
       "cpsmPortBindResult": cpsmPortBindResult,
       "cpsmPortBindLastActTime": cpsmPortBindLastActTime,
       "cpsmPortBindActState": cpsmPortBindActState,
       "cpsmFabricBindTable": cpsmFabricBindTable,
       "cpsmFabricBindEntry": cpsmFabricBindEntry,
       "cpsmFabricBindNwType": cpsmFabricBindNwType,
       "cpsmFabricBindNwIndex": cpsmFabricBindNwIndex,
       "cpsmFabricBindIndex": cpsmFabricBindIndex,
       "cpsmFabricBindSwitchWwn": cpsmFabricBindSwitchWwn,
       "cpsmFabricBindDomId": cpsmFabricBindDomId,
       "cpsmFabricBindRowStatus": cpsmFabricBindRowStatus,
       "cpsmFabricBindActivateTable": cpsmFabricBindActivateTable,
       "cpsmFabricBindActivateEntry": cpsmFabricBindActivateEntry,
       "cpsmFabricBindActivate": cpsmFabricBindActivate,
       "cpsmFabricBindResult": cpsmFabricBindResult,
       "cpsmFabricBindLastActTime": cpsmFabricBindLastActTime,
       "cpsmFabricBindActState": cpsmFabricBindActState,
       "cpsmPortBindCopyTable": cpsmPortBindCopyTable,
       "cpsmPortBindCopyEntry": cpsmPortBindCopyEntry,
       "cpsmPortBindCopyActToConfig": cpsmPortBindCopyActToConfig,
       "cpsmPortBindLastChangeTime": cpsmPortBindLastChangeTime,
       "cpsmFabricBindCopyTable": cpsmFabricBindCopyTable,
       "cpsmFabricBindCopyEntry": cpsmFabricBindCopyEntry,
       "cpsmFabricBindCopyActToConfig": cpsmFabricBindCopyActToConfig,
       "cpsmFabricBindLastChangeTime": cpsmFabricBindLastChangeTime,
       "cpsmPortBindEnfTable": cpsmPortBindEnfTable,
       "cpsmPortBindEnfEntry": cpsmPortBindEnfEntry,
       "cpsmPortBindEnfNwType": cpsmPortBindEnfNwType,
       "cpsmPortBindEnfNwIndex": cpsmPortBindEnfNwIndex,
       "cpsmPortBindEnfIndex": cpsmPortBindEnfIndex,
       "cpsmPortBindEnfLoginDevType": cpsmPortBindEnfLoginDevType,
       "cpsmPortBindEnfLoginDev": cpsmPortBindEnfLoginDev,
       "cpsmPortBindEnfLoginPointType": cpsmPortBindEnfLoginPointType,
       "cpsmPortBindEnfLoginPoint": cpsmPortBindEnfLoginPoint,
       "cpsmPortBindEnfIsLearnt": cpsmPortBindEnfIsLearnt,
       "cpsmFabricBindEnfTable": cpsmFabricBindEnfTable,
       "cpsmFabricBindEnfEntry": cpsmFabricBindEnfEntry,
       "cpsmFabricBindEnfNwType": cpsmFabricBindEnfNwType,
       "cpsmFabricBindEnfNwIndex": cpsmFabricBindEnfNwIndex,
       "cpsmFabricBindEnfIndex": cpsmFabricBindEnfIndex,
       "cpsmFabricBindEnfSwitchWwn": cpsmFabricBindEnfSwitchWwn,
       "cpsmFabricBindEnfDomId": cpsmFabricBindEnfDomId,
       "cpsmFabricBindEnfIsLearnt": cpsmFabricBindEnfIsLearnt,
       "cpsmPortBindAutoLearnTable": cpsmPortBindAutoLearnTable,
       "cpsmPortBindAutoLearnEntry": cpsmPortBindAutoLearnEntry,
       "cpsmPortBindAutoLearnIndexType": cpsmPortBindAutoLearnIndexType,
       "cpsmPortBindAutoLearnIndex": cpsmPortBindAutoLearnIndex,
       "cpsmPortBindAutoLearnEnable": cpsmPortBindAutoLearnEnable,
       "cpsmFabricBindAutoLearnTable": cpsmFabricBindAutoLearnTable,
       "cpsmFabricBindAutoLearnEntry": cpsmFabricBindAutoLearnEntry,
       "cpsmFabricBindAutoLearnIndexType": cpsmFabricBindAutoLearnIndexType,
       "cpsmFabricBindAutoLearnIndex": cpsmFabricBindAutoLearnIndex,
       "cpsmFabricBindAutoLearnEnable": cpsmFabricBindAutoLearnEnable,
       "cpsmPortBindClearTable": cpsmPortBindClearTable,
       "cpsmPortBindClearEntry": cpsmPortBindClearEntry,
       "cpsmPortBindClearNwType": cpsmPortBindClearNwType,
       "cpsmPortBindClearNwIndex": cpsmPortBindClearNwIndex,
       "cpsmPortBindClearStats": cpsmPortBindClearStats,
       "cpsmPortBindClearAutoLearnDb": cpsmPortBindClearAutoLearnDb,
       "cpsmPortBindClearAutoLearnIntf": cpsmPortBindClearAutoLearnIntf,
       "cpsmFabricBindClearTable": cpsmFabricBindClearTable,
       "cpsmFabricBindClearEntry": cpsmFabricBindClearEntry,
       "cpsmFabricBindClearNwType": cpsmFabricBindClearNwType,
       "cpsmFabricBindClearNwIndex": cpsmFabricBindClearNwIndex,
       "cpsmFabricBindClearStats": cpsmFabricBindClearStats,
       "cpsmFabricBindClearAutoLearnDb": cpsmFabricBindClearAutoLearnDb,
       "cpsmFabricBindClearAutoLearnIntf": cpsmFabricBindClearAutoLearnIntf,
       "cpsmPortBindDiffConfigTable": cpsmPortBindDiffConfigTable,
       "cpsmPortBindDiffConfigEntry": cpsmPortBindDiffConfigEntry,
       "cpsmPortBindDiffConfigNwType": cpsmPortBindDiffConfigNwType,
       "cpsmPortBindDiffConfigNwIndex": cpsmPortBindDiffConfigNwIndex,
       "cpsmPortBindDiffConfigDb": cpsmPortBindDiffConfigDb,
       "cpsmPortBindDiffTable": cpsmPortBindDiffTable,
       "cpsmPortBindDiffEntry": cpsmPortBindDiffEntry,
       "cpsmPortBindDiffNwType": cpsmPortBindDiffNwType,
       "cpsmPortBindDiffNwIndex": cpsmPortBindDiffNwIndex,
       "cpsmPortBindDiffIndex": cpsmPortBindDiffIndex,
       "cpsmPortBindDiffReason": cpsmPortBindDiffReason,
       "cpsmPortBindDiffLoginDevType": cpsmPortBindDiffLoginDevType,
       "cpsmPortBindDiffLoginDev": cpsmPortBindDiffLoginDev,
       "cpsmPortBindDiffLoginPointType": cpsmPortBindDiffLoginPointType,
       "cpsmPortBindDiffLoginPoint": cpsmPortBindDiffLoginPoint,
       "cpsmFabricBindDiffConfigTable": cpsmFabricBindDiffConfigTable,
       "cpsmFabricBindDiffConfigEntry": cpsmFabricBindDiffConfigEntry,
       "cpsmFabricBindDiffConfigNwType": cpsmFabricBindDiffConfigNwType,
       "cpsmFabricBindDiffConfigNwIndex": cpsmFabricBindDiffConfigNwIndex,
       "cpsmFabricBindDiffConfigDb": cpsmFabricBindDiffConfigDb,
       "cpsmFabricBindDiffTable": cpsmFabricBindDiffTable,
       "cpsmFabricBindDiffEntry": cpsmFabricBindDiffEntry,
       "cpsmFabricBindDiffNwType": cpsmFabricBindDiffNwType,
       "cpsmFabricBindDiffNwIndex": cpsmFabricBindDiffNwIndex,
       "cpsmFabricBindDiffIndex": cpsmFabricBindDiffIndex,
       "cpsmFabricBindDiffReason": cpsmFabricBindDiffReason,
       "cpsmFabricBindDiffSwitchWwn": cpsmFabricBindDiffSwitchWwn,
       "cpsmFabricBindDiffDomId": cpsmFabricBindDiffDomId,
       "cpsmNotifyEnable": cpsmNotifyEnable,
       "cpsmEfmdConfigTable": cpsmEfmdConfigTable,
       "cpsmEfmdConfigEntry": cpsmEfmdConfigEntry,
       "cpsmEfmdConfigEnforce": cpsmEfmdConfigEnforce,
       "cpsmPortBindNextFreeTable": cpsmPortBindNextFreeTable,
       "cpsmPortBindNextFreeEntry": cpsmPortBindNextFreeEntry,
       "cpsmPortBindNextFreeNwType": cpsmPortBindNextFreeNwType,
       "cpsmPortBindNextFreeNwIndex": cpsmPortBindNextFreeNwIndex,
       "cpsmPortBindNextFreeIndex": cpsmPortBindNextFreeIndex,
       "cpsmFabricBindNextFreeTable": cpsmFabricBindNextFreeTable,
       "cpsmFabricBindNextFreeEntry": cpsmFabricBindNextFreeEntry,
       "cpsmFabricBindNextFreeNwType": cpsmFabricBindNextFreeNwType,
       "cpsmFabricBindNextFreeNwIndex": cpsmFabricBindNextFreeNwIndex,
       "cpsmFabricBindNextFreeIndex": cpsmFabricBindNextFreeIndex,
       "cpsmStats": cpsmStats,
       "cpsmPortBindStatsTable": cpsmPortBindStatsTable,
       "cpsmPortBindStatsEntry": cpsmPortBindStatsEntry,
       "cpsmPortBindVsanVlanType": cpsmPortBindVsanVlanType,
       "cpsmPortBindVsanVlanIndex": cpsmPortBindVsanVlanIndex,
       "cpsmPortBindAllowedLogins": cpsmPortBindAllowedLogins,
       "cpsmPortBindDeniedLogins": cpsmPortBindDeniedLogins,
       "cpsmFabricBindStatsTable": cpsmFabricBindStatsTable,
       "cpsmFabricBindStatsEntry": cpsmFabricBindStatsEntry,
       "cpsmFabricBindVsanVlanType": cpsmFabricBindVsanVlanType,
       "cpsmFabricBindVsanVlanIndex": cpsmFabricBindVsanVlanIndex,
       "cpsmFabricBindAllowedReqs": cpsmFabricBindAllowedReqs,
       "cpsmFabricBindDeniedReqs": cpsmFabricBindDeniedReqs,
       "cpsmPortBindViolationTable": cpsmPortBindViolationTable,
       "cpsmPortBindViolationEntry": cpsmPortBindViolationEntry,
       "cpsmPortBindViolationNwType": cpsmPortBindViolationNwType,
       "cpsmPortBindViolationNwIndex": cpsmPortBindViolationNwIndex,
       "cpsmPortBindViolationIndex": cpsmPortBindViolationIndex,
       "cpsmPortBindLoginPwwn": cpsmPortBindLoginPwwn,
       "cpsmPortBindLoginNwwn": cpsmPortBindLoginNwwn,
       "cpsmPortBindLoginSwwn": cpsmPortBindLoginSwwn,
       "cpsmPortBindLoginPort": cpsmPortBindLoginPort,
       "cpsmPortBindLoginTime": cpsmPortBindLoginTime,
       "cpsmPortBindLoginCount": cpsmPortBindLoginCount,
       "cpsmPortBindLoginIntf": cpsmPortBindLoginIntf,
       "cpsmFabricBindViolationTable": cpsmFabricBindViolationTable,
       "cpsmFabricBindViolationEntry": cpsmFabricBindViolationEntry,
       "cpsmFabricBindViolationIndex": cpsmFabricBindViolationIndex,
       "cpsmFabricBindSwwn": cpsmFabricBindSwwn,
       "cpsmFabricBindLocalPort": cpsmFabricBindLocalPort,
       "cpsmFabricBindDenialTime": cpsmFabricBindDenialTime,
       "cpsmFabricBindLocalIntf": cpsmFabricBindLocalIntf,
       "cpsmFabricBindViolationNewTable": cpsmFabricBindViolationNewTable,
       "cpsmFabricBindViolationNewEntry": cpsmFabricBindViolationNewEntry,
       "cpsmFabricBindViolationNwTypeR1": cpsmFabricBindViolationNwTypeR1,
       "cpsmFabricBindViolationNwIndexR1": cpsmFabricBindViolationNwIndexR1,
       "cpsmFabricBindViolationIndexR1": cpsmFabricBindViolationIndexR1,
       "cpsmFabricBindSwwnR1": cpsmFabricBindSwwnR1,
       "cpsmFabricBindDenialTimeR1": cpsmFabricBindDenialTimeR1,
       "cpsmFabricBindDenialCountR1": cpsmFabricBindDenialCountR1,
       "cpsmFabricBindDenialDomId": cpsmFabricBindDenialDomId,
       "cpsmFabricBindDenialReasonCode": cpsmFabricBindDenialReasonCode,
       "cpsmEfmdStatsTable": cpsmEfmdStatsTable,
       "cpsmEfmdStatsEntry": cpsmEfmdStatsEntry,
       "cpsmEfmdTxMergeReqs": cpsmEfmdTxMergeReqs,
       "cpsmEfmdRxMergeReqs": cpsmEfmdRxMergeReqs,
       "cpsmEfmdTxMergeAccs": cpsmEfmdTxMergeAccs,
       "cpsmEfmdRxMergeAccs": cpsmEfmdRxMergeAccs,
       "cpsmEfmdTxMergeRejs": cpsmEfmdTxMergeRejs,
       "cpsmEfmdRxMergeRejs": cpsmEfmdRxMergeRejs,
       "cpsmEfmdTxMergeBusys": cpsmEfmdTxMergeBusys,
       "cpsmEfmdRxMergeBusys": cpsmEfmdRxMergeBusys,
       "cpsmEfmdTxMergeErrs": cpsmEfmdTxMergeErrs,
       "cpsmEfmdRxMergeErrs": cpsmEfmdRxMergeErrs,
       "ciscoPsmMIBConform": ciscoPsmMIBConform,
       "ciscoPsmMIBCompliances": ciscoPsmMIBCompliances,
       "ciscoPsmMIBCompliance": ciscoPsmMIBCompliance,
       "ciscoPsmMIBComplianceRev1": ciscoPsmMIBComplianceRev1,
       "ciscoPsmMIBComplianceRev2": ciscoPsmMIBComplianceRev2,
       "ciscoPsmMIBComplianceRev3": ciscoPsmMIBComplianceRev3,
       "ciscoPsmMIBComplianceRev4": ciscoPsmMIBComplianceRev4,
       "ciscoPsmMIBComplianceRev5": ciscoPsmMIBComplianceRev5,
       "ciscoPsmMIBGroups": ciscoPsmMIBGroups,
       "ciscoPsmPortBindConfigGroup": ciscoPsmPortBindConfigGroup,
       "ciscoPsmFabricBindConfigGroup": ciscoPsmFabricBindConfigGroup,
       "ciscoPsmPortBindEnforcedGroup": ciscoPsmPortBindEnforcedGroup,
       "ciscoPsmFabricBindEnforcedGroup": ciscoPsmFabricBindEnforcedGroup,
       "ciscoPsmPortBindStatsGroup": ciscoPsmPortBindStatsGroup,
       "ciscoPsmFabricBindStatsGroup": ciscoPsmFabricBindStatsGroup,
       "ciscoPsmPortBindNotifyGroup": ciscoPsmPortBindNotifyGroup,
       "ciscoPsmFabricBindNotifyGroup": ciscoPsmFabricBindNotifyGroup,
       "ciscoPsmPortBindAutoLearnGroup": ciscoPsmPortBindAutoLearnGroup,
       "ciscoPsmFabricBindAutoLearnGroup": ciscoPsmFabricBindAutoLearnGroup,
       "ciscoPsmNotifyEnableGroup": ciscoPsmNotifyEnableGroup,
       "ciscoPsmFabricBindConfigGroup1": ciscoPsmFabricBindConfigGroup1,
       "ciscoPsmFabricBindStatsGroup1": ciscoPsmFabricBindStatsGroup1,
       "ciscoPsmFabricBindNotifyGroupR1": ciscoPsmFabricBindNotifyGroupR1,
       "ciscoPsmEfmdConfigGroup": ciscoPsmEfmdConfigGroup,
       "ciscoPsmEfmdStatsGroup": ciscoPsmEfmdStatsGroup,
       "ciscoPsmFabricBindStatsGroup2": ciscoPsmFabricBindStatsGroup2,
       "ciscoPsmFabricBindStatsGroup3": ciscoPsmFabricBindStatsGroup3,
       "ciscoPsmPortBindConfigGroup1": ciscoPsmPortBindConfigGroup1,
       "ciscoPsmFabricBindConfigGroup2": ciscoPsmFabricBindConfigGroup2}
)
