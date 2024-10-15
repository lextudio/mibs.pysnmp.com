# SNMP MIB module (Nortel-Magellan-Passport-IpVrrpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-IpVrrpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:00 2024
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

(vrIp,
 vrIpIndex,
 vrPpIpPort,
 vrPpIpPortIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-IpMIB",
    "vrIp",
    "vrIpIndex",
    "vrPpIpPort",
    "vrPpIpPortIndex")

(DisplayString,
 Integer32,
 MacAddress,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vrIndex,
 vrPpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vrIndex",
    "vrPpIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VrPpIpPortVrrp_ObjectIdentity = ObjectIdentity
vrPpIpPortVrrp = _VrPpIpPortVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17)
)
_VrPpIpPortVrrpRowStatusTable_Object = MibTable
vrPpIpPortVrrpRowStatusTable = _VrPpIpPortVrrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpRowStatusTable.setStatus("mandatory")
_VrPpIpPortVrrpRowStatusEntry_Object = MibTableRow
vrPpIpPortVrrpRowStatusEntry = _VrPpIpPortVrrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 1, 1)
)
vrPpIpPortVrrpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpRowStatusEntry.setStatus("mandatory")
_VrPpIpPortVrrpRowStatus_Type = RowStatus
_VrPpIpPortVrrpRowStatus_Object = MibTableColumn
vrPpIpPortVrrpRowStatus = _VrPpIpPortVrrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 1, 1, 1),
    _VrPpIpPortVrrpRowStatus_Type()
)
vrPpIpPortVrrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpRowStatus.setStatus("mandatory")
_VrPpIpPortVrrpComponentName_Type = DisplayString
_VrPpIpPortVrrpComponentName_Object = MibTableColumn
vrPpIpPortVrrpComponentName = _VrPpIpPortVrrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 1, 1, 2),
    _VrPpIpPortVrrpComponentName_Type()
)
vrPpIpPortVrrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpComponentName.setStatus("mandatory")
_VrPpIpPortVrrpStorageType_Type = StorageType
_VrPpIpPortVrrpStorageType_Object = MibTableColumn
vrPpIpPortVrrpStorageType = _VrPpIpPortVrrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 1, 1, 4),
    _VrPpIpPortVrrpStorageType_Type()
)
vrPpIpPortVrrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpStorageType.setStatus("mandatory")


class _VrPpIpPortVrrpIndex_Type(Integer32):
    """Custom type vrPpIpPortVrrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrPpIpPortVrrpIndex_Type.__name__ = "Integer32"
_VrPpIpPortVrrpIndex_Object = MibTableColumn
vrPpIpPortVrrpIndex = _VrPpIpPortVrrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 1, 1, 10),
    _VrPpIpPortVrrpIndex_Type()
)
vrPpIpPortVrrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpIndex.setStatus("mandatory")
_VrPpIpPortVrrpProvTable_Object = MibTable
vrPpIpPortVrrpProvTable = _VrPpIpPortVrrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 2)
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpProvTable.setStatus("mandatory")
_VrPpIpPortVrrpProvEntry_Object = MibTableRow
vrPpIpPortVrrpProvEntry = _VrPpIpPortVrrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 2, 1)
)
vrPpIpPortVrrpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpProvEntry.setStatus("mandatory")


class _VrPpIpPortVrrpPriority_Type(Unsigned32):
    """Custom type vrPpIpPortVrrpPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrPpIpPortVrrpPriority_Type.__name__ = "Unsigned32"
_VrPpIpPortVrrpPriority_Object = MibTableColumn
vrPpIpPortVrrpPriority = _VrPpIpPortVrrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 2, 1, 1),
    _VrPpIpPortVrrpPriority_Type()
)
vrPpIpPortVrrpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpPriority.setStatus("mandatory")


