# SNMP MIB module (VMWARE-OBSOLETE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-OBSOLETE-MIB
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(vmwESX,) = mibBuilder.importSymbols(
    "VMWARE-PRODUCTS-MIB",
    "vmwESX")

(vmwCPU,
 vmwMemory) = mibBuilder.importSymbols(
    "VMWARE-RESOURCES-MIB",
    "vmwCPU",
    "vmwMemory")

(vmwNotifications,
 vmwObsolete,
 vmwResources,
 vmwTraps) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwNotifications",
    "vmwObsolete",
    "vmwResources",
    "vmwTraps")

(vmwVmConfigFilePath,
 vmwVmID) = mibBuilder.importSymbols(
    "VMWARE-VMINFO-MIB",
    "vmwVmConfigFilePath",
    "vmwVmID")


# MODULE-IDENTITY

vmwObsoleteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 800, 1)
)
vmwObsoleteMIB.setRevisions(
        ("2008-10-15 11:59",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwCpuTable_Object = MibTable
vmwCpuTable = _VmwCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vmwCpuTable.setStatus("obsolete")
_VmwCpuEntry_Object = MibTableRow
vmwCpuEntry = _VmwCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1)
)
vmwCpuEntry.setIndexNames(
    (0, "VMWARE-OBSOLETE-MIB", "vmwCpuVMID"),
)
if mibBuilder.loadTexts:
    vmwCpuEntry.setStatus("obsolete")


class _VmwCpuVMID_Type(Integer32):
    """Custom type vmwCpuVMID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_VmwCpuVMID_Type.__name__ = "Integer32"
_VmwCpuVMID_Object = MibTableColumn
vmwCpuVMID = _VmwCpuVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 1),
    _VmwCpuVMID_Type()
)
vmwCpuVMID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwCpuVMID.setStatus("current")
_VmwCpuShares_Type = Gauge32
_VmwCpuShares_Object = MibTableColumn
vmwCpuShares = _VmwCpuShares_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 2),
    _VmwCpuShares_Type()
)
vmwCpuShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwCpuShares.setStatus("current")
if mibBuilder.loadTexts:
    vmwCpuShares.setUnits("unknown")
_VmwCpuUtil_Type = Gauge32
_VmwCpuUtil_Object = MibTableColumn
vmwCpuUtil = _VmwCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 3),
    _VmwCpuUtil_Type()
)
vmwCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwCpuUtil.setStatus("current")
if mibBuilder.loadTexts:
    vmwCpuUtil.setUnits("seconds")
_VmwMemTable_Object = MibTable
vmwMemTable = _VmwMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4)
)
if mibBuilder.loadTexts:
    vmwMemTable.setStatus("obsolete")
_VmwMemEntry_Object = MibTableRow
vmwMemEntry = _VmwMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1)
)
vmwMemEntry.setIndexNames(
    (0, "VMWARE-OBSOLETE-MIB", "vmwMemVMID"),
)
if mibBuilder.loadTexts:
    vmwMemEntry.setStatus("obsolete")


class _VmwMemVMID_Type(Integer32):
    """Custom type vmwMemVMID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_VmwMemVMID_Type.__name__ = "Integer32"
_VmwMemVMID_Object = MibTableColumn
vmwMemVMID = _VmwMemVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 1),
    _VmwMemVMID_Type()
)
vmwMemVMID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwMemVMID.setStatus("obsolete")
_VmwMemShares_Type = Gauge32
_VmwMemShares_Object = MibTableColumn
vmwMemShares = _VmwMemShares_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 2),
    _VmwMemShares_Type()
)
vmwMemShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwMemShares.setStatus("obsolete")
if mibBuilder.loadTexts:
    vmwMemShares.setUnits("unknown")
_VmwMemConfigured_Type = Gauge32
_VmwMemConfigured_Object = MibTableColumn
vmwMemConfigured = _VmwMemConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 3),
    _VmwMemConfigured_Type()
)
vmwMemConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwMemConfigured.setStatus("obsolete")
if mibBuilder.loadTexts:
    vmwMemConfigured.setUnits("kilobytes")
