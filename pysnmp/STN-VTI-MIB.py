# SNMP MIB module (STN-VTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-VTI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:21 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification")

(stnRouterVTI,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterVTI")


# MODULE-IDENTITY

stnVti = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnVtiObjects_ObjectIdentity = ObjectIdentity
stnVtiObjects = _StnVtiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1)
)
_StnVtiTable_Object = MibTable
stnVtiTable = _StnVtiTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnVtiTable.setStatus("current")
_StnVtiEntry_Object = MibTableRow
stnVtiEntry = _StnVtiEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1)
)
stnVtiEntry.setIndexNames(
    (0, "STN-VTI-MIB", "stnVtiIfIndex"),
)
if mibBuilder.loadTexts:
    stnVtiEntry.setStatus("current")
_StnVtiIfIndex_Type = InterfaceIndex
_StnVtiIfIndex_Object = MibTableColumn
stnVtiIfIndex = _StnVtiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 1),
    _StnVtiIfIndex_Type()
)
stnVtiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiIfIndex.setStatus("current")
_StnVtiViId_Type = Integer32
_StnVtiViId_Object = MibTableColumn
stnVtiViId = _StnVtiViId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 2),
    _StnVtiViId_Type()
)
stnVtiViId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiViId.setStatus("current")


class _StnVtiName_Type(DisplayString):
    """Custom type stnVtiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StnVtiName_Type.__name__ = "DisplayString"
_StnVtiName_Object = MibTableColumn
stnVtiName = _StnVtiName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 3),
    _StnVtiName_Type()
)
stnVtiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiName.setStatus("current")


class _StnVtiPolicy_Type(DisplayString):
    """Custom type stnVtiPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StnVtiPolicy_Type.__name__ = "DisplayString"
_StnVtiPolicy_Object = MibTableColumn
stnVtiPolicy = _StnVtiPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 4),
    _StnVtiPolicy_Type()
)
stnVtiPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiPolicy.setStatus("current")


class _StnVtiState_Type(Integer32):
    """Custom type stnVtiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_StnVtiState_Type.__name__ = "Integer32"
_StnVtiState_Object = MibTableColumn
stnVtiState = _StnVtiState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 5),
    _StnVtiState_Type()
)
stnVtiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiState.setStatus("current")
_StnVtiLastError_Type = Integer32
_StnVtiLastError_Object = MibTableColumn
stnVtiLastError = _StnVtiLastError_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 6),
    _StnVtiLastError_Type()
)
stnVtiLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiLastError.setStatus("current")
_StnVtiProxyTunnelSerialNum_Type = Integer32
_StnVtiProxyTunnelSerialNum_Object = MibTableColumn
stnVtiProxyTunnelSerialNum = _StnVtiProxyTunnelSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 7),
    _StnVtiProxyTunnelSerialNum_Type()
)
stnVtiProxyTunnelSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiProxyTunnelSerialNum.setStatus("current")
_StnVtiMTU_Type = Integer32
_StnVtiMTU_Object = MibTableColumn
stnVtiMTU = _StnVtiMTU_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 8),
    _StnVtiMTU_Type()
)
stnVtiMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiMTU.setStatus("current")
_StnVtiSpeed_Type = Integer32
_StnVtiSpeed_Object = MibTableColumn
stnVtiSpeed = _StnVtiSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 9),
    _StnVtiSpeed_Type()
)
stnVtiSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiSpeed.setStatus("current")
_StnVtiL2MuxIdx_Type = InterfaceIndex
_StnVtiL2MuxIdx_Object = MibTableColumn
stnVtiL2MuxIdx = _StnVtiL2MuxIdx_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9, 1, 1, 1, 1, 10),
    _StnVtiL2MuxIdx_Type()
)
stnVtiL2MuxIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVtiL2MuxIdx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-VTI-MIB",
    **{"stnVti": stnVti,
       "stnVtiObjects": stnVtiObjects,
       "stnVtiTable": stnVtiTable,
       "stnVtiEntry": stnVtiEntry,
       "stnVtiIfIndex": stnVtiIfIndex,
       "stnVtiViId": stnVtiViId,
       "stnVtiName": stnVtiName,
       "stnVtiPolicy": stnVtiPolicy,
       "stnVtiState": stnVtiState,
       "stnVtiLastError": stnVtiLastError,
       "stnVtiProxyTunnelSerialNum": stnVtiProxyTunnelSerialNum,
       "stnVtiMTU": stnVtiMTU,
       "stnVtiSpeed": stnVtiSpeed,
       "stnVtiL2MuxIdx": stnVtiL2MuxIdx}
)
