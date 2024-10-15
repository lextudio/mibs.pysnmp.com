# SNMP MIB module (VMWARE-VMINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-VMINFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:53 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vmwESXNotifications,) = mibBuilder.importSymbols(
    "VMWARE-ENV-MIB",
    "vmwESXNotifications")

(vmwTraps,
 vmwVirtMachines) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwTraps",
    "vmwVirtMachines")

(VmwConnectedState,) = mibBuilder.importSymbols(
    "VMWARE-TC-MIB",
    "VmwConnectedState")


# MODULE-IDENTITY

vmwVmInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 2, 10)
)
vmwVmInfoMIB.setRevisions(
        ("2011-09-17 00:00",
         "2010-06-22 00:00",
         "2008-10-23 00:00",
         "2007-12-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwVmTable_Object = MibTable
vmwVmTable = _VmwVmTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1)
)
if mibBuilder.loadTexts:
    vmwVmTable.setStatus("current")
_VmwVmEntry_Object = MibTableRow
vmwVmEntry = _VmwVmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1)
)
vmwVmEntry.setIndexNames(
    (0, "VMWARE-VMINFO-MIB", "vmwVmIdx"),
)
if mibBuilder.loadTexts:
    vmwVmEntry.setStatus("current")


class _VmwVmIdx_Type(Integer32):
    """Custom type vmwVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwVmIdx_Type.__name__ = "Integer32"
_VmwVmIdx_Object = MibTableColumn
vmwVmIdx = _VmwVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 1),
    _VmwVmIdx_Type()
)
vmwVmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwVmIdx.setStatus("current")
_VmwVmDisplayName_Type = DisplayString
_VmwVmDisplayName_Object = MibTableColumn
vmwVmDisplayName = _VmwVmDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 2),
    _VmwVmDisplayName_Type()
)
vmwVmDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmDisplayName.setStatus("current")
_VmwVmConfigFile_Type = DisplayString
_VmwVmConfigFile_Object = MibTableColumn
vmwVmConfigFile = _VmwVmConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 3),
    _VmwVmConfigFile_Type()
)
vmwVmConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmConfigFile.setStatus("current")
_VmwVmGuestOS_Type = DisplayString
_VmwVmGuestOS_Object = MibTableColumn
vmwVmGuestOS = _VmwVmGuestOS_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 4),
    _VmwVmGuestOS_Type()
)
vmwVmGuestOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmGuestOS.setStatus("current")
_VmwVmMemSize_Type = Integer32
_VmwVmMemSize_Object = MibTableColumn
vmwVmMemSize = _VmwVmMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 5),
    _VmwVmMemSize_Type()
)
vmwVmMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmMemSize.setStatus("current")
if mibBuilder.loadTexts:
    vmwVmMemSize.setUnits("megabytes")
_VmwVmState_Type = DisplayString
_VmwVmState_Object = MibTableColumn
vmwVmState = _VmwVmState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 6),
    _VmwVmState_Type()
)
vmwVmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmState.setStatus("current")
_VmwVmVMID_Type = Integer32
_VmwVmVMID_Object = MibTableColumn
vmwVmVMID = _VmwVmVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 7),
    _VmwVmVMID_Type()
)
vmwVmVMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmVMID.setStatus("obsolete")
_VmwVmGuestState_Type = DisplayString
_VmwVmGuestState_Object = MibTableColumn
vmwVmGuestState = _VmwVmGuestState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 8),
    _VmwVmGuestState_Type()
)
vmwVmGuestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmGuestState.setStatus("current")
_VmwVmCpus_Type = Integer32
_VmwVmCpus_Object = MibTableColumn
vmwVmCpus = _VmwVmCpus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 9),
    _VmwVmCpus_Type()
)
vmwVmCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmCpus.setStatus("current")


class _VmwVmUUID_Type(OctetString):
    """Custom type vmwVmUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 72),
    )


_VmwVmUUID_Type.__name__ = "OctetString"
_VmwVmUUID_Object = MibTableColumn
vmwVmUUID = _VmwVmUUID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 1, 1, 10),
    _VmwVmUUID_Type()
)
vmwVmUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmUUID.setStatus("current")
_VmwVmHbaTable_Object = MibTable
vmwVmHbaTable = _VmwVmHbaTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2)
)
if mibBuilder.loadTexts:
    vmwVmHbaTable.setStatus("current")
_VmwVmHbaEntry_Object = MibTableRow
vmwVmHbaEntry = _VmwVmHbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1)
)
vmwVmHbaEntry.setIndexNames(
    (0, "VMWARE-VMINFO-MIB", "vmwHbaVmIdx"),
    (0, "VMWARE-VMINFO-MIB", "vmwVmHbaIdx"),
)
if mibBuilder.loadTexts:
    vmwVmHbaEntry.setStatus("current")


