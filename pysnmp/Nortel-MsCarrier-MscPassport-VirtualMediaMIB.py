# SNMP MIB module (Nortel-MsCarrier-MscPassport-VirtualMediaMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VirtualMediaMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:14 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "Link")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscVm_ObjectIdentity = ObjectIdentity
mscVm = _MscVm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133)
)
_MscVmRowStatusTable_Object = MibTable
mscVmRowStatusTable = _MscVmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1)
)
if mibBuilder.loadTexts:
    mscVmRowStatusTable.setStatus("mandatory")
_MscVmRowStatusEntry_Object = MibTableRow
mscVmRowStatusEntry = _MscVmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1)
)
mscVmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"),
)
if mibBuilder.loadTexts:
    mscVmRowStatusEntry.setStatus("mandatory")
_MscVmRowStatus_Type = RowStatus
_MscVmRowStatus_Object = MibTableColumn
mscVmRowStatus = _MscVmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1, 1),
    _MscVmRowStatus_Type()
)
mscVmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVmRowStatus.setStatus("mandatory")
_MscVmComponentName_Type = DisplayString
_MscVmComponentName_Object = MibTableColumn
mscVmComponentName = _MscVmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1, 2),
    _MscVmComponentName_Type()
)
mscVmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmComponentName.setStatus("mandatory")
_MscVmStorageType_Type = StorageType
_MscVmStorageType_Object = MibTableColumn
mscVmStorageType = _MscVmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1, 4),
    _MscVmStorageType_Type()
)
mscVmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmStorageType.setStatus("mandatory")


class _MscVmIndex_Type(Integer32):
    """Custom type mscVmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVmIndex_Type.__name__ = "Integer32"
_MscVmIndex_Object = MibTableColumn
mscVmIndex = _MscVmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1, 10),
    _MscVmIndex_Type()
)
mscVmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVmIndex.setStatus("mandatory")
_MscVmIf_ObjectIdentity = ObjectIdentity
mscVmIf = _MscVmIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2)
)
_MscVmIfRowStatusTable_Object = MibTable
mscVmIfRowStatusTable = _MscVmIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1)
)
if mibBuilder.loadTexts:
    mscVmIfRowStatusTable.setStatus("mandatory")
_MscVmIfRowStatusEntry_Object = MibTableRow
mscVmIfRowStatusEntry = _MscVmIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1)
)
mscVmIfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"),
)
if mibBuilder.loadTexts:
    mscVmIfRowStatusEntry.setStatus("mandatory")
_MscVmIfRowStatus_Type = RowStatus
_MscVmIfRowStatus_Object = MibTableColumn
mscVmIfRowStatus = _MscVmIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1, 1),
    _MscVmIfRowStatus_Type()
)
mscVmIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVmIfRowStatus.setStatus("mandatory")
_MscVmIfComponentName_Type = DisplayString
_MscVmIfComponentName_Object = MibTableColumn
mscVmIfComponentName = _MscVmIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1, 2),
    _MscVmIfComponentName_Type()
)
mscVmIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmIfComponentName.setStatus("mandatory")
_MscVmIfStorageType_Type = StorageType
_MscVmIfStorageType_Object = MibTableColumn
mscVmIfStorageType = _MscVmIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1, 4),
    _MscVmIfStorageType_Type()
)
mscVmIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmIfStorageType.setStatus("mandatory")


class _MscVmIfIndex_Type(Integer32):
    """Custom type mscVmIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVmIfIndex_Type.__name__ = "Integer32"
_MscVmIfIndex_Object = MibTableColumn
mscVmIfIndex = _MscVmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1, 10),
    _MscVmIfIndex_Type()
)
mscVmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVmIfIndex.setStatus("mandatory")
_MscVmIfMpTable_Object = MibTable
mscVmIfMpTable = _MscVmIfMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 10)
)
if mibBuilder.loadTexts:
    mscVmIfMpTable.setStatus("mandatory")
_MscVmIfMpEntry_Object = MibTableRow
mscVmIfMpEntry = _MscVmIfMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 10, 1)
)
mscVmIfMpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"),
)
if mibBuilder.loadTexts:
    mscVmIfMpEntry.setStatus("mandatory")
_MscVmIfLinkToProtocolPort_Type = Link
_MscVmIfLinkToProtocolPort_Object = MibTableColumn
mscVmIfLinkToProtocolPort = _MscVmIfLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 10, 1, 1),
    _MscVmIfLinkToProtocolPort_Type()
)
mscVmIfLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVmIfLinkToProtocolPort.setStatus("mandatory")
_MscVmIfCidDataTable_Object = MibTable
mscVmIfCidDataTable = _MscVmIfCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 11)
)
if mibBuilder.loadTexts:
    mscVmIfCidDataTable.setStatus("mandatory")
_MscVmIfCidDataEntry_Object = MibTableRow
mscVmIfCidDataEntry = _MscVmIfCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 11, 1)
)
mscVmIfCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"),
)
if mibBuilder.loadTexts:
    mscVmIfCidDataEntry.setStatus("mandatory")


