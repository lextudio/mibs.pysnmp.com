# SNMP MIB module (CISCO-DMN-DSG-CI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-CI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:18 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGCI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12)
)
ciscoDSGCI.setRevisions(
        ("2012-03-20 08:00",
         "2010-10-13 08:00",
         "2010-08-30 09:00",
         "2010-04-12 09:00",
         "2010-03-22 05:00",
         "2010-02-12 12:00",
         "2009-12-07 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiTable_ObjectIdentity = ObjectIdentity
ciTable = _CiTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2)
)
_CiConfigTable_Object = MibTable
ciConfigTable = _CiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1)
)
if mibBuilder.loadTexts:
    ciConfigTable.setStatus("current")
_CiConfigEntry_Object = MibTableRow
ciConfigEntry = _CiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1)
)
ciConfigEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-CI-MIB", "ciConfigInstance"),
)
if mibBuilder.loadTexts:
    ciConfigEntry.setStatus("current")


class _CiConfigInstance_Type(Integer32):
    """Custom type ciConfigInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CiConfigInstance_Type.__name__ = "Integer32"
_CiConfigInstance_Object = MibTableColumn
ciConfigInstance = _CiConfigInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1, 1),
    _CiConfigInstance_Type()
)
ciConfigInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciConfigInstance.setStatus("current")


class _CiConfigQuery_Type(Integer32):
    """Custom type ciConfigQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CiConfigQuery_Type.__name__ = "Integer32"
_CiConfigQuery_Object = MibTableColumn
ciConfigQuery = _CiConfigQuery_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1, 2),
    _CiConfigQuery_Type()
)
ciConfigQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciConfigQuery.setStatus("current")


class _CiConfigAutoReset_Type(Integer32):
    """Custom type ciConfigAutoReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CiConfigAutoReset_Type.__name__ = "Integer32"
_CiConfigAutoReset_Object = MibTableColumn
ciConfigAutoReset = _CiConfigAutoReset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1, 3),
    _CiConfigAutoReset_Type()
)
ciConfigAutoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciConfigAutoReset.setStatus("current")


class _CiConfigListMgmt_Type(Integer32):
    """Custom type ciConfigListMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addDelete", 1),
          ("updateAll", 2))
    )


_CiConfigListMgmt_Type.__name__ = "Integer32"
_CiConfigListMgmt_Object = MibTableColumn
ciConfigListMgmt = _CiConfigListMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1, 4),
    _CiConfigListMgmt_Type()
)
ciConfigListMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciConfigListMgmt.setStatus("current")


class _CiConfigOrgNetIDUse_Type(Integer32):
    """Custom type ciConfigOrgNetIDUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CiConfigOrgNetIDUse_Type.__name__ = "Integer32"
_CiConfigOrgNetIDUse_Object = MibTableColumn
ciConfigOrgNetIDUse = _CiConfigOrgNetIDUse_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1, 5),
    _CiConfigOrgNetIDUse_Type()
)
ciConfigOrgNetIDUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciConfigOrgNetIDUse.setStatus("current")


class _CiConfigTransportId_Type(Integer32):
    """Custom type ciConfigTransportId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiConfigTransportId_Type.__name__ = "Integer32"
_CiConfigTransportId_Object = MibTableColumn
ciConfigTransportId = _CiConfigTransportId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1, 6),
    _CiConfigTransportId_Type()
)
ciConfigTransportId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciConfigTransportId.setStatus("current")


class _CiConfigOrgNetID_Type(Integer32):
    """Custom type ciConfigOrgNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiConfigOrgNetID_Type.__name__ = "Integer32"
_CiConfigOrgNetID_Object = MibTableColumn
ciConfigOrgNetID = _CiConfigOrgNetID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1, 7),
    _CiConfigOrgNetID_Type()
)
ciConfigOrgNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciConfigOrgNetID.setStatus("current")


class _CiConfigTsHandling_Type(Integer32):
    """Custom type ciConfigTsHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("entire", 1),
          ("partial", 2))
    )


