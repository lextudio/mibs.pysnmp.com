# SNMP MIB module (COMPAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMPAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:49 2024
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compatible_ObjectIdentity = ObjectIdentity
compatible = _Compatible_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 255)
)
_CompatVars_ObjectIdentity = ObjectIdentity
compatVars = _CompatVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 255, 1)
)
_ProcessorUtilizationPercentage_Type = Gauge32
_ProcessorUtilizationPercentage_Object = MibScalar
processorUtilizationPercentage = _ProcessorUtilizationPercentage_Object(
    (1, 3, 6, 1, 4, 1, 255, 1, 1),
    _ProcessorUtilizationPercentage_Type()
)
processorUtilizationPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorUtilizationPercentage.setStatus("mandatory")
_CompatVPN_ObjectIdentity = ObjectIdentity
compatVPN = _CompatVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 255, 2)
)
_VpnLoginTable_ObjectIdentity = ObjectIdentity
vpnLoginTable = _VpnLoginTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 255, 2, 1)
)
_FailedLogins_Type = Counter32
_FailedLogins_Object = MibScalar
failedLogins = _FailedLogins_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 1, 1),
    _FailedLogins_Type()
)
failedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedLogins.setStatus("mandatory")
_FailedSecurID_Type = Counter32
_FailedSecurID_Object = MibScalar
failedSecurID = _FailedSecurID_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 1, 2),
    _FailedSecurID_Type()
)
failedSecurID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedSecurID.setStatus("mandatory")
_FailedRadiusAuth_Type = Counter32
_FailedRadiusAuth_Object = MibScalar
failedRadiusAuth = _FailedRadiusAuth_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 1, 3),
    _FailedRadiusAuth_Type()
)
failedRadiusAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedRadiusAuth.setStatus("mandatory")
_VPNTunnelTable_ObjectIdentity = ObjectIdentity
vPNTunnelTable = _VPNTunnelTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 255, 2, 2)
)
_VpnTunnelTable_Object = MibTable
vpnTunnelTable = _VpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vpnTunnelTable.setStatus("mandatory")
_VpnTunnelTableEntry_Object = MibTableRow
vpnTunnelTableEntry = _VpnTunnelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1)
)
vpnTunnelTableEntry.setIndexNames(
    (0, "COMPAT-MIB", "vpnTunnelTableIndex"),
)
if mibBuilder.loadTexts:
    vpnTunnelTableEntry.setStatus("mandatory")
_VpnTunnelTableIndex_Type = Integer32
_VpnTunnelTableIndex_Object = MibTableColumn
vpnTunnelTableIndex = _VpnTunnelTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 1),
    _VpnTunnelTableIndex_Type()
)
vpnTunnelTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableIndex.setStatus("mandatory")


class _VpnTunnelTableUserName_Type(DisplayString):
    """Custom type vpnTunnelTableUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VpnTunnelTableUserName_Type.__name__ = "DisplayString"
_VpnTunnelTableUserName_Object = MibTableColumn
vpnTunnelTableUserName = _VpnTunnelTableUserName_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 2),
    _VpnTunnelTableUserName_Type()
)
vpnTunnelTableUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableUserName.setStatus("mandatory")


class _VpnTunnelTableGroupName_Type(DisplayString):
    """Custom type vpnTunnelTableGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VpnTunnelTableGroupName_Type.__name__ = "DisplayString"
