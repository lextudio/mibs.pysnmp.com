# SNMP MIB module (BANYAN-NW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BANYAN-NW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:13 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Banyan_ObjectIdentity = ObjectIdentity
banyan = _Banyan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130)
)
_Others_ObjectIdentity = ObjectIdentity
others = _Others_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 2)
)
_Netware_ObjectIdentity = ObjectIdentity
netware = _Netware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 2, 1)
)
_Nwmib1_ObjectIdentity = ObjectIdentity
nwmib1 = _Nwmib1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1)
)
_Nwfsinfo_ObjectIdentity = ObjectIdentity
nwfsinfo = _Nwfsinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1)
)
_NwName_Type = OctetString
_NwName_Object = MibScalar
nwName = _NwName_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 1),
    _NwName_Type()
)
nwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwName.setStatus("mandatory")
_NwCompany_Type = OctetString
_NwCompany_Object = MibScalar
nwCompany = _NwCompany_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 2),
    _NwCompany_Type()
)
nwCompany.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwCompany.setStatus("mandatory")
_NwRev_Type = OctetString
_NwRev_Object = MibScalar
nwRev = _NwRev_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 3),
    _NwRev_Type()
)
nwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRev.setStatus("mandatory")
_NwRevDate_Type = OctetString
_NwRevDate_Object = MibScalar
nwRevDate = _NwRevDate_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 4),
    _NwRevDate_Type()
)
nwRevDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRevDate.setStatus("mandatory")
_NwCopyRight_Type = OctetString
_NwCopyRight_Object = MibScalar
nwCopyRight = _NwCopyRight_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 5),
    _NwCopyRight_Type()
)
nwCopyRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwCopyRight.setStatus("mandatory")
_NwConnsSupp_Type = Integer32
_NwConnsSupp_Object = MibScalar
nwConnsSupp = _NwConnsSupp_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 6),
    _NwConnsSupp_Type()
)
nwConnsSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnsSupp.setStatus("mandatory")
_NwConnsInUse_Type = Integer32
_NwConnsInUse_Object = MibScalar
nwConnsInUse = _NwConnsInUse_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 7),
    _NwConnsInUse_Type()
)
nwConnsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnsInUse.setStatus("mandatory")
_NwPeakConnectionsUsed_Type = Integer32
_NwPeakConnectionsUsed_Object = MibScalar
nwPeakConnectionsUsed = _NwPeakConnectionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 8),
    _NwPeakConnectionsUsed_Type()
)
nwPeakConnectionsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwPeakConnectionsUsed.setStatus("mandatory")
_NwMaxVolsSupp_Type = Integer32
_NwMaxVolsSupp_Object = MibScalar
nwMaxVolsSupp = _NwMaxVolsSupp_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 9),
    _NwMaxVolsSupp_Type()
)
nwMaxVolsSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwMaxVolsSupp.setStatus("mandatory")
_NwRevArray_Type = OctetString
_NwRevArray_Object = MibScalar
nwRevArray = _NwRevArray_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 1, 10),
    _NwRevArray_Type()
)
nwRevArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRevArray.setStatus("mandatory")
_Nwperipherals_ObjectIdentity = ObjectIdentity
nwperipherals = _Nwperipherals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2)
)
_NwVolNumber_Type = Integer32
_NwVolNumber_Object = MibScalar
nwVolNumber = _NwVolNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 1),
    _NwVolNumber_Type()
)
nwVolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolNumber.setStatus("mandatory")
_NwVolTable_Object = MibTable
nwVolTable = _NwVolTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nwVolTable.setStatus("mandatory")
_NwVolEntry_Object = MibTableRow
nwVolEntry = _NwVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1)
)
nwVolEntry.setIndexNames(
    (0, "BANYAN-NW-MIB", "nwVolIndex"),
)
if mibBuilder.loadTexts:
    nwVolEntry.setStatus("mandatory")