_CiConfigTsHandling_Type.__name__ = "Integer32"
_CiConfigTsHandling_Object = MibTableColumn
ciConfigTsHandling = _CiConfigTsHandling_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 1, 1, 8),
    _CiConfigTsHandling_Type()
)
ciConfigTsHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciConfigTsHandling.setStatus("current")
_CiProgramDecrTable_Object = MibTable
ciProgramDecrTable = _CiProgramDecrTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 2)
)
if mibBuilder.loadTexts:
    ciProgramDecrTable.setStatus("current")
_CiProgramDecrEntry_Object = MibTableRow
ciProgramDecrEntry = _CiProgramDecrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 2, 1)
)
ciProgramDecrEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-CI-MIB", "ciProgramDecrPEID"),
)
if mibBuilder.loadTexts:
    ciProgramDecrEntry.setStatus("current")


class _CiProgramDecrPEID_Type(Integer32):
    """Custom type ciProgramDecrPEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiProgramDecrPEID_Type.__name__ = "Integer32"
_CiProgramDecrPEID_Object = MibTableColumn
ciProgramDecrPEID = _CiProgramDecrPEID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 2, 1, 1),
    _CiProgramDecrPEID_Type()
)
ciProgramDecrPEID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciProgramDecrPEID.setStatus("current")


class _CiProgramDecrDecrypt_Type(Integer32):
    """Custom type ciProgramDecrDecrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("comp", 3),
          ("off", 1),
          ("on", 2))
    )


_CiProgramDecrDecrypt_Type.__name__ = "Integer32"
_CiProgramDecrDecrypt_Object = MibTableColumn
ciProgramDecrDecrypt = _CiProgramDecrDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 2, 1, 2),
    _CiProgramDecrDecrypt_Type()
)
ciProgramDecrDecrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciProgramDecrDecrypt.setStatus("current")


class _CiProgramDecrCISlot_Type(Integer32):
    """Custom type ciProgramDecrCISlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 2),
          ("top", 1))
    )


_CiProgramDecrCISlot_Type.__name__ = "Integer32"
_CiProgramDecrCISlot_Object = MibTableColumn
ciProgramDecrCISlot = _CiProgramDecrCISlot_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 2, 1, 3),
    _CiProgramDecrCISlot_Type()
)
ciProgramDecrCISlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciProgramDecrCISlot.setStatus("current")
_CiCompConfigTable_Object = MibTable
ciCompConfigTable = _CiCompConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3)
)
if mibBuilder.loadTexts:
    ciCompConfigTable.setStatus("current")
_CiCompConfigEntry_Object = MibTableRow
ciCompConfigEntry = _CiCompConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1)
)
ciCompConfigEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-CI-MIB", "ciCompConfigID"),
)
if mibBuilder.loadTexts:
    ciCompConfigEntry.setStatus("current")


class _CiCompConfigID_Type(Integer32):
    """Custom type ciCompConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiCompConfigID_Type.__name__ = "Integer32"
_CiCompConfigID_Object = MibTableColumn
ciCompConfigID = _CiCompConfigID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1, 1),
    _CiCompConfigID_Type()
)
ciCompConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciCompConfigID.setStatus("current")


class _CiCompConfigPEID_Type(Integer32):
    """Custom type ciCompConfigPEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiCompConfigPEID_Type.__name__ = "Integer32"
_CiCompConfigPEID_Object = MibTableColumn
ciCompConfigPEID = _CiCompConfigPEID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1, 2),
    _CiCompConfigPEID_Type()
)
ciCompConfigPEID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCompConfigPEID.setStatus("current")


class _CiCompConfigMode_Type(Integer32):
    """Custom type ciCompConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pid", 1),
          ("stream", 2))
    )


_CiCompConfigMode_Type.__name__ = "Integer32"
_CiCompConfigMode_Object = MibTableColumn
ciCompConfigMode = _CiCompConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1, 3),
    _CiCompConfigMode_Type()
)
ciCompConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCompConfigMode.setStatus("current")