class _MscVmIfCustomerIdentifier_Type(Unsigned32):
    """Custom type mscVmIfCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscVmIfCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscVmIfCustomerIdentifier_Object = MibTableColumn
mscVmIfCustomerIdentifier = _MscVmIfCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 11, 1, 1),
    _MscVmIfCustomerIdentifier_Type()
)
mscVmIfCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVmIfCustomerIdentifier.setStatus("mandatory")
_MscVmIfIfEntryTable_Object = MibTable
mscVmIfIfEntryTable = _MscVmIfIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 12)
)
if mibBuilder.loadTexts:
    mscVmIfIfEntryTable.setStatus("mandatory")
_MscVmIfIfEntryEntry_Object = MibTableRow
mscVmIfIfEntryEntry = _MscVmIfIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 12, 1)
)
mscVmIfIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"),
)
if mibBuilder.loadTexts:
    mscVmIfIfEntryEntry.setStatus("mandatory")


class _MscVmIfIfAdminStatus_Type(Integer32):
    """Custom type mscVmIfIfAdminStatus based on Integer32"""
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


_MscVmIfIfAdminStatus_Type.__name__ = "Integer32"
_MscVmIfIfAdminStatus_Object = MibTableColumn
mscVmIfIfAdminStatus = _MscVmIfIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 12, 1, 1),
    _MscVmIfIfAdminStatus_Type()
)
mscVmIfIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVmIfIfAdminStatus.setStatus("mandatory")


class _MscVmIfIfIndex_Type(InterfaceIndex):
    """Custom type mscVmIfIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVmIfIfIndex_Type.__name__ = "InterfaceIndex"
_MscVmIfIfIndex_Object = MibTableColumn
mscVmIfIfIndex = _MscVmIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 12, 1, 2),
    _MscVmIfIfIndex_Type()
)
mscVmIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmIfIfIndex.setStatus("mandatory")
_MscVmIfOperStatusTable_Object = MibTable
mscVmIfOperStatusTable = _MscVmIfOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 13)
)
if mibBuilder.loadTexts:
    mscVmIfOperStatusTable.setStatus("mandatory")
_MscVmIfOperStatusEntry_Object = MibTableRow
mscVmIfOperStatusEntry = _MscVmIfOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 13, 1)
)
mscVmIfOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"),
)
if mibBuilder.loadTexts:
    mscVmIfOperStatusEntry.setStatus("mandatory")


class _MscVmIfSnmpOperStatus_Type(Integer32):
    """Custom type mscVmIfSnmpOperStatus based on Integer32"""
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


_MscVmIfSnmpOperStatus_Type.__name__ = "Integer32"
_MscVmIfSnmpOperStatus_Object = MibTableColumn
mscVmIfSnmpOperStatus = _MscVmIfSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 13, 1, 1),
    _MscVmIfSnmpOperStatus_Type()
)
mscVmIfSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmIfSnmpOperStatus.setStatus("mandatory")
_MscVmIfStateTable_Object = MibTable
mscVmIfStateTable = _MscVmIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14)
)
if mibBuilder.loadTexts:
    mscVmIfStateTable.setStatus("mandatory")
_MscVmIfStateEntry_Object = MibTableRow
mscVmIfStateEntry = _MscVmIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14, 1)
)
mscVmIfStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"),
)
if mibBuilder.loadTexts:
    mscVmIfStateEntry.setStatus("mandatory")


class _MscVmIfAdminState_Type(Integer32):
    """Custom type mscVmIfAdminState based on Integer32"""
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


_MscVmIfAdminState_Type.__name__ = "Integer32"
_MscVmIfAdminState_Object = MibTableColumn
mscVmIfAdminState = _MscVmIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14, 1, 1),
    _MscVmIfAdminState_Type()
)
mscVmIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmIfAdminState.setStatus("mandatory")


class _MscVmIfOperationalState_Type(Integer32):
    """Custom type mscVmIfOperationalState based on Integer32"""
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


_MscVmIfOperationalState_Type.__name__ = "Integer32"
_MscVmIfOperationalState_Object = MibTableColumn
mscVmIfOperationalState = _MscVmIfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14, 1, 2),
    _MscVmIfOperationalState_Type()
)
mscVmIfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmIfOperationalState.setStatus("mandatory")


class _MscVmIfUsageState_Type(Integer32):
    """Custom type mscVmIfUsageState based on Integer32"""
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


_MscVmIfUsageState_Type.__name__ = "Integer32"
_MscVmIfUsageState_Object = MibTableColumn
mscVmIfUsageState = _MscVmIfUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14, 1, 3),
    _MscVmIfUsageState_Type()
)
mscVmIfUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVmIfUsageState.setStatus("mandatory")
_MscVmIfProvTable_Object = MibTable
mscVmIfProvTable = _MscVmIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 15)
)
if mibBuilder.loadTexts:
    mscVmIfProvTable.setStatus("mandatory")
