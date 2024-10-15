# SNMP MIB module (IPAD-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPAD-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:40 2024
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

(ipad,) = mibBuilder.importSymbols(
    "IPADv2-MIB",
    "ipad")

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


# MODULE-IDENTITY

ipadBridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpadBridgeParms_ObjectIdentity = ObjectIdentity
ipadBridgeParms = _IpadBridgeParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1)
)
_IpadBridgeManagementMacAddress_Type = OctetString
_IpadBridgeManagementMacAddress_Object = MibScalar
ipadBridgeManagementMacAddress = _IpadBridgeManagementMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1, 1),
    _IpadBridgeManagementMacAddress_Type()
)
ipadBridgeManagementMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgeManagementMacAddress.setStatus("current")


class _IpadBridgeEnable_Type(Integer32):
    """Custom type ipadBridgeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadBridgeEnable_Type.__name__ = "Integer32"
_IpadBridgeEnable_Object = MibScalar
ipadBridgeEnable = _IpadBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1, 2),
    _IpadBridgeEnable_Type()
)
ipadBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgeEnable.setStatus("current")


class _IpadBridgePortAdd_Type(Integer32):
    """Custom type ipadBridgePortAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadBridgePortAdd_Type.__name__ = "Integer32"
_IpadBridgePortAdd_Object = MibScalar
ipadBridgePortAdd = _IpadBridgePortAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1, 3),
    _IpadBridgePortAdd_Type()
)
ipadBridgePortAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgePortAdd.setStatus("current")
_IpadBridgePortDelete_Type = Integer32
_IpadBridgePortDelete_Object = MibScalar
ipadBridgePortDelete = _IpadBridgePortDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 1, 4),
    _IpadBridgePortDelete_Type()
)
ipadBridgePortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgePortDelete.setStatus("current")
_IpadBridgePortTable_Object = MibTable
ipadBridgePortTable = _IpadBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2)
)
if mibBuilder.loadTexts:
    ipadBridgePortTable.setStatus("current")
_IpadBridgePortTableEntry_Object = MibTableRow
ipadBridgePortTableEntry = _IpadBridgePortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1)
)
ipadBridgePortTableEntry.setIndexNames(
    (0, "IPAD-BRIDGE-MIB", "ipadBridgePortIndex"),
)
if mibBuilder.loadTexts:
    ipadBridgePortTableEntry.setStatus("current")
_IpadBridgePortIndex_Type = Integer32
_IpadBridgePortIndex_Object = MibTableColumn
ipadBridgePortIndex = _IpadBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 1),
    _IpadBridgePortIndex_Type()
)
ipadBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadBridgePortIndex.setStatus("current")
_IpadBridgePortEndpoint_Type = DisplayString
_IpadBridgePortEndpoint_Object = MibTableColumn
ipadBridgePortEndpoint = _IpadBridgePortEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 2),
    _IpadBridgePortEndpoint_Type()
)
ipadBridgePortEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgePortEndpoint.setStatus("current")


class _IpadBridgePortBPDUOption_Type(Integer32):
    """Custom type ipadBridgePortBPDUOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadBridgePortBPDUOption_Type.__name__ = "Integer32"
_IpadBridgePortBPDUOption_Object = MibTableColumn
ipadBridgePortBPDUOption = _IpadBridgePortBPDUOption_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 3),
    _IpadBridgePortBPDUOption_Type()
)
ipadBridgePortBPDUOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgePortBPDUOption.setStatus("current")


class _IpadBridgePortMulticastAddrDest_Type(Integer32):
    """Custom type ipadBridgePortMulticastAddrDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadBridgePortMulticastAddrDest_Type.__name__ = "Integer32"
_IpadBridgePortMulticastAddrDest_Object = MibTableColumn
ipadBridgePortMulticastAddrDest = _IpadBridgePortMulticastAddrDest_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 4),
    _IpadBridgePortMulticastAddrDest_Type()
)
ipadBridgePortMulticastAddrDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgePortMulticastAddrDest.setStatus("current")


class _IpadBridgePortBroadcastAddrDest_Type(Integer32):
    """Custom type ipadBridgePortBroadcastAddrDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadBridgePortBroadcastAddrDest_Type.__name__ = "Integer32"
_IpadBridgePortBroadcastAddrDest_Object = MibTableColumn
ipadBridgePortBroadcastAddrDest = _IpadBridgePortBroadcastAddrDest_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 5),
    _IpadBridgePortBroadcastAddrDest_Type()
)
ipadBridgePortBroadcastAddrDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgePortBroadcastAddrDest.setStatus("current")


class _IpadBridgePortForwardIpFramesOnly_Type(Integer32):
    """Custom type ipadBridgePortForwardIpFramesOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadBridgePortForwardIpFramesOnly_Type.__name__ = "Integer32"
_IpadBridgePortForwardIpFramesOnly_Object = MibTableColumn
ipadBridgePortForwardIpFramesOnly = _IpadBridgePortForwardIpFramesOnly_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28, 2, 1, 6),
    _IpadBridgePortForwardIpFramesOnly_Type()
)
ipadBridgePortForwardIpFramesOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadBridgePortForwardIpFramesOnly.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPAD-BRIDGE-MIB",
    **{"ipadBridge": ipadBridge,
       "ipadBridgeParms": ipadBridgeParms,
       "ipadBridgeManagementMacAddress": ipadBridgeManagementMacAddress,
       "ipadBridgeEnable": ipadBridgeEnable,
       "ipadBridgePortAdd": ipadBridgePortAdd,
       "ipadBridgePortDelete": ipadBridgePortDelete,
       "ipadBridgePortTable": ipadBridgePortTable,
       "ipadBridgePortTableEntry": ipadBridgePortTableEntry,
       "ipadBridgePortIndex": ipadBridgePortIndex,
       "ipadBridgePortEndpoint": ipadBridgePortEndpoint,
       "ipadBridgePortBPDUOption": ipadBridgePortBPDUOption,
       "ipadBridgePortMulticastAddrDest": ipadBridgePortMulticastAddrDest,
       "ipadBridgePortBroadcastAddrDest": ipadBridgePortBroadcastAddrDest,
       "ipadBridgePortForwardIpFramesOnly": ipadBridgePortForwardIpFramesOnly}
)