class _CiCompConfigPID_Type(Integer32):
    """Custom type ciCompConfigPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_CiCompConfigPID_Type.__name__ = "Integer32"
_CiCompConfigPID_Object = MibTableColumn
ciCompConfigPID = _CiCompConfigPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1, 4),
    _CiCompConfigPID_Type()
)
ciCompConfigPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCompConfigPID.setStatus("current")


class _CiCompConfigStreamCategory_Type(Integer32):
    """Custom type ciCompConfigStreamCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("aud", 3),
          ("subt", 4),
          ("ttx", 8),
          ("user", 12),
          ("vid", 2))
    )


_CiCompConfigStreamCategory_Type.__name__ = "Integer32"
_CiCompConfigStreamCategory_Object = MibTableColumn
ciCompConfigStreamCategory = _CiCompConfigStreamCategory_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1, 5),
    _CiCompConfigStreamCategory_Type()
)
ciCompConfigStreamCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCompConfigStreamCategory.setStatus("current")


class _CiCompConfigStreamTypeVal_Type(Integer32):
    """Custom type ciCompConfigStreamTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiCompConfigStreamTypeVal_Type.__name__ = "Integer32"
_CiCompConfigStreamTypeVal_Object = MibTableColumn
ciCompConfigStreamTypeVal = _CiCompConfigStreamTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1, 6),
    _CiCompConfigStreamTypeVal_Type()
)
ciCompConfigStreamTypeVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCompConfigStreamTypeVal.setStatus("current")


class _CiCompConfigStreamInstance_Type(Integer32):
    """Custom type ciCompConfigStreamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CiCompConfigStreamInstance_Type.__name__ = "Integer32"
_CiCompConfigStreamInstance_Object = MibTableColumn
ciCompConfigStreamInstance = _CiCompConfigStreamInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1, 7),
    _CiCompConfigStreamInstance_Type()
)
ciCompConfigStreamInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCompConfigStreamInstance.setStatus("current")
_CiCompConfigRowCmdStatus_Type = RowStatus
_CiCompConfigRowCmdStatus_Object = MibTableColumn
ciCompConfigRowCmdStatus = _CiCompConfigRowCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 3, 1, 8),
    _CiCompConfigRowCmdStatus_Type()
)
ciCompConfigRowCmdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciCompConfigRowCmdStatus.setStatus("current")
_CiCompStatusTable_Object = MibTable
ciCompStatusTable = _CiCompStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4)
)
if mibBuilder.loadTexts:
    ciCompStatusTable.setStatus("current")
_CiCompStatusEntry_Object = MibTableRow
ciCompStatusEntry = _CiCompStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1)
)
ciCompStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-CI-MIB", "ciStatusSlot"),
)
if mibBuilder.loadTexts:
    ciCompStatusEntry.setStatus("current")


class _CiStatusSlot_Type(Integer32):
    """Custom type ciStatusSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 2),
          ("top", 1))
    )


_CiStatusSlot_Type.__name__ = "Integer32"
_CiStatusSlot_Object = MibTableColumn
ciStatusSlot = _CiStatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 1),
    _CiStatusSlot_Type()
)
ciStatusSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciStatusSlot.setStatus("current")


class _CiStatusSysName_Type(DisplayString):
    """Custom type ciStatusSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiStatusSysName_Type.__name__ = "DisplayString"
_CiStatusSysName_Object = MibTableColumn
ciStatusSysName = _CiStatusSysName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 2),
    _CiStatusSysName_Type()
)
ciStatusSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusSysName.setStatus("current")


class _CiStatusMFGID_Type(DisplayString):
    """Custom type ciStatusMFGID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiStatusMFGID_Type.__name__ = "DisplayString"
_CiStatusMFGID_Object = MibTableColumn
ciStatusMFGID = _CiStatusMFGID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 3),
    _CiStatusMFGID_Type()
)
ciStatusMFGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusMFGID.setStatus("current")


class _CiStatusMFGCode_Type(DisplayString):
    """Custom type ciStatusMFGCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiStatusMFGCode_Type.__name__ = "DisplayString"