_NwVolIndex_Type = Integer32
_NwVolIndex_Object = MibTableColumn
nwVolIndex = _NwVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 1),
    _NwVolIndex_Type()
)
nwVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolIndex.setStatus("mandatory")
_NwVolName_Type = OctetString
_NwVolName_Object = MibTableColumn
nwVolName = _NwVolName_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 2),
    _NwVolName_Type()
)
nwVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolName.setStatus("mandatory")
_NwVolDrive_Type = Integer32
_NwVolDrive_Object = MibTableColumn
nwVolDrive = _NwVolDrive_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 3),
    _NwVolDrive_Type()
)
nwVolDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolDrive.setStatus("mandatory")
_NwVolSectorsPerBlk_Type = Integer32
_NwVolSectorsPerBlk_Object = MibTableColumn
nwVolSectorsPerBlk = _NwVolSectorsPerBlk_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 4),
    _NwVolSectorsPerBlk_Type()
)
nwVolSectorsPerBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolSectorsPerBlk.setStatus("mandatory")
_NwVolStartBlk_Type = Integer32
_NwVolStartBlk_Object = MibTableColumn
nwVolStartBlk = _NwVolStartBlk_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 5),
    _NwVolStartBlk_Type()
)
nwVolStartBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolStartBlk.setStatus("mandatory")
_NwVolTotalBlks_Type = Integer32
_NwVolTotalBlks_Object = MibTableColumn
nwVolTotalBlks = _NwVolTotalBlks_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 6),
    _NwVolTotalBlks_Type()
)
nwVolTotalBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolTotalBlks.setStatus("mandatory")
_NwVolAvailBlks_Type = Integer32
_NwVolAvailBlks_Object = MibTableColumn
nwVolAvailBlks = _NwVolAvailBlks_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 7),
    _NwVolAvailBlks_Type()
)
nwVolAvailBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolAvailBlks.setStatus("mandatory")
_NwVolTotalDirSlots_Type = Integer32
_NwVolTotalDirSlots_Object = MibTableColumn
nwVolTotalDirSlots = _NwVolTotalDirSlots_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 8),
    _NwVolTotalDirSlots_Type()
)
nwVolTotalDirSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolTotalDirSlots.setStatus("mandatory")
_NwVolAvailDirSlots_Type = Integer32
_NwVolAvailDirSlots_Object = MibTableColumn
nwVolAvailDirSlots = _NwVolAvailDirSlots_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 9),
    _NwVolAvailDirSlots_Type()
)
nwVolAvailDirSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolAvailDirSlots.setStatus("mandatory")
_NwVolMaxDirSlots_Type = Integer32
_NwVolMaxDirSlots_Object = MibTableColumn
nwVolMaxDirSlots = _NwVolMaxDirSlots_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 10),
    _NwVolMaxDirSlots_Type()
)
nwVolMaxDirSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolMaxDirSlots.setStatus("mandatory")
_NwVolHashing_Type = Integer32
_NwVolHashing_Object = MibTableColumn
nwVolHashing = _NwVolHashing_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 11),
    _NwVolHashing_Type()
)
nwVolHashing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolHashing.setStatus("mandatory")
_NwVolRemovable_Type = Integer32
_NwVolRemovable_Object = MibTableColumn
nwVolRemovable = _NwVolRemovable_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 12),
    _NwVolRemovable_Type()
)
nwVolRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolRemovable.setStatus("mandatory")
_NwVolMounted_Type = Integer32
_NwVolMounted_Object = MibTableColumn
nwVolMounted = _NwVolMounted_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 13),
    _NwVolMounted_Type()
)
nwVolMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolMounted.setStatus("mandatory")
_NwVolPurgeBlks_Type = Integer32
_NwVolPurgeBlks_Object = MibTableColumn
nwVolPurgeBlks = _NwVolPurgeBlks_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 14),
    _NwVolPurgeBlks_Type()
)
nwVolPurgeBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolPurgeBlks.setStatus("mandatory")
_NwVolNotPurgeBlks_Type = Integer32
_NwVolNotPurgeBlks_Object = MibTableColumn
nwVolNotPurgeBlks = _NwVolNotPurgeBlks_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 2, 2, 1, 15),
    _NwVolNotPurgeBlks_Type()
)
nwVolNotPurgeBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolNotPurgeBlks.setStatus("mandatory")
_Nwinterfaces_ObjectIdentity = ObjectIdentity
nwinterfaces = _Nwinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3)
)
_NwIfNumber_Type = Integer32
_NwIfNumber_Object = MibScalar
nwIfNumber = _NwIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 1),
    _NwIfNumber_Type()
)
nwIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfNumber.setStatus("mandatory")
_NwIfCfgTable_Object = MibTable
nwIfCfgTable = _NwIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nwIfCfgTable.setStatus("mandatory")
_NwIfCfgEntry_Object = MibTableRow
nwIfCfgEntry = _NwIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1)
)
nwIfCfgEntry.setIndexNames(
    (0, "BANYAN-NW-MIB", "nwIfCfgBoardNo"),
)
if mibBuilder.loadTexts:
    nwIfCfgEntry.setStatus("mandatory")
