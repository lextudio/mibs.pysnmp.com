# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:44 2024
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

(lhnModules,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules")

(lhnNusCommonNetwork,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    "lhnNusCommonNetwork")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lhnNusCommonNetworkModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetworkDeviceCount_Type = Integer32
_NetworkDeviceCount_Object = MibScalar
networkDeviceCount = _NetworkDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 1),
    _NetworkDeviceCount_Type()
)
networkDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceCount.setStatus("current")
_NetworkDeviceTable_Object = MibTable
networkDeviceTable = _NetworkDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    networkDeviceTable.setStatus("current")
_NetworkDeviceEntry_Object = MibTableRow
networkDeviceEntry = _NetworkDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1)
)
networkDeviceEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-NETWORK-MIB", "networkIndex"),
)
if mibBuilder.loadTexts:
    networkDeviceEntry.setStatus("current")
_NetworkDeviceIndex_Type = Integer32
_NetworkDeviceIndex_Object = MibTableColumn
networkDeviceIndex = _NetworkDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 1),
    _NetworkDeviceIndex_Type()
)
networkDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceIndex.setStatus("current")
_NetworkDeviceName_Type = OctetString
_NetworkDeviceName_Object = MibTableColumn
networkDeviceName = _NetworkDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 6),
    _NetworkDeviceName_Type()
)
networkDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceName.setStatus("current")
_NetworkDeviceIpAddress_Type = IpAddress
_NetworkDeviceIpAddress_Object = MibTableColumn
networkDeviceIpAddress = _NetworkDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 7),
    _NetworkDeviceIpAddress_Type()
)
networkDeviceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkDeviceIpAddress.setStatus("current")
_NetworkDeviceMask_Type = IpAddress
_NetworkDeviceMask_Object = MibTableColumn
networkDeviceMask = _NetworkDeviceMask_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 8),
    _NetworkDeviceMask_Type()
)
networkDeviceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkDeviceMask.setStatus("current")
_NetworkDeviceDefaultGateway_Type = IpAddress
_NetworkDeviceDefaultGateway_Object = MibTableColumn
networkDeviceDefaultGateway = _NetworkDeviceDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 9),
    _NetworkDeviceDefaultGateway_Type()
)
networkDeviceDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkDeviceDefaultGateway.setStatus("current")


class _NetworkDeviceMode_Type(Integer32):
    """Custom type networkDeviceMode based on Integer32"""
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
        *(("auto", 2),
          ("disabled", 1),
          ("slave", 4),
          ("static", 3))
    )


_NetworkDeviceMode_Type.__name__ = "Integer32"
_NetworkDeviceMode_Object = MibTableColumn
networkDeviceMode = _NetworkDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 10),
    _NetworkDeviceMode_Type()
)
networkDeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkDeviceMode.setStatus("current")
_NetworkDeviceStatus_Type = OctetString
_NetworkDeviceStatus_Object = MibTableColumn
networkDeviceStatus = _NetworkDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 11),
    _NetworkDeviceStatus_Type()
)
networkDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-NETWORK-MIB",
    **{"lhnNusCommonNetworkModule": lhnNusCommonNetworkModule,
       "networkDeviceCount": networkDeviceCount,
       "networkDeviceTable": networkDeviceTable,
       "networkDeviceEntry": networkDeviceEntry,
       "networkDeviceIndex": networkDeviceIndex,
       "networkDeviceName": networkDeviceName,
       "networkDeviceIpAddress": networkDeviceIpAddress,
       "networkDeviceMask": networkDeviceMask,
       "networkDeviceDefaultGateway": networkDeviceDefaultGateway,
       "networkDeviceMode": networkDeviceMode,
       "networkDeviceStatus": networkDeviceStatus}
)