class _VrPpIpPortVrrpAdvertInterval_Type(Unsigned32):
    """Custom type vrPpIpPortVrrpAdvertInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrPpIpPortVrrpAdvertInterval_Type.__name__ = "Unsigned32"
_VrPpIpPortVrrpAdvertInterval_Object = MibTableColumn
vrPpIpPortVrrpAdvertInterval = _VrPpIpPortVrrpAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 2, 1, 3),
    _VrPpIpPortVrrpAdvertInterval_Type()
)
vrPpIpPortVrrpAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpAdvertInterval.setStatus("mandatory")
_VrPpIpPortVrrpLinkToCriticalIp_Type = Link
_VrPpIpPortVrrpLinkToCriticalIp_Object = MibTableColumn
vrPpIpPortVrrpLinkToCriticalIp = _VrPpIpPortVrrpLinkToCriticalIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 2, 1, 5),
    _VrPpIpPortVrrpLinkToCriticalIp_Type()
)
vrPpIpPortVrrpLinkToCriticalIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpLinkToCriticalIp.setStatus("mandatory")
_VrPpIpPortVrrpOperTable_Object = MibTable
vrPpIpPortVrrpOperTable = _VrPpIpPortVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 13)
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpOperTable.setStatus("mandatory")
_VrPpIpPortVrrpOperEntry_Object = MibTableRow
vrPpIpPortVrrpOperEntry = _VrPpIpPortVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 13, 1)
)
vrPpIpPortVrrpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpOperEntry.setStatus("mandatory")


class _VrPpIpPortVrrpVirtualRouterState_Type(Integer32):
    """Custom type vrPpIpPortVrrpVirtualRouterState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("initialize", 0),
          ("master", 2))
    )


_VrPpIpPortVrrpVirtualRouterState_Type.__name__ = "Integer32"
_VrPpIpPortVrrpVirtualRouterState_Object = MibTableColumn
vrPpIpPortVrrpVirtualRouterState = _VrPpIpPortVrrpVirtualRouterState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 13, 1, 1),
    _VrPpIpPortVrrpVirtualRouterState_Type()
)
vrPpIpPortVrrpVirtualRouterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpVirtualRouterState.setStatus("mandatory")


class _VrPpIpPortVrrpVirtualRouterPhysicalAddress_Type(MacAddress):
    """Custom type vrPpIpPortVrrpVirtualRouterPhysicalAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrPpIpPortVrrpVirtualRouterPhysicalAddress_Type.__name__ = "MacAddress"
_VrPpIpPortVrrpVirtualRouterPhysicalAddress_Object = MibTableColumn
vrPpIpPortVrrpVirtualRouterPhysicalAddress = _VrPpIpPortVrrpVirtualRouterPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 13, 1, 2),
    _VrPpIpPortVrrpVirtualRouterPhysicalAddress_Type()
)
vrPpIpPortVrrpVirtualRouterPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpVirtualRouterPhysicalAddress.setStatus("mandatory")
_VrPpIpPortVrrpAdminControlTable_Object = MibTable
vrPpIpPortVrrpAdminControlTable = _VrPpIpPortVrrpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 30)
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpAdminControlTable.setStatus("mandatory")
_VrPpIpPortVrrpAdminControlEntry_Object = MibTableRow
vrPpIpPortVrrpAdminControlEntry = _VrPpIpPortVrrpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 30, 1)
)
vrPpIpPortVrrpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpAdminControlEntry.setStatus("mandatory")


class _VrPpIpPortVrrpSnmpAdminStatus_Type(Integer32):
    """Custom type vrPpIpPortVrrpSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_VrPpIpPortVrrpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrPpIpPortVrrpSnmpAdminStatus_Object = MibTableColumn
vrPpIpPortVrrpSnmpAdminStatus = _VrPpIpPortVrrpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 30, 1, 1),
    _VrPpIpPortVrrpSnmpAdminStatus_Type()
)
vrPpIpPortVrrpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpSnmpAdminStatus.setStatus("mandatory")
_VrPpIpPortVrrpOperStatusTable_Object = MibTable
vrPpIpPortVrrpOperStatusTable = _VrPpIpPortVrrpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 31)
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpOperStatusTable.setStatus("mandatory")
_VrPpIpPortVrrpOperStatusEntry_Object = MibTableRow
vrPpIpPortVrrpOperStatusEntry = _VrPpIpPortVrrpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 31, 1)
)
vrPpIpPortVrrpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpOperStatusEntry.setStatus("mandatory")