_VmwMemUtil_Type = Gauge32
_VmwMemUtil_Object = MibTableColumn
vmwMemUtil = _VmwMemUtil_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 4),
    _VmwMemUtil_Type()
)
vmwMemUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwMemUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    vmwMemUtil.setUnits("kilobytes")
_VmwHBATable_Object = MibTable
vmwHBATable = _VmwHBATable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3)
)
if mibBuilder.loadTexts:
    vmwHBATable.setStatus("obsolete")
_VmwHBAEntry_Object = MibTableRow
vmwHBAEntry = _VmwHBAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1)
)
vmwHBAEntry.setIndexNames(
    (0, "VMWARE-OBSOLETE-MIB", "vmwHbaIdx"),
)
if mibBuilder.loadTexts:
    vmwHBAEntry.setStatus("obsolete")


class _VmwHbaIdx_Type(Integer32):
    """Custom type vmwHbaIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_VmwHbaIdx_Type.__name__ = "Integer32"
_VmwHbaIdx_Object = MibTableColumn
vmwHbaIdx = _VmwHbaIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 1),
    _VmwHbaIdx_Type()
)
vmwHbaIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwHbaIdx.setStatus("obsolete")
_VmwHbaName_Type = DisplayString
_VmwHbaName_Object = MibTableColumn
vmwHbaName = _VmwHbaName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 2),
    _VmwHbaName_Type()
)
vmwHbaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaName.setStatus("obsolete")
_VmwHbaVMID_Type = Integer32
_VmwHbaVMID_Object = MibTableColumn
vmwHbaVMID = _VmwHbaVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 3),
    _VmwHbaVMID_Type()
)
vmwHbaVMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHbaVMID.setStatus("obsolete")
_VmwDiskShares_Type = Gauge32
_VmwDiskShares_Object = MibTableColumn
vmwDiskShares = _VmwDiskShares_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 4),
    _VmwDiskShares_Type()
)
vmwDiskShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwDiskShares.setStatus("obsolete")
_VmwNumReads_Type = Counter32
_VmwNumReads_Object = MibTableColumn
vmwNumReads = _VmwNumReads_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 5),
    _VmwNumReads_Type()
)
vmwNumReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNumReads.setStatus("obsolete")
_VmwKbRead_Type = Counter32
_VmwKbRead_Object = MibTableColumn
vmwKbRead = _VmwKbRead_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 6),
    _VmwKbRead_Type()
)
vmwKbRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwKbRead.setStatus("obsolete")
_VmwNumWrites_Type = Counter32
_VmwNumWrites_Object = MibTableColumn
vmwNumWrites = _VmwNumWrites_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 7),
    _VmwNumWrites_Type()
)
vmwNumWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNumWrites.setStatus("obsolete")
_VmwKbWritten_Type = Counter32
_VmwKbWritten_Object = MibTableColumn
vmwKbWritten = _VmwKbWritten_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 8),
    _VmwKbWritten_Type()
)
vmwKbWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwKbWritten.setStatus("obsolete")
_VmwNetTable_Object = MibTable
vmwNetTable = _VmwNetTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4)
)
if mibBuilder.loadTexts:
    vmwNetTable.setStatus("obsolete")
_VmwNetEntry_Object = MibTableRow
vmwNetEntry = _VmwNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1)
)
vmwNetEntry.setIndexNames(
    (0, "VMWARE-OBSOLETE-MIB", "vmwNetIdx"),
)
if mibBuilder.loadTexts:
    vmwNetEntry.setStatus("obsolete")


class _VmwNetIdx_Type(Integer32):
    """Custom type vmwNetIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VmwNetIdx_Type.__name__ = "Integer32"
