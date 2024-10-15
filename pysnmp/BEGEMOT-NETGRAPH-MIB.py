# SNMP MIB module (BEGEMOT-NETGRAPH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BEGEMOT-NETGRAPH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:46 2024
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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

begemotNg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NgTypeName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class NgNodeName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class NgNodeNameOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class NgHookName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class NgNodeId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NgNodeIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_BegemotNgObjects_ObjectIdentity = ObjectIdentity
begemotNgObjects = _BegemotNgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1)
)
_BegemotNgConfig_ObjectIdentity = ObjectIdentity
begemotNgConfig = _BegemotNgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1)
)
_BegemotNgControlNodeName_Type = NgNodeName
_BegemotNgControlNodeName_Object = MibScalar
begemotNgControlNodeName = _BegemotNgControlNodeName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 1),
    _BegemotNgControlNodeName_Type()
)
begemotNgControlNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgControlNodeName.setStatus("current")


class _BegemotNgResBufSiz_Type(Integer32):
    """Custom type begemotNgResBufSiz based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65536),
    )


_BegemotNgResBufSiz_Type.__name__ = "Integer32"
_BegemotNgResBufSiz_Object = MibScalar
begemotNgResBufSiz = _BegemotNgResBufSiz_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 2),
    _BegemotNgResBufSiz_Type()
)
begemotNgResBufSiz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotNgResBufSiz.setStatus("current")


class _BegemotNgTimeout_Type(Integer32):
    """Custom type begemotNgTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_BegemotNgTimeout_Type.__name__ = "Integer32"
_BegemotNgTimeout_Object = MibScalar
begemotNgTimeout = _BegemotNgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 3),
    _BegemotNgTimeout_Type()
)
begemotNgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotNgTimeout.setStatus("current")
if mibBuilder.loadTexts:
    begemotNgTimeout.setUnits("milliseconds")


class _BegemotNgDebugLevel_Type(Unsigned32):
    """Custom type begemotNgDebugLevel based on Unsigned32"""
    defaultValue = 0


_BegemotNgDebugLevel_Object = MibScalar
begemotNgDebugLevel = _BegemotNgDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 4),
    _BegemotNgDebugLevel_Type()
)
begemotNgDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotNgDebugLevel.setStatus("current")
_BegemotNgStats_ObjectIdentity = ObjectIdentity
begemotNgStats = _BegemotNgStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2)
)
_BegemotNgNoMems_Type = Counter32
_BegemotNgNoMems_Object = MibScalar
begemotNgNoMems = _BegemotNgNoMems_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 1),
    _BegemotNgNoMems_Type()
)
begemotNgNoMems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgNoMems.setStatus("current")
_BegemotNgMsgReadErrs_Type = Counter32
_BegemotNgMsgReadErrs_Object = MibScalar
begemotNgMsgReadErrs = _BegemotNgMsgReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 2),
    _BegemotNgMsgReadErrs_Type()
)
begemotNgMsgReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgMsgReadErrs.setStatus("current")
_BegemotNgTooLargeMsgs_Type = Counter32
_BegemotNgTooLargeMsgs_Object = MibScalar
begemotNgTooLargeMsgs = _BegemotNgTooLargeMsgs_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 3),
    _BegemotNgTooLargeMsgs_Type()
)
begemotNgTooLargeMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgTooLargeMsgs.setStatus("current")
_BegemotNgDataReadErrs_Type = Counter32
_BegemotNgDataReadErrs_Object = MibScalar
begemotNgDataReadErrs = _BegemotNgDataReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 4),
    _BegemotNgDataReadErrs_Type()
)
begemotNgDataReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgDataReadErrs.setStatus("current")
_BegemotNgTooLargeDatas_Type = Counter32
_BegemotNgTooLargeDatas_Object = MibScalar
begemotNgTooLargeDatas = _BegemotNgTooLargeDatas_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 5),
    _BegemotNgTooLargeDatas_Type()
)
begemotNgTooLargeDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgTooLargeDatas.setStatus("current")
_BegemotNgTypeTable_Object = MibTable
begemotNgTypeTable = _BegemotNgTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    begemotNgTypeTable.setStatus("current")
_BegemotNgTypeEntry_Object = MibTableRow
begemotNgTypeEntry = _BegemotNgTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1)
)
begemotNgTypeEntry.setIndexNames(
    (0, "BEGEMOT-NETGRAPH-MIB", "begemotNgTypeName"),
)
if mibBuilder.loadTexts:
    begemotNgTypeEntry.setStatus("current")
