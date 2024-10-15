# SNMP MIB module (Nortel-Magellan-Passport-VirtualMediaMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VirtualMediaMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:33 2024
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

(DisplayString,
 Integer32,
 InterfaceIndex,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "Link")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_Vm_ObjectIdentity = ObjectIdentity
vm = _Vm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133)
)
_VmRowStatusTable_Object = MibTable
vmRowStatusTable = _VmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1)
)
if mibBuilder.loadTexts:
    vmRowStatusTable.setStatus("mandatory")
_VmRowStatusEntry_Object = MibTableRow
vmRowStatusEntry = _VmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1)
)
vmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"),
)
if mibBuilder.loadTexts:
    vmRowStatusEntry.setStatus("mandatory")
_VmRowStatus_Type = RowStatus
_VmRowStatus_Object = MibTableColumn
vmRowStatus = _VmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1, 1),
    _VmRowStatus_Type()
)
vmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmRowStatus.setStatus("mandatory")
_VmComponentName_Type = DisplayString
_VmComponentName_Object = MibTableColumn
vmComponentName = _VmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1, 2),
    _VmComponentName_Type()
)
vmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmComponentName.setStatus("mandatory")
_VmStorageType_Type = StorageType
_VmStorageType_Object = MibTableColumn
vmStorageType = _VmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1, 4),
    _VmStorageType_Type()
)
vmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStorageType.setStatus("mandatory")


class _VmIndex_Type(Integer32):
    """Custom type vmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VmIndex_Type.__name__ = "Integer32"
_VmIndex_Object = MibTableColumn
vmIndex = _VmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1, 10),
    _VmIndex_Type()
)
vmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmIndex.setStatus("mandatory")
_VmIf_ObjectIdentity = ObjectIdentity
vmIf = _VmIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2)
)
_VmIfRowStatusTable_Object = MibTable
vmIfRowStatusTable = _VmIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1)
)
if mibBuilder.loadTexts:
    vmIfRowStatusTable.setStatus("mandatory")
_VmIfRowStatusEntry_Object = MibTableRow
vmIfRowStatusEntry = _VmIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1)
)
vmIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"),
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"),
)
if mibBuilder.loadTexts:
    vmIfRowStatusEntry.setStatus("mandatory")
_VmIfRowStatus_Type = RowStatus
_VmIfRowStatus_Object = MibTableColumn
vmIfRowStatus = _VmIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1, 1),
    _VmIfRowStatus_Type()
)
vmIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmIfRowStatus.setStatus("mandatory")
_VmIfComponentName_Type = DisplayString
_VmIfComponentName_Object = MibTableColumn
vmIfComponentName = _VmIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1, 2),
    _VmIfComponentName_Type()
)
vmIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIfComponentName.setStatus("mandatory")
_VmIfStorageType_Type = StorageType
_VmIfStorageType_Object = MibTableColumn
vmIfStorageType = _VmIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1, 4),
    _VmIfStorageType_Type()
)
vmIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIfStorageType.setStatus("mandatory")


class _VmIfIndex_Type(Integer32):
    """Custom type vmIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VmIfIndex_Type.__name__ = "Integer32"
_VmIfIndex_Object = MibTableColumn
vmIfIndex = _VmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1, 10),
    _VmIfIndex_Type()
)
vmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmIfIndex.setStatus("mandatory")
_VmIfMpTable_Object = MibTable
vmIfMpTable = _VmIfMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 10)
)
if mibBuilder.loadTexts:
    vmIfMpTable.setStatus("mandatory")
_VmIfMpEntry_Object = MibTableRow
vmIfMpEntry = _VmIfMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 10, 1)
)
vmIfMpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"),
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"),
)
if mibBuilder.loadTexts:
    vmIfMpEntry.setStatus("mandatory")
_VmIfLinkToProtocolPort_Type = Link
_VmIfLinkToProtocolPort_Object = MibTableColumn
vmIfLinkToProtocolPort = _VmIfLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 10, 1, 1),
    _VmIfLinkToProtocolPort_Type()
)
vmIfLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmIfLinkToProtocolPort.setStatus("mandatory")
_VmIfCidDataTable_Object = MibTable
vmIfCidDataTable = _VmIfCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 11)
)
if mibBuilder.loadTexts:
    vmIfCidDataTable.setStatus("mandatory")
_VmIfCidDataEntry_Object = MibTableRow
vmIfCidDataEntry = _VmIfCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 11, 1)
)
vmIfCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"),
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"),
)
if mibBuilder.loadTexts:
    vmIfCidDataEntry.setStatus("mandatory")