_VmwNetIdx_Object = MibTableColumn
vmwNetIdx = _VmwNetIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 1),
    _VmwNetIdx_Type()
)
vmwNetIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwNetIdx.setStatus("obsolete")
_VmwNetName_Type = DisplayString
_VmwNetName_Object = MibTableColumn
vmwNetName = _VmwNetName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 2),
    _VmwNetName_Type()
)
vmwNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetName.setStatus("obsolete")
_VmwNetVMID_Type = Integer32
_VmwNetVMID_Object = MibTableColumn
vmwNetVMID = _VmwNetVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 3),
    _VmwNetVMID_Type()
)
vmwNetVMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetVMID.setStatus("obsolete")
_VmwNetIfAddr_Type = DisplayString
_VmwNetIfAddr_Object = MibTableColumn
vmwNetIfAddr = _VmwNetIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 4),
    _VmwNetIfAddr_Type()
)
vmwNetIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetIfAddr.setStatus("obsolete")
_VmwNetShares_Type = Gauge32
_VmwNetShares_Object = MibTableColumn
vmwNetShares = _VmwNetShares_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 5),
    _VmwNetShares_Type()
)
vmwNetShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetShares.setStatus("obsolete")
_VmwNetPktsTx_Type = Counter32
_VmwNetPktsTx_Object = MibTableColumn
vmwNetPktsTx = _VmwNetPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 6),
    _VmwNetPktsTx_Type()
)
vmwNetPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetPktsTx.setStatus("obsolete")
_VmwNetKbTx_Type = Counter32
_VmwNetKbTx_Object = MibTableColumn
vmwNetKbTx = _VmwNetKbTx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 7),
    _VmwNetKbTx_Type()
)
vmwNetKbTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetKbTx.setStatus("obsolete")
_VmwNetPktsRx_Type = Counter32
_VmwNetPktsRx_Object = MibTableColumn
vmwNetPktsRx = _VmwNetPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 8),
    _VmwNetPktsRx_Type()
)
vmwNetPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetPktsRx.setStatus("obsolete")
_VmwNetKbRx_Type = Counter32
_VmwNetKbRx_Object = MibTableColumn
vmwNetKbRx = _VmwNetKbRx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 9),
    _VmwNetKbRx_Type()
)
vmwNetKbRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetKbRx.setStatus("obsolete")
_VmwNetHCPktsTx_Type = Counter64
_VmwNetHCPktsTx_Object = MibTableColumn
vmwNetHCPktsTx = _VmwNetHCPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 10),
    _VmwNetHCPktsTx_Type()
)
vmwNetHCPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetHCPktsTx.setStatus("obsolete")
_VmwNetHCKbTx_Type = Counter64
_VmwNetHCKbTx_Object = MibTableColumn
vmwNetHCKbTx = _VmwNetHCKbTx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 11),
    _VmwNetHCKbTx_Type()
)
vmwNetHCKbTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetHCKbTx.setStatus("obsolete")
_VmwNetHCPktsRx_Type = Counter64
_VmwNetHCPktsRx_Object = MibTableColumn
vmwNetHCPktsRx = _VmwNetHCPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 12),
    _VmwNetHCPktsRx_Type()
)
vmwNetHCPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetHCPktsRx.setStatus("obsolete")
_VmwNetHCKbRx_Type = Counter64
_VmwNetHCKbRx_Object = MibTableColumn
vmwNetHCKbRx = _VmwNetHCKbRx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 13),
    _VmwNetHCKbRx_Type()
)
vmwNetHCKbRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwNetHCKbRx.setStatus("obsolete")
_VmkLoaded_Type = DisplayString
_VmkLoaded_Object = MibScalar
vmkLoaded = _VmkLoaded_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 1),
    _VmkLoaded_Type()
)
vmkLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmkLoaded.setStatus("obsolete")
_VpxdTrapType_Type = DisplayString
_VpxdTrapType_Object = MibScalar
vpxdTrapType = _VpxdTrapType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 301),
    _VpxdTrapType_Type()
)
vpxdTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vpxdTrapType.setStatus("current")
_VpxdHostName_Type = DisplayString
_VpxdHostName_Object = MibScalar
vpxdHostName = _VpxdHostName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 302),
    _VpxdHostName_Type()
)
vpxdHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vpxdHostName.setStatus("current")
_VpxdVMName_Type = DisplayString
_VpxdVMName_Object = MibScalar
vpxdVMName = _VpxdVMName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 303),
    _VpxdVMName_Type()
)
vpxdVMName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vpxdVMName.setStatus("current")
_VpxdOldStatus_Type = DisplayString
_VpxdOldStatus_Object = MibScalar
vpxdOldStatus = _VpxdOldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 304),
    _VpxdOldStatus_Type()
)
vpxdOldStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vpxdOldStatus.setStatus("current")
_VpxdNewStatus_Type = DisplayString
_VpxdNewStatus_Object = MibScalar
vpxdNewStatus = _VpxdNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 305),
    _VpxdNewStatus_Type()
)
vpxdNewStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vpxdNewStatus.setStatus("current")
_VpxdObjValue_Type = DisplayString
_VpxdObjValue_Object = MibScalar
vpxdObjValue = _VpxdObjValue_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 306),
    _VpxdObjValue_Type()
)
vpxdObjValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vpxdObjValue.setStatus("current")
_VmwObsoleteMIBConformance_ObjectIdentity = ObjectIdentity
vmwObsoleteMIBConformance = _VmwObsoleteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 800, 1, 2)
)
_VmwObsoleteMIBCompliances_ObjectIdentity = ObjectIdentity
vmwObsoleteMIBCompliances = _VmwObsoleteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 1)
)
_VmwObsMIBGroups_ObjectIdentity = ObjectIdentity
vmwObsMIBGroups = _VmwObsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 2)
)