_VpnTunnelTableGroupName_Object = MibTableColumn
vpnTunnelTableGroupName = _VpnTunnelTableGroupName_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 3),
    _VpnTunnelTableGroupName_Type()
)
vpnTunnelTableGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableGroupName.setStatus("mandatory")
_VpnTunnelTableIpAddress_Type = IpAddress
_VpnTunnelTableIpAddress_Object = MibTableColumn
vpnTunnelTableIpAddress = _VpnTunnelTableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 4),
    _VpnTunnelTableIpAddress_Type()
)
vpnTunnelTableIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableIpAddress.setStatus("mandatory")
_VpnTunnelTableAssignedIpAddress_Type = IpAddress
_VpnTunnelTableAssignedIpAddress_Object = MibTableColumn
vpnTunnelTableAssignedIpAddress = _VpnTunnelTableAssignedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 5),
    _VpnTunnelTableAssignedIpAddress_Type()
)
vpnTunnelTableAssignedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableAssignedIpAddress.setStatus("mandatory")
_VpnTunnelTableIpBytesRcvd_Type = Counter32
_VpnTunnelTableIpBytesRcvd_Object = MibTableColumn
vpnTunnelTableIpBytesRcvd = _VpnTunnelTableIpBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 6),
    _VpnTunnelTableIpBytesRcvd_Type()
)
vpnTunnelTableIpBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableIpBytesRcvd.setStatus("mandatory")
_VpnTunnelTableIpBytesSent_Type = Counter32
_VpnTunnelTableIpBytesSent_Object = MibTableColumn
vpnTunnelTableIpBytesSent = _VpnTunnelTableIpBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 7),
    _VpnTunnelTableIpBytesSent_Type()
)
vpnTunnelTableIpBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableIpBytesSent.setStatus("mandatory")
_VpnTunnelTableIpxBytesRcvd_Type = Counter32
_VpnTunnelTableIpxBytesRcvd_Object = MibTableColumn
vpnTunnelTableIpxBytesRcvd = _VpnTunnelTableIpxBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 8),
    _VpnTunnelTableIpxBytesRcvd_Type()
)
vpnTunnelTableIpxBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableIpxBytesRcvd.setStatus("mandatory")
_VpnTunnelTableIpxBytesSent_Type = Counter32
_VpnTunnelTableIpxBytesSent_Object = MibTableColumn
vpnTunnelTableIpxBytesSent = _VpnTunnelTableIpxBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 9),
    _VpnTunnelTableIpxBytesSent_Type()
)
vpnTunnelTableIpxBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableIpxBytesSent.setStatus("mandatory")
_VpnTunnelTableAppletalkBytesRcvd_Type = Counter32
_VpnTunnelTableAppletalkBytesRcvd_Object = MibTableColumn
vpnTunnelTableAppletalkBytesRcvd = _VpnTunnelTableAppletalkBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 10),
    _VpnTunnelTableAppletalkBytesRcvd_Type()
)
vpnTunnelTableAppletalkBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableAppletalkBytesRcvd.setStatus("mandatory")
_VpnTunnelTableAppletalkBytesSent_Type = Counter32
_VpnTunnelTableAppletalkBytesSent_Object = MibTableColumn
vpnTunnelTableAppletalkBytesSent = _VpnTunnelTableAppletalkBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 11),
    _VpnTunnelTableAppletalkBytesSent_Type()
)
vpnTunnelTableAppletalkBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableAppletalkBytesSent.setStatus("mandatory")
_VpnTunnelTableUptime_Type = TimeTicks
_VpnTunnelTableUptime_Object = MibTableColumn
vpnTunnelTableUptime = _VpnTunnelTableUptime_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 12),
    _VpnTunnelTableUptime_Type()
)
vpnTunnelTableUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableUptime.setStatus("mandatory")
_VpnTunnelTableLatency_Type = Integer32
_VpnTunnelTableLatency_Object = MibTableColumn
vpnTunnelTableLatency = _VpnTunnelTableLatency_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 13),
    _VpnTunnelTableLatency_Type()
)
vpnTunnelTableLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableLatency.setStatus("mandatory")
_VpnTunnelTableBandwidthOut_Type = Integer32
_VpnTunnelTableBandwidthOut_Object = MibTableColumn
vpnTunnelTableBandwidthOut = _VpnTunnelTableBandwidthOut_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 14),
    _VpnTunnelTableBandwidthOut_Type()
)
vpnTunnelTableBandwidthOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableBandwidthOut.setStatus("mandatory")
_VpnTunnelTableBandwidthReturn_Type = Integer32
_VpnTunnelTableBandwidthReturn_Object = MibTableColumn
vpnTunnelTableBandwidthReturn = _VpnTunnelTableBandwidthReturn_Object(
    (1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 15),
    _VpnTunnelTableBandwidthReturn_Type()
)
vpnTunnelTableBandwidthReturn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelTableBandwidthReturn.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMPAT-MIB",
    **{"DisplayString": DisplayString,
       "compatible": compatible,
       "compatVars": compatVars,
       "processorUtilizationPercentage": processorUtilizationPercentage,
       "compatVPN": compatVPN,
       "vpnLoginTable": vpnLoginTable,
       "failedLogins": failedLogins,
       "failedSecurID": failedSecurID,
       "failedRadiusAuth": failedRadiusAuth,
       "vPNTunnelTable": vPNTunnelTable,
       "vpnTunnelTable": vpnTunnelTable,
       "vpnTunnelTableEntry": vpnTunnelTableEntry,
       "vpnTunnelTableIndex": vpnTunnelTableIndex,
       "vpnTunnelTableUserName": vpnTunnelTableUserName,
       "vpnTunnelTableGroupName": vpnTunnelTableGroupName,
       "vpnTunnelTableIpAddress": vpnTunnelTableIpAddress,
       "vpnTunnelTableAssignedIpAddress": vpnTunnelTableAssignedIpAddress,
       "vpnTunnelTableIpBytesRcvd": vpnTunnelTableIpBytesRcvd,
       "vpnTunnelTableIpBytesSent": vpnTunnelTableIpBytesSent,
       "vpnTunnelTableIpxBytesRcvd": vpnTunnelTableIpxBytesRcvd,
       "vpnTunnelTableIpxBytesSent": vpnTunnelTableIpxBytesSent,
       "vpnTunnelTableAppletalkBytesRcvd": vpnTunnelTableAppletalkBytesRcvd,
       "vpnTunnelTableAppletalkBytesSent": vpnTunnelTableAppletalkBytesSent,
       "vpnTunnelTableUptime": vpnTunnelTableUptime,
       "vpnTunnelTableLatency": vpnTunnelTableLatency,
       "vpnTunnelTableBandwidthOut": vpnTunnelTableBandwidthOut,
       "vpnTunnelTableBandwidthReturn": vpnTunnelTableBandwidthReturn}
)