_NwIfCfgSignature_Type = OctetString
_NwIfCfgSignature_Object = MibTableColumn
nwIfCfgSignature = _NwIfCfgSignature_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 1),
    _NwIfCfgSignature_Type()
)
nwIfCfgSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgSignature.setStatus("mandatory")
_NwIfCfgMajVer_Type = Integer32
_NwIfCfgMajVer_Object = MibTableColumn
nwIfCfgMajVer = _NwIfCfgMajVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 2),
    _NwIfCfgMajVer_Type()
)
nwIfCfgMajVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMajVer.setStatus("mandatory")
_NwIfCfgMinVer_Type = Integer32
_NwIfCfgMinVer_Object = MibTableColumn
nwIfCfgMinVer = _NwIfCfgMinVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 3),
    _NwIfCfgMinVer_Type()
)
nwIfCfgMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMinVer.setStatus("mandatory")
_NwIfCfgNodeAddress_Type = OctetString
_NwIfCfgNodeAddress_Object = MibTableColumn
nwIfCfgNodeAddress = _NwIfCfgNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 4),
    _NwIfCfgNodeAddress_Type()
)
nwIfCfgNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgNodeAddress.setStatus("mandatory")
_NwIfCfgModeFlags_Type = Integer32
_NwIfCfgModeFlags_Object = MibTableColumn
nwIfCfgModeFlags = _NwIfCfgModeFlags_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 5),
    _NwIfCfgModeFlags_Type()
)
nwIfCfgModeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgModeFlags.setStatus("mandatory")
_NwIfCfgBoardNo_Type = Integer32
_NwIfCfgBoardNo_Object = MibTableColumn
nwIfCfgBoardNo = _NwIfCfgBoardNo_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 6),
    _NwIfCfgBoardNo_Type()
)
nwIfCfgBoardNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgBoardNo.setStatus("mandatory")
_NwIfCfgBoardInst_Type = Integer32
_NwIfCfgBoardInst_Object = MibTableColumn
nwIfCfgBoardInst = _NwIfCfgBoardInst_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 7),
    _NwIfCfgBoardInst_Type()
)
nwIfCfgBoardInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgBoardInst.setStatus("mandatory")
_NwIfCfgMaxDataSz_Type = Integer32
_NwIfCfgMaxDataSz_Object = MibTableColumn
nwIfCfgMaxDataSz = _NwIfCfgMaxDataSz_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 8),
    _NwIfCfgMaxDataSz_Type()
)
nwIfCfgMaxDataSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMaxDataSz.setStatus("mandatory")
_NwIfCfgMaxRcvSz_Type = Integer32
_NwIfCfgMaxRcvSz_Object = MibTableColumn
nwIfCfgMaxRcvSz = _NwIfCfgMaxRcvSz_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 9),
    _NwIfCfgMaxRcvSz_Type()
)
nwIfCfgMaxRcvSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMaxRcvSz.setStatus("mandatory")
_NwIfCfgRcvSz_Type = Integer32
_NwIfCfgRcvSz_Object = MibTableColumn
nwIfCfgRcvSz = _NwIfCfgRcvSz_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 10),
    _NwIfCfgRcvSz_Type()
)
nwIfCfgRcvSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgRcvSz.setStatus("mandatory")
_NwIfCfgCardName_Type = OctetString
_NwIfCfgCardName_Object = MibTableColumn
nwIfCfgCardName = _NwIfCfgCardName_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 11),
    _NwIfCfgCardName_Type()
)
nwIfCfgCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgCardName.setStatus("mandatory")
_NwIfCfgShortName_Type = OctetString
_NwIfCfgShortName_Object = MibTableColumn
nwIfCfgShortName = _NwIfCfgShortName_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 12),
    _NwIfCfgShortName_Type()
)
nwIfCfgShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgShortName.setStatus("mandatory")
_NwIfCfgMediaType_Type = OctetString
_NwIfCfgMediaType_Object = MibTableColumn
nwIfCfgMediaType = _NwIfCfgMediaType_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 13),
    _NwIfCfgMediaType_Type()
)
nwIfCfgMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMediaType.setStatus("mandatory")
_NwIfCfgCardId_Type = Integer32
_NwIfCfgCardId_Object = MibTableColumn
nwIfCfgCardId = _NwIfCfgCardId_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 14),
    _NwIfCfgCardId_Type()
)
nwIfCfgCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgCardId.setStatus("mandatory")
_NwIfCfgMediaId_Type = Integer32
_NwIfCfgMediaId_Object = MibTableColumn
nwIfCfgMediaId = _NwIfCfgMediaId_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 15),
    _NwIfCfgMediaId_Type()
)
nwIfCfgMediaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMediaId.setStatus("mandatory")
_NwIfCfgTransportTM_Type = Integer32
_NwIfCfgTransportTM_Object = MibTableColumn
nwIfCfgTransportTM = _NwIfCfgTransportTM_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 16),
    _NwIfCfgTransportTM_Type()
)
nwIfCfgTransportTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgTransportTM.setStatus("mandatory")
_NwIfCfgMlidMajVer_Type = Integer32
_NwIfCfgMlidMajVer_Object = MibTableColumn
nwIfCfgMlidMajVer = _NwIfCfgMlidMajVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 17),
    _NwIfCfgMlidMajVer_Type()
)
nwIfCfgMlidMajVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMlidMajVer.setStatus("mandatory")
_NwIfCfgMlidMinVer_Type = Integer32
_NwIfCfgMlidMinVer_Object = MibTableColumn
nwIfCfgMlidMinVer = _NwIfCfgMlidMinVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 18),
    _NwIfCfgMlidMinVer_Type()
)
nwIfCfgMlidMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMlidMinVer.setStatus("mandatory")
_NwIfCfgFlags_Type = Integer32
_NwIfCfgFlags_Object = MibTableColumn
nwIfCfgFlags = _NwIfCfgFlags_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 19),
    _NwIfCfgFlags_Type()
)
nwIfCfgFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgFlags.setStatus("mandatory")
_NwIfCfgSendRetries_Type = Integer32
_NwIfCfgSendRetries_Object = MibTableColumn
nwIfCfgSendRetries = _NwIfCfgSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 20),
    _NwIfCfgSendRetries_Type()
)
nwIfCfgSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgSendRetries.setStatus("mandatory")
_NwIfCfgShareFlags_Type = Integer32
_NwIfCfgShareFlags_Object = MibTableColumn
nwIfCfgShareFlags = _NwIfCfgShareFlags_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 21),
    _NwIfCfgShareFlags_Type()
)
nwIfCfgShareFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgShareFlags.setStatus("mandatory")
_NwIfCfgSlot_Type = Integer32
_NwIfCfgSlot_Object = MibTableColumn
nwIfCfgSlot = _NwIfCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 22),
    _NwIfCfgSlot_Type()
)
nwIfCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgSlot.setStatus("mandatory")
_NwIfCfgIoAddr1_Type = Integer32
_NwIfCfgIoAddr1_Object = MibTableColumn
nwIfCfgIoAddr1 = _NwIfCfgIoAddr1_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 23),
    _NwIfCfgIoAddr1_Type()
)
nwIfCfgIoAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgIoAddr1.setStatus("mandatory")
_NwIfCfgIoRange1_Type = Integer32
_NwIfCfgIoRange1_Object = MibTableColumn
nwIfCfgIoRange1 = _NwIfCfgIoRange1_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 24),
    _NwIfCfgIoRange1_Type()
)
nwIfCfgIoRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgIoRange1.setStatus("mandatory")
_NwIfCfgIoAddr2_Type = Integer32
_NwIfCfgIoAddr2_Object = MibTableColumn
nwIfCfgIoAddr2 = _NwIfCfgIoAddr2_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 25),
    _NwIfCfgIoAddr2_Type()
)
nwIfCfgIoAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgIoAddr2.setStatus("mandatory")
_NwIfCfgIoRange2_Type = Integer32
_NwIfCfgIoRange2_Object = MibTableColumn
nwIfCfgIoRange2 = _NwIfCfgIoRange2_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 26),
    _NwIfCfgIoRange2_Type()
)
nwIfCfgIoRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgIoRange2.setStatus("mandatory")
_NwIfCfgMemAddr1_Type = Integer32
_NwIfCfgMemAddr1_Object = MibTableColumn
nwIfCfgMemAddr1 = _NwIfCfgMemAddr1_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 27),
    _NwIfCfgMemAddr1_Type()
)
nwIfCfgMemAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMemAddr1.setStatus("mandatory")
_NwIfCfgMemSize1_Type = Integer32
_NwIfCfgMemSize1_Object = MibTableColumn
nwIfCfgMemSize1 = _NwIfCfgMemSize1_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 28),
    _NwIfCfgMemSize1_Type()
)
nwIfCfgMemSize1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMemSize1.setStatus("mandatory")
_NwIfCfgMemAddr2_Type = Integer32
_NwIfCfgMemAddr2_Object = MibTableColumn
nwIfCfgMemAddr2 = _NwIfCfgMemAddr2_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 29),
    _NwIfCfgMemAddr2_Type()
)
nwIfCfgMemAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMemAddr2.setStatus("mandatory")
_NwIfCfgMemSize2_Type = Integer32
_NwIfCfgMemSize2_Object = MibTableColumn
nwIfCfgMemSize2 = _NwIfCfgMemSize2_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 30),
    _NwIfCfgMemSize2_Type()
)
nwIfCfgMemSize2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgMemSize2.setStatus("mandatory")
_NwIfCfgInt1_Type = Integer32
_NwIfCfgInt1_Object = MibTableColumn
nwIfCfgInt1 = _NwIfCfgInt1_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 31),
    _NwIfCfgInt1_Type()
)
nwIfCfgInt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgInt1.setStatus("mandatory")
_NwIfCfgInt2_Type = Integer32
_NwIfCfgInt2_Object = MibTableColumn
nwIfCfgInt2 = _NwIfCfgInt2_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 32),
    _NwIfCfgInt2_Type()
)
nwIfCfgInt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgInt2.setStatus("mandatory")
_NwIfCfgDma1_Type = Integer32
_NwIfCfgDma1_Object = MibTableColumn
nwIfCfgDma1 = _NwIfCfgDma1_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 33),
    _NwIfCfgDma1_Type()
)
nwIfCfgDma1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgDma1.setStatus("mandatory")
_NwIfCfgDma2_Type = Integer32
_NwIfCfgDma2_Object = MibTableColumn
nwIfCfgDma2 = _NwIfCfgDma2_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 2, 1, 34),
    _NwIfCfgDma2_Type()
)
nwIfCfgDma2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCfgDma2.setStatus("mandatory")
_NwIfStatsTable_Object = MibTable
nwIfStatsTable = _NwIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    nwIfStatsTable.setStatus("mandatory")
_NwIfStatsEntry_Object = MibTableRow
nwIfStatsEntry = _NwIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1)
)
nwIfStatsEntry.setIndexNames(
    (0, "BANYAN-NW-MIB", "nwIfStatsBoardNo"),
)
if mibBuilder.loadTexts:
    nwIfStatsEntry.setStatus("mandatory")