class _VmIfCustomerIdentifier_Type(Unsigned32):
    """Custom type vmIfCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_VmIfCustomerIdentifier_Type.__name__ = "Unsigned32"
_VmIfCustomerIdentifier_Object = MibTableColumn
vmIfCustomerIdentifier = _VmIfCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 11, 1, 1),
    _VmIfCustomerIdentifier_Type()
)
vmIfCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmIfCustomerIdentifier.setStatus("mandatory")
_VmIfIfEntryTable_Object = MibTable
vmIfIfEntryTable = _VmIfIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 12)
)
if mibBuilder.loadTexts:
    vmIfIfEntryTable.setStatus("mandatory")
_VmIfIfEntryEntry_Object = MibTableRow
vmIfIfEntryEntry = _VmIfIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 12, 1)
)
vmIfIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"),
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"),
)
if mibBuilder.loadTexts:
    vmIfIfEntryEntry.setStatus("mandatory")


class _VmIfIfAdminStatus_Type(Integer32):
    """Custom type vmIfIfAdminStatus based on Integer32"""
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


_VmIfIfAdminStatus_Type.__name__ = "Integer32"
_VmIfIfAdminStatus_Object = MibTableColumn
vmIfIfAdminStatus = _VmIfIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 12, 1, 1),
    _VmIfIfAdminStatus_Type()
)
vmIfIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmIfIfAdminStatus.setStatus("mandatory")


class _VmIfIfIndex_Type(InterfaceIndex):
    """Custom type vmIfIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VmIfIfIndex_Type.__name__ = "InterfaceIndex"
_VmIfIfIndex_Object = MibTableColumn
vmIfIfIndex = _VmIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 12, 1, 2),
    _VmIfIfIndex_Type()
)
vmIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIfIfIndex.setStatus("mandatory")
_VmIfOperStatusTable_Object = MibTable
vmIfOperStatusTable = _VmIfOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 13)
)
if mibBuilder.loadTexts:
    vmIfOperStatusTable.setStatus("mandatory")
_VmIfOperStatusEntry_Object = MibTableRow
vmIfOperStatusEntry = _VmIfOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 13, 1)
)
vmIfOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"),
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"),
)
if mibBuilder.loadTexts:
    vmIfOperStatusEntry.setStatus("mandatory")


class _VmIfSnmpOperStatus_Type(Integer32):
    """Custom type vmIfSnmpOperStatus based on Integer32"""
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


_VmIfSnmpOperStatus_Type.__name__ = "Integer32"
_VmIfSnmpOperStatus_Object = MibTableColumn
vmIfSnmpOperStatus = _VmIfSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 13, 1, 1),
    _VmIfSnmpOperStatus_Type()
)
vmIfSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIfSnmpOperStatus.setStatus("mandatory")
_VmIfStateTable_Object = MibTable
vmIfStateTable = _VmIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14)
)
if mibBuilder.loadTexts:
    vmIfStateTable.setStatus("mandatory")
_VmIfStateEntry_Object = MibTableRow
vmIfStateEntry = _VmIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14, 1)
)
vmIfStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"),
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"),
)
if mibBuilder.loadTexts:
    vmIfStateEntry.setStatus("mandatory")


class _VmIfAdminState_Type(Integer32):
    """Custom type vmIfAdminState based on Integer32"""
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


_VmIfAdminState_Type.__name__ = "Integer32"
_VmIfAdminState_Object = MibTableColumn
vmIfAdminState = _VmIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14, 1, 1),
    _VmIfAdminState_Type()
)
vmIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIfAdminState.setStatus("mandatory")


class _VmIfOperationalState_Type(Integer32):
    """Custom type vmIfOperationalState based on Integer32"""
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


_VmIfOperationalState_Type.__name__ = "Integer32"
_VmIfOperationalState_Object = MibTableColumn
vmIfOperationalState = _VmIfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14, 1, 2),
    _VmIfOperationalState_Type()
)
vmIfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIfOperationalState.setStatus("mandatory")


class _VmIfUsageState_Type(Integer32):
    """Custom type vmIfUsageState based on Integer32"""
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


_VmIfUsageState_Type.__name__ = "Integer32"
_VmIfUsageState_Object = MibTableColumn
vmIfUsageState = _VmIfUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14, 1, 3),
    _VmIfUsageState_Type()
)
vmIfUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIfUsageState.setStatus("mandatory")
_VmIfProvTable_Object = MibTable
vmIfProvTable = _VmIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 15)
)
if mibBuilder.loadTexts:
    vmIfProvTable.setStatus("mandatory")
_VmIfProvEntry_Object = MibTableRow
vmIfProvEntry = _VmIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 15, 1)
)
vmIfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"),
    (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"),
)
if mibBuilder.loadTexts:
    vmIfProvEntry.setStatus("mandatory")