_MscVmIfProvEntry_Object = MibTableRow
mscVmIfProvEntry = _MscVmIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 15, 1)
)
mscVmIfProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"),
)
if mibBuilder.loadTexts:
    mscVmIfProvEntry.setStatus("mandatory")


class _MscVmIfMode_Type(Integer32):
    """Custom type mscVmIfMode based on Integer32"""
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


_MscVmIfMode_Type.__name__ = "Integer32"
_MscVmIfMode_Object = MibTableColumn
mscVmIfMode = _MscVmIfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 15, 1, 1),
    _MscVmIfMode_Type()
)
mscVmIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVmIfMode.setStatus("mandatory")
_VirtualMediaMIB_ObjectIdentity = ObjectIdentity
virtualMediaMIB = _VirtualMediaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135)
)
_VirtualMediaGroup_ObjectIdentity = ObjectIdentity
virtualMediaGroup = _VirtualMediaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 1)
)
_VirtualMediaGroupCA_ObjectIdentity = ObjectIdentity
virtualMediaGroupCA = _VirtualMediaGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 1, 1)
)
_VirtualMediaGroupCA02_ObjectIdentity = ObjectIdentity
virtualMediaGroupCA02 = _VirtualMediaGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 1, 1, 3)
)
_VirtualMediaGroupCA02A_ObjectIdentity = ObjectIdentity
virtualMediaGroupCA02A = _VirtualMediaGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 1, 1, 3, 2)
)
_VirtualMediaCapabilities_ObjectIdentity = ObjectIdentity
virtualMediaCapabilities = _VirtualMediaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 3)
)
_VirtualMediaCapabilitiesCA_ObjectIdentity = ObjectIdentity
virtualMediaCapabilitiesCA = _VirtualMediaCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 3, 1)
)
_VirtualMediaCapabilitiesCA02_ObjectIdentity = ObjectIdentity
virtualMediaCapabilitiesCA02 = _VirtualMediaCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 3, 1, 3)
)
_VirtualMediaCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
virtualMediaCapabilitiesCA02A = _VirtualMediaCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualMediaMIB",
    **{"mscVm": mscVm,
       "mscVmRowStatusTable": mscVmRowStatusTable,
       "mscVmRowStatusEntry": mscVmRowStatusEntry,
       "mscVmRowStatus": mscVmRowStatus,
       "mscVmComponentName": mscVmComponentName,
       "mscVmStorageType": mscVmStorageType,
       "mscVmIndex": mscVmIndex,
       "mscVmIf": mscVmIf,
       "mscVmIfRowStatusTable": mscVmIfRowStatusTable,
       "mscVmIfRowStatusEntry": mscVmIfRowStatusEntry,
       "mscVmIfRowStatus": mscVmIfRowStatus,
       "mscVmIfComponentName": mscVmIfComponentName,
       "mscVmIfStorageType": mscVmIfStorageType,
       "mscVmIfIndex": mscVmIfIndex,
       "mscVmIfMpTable": mscVmIfMpTable,
       "mscVmIfMpEntry": mscVmIfMpEntry,
       "mscVmIfLinkToProtocolPort": mscVmIfLinkToProtocolPort,
       "mscVmIfCidDataTable": mscVmIfCidDataTable,
       "mscVmIfCidDataEntry": mscVmIfCidDataEntry,
       "mscVmIfCustomerIdentifier": mscVmIfCustomerIdentifier,
       "mscVmIfIfEntryTable": mscVmIfIfEntryTable,
       "mscVmIfIfEntryEntry": mscVmIfIfEntryEntry,
       "mscVmIfIfAdminStatus": mscVmIfIfAdminStatus,
       "mscVmIfIfIndex": mscVmIfIfIndex,
       "mscVmIfOperStatusTable": mscVmIfOperStatusTable,
       "mscVmIfOperStatusEntry": mscVmIfOperStatusEntry,
       "mscVmIfSnmpOperStatus": mscVmIfSnmpOperStatus,
       "mscVmIfStateTable": mscVmIfStateTable,
       "mscVmIfStateEntry": mscVmIfStateEntry,
       "mscVmIfAdminState": mscVmIfAdminState,
       "mscVmIfOperationalState": mscVmIfOperationalState,
       "mscVmIfUsageState": mscVmIfUsageState,
       "mscVmIfProvTable": mscVmIfProvTable,
       "mscVmIfProvEntry": mscVmIfProvEntry,
       "mscVmIfMode": mscVmIfMode,
       "virtualMediaMIB": virtualMediaMIB,
       "virtualMediaGroup": virtualMediaGroup,
       "virtualMediaGroupCA": virtualMediaGroupCA,
       "virtualMediaGroupCA02": virtualMediaGroupCA02,
       "virtualMediaGroupCA02A": virtualMediaGroupCA02A,
       "virtualMediaCapabilities": virtualMediaCapabilities,
       "virtualMediaCapabilitiesCA": virtualMediaCapabilitiesCA,
       "virtualMediaCapabilitiesCA02": virtualMediaCapabilitiesCA02,
       "virtualMediaCapabilitiesCA02A": virtualMediaCapabilitiesCA02A}
)
