# SNMP MIB module (HIPATH-WIRELESS-BRANCH-OFFICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIPATH-WIRELESS-BRANCH-OFFICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:28 2024
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

(apIndex,) = mibBuilder.importSymbols(
    "HIPATH-WIRELESS-HWC-MIB",
    "apIndex")

(hiPathWirelessMgmt,
 hiPathWirelessModules) = mibBuilder.importSymbols(
    "HIPATH-WIRELESS-SMI",
    "hiPathWirelessMgmt",
    "hiPathWirelessModules")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hiPathWirelessBranchOfficeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 5, 4)
)
hiPathWirelessBranchOfficeMIB.setRevisions(
        ("2005-07-29 14:43",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HiPathWirelessBranchOfficeMib_ObjectIdentity = ObjectIdentity
hiPathWirelessBranchOfficeMib = _HiPathWirelessBranchOfficeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22)
)
_BranchOfficeObjects_ObjectIdentity = ObjectIdentity
branchOfficeObjects = _BranchOfficeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1)
)
_BranchOfficeTable_Object = MibTable
branchOfficeTable = _BranchOfficeTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 1)
)
if mibBuilder.loadTexts:
    branchOfficeTable.setStatus("obsolete")
_BranchOfficeEntry_Object = MibTableRow
branchOfficeEntry = _BranchOfficeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 1, 1)
)
branchOfficeEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    branchOfficeEntry.setStatus("obsolete")


class _BoConnectMode_Type(Integer32):
    """Custom type boConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoDiscovery", 1),
          ("staticConnect", 2))
    )


_BoConnectMode_Type.__name__ = "Integer32"
_BoConnectMode_Object = MibTableColumn
boConnectMode = _BoConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 1, 1, 1),
    _BoConnectMode_Type()
)
boConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boConnectMode.setStatus("obsolete")


class _BoIpAllocation_Type(Integer32):
    """Custom type boIpAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )


_BoIpAllocation_Type.__name__ = "Integer32"
_BoIpAllocation_Object = MibTableColumn
boIpAllocation = _BoIpAllocation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 1, 1, 2),
    _BoIpAllocation_Type()
)
boIpAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boIpAllocation.setStatus("obsolete")
_BoStaticIpAddress_Type = IpAddress
_BoStaticIpAddress_Object = MibTableColumn
boStaticIpAddress = _BoStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 1, 1, 3),
    _BoStaticIpAddress_Type()
)
boStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boStaticIpAddress.setStatus("obsolete")
_BoStaticNetmask_Type = IpAddress
_BoStaticNetmask_Object = MibTableColumn
boStaticNetmask = _BoStaticNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 1, 1, 4),
    _BoStaticNetmask_Type()
)
boStaticNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boStaticNetmask.setStatus("obsolete")
_BoStaticGateway_Type = IpAddress
_BoStaticGateway_Object = MibTableColumn
boStaticGateway = _BoStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 1, 1, 5),
    _BoStaticGateway_Type()
)
boStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boStaticGateway.setStatus("obsolete")
_BoRebootOnPollFailure_Type = Integer32
_BoRebootOnPollFailure_Object = MibTableColumn
boRebootOnPollFailure = _BoRebootOnPollFailure_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 1, 1, 6),
    _BoRebootOnPollFailure_Type()
)
boRebootOnPollFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boRebootOnPollFailure.setStatus("obsolete")
_BranchOfficeHWCTable_Object = MibTable
branchOfficeHWCTable = _BranchOfficeHWCTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 2)
)
if mibBuilder.loadTexts:
    branchOfficeHWCTable.setStatus("current")
_BranchOfficeHWCEntry_Object = MibTableRow
branchOfficeHWCEntry = _BranchOfficeHWCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 2, 1)
)
branchOfficeHWCEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    branchOfficeHWCEntry.setStatus("current")
_BoHWCConnectOrder_Type = Integer32
_BoHWCConnectOrder_Object = MibTableColumn
boHWCConnectOrder = _BoHWCConnectOrder_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 2, 1, 1),
    _BoHWCConnectOrder_Type()
)
boHWCConnectOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boHWCConnectOrder.setStatus("current")
_BoHWCIpAddress_Type = IpAddress
_BoHWCIpAddress_Object = MibTableColumn
boHWCIpAddress = _BoHWCIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 2, 1, 2),
    _BoHWCIpAddress_Type()
)
boHWCIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boHWCIpAddress.setStatus("current")
_BoHWCRowStatus_Type = RowStatus
_BoHWCRowStatus_Object = MibTableColumn
boHWCRowStatus = _BoHWCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 1, 2, 1, 3),
    _BoHWCRowStatus_Type()
)
boHWCRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boHWCRowStatus.setStatus("current")
_HiPathWirelessBranchOfficeConformance_ObjectIdentity = ObjectIdentity
hiPathWirelessBranchOfficeConformance = _HiPathWirelessBranchOfficeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 2)
)

# Managed Objects groups

hiPathWirelessBranchOfficeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 2, 1)
)
hiPathWirelessBranchOfficeGroup.setObjects(
      *(("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boHWCRowStatus"),
        ("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boHWCIpAddress"),
        ("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boHWCConnectOrder"))
)
if mibBuilder.loadTexts:
    hiPathWirelessBranchOfficeGroup.setStatus("current")

hiPathWirelessBOObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 2, 3)
)
hiPathWirelessBOObsoleteGroup.setObjects(
      *(("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boConnectMode"),
        ("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boIpAllocation"),
        ("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boStaticIpAddress"),
        ("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boStaticNetmask"),
        ("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boStaticGateway"),
        ("HIPATH-WIRELESS-BRANCH-OFFICE-MIB", "boRebootOnPollFailure"))
)
if mibBuilder.loadTexts:
    hiPathWirelessBOObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hiPathWirelessBOConformance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 22, 2, 2)
)
if mibBuilder.loadTexts:
    hiPathWirelessBOConformance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIPATH-WIRELESS-BRANCH-OFFICE-MIB",
    **{"hiPathWirelessBranchOfficeMib": hiPathWirelessBranchOfficeMib,
       "branchOfficeObjects": branchOfficeObjects,
       "branchOfficeTable": branchOfficeTable,
       "branchOfficeEntry": branchOfficeEntry,
       "boConnectMode": boConnectMode,
       "boIpAllocation": boIpAllocation,
       "boStaticIpAddress": boStaticIpAddress,
       "boStaticNetmask": boStaticNetmask,
       "boStaticGateway": boStaticGateway,
       "boRebootOnPollFailure": boRebootOnPollFailure,
       "branchOfficeHWCTable": branchOfficeHWCTable,
       "branchOfficeHWCEntry": branchOfficeHWCEntry,
       "boHWCConnectOrder": boHWCConnectOrder,
       "boHWCIpAddress": boHWCIpAddress,
       "boHWCRowStatus": boHWCRowStatus,
       "hiPathWirelessBranchOfficeConformance": hiPathWirelessBranchOfficeConformance,
       "hiPathWirelessBranchOfficeGroup": hiPathWirelessBranchOfficeGroup,
       "hiPathWirelessBOConformance": hiPathWirelessBOConformance,
       "hiPathWirelessBOObsoleteGroup": hiPathWirelessBOObsoleteGroup,
       "hiPathWirelessBranchOfficeMIB": hiPathWirelessBranchOfficeMIB}
)