class _VrPpIpPortVrrpSnmpOperStatus_Type(Integer32):
    """Custom type vrPpIpPortVrrpSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_VrPpIpPortVrrpSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpIpPortVrrpSnmpOperStatus_Object = MibTableColumn
vrPpIpPortVrrpSnmpOperStatus = _VrPpIpPortVrrpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 31, 1, 1),
    _VrPpIpPortVrrpSnmpOperStatus_Type()
)
vrPpIpPortVrrpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpSnmpOperStatus.setStatus("mandatory")
_VrPpIpPortVrrpStateTable_Object = MibTable
vrPpIpPortVrrpStateTable = _VrPpIpPortVrrpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 32)
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpStateTable.setStatus("mandatory")
_VrPpIpPortVrrpStateEntry_Object = MibTableRow
vrPpIpPortVrrpStateEntry = _VrPpIpPortVrrpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 32, 1)
)
vrPpIpPortVrrpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpStateEntry.setStatus("mandatory")


class _VrPpIpPortVrrpAdminState_Type(Integer32):
    """Custom type vrPpIpPortVrrpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_VrPpIpPortVrrpAdminState_Type.__name__ = "Integer32"
_VrPpIpPortVrrpAdminState_Object = MibTableColumn
vrPpIpPortVrrpAdminState = _VrPpIpPortVrrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 32, 1, 1),
    _VrPpIpPortVrrpAdminState_Type()
)
vrPpIpPortVrrpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpAdminState.setStatus("mandatory")


class _VrPpIpPortVrrpOperationalState_Type(Integer32):
    """Custom type vrPpIpPortVrrpOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VrPpIpPortVrrpOperationalState_Type.__name__ = "Integer32"
_VrPpIpPortVrrpOperationalState_Object = MibTableColumn
vrPpIpPortVrrpOperationalState = _VrPpIpPortVrrpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 32, 1, 2),
    _VrPpIpPortVrrpOperationalState_Type()
)
vrPpIpPortVrrpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpOperationalState.setStatus("mandatory")


class _VrPpIpPortVrrpUsageState_Type(Integer32):
    """Custom type vrPpIpPortVrrpUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_VrPpIpPortVrrpUsageState_Type.__name__ = "Integer32"
_VrPpIpPortVrrpUsageState_Object = MibTableColumn
vrPpIpPortVrrpUsageState = _VrPpIpPortVrrpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 32, 1, 3),
    _VrPpIpPortVrrpUsageState_Type()
)
vrPpIpPortVrrpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpUsageState.setStatus("mandatory")
_VrPpIpPortVrrpIpAddressesTable_Object = MibTable
vrPpIpPortVrrpIpAddressesTable = _VrPpIpPortVrrpIpAddressesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 700)
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpIpAddressesTable.setStatus("mandatory")
_VrPpIpPortVrrpIpAddressesEntry_Object = MibTableRow
vrPpIpPortVrrpIpAddressesEntry = _VrPpIpPortVrrpIpAddressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 700, 1)
)
vrPpIpPortVrrpIpAddressesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortVrrpIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortVrrpIpAddressesValue"),
)
if mibBuilder.loadTexts:
    vrPpIpPortVrrpIpAddressesEntry.setStatus("mandatory")
_VrPpIpPortVrrpIpAddressesValue_Type = IpAddress
_VrPpIpPortVrrpIpAddressesValue_Object = MibTableColumn
vrPpIpPortVrrpIpAddressesValue = _VrPpIpPortVrrpIpAddressesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 700, 1, 1),
    _VrPpIpPortVrrpIpAddressesValue_Type()
)
vrPpIpPortVrrpIpAddressesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpIpAddressesValue.setStatus("mandatory")
_VrPpIpPortVrrpIpAddressesRowStatus_Type = RowStatus
_VrPpIpPortVrrpIpAddressesRowStatus_Object = MibTableColumn
vrPpIpPortVrrpIpAddressesRowStatus = _VrPpIpPortVrrpIpAddressesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 17, 700, 1, 2),
    _VrPpIpPortVrrpIpAddressesRowStatus_Type()
)
vrPpIpPortVrrpIpAddressesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrPpIpPortVrrpIpAddressesRowStatus.setStatus("mandatory")
_VrPpIpPortCriticalIp_ObjectIdentity = ObjectIdentity
vrPpIpPortCriticalIp = _VrPpIpPortCriticalIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18)
)
_VrPpIpPortCriticalIpRowStatusTable_Object = MibTable
vrPpIpPortCriticalIpRowStatusTable = _VrPpIpPortCriticalIpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpRowStatusTable.setStatus("mandatory")
_VrPpIpPortCriticalIpRowStatusEntry_Object = MibTableRow
vrPpIpPortCriticalIpRowStatusEntry = _VrPpIpPortCriticalIpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 1, 1)
)
vrPpIpPortCriticalIpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortCriticalIpIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpRowStatusEntry.setStatus("mandatory")
_VrPpIpPortCriticalIpRowStatus_Type = RowStatus
_VrPpIpPortCriticalIpRowStatus_Object = MibTableColumn
vrPpIpPortCriticalIpRowStatus = _VrPpIpPortCriticalIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 1, 1, 1),
    _VrPpIpPortCriticalIpRowStatus_Type()
)
vrPpIpPortCriticalIpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpRowStatus.setStatus("mandatory")
_VrPpIpPortCriticalIpComponentName_Type = DisplayString
_VrPpIpPortCriticalIpComponentName_Object = MibTableColumn
vrPpIpPortCriticalIpComponentName = _VrPpIpPortCriticalIpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 1, 1, 2),
    _VrPpIpPortCriticalIpComponentName_Type()
)
vrPpIpPortCriticalIpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpComponentName.setStatus("mandatory")
_VrPpIpPortCriticalIpStorageType_Type = StorageType
_VrPpIpPortCriticalIpStorageType_Object = MibTableColumn
vrPpIpPortCriticalIpStorageType = _VrPpIpPortCriticalIpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 1, 1, 4),
    _VrPpIpPortCriticalIpStorageType_Type()
)
vrPpIpPortCriticalIpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpStorageType.setStatus("mandatory")


