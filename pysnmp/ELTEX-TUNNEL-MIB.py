# SNMP MIB module (ELTEX-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:19 2024
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(IANAtunnelType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAtunnelType")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltexTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 21)
)
eltexTunnelMIB.setRevisions(
        ("2015-12-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TunnelWiFiConfigTable_Object = MibTable
tunnelWiFiConfigTable = _TunnelWiFiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1)
)
if mibBuilder.loadTexts:
    tunnelWiFiConfigTable.setStatus("current")
_TunnelWiFiConfigEntry_Object = MibTableRow
tunnelWiFiConfigEntry = _TunnelWiFiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1)
)
tunnelWiFiConfigEntry.setIndexNames(
    (0, "ELTEX-TUNNEL-MIB", "tunnelWiFiConfigLocalAddressType"),
    (0, "ELTEX-TUNNEL-MIB", "tunnelWiFiConfigLocalAddress"),
    (0, "ELTEX-TUNNEL-MIB", "tunnelWiFiConfigRemoteAddressType"),
    (0, "ELTEX-TUNNEL-MIB", "tunnelWiFiConfigRemoteAddress"),
    (0, "ELTEX-TUNNEL-MIB", "tunnelWiFiConfigEncapsMethod"),
    (0, "ELTEX-TUNNEL-MIB", "tunnelWiFiConfigID"),
)
if mibBuilder.loadTexts:
    tunnelWiFiConfigEntry.setStatus("current")
_TunnelWiFiConfigLocalAddressType_Type = InetAddressType
_TunnelWiFiConfigLocalAddressType_Object = MibTableColumn
tunnelWiFiConfigLocalAddressType = _TunnelWiFiConfigLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 1),
    _TunnelWiFiConfigLocalAddressType_Type()
)
tunnelWiFiConfigLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelWiFiConfigLocalAddressType.setStatus("current")
_TunnelWiFiConfigLocalAddress_Type = InetAddress
_TunnelWiFiConfigLocalAddress_Object = MibTableColumn
tunnelWiFiConfigLocalAddress = _TunnelWiFiConfigLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 2),
    _TunnelWiFiConfigLocalAddress_Type()
)
tunnelWiFiConfigLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelWiFiConfigLocalAddress.setStatus("current")
_TunnelWiFiConfigRemoteAddressType_Type = InetAddressType
_TunnelWiFiConfigRemoteAddressType_Object = MibTableColumn
tunnelWiFiConfigRemoteAddressType = _TunnelWiFiConfigRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 3),
    _TunnelWiFiConfigRemoteAddressType_Type()
)
tunnelWiFiConfigRemoteAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelWiFiConfigRemoteAddressType.setStatus("current")
_TunnelWiFiConfigRemoteAddress_Type = InetAddress
_TunnelWiFiConfigRemoteAddress_Object = MibTableColumn
tunnelWiFiConfigRemoteAddress = _TunnelWiFiConfigRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 4),
    _TunnelWiFiConfigRemoteAddress_Type()
)
tunnelWiFiConfigRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelWiFiConfigRemoteAddress.setStatus("current")
_TunnelWiFiConfigEncapsMethod_Type = IANAtunnelType
_TunnelWiFiConfigEncapsMethod_Object = MibTableColumn
tunnelWiFiConfigEncapsMethod = _TunnelWiFiConfigEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 5),
    _TunnelWiFiConfigEncapsMethod_Type()
)
tunnelWiFiConfigEncapsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelWiFiConfigEncapsMethod.setStatus("current")


class _TunnelWiFiConfigID_Type(Integer32):
    """Custom type tunnelWiFiConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TunnelWiFiConfigID_Type.__name__ = "Integer32"
_TunnelWiFiConfigID_Object = MibTableColumn
tunnelWiFiConfigID = _TunnelWiFiConfigID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 6),
    _TunnelWiFiConfigID_Type()
)
tunnelWiFiConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelWiFiConfigID.setStatus("current")
_TunnelWiFiConfigIfIndex_Type = InterfaceIndexOrZero
_TunnelWiFiConfigIfIndex_Object = MibTableColumn
tunnelWiFiConfigIfIndex = _TunnelWiFiConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 7),
    _TunnelWiFiConfigIfIndex_Type()
)
tunnelWiFiConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelWiFiConfigIfIndex.setStatus("current")
_TunnelWiFiConfigStatus_Type = RowStatus
_TunnelWiFiConfigStatus_Object = MibTableColumn
tunnelWiFiConfigStatus = _TunnelWiFiConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 8),
    _TunnelWiFiConfigStatus_Type()
)
tunnelWiFiConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tunnelWiFiConfigStatus.setStatus("current")


class _TunnelWiFiConfigMode_Type(Integer32):
    """Custom type tunnelWiFiConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("management", 1),
          ("notConfigured", 0))
    )


_TunnelWiFiConfigMode_Type.__name__ = "Integer32"
_TunnelWiFiConfigMode_Object = MibTableColumn
tunnelWiFiConfigMode = _TunnelWiFiConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 9),
    _TunnelWiFiConfigMode_Type()
)
tunnelWiFiConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelWiFiConfigMode.setStatus("current")
_TunnelWiFiConfigDefaultProfile_Type = TruthValue
_TunnelWiFiConfigDefaultProfile_Object = MibTableColumn
tunnelWiFiConfigDefaultProfile = _TunnelWiFiConfigDefaultProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 21, 1, 1, 10),
    _TunnelWiFiConfigDefaultProfile_Type()
)
tunnelWiFiConfigDefaultProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelWiFiConfigDefaultProfile.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-TUNNEL-MIB",
    **{"eltexTunnelMIB": eltexTunnelMIB,
       "tunnelWiFiConfigTable": tunnelWiFiConfigTable,
       "tunnelWiFiConfigEntry": tunnelWiFiConfigEntry,
       "tunnelWiFiConfigLocalAddressType": tunnelWiFiConfigLocalAddressType,
       "tunnelWiFiConfigLocalAddress": tunnelWiFiConfigLocalAddress,
       "tunnelWiFiConfigRemoteAddressType": tunnelWiFiConfigRemoteAddressType,
       "tunnelWiFiConfigRemoteAddress": tunnelWiFiConfigRemoteAddress,
       "tunnelWiFiConfigEncapsMethod": tunnelWiFiConfigEncapsMethod,
       "tunnelWiFiConfigID": tunnelWiFiConfigID,
       "tunnelWiFiConfigIfIndex": tunnelWiFiConfigIfIndex,
       "tunnelWiFiConfigStatus": tunnelWiFiConfigStatus,
       "tunnelWiFiConfigMode": tunnelWiFiConfigMode,
       "tunnelWiFiConfigDefaultProfile": tunnelWiFiConfigDefaultProfile}
)
