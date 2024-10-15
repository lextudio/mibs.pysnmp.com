# SNMP MIB module (POLICY-DEVICE-AUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POLICY-DEVICE-AUX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:10 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

policyDeviceAuxMib = ModuleIdentity(
    (1, 3, 6, 1, 3, 999)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Role(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class RoleCombination(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_PolicyDeviceAuxObjects_ObjectIdentity = ObjectIdentity
policyDeviceAuxObjects = _PolicyDeviceAuxObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 1)
)
_PolicyDeviceConfig_ObjectIdentity = ObjectIdentity
policyDeviceConfig = _PolicyDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 1, 1)
)
_PolicyInterfaceTable_Object = MibTable
policyInterfaceTable = _PolicyInterfaceTable_Object(
    (1, 3, 6, 1, 3, 999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    policyInterfaceTable.setStatus("current")
_PolicyInterfaceEntry_Object = MibTableRow
policyInterfaceEntry = _PolicyInterfaceEntry_Object(
    (1, 3, 6, 1, 3, 999, 1, 1, 1, 1)
)
policyInterfaceEntry.setIndexNames(
    (0, "POLICY-DEVICE-AUX-MIB", "policyInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    policyInterfaceEntry.setStatus("current")
_PolicyInterfaceIfIndex_Type = InterfaceIndex
_PolicyInterfaceIfIndex_Object = MibTableColumn
policyInterfaceIfIndex = _PolicyInterfaceIfIndex_Object(
    (1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 1),
    _PolicyInterfaceIfIndex_Type()
)
policyInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyInterfaceIfIndex.setStatus("current")
_PolicyInterfaceRoleCombo_Type = RoleCombination
_PolicyInterfaceRoleCombo_Object = MibTableColumn
policyInterfaceRoleCombo = _PolicyInterfaceRoleCombo_Object(
    (1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 2),
    _PolicyInterfaceRoleCombo_Type()
)
policyInterfaceRoleCombo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyInterfaceRoleCombo.setStatus("current")


class _PolicyInterfaceStorage_Type(StorageType):
    """Custom type policyInterfaceStorage based on StorageType"""


_PolicyInterfaceStorage_Object = MibTableColumn
policyInterfaceStorage = _PolicyInterfaceStorage_Object(
    (1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 3),
    _PolicyInterfaceStorage_Type()
)
policyInterfaceStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyInterfaceStorage.setStatus("current")
_PolicyInterfaceStatus_Type = RowStatus
_PolicyInterfaceStatus_Object = MibTableColumn
policyInterfaceStatus = _PolicyInterfaceStatus_Object(
    (1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 4),
    _PolicyInterfaceStatus_Type()
)
policyInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyInterfaceStatus.setStatus("current")
_PolicyDeviceAuxConformance_ObjectIdentity = ObjectIdentity
policyDeviceAuxConformance = _PolicyDeviceAuxConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 2)
)
_PolicyDeviceCompliances_ObjectIdentity = ObjectIdentity
policyDeviceCompliances = _PolicyDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 2, 1)
)
_PolicyDeviceGroups_ObjectIdentity = ObjectIdentity
policyDeviceGroups = _PolicyDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 999, 2, 2)
)

# Managed Objects groups

policyInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 999, 2, 2, 1)
)
policyInterfaceGroup.setObjects(
      *(("POLICY-DEVICE-AUX-MIB", "policyInterfaceRoleCombo"),
        ("POLICY-DEVICE-AUX-MIB", "policyInterfaceStorage"),
        ("POLICY-DEVICE-AUX-MIB", "policyInterfaceStatus"))
)
if mibBuilder.loadTexts:
    policyInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

policyDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    policyDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLICY-DEVICE-AUX-MIB",
    **{"Role": Role,
       "RoleCombination": RoleCombination,
       "policyDeviceAuxMib": policyDeviceAuxMib,
       "policyDeviceAuxObjects": policyDeviceAuxObjects,
       "policyDeviceConfig": policyDeviceConfig,
       "policyInterfaceTable": policyInterfaceTable,
       "policyInterfaceEntry": policyInterfaceEntry,
       "policyInterfaceIfIndex": policyInterfaceIfIndex,
       "policyInterfaceRoleCombo": policyInterfaceRoleCombo,
       "policyInterfaceStorage": policyInterfaceStorage,
       "policyInterfaceStatus": policyInterfaceStatus,
       "policyDeviceAuxConformance": policyDeviceAuxConformance,
       "policyDeviceCompliances": policyDeviceCompliances,
       "policyDeviceCompliance": policyDeviceCompliance,
       "policyDeviceGroups": policyDeviceGroups,
       "policyInterfaceGroup": policyInterfaceGroup}
)
