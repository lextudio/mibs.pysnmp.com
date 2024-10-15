# SNMP MIB module (IPGW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPGW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:54 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
 experimental,
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
    "enterprises",
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Ipgw_ObjectIdentity = ObjectIdentity
ipgw = _Ipgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 13)
)
_IpgwCfg_ObjectIdentity = ObjectIdentity
ipgwCfg = _IpgwCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1)
)
_IpgwCfgTable_Object = MibTable
ipgwCfgTable = _IpgwCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    ipgwCfgTable.setStatus("mandatory")
_IpgwCfgEntry_Object = MibTableRow
ipgwCfgEntry = _IpgwCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1)
)
ipgwCfgEntry.setIndexNames(
    (0, "IPGW-MIB", "ipgwCfgIndex"),
)
if mibBuilder.loadTexts:
    ipgwCfgEntry.setStatus("mandatory")
_IpgwCfgIndex_Type = Integer32
_IpgwCfgIndex_Object = MibTableColumn
ipgwCfgIndex = _IpgwCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 1),
    _IpgwCfgIndex_Type()
)
ipgwCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipgwCfgIndex.setStatus("mandatory")
_IpgwCfgLocalIpAdrs_Type = IpAddress
_IpgwCfgLocalIpAdrs_Object = MibTableColumn
ipgwCfgLocalIpAdrs = _IpgwCfgLocalIpAdrs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 2),
    _IpgwCfgLocalIpAdrs_Type()
)
ipgwCfgLocalIpAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCfgLocalIpAdrs.setStatus("mandatory")
_IpgwCfgGatewayIpAdrs_Type = IpAddress
_IpgwCfgGatewayIpAdrs_Object = MibTableColumn
ipgwCfgGatewayIpAdrs = _IpgwCfgGatewayIpAdrs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 3),
    _IpgwCfgGatewayIpAdrs_Type()
)
ipgwCfgGatewayIpAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCfgGatewayIpAdrs.setStatus("mandatory")


class _IpgwCfgTrapDest_Type(Integer32):
    """Custom type ipgwCfgTrapDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("local", 2),
          ("nmc", 1))
    )


_IpgwCfgTrapDest_Type.__name__ = "Integer32"
_IpgwCfgTrapDest_Object = MibTableColumn
ipgwCfgTrapDest = _IpgwCfgTrapDest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 4),
    _IpgwCfgTrapDest_Type()
)
ipgwCfgTrapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCfgTrapDest.setStatus("mandatory")
_IpgwCfgGatewayNetMask_Type = IpAddress
_IpgwCfgGatewayNetMask_Object = MibTableColumn
ipgwCfgGatewayNetMask = _IpgwCfgGatewayNetMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 5),
    _IpgwCfgGatewayNetMask_Type()
)
ipgwCfgGatewayNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCfgGatewayNetMask.setStatus("mandatory")


class _IpgwCfgEthnetFraming_Type(Integer32):
    """Custom type ipgwCfgEthnetFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dix", 2),
          ("snap", 1))
    )


_IpgwCfgEthnetFraming_Type.__name__ = "Integer32"
_IpgwCfgEthnetFraming_Object = MibTableColumn
ipgwCfgEthnetFraming = _IpgwCfgEthnetFraming_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 6),
    _IpgwCfgEthnetFraming_Type()
)
ipgwCfgEthnetFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCfgEthnetFraming.setStatus("mandatory")


class _IpgwCfgEthIfaceName_Type(DisplayString):
    """Custom type ipgwCfgEthIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpgwCfgEthIfaceName_Type.__name__ = "DisplayString"
_IpgwCfgEthIfaceName_Object = MibTableColumn
ipgwCfgEthIfaceName = _IpgwCfgEthIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 7),
    _IpgwCfgEthIfaceName_Type()
)
ipgwCfgEthIfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCfgEthIfaceName.setStatus("mandatory")
_IpgwCfgDefMgmtStationIp_Type = IpAddress
_IpgwCfgDefMgmtStationIp_Object = MibTableColumn
ipgwCfgDefMgmtStationIp = _IpgwCfgDefMgmtStationIp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 8),
    _IpgwCfgDefMgmtStationIp_Type()
)
ipgwCfgDefMgmtStationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCfgDefMgmtStationIp.setStatus("mandatory")


class _IpgwCfgDefCommStr_Type(DisplayString):
    """Custom type ipgwCfgDefCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpgwCfgDefCommStr_Type.__name__ = "DisplayString"