_CiStatusMFGCode_Object = MibTableColumn
ciStatusMFGCode = _CiStatusMFGCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 4),
    _CiStatusMFGCode_Type()
)
ciStatusMFGCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusMFGCode.setStatus("current")


class _CiStatusSerialNum_Type(DisplayString):
    """Custom type ciStatusSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CiStatusSerialNum_Type.__name__ = "DisplayString"
_CiStatusSerialNum_Object = MibTableColumn
ciStatusSerialNum = _CiStatusSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 5),
    _CiStatusSerialNum_Type()
)
ciStatusSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusSerialNum.setStatus("current")


class _CiStatusHWVer_Type(DisplayString):
    """Custom type ciStatusHWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CiStatusHWVer_Type.__name__ = "DisplayString"
_CiStatusHWVer_Object = MibTableColumn
ciStatusHWVer = _CiStatusHWVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 6),
    _CiStatusHWVer_Type()
)
ciStatusHWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusHWVer.setStatus("current")


class _CiStatusAppVer_Type(DisplayString):
    """Custom type ciStatusAppVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CiStatusAppVer_Type.__name__ = "DisplayString"
_CiStatusAppVer_Object = MibTableColumn
ciStatusAppVer = _CiStatusAppVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 7),
    _CiStatusAppVer_Type()
)
ciStatusAppVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusAppVer.setStatus("current")


class _CiStatusCompany_Type(DisplayString):
    """Custom type ciStatusCompany based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_CiStatusCompany_Type.__name__ = "DisplayString"
_CiStatusCompany_Object = MibTableColumn
ciStatusCompany = _CiStatusCompany_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 8),
    _CiStatusCompany_Type()
)
ciStatusCompany.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusCompany.setStatus("current")


class _CiStatusProdname_Type(DisplayString):
    """Custom type ciStatusProdname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_CiStatusProdname_Type.__name__ = "DisplayString"
_CiStatusProdname_Object = MibTableColumn
ciStatusProdname = _CiStatusProdname_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 9),
    _CiStatusProdname_Type()
)
ciStatusProdname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusProdname.setStatus("current")


class _CiStatusCamStatus_Type(Integer32):
    """Custom type ciStatusCamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 1),
          ("ready", 2))
    )


_CiStatusCamStatus_Type.__name__ = "Integer32"
_CiStatusCamStatus_Object = MibTableColumn
ciStatusCamStatus = _CiStatusCamStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 4, 1, 10),
    _CiStatusCamStatus_Type()
)
ciStatusCamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciStatusCamStatus.setStatus("current")
_CiSystemIDTable_Object = MibTable
ciSystemIDTable = _CiSystemIDTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 5)
)
if mibBuilder.loadTexts:
    ciSystemIDTable.setStatus("current")
_CiSystemIDEntry_Object = MibTableRow
ciSystemIDEntry = _CiSystemIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 5, 1)
)
ciSystemIDEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-CI-MIB", "ciSystemIDSlot"),
    (0, "CISCO-DMN-DSG-CI-MIB", "ciSystemIDIndex"),
)
if mibBuilder.loadTexts:
    ciSystemIDEntry.setStatus("current")


class _CiSystemIDSlot_Type(Integer32):
    """Custom type ciSystemIDSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 2),
          ("top", 1))
    )


_CiSystemIDSlot_Type.__name__ = "Integer32"
_CiSystemIDSlot_Object = MibTableColumn
ciSystemIDSlot = _CiSystemIDSlot_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 5, 1, 1),
    _CiSystemIDSlot_Type()
)
ciSystemIDSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciSystemIDSlot.setStatus("current")


class _CiSystemIDIndex_Type(Integer32):
    """Custom type ciSystemIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiSystemIDIndex_Type.__name__ = "Integer32"
_CiSystemIDIndex_Object = MibTableColumn
ciSystemIDIndex = _CiSystemIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 5, 1, 2),
    _CiSystemIDIndex_Type()
)
ciSystemIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciSystemIDIndex.setStatus("current")


