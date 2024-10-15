# SNMP MIB module (PAIRGAIN-COMMON-HD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-COMMON-HD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:49 2024
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

_Pairgain_ObjectIdentity = ObjectIdentity
pairgain = _Pairgain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1)
)
_PgainOHdsl_ObjectIdentity = ObjectIdentity
pgainOHdsl = _PgainOHdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 1)
)
_PgainAgent_ObjectIdentity = ObjectIdentity
pgainAgent = _PgainAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 2)
)
_PgainCampus_ObjectIdentity = ObjectIdentity
pgainCampus = _PgainCampus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 3)
)
_PgCampusChassis_ObjectIdentity = ObjectIdentity
pgCampusChassis = _PgCampusChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 3, 1)
)
_PgCampusCmu_ObjectIdentity = ObjectIdentity
pgCampusCmu = _PgCampusCmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 3, 2)
)
_PgCampusLocLu_ObjectIdentity = ObjectIdentity
pgCampusLocLu = _PgCampusLocLu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 3, 3)
)
_PgCampusRemUnit_ObjectIdentity = ObjectIdentity
pgCampusRemUnit = _PgCampusRemUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 3, 4)
)
_PgCampusDoubler1_ObjectIdentity = ObjectIdentity
pgCampusDoubler1 = _PgCampusDoubler1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 3, 5)
)
_PgCampusDoubler2_ObjectIdentity = ObjectIdentity
pgCampusDoubler2 = _PgCampusDoubler2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 3, 6)
)
_PgainHigain_ObjectIdentity = ObjectIdentity
pgainHigain = _PgainHigain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 4)
)
_PgHigainChassis_ObjectIdentity = ObjectIdentity
pgHigainChassis = _PgHigainChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 4, 1)
)
_PgainREX_ObjectIdentity = ObjectIdentity
pgainREX = _PgainREX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 5)
)
_PgainETSI_ObjectIdentity = ObjectIdentity
pgainETSI = _PgainETSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 6)
)
_PgETSIChassis_ObjectIdentity = ObjectIdentity
pgETSIChassis = _PgETSIChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 6, 1)
)
_PgainHDSL_ObjectIdentity = ObjectIdentity
pgainHDSL = _PgainHDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 7)
)
_PgainEPhone_ObjectIdentity = ObjectIdentity
pgainEPhone = _PgainEPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 8)
)
_PgEPhoneChassis_ObjectIdentity = ObjectIdentity
pgEPhoneChassis = _PgEPhoneChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 1)
)
_PgEPhoneLocUnit_ObjectIdentity = ObjectIdentity
pgEPhoneLocUnit = _PgEPhoneLocUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2)
)
_PgEPhoneRemUnit_ObjectIdentity = ObjectIdentity
pgEPhoneRemUnit = _PgEPhoneRemUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3)
)
_PgainDSLAM_ObjectIdentity = ObjectIdentity
pgainDSLAM = _PgainDSLAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9)
)
_PgDSLAMChassis_ObjectIdentity = ObjectIdentity
pgDSLAMChassis = _PgDSLAMChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 1)
)
_PgLantMIB_ObjectIdentity = ObjectIdentity
pgLantMIB = _PgLantMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2)
)
_PgDSLAMAlarmSeverity_ObjectIdentity = ObjectIdentity
pgDSLAMAlarmSeverity = _PgDSLAMAlarmSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 3)
)
_PgDSLAMAlarm_ObjectIdentity = ObjectIdentity
pgDSLAMAlarm = _PgDSLAMAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 4)
)
_PgDSLAMFlashMIB_ObjectIdentity = ObjectIdentity
pgDSLAMFlashMIB = _PgDSLAMFlashMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5)
)
_PgService_ObjectIdentity = ObjectIdentity
pgService = _PgService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6)
)
_PgIpoaRouteMIB_ObjectIdentity = ObjectIdentity
pgIpoaRouteMIB = _PgIpoaRouteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 7)
)
_PgsessionMIB_ObjectIdentity = ObjectIdentity
pgsessionMIB = _PgsessionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8)
)
_PgATMTestMIB_ObjectIdentity = ObjectIdentity
pgATMTestMIB = _PgATMTestMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9)
)
_PgIpAccessMIB_ObjectIdentity = ObjectIdentity
pgIpAccessMIB = _PgIpAccessMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 10)
)
_PgUpcMIB_ObjectIdentity = ObjectIdentity
pgUpcMIB = _PgUpcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11)
)
_PgApsMIB_ObjectIdentity = ObjectIdentity
pgApsMIB = _PgApsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 12)
)
_PgIISPMIB_ObjectIdentity = ObjectIdentity
pgIISPMIB = _PgIISPMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13)
)
_AvSubtendMIB_ObjectIdentity = ObjectIdentity
avSubtendMIB = _AvSubtendMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 14)
)
_PgAtmTcMIB_ObjectIdentity = ObjectIdentity
pgAtmTcMIB = _PgAtmTcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16)
)
_Pgds1Mib_ObjectIdentity = ObjectIdentity
pgds1Mib = _Pgds1Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 17)
)
_PgBackupMIB_ObjectIdentity = ObjectIdentity
pgBackupMIB = _PgBackupMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19)
)
_PgainSysLog_ObjectIdentity = ObjectIdentity
pgainSysLog = _PgainSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 10)
)
_PgainTiger_ObjectIdentity = ObjectIdentity
pgainTiger = _PgainTiger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 11)
)
_PgTigerMIB_ObjectIdentity = ObjectIdentity
pgTigerMIB = _PgTigerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 11, 1)
)
_PgainADSL_ObjectIdentity = ObjectIdentity
pgainADSL = _PgainADSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 12)
)
_PgainSDSL_ObjectIdentity = ObjectIdentity
pgainSDSL = _PgainSDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 13)
)
_PgainSDSLCell_ObjectIdentity = ObjectIdentity
pgainSDSLCell = _PgainSDSLCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 14)
)
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 2)
)
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3)
)
_Pgreg_other_ObjectIdentity = ObjectIdentity
pgreg_other = _Pgreg_other_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 1)
)
_Pgreg_campus_ObjectIdentity = ObjectIdentity
pgreg_campus = _Pgreg_campus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 2)
)
_Pgreg_Cmu_ObjectIdentity = ObjectIdentity
pgreg_Cmu = _Pgreg_Cmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 2, 1)
)
_Pgreg_higain_ObjectIdentity = ObjectIdentity
pgreg_higain = _Pgreg_higain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 3)
)
_Pgreg_Hmu_ObjectIdentity = ObjectIdentity
pgreg_Hmu = _Pgreg_Hmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 3, 1)
)
_Pgreg_ebridge_ObjectIdentity = ObjectIdentity
pgreg_ebridge = _Pgreg_ebridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 4)
)
_Pgreg_EBM_ObjectIdentity = ObjectIdentity
pgreg_EBM = _Pgreg_EBM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 4, 1)
)
_Pgreg_ETSI_ObjectIdentity = ObjectIdentity
pgreg_ETSI = _Pgreg_ETSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 5)
)
_Pgreg_Emu_ObjectIdentity = ObjectIdentity
pgreg_Emu = _Pgreg_Emu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 5, 1)
)
_Pgreg_EPhone_ObjectIdentity = ObjectIdentity
pgreg_EPhone = _Pgreg_EPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 6)
)
_Pgreg_EPmu_ObjectIdentity = ObjectIdentity
pgreg_EPmu = _Pgreg_EPmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 6, 1)
)
_Pgreg_DSLAM_ObjectIdentity = ObjectIdentity
pgreg_DSLAM = _Pgreg_DSLAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 7)
)
_PgAvidia8000_ObjectIdentity = ObjectIdentity
pgAvidia8000 = _PgAvidia8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 7, 1)
)
_PgAvidia3000_ObjectIdentity = ObjectIdentity
pgAvidia3000 = _PgAvidia3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 7, 2)
)
_PgAvidia2200_ObjectIdentity = ObjectIdentity
pgAvidia2200 = _PgAvidia2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 7, 3)
)
_Pgreg_Tiger_ObjectIdentity = ObjectIdentity
pgreg_Tiger = _Pgreg_Tiger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 3, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    **{"pairgain": pairgain,
       "products": products,
       "pgainOHdsl": pgainOHdsl,
       "pgainAgent": pgainAgent,
       "pgainCampus": pgainCampus,
       "pgCampusChassis": pgCampusChassis,
       "pgCampusCmu": pgCampusCmu,
       "pgCampusLocLu": pgCampusLocLu,
       "pgCampusRemUnit": pgCampusRemUnit,
       "pgCampusDoubler1": pgCampusDoubler1,
       "pgCampusDoubler2": pgCampusDoubler2,
       "pgainHigain": pgainHigain,
       "pgHigainChassis": pgHigainChassis,
       "pgainREX": pgainREX,
       "pgainETSI": pgainETSI,
       "pgETSIChassis": pgETSIChassis,
       "pgainHDSL": pgainHDSL,
       "pgainEPhone": pgainEPhone,
       "pgEPhoneChassis": pgEPhoneChassis,
       "pgEPhoneLocUnit": pgEPhoneLocUnit,
       "pgEPhoneRemUnit": pgEPhoneRemUnit,
       "pgainDSLAM": pgainDSLAM,
       "pgDSLAMChassis": pgDSLAMChassis,
       "pgLantMIB": pgLantMIB,
       "pgDSLAMAlarmSeverity": pgDSLAMAlarmSeverity,
       "pgDSLAMAlarm": pgDSLAMAlarm,
       "pgDSLAMFlashMIB": pgDSLAMFlashMIB,
       "pgService": pgService,
       "pgIpoaRouteMIB": pgIpoaRouteMIB,
       "pgsessionMIB": pgsessionMIB,
       "pgATMTestMIB": pgATMTestMIB,
       "pgIpAccessMIB": pgIpAccessMIB,
       "pgUpcMIB": pgUpcMIB,
       "pgApsMIB": pgApsMIB,
       "pgIISPMIB": pgIISPMIB,
       "avSubtendMIB": avSubtendMIB,
       "pgAtmTcMIB": pgAtmTcMIB,
       "pgds1Mib": pgds1Mib,
       "pgBackupMIB": pgBackupMIB,
       "pgainSysLog": pgainSysLog,
       "pgainTiger": pgainTiger,
       "pgTigerMIB": pgTigerMIB,
       "pgainADSL": pgainADSL,
       "pgainSDSL": pgainSDSL,
       "pgainSDSLCell": pgainSDSLCell,
       "temporary": temporary,
       "registration": registration,
       "pgreg-other": pgreg_other,
       "pgreg-campus": pgreg_campus,
       "pgreg-Cmu": pgreg_Cmu,
       "pgreg-higain": pgreg_higain,
       "pgreg-Hmu": pgreg_Hmu,
       "pgreg-ebridge": pgreg_ebridge,
       "pgreg-EBM": pgreg_EBM,
       "pgreg-ETSI": pgreg_ETSI,
       "pgreg-Emu": pgreg_Emu,
       "pgreg-EPhone": pgreg_EPhone,
       "pgreg-EPmu": pgreg_EPmu,
       "pgreg-DSLAM": pgreg_DSLAM,
       "pgAvidia8000": pgAvidia8000,
       "pgAvidia3000": pgAvidia3000,
       "pgAvidia2200": pgAvidia2200,
       "pgreg-Tiger": pgreg_Tiger}
)