# Managed Objects groups

vmwObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 2, 2)
)
vmwObsoleteGroup.setObjects(
      *(("VMWARE-OBSOLETE-MIB", "vmkLoaded"),
        ("VMWARE-OBSOLETE-MIB", "vmwCpuShares"),
        ("VMWARE-OBSOLETE-MIB", "vmwCpuUtil"),
        ("VMWARE-OBSOLETE-MIB", "vmwMemShares"),
        ("VMWARE-OBSOLETE-MIB", "vmwMemConfigured"),
        ("VMWARE-OBSOLETE-MIB", "vmwMemUtil"),
        ("VMWARE-OBSOLETE-MIB", "vmwHbaName"),
        ("VMWARE-OBSOLETE-MIB", "vmwHbaVMID"),
        ("VMWARE-OBSOLETE-MIB", "vmwDiskShares"),
        ("VMWARE-OBSOLETE-MIB", "vmwNumReads"),
        ("VMWARE-OBSOLETE-MIB", "vmwKbRead"),
        ("VMWARE-OBSOLETE-MIB", "vmwNumWrites"),
        ("VMWARE-OBSOLETE-MIB", "vmwKbWritten"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetName"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetVMID"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetIfAddr"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetShares"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetPktsTx"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetKbTx"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetPktsRx"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetKbRx"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetHCPktsTx"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetHCKbTx"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetHCPktsRx"),
        ("VMWARE-OBSOLETE-MIB", "vmwNetHCKbRx"),
        ("VMWARE-OBSOLETE-MIB", "vpxdTrapType"),
        ("VMWARE-OBSOLETE-MIB", "vpxdHostName"),
        ("VMWARE-OBSOLETE-MIB", "vpxdVMName"),
        ("VMWARE-OBSOLETE-MIB", "vpxdOldStatus"),
        ("VMWARE-OBSOLETE-MIB", "vpxdNewStatus"),
        ("VMWARE-OBSOLETE-MIB", "vpxdObjValue"))
)
if mibBuilder.loadTexts:
    vmwObsoleteGroup.setStatus("obsolete")


# Notification objects

vmPoweredOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 1)
)
vmPoweredOn.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
)
if mibBuilder.loadTexts:
    vmPoweredOn.setStatus(
        "obsolete"
    )

vmPoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 2)
)
vmPoweredOff.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
)
if mibBuilder.loadTexts:
    vmPoweredOff.setStatus(
        "obsolete"
    )

vmHBLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 3)
)
vmHBLost.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
)
if mibBuilder.loadTexts:
    vmHBLost.setStatus(
        "obsolete"
    )

vmHBDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 4)
)
vmHBDetected.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
)
if mibBuilder.loadTexts:
    vmHBDetected.setStatus(
        "obsolete"
    )

vmSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 5)
)
vmSuspended.setObjects(
      *(("VMWARE-VMINFO-MIB", "vmwVmID"),
        ("VMWARE-VMINFO-MIB", "vmwVmConfigFilePath"))
)
if mibBuilder.loadTexts:
    vmSuspended.setStatus(
        "obsolete"
    )

vpxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 201)
)
vpxdTrap.setObjects(
      *(("VMWARE-OBSOLETE-MIB", "vpxdTrapType"),
        ("VMWARE-OBSOLETE-MIB", "vpxdHostName"),
        ("VMWARE-OBSOLETE-MIB", "vpxdVMName"),
        ("VMWARE-OBSOLETE-MIB", "vpxdNewStatus"),
        ("VMWARE-OBSOLETE-MIB", "vpxdOldStatus"),
        ("VMWARE-OBSOLETE-MIB", "vpxdObjValue"))
)
if mibBuilder.loadTexts:
    vpxdTrap.setStatus(
        "obsolete"
    )