_NwIfStatsMajVer_Type = Integer32
_NwIfStatsMajVer_Object = MibTableColumn
nwIfStatsMajVer = _NwIfStatsMajVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 1),
    _NwIfStatsMajVer_Type()
)
nwIfStatsMajVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsMajVer.setStatus("mandatory")
_NwIfStatsMinVer_Type = Integer32
_NwIfStatsMinVer_Object = MibTableColumn
nwIfStatsMinVer = _NwIfStatsMinVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 2),
    _NwIfStatsMinVer_Type()
)
nwIfStatsMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsMinVer.setStatus("mandatory")
_NwIfStatsValidMask_Type = Integer32
_NwIfStatsValidMask_Object = MibTableColumn
nwIfStatsValidMask = _NwIfStatsValidMask_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 3),
    _NwIfStatsValidMask_Type()
)
nwIfStatsValidMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsValidMask.setStatus("mandatory")
_NwIfStatsTotalTxPkts_Type = Counter32
_NwIfStatsTotalTxPkts_Object = MibTableColumn
nwIfStatsTotalTxPkts = _NwIfStatsTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 4),
    _NwIfStatsTotalTxPkts_Type()
)
nwIfStatsTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsTotalTxPkts.setStatus("mandatory")
_NwIfStatsTotalRxPkts_Type = Counter32
_NwIfStatsTotalRxPkts_Object = MibTableColumn
nwIfStatsTotalRxPkts = _NwIfStatsTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 5),
    _NwIfStatsTotalRxPkts_Type()
)
nwIfStatsTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsTotalRxPkts.setStatus("mandatory")
_NwIfStatsNoAvailEcbs_Type = Counter32
_NwIfStatsNoAvailEcbs_Object = MibTableColumn
nwIfStatsNoAvailEcbs = _NwIfStatsNoAvailEcbs_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 6),
    _NwIfStatsNoAvailEcbs_Type()
)
nwIfStatsNoAvailEcbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsNoAvailEcbs.setStatus("mandatory")
_NwIfStatsTxTooBigs_Type = Counter32
_NwIfStatsTxTooBigs_Object = MibTableColumn
nwIfStatsTxTooBigs = _NwIfStatsTxTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 7),
    _NwIfStatsTxTooBigs_Type()
)
nwIfStatsTxTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsTxTooBigs.setStatus("mandatory")
_NwIfStatsTxTooSmalls_Type = Counter32
_NwIfStatsTxTooSmalls_Object = MibTableColumn
nwIfStatsTxTooSmalls = _NwIfStatsTxTooSmalls_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 8),
    _NwIfStatsTxTooSmalls_Type()
)
nwIfStatsTxTooSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsTxTooSmalls.setStatus("mandatory")
_NwIfStatsRxOverFlows_Type = Counter32
_NwIfStatsRxOverFlows_Object = MibTableColumn
nwIfStatsRxOverFlows = _NwIfStatsRxOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 9),
    _NwIfStatsRxOverFlows_Type()
)
nwIfStatsRxOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsRxOverFlows.setStatus("mandatory")
_NwIfStatsRxTooBigs_Type = Counter32
_NwIfStatsRxTooBigs_Object = MibTableColumn
nwIfStatsRxTooBigs = _NwIfStatsRxTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 10),
    _NwIfStatsRxTooBigs_Type()
)
nwIfStatsRxTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsRxTooBigs.setStatus("mandatory")
_NwIfStatsRxTooSmalls_Type = Counter32
_NwIfStatsRxTooSmalls_Object = MibTableColumn
nwIfStatsRxTooSmalls = _NwIfStatsRxTooSmalls_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 11),
    _NwIfStatsRxTooSmalls_Type()
)
nwIfStatsRxTooSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsRxTooSmalls.setStatus("mandatory")
_NwIfStatsTxMiscErrs_Type = Counter32
_NwIfStatsTxMiscErrs_Object = MibTableColumn
nwIfStatsTxMiscErrs = _NwIfStatsTxMiscErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 12),
    _NwIfStatsTxMiscErrs_Type()
)
nwIfStatsTxMiscErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsTxMiscErrs.setStatus("mandatory")
_NwIfStatsRxMiscErrs_Type = Counter32
_NwIfStatsRxMiscErrs_Object = MibTableColumn
nwIfStatsRxMiscErrs = _NwIfStatsRxMiscErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 13),
    _NwIfStatsRxMiscErrs_Type()
)
nwIfStatsRxMiscErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsRxMiscErrs.setStatus("mandatory")
_NwIfStatsTxRetrys_Type = Counter32
_NwIfStatsTxRetrys_Object = MibTableColumn
nwIfStatsTxRetrys = _NwIfStatsTxRetrys_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 14),
    _NwIfStatsTxRetrys_Type()
)
nwIfStatsTxRetrys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsTxRetrys.setStatus("mandatory")
_NwIfStatsRxChkSumErrs_Type = Counter32
_NwIfStatsRxChkSumErrs_Object = MibTableColumn
nwIfStatsRxChkSumErrs = _NwIfStatsRxChkSumErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 15),
    _NwIfStatsRxChkSumErrs_Type()
)
nwIfStatsRxChkSumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsRxChkSumErrs.setStatus("mandatory")
_NwIfStatsRxMismatchs_Type = Counter32
_NwIfStatsRxMismatchs_Object = MibTableColumn
nwIfStatsRxMismatchs = _NwIfStatsRxMismatchs_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 16),
    _NwIfStatsRxMismatchs_Type()
)
nwIfStatsRxMismatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsRxMismatchs.setStatus("mandatory")
_NwIfStatsBoardNo_Type = Integer32
_NwIfStatsBoardNo_Object = MibTableColumn
nwIfStatsBoardNo = _NwIfStatsBoardNo_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 17),
    _NwIfStatsBoardNo_Type()
)
nwIfStatsBoardNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsBoardNo.setStatus("mandatory")
_NwIfStatsCustom_Type = Integer32
_NwIfStatsCustom_Object = MibTableColumn
nwIfStatsCustom = _NwIfStatsCustom_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 3, 1, 18),
    _NwIfStatsCustom_Type()
)
nwIfStatsCustom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfStatsCustom.setStatus("mandatory")
_NwIfCustomStatsTable_Object = MibTable
nwIfCustomStatsTable = _NwIfCustomStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    nwIfCustomStatsTable.setStatus("mandatory")
_NwIfCustomStatsEntry_Object = MibTableRow
nwIfCustomStatsEntry = _NwIfCustomStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 4, 1)
)
nwIfCustomStatsEntry.setIndexNames(
    (0, "BANYAN-NW-MIB", "nwIfCustomStatsBoardNo"),
    (0, "BANYAN-NW-MIB", "nwIfCustomStatsIndex"),
)
if mibBuilder.loadTexts:
    nwIfCustomStatsEntry.setStatus("mandatory")