_BegemotNgTypeName_Type = NgTypeName
_BegemotNgTypeName_Object = MibTableColumn
begemotNgTypeName = _BegemotNgTypeName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1, 1),
    _BegemotNgTypeName_Type()
)
begemotNgTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotNgTypeName.setStatus("current")


class _BegemotNgTypeStatus_Type(Integer32):
    """Custom type begemotNgTypeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("unloaded", 2))
    )


_BegemotNgTypeStatus_Type.__name__ = "Integer32"
_BegemotNgTypeStatus_Object = MibTableColumn
begemotNgTypeStatus = _BegemotNgTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1, 2),
    _BegemotNgTypeStatus_Type()
)
begemotNgTypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    begemotNgTypeStatus.setStatus("current")
_BegemotNgNodeTable_Object = MibTable
begemotNgNodeTable = _BegemotNgNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    begemotNgNodeTable.setStatus("current")
_BegemotNgNodeEntry_Object = MibTableRow
begemotNgNodeEntry = _BegemotNgNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1)
)
begemotNgNodeEntry.setIndexNames(
    (0, "BEGEMOT-NETGRAPH-MIB", "begemotNgNodeId"),
)
if mibBuilder.loadTexts:
    begemotNgNodeEntry.setStatus("current")
_BegemotNgNodeId_Type = NgNodeId
_BegemotNgNodeId_Object = MibTableColumn
begemotNgNodeId = _BegemotNgNodeId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 1),
    _BegemotNgNodeId_Type()
)
begemotNgNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotNgNodeId.setStatus("current")


class _BegemotNgNodeStatus_Type(Integer32):
    """Custom type begemotNgNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_BegemotNgNodeStatus_Type.__name__ = "Integer32"
_BegemotNgNodeStatus_Object = MibTableColumn
begemotNgNodeStatus = _BegemotNgNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 2),
    _BegemotNgNodeStatus_Type()
)
begemotNgNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgNodeStatus.setStatus("current")
_BegemotNgNodeName_Type = NgNodeNameOrEmpty
_BegemotNgNodeName_Object = MibTableColumn
begemotNgNodeName = _BegemotNgNodeName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 3),
    _BegemotNgNodeName_Type()
)
begemotNgNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgNodeName.setStatus("current")
_BegemotNgNodeType_Type = NgTypeName
_BegemotNgNodeType_Object = MibTableColumn
begemotNgNodeType = _BegemotNgNodeType_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 4),
    _BegemotNgNodeType_Type()
)
begemotNgNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgNodeType.setStatus("current")
_BegemotNgNodeHooks_Type = Unsigned32
_BegemotNgNodeHooks_Object = MibTableColumn
begemotNgNodeHooks = _BegemotNgNodeHooks_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 5),
    _BegemotNgNodeHooks_Type()
)
begemotNgNodeHooks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgNodeHooks.setStatus("current")
_BegemotNgHookTable_Object = MibTable
begemotNgHookTable = _BegemotNgHookTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    begemotNgHookTable.setStatus("current")
_BegemotNgHookEntry_Object = MibTableRow
begemotNgHookEntry = _BegemotNgHookEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1)
)
begemotNgHookEntry.setIndexNames(
    (0, "BEGEMOT-NETGRAPH-MIB", "begemotNgHookNodeId"),
    (0, "BEGEMOT-NETGRAPH-MIB", "begemotNgHookHook"),
)
if mibBuilder.loadTexts:
    begemotNgHookEntry.setStatus("current")