class _VmwHbaVmIdx_Type(Integer32):
    """Custom type vmwHbaVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwHbaVmIdx_Type.__name__ = "Integer32"
_VmwHbaVmIdx_Object = MibTableColumn
vmwHbaVmIdx = _VmwHbaVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 1),
    _VmwHbaVmIdx_Type()
)
vmwHbaVmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwHbaVmIdx.setStatus("current")


class _VmwVmHbaIdx_Type(Integer32):
    """Custom type vmwVmHbaIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwVmHbaIdx_Type.__name__ = "Integer32"
_VmwVmHbaIdx_Object = MibTableColumn
vmwVmHbaIdx = _VmwVmHbaIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 2),
    _VmwVmHbaIdx_Type()
)
vmwVmHbaIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwVmHbaIdx.setStatus("current")
_VmwHbaNum_Type = DisplayString
_VmwHbaNum_Object = MibTableColumn
vmwHbaNum = _VmwHbaNum_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 3),
    _VmwHbaNum_Type()
)
vmwHbaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaNum.setStatus("current")
_VmwHbaVirtDev_Type = DisplayString
_VmwHbaVirtDev_Object = MibTableColumn
vmwHbaVirtDev = _VmwHbaVirtDev_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 2, 1, 4),
    _VmwHbaVirtDev_Type()
)
vmwHbaVirtDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaVirtDev.setStatus("current")
_VmwHbaTgtTable_Object = MibTable
vmwHbaTgtTable = _VmwHbaTgtTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3)
)
if mibBuilder.loadTexts:
    vmwHbaTgtTable.setStatus("current")
_VmwHbaTgtEntry_Object = MibTableRow
vmwHbaTgtEntry = _VmwHbaTgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3, 1)
)
vmwHbaTgtEntry.setIndexNames(
    (0, "VMWARE-VMINFO-MIB", "vmwHbaTgtVmIdx"),
    (0, "VMWARE-VMINFO-MIB", "vmwHbaTgtIdx"),
)
if mibBuilder.loadTexts:
    vmwHbaTgtEntry.setStatus("current")


class _VmwHbaTgtVmIdx_Type(Integer32):
    """Custom type vmwHbaTgtVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwHbaTgtVmIdx_Type.__name__ = "Integer32"
_VmwHbaTgtVmIdx_Object = MibTableColumn
vmwHbaTgtVmIdx = _VmwHbaTgtVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 1),
    _VmwHbaTgtVmIdx_Type()
)
vmwHbaTgtVmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwHbaTgtVmIdx.setStatus("current")


class _VmwHbaTgtIdx_Type(Integer32):
    """Custom type vmwHbaTgtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwHbaTgtIdx_Type.__name__ = "Integer32"
_VmwHbaTgtIdx_Object = MibTableColumn
vmwHbaTgtIdx = _VmwHbaTgtIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 2),
    _VmwHbaTgtIdx_Type()
)
vmwHbaTgtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwHbaTgtIdx.setStatus("current")
_VmwHbaTgtNum_Type = DisplayString
_VmwHbaTgtNum_Object = MibTableColumn
vmwHbaTgtNum = _VmwHbaTgtNum_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 3, 1, 3),
    _VmwHbaTgtNum_Type()
)
vmwHbaTgtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaTgtNum.setStatus("current")
_VmwVmNetTable_Object = MibTable
vmwVmNetTable = _VmwVmNetTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4)
)
if mibBuilder.loadTexts:
    vmwVmNetTable.setStatus("current")
_VmwVmNetEntry_Object = MibTableRow
vmwVmNetEntry = _VmwVmNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1)
)
vmwVmNetEntry.setIndexNames(
    (0, "VMWARE-VMINFO-MIB", "vmwVmNetVmIdx"),
    (0, "VMWARE-VMINFO-MIB", "vmwVmNetIdx"),
)
if mibBuilder.loadTexts:
    vmwVmNetEntry.setStatus("current")


class _VmwVmNetVmIdx_Type(Integer32):
    """Custom type vmwVmNetVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwVmNetVmIdx_Type.__name__ = "Integer32"
_VmwVmNetVmIdx_Object = MibTableColumn
vmwVmNetVmIdx = _VmwVmNetVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 1),
    _VmwVmNetVmIdx_Type()
)
vmwVmNetVmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwVmNetVmIdx.setStatus("current")


class _VmwVmNetIdx_Type(Integer32):
    """Custom type vmwVmNetIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwVmNetIdx_Type.__name__ = "Integer32"