_NwIfCustomStatsBoardNo_Type = Integer32
_NwIfCustomStatsBoardNo_Object = MibTableColumn
nwIfCustomStatsBoardNo = _NwIfCustomStatsBoardNo_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 4, 1, 1),
    _NwIfCustomStatsBoardNo_Type()
)
nwIfCustomStatsBoardNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCustomStatsBoardNo.setStatus("mandatory")
_NwIfCustomStatsIndex_Type = Integer32
_NwIfCustomStatsIndex_Object = MibTableColumn
nwIfCustomStatsIndex = _NwIfCustomStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 4, 1, 2),
    _NwIfCustomStatsIndex_Type()
)
nwIfCustomStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCustomStatsIndex.setStatus("mandatory")
_NwIfCustomStatsDescr_Type = OctetString
_NwIfCustomStatsDescr_Object = MibTableColumn
nwIfCustomStatsDescr = _NwIfCustomStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 4, 1, 3),
    _NwIfCustomStatsDescr_Type()
)
nwIfCustomStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCustomStatsDescr.setStatus("mandatory")
_NwIfCustomStatsValue_Type = Counter32
_NwIfCustomStatsValue_Object = MibTableColumn
nwIfCustomStatsValue = _NwIfCustomStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 3, 4, 1, 4),
    _NwIfCustomStatsValue_Type()
)
nwIfCustomStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIfCustomStatsValue.setStatus("mandatory")
_Nwprotocols_ObjectIdentity = ObjectIdentity
nwprotocols = _Nwprotocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4)
)
_NwProtNumber_Type = Integer32
_NwProtNumber_Object = MibScalar
nwProtNumber = _NwProtNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 1),
    _NwProtNumber_Type()
)
nwProtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtNumber.setStatus("mandatory")
_NwProtCfgTable_Object = MibTable
nwProtCfgTable = _NwProtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    nwProtCfgTable.setStatus("mandatory")
_NwProtCfgEntry_Object = MibTableRow
nwProtCfgEntry = _NwProtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2, 1)
)
nwProtCfgEntry.setIndexNames(
    (0, "BANYAN-NW-MIB", "nwProtCfgProtNo"),
)
if mibBuilder.loadTexts:
    nwProtCfgEntry.setStatus("mandatory")