class _VrPpIpPortCriticalIpIndex_Type(Integer32):
    """Custom type vrPpIpPortCriticalIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrPpIpPortCriticalIpIndex_Type.__name__ = "Integer32"
_VrPpIpPortCriticalIpIndex_Object = MibTableColumn
vrPpIpPortCriticalIpIndex = _VrPpIpPortCriticalIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 1, 1, 10),
    _VrPpIpPortCriticalIpIndex_Type()
)
vrPpIpPortCriticalIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpIndex.setStatus("mandatory")
_VrPpIpPortCriticalIpProvTable_Object = MibTable
vrPpIpPortCriticalIpProvTable = _VrPpIpPortCriticalIpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 24)
)
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpProvTable.setStatus("mandatory")
_VrPpIpPortCriticalIpProvEntry_Object = MibTableRow
vrPpIpPortCriticalIpProvEntry = _VrPpIpPortCriticalIpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 24, 1)
)
vrPpIpPortCriticalIpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrPpIpPortCriticalIpIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpProvEntry.setStatus("mandatory")
_VrPpIpPortCriticalIpLinkToVrrp_Type = Link
_VrPpIpPortCriticalIpLinkToVrrp_Object = MibTableColumn
vrPpIpPortCriticalIpLinkToVrrp = _VrPpIpPortCriticalIpLinkToVrrp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 18, 24, 1, 1),
    _VrPpIpPortCriticalIpLinkToVrrp_Type()
)
vrPpIpPortCriticalIpLinkToVrrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortCriticalIpLinkToVrrp.setStatus("mandatory")
_VrIpIpVrrp_ObjectIdentity = ObjectIdentity
vrIpIpVrrp = _VrIpIpVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25)
)
_VrIpIpVrrpRowStatusTable_Object = MibTable
vrIpIpVrrpRowStatusTable = _VrIpIpVrrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 1)
)
if mibBuilder.loadTexts:
    vrIpIpVrrpRowStatusTable.setStatus("mandatory")
_VrIpIpVrrpRowStatusEntry_Object = MibTableRow
vrIpIpVrrpRowStatusEntry = _VrIpIpVrrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 1, 1)
)
vrIpIpVrrpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrIpIpVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpIpVrrpRowStatusEntry.setStatus("mandatory")
_VrIpIpVrrpRowStatus_Type = RowStatus
_VrIpIpVrrpRowStatus_Object = MibTableColumn
vrIpIpVrrpRowStatus = _VrIpIpVrrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 1, 1, 1),
    _VrIpIpVrrpRowStatus_Type()
)
vrIpIpVrrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpIpVrrpRowStatus.setStatus("mandatory")
_VrIpIpVrrpComponentName_Type = DisplayString
_VrIpIpVrrpComponentName_Object = MibTableColumn
vrIpIpVrrpComponentName = _VrIpIpVrrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 1, 1, 2),
    _VrIpIpVrrpComponentName_Type()
)
vrIpIpVrrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIpVrrpComponentName.setStatus("mandatory")
_VrIpIpVrrpStorageType_Type = StorageType
_VrIpIpVrrpStorageType_Object = MibTableColumn
vrIpIpVrrpStorageType = _VrIpIpVrrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 1, 1, 4),
    _VrIpIpVrrpStorageType_Type()
)
vrIpIpVrrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIpVrrpStorageType.setStatus("mandatory")
_VrIpIpVrrpIndex_Type = NonReplicated
_VrIpIpVrrpIndex_Object = MibTableColumn
vrIpIpVrrpIndex = _VrIpIpVrrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 1, 1, 10),
    _VrIpIpVrrpIndex_Type()
)
vrIpIpVrrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpIpVrrpIndex.setStatus("mandatory")
_VrIpIpVrrpAdminControlTable_Object = MibTable
vrIpIpVrrpAdminControlTable = _VrIpIpVrrpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 30)
)
if mibBuilder.loadTexts:
    vrIpIpVrrpAdminControlTable.setStatus("mandatory")
_VrIpIpVrrpAdminControlEntry_Object = MibTableRow
vrIpIpVrrpAdminControlEntry = _VrIpIpVrrpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 30, 1)
)
vrIpIpVrrpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrIpIpVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpIpVrrpAdminControlEntry.setStatus("mandatory")


class _VrIpIpVrrpSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpIpVrrpSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_VrIpIpVrrpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpIpVrrpSnmpAdminStatus_Object = MibTableColumn
vrIpIpVrrpSnmpAdminStatus = _VrIpIpVrrpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 30, 1, 1),
    _VrIpIpVrrpSnmpAdminStatus_Type()
)
vrIpIpVrrpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpIpVrrpSnmpAdminStatus.setStatus("mandatory")
_VrIpIpVrrpOperStatusTable_Object = MibTable
vrIpIpVrrpOperStatusTable = _VrIpIpVrrpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 31)
)
if mibBuilder.loadTexts:
    vrIpIpVrrpOperStatusTable.setStatus("mandatory")
_VrIpIpVrrpOperStatusEntry_Object = MibTableRow
vrIpIpVrrpOperStatusEntry = _VrIpIpVrrpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 31, 1)
)
vrIpIpVrrpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrIpIpVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpIpVrrpOperStatusEntry.setStatus("mandatory")


class _VrIpIpVrrpSnmpOperStatus_Type(Integer32):
    """Custom type vrIpIpVrrpSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_VrIpIpVrrpSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpIpVrrpSnmpOperStatus_Object = MibTableColumn