_VmwVmNetIdx_Object = MibTableColumn
vmwVmNetIdx = _VmwVmNetIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 2),
    _VmwVmNetIdx_Type()
)
vmwVmNetIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwVmNetIdx.setStatus("current")
_VmwVmNetNum_Type = DisplayString
_VmwVmNetNum_Object = MibTableColumn
vmwVmNetNum = _VmwVmNetNum_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 3),
    _VmwVmNetNum_Type()
)
vmwVmNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmNetNum.setStatus("current")
_VmwVmNetName_Type = DisplayString
_VmwVmNetName_Object = MibTableColumn
vmwVmNetName = _VmwVmNetName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 4),
    _VmwVmNetName_Type()
)
vmwVmNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmNetName.setStatus("current")
_VmwVmNetConnType_Type = DisplayString
_VmwVmNetConnType_Object = MibTableColumn
vmwVmNetConnType = _VmwVmNetConnType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 5),
    _VmwVmNetConnType_Type()
)
vmwVmNetConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmNetConnType.setStatus("obsolete")
_VmwVmNetConnected_Type = VmwConnectedState
_VmwVmNetConnected_Object = MibTableColumn
vmwVmNetConnected = _VmwVmNetConnected_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 6),
    _VmwVmNetConnected_Type()
)
vmwVmNetConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmNetConnected.setStatus("current")
_VmwVmMAC_Type = PhysAddress
_VmwVmMAC_Object = MibTableColumn
vmwVmMAC = _VmwVmMAC_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 4, 1, 7),
    _VmwVmMAC_Type()
)
vmwVmMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwVmMAC.setStatus("current")
_VmwFloppyTable_Object = MibTable
vmwFloppyTable = _VmwFloppyTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5)
)
if mibBuilder.loadTexts:
    vmwFloppyTable.setStatus("current")
_VmwFloppyEntry_Object = MibTableRow
vmwFloppyEntry = _VmwFloppyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1)
)
vmwFloppyEntry.setIndexNames(
    (0, "VMWARE-VMINFO-MIB", "vmwFdVmIdx"),
    (0, "VMWARE-VMINFO-MIB", "vmwFdIdx"),
)
if mibBuilder.loadTexts:
    vmwFloppyEntry.setStatus("current")


class _VmwFdVmIdx_Type(Integer32):
    """Custom type vmwFdVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwFdVmIdx_Type.__name__ = "Integer32"
_VmwFdVmIdx_Object = MibTableColumn
vmwFdVmIdx = _VmwFdVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 1),
    _VmwFdVmIdx_Type()
)
vmwFdVmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwFdVmIdx.setStatus("current")


class _VmwFdIdx_Type(Integer32):
    """Custom type vmwFdIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwFdIdx_Type.__name__ = "Integer32"
_VmwFdIdx_Object = MibTableColumn
vmwFdIdx = _VmwFdIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 2),
    _VmwFdIdx_Type()
)
vmwFdIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwFdIdx.setStatus("current")
_VmwFdName_Type = DisplayString
_VmwFdName_Object = MibTableColumn
vmwFdName = _VmwFdName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 3),
    _VmwFdName_Type()
)
vmwFdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwFdName.setStatus("current")
_VmwFdConnected_Type = VmwConnectedState
_VmwFdConnected_Object = MibTableColumn
vmwFdConnected = _VmwFdConnected_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 5, 1, 4),
    _VmwFdConnected_Type()
)
vmwFdConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwFdConnected.setStatus("current")
_VmwCdromTable_Object = MibTable
vmwCdromTable = _VmwCdromTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6)
)
if mibBuilder.loadTexts:
    vmwCdromTable.setStatus("current")
_VmwCdromEntry_Object = MibTableRow
vmwCdromEntry = _VmwCdromEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1)
)
vmwCdromEntry.setIndexNames(
    (0, "VMWARE-VMINFO-MIB", "vmwCdVmIdx"),
    (0, "VMWARE-VMINFO-MIB", "vmwCdromIdx"),
)
if mibBuilder.loadTexts:
    vmwCdromEntry.setStatus("current")


class _VmwCdVmIdx_Type(Integer32):
    """Custom type vmwCdVmIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwCdVmIdx_Type.__name__ = "Integer32"
_VmwCdVmIdx_Object = MibTableColumn
vmwCdVmIdx = _VmwCdVmIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 1),
    _VmwCdVmIdx_Type()
)
vmwCdVmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwCdVmIdx.setStatus("current")


class _VmwCdromIdx_Type(Integer32):
    """Custom type vmwCdromIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmwCdromIdx_Type.__name__ = "Integer32"