_NwProtCfgProtNo_Type = Integer32
_NwProtCfgProtNo_Object = MibTableColumn
nwProtCfgProtNo = _NwProtCfgProtNo_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2, 1, 1),
    _NwProtCfgProtNo_Type()
)
nwProtCfgProtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCfgProtNo.setStatus("mandatory")
_NwProtCfgMajVer_Type = Integer32
_NwProtCfgMajVer_Object = MibTableColumn
nwProtCfgMajVer = _NwProtCfgMajVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2, 1, 2),
    _NwProtCfgMajVer_Type()
)
nwProtCfgMajVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCfgMajVer.setStatus("mandatory")
_NwProtCfgMinVer_Type = Integer32
_NwProtCfgMinVer_Object = MibTableColumn
nwProtCfgMinVer = _NwProtCfgMinVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2, 1, 3),
    _NwProtCfgMinVer_Type()
)
nwProtCfgMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCfgMinVer.setStatus("mandatory")
_NwProtCfgName_Type = OctetString
_NwProtCfgName_Object = MibTableColumn
nwProtCfgName = _NwProtCfgName_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2, 1, 4),
    _NwProtCfgName_Type()
)
nwProtCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCfgName.setStatus("mandatory")
_NwProtCfgRegName_Type = OctetString
_NwProtCfgRegName_Object = MibTableColumn
nwProtCfgRegName = _NwProtCfgRegName_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2, 1, 5),
    _NwProtCfgRegName_Type()
)
nwProtCfgRegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCfgRegName.setStatus("mandatory")
_NwProtCfgStkMajVer_Type = Integer32
_NwProtCfgStkMajVer_Object = MibTableColumn
nwProtCfgStkMajVer = _NwProtCfgStkMajVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2, 1, 6),
    _NwProtCfgStkMajVer_Type()
)
nwProtCfgStkMajVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCfgStkMajVer.setStatus("mandatory")
_NwProtCfgStkMinVer_Type = Integer32
_NwProtCfgStkMinVer_Object = MibTableColumn
nwProtCfgStkMinVer = _NwProtCfgStkMinVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 2, 1, 7),
    _NwProtCfgStkMinVer_Type()
)
nwProtCfgStkMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCfgStkMinVer.setStatus("mandatory")
_NwProtStatsTable_Object = MibTable
nwProtStatsTable = _NwProtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    nwProtStatsTable.setStatus("mandatory")
_NwProtStatsEntry_Object = MibTableRow
nwProtStatsEntry = _NwProtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1)
)
nwProtStatsEntry.setIndexNames(
    (0, "BANYAN-NW-MIB", "nwProtStatsProtNo"),
)
if mibBuilder.loadTexts:
    nwProtStatsEntry.setStatus("mandatory")
_NwProtStatsProtNo_Type = Integer32
_NwProtStatsProtNo_Object = MibTableColumn
nwProtStatsProtNo = _NwProtStatsProtNo_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1, 1),
    _NwProtStatsProtNo_Type()
)
nwProtStatsProtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtStatsProtNo.setStatus("mandatory")
_NwProtStatsMajVer_Type = Integer32
_NwProtStatsMajVer_Object = MibTableColumn
nwProtStatsMajVer = _NwProtStatsMajVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1, 2),
    _NwProtStatsMajVer_Type()
)
nwProtStatsMajVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtStatsMajVer.setStatus("mandatory")
_NwProtStatsMinVer_Type = Integer32
_NwProtStatsMinVer_Object = MibTableColumn
nwProtStatsMinVer = _NwProtStatsMinVer_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1, 3),
    _NwProtStatsMinVer_Type()
)
nwProtStatsMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtStatsMinVer.setStatus("mandatory")
_NwProtStatsValidMask_Type = Integer32
_NwProtStatsValidMask_Object = MibTableColumn
nwProtStatsValidMask = _NwProtStatsValidMask_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1, 4),
    _NwProtStatsValidMask_Type()
)
nwProtStatsValidMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtStatsValidMask.setStatus("mandatory")
_NwProtStatsTotalTxPkts_Type = Counter32
_NwProtStatsTotalTxPkts_Object = MibTableColumn
nwProtStatsTotalTxPkts = _NwProtStatsTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1, 5),
    _NwProtStatsTotalTxPkts_Type()
)
nwProtStatsTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtStatsTotalTxPkts.setStatus("mandatory")
_NwProtStatsTotalRxPkts_Type = Counter32
_NwProtStatsTotalRxPkts_Object = MibTableColumn
nwProtStatsTotalRxPkts = _NwProtStatsTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1, 6),
    _NwProtStatsTotalRxPkts_Type()
)
nwProtStatsTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtStatsTotalRxPkts.setStatus("mandatory")
_NwProtStatsIgnoredRxPkts_Type = Counter32
_NwProtStatsIgnoredRxPkts_Object = MibTableColumn
nwProtStatsIgnoredRxPkts = _NwProtStatsIgnoredRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1, 7),
    _NwProtStatsIgnoredRxPkts_Type()
)
nwProtStatsIgnoredRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtStatsIgnoredRxPkts.setStatus("mandatory")
_NwProtStatsCustom_Type = Counter32
_NwProtStatsCustom_Object = MibTableColumn
nwProtStatsCustom = _NwProtStatsCustom_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 3, 1, 8),
    _NwProtStatsCustom_Type()
)
nwProtStatsCustom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtStatsCustom.setStatus("mandatory")
_NwProtCustomStatsTable_Object = MibTable
nwProtCustomStatsTable = _NwProtCustomStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    nwProtCustomStatsTable.setStatus("mandatory")
_NwProtCustomStatsEntry_Object = MibTableRow
nwProtCustomStatsEntry = _NwProtCustomStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 4, 1)
)
nwProtCustomStatsEntry.setIndexNames(
    (0, "BANYAN-NW-MIB", "nwProtCustomStatsProtNo"),
    (0, "BANYAN-NW-MIB", "nwProtCustomStatsIndex"),
)
if mibBuilder.loadTexts:
    nwProtCustomStatsEntry.setStatus("mandatory")