vrIpIpVrrpSnmpOperStatus = _VrIpIpVrrpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 31, 1, 1),
    _VrIpIpVrrpSnmpOperStatus_Type()
)
vrIpIpVrrpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIpVrrpSnmpOperStatus.setStatus("mandatory")
_VrIpIpVrrpStateTable_Object = MibTable
vrIpIpVrrpStateTable = _VrIpIpVrrpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 32)
)
if mibBuilder.loadTexts:
    vrIpIpVrrpStateTable.setStatus("mandatory")
_VrIpIpVrrpStateEntry_Object = MibTableRow
vrIpIpVrrpStateEntry = _VrIpIpVrrpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 32, 1)
)
vrIpIpVrrpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpVrrpMIB", "vrIpIpVrrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpIpVrrpStateEntry.setStatus("mandatory")


class _VrIpIpVrrpAdminState_Type(Integer32):
    """Custom type vrIpIpVrrpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_VrIpIpVrrpAdminState_Type.__name__ = "Integer32"
_VrIpIpVrrpAdminState_Object = MibTableColumn
vrIpIpVrrpAdminState = _VrIpIpVrrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 32, 1, 1),
    _VrIpIpVrrpAdminState_Type()
)
vrIpIpVrrpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIpVrrpAdminState.setStatus("mandatory")


class _VrIpIpVrrpOperationalState_Type(Integer32):
    """Custom type vrIpIpVrrpOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VrIpIpVrrpOperationalState_Type.__name__ = "Integer32"
_VrIpIpVrrpOperationalState_Object = MibTableColumn
vrIpIpVrrpOperationalState = _VrIpIpVrrpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 32, 1, 2),
    _VrIpIpVrrpOperationalState_Type()
)
vrIpIpVrrpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIpVrrpOperationalState.setStatus("mandatory")