_VmwCdromIdx_Object = MibTableColumn
vmwCdromIdx = _VmwCdromIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 2),
    _VmwCdromIdx_Type()
)
vmwCdromIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwCdromIdx.setStatus("current")
_VmwCdromName_Type = DisplayString
_VmwCdromName_Object = MibTableColumn
vmwCdromName = _VmwCdromName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 3),
    _VmwCdromName_Type()
)
vmwCdromName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwCdromName.setStatus("current")
_VmwCdromConnected_Type = VmwConnectedState
_VmwCdromConnected_Object = MibTableColumn
vmwCdromConnected = _VmwCdromConnected_Object(
    (1, 3, 6, 1, 4, 1, 6876, 2, 6, 1, 4),
    _VmwCdromConnected_Type()
)
vmwCdromConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwCdromConnected.setStatus("current")
_VmwVmInfoMIBConformance_ObjectIdentity = ObjectIdentity
vmwVmInfoMIBConformance = _VmwVmInfoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 2, 10, 2)
)
_VmwVmInfoMIBCompliances_ObjectIdentity = ObjectIdentity
vmwVmInfoMIBCompliances = _VmwVmInfoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 1)
)
_VmwVmInfoMIBGroups_ObjectIdentity = ObjectIdentity
vmwVmInfoMIBGroups = _VmwVmInfoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2)
)
_VmwVmID_Type = Integer32
_VmwVmID_Object = MibScalar
vmwVmID = _VmwVmID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 101),
    _VmwVmID_Type()
)
vmwVmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVmID.setStatus("current")
_VmwVmConfigFilePath_Type = DisplayString
_VmwVmConfigFilePath_Object = MibScalar
vmwVmConfigFilePath = _VmwVmConfigFilePath_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 102),
    _VmwVmConfigFilePath_Type()
)
vmwVmConfigFilePath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVmConfigFilePath.setStatus("current")

# Managed Objects groups

vmwVmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 1)
)
vmwVmInfoGroup.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmDisplayName"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFile"),
        ("VMWARE-VMINFO-MIB", "vmwVmGuestOS"),
        ("VMWARE-VMINFO-MIB", "vmwVmMemSize"),
        ("VMWARE-VMINFO-MIB", "vmwVmState"),
        ("VMWARE-VMINFO-MIB", "vmwVmGuestState"),
        ("VMWARE-VMINFO-MIB", "vmwHbaNum"),
        ("VMWARE-VMINFO-MIB", "vmwHbaVirtDev"),
        ("VMWARE-VMINFO-MIB", "vmwHbaTgtNum"),
        ("VMWARE-VMINFO-MIB", "vmwVmNetNum"),
        ("VMWARE-VMINFO-MIB", "vmwVmNetName"),
        ("VMWARE-VMINFO-MIB", "vmwVmNetConnected"),
        ("VMWARE-VMINFO-MIB", "vmwVmMAC"),
        ("VMWARE-VMINFO-MIB", "vmwFdName"),
        ("VMWARE-VMINFO-MIB", "vmwFdConnected"),
        ("VMWARE-VMINFO-MIB", "vmwCdromName"),
        ("VMWARE-VMINFO-MIB", "vmwCdromConnected"),
        ("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"),
        ("VMWARE-VMINFO-MIB", "vmwVmCpus"),
        ("VMWARE-VMINFO-MIB", "vmwVmUUID"))
)
if mibBuilder.loadTexts:
    vmwVmInfoGroup.setStatus("current")

vmwVmObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 3)
)
vmwVmObsoleteGroup.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmVMID"),
        ("VMWARE-VMINFO-MIB", "vmwVmNetConnType"))
)
if mibBuilder.loadTexts:
    vmwVmObsoleteGroup.setStatus("obsolete")


# Notification objects

vmwVmPoweredOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 1)
)
vmwVmPoweredOn.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"),
        ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
)
if mibBuilder.loadTexts:
    vmwVmPoweredOn.setStatus(
        "current"
    )

vmwVmPoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 2)
)
vmwVmPoweredOff.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"),
        ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
)
if mibBuilder.loadTexts:
    vmwVmPoweredOff.setStatus(
        "current"
    )

vmwVmHBLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 3)
)
vmwVmHBLost.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"),
        ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
)
if mibBuilder.loadTexts:
    vmwVmHBLost.setStatus(
        "current"
    )

vmwVmHBDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 4)
)
vmwVmHBDetected.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"),
        ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
)
if mibBuilder.loadTexts:
    vmwVmHBDetected.setStatus(
        "current"
    )

vmwVmSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 5)
)
vmwVmSuspended.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"),
        ("VMWARE-VMINFO-MIB", "vmwVmDisplayName"))
)
if mibBuilder.loadTexts:
    vmwVmSuspended.setStatus(
        "current"
    )


# Notifications groups

vmwVmInfoNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 2, 2)
)
vmwVmInfoNotificationGroup.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmPoweredOn"),
        ("VMWARE-VMINFO-MIB", "vmwVmPoweredOff"),
        ("VMWARE-VMINFO-MIB", "vmwVmHBLost"),
        ("VMWARE-VMINFO-MIB", "vmwVmHBDetected"),
        ("VMWARE-VMINFO-MIB", "vmwVmSuspended"))
)
if mibBuilder.loadTexts:
    vmwVmInfoNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwResMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 2, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vmwResMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VMINFO-MIB",
    **{"vmwVmTable": vmwVmTable,
       "vmwVmEntry": vmwVmEntry,
       "vmwVmIdx": vmwVmIdx,
       "vmwVmDisplayName": vmwVmDisplayName,
       "vmwVmConfigFile": vmwVmConfigFile,
       "vmwVmGuestOS": vmwVmGuestOS,
       "vmwVmMemSize": vmwVmMemSize,
       "vmwVmState": vmwVmState,
       "vmwVmVMID": vmwVmVMID,
       "vmwVmGuestState": vmwVmGuestState,
       "vmwVmCpus": vmwVmCpus,
       "vmwVmUUID": vmwVmUUID,
       "vmwVmHbaTable": vmwVmHbaTable,
       "vmwVmHbaEntry": vmwVmHbaEntry,
       "vmwHbaVmIdx": vmwHbaVmIdx,
       "vmwVmHbaIdx": vmwVmHbaIdx,
       "vmwHbaNum": vmwHbaNum,
       "vmwHbaVirtDev": vmwHbaVirtDev,
       "vmwHbaTgtTable": vmwHbaTgtTable,
       "vmwHbaTgtEntry": vmwHbaTgtEntry,
       "vmwHbaTgtVmIdx": vmwHbaTgtVmIdx,
       "vmwHbaTgtIdx": vmwHbaTgtIdx,
       "vmwHbaTgtNum": vmwHbaTgtNum,
       "vmwVmNetTable": vmwVmNetTable,
       "vmwVmNetEntry": vmwVmNetEntry,
       "vmwVmNetVmIdx": vmwVmNetVmIdx,
       "vmwVmNetIdx": vmwVmNetIdx,
       "vmwVmNetNum": vmwVmNetNum,
       "vmwVmNetName": vmwVmNetName,
       "vmwVmNetConnType": vmwVmNetConnType,
       "vmwVmNetConnected": vmwVmNetConnected,
       "vmwVmMAC": vmwVmMAC,
       "vmwFloppyTable": vmwFloppyTable,
       "vmwFloppyEntry": vmwFloppyEntry,
       "vmwFdVmIdx": vmwFdVmIdx,
       "vmwFdIdx": vmwFdIdx,
       "vmwFdName": vmwFdName,
       "vmwFdConnected": vmwFdConnected,
       "vmwCdromTable": vmwCdromTable,
       "vmwCdromEntry": vmwCdromEntry,
       "vmwCdVmIdx": vmwCdVmIdx,
       "vmwCdromIdx": vmwCdromIdx,
       "vmwCdromName": vmwCdromName,
       "vmwCdromConnected": vmwCdromConnected,
       "vmwVmInfoMIB": vmwVmInfoMIB,
       "vmwVmInfoMIBConformance": vmwVmInfoMIBConformance,
       "vmwVmInfoMIBCompliances": vmwVmInfoMIBCompliances,
       "vmwResMIBBasicCompliance": vmwResMIBBasicCompliance,
       "vmwVmInfoMIBGroups": vmwVmInfoMIBGroups,
       "vmwVmInfoGroup": vmwVmInfoGroup,
       "vmwVmInfoNotificationGroup": vmwVmInfoNotificationGroup,
       "vmwVmObsoleteGroup": vmwVmObsoleteGroup,
       "vmwVmPoweredOn": vmwVmPoweredOn,
       "vmwVmPoweredOff": vmwVmPoweredOff,
       "vmwVmHBLost": vmwVmHBLost,
       "vmwVmHBDetected": vmwVmHBDetected,
       "vmwVmSuspended": vmwVmSuspended,
       "vmwVmID": vmwVmID,
       "vmwVmConfigFilePath": vmwVmConfigFilePath}
)