_BegemotNgHookNodeId_Type = NgNodeId
_BegemotNgHookNodeId_Object = MibTableColumn
begemotNgHookNodeId = _BegemotNgHookNodeId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 1),
    _BegemotNgHookNodeId_Type()
)
begemotNgHookNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotNgHookNodeId.setStatus("current")
_BegemotNgHookHook_Type = NgHookName
_BegemotNgHookHook_Object = MibTableColumn
begemotNgHookHook = _BegemotNgHookHook_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 2),
    _BegemotNgHookHook_Type()
)
begemotNgHookHook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgHookHook.setStatus("current")


class _BegemotNgHookStatus_Type(Integer32):
    """Custom type begemotNgHookStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_BegemotNgHookStatus_Type.__name__ = "Integer32"
_BegemotNgHookStatus_Object = MibTableColumn
begemotNgHookStatus = _BegemotNgHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 3),
    _BegemotNgHookStatus_Type()
)
begemotNgHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgHookStatus.setStatus("current")
_BegemotNgHookPeerNodeId_Type = NgNodeId
_BegemotNgHookPeerNodeId_Object = MibTableColumn
begemotNgHookPeerNodeId = _BegemotNgHookPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 4),
    _BegemotNgHookPeerNodeId_Type()
)
begemotNgHookPeerNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgHookPeerNodeId.setStatus("current")
_BegemotNgHookPeerHook_Type = NgHookName
_BegemotNgHookPeerHook_Object = MibTableColumn
begemotNgHookPeerHook = _BegemotNgHookPeerHook_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 5),
    _BegemotNgHookPeerHook_Type()
)
begemotNgHookPeerHook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgHookPeerHook.setStatus("current")
_BegemotNgHookPeerType_Type = NgTypeName
_BegemotNgHookPeerType_Object = MibTableColumn
begemotNgHookPeerType = _BegemotNgHookPeerType_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 6),
    _BegemotNgHookPeerType_Type()
)
begemotNgHookPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNgHookPeerType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-NETGRAPH-MIB",
    **{"NgTypeName": NgTypeName,
       "NgNodeName": NgNodeName,
       "NgNodeNameOrEmpty": NgNodeNameOrEmpty,
       "NgHookName": NgHookName,
       "NgNodeId": NgNodeId,
       "NgNodeIdOrZero": NgNodeIdOrZero,
       "begemotNg": begemotNg,
       "begemotNgObjects": begemotNgObjects,
       "begemotNgConfig": begemotNgConfig,
       "begemotNgControlNodeName": begemotNgControlNodeName,
       "begemotNgResBufSiz": begemotNgResBufSiz,
       "begemotNgTimeout": begemotNgTimeout,
       "begemotNgDebugLevel": begemotNgDebugLevel,
       "begemotNgStats": begemotNgStats,
       "begemotNgNoMems": begemotNgNoMems,
       "begemotNgMsgReadErrs": begemotNgMsgReadErrs,
       "begemotNgTooLargeMsgs": begemotNgTooLargeMsgs,
       "begemotNgDataReadErrs": begemotNgDataReadErrs,
       "begemotNgTooLargeDatas": begemotNgTooLargeDatas,
       "begemotNgTypeTable": begemotNgTypeTable,
       "begemotNgTypeEntry": begemotNgTypeEntry,
       "begemotNgTypeName": begemotNgTypeName,
       "begemotNgTypeStatus": begemotNgTypeStatus,
       "begemotNgNodeTable": begemotNgNodeTable,
       "begemotNgNodeEntry": begemotNgNodeEntry,
       "begemotNgNodeId": begemotNgNodeId,
       "begemotNgNodeStatus": begemotNgNodeStatus,
       "begemotNgNodeName": begemotNgNodeName,
       "begemotNgNodeType": begemotNgNodeType,
       "begemotNgNodeHooks": begemotNgNodeHooks,
       "begemotNgHookTable": begemotNgHookTable,
       "begemotNgHookEntry": begemotNgHookEntry,
       "begemotNgHookNodeId": begemotNgHookNodeId,
       "begemotNgHookHook": begemotNgHookHook,
       "begemotNgHookStatus": begemotNgHookStatus,
       "begemotNgHookPeerNodeId": begemotNgHookPeerNodeId,
       "begemotNgHookPeerHook": begemotNgHookPeerHook,
       "begemotNgHookPeerType": begemotNgHookPeerType}
)