class _VrIpIpVrrpUsageState_Type(Integer32):
    """Custom type vrIpIpVrrpUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_VrIpIpVrrpUsageState_Type.__name__ = "Integer32"
_VrIpIpVrrpUsageState_Object = MibTableColumn
vrIpIpVrrpUsageState = _VrIpIpVrrpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 25, 32, 1, 3),
    _VrIpIpVrrpUsageState_Type()
)
vrIpIpVrrpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIpVrrpUsageState.setStatus("mandatory")
_IpVrrpMIB_ObjectIdentity = ObjectIdentity
ipVrrpMIB = _IpVrrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161)
)
_IpVrrpGroup_ObjectIdentity = ObjectIdentity
ipVrrpGroup = _IpVrrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161, 1)
)
_IpVrrpGroupBG_ObjectIdentity = ObjectIdentity
ipVrrpGroupBG = _IpVrrpGroupBG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161, 1, 7)
)
_IpVrrpGroupBG00_ObjectIdentity = ObjectIdentity
ipVrrpGroupBG00 = _IpVrrpGroupBG00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161, 1, 7, 1)
)
_IpVrrpGroupBG00A_ObjectIdentity = ObjectIdentity
ipVrrpGroupBG00A = _IpVrrpGroupBG00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161, 1, 7, 1, 2)
)
_IpVrrpCapabilities_ObjectIdentity = ObjectIdentity
ipVrrpCapabilities = _IpVrrpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161, 3)
)
_IpVrrpCapabilitiesBG_ObjectIdentity = ObjectIdentity
ipVrrpCapabilitiesBG = _IpVrrpCapabilitiesBG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161, 3, 7)
)
_IpVrrpCapabilitiesBG00_ObjectIdentity = ObjectIdentity
ipVrrpCapabilitiesBG00 = _IpVrrpCapabilitiesBG00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161, 3, 7, 1)
)
_IpVrrpCapabilitiesBG00A_ObjectIdentity = ObjectIdentity
ipVrrpCapabilitiesBG00A = _IpVrrpCapabilitiesBG00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 161, 3, 7, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-IpVrrpMIB",
    **{"vrPpIpPortVrrp": vrPpIpPortVrrp,
       "vrPpIpPortVrrpRowStatusTable": vrPpIpPortVrrpRowStatusTable,
       "vrPpIpPortVrrpRowStatusEntry": vrPpIpPortVrrpRowStatusEntry,
       "vrPpIpPortVrrpRowStatus": vrPpIpPortVrrpRowStatus,
       "vrPpIpPortVrrpComponentName": vrPpIpPortVrrpComponentName,
       "vrPpIpPortVrrpStorageType": vrPpIpPortVrrpStorageType,
       "vrPpIpPortVrrpIndex": vrPpIpPortVrrpIndex,
       "vrPpIpPortVrrpProvTable": vrPpIpPortVrrpProvTable,
       "vrPpIpPortVrrpProvEntry": vrPpIpPortVrrpProvEntry,
       "vrPpIpPortVrrpPriority": vrPpIpPortVrrpPriority,
       "vrPpIpPortVrrpAdvertInterval": vrPpIpPortVrrpAdvertInterval,
       "vrPpIpPortVrrpLinkToCriticalIp": vrPpIpPortVrrpLinkToCriticalIp,
       "vrPpIpPortVrrpOperTable": vrPpIpPortVrrpOperTable,
       "vrPpIpPortVrrpOperEntry": vrPpIpPortVrrpOperEntry,
       "vrPpIpPortVrrpVirtualRouterState": vrPpIpPortVrrpVirtualRouterState,
       "vrPpIpPortVrrpVirtualRouterPhysicalAddress": vrPpIpPortVrrpVirtualRouterPhysicalAddress,
       "vrPpIpPortVrrpAdminControlTable": vrPpIpPortVrrpAdminControlTable,
       "vrPpIpPortVrrpAdminControlEntry": vrPpIpPortVrrpAdminControlEntry,
       "vrPpIpPortVrrpSnmpAdminStatus": vrPpIpPortVrrpSnmpAdminStatus,
       "vrPpIpPortVrrpOperStatusTable": vrPpIpPortVrrpOperStatusTable,
       "vrPpIpPortVrrpOperStatusEntry": vrPpIpPortVrrpOperStatusEntry,
       "vrPpIpPortVrrpSnmpOperStatus": vrPpIpPortVrrpSnmpOperStatus,
       "vrPpIpPortVrrpStateTable": vrPpIpPortVrrpStateTable,
       "vrPpIpPortVrrpStateEntry": vrPpIpPortVrrpStateEntry,
       "vrPpIpPortVrrpAdminState": vrPpIpPortVrrpAdminState,
       "vrPpIpPortVrrpOperationalState": vrPpIpPortVrrpOperationalState,
       "vrPpIpPortVrrpUsageState": vrPpIpPortVrrpUsageState,
       "vrPpIpPortVrrpIpAddressesTable": vrPpIpPortVrrpIpAddressesTable,
       "vrPpIpPortVrrpIpAddressesEntry": vrPpIpPortVrrpIpAddressesEntry,
       "vrPpIpPortVrrpIpAddressesValue": vrPpIpPortVrrpIpAddressesValue,
       "vrPpIpPortVrrpIpAddressesRowStatus": vrPpIpPortVrrpIpAddressesRowStatus,
       "vrPpIpPortCriticalIp": vrPpIpPortCriticalIp,
       "vrPpIpPortCriticalIpRowStatusTable": vrPpIpPortCriticalIpRowStatusTable,
       "vrPpIpPortCriticalIpRowStatusEntry": vrPpIpPortCriticalIpRowStatusEntry,
       "vrPpIpPortCriticalIpRowStatus": vrPpIpPortCriticalIpRowStatus,
       "vrPpIpPortCriticalIpComponentName": vrPpIpPortCriticalIpComponentName,
       "vrPpIpPortCriticalIpStorageType": vrPpIpPortCriticalIpStorageType,
       "vrPpIpPortCriticalIpIndex": vrPpIpPortCriticalIpIndex,
       "vrPpIpPortCriticalIpProvTable": vrPpIpPortCriticalIpProvTable,
       "vrPpIpPortCriticalIpProvEntry": vrPpIpPortCriticalIpProvEntry,
       "vrPpIpPortCriticalIpLinkToVrrp": vrPpIpPortCriticalIpLinkToVrrp,
       "vrIpIpVrrp": vrIpIpVrrp,
       "vrIpIpVrrpRowStatusTable": vrIpIpVrrpRowStatusTable,
       "vrIpIpVrrpRowStatusEntry": vrIpIpVrrpRowStatusEntry,
       "vrIpIpVrrpRowStatus": vrIpIpVrrpRowStatus,
       "vrIpIpVrrpComponentName": vrIpIpVrrpComponentName,
       "vrIpIpVrrpStorageType": vrIpIpVrrpStorageType,
       "vrIpIpVrrpIndex": vrIpIpVrrpIndex,
       "vrIpIpVrrpAdminControlTable": vrIpIpVrrpAdminControlTable,
       "vrIpIpVrrpAdminControlEntry": vrIpIpVrrpAdminControlEntry,
       "vrIpIpVrrpSnmpAdminStatus": vrIpIpVrrpSnmpAdminStatus,
       "vrIpIpVrrpOperStatusTable": vrIpIpVrrpOperStatusTable,
       "vrIpIpVrrpOperStatusEntry": vrIpIpVrrpOperStatusEntry,
       "vrIpIpVrrpSnmpOperStatus": vrIpIpVrrpSnmpOperStatus,
       "vrIpIpVrrpStateTable": vrIpIpVrrpStateTable,
       "vrIpIpVrrpStateEntry": vrIpIpVrrpStateEntry,
       "vrIpIpVrrpAdminState": vrIpIpVrrpAdminState,
       "vrIpIpVrrpOperationalState": vrIpIpVrrpOperationalState,
       "vrIpIpVrrpUsageState": vrIpIpVrrpUsageState,
       "ipVrrpMIB": ipVrrpMIB,
       "ipVrrpGroup": ipVrrpGroup,
       "ipVrrpGroupBG": ipVrrpGroupBG,
       "ipVrrpGroupBG00": ipVrrpGroupBG00,
       "ipVrrpGroupBG00A": ipVrrpGroupBG00A,
       "ipVrrpCapabilities": ipVrrpCapabilities,
       "ipVrrpCapabilitiesBG": ipVrrpCapabilitiesBG,
       "ipVrrpCapabilitiesBG00": ipVrrpCapabilitiesBG00,
       "ipVrrpCapabilitiesBG00A": ipVrrpCapabilitiesBG00A}
)