_IpgwCfgDefCommStr_Object = MibTableColumn
ipgwCfgDefCommStr = _IpgwCfgDefCommStr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 1, 1, 1, 9),
    _IpgwCfgDefCommStr_Type()
)
ipgwCfgDefCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCfgDefCommStr.setStatus("mandatory")
_IpgwCmd_ObjectIdentity = ObjectIdentity
ipgwCmd = _IpgwCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3)
)
_IpgwCmdTable_Object = MibTable
ipgwCmdTable = _IpgwCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    ipgwCmdTable.setStatus("mandatory")
_IpgwCmdEntry_Object = MibTableRow
ipgwCmdEntry = _IpgwCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1)
)
ipgwCmdEntry.setIndexNames(
    (0, "IPGW-MIB", "ipgwCmdIndex"),
)
if mibBuilder.loadTexts:
    ipgwCmdEntry.setStatus("mandatory")
_IpgwCmdIndex_Type = Integer32
_IpgwCmdIndex_Object = MibTableColumn
ipgwCmdIndex = _IpgwCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1, 1),
    _IpgwCmdIndex_Type()
)
ipgwCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipgwCmdIndex.setStatus("mandatory")


class _IpgwCmdMgtStationId_Type(OctetString):
    """Custom type ipgwCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IpgwCmdMgtStationId_Type.__name__ = "OctetString"
_IpgwCmdMgtStationId_Object = MibTableColumn
ipgwCmdMgtStationId = _IpgwCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1, 2),
    _IpgwCmdMgtStationId_Type()
)
ipgwCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCmdMgtStationId.setStatus("mandatory")
_IpgwCmdReqId_Type = Integer32
_IpgwCmdReqId_Object = MibTableColumn
ipgwCmdReqId = _IpgwCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1, 3),
    _IpgwCmdReqId_Type()
)
ipgwCmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipgwCmdReqId.setStatus("mandatory")


class _IpgwCmdFunction_Type(Integer32):
    """Custom type ipgwCmdFunction based on Integer32"""
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
        *(("bulkfileDownload", 10),
          ("bulkfileUpload", 9),
          ("disruptSelfTest", 6),
          ("lanLoopBack", 8),
          ("noCommand", 1),
          ("nonDisruptSelfTest", 5),
          ("restoreFromDefault", 4),
          ("restoreFromNVRAM", 3),
          ("saveToNVRAM", 2),
          ("softwareReset", 7))
    )


_IpgwCmdFunction_Type.__name__ = "Integer32"
_IpgwCmdFunction_Object = MibTableColumn
ipgwCmdFunction = _IpgwCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1, 4),
    _IpgwCmdFunction_Type()
)
ipgwCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCmdFunction.setStatus("mandatory")


class _IpgwCmdForce_Type(Integer32):
    """Custom type ipgwCmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_IpgwCmdForce_Type.__name__ = "Integer32"
_IpgwCmdForce_Object = MibTableColumn
ipgwCmdForce = _IpgwCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1, 5),
    _IpgwCmdForce_Type()
)
ipgwCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCmdForce.setStatus("mandatory")
_IpgwCmdParam_Type = OctetString
_IpgwCmdParam_Object = MibTableColumn
ipgwCmdParam = _IpgwCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1, 6),
    _IpgwCmdParam_Type()
)
ipgwCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwCmdParam.setStatus("mandatory")


class _IpgwCmdResult_Type(Integer32):
    """Custom type ipgwCmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_IpgwCmdResult_Type.__name__ = "Integer32"
_IpgwCmdResult_Object = MibTableColumn
ipgwCmdResult = _IpgwCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1, 7),
    _IpgwCmdResult_Type()
)
ipgwCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipgwCmdResult.setStatus("mandatory")


class _IpgwCmdCode_Type(Integer32):
    """Custom type ipgwCmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              20,
              22,
              25,
              58,
              73)
        )
    )
    namedValues = NamedValues(
        *(("deviceDisabled", 22),
          ("noError", 1),
          ("noResponse", 12),
          ("pendingSoftwareDownload", 73),
          ("slotEmpty", 8),
          ("testFailed", 25),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20),
          ("userInterfaceActive", 58))
    )