# Notifications groups

vmwOldVCNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 2, 3)
)
vmwOldVCNotificationGroup.setObjects(
      *(("VMWARE-OBSOLETE-MIB", "vpxdTrap"),
        ("VMWARE-OBSOLETE-MIB", "vmPoweredOn"),
        ("VMWARE-OBSOLETE-MIB", "vmPoweredOff"),
        ("VMWARE-OBSOLETE-MIB", "vmHBLost"),
        ("VMWARE-OBSOLETE-MIB", "vmHBDetected"),
        ("VMWARE-OBSOLETE-MIB", "vmSuspended"))
)
if mibBuilder.loadTexts:
    vmwOldVCNotificationGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

vmwObsoleteObsoleteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 800, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    vmwObsoleteObsoleteMIBCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-OBSOLETE-MIB",
    **{"vmPoweredOn": vmPoweredOn,
       "vmPoweredOff": vmPoweredOff,
       "vmHBLost": vmHBLost,
       "vmHBDetected": vmHBDetected,
       "vmSuspended": vmSuspended,
       "vpxdTrap": vpxdTrap,
       "vmwCpuTable": vmwCpuTable,
       "vmwCpuEntry": vmwCpuEntry,
       "vmwCpuVMID": vmwCpuVMID,
       "vmwCpuShares": vmwCpuShares,
       "vmwCpuUtil": vmwCpuUtil,
       "vmwMemTable": vmwMemTable,
       "vmwMemEntry": vmwMemEntry,
       "vmwMemVMID": vmwMemVMID,
       "vmwMemShares": vmwMemShares,
       "vmwMemConfigured": vmwMemConfigured,
       "vmwMemUtil": vmwMemUtil,
       "vmwHBATable": vmwHBATable,
       "vmwHBAEntry": vmwHBAEntry,
       "vmwHbaIdx": vmwHbaIdx,
       "vmwHbaName": vmwHbaName,
       "vmwHbaVMID": vmwHbaVMID,
       "vmwDiskShares": vmwDiskShares,
       "vmwNumReads": vmwNumReads,
       "vmwKbRead": vmwKbRead,
       "vmwNumWrites": vmwNumWrites,
       "vmwKbWritten": vmwKbWritten,
       "vmwNetTable": vmwNetTable,
       "vmwNetEntry": vmwNetEntry,
       "vmwNetIdx": vmwNetIdx,
       "vmwNetName": vmwNetName,
       "vmwNetVMID": vmwNetVMID,
       "vmwNetIfAddr": vmwNetIfAddr,
       "vmwNetShares": vmwNetShares,
       "vmwNetPktsTx": vmwNetPktsTx,
       "vmwNetKbTx": vmwNetKbTx,
       "vmwNetPktsRx": vmwNetPktsRx,
       "vmwNetKbRx": vmwNetKbRx,
       "vmwNetHCPktsTx": vmwNetHCPktsTx,
       "vmwNetHCKbTx": vmwNetHCKbTx,
       "vmwNetHCPktsRx": vmwNetHCPktsRx,
       "vmwNetHCKbRx": vmwNetHCKbRx,
       "vmkLoaded": vmkLoaded,
       "vpxdTrapType": vpxdTrapType,
       "vpxdHostName": vpxdHostName,
       "vpxdVMName": vpxdVMName,
       "vpxdOldStatus": vpxdOldStatus,
       "vpxdNewStatus": vpxdNewStatus,
       "vpxdObjValue": vpxdObjValue,
       "vmwObsoleteMIB": vmwObsoleteMIB,
       "vmwObsoleteMIBConformance": vmwObsoleteMIBConformance,
       "vmwObsoleteMIBCompliances": vmwObsoleteMIBCompliances,
       "vmwObsoleteObsoleteMIBCompliance": vmwObsoleteObsoleteMIBCompliance,
       "vmwObsMIBGroups": vmwObsMIBGroups,
       "vmwObsoleteGroup": vmwObsoleteGroup,
       "vmwOldVCNotificationGroup": vmwOldVCNotificationGroup}
)