class _CiSystemIDName_Type(DisplayString):
    """Custom type ciSystemIDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiSystemIDName_Type.__name__ = "DisplayString"
_CiSystemIDName_Object = MibTableColumn
ciSystemIDName = _CiSystemIDName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 5, 1, 3),
    _CiSystemIDName_Type()
)
ciSystemIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciSystemIDName.setStatus("current")


class _CiSystemID_Type(DisplayString):
    """Custom type ciSystemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiSystemID_Type.__name__ = "DisplayString"
_CiSystemID_Object = MibTableColumn
ciSystemID = _CiSystemID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 5, 1, 4),
    _CiSystemID_Type()
)
ciSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciSystemID.setStatus("current")


class _CiSystemSysNameID_Type(DisplayString):
    """Custom type ciSystemSysNameID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_CiSystemSysNameID_Type.__name__ = "DisplayString"
_CiSystemSysNameID_Object = MibTableColumn
ciSystemSysNameID = _CiSystemSysNameID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 12, 2, 5, 1, 5),
    _CiSystemSysNameID_Type()
)
ciSystemSysNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciSystemSysNameID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-CI-MIB",
    **{"ciscoDSGCI": ciscoDSGCI,
       "ciTable": ciTable,
       "ciConfigTable": ciConfigTable,
       "ciConfigEntry": ciConfigEntry,
       "ciConfigInstance": ciConfigInstance,
       "ciConfigQuery": ciConfigQuery,
       "ciConfigAutoReset": ciConfigAutoReset,
       "ciConfigListMgmt": ciConfigListMgmt,
       "ciConfigOrgNetIDUse": ciConfigOrgNetIDUse,
       "ciConfigTransportId": ciConfigTransportId,
       "ciConfigOrgNetID": ciConfigOrgNetID,
       "ciConfigTsHandling": ciConfigTsHandling,
       "ciProgramDecrTable": ciProgramDecrTable,
       "ciProgramDecrEntry": ciProgramDecrEntry,
       "ciProgramDecrPEID": ciProgramDecrPEID,
       "ciProgramDecrDecrypt": ciProgramDecrDecrypt,
       "ciProgramDecrCISlot": ciProgramDecrCISlot,
       "ciCompConfigTable": ciCompConfigTable,
       "ciCompConfigEntry": ciCompConfigEntry,
       "ciCompConfigID": ciCompConfigID,
       "ciCompConfigPEID": ciCompConfigPEID,
       "ciCompConfigMode": ciCompConfigMode,
       "ciCompConfigPID": ciCompConfigPID,
       "ciCompConfigStreamCategory": ciCompConfigStreamCategory,
       "ciCompConfigStreamTypeVal": ciCompConfigStreamTypeVal,
       "ciCompConfigStreamInstance": ciCompConfigStreamInstance,
       "ciCompConfigRowCmdStatus": ciCompConfigRowCmdStatus,
       "ciCompStatusTable": ciCompStatusTable,
       "ciCompStatusEntry": ciCompStatusEntry,
       "ciStatusSlot": ciStatusSlot,
       "ciStatusSysName": ciStatusSysName,
       "ciStatusMFGID": ciStatusMFGID,
       "ciStatusMFGCode": ciStatusMFGCode,
       "ciStatusSerialNum": ciStatusSerialNum,
       "ciStatusHWVer": ciStatusHWVer,
       "ciStatusAppVer": ciStatusAppVer,
       "ciStatusCompany": ciStatusCompany,
       "ciStatusProdname": ciStatusProdname,
       "ciStatusCamStatus": ciStatusCamStatus,
       "ciSystemIDTable": ciSystemIDTable,
       "ciSystemIDEntry": ciSystemIDEntry,
       "ciSystemIDSlot": ciSystemIDSlot,
       "ciSystemIDIndex": ciSystemIDIndex,
       "ciSystemIDName": ciSystemIDName,
       "ciSystemID": ciSystemID,
       "ciSystemSysNameID": ciSystemSysNameID}
)