_IpgwCmdCode_Type.__name__ = "Integer32"
_IpgwCmdCode_Object = MibTableColumn
ipgwCmdCode = _IpgwCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 3, 1, 1, 8),
    _IpgwCmdCode_Type()
)
ipgwCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipgwCmdCode.setStatus("mandatory")
_IpgwTrap_ObjectIdentity = ObjectIdentity
ipgwTrap = _IpgwTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 4)
)
_IpgwTrapEnaTable_Object = MibTable
ipgwTrapEnaTable = _IpgwTrapEnaTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 4, 1)
)
if mibBuilder.loadTexts:
    ipgwTrapEnaTable.setStatus("mandatory")
_IpgwTrapEnaEntry_Object = MibTableRow
ipgwTrapEnaEntry = _IpgwTrapEnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 4, 1, 1)
)
ipgwTrapEnaEntry.setIndexNames(
    (0, "IPGW-MIB", "ipgwTrapEnaIndex"),
)
if mibBuilder.loadTexts:
    ipgwTrapEnaEntry.setStatus("mandatory")
_IpgwTrapEnaIndex_Type = Integer32
_IpgwTrapEnaIndex_Object = MibTableColumn
ipgwTrapEnaIndex = _IpgwTrapEnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 4, 1, 1, 1),
    _IpgwTrapEnaIndex_Type()
)
ipgwTrapEnaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipgwTrapEnaIndex.setStatus("mandatory")


class _IpgwTrapEnaUiReset_Type(Integer32):
    """Custom type ipgwTrapEnaUiReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IpgwTrapEnaUiReset_Type.__name__ = "Integer32"
_IpgwTrapEnaUiReset_Object = MibTableColumn
ipgwTrapEnaUiReset = _IpgwTrapEnaUiReset_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 13, 4, 1, 1, 2),
    _IpgwTrapEnaUiReset_Type()
)
ipgwTrapEnaUiReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipgwTrapEnaUiReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPGW-MIB",
    **{"usr": usr,
       "nas": nas,
       "ipgw": ipgw,
       "ipgwCfg": ipgwCfg,
       "ipgwCfgTable": ipgwCfgTable,
       "ipgwCfgEntry": ipgwCfgEntry,
       "ipgwCfgIndex": ipgwCfgIndex,
       "ipgwCfgLocalIpAdrs": ipgwCfgLocalIpAdrs,
       "ipgwCfgGatewayIpAdrs": ipgwCfgGatewayIpAdrs,
       "ipgwCfgTrapDest": ipgwCfgTrapDest,
       "ipgwCfgGatewayNetMask": ipgwCfgGatewayNetMask,
       "ipgwCfgEthnetFraming": ipgwCfgEthnetFraming,
       "ipgwCfgEthIfaceName": ipgwCfgEthIfaceName,
       "ipgwCfgDefMgmtStationIp": ipgwCfgDefMgmtStationIp,
       "ipgwCfgDefCommStr": ipgwCfgDefCommStr,
       "ipgwCmd": ipgwCmd,
       "ipgwCmdTable": ipgwCmdTable,
       "ipgwCmdEntry": ipgwCmdEntry,
       "ipgwCmdIndex": ipgwCmdIndex,
       "ipgwCmdMgtStationId": ipgwCmdMgtStationId,
       "ipgwCmdReqId": ipgwCmdReqId,
       "ipgwCmdFunction": ipgwCmdFunction,
       "ipgwCmdForce": ipgwCmdForce,
       "ipgwCmdParam": ipgwCmdParam,
       "ipgwCmdResult": ipgwCmdResult,
       "ipgwCmdCode": ipgwCmdCode,
       "ipgwTrap": ipgwTrap,
       "ipgwTrapEnaTable": ipgwTrapEnaTable,
       "ipgwTrapEnaEntry": ipgwTrapEnaEntry,
       "ipgwTrapEnaIndex": ipgwTrapEnaIndex,
       "ipgwTrapEnaUiReset": ipgwTrapEnaUiReset}
)