class _VmIfMode_Type(Integer32):
    """Custom type vmIfMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alwaysUpInterface", 0),
          ("interVrConnection", 1))
    )


_VmIfMode_Type.__name__ = "Integer32"
_VmIfMode_Object = MibTableColumn
vmIfMode = _VmIfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 15, 1, 1),
    _VmIfMode_Type()
)
vmIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmIfMode.setStatus("mandatory")
_VirtualMediaMIB_ObjectIdentity = ObjectIdentity
virtualMediaMIB = _VirtualMediaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135)
)
_VirtualMediaGroup_ObjectIdentity = ObjectIdentity
virtualMediaGroup = _VirtualMediaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 1)
)
_VirtualMediaGroupBE_ObjectIdentity = ObjectIdentity
virtualMediaGroupBE = _VirtualMediaGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 1, 5)
)
_VirtualMediaGroupBE01_ObjectIdentity = ObjectIdentity
virtualMediaGroupBE01 = _VirtualMediaGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 1, 5, 2)
)
_VirtualMediaGroupBE01A_ObjectIdentity = ObjectIdentity
virtualMediaGroupBE01A = _VirtualMediaGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 1, 5, 2, 2)
)
_VirtualMediaCapabilities_ObjectIdentity = ObjectIdentity
virtualMediaCapabilities = _VirtualMediaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 3)
)
_VirtualMediaCapabilitiesBE_ObjectIdentity = ObjectIdentity
virtualMediaCapabilitiesBE = _VirtualMediaCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 3, 5)
)
_VirtualMediaCapabilitiesBE01_ObjectIdentity = ObjectIdentity
virtualMediaCapabilitiesBE01 = _VirtualMediaCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 3, 5, 2)
)
_VirtualMediaCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
virtualMediaCapabilitiesBE01A = _VirtualMediaCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VirtualMediaMIB",
    **{"vm": vm,
       "vmRowStatusTable": vmRowStatusTable,
       "vmRowStatusEntry": vmRowStatusEntry,
       "vmRowStatus": vmRowStatus,
       "vmComponentName": vmComponentName,
       "vmStorageType": vmStorageType,
       "vmIndex": vmIndex,
       "vmIf": vmIf,
       "vmIfRowStatusTable": vmIfRowStatusTable,
       "vmIfRowStatusEntry": vmIfRowStatusEntry,
       "vmIfRowStatus": vmIfRowStatus,
       "vmIfComponentName": vmIfComponentName,
       "vmIfStorageType": vmIfStorageType,
       "vmIfIndex": vmIfIndex,
       "vmIfMpTable": vmIfMpTable,
       "vmIfMpEntry": vmIfMpEntry,
       "vmIfLinkToProtocolPort": vmIfLinkToProtocolPort,
       "vmIfCidDataTable": vmIfCidDataTable,
       "vmIfCidDataEntry": vmIfCidDataEntry,
       "vmIfCustomerIdentifier": vmIfCustomerIdentifier,
       "vmIfIfEntryTable": vmIfIfEntryTable,
       "vmIfIfEntryEntry": vmIfIfEntryEntry,
       "vmIfIfAdminStatus": vmIfIfAdminStatus,
       "vmIfIfIndex": vmIfIfIndex,
       "vmIfOperStatusTable": vmIfOperStatusTable,
       "vmIfOperStatusEntry": vmIfOperStatusEntry,
       "vmIfSnmpOperStatus": vmIfSnmpOperStatus,
       "vmIfStateTable": vmIfStateTable,
       "vmIfStateEntry": vmIfStateEntry,
       "vmIfAdminState": vmIfAdminState,
       "vmIfOperationalState": vmIfOperationalState,
       "vmIfUsageState": vmIfUsageState,
       "vmIfProvTable": vmIfProvTable,
       "vmIfProvEntry": vmIfProvEntry,
       "vmIfMode": vmIfMode,
       "virtualMediaMIB": virtualMediaMIB,
       "virtualMediaGroup": virtualMediaGroup,
       "virtualMediaGroupBE": virtualMediaGroupBE,
       "virtualMediaGroupBE01": virtualMediaGroupBE01,
       "virtualMediaGroupBE01A": virtualMediaGroupBE01A,
       "virtualMediaCapabilities": virtualMediaCapabilities,
       "virtualMediaCapabilitiesBE": virtualMediaCapabilitiesBE,
       "virtualMediaCapabilitiesBE01": virtualMediaCapabilitiesBE01,
       "virtualMediaCapabilitiesBE01A": virtualMediaCapabilitiesBE01A}
)