_NwProtCustomStatsProtNo_Type = Integer32
_NwProtCustomStatsProtNo_Object = MibTableColumn
nwProtCustomStatsProtNo = _NwProtCustomStatsProtNo_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 4, 1, 1),
    _NwProtCustomStatsProtNo_Type()
)
nwProtCustomStatsProtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCustomStatsProtNo.setStatus("mandatory")
_NwProtCustomStatsIndex_Type = Integer32
_NwProtCustomStatsIndex_Object = MibTableColumn
nwProtCustomStatsIndex = _NwProtCustomStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 4, 1, 2),
    _NwProtCustomStatsIndex_Type()
)
nwProtCustomStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCustomStatsIndex.setStatus("mandatory")
_NwProtCustomStatsDescr_Type = OctetString
_NwProtCustomStatsDescr_Object = MibTableColumn
nwProtCustomStatsDescr = _NwProtCustomStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 4, 1, 3),
    _NwProtCustomStatsDescr_Type()
)
nwProtCustomStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCustomStatsDescr.setStatus("mandatory")
_NwProtCustomStatsValue_Type = Counter32
_NwProtCustomStatsValue_Object = MibTableColumn
nwProtCustomStatsValue = _NwProtCustomStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 130, 2, 1, 1, 4, 4, 1, 4),
    _NwProtCustomStatsValue_Type()
)
nwProtCustomStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwProtCustomStatsValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BANYAN-NW-MIB",
    **{"banyan": banyan,
       "others": others,
       "netware": netware,
       "nwmib1": nwmib1,
       "nwfsinfo": nwfsinfo,
       "nwName": nwName,
       "nwCompany": nwCompany,
       "nwRev": nwRev,
       "nwRevDate": nwRevDate,
       "nwCopyRight": nwCopyRight,
       "nwConnsSupp": nwConnsSupp,
       "nwConnsInUse": nwConnsInUse,
       "nwPeakConnectionsUsed": nwPeakConnectionsUsed,
       "nwMaxVolsSupp": nwMaxVolsSupp,
       "nwRevArray": nwRevArray,
       "nwperipherals": nwperipherals,
       "nwVolNumber": nwVolNumber,
       "nwVolTable": nwVolTable,
       "nwVolEntry": nwVolEntry,
       "nwVolIndex": nwVolIndex,
       "nwVolName": nwVolName,
       "nwVolDrive": nwVolDrive,
       "nwVolSectorsPerBlk": nwVolSectorsPerBlk,
       "nwVolStartBlk": nwVolStartBlk,
       "nwVolTotalBlks": nwVolTotalBlks,
       "nwVolAvailBlks": nwVolAvailBlks,
       "nwVolTotalDirSlots": nwVolTotalDirSlots,
       "nwVolAvailDirSlots": nwVolAvailDirSlots,
       "nwVolMaxDirSlots": nwVolMaxDirSlots,
       "nwVolHashing": nwVolHashing,
       "nwVolRemovable": nwVolRemovable,
       "nwVolMounted": nwVolMounted,
       "nwVolPurgeBlks": nwVolPurgeBlks,
       "nwVolNotPurgeBlks": nwVolNotPurgeBlks,
       "nwinterfaces": nwinterfaces,
       "nwIfNumber": nwIfNumber,
       "nwIfCfgTable": nwIfCfgTable,
       "nwIfCfgEntry": nwIfCfgEntry,
       "nwIfCfgSignature": nwIfCfgSignature,
       "nwIfCfgMajVer": nwIfCfgMajVer,
       "nwIfCfgMinVer": nwIfCfgMinVer,
       "nwIfCfgNodeAddress": nwIfCfgNodeAddress,
       "nwIfCfgModeFlags": nwIfCfgModeFlags,
       "nwIfCfgBoardNo": nwIfCfgBoardNo,
       "nwIfCfgBoardInst": nwIfCfgBoardInst,
       "nwIfCfgMaxDataSz": nwIfCfgMaxDataSz,
       "nwIfCfgMaxRcvSz": nwIfCfgMaxRcvSz,
       "nwIfCfgRcvSz": nwIfCfgRcvSz,
       "nwIfCfgCardName": nwIfCfgCardName,
       "nwIfCfgShortName": nwIfCfgShortName,
       "nwIfCfgMediaType": nwIfCfgMediaType,
       "nwIfCfgCardId": nwIfCfgCardId,
       "nwIfCfgMediaId": nwIfCfgMediaId,
       "nwIfCfgTransportTM": nwIfCfgTransportTM,
       "nwIfCfgMlidMajVer": nwIfCfgMlidMajVer,
       "nwIfCfgMlidMinVer": nwIfCfgMlidMinVer,
       "nwIfCfgFlags": nwIfCfgFlags,
       "nwIfCfgSendRetries": nwIfCfgSendRetries,
       "nwIfCfgShareFlags": nwIfCfgShareFlags,
       "nwIfCfgSlot": nwIfCfgSlot,
       "nwIfCfgIoAddr1": nwIfCfgIoAddr1,
       "nwIfCfgIoRange1": nwIfCfgIoRange1,
       "nwIfCfgIoAddr2": nwIfCfgIoAddr2,
       "nwIfCfgIoRange2": nwIfCfgIoRange2,
       "nwIfCfgMemAddr1": nwIfCfgMemAddr1,
       "nwIfCfgMemSize1": nwIfCfgMemSize1,
       "nwIfCfgMemAddr2": nwIfCfgMemAddr2,
       "nwIfCfgMemSize2": nwIfCfgMemSize2,
       "nwIfCfgInt1": nwIfCfgInt1,
       "nwIfCfgInt2": nwIfCfgInt2,
       "nwIfCfgDma1": nwIfCfgDma1,
       "nwIfCfgDma2": nwIfCfgDma2,
       "nwIfStatsTable": nwIfStatsTable,
       "nwIfStatsEntry": nwIfStatsEntry,
       "nwIfStatsMajVer": nwIfStatsMajVer,
       "nwIfStatsMinVer": nwIfStatsMinVer,
       "nwIfStatsValidMask": nwIfStatsValidMask,
       "nwIfStatsTotalTxPkts": nwIfStatsTotalTxPkts,
       "nwIfStatsTotalRxPkts": nwIfStatsTotalRxPkts,
       "nwIfStatsNoAvailEcbs": nwIfStatsNoAvailEcbs,
       "nwIfStatsTxTooBigs": nwIfStatsTxTooBigs,
       "nwIfStatsTxTooSmalls": nwIfStatsTxTooSmalls,
       "nwIfStatsRxOverFlows": nwIfStatsRxOverFlows,
       "nwIfStatsRxTooBigs": nwIfStatsRxTooBigs,
       "nwIfStatsRxTooSmalls": nwIfStatsRxTooSmalls,
       "nwIfStatsTxMiscErrs": nwIfStatsTxMiscErrs,
       "nwIfStatsRxMiscErrs": nwIfStatsRxMiscErrs,
       "nwIfStatsTxRetrys": nwIfStatsTxRetrys,
       "nwIfStatsRxChkSumErrs": nwIfStatsRxChkSumErrs,
       "nwIfStatsRxMismatchs": nwIfStatsRxMismatchs,
       "nwIfStatsBoardNo": nwIfStatsBoardNo,
       "nwIfStatsCustom": nwIfStatsCustom,
       "nwIfCustomStatsTable": nwIfCustomStatsTable,
       "nwIfCustomStatsEntry": nwIfCustomStatsEntry,
       "nwIfCustomStatsBoardNo": nwIfCustomStatsBoardNo,
       "nwIfCustomStatsIndex": nwIfCustomStatsIndex,
       "nwIfCustomStatsDescr": nwIfCustomStatsDescr,
       "nwIfCustomStatsValue": nwIfCustomStatsValue,
       "nwprotocols": nwprotocols,
       "nwProtNumber": nwProtNumber,
       "nwProtCfgTable": nwProtCfgTable,
       "nwProtCfgEntry": nwProtCfgEntry,
       "nwProtCfgProtNo": nwProtCfgProtNo,
       "nwProtCfgMajVer": nwProtCfgMajVer,
       "nwProtCfgMinVer": nwProtCfgMinVer,
       "nwProtCfgName": nwProtCfgName,
       "nwProtCfgRegName": nwProtCfgRegName,
       "nwProtCfgStkMajVer": nwProtCfgStkMajVer,
       "nwProtCfgStkMinVer": nwProtCfgStkMinVer,
       "nwProtStatsTable": nwProtStatsTable,
       "nwProtStatsEntry": nwProtStatsEntry,
       "nwProtStatsProtNo": nwProtStatsProtNo,
       "nwProtStatsMajVer": nwProtStatsMajVer,
       "nwProtStatsMinVer": nwProtStatsMinVer,
       "nwProtStatsValidMask": nwProtStatsValidMask,
       "nwProtStatsTotalTxPkts": nwProtStatsTotalTxPkts,
       "nwProtStatsTotalRxPkts": nwProtStatsTotalRxPkts,
       "nwProtStatsIgnoredRxPkts": nwProtStatsIgnoredRxPkts,
       "nwProtStatsCustom": nwProtStatsCustom,
       "nwProtCustomStatsTable": nwProtCustomStatsTable,
       "nwProtCustomStatsEntry": nwProtCustomStatsEntry,
       "nwProtCustomStatsProtNo": nwProtCustomStatsProtNo,
       "nwProtCustomStatsIndex": nwProtCustomStatsIndex,
       "nwProtCustomStatsDescr": nwProtCustomStatsDescr,
       "nwProtCustomStatsValue": nwProtCustomStatsValue}
)
