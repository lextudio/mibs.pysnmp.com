# SNMP MIB module (MWRM-UNIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MWRM-UNIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:10 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class EnableDisable(Integer32):
    """Custom type EnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )





class EnableDisableSMI2(Integer32):
    """Custom type EnableDisableSMI2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )





class OffOn(Integer32):
    """Custom type OffOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )





class MetricImperial(Integer32):
    """Custom type MetricImperial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("imperial", 1),
          ("metric", 0))
    )





class AllowedNotAllowed(Integer32):
    """Custom type AllowedNotAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("not-allowed", 0))
    )





class NoYes(Integer32):
    """Custom type NoYes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )





class DownUp(Integer32):
    """Custom type DownUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )





class SupportedNotsupported(Integer32):
    """Custom type SupportedNotsupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 3),
          ("supported", 2))
    )





class ProgressStatus(Integer32):
    """Custom type ProgressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("inProgress", 1),
          ("ready", 0),
          ("success", 2))
    )





class Severity(Integer32):
    """Custom type Severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 5),
          ("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )





class TrailIfType(Integer32):
    """Custom type TrailIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("line", 0),
          ("radio", 1),
          ("stm-1-oc-3", 2),
          ("sync", 4),
          ("unknown", -1))
    )





class PmTableType(Integer32):
    """Custom type PmTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pm15min", 2),
          ("pm15mincurr", 1),
          ("pm24hr", 4),
          ("pm24hrcurr", 3))
    )





class RateMbps(Integer32):
    """Custom type RateMbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n10", 0),
          ("n100", 1),
          ("n1000", 2),
          ("not-applicable", -1))
    )





class HalfFull(Integer32):
    """Custom type HalfFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("full", 1),
          ("half", 0),
          ("not-applicable", -1))
    )





class BerLevel(Integer32):
    """Custom type BerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n1e-3", 2),
          ("n1e-4", 3),
          ("n1e-5", 4))
    )





class SignalLevel(Integer32):
    """Custom type SignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("n1e-6", 5),
          ("n1e-7", 6),
          ("n1e-8", 7),
          ("n1e-9", 8))
    )





class Exponent(Integer32):
    """Custom type Exponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("n1e-0", 18),
          ("n1e-10", 9),
          ("n1e-11", 10),
          ("n1e-12", 11),
          ("n1e-13", 12),
          ("n1e-14", 13),
          ("n1e-15", 14),
          ("n1e-16", 15),
          ("n1e-17", 16),
          ("n1e-18", 17),
          ("n1e-2", 1),
          ("n1e-3", 2),
          ("n1e-4", 3),
          ("n1e-5", 4),
          ("n1e-6", 5),
          ("n1e-7", 6),
          ("n1e-8", 7),
          ("n1e-9", 8))
    )





class LoopbackType(Integer32):
    """Custom type LoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("towardsLine", 1),
          ("towardsRadio", 2))
    )





class QueueName(Integer32):
    """Custom type QueueName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("first-queue", 0),
          ("fourth-queue", 3),
          ("none", 4),
          ("second-queue", 1),
          ("third-queue", 2))
    )





class RadioId(Integer32):
    """Custom type RadioId based on Integer32"""




class RfuId(Integer32):
    """Custom type RfuId based on Integer32"""




class SwCommand(Integer32):
    """Custom type SwCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("downgrade", 4),
          ("downloadDowngradeVersion", 5),
          ("downloadUpgradeVersion", 1),
          ("noOperation", 0),
          ("rollback", 3),
          ("upgrade", 2))
    )





class TrailProtectedType(Integer32):
    """Custom type TrailProtectedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )





class ClockSrc(Integer32):
    """Custom type ClockSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local-clock", 0),
          ("system-clock-source", 1))
    )





class SlotId(Integer32):
    """Custom type SlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("slot1", 1),
          ("slot10", 10),
          ("slot11", 11),
          ("slot12", 12),
          ("slot2", 2),
          ("slot3", 3),
          ("slot4", 4),
          ("slot5", 5),
          ("slot6", 6),
          ("slot7", 7),
          ("slot8", 8),
          ("slot9", 9),
          ("standalone", 0))
    )





class Integrity(Integer32):
    """Custom type Integrity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integrity", 0),
          ("nointegrity", 1))
    )





class GreenYellow(Integer32):
    """Custom type GreenYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("yellow", 1))
    )





class InputSeverity(Integer32):
    """Custom type InputSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )





class SwCommandTimer(Integer32):
    """Custom type SwCommandTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("abortTimedInstallation", 9),
          ("downgrade", 4),
          ("downgradeTimer", 8),
          ("downloadDowngradeVersion", 5),
          ("downloadUpgradeVersion", 1),
          ("noOperation", 0),
          ("rollback", 3),
          ("rollbackTimer", 7),
          ("upgrade", 2),
          ("upgradeTimer", 6))
    )





class FileTransferStatus(Integer32):
    """Custom type FileTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("inTransfer", 1),
          ("ready", 0),
          ("success", 3))
    )





class FileRestoreStatus(Integer32):
    """Custom type FileRestoreStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("ready", 0),
          ("restoring-configuration", 1),
          ("success", 3))
    )





class RbacAccessLevel(Integer32):
    """Custom type RbacAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advance", 2),
          ("none", 0),
          ("normal", 1))
    )





class InventoryCardType(Integer32):
    """Custom type InventoryCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              11,
              12,
              13,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56)
        )
    )
    namedValues = NamedValues(
        *(("capacityBooster", 31),
          ("chassis1U2U", 30),
          ("cleared", 0),
          ("eLicEth4x1GEA", 29),
          ("essFpga", 45),
          ("fan1U", 37),
          ("fan2U", 36),
          ("ip20cEband", 53),
          ("ip20g", 47),
          ("licStm1oc3rst", 51),
          ("licXe4opt", 48),
          ("nativeTdm16xE1T1", 25),
          ("nexusDc", 12),
          ("nexusQc", 13),
          ("nexusSc", 10),
          ("nexusScLp", 11),
          ("pdc24v1uDualFeed", 41),
          ("pdc24v1uSingleFeed", 40),
          ("pdc24v2uSingleFeed", 39),
          ("pdc48v1uDualFeed", 35),
          ("pdc48v1uSingleFeed", 34),
          ("pdc48v2uSingleFeed", 33),
          ("pwe3-16xE1T1", 26),
          ("pwe3-1xSTM1", 32),
          ("ricE", 43),
          ("rmcA", 22),
          ("rmcB", 23),
          ("rmcE", 50),
          ("rmcNDc", 24),
          ("tccA", 20),
          ("tccA2", 54),
          ("tccA2mc", 55),
          ("tccAmc", 52),
          ("tccB", 21),
          ("tccB2", 56),
          ("tccBmc", 49),
          ("tccR", 19),
          ("tdm1xOc3", 28),
          ("tdm1xStm1", 27),
          ("test-card", 38),
          ("trafficFpga", 44),
          ("tressFpga", 46),
          ("unknownCard", 42))
    )





class FtpProtocolType(Integer32):
    """Custom type FtpProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("sftp", 1))
    )





class CfgUnitInfoOper(Integer32):
    """Custom type CfgUnitInfoOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create-pakcge", 1),
          ("export-pakcge", 2),
          ("invalid-operation", 0))
    )





class CfgOper(Integer32):
    """Custom type CfgOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("delete", 3),
          ("export", 5),
          ("import", 4),
          ("invalid-operation", 0),
          ("restore", 2))
    )





class CardOccupancy(Integer32):
    """Custom type CardOccupancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("equipped", 2),
          ("not-operational", 3))
    )





class OperState(Integer32):
    """Custom type OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("init", 2),
          ("loaded", 4),
          ("loading", 3),
          ("up", 5),
          ("up-with-alarms", 6))
    )





class LicenseGeneric(Integer32):
    """Custom type LicenseGeneric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100000,
              100001,
              100010,
              100011,
              100020,
              100021,
              100022,
              100023,
              100024,
              100025)
        )
    )
    namedValues = NamedValues(
        *(("access-cet", 100024),
          ("aggregation-cet", 100025),
          ("allowed", 100001),
          ("disable", 100010),
          ("edge-cet", 100023),
          ("enable", 100011),
          ("enhanced-pipe", 100022),
          ("not-allowed", 100000),
          ("only-management", 100020),
          ("smart-pipe", 100021))
    )





class RaduisAcceaaLevel(Integer32):
    """Custom type RaduisAcceaaLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 2),
          ("none", 0),
          ("normal", 1),
          ("root", 3))
    )





class VmResetType(Integer32):
    """Custom type VmResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("card-cold-reset", 5),
          ("card-warm-reset", 4),
          ("main-board-cold-reset", 3),
          ("main-board-warm-reset", 1),
          ("no-reset", 0),
          ("not-applicable-reset", 6),
          ("tcc-cold-reset", 2))
    )





class FTStatus(Integer32):
    """Custom type FTStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("file-in-transfer", 1),
          ("ready", 0),
          ("success", 3))
    )





class CsrCertificateFTState(Integer32):
    """Custom type CsrCertificateFTState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("no-operation", 0),
          ("upload", 1))
    )





class CsrFileFormat(Integer32):
    """Custom type CsrFileFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("der", 2),
          ("pem", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Microwave_radio_ObjectIdentity = ObjectIdentity
microwave_radio = _Microwave_radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281)
)
_GenEquip_ObjectIdentity = ObjectIdentity
genEquip = _GenEquip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10)
)
_GenEquipUnit_ObjectIdentity = ObjectIdentity
genEquipUnit = _GenEquipUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1)
)
_GenEquipUnitInfo_ObjectIdentity = ObjectIdentity
genEquipUnitInfo = _GenEquipUnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1)
)
_GenEquipLastCfgTimeStamp_Type = Integer32
_GenEquipLastCfgTimeStamp_Object = MibScalar
genEquipLastCfgTimeStamp = _GenEquipLastCfgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 1),
    _GenEquipLastCfgTimeStamp_Type()
)
genEquipLastCfgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipLastCfgTimeStamp.setStatus("mandatory")


class _GenEquipRealTimeandDate_Type(OctetString):
    """Custom type genEquipRealTimeandDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GenEquipRealTimeandDate_Type.__name__ = "OctetString"
_GenEquipRealTimeandDate_Object = MibScalar
genEquipRealTimeandDate = _GenEquipRealTimeandDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 2),
    _GenEquipRealTimeandDate_Type()
)
genEquipRealTimeandDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRealTimeandDate.setStatus("mandatory")
_GenEquipPMGenTime_Type = Integer32
_GenEquipPMGenTime_Object = MibScalar
genEquipPMGenTime = _GenEquipPMGenTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 3),
    _GenEquipPMGenTime_Type()
)
genEquipPMGenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPMGenTime.setStatus("mandatory")
_GenEquipInvGenTime_Type = Integer32
_GenEquipInvGenTime_Object = MibScalar
genEquipInvGenTime = _GenEquipInvGenTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 4),
    _GenEquipInvGenTime_Type()
)
genEquipInvGenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipInvGenTime.setStatus("mandatory")


class _GenEquipOperation_Type(Integer32):
    """Custom type genEquipOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idcHwReset", 1),
          ("noAction", 0))
    )


_GenEquipOperation_Type.__name__ = "Integer32"
_GenEquipOperation_Object = MibScalar
genEquipOperation = _GenEquipOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 5),
    _GenEquipOperation_Type()
)
genEquipOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipOperation.setStatus("mandatory")
_GenEquipMIBVersion_Type = DisplayString
_GenEquipMIBVersion_Object = MibScalar
genEquipMIBVersion = _GenEquipMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 6),
    _GenEquipMIBVersion_Type()
)
genEquipMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMIBVersion.setStatus("mandatory")


class _GenEquipUnitCLLI_Type(DisplayString):
    """Custom type genEquipUnitCLLI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GenEquipUnitCLLI_Type.__name__ = "DisplayString"
_GenEquipUnitCLLI_Object = MibScalar
genEquipUnitCLLI = _GenEquipUnitCLLI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 7),
    _GenEquipUnitCLLI_Type()
)
genEquipUnitCLLI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitCLLI.setStatus("mandatory")
_GenEquipUnitMeasurementSystem_Type = MetricImperial
_GenEquipUnitMeasurementSystem_Object = MibScalar
genEquipUnitMeasurementSystem = _GenEquipUnitMeasurementSystem_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 8),
    _GenEquipUnitMeasurementSystem_Type()
)
genEquipUnitMeasurementSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitMeasurementSystem.setStatus("mandatory")
_GenEquipUnitIduTemperature_Type = Integer32
_GenEquipUnitIduTemperature_Object = MibScalar
genEquipUnitIduTemperature = _GenEquipUnitIduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 9),
    _GenEquipUnitIduTemperature_Type()
)
genEquipUnitIduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitIduTemperature.setStatus("mandatory")
_GenEquipUnitIduVoltageInput_Type = Integer32
_GenEquipUnitIduVoltageInput_Object = MibScalar
genEquipUnitIduVoltageInput = _GenEquipUnitIduVoltageInput_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 10),
    _GenEquipUnitIduVoltageInput_Type()
)
genEquipUnitIduVoltageInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitIduVoltageInput.setStatus("mandatory")
_GenEquipUnitInfoTime_ObjectIdentity = ObjectIdentity
genEquipUnitInfoTime = _GenEquipUnitInfoTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11)
)


class _GenEquipUnitGMTHours_Type(Integer32):
    """Custom type genEquipUnitGMTHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_GenEquipUnitGMTHours_Type.__name__ = "Integer32"
_GenEquipUnitGMTHours_Object = MibScalar
genEquipUnitGMTHours = _GenEquipUnitGMTHours_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 1),
    _GenEquipUnitGMTHours_Type()
)
genEquipUnitGMTHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitGMTHours.setStatus("mandatory")


class _GenEquipUnitGMTMins_Type(Integer32):
    """Custom type genEquipUnitGMTMins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_GenEquipUnitGMTMins_Type.__name__ = "Integer32"
_GenEquipUnitGMTMins_Object = MibScalar
genEquipUnitGMTMins = _GenEquipUnitGMTMins_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 2),
    _GenEquipUnitGMTMins_Type()
)
genEquipUnitGMTMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitGMTMins.setStatus("mandatory")
_GenEquipUnitInfoNTP_ObjectIdentity = ObjectIdentity
genEquipUnitInfoNTP = _GenEquipUnitInfoNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6)
)
_GenEquipUnitInfoNTPAdmin_Type = EnableDisable
_GenEquipUnitInfoNTPAdmin_Object = MibScalar
genEquipUnitInfoNTPAdmin = _GenEquipUnitInfoNTPAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 1),
    _GenEquipUnitInfoNTPAdmin_Type()
)
genEquipUnitInfoNTPAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoNTPAdmin.setStatus("mandatory")
_GenEquipUnitInfoNTPServerIP_Type = IpAddress
_GenEquipUnitInfoNTPServerIP_Object = MibScalar
genEquipUnitInfoNTPServerIP = _GenEquipUnitInfoNTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 2),
    _GenEquipUnitInfoNTPServerIP_Type()
)
genEquipUnitInfoNTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoNTPServerIP.setStatus("mandatory")


class _GenEquipUnitInfoNTPStatus_Type(Integer32):
    """Custom type genEquipUnitInfoNTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_GenEquipUnitInfoNTPStatus_Type.__name__ = "Integer32"
_GenEquipUnitInfoNTPStatus_Object = MibScalar
genEquipUnitInfoNTPStatus = _GenEquipUnitInfoNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 3),
    _GenEquipUnitInfoNTPStatus_Type()
)
genEquipUnitInfoNTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoNTPStatus.setStatus("mandatory")
_GenEquipUnitInfoNTPSync_Type = DisplayString
_GenEquipUnitInfoNTPSync_Object = MibScalar
genEquipUnitInfoNTPSync = _GenEquipUnitInfoNTPSync_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 4),
    _GenEquipUnitInfoNTPSync_Type()
)
genEquipUnitInfoNTPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoNTPSync.setStatus("mandatory")


class _GenEquipUnitInfoNTPPollInterval_Type(Integer32):
    """Custom type genEquipUnitInfoNTPPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024),
    )


_GenEquipUnitInfoNTPPollInterval_Type.__name__ = "Integer32"
_GenEquipUnitInfoNTPPollInterval_Object = MibScalar
genEquipUnitInfoNTPPollInterval = _GenEquipUnitInfoNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 5),
    _GenEquipUnitInfoNTPPollInterval_Type()
)
genEquipUnitInfoNTPPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoNTPPollInterval.setStatus("mandatory")
_GenEquipUnitInfoNtpStatusTable_Object = MibTable
genEquipUnitInfoNtpStatusTable = _GenEquipUnitInfoNtpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 6)
)
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpStatusTable.setStatus("mandatory")
_GenEquipUnitInfoNtpStatusEntry_Object = MibTableRow
genEquipUnitInfoNtpStatusEntry = _GenEquipUnitInfoNtpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 6, 1)
)
genEquipUnitInfoNtpStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitInfoNtpStatusIndex"),
)
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpStatusEntry.setStatus("mandatory")
_GenEquipUnitInfoNtpStatusIndex_Type = Integer32
_GenEquipUnitInfoNtpStatusIndex_Object = MibTableColumn
genEquipUnitInfoNtpStatusIndex = _GenEquipUnitInfoNtpStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 6, 1, 1),
    _GenEquipUnitInfoNtpStatusIndex_Type()
)
genEquipUnitInfoNtpStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpStatusIndex.setStatus("mandatory")


class _GenEquipUnitInfoNtpStatusPollInterval_Type(Integer32):
    """Custom type genEquipUnitInfoNtpStatusPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_GenEquipUnitInfoNtpStatusPollInterval_Type.__name__ = "Integer32"
_GenEquipUnitInfoNtpStatusPollInterval_Object = MibTableColumn
genEquipUnitInfoNtpStatusPollInterval = _GenEquipUnitInfoNtpStatusPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 6, 1, 2),
    _GenEquipUnitInfoNtpStatusPollInterval_Type()
)
genEquipUnitInfoNtpStatusPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpStatusPollInterval.setStatus("mandatory")
_GenEquipUnitInfoNtpStatusSyncServerIP_Type = IpAddress
_GenEquipUnitInfoNtpStatusSyncServerIP_Object = MibTableColumn
genEquipUnitInfoNtpStatusSyncServerIP = _GenEquipUnitInfoNtpStatusSyncServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 6, 1, 3),
    _GenEquipUnitInfoNtpStatusSyncServerIP_Type()
)
genEquipUnitInfoNtpStatusSyncServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpStatusSyncServerIP.setStatus("mandatory")


class _GenEquipUnitInfoNtpStatusLockState_Type(Integer32):
    """Custom type genEquipUnitInfoNtpStatusLockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("locked", 2),
          ("none", 0))
    )


_GenEquipUnitInfoNtpStatusLockState_Type.__name__ = "Integer32"
_GenEquipUnitInfoNtpStatusLockState_Object = MibTableColumn
genEquipUnitInfoNtpStatusLockState = _GenEquipUnitInfoNtpStatusLockState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 6, 1, 4),
    _GenEquipUnitInfoNtpStatusLockState_Type()
)
genEquipUnitInfoNtpStatusLockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpStatusLockState.setStatus("mandatory")
_GenEquipUnitInfoNtpConfigTable_Object = MibTable
genEquipUnitInfoNtpConfigTable = _GenEquipUnitInfoNtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 7)
)
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpConfigTable.setStatus("mandatory")
_GenEquipUnitInfoNtpConfigEntry_Object = MibTableRow
genEquipUnitInfoNtpConfigEntry = _GenEquipUnitInfoNtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 7, 1)
)
genEquipUnitInfoNtpConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitInfoNtpConfigIndex"),
)
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpConfigEntry.setStatus("mandatory")
_GenEquipUnitInfoNtpConfigIndex_Type = Integer32
_GenEquipUnitInfoNtpConfigIndex_Object = MibTableColumn
genEquipUnitInfoNtpConfigIndex = _GenEquipUnitInfoNtpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 7, 1, 1),
    _GenEquipUnitInfoNtpConfigIndex_Type()
)
genEquipUnitInfoNtpConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpConfigIndex.setStatus("mandatory")
_GenEquipUnitInfoNtpConfigAdmin_Type = EnableDisable
_GenEquipUnitInfoNtpConfigAdmin_Object = MibTableColumn
genEquipUnitInfoNtpConfigAdmin = _GenEquipUnitInfoNtpConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 7, 1, 2),
    _GenEquipUnitInfoNtpConfigAdmin_Type()
)
genEquipUnitInfoNtpConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpConfigAdmin.setStatus("mandatory")


class _GenEquipUnitInfoNtpConfigVersion_Type(Integer32):
    """Custom type genEquipUnitInfoNtpConfigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntpv3", 1),
          ("ntpv4", 2))
    )


_GenEquipUnitInfoNtpConfigVersion_Type.__name__ = "Integer32"
_GenEquipUnitInfoNtpConfigVersion_Object = MibTableColumn
genEquipUnitInfoNtpConfigVersion = _GenEquipUnitInfoNtpConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 7, 1, 3),
    _GenEquipUnitInfoNtpConfigVersion_Type()
)
genEquipUnitInfoNtpConfigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpConfigVersion.setStatus("mandatory")
_GenEquipUnitInfoNtpConfigServerIPaddress1_Type = IpAddress
_GenEquipUnitInfoNtpConfigServerIPaddress1_Object = MibTableColumn
genEquipUnitInfoNtpConfigServerIPaddress1 = _GenEquipUnitInfoNtpConfigServerIPaddress1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 7, 1, 4),
    _GenEquipUnitInfoNtpConfigServerIPaddress1_Type()
)
genEquipUnitInfoNtpConfigServerIPaddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpConfigServerIPaddress1.setStatus("mandatory")
_GenEquipUnitInfoNtpConfigServerIPaddress2_Type = IpAddress
_GenEquipUnitInfoNtpConfigServerIPaddress2_Object = MibTableColumn
genEquipUnitInfoNtpConfigServerIPaddress2 = _GenEquipUnitInfoNtpConfigServerIPaddress2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 6, 7, 1, 5),
    _GenEquipUnitInfoNtpConfigServerIPaddress2_Type()
)
genEquipUnitInfoNtpConfigServerIPaddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoNtpConfigServerIPaddress2.setStatus("mandatory")


class _GenEquipUnitDaylightSavingTimeStartMonth_Type(Integer32):
    """Custom type genEquipUnitDaylightSavingTimeStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_GenEquipUnitDaylightSavingTimeStartMonth_Type.__name__ = "Integer32"
_GenEquipUnitDaylightSavingTimeStartMonth_Object = MibScalar
genEquipUnitDaylightSavingTimeStartMonth = _GenEquipUnitDaylightSavingTimeStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 7),
    _GenEquipUnitDaylightSavingTimeStartMonth_Type()
)
genEquipUnitDaylightSavingTimeStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitDaylightSavingTimeStartMonth.setStatus("mandatory")


class _GenEquipUnitDaylightSavingTimeStartDay_Type(Integer32):
    """Custom type genEquipUnitDaylightSavingTimeStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_GenEquipUnitDaylightSavingTimeStartDay_Type.__name__ = "Integer32"
_GenEquipUnitDaylightSavingTimeStartDay_Object = MibScalar
genEquipUnitDaylightSavingTimeStartDay = _GenEquipUnitDaylightSavingTimeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 8),
    _GenEquipUnitDaylightSavingTimeStartDay_Type()
)
genEquipUnitDaylightSavingTimeStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitDaylightSavingTimeStartDay.setStatus("mandatory")


class _GenEquipUnitDaylightSavingTimeEndMonth_Type(Integer32):
    """Custom type genEquipUnitDaylightSavingTimeEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_GenEquipUnitDaylightSavingTimeEndMonth_Type.__name__ = "Integer32"
_GenEquipUnitDaylightSavingTimeEndMonth_Object = MibScalar
genEquipUnitDaylightSavingTimeEndMonth = _GenEquipUnitDaylightSavingTimeEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 9),
    _GenEquipUnitDaylightSavingTimeEndMonth_Type()
)
genEquipUnitDaylightSavingTimeEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitDaylightSavingTimeEndMonth.setStatus("mandatory")


class _GenEquipUnitDaylightSavingTimeEndDay_Type(Integer32):
    """Custom type genEquipUnitDaylightSavingTimeEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_GenEquipUnitDaylightSavingTimeEndDay_Type.__name__ = "Integer32"
_GenEquipUnitDaylightSavingTimeEndDay_Object = MibScalar
genEquipUnitDaylightSavingTimeEndDay = _GenEquipUnitDaylightSavingTimeEndDay_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 10),
    _GenEquipUnitDaylightSavingTimeEndDay_Type()
)
genEquipUnitDaylightSavingTimeEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitDaylightSavingTimeEndDay.setStatus("mandatory")


class _GenEquipUnitDaylightSavingTimeOffset_Type(Integer32):
    """Custom type genEquipUnitDaylightSavingTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GenEquipUnitDaylightSavingTimeOffset_Type.__name__ = "Integer32"
_GenEquipUnitDaylightSavingTimeOffset_Object = MibScalar
genEquipUnitDaylightSavingTimeOffset = _GenEquipUnitDaylightSavingTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 11),
    _GenEquipUnitDaylightSavingTimeOffset_Type()
)
genEquipUnitDaylightSavingTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitDaylightSavingTimeOffset.setStatus("mandatory")
_GenEquipUnitInfoTimeServicesTable_Object = MibTable
genEquipUnitInfoTimeServicesTable = _GenEquipUnitInfoTimeServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12)
)
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesTable.setStatus("mandatory")
_GenEquipUnitInfoTimeServicesEntry_Object = MibTableRow
genEquipUnitInfoTimeServicesEntry = _GenEquipUnitInfoTimeServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1)
)
genEquipUnitInfoTimeServicesEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitInfoTimeServicesIndex"),
)
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesEntry.setStatus("mandatory")
_GenEquipUnitInfoTimeServicesIndex_Type = Integer32
_GenEquipUnitInfoTimeServicesIndex_Object = MibTableColumn
genEquipUnitInfoTimeServicesIndex = _GenEquipUnitInfoTimeServicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 1),
    _GenEquipUnitInfoTimeServicesIndex_Type()
)
genEquipUnitInfoTimeServicesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesIndex.setStatus("mandatory")


class _GenEquipUnitInfoTimeServicesUtcHours_Type(Integer32):
    """Custom type genEquipUnitInfoTimeServicesUtcHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_GenEquipUnitInfoTimeServicesUtcHours_Type.__name__ = "Integer32"
_GenEquipUnitInfoTimeServicesUtcHours_Object = MibTableColumn
genEquipUnitInfoTimeServicesUtcHours = _GenEquipUnitInfoTimeServicesUtcHours_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 2),
    _GenEquipUnitInfoTimeServicesUtcHours_Type()
)
genEquipUnitInfoTimeServicesUtcHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesUtcHours.setStatus("mandatory")


class _GenEquipUnitInfoTimeServicesUtcMinutes_Type(Integer32):
    """Custom type genEquipUnitInfoTimeServicesUtcMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_GenEquipUnitInfoTimeServicesUtcMinutes_Type.__name__ = "Integer32"
_GenEquipUnitInfoTimeServicesUtcMinutes_Object = MibTableColumn
genEquipUnitInfoTimeServicesUtcMinutes = _GenEquipUnitInfoTimeServicesUtcMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 3),
    _GenEquipUnitInfoTimeServicesUtcMinutes_Type()
)
genEquipUnitInfoTimeServicesUtcMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesUtcMinutes.setStatus("mandatory")


class _GenEquipUnitInfoTimeServicesDstStartMonth_Type(Integer32):
    """Custom type genEquipUnitInfoTimeServicesDstStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_GenEquipUnitInfoTimeServicesDstStartMonth_Type.__name__ = "Integer32"
_GenEquipUnitInfoTimeServicesDstStartMonth_Object = MibTableColumn
genEquipUnitInfoTimeServicesDstStartMonth = _GenEquipUnitInfoTimeServicesDstStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 4),
    _GenEquipUnitInfoTimeServicesDstStartMonth_Type()
)
genEquipUnitInfoTimeServicesDstStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesDstStartMonth.setStatus("mandatory")


class _GenEquipUnitInfoTimeServicesDstStartDay_Type(Integer32):
    """Custom type genEquipUnitInfoTimeServicesDstStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_GenEquipUnitInfoTimeServicesDstStartDay_Type.__name__ = "Integer32"
_GenEquipUnitInfoTimeServicesDstStartDay_Object = MibTableColumn
genEquipUnitInfoTimeServicesDstStartDay = _GenEquipUnitInfoTimeServicesDstStartDay_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 5),
    _GenEquipUnitInfoTimeServicesDstStartDay_Type()
)
genEquipUnitInfoTimeServicesDstStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesDstStartDay.setStatus("mandatory")


class _GenEquipUnitInfoTimeServicesDstEndMonth_Type(Integer32):
    """Custom type genEquipUnitInfoTimeServicesDstEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_GenEquipUnitInfoTimeServicesDstEndMonth_Type.__name__ = "Integer32"
_GenEquipUnitInfoTimeServicesDstEndMonth_Object = MibTableColumn
genEquipUnitInfoTimeServicesDstEndMonth = _GenEquipUnitInfoTimeServicesDstEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 6),
    _GenEquipUnitInfoTimeServicesDstEndMonth_Type()
)
genEquipUnitInfoTimeServicesDstEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesDstEndMonth.setStatus("mandatory")


class _GenEquipUnitInfoTimeServicesDstEndDay_Type(Integer32):
    """Custom type genEquipUnitInfoTimeServicesDstEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_GenEquipUnitInfoTimeServicesDstEndDay_Type.__name__ = "Integer32"
_GenEquipUnitInfoTimeServicesDstEndDay_Object = MibTableColumn
genEquipUnitInfoTimeServicesDstEndDay = _GenEquipUnitInfoTimeServicesDstEndDay_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 7),
    _GenEquipUnitInfoTimeServicesDstEndDay_Type()
)
genEquipUnitInfoTimeServicesDstEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesDstEndDay.setStatus("mandatory")


class _GenEquipUnitInfoTimeServicesDstOffset_Type(Integer32):
    """Custom type genEquipUnitInfoTimeServicesDstOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GenEquipUnitInfoTimeServicesDstOffset_Type.__name__ = "Integer32"
_GenEquipUnitInfoTimeServicesDstOffset_Object = MibTableColumn
genEquipUnitInfoTimeServicesDstOffset = _GenEquipUnitInfoTimeServicesDstOffset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 8),
    _GenEquipUnitInfoTimeServicesDstOffset_Type()
)
genEquipUnitInfoTimeServicesDstOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesDstOffset.setStatus("mandatory")
_GenEquipUnitInfoTimeServicesUtcDateAndTime_Type = Integer32
_GenEquipUnitInfoTimeServicesUtcDateAndTime_Object = MibTableColumn
genEquipUnitInfoTimeServicesUtcDateAndTime = _GenEquipUnitInfoTimeServicesUtcDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 9),
    _GenEquipUnitInfoTimeServicesUtcDateAndTime_Type()
)
genEquipUnitInfoTimeServicesUtcDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesUtcDateAndTime.setStatus("mandatory")
_GenEquipUnitInfoTimeServicesUtcCurrentDateAndTime_Type = Integer32
_GenEquipUnitInfoTimeServicesUtcCurrentDateAndTime_Object = MibTableColumn
genEquipUnitInfoTimeServicesUtcCurrentDateAndTime = _GenEquipUnitInfoTimeServicesUtcCurrentDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 11, 12, 1, 10),
    _GenEquipUnitInfoTimeServicesUtcCurrentDateAndTime_Type()
)
genEquipUnitInfoTimeServicesUtcCurrentDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitInfoTimeServicesUtcCurrentDateAndTime.setStatus("mandatory")
_GenEquipUnitIduPowerSupply1AlarmAdmin_Type = EnableDisable
_GenEquipUnitIduPowerSupply1AlarmAdmin_Object = MibScalar
genEquipUnitIduPowerSupply1AlarmAdmin = _GenEquipUnitIduPowerSupply1AlarmAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 12),
    _GenEquipUnitIduPowerSupply1AlarmAdmin_Type()
)
genEquipUnitIduPowerSupply1AlarmAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitIduPowerSupply1AlarmAdmin.setStatus("mandatory")
_GenEquipUnitIduPowerSupply2AlarmAdmin_Type = EnableDisable
_GenEquipUnitIduPowerSupply2AlarmAdmin_Object = MibScalar
genEquipUnitIduPowerSupply2AlarmAdmin = _GenEquipUnitIduPowerSupply2AlarmAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 13),
    _GenEquipUnitIduPowerSupply2AlarmAdmin_Type()
)
genEquipUnitIduPowerSupply2AlarmAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitIduPowerSupply2AlarmAdmin.setStatus("mandatory")
_GenEquipUnitInfoNG_ObjectIdentity = ObjectIdentity
genEquipUnitInfoNG = _GenEquipUnitInfoNG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14)
)
_GenEquipUnitName_Type = DisplayString
_GenEquipUnitName_Object = MibScalar
genEquipUnitName = _GenEquipUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14, 1),
    _GenEquipUnitName_Type()
)
genEquipUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitName.setStatus("mandatory")
_GenEquipUnitDescription_Type = DisplayString
_GenEquipUnitDescription_Object = MibScalar
genEquipUnitDescription = _GenEquipUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14, 2),
    _GenEquipUnitDescription_Type()
)
genEquipUnitDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitDescription.setStatus("mandatory")
_GenEquipUnitContactPerson_Type = DisplayString
_GenEquipUnitContactPerson_Object = MibScalar
genEquipUnitContactPerson = _GenEquipUnitContactPerson_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14, 3),
    _GenEquipUnitContactPerson_Type()
)
genEquipUnitContactPerson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitContactPerson.setStatus("mandatory")
_GenEquipUnitLocation_Type = DisplayString
_GenEquipUnitLocation_Object = MibScalar
genEquipUnitLocation = _GenEquipUnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14, 4),
    _GenEquipUnitLocation_Type()
)
genEquipUnitLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitLocation.setStatus("mandatory")
_GenEquipUnitLatitude_Type = DisplayString
_GenEquipUnitLatitude_Object = MibScalar
genEquipUnitLatitude = _GenEquipUnitLatitude_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14, 5),
    _GenEquipUnitLatitude_Type()
)
genEquipUnitLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitLatitude.setStatus("mandatory")
_GenEquipUnitLongitude_Type = DisplayString
_GenEquipUnitLongitude_Object = MibScalar
genEquipUnitLongitude = _GenEquipUnitLongitude_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14, 6),
    _GenEquipUnitLongitude_Type()
)
genEquipUnitLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitLongitude.setStatus("mandatory")


class _GenEquipUnitIpAddressType_Type(Integer32):
    """Custom type genEquipUnitIpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )


_GenEquipUnitIpAddressType_Type.__name__ = "Integer32"
_GenEquipUnitIpAddressType_Object = MibScalar
genEquipUnitIpAddressType = _GenEquipUnitIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14, 7),
    _GenEquipUnitIpAddressType_Type()
)
genEquipUnitIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitIpAddressType.setStatus("mandatory")


class _GenEquipUnitInfoNGTdmInterfaceStandard_Type(Integer32):
    """Custom type genEquipUnitInfoNGTdmInterfaceStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("ets1", 0))
    )


_GenEquipUnitInfoNGTdmInterfaceStandard_Type.__name__ = "Integer32"
_GenEquipUnitInfoNGTdmInterfaceStandard_Object = MibScalar
genEquipUnitInfoNGTdmInterfaceStandard = _GenEquipUnitInfoNGTdmInterfaceStandard_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 1, 14, 8),
    _GenEquipUnitInfoNGTdmInterfaceStandard_Type()
)
genEquipUnitInfoNGTdmInterfaceStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitInfoNGTdmInterfaceStandard.setStatus("mandatory")
_GenEquipUnitInventory_ObjectIdentity = ObjectIdentity
genEquipUnitInventory = _GenEquipUnitInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2)
)
_GenEquipUnitIDUSerialNumber_Type = DisplayString
_GenEquipUnitIDUSerialNumber_Object = MibScalar
genEquipUnitIDUSerialNumber = _GenEquipUnitIDUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 1),
    _GenEquipUnitIDUSerialNumber_Type()
)
genEquipUnitIDUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitIDUSerialNumber.setStatus("mandatory")
_GenEquipUnitIDUPartNumber_Type = DisplayString
_GenEquipUnitIDUPartNumber_Object = MibScalar
genEquipUnitIDUPartNumber = _GenEquipUnitIDUPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 2),
    _GenEquipUnitIDUPartNumber_Type()
)
genEquipUnitIDUPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitIDUPartNumber.setStatus("mandatory")
_GenEquipUnitInventoryNG_ObjectIdentity = ObjectIdentity
genEquipUnitInventoryNG = _GenEquipUnitInventoryNG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10)
)
_GenEquipInventoryTable_Object = MibTable
genEquipInventoryTable = _GenEquipInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    genEquipInventoryTable.setStatus("mandatory")
_GenEquipInventoryEntry_Object = MibTableRow
genEquipInventoryEntry = _GenEquipInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1, 1)
)
genEquipInventoryEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipInventorySlotIndex"),
)
if mibBuilder.loadTexts:
    genEquipInventoryEntry.setStatus("mandatory")
_GenEquipInventorySlotIndex_Type = Integer32
_GenEquipInventorySlotIndex_Object = MibTableColumn
genEquipInventorySlotIndex = _GenEquipInventorySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1, 1, 1),
    _GenEquipInventorySlotIndex_Type()
)
genEquipInventorySlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipInventorySlotIndex.setStatus("mandatory")
_GenEquipInventoryCardName_Type = DisplayString
_GenEquipInventoryCardName_Object = MibTableColumn
genEquipInventoryCardName = _GenEquipInventoryCardName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1, 1, 2),
    _GenEquipInventoryCardName_Type()
)
genEquipInventoryCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipInventoryCardName.setStatus("mandatory")
_GenEquipInventoryCardType_Type = InventoryCardType
_GenEquipInventoryCardType_Object = MibTableColumn
genEquipInventoryCardType = _GenEquipInventoryCardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1, 1, 3),
    _GenEquipInventoryCardType_Type()
)
genEquipInventoryCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipInventoryCardType.setStatus("mandatory")
_GenEquipInventoryCardSubType_Type = Integer32
_GenEquipInventoryCardSubType_Object = MibTableColumn
genEquipInventoryCardSubType = _GenEquipInventoryCardSubType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1, 1, 4),
    _GenEquipInventoryCardSubType_Type()
)
genEquipInventoryCardSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipInventoryCardSubType.setStatus("mandatory")
_GenEquipInventoryPartNumber_Type = DisplayString
_GenEquipInventoryPartNumber_Object = MibTableColumn
genEquipInventoryPartNumber = _GenEquipInventoryPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1, 1, 5),
    _GenEquipInventoryPartNumber_Type()
)
genEquipInventoryPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipInventoryPartNumber.setStatus("mandatory")
_GenEquipInventorySerialNumber_Type = DisplayString
_GenEquipInventorySerialNumber_Object = MibTableColumn
genEquipInventorySerialNumber = _GenEquipInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1, 1, 6),
    _GenEquipInventorySerialNumber_Type()
)
genEquipInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipInventorySerialNumber.setStatus("mandatory")
_GenEquipInventoryNumberWorkingDays_Type = Integer32
_GenEquipInventoryNumberWorkingDays_Object = MibTableColumn
genEquipInventoryNumberWorkingDays = _GenEquipInventoryNumberWorkingDays_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 2, 10, 1, 1, 7),
    _GenEquipInventoryNumberWorkingDays_Type()
)
genEquipInventoryNumberWorkingDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipInventoryNumberWorkingDays.setStatus("mandatory")
_GenEquipUnitLicenseInfo_ObjectIdentity = ObjectIdentity
genEquipUnitLicenseInfo = _GenEquipUnitLicenseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3)
)


class _GenEquipUnitLicenseType_Type(Integer32):
    """Custom type genEquipUnitLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("demo", 2),
          ("normal", 1))
    )


_GenEquipUnitLicenseType_Type.__name__ = "Integer32"
_GenEquipUnitLicenseType_Object = MibScalar
genEquipUnitLicenseType = _GenEquipUnitLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 1),
    _GenEquipUnitLicenseType_Type()
)
genEquipUnitLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseType.setStatus("mandatory")
_GenEquipUnitLicenseCode_Type = DisplayString
_GenEquipUnitLicenseCode_Object = MibScalar
genEquipUnitLicenseCode = _GenEquipUnitLicenseCode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 2),
    _GenEquipUnitLicenseCode_Type()
)
genEquipUnitLicenseCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitLicenseCode.setStatus("mandatory")
_GenEquipUnitACMLicense_Type = AllowedNotAllowed
_GenEquipUnitACMLicense_Object = MibScalar
genEquipUnitACMLicense = _GenEquipUnitACMLicense_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 3),
    _GenEquipUnitACMLicense_Type()
)
genEquipUnitACMLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitACMLicense.setStatus("mandatory")


class _GenEquipUnitSwitchAppLicense_Type(Integer32):
    """Custom type genEquipUnitSwitchAppLicense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("single-pipe", 0),
          ("switch", 8))
    )


_GenEquipUnitSwitchAppLicense_Type.__name__ = "Integer32"
_GenEquipUnitSwitchAppLicense_Object = MibScalar
genEquipUnitSwitchAppLicense = _GenEquipUnitSwitchAppLicense_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 4),
    _GenEquipUnitSwitchAppLicense_Type()
)
genEquipUnitSwitchAppLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitSwitchAppLicense.setStatus("mandatory")


class _GenEquipUnitCapacityLicense_Type(Integer32):
    """Custom type genEquipUnitCapacityLicense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 510),
    )


_GenEquipUnitCapacityLicense_Type.__name__ = "Integer32"
_GenEquipUnitCapacityLicense_Object = MibScalar
genEquipUnitCapacityLicense = _GenEquipUnitCapacityLicense_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 5),
    _GenEquipUnitCapacityLicense_Type()
)
genEquipUnitCapacityLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitCapacityLicense.setStatus("mandatory")
_GenEquipUnitLicenseDemoAdmin_Type = EnableDisable
_GenEquipUnitLicenseDemoAdmin_Object = MibScalar
genEquipUnitLicenseDemoAdmin = _GenEquipUnitLicenseDemoAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 6),
    _GenEquipUnitLicenseDemoAdmin_Type()
)
genEquipUnitLicenseDemoAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitLicenseDemoAdmin.setStatus("mandatory")
_GenEquipUnitLicenseDemoTimer_Type = Integer32
_GenEquipUnitLicenseDemoTimer_Object = MibScalar
genEquipUnitLicenseDemoTimer = _GenEquipUnitLicenseDemoTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 7),
    _GenEquipUnitLicenseDemoTimer_Type()
)
genEquipUnitLicenseDemoTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseDemoTimer.setStatus("mandatory")
_GenEquipUnitLicenseSyncU_Type = AllowedNotAllowed
_GenEquipUnitLicenseSyncU_Object = MibScalar
genEquipUnitLicenseSyncU = _GenEquipUnitLicenseSyncU_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 8),
    _GenEquipUnitLicenseSyncU_Type()
)
genEquipUnitLicenseSyncU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseSyncU.setStatus("mandatory")
_GenEquipUnitLicenseNetworkResiliency_Type = AllowedNotAllowed
_GenEquipUnitLicenseNetworkResiliency_Object = MibScalar
genEquipUnitLicenseNetworkResiliency = _GenEquipUnitLicenseNetworkResiliency_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 9),
    _GenEquipUnitLicenseNetworkResiliency_Type()
)
genEquipUnitLicenseNetworkResiliency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseNetworkResiliency.setStatus("mandatory")
_GenEquipUnitLicenseTDMCapacity_Type = AllowedNotAllowed
_GenEquipUnitLicenseTDMCapacity_Object = MibScalar
genEquipUnitLicenseTDMCapacity = _GenEquipUnitLicenseTDMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 10),
    _GenEquipUnitLicenseTDMCapacity_Type()
)
genEquipUnitLicenseTDMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseTDMCapacity.setStatus("mandatory")
_GenEquipUnitLicenseTDMCapacityValue_Type = Integer32
_GenEquipUnitLicenseTDMCapacityValue_Object = MibScalar
genEquipUnitLicenseTDMCapacityValue = _GenEquipUnitLicenseTDMCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 11),
    _GenEquipUnitLicenseTDMCapacityValue_Type()
)
genEquipUnitLicenseTDMCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseTDMCapacityValue.setStatus("mandatory")
_GenEquipUnitLicensePerUsage_Type = AllowedNotAllowed
_GenEquipUnitLicensePerUsage_Object = MibScalar
genEquipUnitLicensePerUsage = _GenEquipUnitLicensePerUsage_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 12),
    _GenEquipUnitLicensePerUsage_Type()
)
genEquipUnitLicensePerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicensePerUsage.setStatus("mandatory")
_GenEquipUnitLicenseAsymScripts_Type = AllowedNotAllowed
_GenEquipUnitLicenseAsymScripts_Object = MibScalar
genEquipUnitLicenseAsymScripts = _GenEquipUnitLicenseAsymScripts_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 13),
    _GenEquipUnitLicenseAsymScripts_Type()
)
genEquipUnitLicenseAsymScripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseAsymScripts.setStatus("mandatory")
_GenEquipUnitLicenseDateCode_Type = Integer32
_GenEquipUnitLicenseDateCode_Object = MibScalar
genEquipUnitLicenseDateCode = _GenEquipUnitLicenseDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 14),
    _GenEquipUnitLicenseDateCode_Type()
)
genEquipUnitLicenseDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseDateCode.setStatus("mandatory")
_GenEquipUnitLicenseValidationNumber_Type = Integer32
_GenEquipUnitLicenseValidationNumber_Object = MibScalar
genEquipUnitLicenseValidationNumber = _GenEquipUnitLicenseValidationNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 15),
    _GenEquipUnitLicenseValidationNumber_Type()
)
genEquipUnitLicenseValidationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseValidationNumber.setStatus("mandatory")
_GenEquipUnitLicenseFeatureTable_Object = MibTable
genEquipUnitLicenseFeatureTable = _GenEquipUnitLicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 16)
)
if mibBuilder.loadTexts:
    genEquipUnitLicenseFeatureTable.setStatus("mandatory")
_GenEquipUnitLicenseFeatureEntry_Object = MibTableRow
genEquipUnitLicenseFeatureEntry = _GenEquipUnitLicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 16, 1)
)
genEquipUnitLicenseFeatureEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitLicenseFeatureId"),
)
if mibBuilder.loadTexts:
    genEquipUnitLicenseFeatureEntry.setStatus("mandatory")
_GenEquipUnitLicenseFeatureId_Type = Integer32
_GenEquipUnitLicenseFeatureId_Object = MibTableColumn
genEquipUnitLicenseFeatureId = _GenEquipUnitLicenseFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 16, 1, 1),
    _GenEquipUnitLicenseFeatureId_Type()
)
genEquipUnitLicenseFeatureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseFeatureId.setStatus("mandatory")
_GenEquipUnitLicenseFeatureName_Type = DisplayString
_GenEquipUnitLicenseFeatureName_Object = MibTableColumn
genEquipUnitLicenseFeatureName = _GenEquipUnitLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 16, 1, 2),
    _GenEquipUnitLicenseFeatureName_Type()
)
genEquipUnitLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseFeatureName.setStatus("mandatory")
_GenEquipUnitLicenseFeatureDescription_Type = DisplayString
_GenEquipUnitLicenseFeatureDescription_Object = MibTableColumn
genEquipUnitLicenseFeatureDescription = _GenEquipUnitLicenseFeatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 16, 1, 3),
    _GenEquipUnitLicenseFeatureDescription_Type()
)
genEquipUnitLicenseFeatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseFeatureDescription.setStatus("mandatory")
_GenEquipUnitLicenseFeatureIsUsed_Type = LicenseGeneric
_GenEquipUnitLicenseFeatureIsUsed_Object = MibTableColumn
genEquipUnitLicenseFeatureIsUsed = _GenEquipUnitLicenseFeatureIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 16, 1, 4),
    _GenEquipUnitLicenseFeatureIsUsed_Type()
)
genEquipUnitLicenseFeatureIsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseFeatureIsUsed.setStatus("mandatory")
_GenEquipUnitLicenseFeatureIsAllowed_Type = LicenseGeneric
_GenEquipUnitLicenseFeatureIsAllowed_Object = MibTableColumn
genEquipUnitLicenseFeatureIsAllowed = _GenEquipUnitLicenseFeatureIsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 16, 1, 5),
    _GenEquipUnitLicenseFeatureIsAllowed_Type()
)
genEquipUnitLicenseFeatureIsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseFeatureIsAllowed.setStatus("mandatory")


class _GenEquipUnitLicenseViolationStatus_Type(Integer32):
    """Custom type genEquipUnitLicenseViolationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("violated", 1))
    )


_GenEquipUnitLicenseViolationStatus_Type.__name__ = "Integer32"
_GenEquipUnitLicenseViolationStatus_Object = MibTableColumn
genEquipUnitLicenseViolationStatus = _GenEquipUnitLicenseViolationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 16, 1, 6),
    _GenEquipUnitLicenseViolationStatus_Type()
)
genEquipUnitLicenseViolationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseViolationStatus.setStatus("mandatory")
_GenEquipUnitLicenseCutThrough_Type = AllowedNotAllowed
_GenEquipUnitLicenseCutThrough_Object = MibScalar
genEquipUnitLicenseCutThrough = _GenEquipUnitLicenseCutThrough_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 20),
    _GenEquipUnitLicenseCutThrough_Type()
)
genEquipUnitLicenseCutThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseCutThrough.setStatus("mandatory")


class _GenEquipUnitLicenseTdmInterfaceStandard_Type(Integer32):
    """Custom type genEquipUnitLicenseTdmInterfaceStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("ets1", 0))
    )


_GenEquipUnitLicenseTdmInterfaceStandard_Type.__name__ = "Integer32"
_GenEquipUnitLicenseTdmInterfaceStandard_Object = MibScalar
genEquipUnitLicenseTdmInterfaceStandard = _GenEquipUnitLicenseTdmInterfaceStandard_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 3, 21),
    _GenEquipUnitLicenseTdmInterfaceStandard_Type()
)
genEquipUnitLicenseTdmInterfaceStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitLicenseTdmInterfaceStandard.setStatus("mandatory")
_GenEquipUnitExternalAlarms_ObjectIdentity = ObjectIdentity
genEquipUnitExternalAlarms = _GenEquipUnitExternalAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4)
)
_GenEquipUnitAlarmInput_ObjectIdentity = ObjectIdentity
genEquipUnitAlarmInput = _GenEquipUnitAlarmInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 1)
)
_GenEquipUnitAlarmInputTable_Object = MibTable
genEquipUnitAlarmInputTable = _GenEquipUnitAlarmInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    genEquipUnitAlarmInputTable.setStatus("mandatory")
_GenEquipUnitAlarmInputEntry_Object = MibTableRow
genEquipUnitAlarmInputEntry = _GenEquipUnitAlarmInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 1, 1, 1)
)
genEquipUnitAlarmInputEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitAlarmInputCounter"),
)
if mibBuilder.loadTexts:
    genEquipUnitAlarmInputEntry.setStatus("mandatory")
_GenEquipUnitAlarmInputCounter_Type = Integer32
_GenEquipUnitAlarmInputCounter_Object = MibTableColumn
genEquipUnitAlarmInputCounter = _GenEquipUnitAlarmInputCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 1, 1, 1, 1),
    _GenEquipUnitAlarmInputCounter_Type()
)
genEquipUnitAlarmInputCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitAlarmInputCounter.setStatus("mandatory")
_GenEquipUnitAlarmInputAdmin_Type = EnableDisableSMI2
_GenEquipUnitAlarmInputAdmin_Object = MibTableColumn
genEquipUnitAlarmInputAdmin = _GenEquipUnitAlarmInputAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 1, 1, 1, 2),
    _GenEquipUnitAlarmInputAdmin_Type()
)
genEquipUnitAlarmInputAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitAlarmInputAdmin.setStatus("mandatory")


class _GenEquipUnitAlarmInputText_Type(DisplayString):
    """Custom type genEquipUnitAlarmInputText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_GenEquipUnitAlarmInputText_Type.__name__ = "DisplayString"
_GenEquipUnitAlarmInputText_Object = MibTableColumn
genEquipUnitAlarmInputText = _GenEquipUnitAlarmInputText_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 1, 1, 1, 3),
    _GenEquipUnitAlarmInputText_Type()
)
genEquipUnitAlarmInputText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitAlarmInputText.setStatus("mandatory")
_GenEquipUnitAlarmInputSeverity_Type = InputSeverity
_GenEquipUnitAlarmInputSeverity_Object = MibTableColumn
genEquipUnitAlarmInputSeverity = _GenEquipUnitAlarmInputSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 1, 1, 1, 4),
    _GenEquipUnitAlarmInputSeverity_Type()
)
genEquipUnitAlarmInputSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitAlarmInputSeverity.setStatus("mandatory")
_GenEquipUnitAlarmInputState_Type = OffOn
_GenEquipUnitAlarmInputState_Object = MibTableColumn
genEquipUnitAlarmInputState = _GenEquipUnitAlarmInputState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 1, 1, 1, 5),
    _GenEquipUnitAlarmInputState_Type()
)
genEquipUnitAlarmInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitAlarmInputState.setStatus("mandatory")
_GenEquipUnitAlarmOutput_ObjectIdentity = ObjectIdentity
genEquipUnitAlarmOutput = _GenEquipUnitAlarmOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 2)
)
_GenEquipUnitAlarmOutputTable_Object = MibTable
genEquipUnitAlarmOutputTable = _GenEquipUnitAlarmOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    genEquipUnitAlarmOutputTable.setStatus("mandatory")
_GenEquipUnitAlarmOutputEntry_Object = MibTableRow
genEquipUnitAlarmOutputEntry = _GenEquipUnitAlarmOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 2, 1, 1)
)
genEquipUnitAlarmOutputEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitAlarmOutputCounter"),
)
if mibBuilder.loadTexts:
    genEquipUnitAlarmOutputEntry.setStatus("mandatory")
_GenEquipUnitAlarmOutputCounter_Type = Integer32
_GenEquipUnitAlarmOutputCounter_Object = MibTableColumn
genEquipUnitAlarmOutputCounter = _GenEquipUnitAlarmOutputCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 2, 1, 1, 1),
    _GenEquipUnitAlarmOutputCounter_Type()
)
genEquipUnitAlarmOutputCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitAlarmOutputCounter.setStatus("mandatory")


class _GenEquipUnitAlarmOutputAdmin_Type(Integer32):
    """Custom type genEquipUnitAlarmOutputAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("test", 2))
    )


_GenEquipUnitAlarmOutputAdmin_Type.__name__ = "Integer32"
_GenEquipUnitAlarmOutputAdmin_Object = MibTableColumn
genEquipUnitAlarmOutputAdmin = _GenEquipUnitAlarmOutputAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 2, 1, 1, 2),
    _GenEquipUnitAlarmOutputAdmin_Type()
)
genEquipUnitAlarmOutputAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitAlarmOutputAdmin.setStatus("mandatory")


class _GenEquipUnitAlarmOutputStatus_Type(Integer32):
    """Custom type genEquipUnitAlarmOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("on-test", 2))
    )


_GenEquipUnitAlarmOutputStatus_Type.__name__ = "Integer32"
_GenEquipUnitAlarmOutputStatus_Object = MibTableColumn
genEquipUnitAlarmOutputStatus = _GenEquipUnitAlarmOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 2, 1, 1, 3),
    _GenEquipUnitAlarmOutputStatus_Type()
)
genEquipUnitAlarmOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitAlarmOutputStatus.setStatus("mandatory")


class _GenEquipUnitAlarmOutputGroup_Type(Integer32):
    """Custom type genEquipUnitAlarmOutputGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all-groups", 6),
          ("communication", 1),
          ("environmental", 5),
          ("equipment", 4),
          ("processing", 3),
          ("quality-of-service", 2))
    )


_GenEquipUnitAlarmOutputGroup_Type.__name__ = "Integer32"
_GenEquipUnitAlarmOutputGroup_Object = MibTableColumn
genEquipUnitAlarmOutputGroup = _GenEquipUnitAlarmOutputGroup_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 4, 2, 1, 1, 4),
    _GenEquipUnitAlarmOutputGroup_Type()
)
genEquipUnitAlarmOutputGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitAlarmOutputGroup.setStatus("mandatory")
_GenEquipUnitShelf_ObjectIdentity = ObjectIdentity
genEquipUnitShelf = _GenEquipUnitShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5)
)


class _GenEquipUnitShelfInstallation_Type(Integer32):
    """Custom type genEquipUnitShelfInstallation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chassisModule", 1),
          ("standalone", 0))
    )


_GenEquipUnitShelfInstallation_Type.__name__ = "Integer32"
_GenEquipUnitShelfInstallation_Object = MibScalar
genEquipUnitShelfInstallation = _GenEquipUnitShelfInstallation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 1),
    _GenEquipUnitShelfInstallation_Type()
)
genEquipUnitShelfInstallation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfInstallation.setStatus("mandatory")


class _GenEquipUnitShelfModuleRole_Type(Integer32):
    """Custom type genEquipUnitShelfModuleRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("extention", 1),
          ("main", 0))
    )


_GenEquipUnitShelfModuleRole_Type.__name__ = "Integer32"
_GenEquipUnitShelfModuleRole_Object = MibScalar
genEquipUnitShelfModuleRole = _GenEquipUnitShelfModuleRole_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 2),
    _GenEquipUnitShelfModuleRole_Type()
)
genEquipUnitShelfModuleRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfModuleRole.setStatus("mandatory")


class _GenEquipUnitShelfSlotLabel_Type(DisplayString):
    """Custom type genEquipUnitShelfSlotLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GenEquipUnitShelfSlotLabel_Type.__name__ = "DisplayString"
_GenEquipUnitShelfSlotLabel_Object = MibScalar
genEquipUnitShelfSlotLabel = _GenEquipUnitShelfSlotLabel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 3),
    _GenEquipUnitShelfSlotLabel_Type()
)
genEquipUnitShelfSlotLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotLabel.setStatus("mandatory")
_GenEquipUnitShelfArchivesOperationStatus_Type = ProgressStatus
_GenEquipUnitShelfArchivesOperationStatus_Object = MibScalar
genEquipUnitShelfArchivesOperationStatus = _GenEquipUnitShelfArchivesOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 4),
    _GenEquipUnitShelfArchivesOperationStatus_Type()
)
genEquipUnitShelfArchivesOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfArchivesOperationStatus.setStatus("mandatory")
_GenEquipUnitShelfManagmentTable_Object = MibTable
genEquipUnitShelfManagmentTable = _GenEquipUnitShelfManagmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5)
)
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentTable.setStatus("mandatory")
_GenEquipUnitShelfManagmentEntry_Object = MibTableRow
genEquipUnitShelfManagmentEntry = _GenEquipUnitShelfManagmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5, 1)
)
genEquipUnitShelfManagmentEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitShelfManagmentSlot"),
)
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentEntry.setStatus("mandatory")
_GenEquipUnitShelfManagmentSlot_Type = SlotId
_GenEquipUnitShelfManagmentSlot_Object = MibTableColumn
genEquipUnitShelfManagmentSlot = _GenEquipUnitShelfManagmentSlot_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5, 1, 1),
    _GenEquipUnitShelfManagmentSlot_Type()
)
genEquipUnitShelfManagmentSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSlot.setStatus("mandatory")


class _GenEquipUnitShelfManagmentSlotPopulation_Type(Integer32):
    """Custom type genEquipUnitShelfManagmentSlotPopulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 0),
          ("present", 1))
    )


_GenEquipUnitShelfManagmentSlotPopulation_Type.__name__ = "Integer32"
_GenEquipUnitShelfManagmentSlotPopulation_Object = MibTableColumn
genEquipUnitShelfManagmentSlotPopulation = _GenEquipUnitShelfManagmentSlotPopulation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5, 1, 2),
    _GenEquipUnitShelfManagmentSlotPopulation_Type()
)
genEquipUnitShelfManagmentSlotPopulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSlotPopulation.setStatus("mandatory")


class _GenEquipUnitShelfManagmentCommunicationStatus_Type(Integer32):
    """Custom type genEquipUnitShelfManagmentCommunicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("communicationDown", 0),
          ("communicationUp", 1))
    )


_GenEquipUnitShelfManagmentCommunicationStatus_Type.__name__ = "Integer32"
_GenEquipUnitShelfManagmentCommunicationStatus_Object = MibTableColumn
genEquipUnitShelfManagmentCommunicationStatus = _GenEquipUnitShelfManagmentCommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5, 1, 3),
    _GenEquipUnitShelfManagmentCommunicationStatus_Type()
)
genEquipUnitShelfManagmentCommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentCommunicationStatus.setStatus("mandatory")
_GenEquipUnitShelfManagmentSlotMostSevereAlarm_Type = Severity
_GenEquipUnitShelfManagmentSlotMostSevereAlarm_Object = MibTableColumn
genEquipUnitShelfManagmentSlotMostSevereAlarm = _GenEquipUnitShelfManagmentSlotMostSevereAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5, 1, 4),
    _GenEquipUnitShelfManagmentSlotMostSevereAlarm_Type()
)
genEquipUnitShelfManagmentSlotMostSevereAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSlotMostSevereAlarm.setStatus("mandatory")
_GenEquipUnitShelfManagmentMngSwCommand_Type = SwCommand
_GenEquipUnitShelfManagmentMngSwCommand_Object = MibTableColumn
genEquipUnitShelfManagmentMngSwCommand = _GenEquipUnitShelfManagmentMngSwCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5, 1, 5),
    _GenEquipUnitShelfManagmentMngSwCommand_Type()
)
genEquipUnitShelfManagmentMngSwCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentMngSwCommand.setStatus("mandatory")
_GenEquipUnitShelfManagmentSlotReset_Type = OffOn
_GenEquipUnitShelfManagmentSlotReset_Object = MibTableColumn
genEquipUnitShelfManagmentSlotReset = _GenEquipUnitShelfManagmentSlotReset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5, 1, 6),
    _GenEquipUnitShelfManagmentSlotReset_Type()
)
genEquipUnitShelfManagmentSlotReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSlotReset.setStatus("mandatory")
_GenEquipUnitShelfManagmentSlotIp_Type = IpAddress
_GenEquipUnitShelfManagmentSlotIp_Object = MibTableColumn
genEquipUnitShelfManagmentSlotIp = _GenEquipUnitShelfManagmentSlotIp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 5, 1, 7),
    _GenEquipUnitShelfManagmentSlotIp_Type()
)
genEquipUnitShelfManagmentSlotIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSlotIp.setStatus("mandatory")
_GenEquipUnitShelfReset_Type = OffOn
_GenEquipUnitShelfReset_Object = MibScalar
genEquipUnitShelfReset = _GenEquipUnitShelfReset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 6),
    _GenEquipUnitShelfReset_Type()
)
genEquipUnitShelfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfReset.setStatus("mandatory")
_GenEquipUnitshelfAllODUAdmin_Type = EnableDisable
_GenEquipUnitshelfAllODUAdmin_Object = MibScalar
genEquipUnitshelfAllODUAdmin = _GenEquipUnitshelfAllODUAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 7),
    _GenEquipUnitshelfAllODUAdmin_Type()
)
genEquipUnitshelfAllODUAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitshelfAllODUAdmin.setStatus("mandatory")
_GenEquipUnitShelfSlotConfigTable_Object = MibTable
genEquipUnitShelfSlotConfigTable = _GenEquipUnitShelfSlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 8)
)
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotConfigTable.setStatus("mandatory")
_GenEquipUnitShelfSlotConfigEntry_Object = MibTableRow
genEquipUnitShelfSlotConfigEntry = _GenEquipUnitShelfSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 8, 1)
)
genEquipUnitShelfSlotConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitShelfSlotConfigSlotID"),
)
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotConfigEntry.setStatus("mandatory")
_GenEquipUnitShelfSlotConfigSlotID_Type = SlotId
_GenEquipUnitShelfSlotConfigSlotID_Object = MibTableColumn
genEquipUnitShelfSlotConfigSlotID = _GenEquipUnitShelfSlotConfigSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 8, 1, 1),
    _GenEquipUnitShelfSlotConfigSlotID_Type()
)
genEquipUnitShelfSlotConfigSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotConfigSlotID.setStatus("mandatory")
_GenEquipUnitShelfSlotConfigExpectedCardType_Type = InventoryCardType
_GenEquipUnitShelfSlotConfigExpectedCardType_Object = MibTableColumn
genEquipUnitShelfSlotConfigExpectedCardType = _GenEquipUnitShelfSlotConfigExpectedCardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 8, 1, 2),
    _GenEquipUnitShelfSlotConfigExpectedCardType_Type()
)
genEquipUnitShelfSlotConfigExpectedCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotConfigExpectedCardType.setStatus("mandatory")
_GenEquipUnitShelfSlotConfigLabel_Type = DisplayString
_GenEquipUnitShelfSlotConfigLabel_Object = MibTableColumn
genEquipUnitShelfSlotConfigLabel = _GenEquipUnitShelfSlotConfigLabel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 8, 1, 3),
    _GenEquipUnitShelfSlotConfigLabel_Type()
)
genEquipUnitShelfSlotConfigLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotConfigLabel.setStatus("mandatory")
_GenEquipUnitShelfSlotConfigAdmin_Type = EnableDisable
_GenEquipUnitShelfSlotConfigAdmin_Object = MibTableColumn
genEquipUnitShelfSlotConfigAdmin = _GenEquipUnitShelfSlotConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 8, 1, 4),
    _GenEquipUnitShelfSlotConfigAdmin_Type()
)
genEquipUnitShelfSlotConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotConfigAdmin.setStatus("mandatory")
_GenEquipUnitShelfSlotConfigSlotReset_Type = OffOn
_GenEquipUnitShelfSlotConfigSlotReset_Object = MibTableColumn
genEquipUnitShelfSlotConfigSlotReset = _GenEquipUnitShelfSlotConfigSlotReset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 8, 1, 5),
    _GenEquipUnitShelfSlotConfigSlotReset_Type()
)
genEquipUnitShelfSlotConfigSlotReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotConfigSlotReset.setStatus("mandatory")
_GenEquipUnitShelfTccConfigTable_Object = MibTable
genEquipUnitShelfTccConfigTable = _GenEquipUnitShelfTccConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 9)
)
if mibBuilder.loadTexts:
    genEquipUnitShelfTccConfigTable.setStatus("mandatory")
_GenEquipUnitShelfTccConfigEntry_Object = MibTableRow
genEquipUnitShelfTccConfigEntry = _GenEquipUnitShelfTccConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 9, 1)
)
genEquipUnitShelfTccConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitShelfTccConfigSlotID"),
)
if mibBuilder.loadTexts:
    genEquipUnitShelfTccConfigEntry.setStatus("mandatory")
_GenEquipUnitShelfTccConfigSlotID_Type = SlotId
_GenEquipUnitShelfTccConfigSlotID_Object = MibTableColumn
genEquipUnitShelfTccConfigSlotID = _GenEquipUnitShelfTccConfigSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 9, 1, 1),
    _GenEquipUnitShelfTccConfigSlotID_Type()
)
genEquipUnitShelfTccConfigSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccConfigSlotID.setStatus("mandatory")
_GenEquipUnitShelfTccConfigExpectedCardType_Type = InventoryCardType
_GenEquipUnitShelfTccConfigExpectedCardType_Object = MibTableColumn
genEquipUnitShelfTccConfigExpectedCardType = _GenEquipUnitShelfTccConfigExpectedCardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 9, 1, 2),
    _GenEquipUnitShelfTccConfigExpectedCardType_Type()
)
genEquipUnitShelfTccConfigExpectedCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccConfigExpectedCardType.setStatus("mandatory")
_GenEquipUnitShelfTccConfigLabel_Type = DisplayString
_GenEquipUnitShelfTccConfigLabel_Object = MibTableColumn
genEquipUnitShelfTccConfigLabel = _GenEquipUnitShelfTccConfigLabel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 9, 1, 3),
    _GenEquipUnitShelfTccConfigLabel_Type()
)
genEquipUnitShelfTccConfigLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccConfigLabel.setStatus("mandatory")
_GenEquipUnitShelfTccConfigAdmin_Type = EnableDisable
_GenEquipUnitShelfTccConfigAdmin_Object = MibTableColumn
genEquipUnitShelfTccConfigAdmin = _GenEquipUnitShelfTccConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 9, 1, 4),
    _GenEquipUnitShelfTccConfigAdmin_Type()
)
genEquipUnitShelfTccConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccConfigAdmin.setStatus("mandatory")
_GenEquipUnitShelfTccConfigReset_Type = OffOn
_GenEquipUnitShelfTccConfigReset_Object = MibTableColumn
genEquipUnitShelfTccConfigReset = _GenEquipUnitShelfTccConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 9, 1, 5),
    _GenEquipUnitShelfTccConfigReset_Type()
)
genEquipUnitShelfTccConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccConfigReset.setStatus("mandatory")
_GenEquipUnitShelfSlotStatusTable_Object = MibTable
genEquipUnitShelfSlotStatusTable = _GenEquipUnitShelfSlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 10)
)
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotStatusTable.setStatus("mandatory")
_GenEquipUnitShelfSlotStatusEntry_Object = MibTableRow
genEquipUnitShelfSlotStatusEntry = _GenEquipUnitShelfSlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 10, 1)
)
genEquipUnitShelfSlotStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitShelfSlotStatusSlotID"),
)
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotStatusEntry.setStatus("mandatory")
_GenEquipUnitShelfSlotStatusSlotID_Type = SlotId
_GenEquipUnitShelfSlotStatusSlotID_Object = MibTableColumn
genEquipUnitShelfSlotStatusSlotID = _GenEquipUnitShelfSlotStatusSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 10, 1, 1),
    _GenEquipUnitShelfSlotStatusSlotID_Type()
)
genEquipUnitShelfSlotStatusSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotStatusSlotID.setStatus("mandatory")
_GenEquipUnitShelfSlotStatusOccupancy_Type = CardOccupancy
_GenEquipUnitShelfSlotStatusOccupancy_Object = MibTableColumn
genEquipUnitShelfSlotStatusOccupancy = _GenEquipUnitShelfSlotStatusOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 10, 1, 2),
    _GenEquipUnitShelfSlotStatusOccupancy_Type()
)
genEquipUnitShelfSlotStatusOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotStatusOccupancy.setStatus("mandatory")
_GenEquipUnitShelfSlotStatusAllowedCardTypes_Type = Counter64
_GenEquipUnitShelfSlotStatusAllowedCardTypes_Object = MibTableColumn
genEquipUnitShelfSlotStatusAllowedCardTypes = _GenEquipUnitShelfSlotStatusAllowedCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 10, 1, 3),
    _GenEquipUnitShelfSlotStatusAllowedCardTypes_Type()
)
genEquipUnitShelfSlotStatusAllowedCardTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotStatusAllowedCardTypes.setStatus("mandatory")
_GenEquipUnitShelfSlotStatusCardType_Type = InventoryCardType
_GenEquipUnitShelfSlotStatusCardType_Object = MibTableColumn
genEquipUnitShelfSlotStatusCardType = _GenEquipUnitShelfSlotStatusCardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 10, 1, 4),
    _GenEquipUnitShelfSlotStatusCardType_Type()
)
genEquipUnitShelfSlotStatusCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotStatusCardType.setStatus("mandatory")
_GenEquipUnitShelfSlotStatusOperationalState_Type = OperState
_GenEquipUnitShelfSlotStatusOperationalState_Object = MibTableColumn
genEquipUnitShelfSlotStatusOperationalState = _GenEquipUnitShelfSlotStatusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 10, 1, 5),
    _GenEquipUnitShelfSlotStatusOperationalState_Type()
)
genEquipUnitShelfSlotStatusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotStatusOperationalState.setStatus("mandatory")
_GenEquipUnitShelfSlotStatusCommunication_Type = DownUp
_GenEquipUnitShelfSlotStatusCommunication_Object = MibTableColumn
genEquipUnitShelfSlotStatusCommunication = _GenEquipUnitShelfSlotStatusCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 10, 1, 6),
    _GenEquipUnitShelfSlotStatusCommunication_Type()
)
genEquipUnitShelfSlotStatusCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfSlotStatusCommunication.setStatus("mandatory")
_GenEquipUnitShelfTccStatusTable_Object = MibTable
genEquipUnitShelfTccStatusTable = _GenEquipUnitShelfTccStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 11)
)
if mibBuilder.loadTexts:
    genEquipUnitShelfTccStatusTable.setStatus("mandatory")
_GenEquipUnitShelfTccStatusEntry_Object = MibTableRow
genEquipUnitShelfTccStatusEntry = _GenEquipUnitShelfTccStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 11, 1)
)
genEquipUnitShelfTccStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitShelfTccStatusSlotID"),
)
if mibBuilder.loadTexts:
    genEquipUnitShelfTccStatusEntry.setStatus("mandatory")
_GenEquipUnitShelfTccStatusSlotID_Type = SlotId
_GenEquipUnitShelfTccStatusSlotID_Object = MibTableColumn
genEquipUnitShelfTccStatusSlotID = _GenEquipUnitShelfTccStatusSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 11, 1, 1),
    _GenEquipUnitShelfTccStatusSlotID_Type()
)
genEquipUnitShelfTccStatusSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccStatusSlotID.setStatus("mandatory")
_GenEquipUnitShelfTccStatusOccupancy_Type = CardOccupancy
_GenEquipUnitShelfTccStatusOccupancy_Object = MibTableColumn
genEquipUnitShelfTccStatusOccupancy = _GenEquipUnitShelfTccStatusOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 11, 1, 2),
    _GenEquipUnitShelfTccStatusOccupancy_Type()
)
genEquipUnitShelfTccStatusOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccStatusOccupancy.setStatus("mandatory")
_GenEquipUnitShelfTccStatusAllowedCardTypes_Type = Counter64
_GenEquipUnitShelfTccStatusAllowedCardTypes_Object = MibTableColumn
genEquipUnitShelfTccStatusAllowedCardTypes = _GenEquipUnitShelfTccStatusAllowedCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 11, 1, 3),
    _GenEquipUnitShelfTccStatusAllowedCardTypes_Type()
)
genEquipUnitShelfTccStatusAllowedCardTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccStatusAllowedCardTypes.setStatus("mandatory")
_GenEquipUnitShelfTccStatusCardType_Type = InventoryCardType
_GenEquipUnitShelfTccStatusCardType_Object = MibTableColumn
genEquipUnitShelfTccStatusCardType = _GenEquipUnitShelfTccStatusCardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 11, 1, 4),
    _GenEquipUnitShelfTccStatusCardType_Type()
)
genEquipUnitShelfTccStatusCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccStatusCardType.setStatus("mandatory")
_GenEquipUnitShelfTccStatusOperationalState_Type = OperState
_GenEquipUnitShelfTccStatusOperationalState_Object = MibTableColumn
genEquipUnitShelfTccStatusOperationalState = _GenEquipUnitShelfTccStatusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 11, 1, 5),
    _GenEquipUnitShelfTccStatusOperationalState_Type()
)
genEquipUnitShelfTccStatusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccStatusOperationalState.setStatus("mandatory")
_GenEquipUnitShelfTccStatusCommunication_Type = DownUp
_GenEquipUnitShelfTccStatusCommunication_Object = MibTableColumn
genEquipUnitShelfTccStatusCommunication = _GenEquipUnitShelfTccStatusCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 11, 1, 6),
    _GenEquipUnitShelfTccStatusCommunication_Type()
)
genEquipUnitShelfTccStatusCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfTccStatusCommunication.setStatus("mandatory")
_GenEquipUnitShelfManagmentSeverityTable_Object = MibTable
genEquipUnitShelfManagmentSeverityTable = _GenEquipUnitShelfManagmentSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 12)
)
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSeverityTable.setStatus("mandatory")
_GenEquipUnitShelfManagmentSeverityEntry_Object = MibTableRow
genEquipUnitShelfManagmentSeverityEntry = _GenEquipUnitShelfManagmentSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 12, 1)
)
genEquipUnitShelfManagmentSeverityEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitShelfManagmentSeveritySlot"),
)
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSeverityEntry.setStatus("mandatory")
_GenEquipUnitShelfManagmentSeveritySlot_Type = Integer32
_GenEquipUnitShelfManagmentSeveritySlot_Object = MibTableColumn
genEquipUnitShelfManagmentSeveritySlot = _GenEquipUnitShelfManagmentSeveritySlot_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 12, 1, 1),
    _GenEquipUnitShelfManagmentSeveritySlot_Type()
)
genEquipUnitShelfManagmentSeveritySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSeveritySlot.setStatus("mandatory")
_GenEquipUnitShelfManagmentSeverityCritical_Type = Integer32
_GenEquipUnitShelfManagmentSeverityCritical_Object = MibTableColumn
genEquipUnitShelfManagmentSeverityCritical = _GenEquipUnitShelfManagmentSeverityCritical_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 12, 1, 2),
    _GenEquipUnitShelfManagmentSeverityCritical_Type()
)
genEquipUnitShelfManagmentSeverityCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSeverityCritical.setStatus("mandatory")
_GenEquipUnitShelfManagmentSeverityMajor_Type = Integer32
_GenEquipUnitShelfManagmentSeverityMajor_Object = MibTableColumn
genEquipUnitShelfManagmentSeverityMajor = _GenEquipUnitShelfManagmentSeverityMajor_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 12, 1, 3),
    _GenEquipUnitShelfManagmentSeverityMajor_Type()
)
genEquipUnitShelfManagmentSeverityMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSeverityMajor.setStatus("mandatory")
_GenEquipUnitShelfManagmentSeverityMinor_Type = Integer32
_GenEquipUnitShelfManagmentSeverityMinor_Object = MibTableColumn
genEquipUnitShelfManagmentSeverityMinor = _GenEquipUnitShelfManagmentSeverityMinor_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 12, 1, 4),
    _GenEquipUnitShelfManagmentSeverityMinor_Type()
)
genEquipUnitShelfManagmentSeverityMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSeverityMinor.setStatus("mandatory")
_GenEquipUnitShelfManagmentSeverityWarning_Type = Integer32
_GenEquipUnitShelfManagmentSeverityWarning_Object = MibTableColumn
genEquipUnitShelfManagmentSeverityWarning = _GenEquipUnitShelfManagmentSeverityWarning_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 12, 1, 5),
    _GenEquipUnitShelfManagmentSeverityWarning_Type()
)
genEquipUnitShelfManagmentSeverityWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSeverityWarning.setStatus("mandatory")
_GenEquipUnitShelfManagmentSeverityIndeterminate_Type = Integer32
_GenEquipUnitShelfManagmentSeverityIndeterminate_Object = MibTableColumn
genEquipUnitShelfManagmentSeverityIndeterminate = _GenEquipUnitShelfManagmentSeverityIndeterminate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 12, 1, 6),
    _GenEquipUnitShelfManagmentSeverityIndeterminate_Type()
)
genEquipUnitShelfManagmentSeverityIndeterminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfManagmentSeverityIndeterminate.setStatus("mandatory")
_GenEquipUnitShelfPdcFanStatusTable_Object = MibTable
genEquipUnitShelfPdcFanStatusTable = _GenEquipUnitShelfPdcFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 13)
)
if mibBuilder.loadTexts:
    genEquipUnitShelfPdcFanStatusTable.setStatus("mandatory")
_GenEquipUnitShelfPdcFanStatusEntry_Object = MibTableRow
genEquipUnitShelfPdcFanStatusEntry = _GenEquipUnitShelfPdcFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 13, 1)
)
genEquipUnitShelfPdcFanStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitShelfPdcFanStatusPdcFanId"),
)
if mibBuilder.loadTexts:
    genEquipUnitShelfPdcFanStatusEntry.setStatus("mandatory")
_GenEquipUnitShelfPdcFanStatusPdcFanId_Type = Integer32
_GenEquipUnitShelfPdcFanStatusPdcFanId_Object = MibTableColumn
genEquipUnitShelfPdcFanStatusPdcFanId = _GenEquipUnitShelfPdcFanStatusPdcFanId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 13, 1, 1),
    _GenEquipUnitShelfPdcFanStatusPdcFanId_Type()
)
genEquipUnitShelfPdcFanStatusPdcFanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfPdcFanStatusPdcFanId.setStatus("mandatory")
_GenEquipUnitShelfPdcFanStatusPdcFanExMonitor_Type = EnableDisable
_GenEquipUnitShelfPdcFanStatusPdcFanExMonitor_Object = MibTableColumn
genEquipUnitShelfPdcFanStatusPdcFanExMonitor = _GenEquipUnitShelfPdcFanStatusPdcFanExMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 13, 1, 2),
    _GenEquipUnitShelfPdcFanStatusPdcFanExMonitor_Type()
)
genEquipUnitShelfPdcFanStatusPdcFanExMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfPdcFanStatusPdcFanExMonitor.setStatus("mandatory")
_GenEquipUnitShelfPdcFanStatusPdcFanOccupancy_Type = CardOccupancy
_GenEquipUnitShelfPdcFanStatusPdcFanOccupancy_Object = MibTableColumn
genEquipUnitShelfPdcFanStatusPdcFanOccupancy = _GenEquipUnitShelfPdcFanStatusPdcFanOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 13, 1, 3),
    _GenEquipUnitShelfPdcFanStatusPdcFanOccupancy_Type()
)
genEquipUnitShelfPdcFanStatusPdcFanOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfPdcFanStatusPdcFanOccupancy.setStatus("mandatory")
_GenEquipUnitShelfPdcFanStatusPdcFanCardType_Type = InventoryCardType
_GenEquipUnitShelfPdcFanStatusPdcFanCardType_Object = MibTableColumn
genEquipUnitShelfPdcFanStatusPdcFanCardType = _GenEquipUnitShelfPdcFanStatusPdcFanCardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 13, 1, 4),
    _GenEquipUnitShelfPdcFanStatusPdcFanCardType_Type()
)
genEquipUnitShelfPdcFanStatusPdcFanCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfPdcFanStatusPdcFanCardType.setStatus("mandatory")
_GenEquipUnitShelfAbcMuxTable_Object = MibTable
genEquipUnitShelfAbcMuxTable = _GenEquipUnitShelfAbcMuxTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 14)
)
if mibBuilder.loadTexts:
    genEquipUnitShelfAbcMuxTable.setStatus("mandatory")
_GenEquipUnitShelfAbcMuxEntry_Object = MibTableRow
genEquipUnitShelfAbcMuxEntry = _GenEquipUnitShelfAbcMuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 14, 1)
)
genEquipUnitShelfAbcMuxEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipUnitShelfAbcMuxNumber"),
)
if mibBuilder.loadTexts:
    genEquipUnitShelfAbcMuxEntry.setStatus("mandatory")
_GenEquipUnitShelfAbcMuxNumber_Type = Integer32
_GenEquipUnitShelfAbcMuxNumber_Object = MibTableColumn
genEquipUnitShelfAbcMuxNumber = _GenEquipUnitShelfAbcMuxNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 14, 1, 1),
    _GenEquipUnitShelfAbcMuxNumber_Type()
)
genEquipUnitShelfAbcMuxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipUnitShelfAbcMuxNumber.setStatus("mandatory")
_GenEquipUnitShelfAbcMuxAdmin_Type = EnableDisable
_GenEquipUnitShelfAbcMuxAdmin_Object = MibTableColumn
genEquipUnitShelfAbcMuxAdmin = _GenEquipUnitShelfAbcMuxAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 14, 1, 2),
    _GenEquipUnitShelfAbcMuxAdmin_Type()
)
genEquipUnitShelfAbcMuxAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfAbcMuxAdmin.setStatus("mandatory")


class _GenEquipUnitShelfMultiplexTrafficSource_Type(Integer32):
    """Custom type genEquipUnitShelfMultiplexTrafficSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_GenEquipUnitShelfMultiplexTrafficSource_Type.__name__ = "Integer32"
_GenEquipUnitShelfMultiplexTrafficSource_Object = MibScalar
genEquipUnitShelfMultiplexTrafficSource = _GenEquipUnitShelfMultiplexTrafficSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 23),
    _GenEquipUnitShelfMultiplexTrafficSource_Type()
)
genEquipUnitShelfMultiplexTrafficSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfMultiplexTrafficSource.setStatus("mandatory")
_GenEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed_Type = EnableDisable
_GenEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed_Object = MibScalar
genEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed = _GenEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 24),
    _GenEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed_Type()
)
genEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed.setStatus("mandatory")
_GenEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed_Type = EnableDisable
_GenEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed_Object = MibScalar
genEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed = _GenEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 5, 25),
    _GenEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed_Type()
)
genEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed.setStatus("mandatory")
_GenEquipProtection_ObjectIdentity = ObjectIdentity
genEquipProtection = _GenEquipProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6)
)


class _GenEquipProtectionAdmin_Type(Integer32):
    """Custom type genEquipProtectionAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("protection1Plus1Hsb", 2),
          ("protection2Plus0Hsb", 5),
          ("protection2Plus2Hsb", 4),
          ("protectionDisable", 3))
    )


_GenEquipProtectionAdmin_Type.__name__ = "Integer32"
_GenEquipProtectionAdmin_Object = MibScalar
genEquipProtectionAdmin = _GenEquipProtectionAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 1),
    _GenEquipProtectionAdmin_Type()
)
genEquipProtectionAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionAdmin.setStatus("mandatory")


class _GenEquipProtectionMode_Type(Integer32):
    """Custom type genEquipProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("standby", 1))
    )


_GenEquipProtectionMode_Type.__name__ = "Integer32"
_GenEquipProtectionMode_Object = MibScalar
genEquipProtectionMode = _GenEquipProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 2),
    _GenEquipProtectionMode_Type()
)
genEquipProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipProtectionMode.setStatus("mandatory")
_GenEquipProtectionMateIPAddr_Type = IpAddress
_GenEquipProtectionMateIPAddr_Object = MibScalar
genEquipProtectionMateIPAddr = _GenEquipProtectionMateIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 3),
    _GenEquipProtectionMateIPAddr_Type()
)
genEquipProtectionMateIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipProtectionMateIPAddr.setStatus("mandatory")
_GenEquipProtectionMateMACAddr_Type = MacAddress
_GenEquipProtectionMateMACAddr_Object = MibScalar
genEquipProtectionMateMACAddr = _GenEquipProtectionMateMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 4),
    _GenEquipProtectionMateMACAddr_Type()
)
genEquipProtectionMateMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipProtectionMateMACAddr.setStatus("mandatory")
_GenEquipProtectionRadioExcessiveBERSwitch_Type = EnableDisable
_GenEquipProtectionRadioExcessiveBERSwitch_Object = MibScalar
genEquipProtectionRadioExcessiveBERSwitch = _GenEquipProtectionRadioExcessiveBERSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 5),
    _GenEquipProtectionRadioExcessiveBERSwitch_Type()
)
genEquipProtectionRadioExcessiveBERSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionRadioExcessiveBERSwitch.setStatus("mandatory")
_GenEquipProtectionLockout_Type = OffOn
_GenEquipProtectionLockout_Object = MibScalar
genEquipProtectionLockout = _GenEquipProtectionLockout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 6),
    _GenEquipProtectionLockout_Type()
)
genEquipProtectionLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionLockout.setStatus("mandatory")
_GenEquipProtectionForceSwitch_Type = OffOn
_GenEquipProtectionForceSwitch_Object = MibScalar
genEquipProtectionForceSwitch = _GenEquipProtectionForceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 7),
    _GenEquipProtectionForceSwitch_Type()
)
genEquipProtectionForceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionForceSwitch.setStatus("mandatory")
_GenEquipProtectionManualSwitch_Type = OffOn
_GenEquipProtectionManualSwitch_Object = MibScalar
genEquipProtectionManualSwitch = _GenEquipProtectionManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 8),
    _GenEquipProtectionManualSwitch_Type()
)
genEquipProtectionManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionManualSwitch.setStatus("mandatory")
_GenEquipProtectionCopyToMateComand_Type = OffOn
_GenEquipProtectionCopyToMateComand_Object = MibScalar
genEquipProtectionCopyToMateComand = _GenEquipProtectionCopyToMateComand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 9),
    _GenEquipProtectionCopyToMateComand_Type()
)
genEquipProtectionCopyToMateComand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionCopyToMateComand.setStatus("mandatory")
_GenEquipProtectionCopyToMateStatus_Type = ProgressStatus
_GenEquipProtectionCopyToMateStatus_Object = MibScalar
genEquipProtectionCopyToMateStatus = _GenEquipProtectionCopyToMateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 10),
    _GenEquipProtectionCopyToMateStatus_Type()
)
genEquipProtectionCopyToMateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipProtectionCopyToMateStatus.setStatus("mandatory")
_GenEquipProtectionMultiUnitLAGAdmin_Type = EnableDisable
_GenEquipProtectionMultiUnitLAGAdmin_Object = MibScalar
genEquipProtectionMultiUnitLAGAdmin = _GenEquipProtectionMultiUnitLAGAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 11),
    _GenEquipProtectionMultiUnitLAGAdmin_Type()
)
genEquipProtectionMultiUnitLAGAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionMultiUnitLAGAdmin.setStatus("mandatory")
_GenEquipProtectionRevertiveAdmin_Type = EnableDisable
_GenEquipProtectionRevertiveAdmin_Object = MibScalar
genEquipProtectionRevertiveAdmin = _GenEquipProtectionRevertiveAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 12),
    _GenEquipProtectionRevertiveAdmin_Type()
)
genEquipProtectionRevertiveAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionRevertiveAdmin.setStatus("mandatory")


class _GenEquipProtectionRevertivePrimaryIDU_Type(Integer32):
    """Custom type genEquipProtectionRevertivePrimaryIDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lower", 0),
          ("upper", 1))
    )


_GenEquipProtectionRevertivePrimaryIDU_Type.__name__ = "Integer32"
_GenEquipProtectionRevertivePrimaryIDU_Object = MibScalar
genEquipProtectionRevertivePrimaryIDU = _GenEquipProtectionRevertivePrimaryIDU_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 13),
    _GenEquipProtectionRevertivePrimaryIDU_Type()
)
genEquipProtectionRevertivePrimaryIDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionRevertivePrimaryIDU.setStatus("mandatory")


class _GenEquipProtectionRevertiveMinTimer_Type(Integer32):
    """Custom type genEquipProtectionRevertiveMinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GenEquipProtectionRevertiveMinTimer_Type.__name__ = "Integer32"
_GenEquipProtectionRevertiveMinTimer_Object = MibScalar
genEquipProtectionRevertiveMinTimer = _GenEquipProtectionRevertiveMinTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 14),
    _GenEquipProtectionRevertiveMinTimer_Type()
)
genEquipProtectionRevertiveMinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionRevertiveMinTimer.setStatus("mandatory")


class _GenEquipProtectionRevertiveMaxNumOfTries_Type(Integer32):
    """Custom type genEquipProtectionRevertiveMaxNumOfTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_GenEquipProtectionRevertiveMaxNumOfTries_Type.__name__ = "Integer32"
_GenEquipProtectionRevertiveMaxNumOfTries_Object = MibScalar
genEquipProtectionRevertiveMaxNumOfTries = _GenEquipProtectionRevertiveMaxNumOfTries_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 15),
    _GenEquipProtectionRevertiveMaxNumOfTries_Type()
)
genEquipProtectionRevertiveMaxNumOfTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionRevertiveMaxNumOfTries.setStatus("mandatory")


class _GenEquipProtectionRevertiveTimerMultiplier_Type(Integer32):
    """Custom type genEquipProtectionRevertiveTimerMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GenEquipProtectionRevertiveTimerMultiplier_Type.__name__ = "Integer32"
_GenEquipProtectionRevertiveTimerMultiplier_Object = MibScalar
genEquipProtectionRevertiveTimerMultiplier = _GenEquipProtectionRevertiveTimerMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 16),
    _GenEquipProtectionRevertiveTimerMultiplier_Type()
)
genEquipProtectionRevertiveTimerMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionRevertiveTimerMultiplier.setStatus("mandatory")
_GenEquipProtectionAspRevertive_Type = EnableDisable
_GenEquipProtectionAspRevertive_Object = MibScalar
genEquipProtectionAspRevertive = _GenEquipProtectionAspRevertive_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 6, 17),
    _GenEquipProtectionAspRevertive_Type()
)
genEquipProtectionAspRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipProtectionAspRevertive.setStatus("mandatory")
_GenEquipDiversity_ObjectIdentity = ObjectIdentity
genEquipDiversity = _GenEquipDiversity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7)
)


class _GenEquipDiversityType_Type(Integer32):
    """Custom type genEquipDiversityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frequency-diversity", 3),
          ("none", 1),
          ("space-diversity", 2))
    )


_GenEquipDiversityType_Type.__name__ = "Integer32"
_GenEquipDiversityType_Object = MibScalar
genEquipDiversityType = _GenEquipDiversityType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7, 1),
    _GenEquipDiversityType_Type()
)
genEquipDiversityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiversityType.setStatus("mandatory")


class _GenEquipDiversityRevertiveMode_Type(Integer32):
    """Custom type genEquipDiversityRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-revertive", 1),
          ("revertive", 2))
    )


_GenEquipDiversityRevertiveMode_Type.__name__ = "Integer32"
_GenEquipDiversityRevertiveMode_Object = MibScalar
genEquipDiversityRevertiveMode = _GenEquipDiversityRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7, 2),
    _GenEquipDiversityRevertiveMode_Type()
)
genEquipDiversityRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiversityRevertiveMode.setStatus("mandatory")


class _GenEquipDiversityPrimaryRadio_Type(Integer32):
    """Custom type genEquipDiversityPrimaryRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower-radio", 2),
          ("upper-radio", 1))
    )


_GenEquipDiversityPrimaryRadio_Type.__name__ = "Integer32"
_GenEquipDiversityPrimaryRadio_Object = MibScalar
genEquipDiversityPrimaryRadio = _GenEquipDiversityPrimaryRadio_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7, 3),
    _GenEquipDiversityPrimaryRadio_Type()
)
genEquipDiversityPrimaryRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiversityPrimaryRadio.setStatus("mandatory")


class _GenEquipDiversityRevertiveTimer_Type(Integer32):
    """Custom type genEquipDiversityRevertiveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GenEquipDiversityRevertiveTimer_Type.__name__ = "Integer32"
_GenEquipDiversityRevertiveTimer_Object = MibScalar
genEquipDiversityRevertiveTimer = _GenEquipDiversityRevertiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7, 4),
    _GenEquipDiversityRevertiveTimer_Type()
)
genEquipDiversityRevertiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiversityRevertiveTimer.setStatus("mandatory")


class _GenEquipDiversityForceActive_Type(Integer32):
    """Custom type genEquipDiversityForceActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-radio", 1),
          ("mate-radio", 2),
          ("none", 0))
    )


_GenEquipDiversityForceActive_Type.__name__ = "Integer32"
_GenEquipDiversityForceActive_Object = MibScalar
genEquipDiversityForceActive = _GenEquipDiversityForceActive_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7, 5),
    _GenEquipDiversityForceActive_Type()
)
genEquipDiversityForceActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiversityForceActive.setStatus("mandatory")
_GenEquipDiversitySwitchCounter_Type = Integer32
_GenEquipDiversitySwitchCounter_Object = MibScalar
genEquipDiversitySwitchCounter = _GenEquipDiversitySwitchCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7, 6),
    _GenEquipDiversitySwitchCounter_Type()
)
genEquipDiversitySwitchCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipDiversitySwitchCounter.setStatus("mandatory")
_GenEquipDiversitySwitchCounterClear_Type = OffOn
_GenEquipDiversitySwitchCounterClear_Object = MibScalar
genEquipDiversitySwitchCounterClear = _GenEquipDiversitySwitchCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7, 7),
    _GenEquipDiversitySwitchCounterClear_Type()
)
genEquipDiversitySwitchCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiversitySwitchCounterClear.setStatus("mandatory")


class _GenEquipDiversityReceiveRadio_Type(Integer32):
    """Custom type genEquipDiversityReceiveRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lower-idu", 0),
          ("upper-idu", 1))
    )


_GenEquipDiversityReceiveRadio_Type.__name__ = "Integer32"
_GenEquipDiversityReceiveRadio_Object = MibScalar
genEquipDiversityReceiveRadio = _GenEquipDiversityReceiveRadio_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1, 7, 8),
    _GenEquipDiversityReceiveRadio_Type()
)
genEquipDiversityReceiveRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipDiversityReceiveRadio.setStatus("mandatory")
_GenEquipFault_ObjectIdentity = ObjectIdentity
genEquipFault = _GenEquipFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3)
)
_GenEquipCurrentAlarm_ObjectIdentity = ObjectIdentity
genEquipCurrentAlarm = _GenEquipCurrentAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1)
)
_GenEquipCurrentAlarmLastChangeCounter_Type = Integer32
_GenEquipCurrentAlarmLastChangeCounter_Object = MibScalar
genEquipCurrentAlarmLastChangeCounter = _GenEquipCurrentAlarmLastChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 1),
    _GenEquipCurrentAlarmLastChangeCounter_Type()
)
genEquipCurrentAlarmLastChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmLastChangeCounter.setStatus("mandatory")
_GenEquipCurrentAlarmTable_Object = MibTable
genEquipCurrentAlarmTable = _GenEquipCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2)
)
if mibBuilder.loadTexts:
    genEquipCurrentAlarmTable.setStatus("mandatory")
_GenEquipCurrentAlarmEntry_Object = MibTableRow
genEquipCurrentAlarmEntry = _GenEquipCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1)
)
genEquipCurrentAlarmEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipCurrentAlarmCounter"),
)
if mibBuilder.loadTexts:
    genEquipCurrentAlarmEntry.setStatus("mandatory")
_GenEquipCurrentAlarmCounter_Type = Integer32
_GenEquipCurrentAlarmCounter_Object = MibTableColumn
genEquipCurrentAlarmCounter = _GenEquipCurrentAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 1),
    _GenEquipCurrentAlarmCounter_Type()
)
genEquipCurrentAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmCounter.setStatus("mandatory")
_GenEquipCurrentAlarmRaisedTimeT_Type = Integer32
_GenEquipCurrentAlarmRaisedTimeT_Object = MibTableColumn
genEquipCurrentAlarmRaisedTimeT = _GenEquipCurrentAlarmRaisedTimeT_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 2),
    _GenEquipCurrentAlarmRaisedTimeT_Type()
)
genEquipCurrentAlarmRaisedTimeT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmRaisedTimeT.setStatus("mandatory")
_GenEquipCurrentAlarmId_Type = Integer32
_GenEquipCurrentAlarmId_Object = MibTableColumn
genEquipCurrentAlarmId = _GenEquipCurrentAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 3),
    _GenEquipCurrentAlarmId_Type()
)
genEquipCurrentAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmId.setStatus("mandatory")
_GenEquipCurrentAlarmName_Type = DisplayString
_GenEquipCurrentAlarmName_Object = MibTableColumn
genEquipCurrentAlarmName = _GenEquipCurrentAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 4),
    _GenEquipCurrentAlarmName_Type()
)
genEquipCurrentAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmName.setStatus("mandatory")
_GenEquipCurrentAlarmInstance_Type = Integer32
_GenEquipCurrentAlarmInstance_Object = MibTableColumn
genEquipCurrentAlarmInstance = _GenEquipCurrentAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 5),
    _GenEquipCurrentAlarmInstance_Type()
)
genEquipCurrentAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmInstance.setStatus("mandatory")


class _GenEquipCurrentAlarmSeverity_Type(Severity):
    """Custom type genEquipCurrentAlarmSeverity based on Severity"""


_GenEquipCurrentAlarmSeverity_Object = MibTableColumn
genEquipCurrentAlarmSeverity = _GenEquipCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 6),
    _GenEquipCurrentAlarmSeverity_Type()
)
genEquipCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmSeverity.setStatus("mandatory")
_GenEquipCurrentAlarmIfIndex_Type = Integer32
_GenEquipCurrentAlarmIfIndex_Object = MibTableColumn
genEquipCurrentAlarmIfIndex = _GenEquipCurrentAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 7),
    _GenEquipCurrentAlarmIfIndex_Type()
)
genEquipCurrentAlarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmIfIndex.setStatus("mandatory")
_GenEquipCurrentAlarmModule_Type = DisplayString
_GenEquipCurrentAlarmModule_Object = MibTableColumn
genEquipCurrentAlarmModule = _GenEquipCurrentAlarmModule_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 8),
    _GenEquipCurrentAlarmModule_Type()
)
genEquipCurrentAlarmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmModule.setStatus("mandatory")
_GenEquipCurrentAlarmDesc_Type = DisplayString
_GenEquipCurrentAlarmDesc_Object = MibTableColumn
genEquipCurrentAlarmDesc = _GenEquipCurrentAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 9),
    _GenEquipCurrentAlarmDesc_Type()
)
genEquipCurrentAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmDesc.setStatus("mandatory")
_GenEquipCurrentAlarmProbableCause_Type = DisplayString
_GenEquipCurrentAlarmProbableCause_Object = MibTableColumn
genEquipCurrentAlarmProbableCause = _GenEquipCurrentAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 10),
    _GenEquipCurrentAlarmProbableCause_Type()
)
genEquipCurrentAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmProbableCause.setStatus("mandatory")
_GenEquipCurrentAlarmCorrectiveActions_Type = DisplayString
_GenEquipCurrentAlarmCorrectiveActions_Object = MibTableColumn
genEquipCurrentAlarmCorrectiveActions = _GenEquipCurrentAlarmCorrectiveActions_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 11),
    _GenEquipCurrentAlarmCorrectiveActions_Type()
)
genEquipCurrentAlarmCorrectiveActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmCorrectiveActions.setStatus("mandatory")


class _GenEquipCurrentAlarmState_Type(Integer32):
    """Custom type genEquipCurrentAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("event", 2),
          ("raised", 1))
    )


_GenEquipCurrentAlarmState_Type.__name__ = "Integer32"
_GenEquipCurrentAlarmState_Object = MibTableColumn
genEquipCurrentAlarmState = _GenEquipCurrentAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 12),
    _GenEquipCurrentAlarmState_Type()
)
genEquipCurrentAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmState.setStatus("mandatory")
_GenEquipCurrentAlarmSlotId_Type = SlotId
_GenEquipCurrentAlarmSlotId_Object = MibTableColumn
genEquipCurrentAlarmSlotId = _GenEquipCurrentAlarmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 13),
    _GenEquipCurrentAlarmSlotId_Type()
)
genEquipCurrentAlarmSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmSlotId.setStatus("mandatory")
_GenEquipCurrentAlarmAdditionalInfo_Type = DisplayString
_GenEquipCurrentAlarmAdditionalInfo_Object = MibTableColumn
genEquipCurrentAlarmAdditionalInfo = _GenEquipCurrentAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 14),
    _GenEquipCurrentAlarmAdditionalInfo_Type()
)
genEquipCurrentAlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmAdditionalInfo.setStatus("mandatory")
_GenEquipCurrentAlarmUserText_Type = DisplayString
_GenEquipCurrentAlarmUserText_Object = MibTableColumn
genEquipCurrentAlarmUserText = _GenEquipCurrentAlarmUserText_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 2, 1, 15),
    _GenEquipCurrentAlarmUserText_Type()
)
genEquipCurrentAlarmUserText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipCurrentAlarmUserText.setStatus("mandatory")
_GenEquipMostSevereAlarm_Type = Severity
_GenEquipMostSevereAlarm_Object = MibScalar
genEquipMostSevereAlarm = _GenEquipMostSevereAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 3),
    _GenEquipMostSevereAlarm_Type()
)
genEquipMostSevereAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMostSevereAlarm.setStatus("mandatory")
_GenEquipAlarmConfigDefault_Type = OffOn
_GenEquipAlarmConfigDefault_Object = MibScalar
genEquipAlarmConfigDefault = _GenEquipAlarmConfigDefault_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 4),
    _GenEquipAlarmConfigDefault_Type()
)
genEquipAlarmConfigDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipAlarmConfigDefault.setStatus("mandatory")
_GenEquipAlarmConfigTable_Object = MibTable
genEquipAlarmConfigTable = _GenEquipAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 5)
)
if mibBuilder.loadTexts:
    genEquipAlarmConfigTable.setStatus("mandatory")
_GenEquipAlarmConfigEntry_Object = MibTableRow
genEquipAlarmConfigEntry = _GenEquipAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 5, 1)
)
genEquipAlarmConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipAlarmConfigId"),
)
if mibBuilder.loadTexts:
    genEquipAlarmConfigEntry.setStatus("mandatory")
_GenEquipAlarmConfigId_Type = Integer32
_GenEquipAlarmConfigId_Object = MibTableColumn
genEquipAlarmConfigId = _GenEquipAlarmConfigId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 5, 1, 1),
    _GenEquipAlarmConfigId_Type()
)
genEquipAlarmConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipAlarmConfigId.setStatus("mandatory")
_GenEquipAlarmConfigSeverity_Type = Severity
_GenEquipAlarmConfigSeverity_Object = MibTableColumn
genEquipAlarmConfigSeverity = _GenEquipAlarmConfigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 5, 1, 2),
    _GenEquipAlarmConfigSeverity_Type()
)
genEquipAlarmConfigSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipAlarmConfigSeverity.setStatus("mandatory")
_GenEquipAlarmConfigDescr_Type = DisplayString
_GenEquipAlarmConfigDescr_Object = MibTableColumn
genEquipAlarmConfigDescr = _GenEquipAlarmConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 5, 1, 3),
    _GenEquipAlarmConfigDescr_Type()
)
genEquipAlarmConfigDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipAlarmConfigDescr.setStatus("mandatory")
_GenEquipAlarmConfigAdditionalText_Type = DisplayString
_GenEquipAlarmConfigAdditionalText_Object = MibTableColumn
genEquipAlarmConfigAdditionalText = _GenEquipAlarmConfigAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 5, 1, 4),
    _GenEquipAlarmConfigAdditionalText_Type()
)
genEquipAlarmConfigAdditionalText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipAlarmConfigAdditionalText.setStatus("mandatory")
_GenEquipAlarmServiceAffect_Type = OffOn
_GenEquipAlarmServiceAffect_Object = MibTableColumn
genEquipAlarmServiceAffect = _GenEquipAlarmServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 1, 5, 1, 5),
    _GenEquipAlarmServiceAffect_Type()
)
genEquipAlarmServiceAffect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipAlarmServiceAffect.setStatus("mandatory")
_GenEquipTrapCfg_ObjectIdentity = ObjectIdentity
genEquipTrapCfg = _GenEquipTrapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2)
)
_GenEquipTrapCfgMgrTable_Object = MibTable
genEquipTrapCfgMgrTable = _GenEquipTrapCfgMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1)
)
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrTable.setStatus("mandatory")
_GenEquipTrapCfgMgrEntry_Object = MibTableRow
genEquipTrapCfgMgrEntry = _GenEquipTrapCfgMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1)
)
genEquipTrapCfgMgrEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipTrapCfgMgrId"),
)
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrEntry.setStatus("mandatory")
_GenEquipTrapCfgMgrId_Type = Integer32
_GenEquipTrapCfgMgrId_Object = MibTableColumn
genEquipTrapCfgMgrId = _GenEquipTrapCfgMgrId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 1),
    _GenEquipTrapCfgMgrId_Type()
)
genEquipTrapCfgMgrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrId.setStatus("mandatory")
_GenEquipTrapCfgMgrAdmin_Type = EnableDisable
_GenEquipTrapCfgMgrAdmin_Object = MibTableColumn
genEquipTrapCfgMgrAdmin = _GenEquipTrapCfgMgrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 2),
    _GenEquipTrapCfgMgrAdmin_Type()
)
genEquipTrapCfgMgrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrAdmin.setStatus("mandatory")
_GenEquipTrapCfgMgrIP_Type = IpAddress
_GenEquipTrapCfgMgrIP_Object = MibTableColumn
genEquipTrapCfgMgrIP = _GenEquipTrapCfgMgrIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 3),
    _GenEquipTrapCfgMgrIP_Type()
)
genEquipTrapCfgMgrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrIP.setStatus("mandatory")


class _GenEquipTrapCfgMgrPort_Type(Integer32):
    """Custom type genEquipTrapCfgMgrPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 65535),
    )


_GenEquipTrapCfgMgrPort_Type.__name__ = "Integer32"
_GenEquipTrapCfgMgrPort_Object = MibTableColumn
genEquipTrapCfgMgrPort = _GenEquipTrapCfgMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 4),
    _GenEquipTrapCfgMgrPort_Type()
)
genEquipTrapCfgMgrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrPort.setStatus("mandatory")


class _GenEquipTrapCfgMgrName_Type(DisplayString):
    """Custom type genEquipTrapCfgMgrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GenEquipTrapCfgMgrName_Type.__name__ = "DisplayString"
_GenEquipTrapCfgMgrName_Object = MibTableColumn
genEquipTrapCfgMgrName = _GenEquipTrapCfgMgrName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 5),
    _GenEquipTrapCfgMgrName_Type()
)
genEquipTrapCfgMgrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrName.setStatus("mandatory")


class _GenEquipTrapCfgMgrCommunity_Type(DisplayString):
    """Custom type genEquipTrapCfgMgrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GenEquipTrapCfgMgrCommunity_Type.__name__ = "DisplayString"
_GenEquipTrapCfgMgrCommunity_Object = MibTableColumn
genEquipTrapCfgMgrCommunity = _GenEquipTrapCfgMgrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 6),
    _GenEquipTrapCfgMgrCommunity_Type()
)
genEquipTrapCfgMgrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrCommunity.setStatus("mandatory")
_GenEquipTrapCfgMgrSeverityFilter_Type = Integer32
_GenEquipTrapCfgMgrSeverityFilter_Object = MibTableColumn
genEquipTrapCfgMgrSeverityFilter = _GenEquipTrapCfgMgrSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 7),
    _GenEquipTrapCfgMgrSeverityFilter_Type()
)
genEquipTrapCfgMgrSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrSeverityFilter.setStatus("mandatory")
_GenEquipTrapCfgMgrStatusChangeFilter_Type = OffOn
_GenEquipTrapCfgMgrStatusChangeFilter_Object = MibTableColumn
genEquipTrapCfgMgrStatusChangeFilter = _GenEquipTrapCfgMgrStatusChangeFilter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 8),
    _GenEquipTrapCfgMgrStatusChangeFilter_Type()
)
genEquipTrapCfgMgrStatusChangeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrStatusChangeFilter.setStatus("mandatory")


class _GenEquipTrapCfgMgrCLLI_Type(DisplayString):
    """Custom type genEquipTrapCfgMgrCLLI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GenEquipTrapCfgMgrCLLI_Type.__name__ = "DisplayString"
_GenEquipTrapCfgMgrCLLI_Object = MibTableColumn
genEquipTrapCfgMgrCLLI = _GenEquipTrapCfgMgrCLLI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 9),
    _GenEquipTrapCfgMgrCLLI_Type()
)
genEquipTrapCfgMgrCLLI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrCLLI.setStatus("mandatory")


class _GenEquipTrapCfgMgrHeartbeatPeriod_Type(Integer32):
    """Custom type genEquipTrapCfgMgrHeartbeatPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GenEquipTrapCfgMgrHeartbeatPeriod_Type.__name__ = "Integer32"
_GenEquipTrapCfgMgrHeartbeatPeriod_Object = MibTableColumn
genEquipTrapCfgMgrHeartbeatPeriod = _GenEquipTrapCfgMgrHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 10),
    _GenEquipTrapCfgMgrHeartbeatPeriod_Type()
)
genEquipTrapCfgMgrHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrHeartbeatPeriod.setStatus("mandatory")


class _GenEquipTrapCfgMgrIPv6_Type(OctetString):
    """Custom type genEquipTrapCfgMgrIPv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipTrapCfgMgrIPv6_Type.__name__ = "OctetString"
_GenEquipTrapCfgMgrIPv6_Object = MibTableColumn
genEquipTrapCfgMgrIPv6 = _GenEquipTrapCfgMgrIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 11),
    _GenEquipTrapCfgMgrIPv6_Type()
)
genEquipTrapCfgMgrIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrIPv6.setStatus("mandatory")
_GenEquipTrapCfgMgrV3User_Type = DisplayString
_GenEquipTrapCfgMgrV3User_Object = MibTableColumn
genEquipTrapCfgMgrV3User = _GenEquipTrapCfgMgrV3User_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 2, 1, 1, 12),
    _GenEquipTrapCfgMgrV3User_Type()
)
genEquipTrapCfgMgrV3User.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrapCfgMgrV3User.setStatus("mandatory")
_GenEquipEventLog_ObjectIdentity = ObjectIdentity
genEquipEventLog = _GenEquipEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3)
)
_GenEquipEventLogTable_Object = MibTable
genEquipEventLogTable = _GenEquipEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1)
)
if mibBuilder.loadTexts:
    genEquipEventLogTable.setStatus("mandatory")
_GenEquipEventLogEntry_Object = MibTableRow
genEquipEventLogEntry = _GenEquipEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1)
)
genEquipEventLogEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipEventLogCounter"),
)
if mibBuilder.loadTexts:
    genEquipEventLogEntry.setStatus("mandatory")
_GenEquipEventLogCounter_Type = Integer32
_GenEquipEventLogCounter_Object = MibTableColumn
genEquipEventLogCounter = _GenEquipEventLogCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 1),
    _GenEquipEventLogCounter_Type()
)
genEquipEventLogCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogCounter.setStatus("mandatory")
_GenEquipEventLogRaisedTimeT_Type = Integer32
_GenEquipEventLogRaisedTimeT_Object = MibTableColumn
genEquipEventLogRaisedTimeT = _GenEquipEventLogRaisedTimeT_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 2),
    _GenEquipEventLogRaisedTimeT_Type()
)
genEquipEventLogRaisedTimeT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogRaisedTimeT.setStatus("mandatory")
_GenEquipEventLogSeverity_Type = Severity
_GenEquipEventLogSeverity_Object = MibTableColumn
genEquipEventLogSeverity = _GenEquipEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 3),
    _GenEquipEventLogSeverity_Type()
)
genEquipEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogSeverity.setStatus("mandatory")
_GenEquipEventLogModule_Type = DisplayString
_GenEquipEventLogModule_Object = MibTableColumn
genEquipEventLogModule = _GenEquipEventLogModule_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 4),
    _GenEquipEventLogModule_Type()
)
genEquipEventLogModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogModule.setStatus("mandatory")
_GenEquipEventLogDesc_Type = DisplayString
_GenEquipEventLogDesc_Object = MibTableColumn
genEquipEventLogDesc = _GenEquipEventLogDesc_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 5),
    _GenEquipEventLogDesc_Type()
)
genEquipEventLogDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogDesc.setStatus("mandatory")


class _GenEquipEventLogState_Type(Integer32):
    """Custom type genEquipEventLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("event", 2),
          ("raised", 1))
    )


_GenEquipEventLogState_Type.__name__ = "Integer32"
_GenEquipEventLogState_Object = MibTableColumn
genEquipEventLogState = _GenEquipEventLogState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 6),
    _GenEquipEventLogState_Type()
)
genEquipEventLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogState.setStatus("mandatory")
_GenEquipEventLogProbableCause_Type = DisplayString
_GenEquipEventLogProbableCause_Object = MibTableColumn
genEquipEventLogProbableCause = _GenEquipEventLogProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 7),
    _GenEquipEventLogProbableCause_Type()
)
genEquipEventLogProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogProbableCause.setStatus("mandatory")
_GenEquipEventLogCorrectiveActions_Type = DisplayString
_GenEquipEventLogCorrectiveActions_Object = MibTableColumn
genEquipEventLogCorrectiveActions = _GenEquipEventLogCorrectiveActions_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 8),
    _GenEquipEventLogCorrectiveActions_Type()
)
genEquipEventLogCorrectiveActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogCorrectiveActions.setStatus("mandatory")
_GenEquipEventLogAdditionalInfo_Type = DisplayString
_GenEquipEventLogAdditionalInfo_Object = MibTableColumn
genEquipEventLogAdditionalInfo = _GenEquipEventLogAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 9),
    _GenEquipEventLogAdditionalInfo_Type()
)
genEquipEventLogAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogAdditionalInfo.setStatus("mandatory")
_GenEquipEventLogUserText_Type = DisplayString
_GenEquipEventLogUserText_Object = MibTableColumn
genEquipEventLogUserText = _GenEquipEventLogUserText_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 10),
    _GenEquipEventLogUserText_Type()
)
genEquipEventLogUserText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogUserText.setStatus("mandatory")
_GenEquipEventLogIfIndex_Type = Integer32
_GenEquipEventLogIfIndex_Object = MibTableColumn
genEquipEventLogIfIndex = _GenEquipEventLogIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 11),
    _GenEquipEventLogIfIndex_Type()
)
genEquipEventLogIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogIfIndex.setStatus("mandatory")
_GenEquipEventLogId_Type = Integer32
_GenEquipEventLogId_Object = MibTableColumn
genEquipEventLogId = _GenEquipEventLogId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 1, 1, 12),
    _GenEquipEventLogId_Type()
)
genEquipEventLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogId.setStatus("mandatory")
_GenEquipEventLogClear_Type = OffOn
_GenEquipEventLogClear_Object = MibScalar
genEquipEventLogClear = _GenEquipEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 2),
    _GenEquipEventLogClear_Type()
)
genEquipEventLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipEventLogClear.setStatus("mandatory")
_GenEquipEventLogLastChangeCounter_Type = Integer32
_GenEquipEventLogLastChangeCounter_Object = MibScalar
genEquipEventLogLastChangeCounter = _GenEquipEventLogLastChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 3, 3),
    _GenEquipEventLogLastChangeCounter_Type()
)
genEquipEventLogLastChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipEventLogLastChangeCounter.setStatus("mandatory")
_GenEquipFaultErrno_Type = Integer32
_GenEquipFaultErrno_Object = MibScalar
genEquipFaultErrno = _GenEquipFaultErrno_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 4),
    _GenEquipFaultErrno_Type()
)
genEquipFaultErrno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipFaultErrno.setStatus("mandatory")
_GenEquipFaultErrDescr_Type = DisplayString
_GenEquipFaultErrDescr_Object = MibScalar
genEquipFaultErrDescr = _GenEquipFaultErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 3, 5),
    _GenEquipFaultErrDescr_Type()
)
genEquipFaultErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipFaultErrDescr.setStatus("mandatory")
_GenEquipMng_ObjectIdentity = ObjectIdentity
genEquipMng = _GenEquipMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4)
)
_GenEquipMngSw_ObjectIdentity = ObjectIdentity
genEquipMngSw = _GenEquipMngSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1)
)
_GenEquipMngSwServerUrl_Type = DisplayString
_GenEquipMngSwServerUrl_Object = MibScalar
genEquipMngSwServerUrl = _GenEquipMngSwServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 1),
    _GenEquipMngSwServerUrl_Type()
)
genEquipMngSwServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwServerUrl.setStatus("mandatory")
_GenEquipMngSwServerLogin_Type = DisplayString
_GenEquipMngSwServerLogin_Object = MibScalar
genEquipMngSwServerLogin = _GenEquipMngSwServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 2),
    _GenEquipMngSwServerLogin_Type()
)
genEquipMngSwServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwServerLogin.setStatus("mandatory")
_GenEquipMngSwServerPassword_Type = DisplayString
_GenEquipMngSwServerPassword_Object = MibScalar
genEquipMngSwServerPassword = _GenEquipMngSwServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 3),
    _GenEquipMngSwServerPassword_Type()
)
genEquipMngSwServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwServerPassword.setStatus("mandatory")
_GenEquipMngSwProxyUrl_Type = DisplayString
_GenEquipMngSwProxyUrl_Object = MibScalar
genEquipMngSwProxyUrl = _GenEquipMngSwProxyUrl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 4),
    _GenEquipMngSwProxyUrl_Type()
)
genEquipMngSwProxyUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwProxyUrl.setStatus("obsolete")
_GenEquipMngSwProxyLogin_Type = DisplayString
_GenEquipMngSwProxyLogin_Object = MibScalar
genEquipMngSwProxyLogin = _GenEquipMngSwProxyLogin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 5),
    _GenEquipMngSwProxyLogin_Type()
)
genEquipMngSwProxyLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwProxyLogin.setStatus("obsolete")
_GenEquipMngSwProxyPassword_Type = DisplayString
_GenEquipMngSwProxyPassword_Object = MibScalar
genEquipMngSwProxyPassword = _GenEquipMngSwProxyPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 6),
    _GenEquipMngSwProxyPassword_Type()
)
genEquipMngSwProxyPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwProxyPassword.setStatus("obsolete")
_GenEquipMngSwDownloadStatus_Type = ProgressStatus
_GenEquipMngSwDownloadStatus_Object = MibScalar
genEquipMngSwDownloadStatus = _GenEquipMngSwDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 7),
    _GenEquipMngSwDownloadStatus_Type()
)
genEquipMngSwDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwDownloadStatus.setStatus("mandatory")
_GenEquipMngSwInstallStatus_Type = ProgressStatus
_GenEquipMngSwInstallStatus_Object = MibScalar
genEquipMngSwInstallStatus = _GenEquipMngSwInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 8),
    _GenEquipMngSwInstallStatus_Type()
)
genEquipMngSwInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwInstallStatus.setStatus("mandatory")
_GenEquipMngSwCommand_Type = SwCommandTimer
_GenEquipMngSwCommand_Object = MibScalar
genEquipMngSwCommand = _GenEquipMngSwCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 9),
    _GenEquipMngSwCommand_Type()
)
genEquipMngSwCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwCommand.setStatus("mandatory")
_GenEquipMngSwInstalledIduVersion_Type = DisplayString
_GenEquipMngSwInstalledIduVersion_Object = MibScalar
genEquipMngSwInstalledIduVersion = _GenEquipMngSwInstalledIduVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 10),
    _GenEquipMngSwInstalledIduVersion_Type()
)
genEquipMngSwInstalledIduVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwInstalledIduVersion.setStatus("mandatory")
_GenEquipMngSwInstalledRfuVersion_Type = DisplayString
_GenEquipMngSwInstalledRfuVersion_Object = MibScalar
genEquipMngSwInstalledRfuVersion = _GenEquipMngSwInstalledRfuVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 11),
    _GenEquipMngSwInstalledRfuVersion_Type()
)
genEquipMngSwInstalledRfuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwInstalledRfuVersion.setStatus("mandatory")
_GenEquipMngSwVersions_ObjectIdentity = ObjectIdentity
genEquipMngSwVersions = _GenEquipMngSwVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13)
)
_GenEquipMngSwIDUVersionsTable_Object = MibTable
genEquipMngSwIDUVersionsTable = _GenEquipMngSwIDUVersionsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsTable.setStatus("mandatory")
_GenEquipMngSwIDUVersionsEntry_Object = MibTableRow
genEquipMngSwIDUVersionsEntry = _GenEquipMngSwIDUVersionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1)
)
genEquipMngSwIDUVersionsEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngSwIDUVersionsCounter"),
)
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsEntry.setStatus("mandatory")
_GenEquipMngSwIDUVersionsCounter_Type = Integer32
_GenEquipMngSwIDUVersionsCounter_Object = MibTableColumn
genEquipMngSwIDUVersionsCounter = _GenEquipMngSwIDUVersionsCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1, 1),
    _GenEquipMngSwIDUVersionsCounter_Type()
)
genEquipMngSwIDUVersionsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsCounter.setStatus("mandatory")
_GenEquipMngSwIDUVersionsPackageName_Type = DisplayString
_GenEquipMngSwIDUVersionsPackageName_Object = MibTableColumn
genEquipMngSwIDUVersionsPackageName = _GenEquipMngSwIDUVersionsPackageName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1, 2),
    _GenEquipMngSwIDUVersionsPackageName_Type()
)
genEquipMngSwIDUVersionsPackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsPackageName.setStatus("mandatory")
_GenEquipMngSwIDUVersionsTargetDevice_Type = DisplayString
_GenEquipMngSwIDUVersionsTargetDevice_Object = MibTableColumn
genEquipMngSwIDUVersionsTargetDevice = _GenEquipMngSwIDUVersionsTargetDevice_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1, 3),
    _GenEquipMngSwIDUVersionsTargetDevice_Type()
)
genEquipMngSwIDUVersionsTargetDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsTargetDevice.setStatus("mandatory")
_GenEquipMngSwIDUVersionsRunningVersion_Type = DisplayString
_GenEquipMngSwIDUVersionsRunningVersion_Object = MibTableColumn
genEquipMngSwIDUVersionsRunningVersion = _GenEquipMngSwIDUVersionsRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1, 4),
    _GenEquipMngSwIDUVersionsRunningVersion_Type()
)
genEquipMngSwIDUVersionsRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsRunningVersion.setStatus("mandatory")
_GenEquipMngSwIDUVersionsInstalledVersion_Type = DisplayString
_GenEquipMngSwIDUVersionsInstalledVersion_Object = MibTableColumn
genEquipMngSwIDUVersionsInstalledVersion = _GenEquipMngSwIDUVersionsInstalledVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1, 5),
    _GenEquipMngSwIDUVersionsInstalledVersion_Type()
)
genEquipMngSwIDUVersionsInstalledVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsInstalledVersion.setStatus("mandatory")
_GenEquipMngSwIDUVersionsUpgradePackage_Type = DisplayString
_GenEquipMngSwIDUVersionsUpgradePackage_Object = MibTableColumn
genEquipMngSwIDUVersionsUpgradePackage = _GenEquipMngSwIDUVersionsUpgradePackage_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1, 6),
    _GenEquipMngSwIDUVersionsUpgradePackage_Type()
)
genEquipMngSwIDUVersionsUpgradePackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsUpgradePackage.setStatus("mandatory")
_GenEquipMngSwIDUVersionsDowngradePackage_Type = DisplayString
_GenEquipMngSwIDUVersionsDowngradePackage_Object = MibTableColumn
genEquipMngSwIDUVersionsDowngradePackage = _GenEquipMngSwIDUVersionsDowngradePackage_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1, 7),
    _GenEquipMngSwIDUVersionsDowngradePackage_Type()
)
genEquipMngSwIDUVersionsDowngradePackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsDowngradePackage.setStatus("mandatory")


class _GenEquipMngSwIDUVersionsResetType_Type(Integer32):
    """Custom type genEquipMngSwIDUVersionsResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("appWarmReset", 1),
          ("applicationRestart", 5),
          ("cardReset", 6),
          ("mainBoardColdReset", 3),
          ("mainBoardWarmReset", 4),
          ("noReset", 0),
          ("notApplicable", 7),
          ("tccColdReset", 2))
    )


_GenEquipMngSwIDUVersionsResetType_Type.__name__ = "Integer32"
_GenEquipMngSwIDUVersionsResetType_Object = MibTableColumn
genEquipMngSwIDUVersionsResetType = _GenEquipMngSwIDUVersionsResetType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 1, 1, 8),
    _GenEquipMngSwIDUVersionsResetType_Type()
)
genEquipMngSwIDUVersionsResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsResetType.setStatus("mandatory")
_GenEquipMngSwTimerTable_Object = MibTable
genEquipMngSwTimerTable = _GenEquipMngSwTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 2)
)
if mibBuilder.loadTexts:
    genEquipMngSwTimerTable.setStatus("mandatory")
_GenEquipMngSwTimerEntry_Object = MibTableRow
genEquipMngSwTimerEntry = _GenEquipMngSwTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 2, 1)
)
genEquipMngSwTimerEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngSwTimerSlotNumber"),
)
if mibBuilder.loadTexts:
    genEquipMngSwTimerEntry.setStatus("mandatory")


class _GenEquipMngSwTimerSlotNumber_Type(Integer32):
    """Custom type genEquipMngSwTimerSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_GenEquipMngSwTimerSlotNumber_Type.__name__ = "Integer32"
_GenEquipMngSwTimerSlotNumber_Object = MibTableColumn
genEquipMngSwTimerSlotNumber = _GenEquipMngSwTimerSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 2, 1, 1),
    _GenEquipMngSwTimerSlotNumber_Type()
)
genEquipMngSwTimerSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwTimerSlotNumber.setStatus("mandatory")


class _GenEquipMngSwTimerInstallationTimer_Type(Integer32):
    """Custom type genEquipMngSwTimerInstallationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_GenEquipMngSwTimerInstallationTimer_Type.__name__ = "Integer32"
_GenEquipMngSwTimerInstallationTimer_Object = MibTableColumn
genEquipMngSwTimerInstallationTimer = _GenEquipMngSwTimerInstallationTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 2, 1, 2),
    _GenEquipMngSwTimerInstallationTimer_Type()
)
genEquipMngSwTimerInstallationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwTimerInstallationTimer.setStatus("mandatory")


class _GenEquipMngSwTimerTimeToInstall_Type(Integer32):
    """Custom type genEquipMngSwTimerTimeToInstall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_GenEquipMngSwTimerTimeToInstall_Type.__name__ = "Integer32"
_GenEquipMngSwTimerTimeToInstall_Object = MibTableColumn
genEquipMngSwTimerTimeToInstall = _GenEquipMngSwTimerTimeToInstall_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 2, 1, 3),
    _GenEquipMngSwTimerTimeToInstall_Type()
)
genEquipMngSwTimerTimeToInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwTimerTimeToInstall.setStatus("mandatory")


class _GenEquipMngSwTimerTimerAbort_Type(Integer32):
    """Custom type genEquipMngSwTimerTimerAbort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abort", 1),
          ("proceed", 0))
    )


_GenEquipMngSwTimerTimerAbort_Type.__name__ = "Integer32"
_GenEquipMngSwTimerTimerAbort_Object = MibTableColumn
genEquipMngSwTimerTimerAbort = _GenEquipMngSwTimerTimerAbort_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 2, 1, 4),
    _GenEquipMngSwTimerTimerAbort_Type()
)
genEquipMngSwTimerTimerAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwTimerTimerAbort.setStatus("mandatory")
_GenEquipMngSwFTPTimer_Type = Integer32
_GenEquipMngSwFTPTimer_Object = MibScalar
genEquipMngSwFTPTimer = _GenEquipMngSwFTPTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 13, 10),
    _GenEquipMngSwFTPTimer_Type()
)
genEquipMngSwFTPTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwFTPTimer.setStatus("mandatory")


class _GenEquipMngSwInstallationTimer_Type(Integer32):
    """Custom type genEquipMngSwInstallationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_GenEquipMngSwInstallationTimer_Type.__name__ = "Integer32"
_GenEquipMngSwInstallationTimer_Object = MibScalar
genEquipMngSwInstallationTimer = _GenEquipMngSwInstallationTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 14),
    _GenEquipMngSwInstallationTimer_Type()
)
genEquipMngSwInstallationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwInstallationTimer.setStatus("mandatory")


class _GenEquipMngSwTimeToInstall_Type(Integer32):
    """Custom type genEquipMngSwTimeToInstall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_GenEquipMngSwTimeToInstall_Type.__name__ = "Integer32"
_GenEquipMngSwTimeToInstall_Object = MibScalar
genEquipMngSwTimeToInstall = _GenEquipMngSwTimeToInstall_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 15),
    _GenEquipMngSwTimeToInstall_Type()
)
genEquipMngSwTimeToInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwTimeToInstall.setStatus("mandatory")
_GenEquipMngSwUpgradeCommonRfuVersion_Type = DisplayString
_GenEquipMngSwUpgradeCommonRfuVersion_Object = MibScalar
genEquipMngSwUpgradeCommonRfuVersion = _GenEquipMngSwUpgradeCommonRfuVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 16),
    _GenEquipMngSwUpgradeCommonRfuVersion_Type()
)
genEquipMngSwUpgradeCommonRfuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwUpgradeCommonRfuVersion.setStatus("mandatory")
_GenEquipMngSwDowngradeCommonRfuVersion_Type = DisplayString
_GenEquipMngSwDowngradeCommonRfuVersion_Object = MibScalar
genEquipMngSwDowngradeCommonRfuVersion = _GenEquipMngSwDowngradeCommonRfuVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 17),
    _GenEquipMngSwDowngradeCommonRfuVersion_Type()
)
genEquipMngSwDowngradeCommonRfuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwDowngradeCommonRfuVersion.setStatus("mandatory")
_GenEquipMngSwFileTransferTable_Object = MibTable
genEquipMngSwFileTransferTable = _GenEquipMngSwFileTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18)
)
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferTable.setStatus("mandatory")
_GenEquipMngSwFileTransferEntry_Object = MibTableRow
genEquipMngSwFileTransferEntry = _GenEquipMngSwFileTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18, 1)
)
genEquipMngSwFileTransferEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngSwFileTransferIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferEntry.setStatus("mandatory")
_GenEquipMngSwFileTransferIndex_Type = Integer32
_GenEquipMngSwFileTransferIndex_Object = MibTableColumn
genEquipMngSwFileTransferIndex = _GenEquipMngSwFileTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18, 1, 1),
    _GenEquipMngSwFileTransferIndex_Type()
)
genEquipMngSwFileTransferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferIndex.setStatus("mandatory")
_GenEquipMngSwFileTransferProtocol_Type = FtpProtocolType
_GenEquipMngSwFileTransferProtocol_Object = MibTableColumn
genEquipMngSwFileTransferProtocol = _GenEquipMngSwFileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18, 1, 2),
    _GenEquipMngSwFileTransferProtocol_Type()
)
genEquipMngSwFileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferProtocol.setStatus("mandatory")
_GenEquipMngSwFileTransferUserName_Type = DisplayString
_GenEquipMngSwFileTransferUserName_Object = MibTableColumn
genEquipMngSwFileTransferUserName = _GenEquipMngSwFileTransferUserName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18, 1, 3),
    _GenEquipMngSwFileTransferUserName_Type()
)
genEquipMngSwFileTransferUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferUserName.setStatus("mandatory")
_GenEquipMngSwFileTransferPassword_Type = DisplayString
_GenEquipMngSwFileTransferPassword_Object = MibTableColumn
genEquipMngSwFileTransferPassword = _GenEquipMngSwFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18, 1, 4),
    _GenEquipMngSwFileTransferPassword_Type()
)
genEquipMngSwFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferPassword.setStatus("mandatory")
_GenEquipMngSwFileTransferAddress_Type = IpAddress
_GenEquipMngSwFileTransferAddress_Object = MibTableColumn
genEquipMngSwFileTransferAddress = _GenEquipMngSwFileTransferAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18, 1, 5),
    _GenEquipMngSwFileTransferAddress_Type()
)
genEquipMngSwFileTransferAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferAddress.setStatus("mandatory")
_GenEquipMngSwFileTransferPath_Type = DisplayString
_GenEquipMngSwFileTransferPath_Object = MibTableColumn
genEquipMngSwFileTransferPath = _GenEquipMngSwFileTransferPath_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18, 1, 6),
    _GenEquipMngSwFileTransferPath_Type()
)
genEquipMngSwFileTransferPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferPath.setStatus("mandatory")


class _GenEquipMngSwFileTransferIpv6Address_Type(OctetString):
    """Custom type genEquipMngSwFileTransferIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipMngSwFileTransferIpv6Address_Type.__name__ = "OctetString"
_GenEquipMngSwFileTransferIpv6Address_Object = MibTableColumn
genEquipMngSwFileTransferIpv6Address = _GenEquipMngSwFileTransferIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 18, 1, 7),
    _GenEquipMngSwFileTransferIpv6Address_Type()
)
genEquipMngSwFileTransferIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferIpv6Address.setStatus("mandatory")
_GenEquipMngSwFileTransferStatusTable_Object = MibTable
genEquipMngSwFileTransferStatusTable = _GenEquipMngSwFileTransferStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 19)
)
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferStatusTable.setStatus("mandatory")
_GenEquipMngSwFileTransferStatusEntry_Object = MibTableRow
genEquipMngSwFileTransferStatusEntry = _GenEquipMngSwFileTransferStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 19, 1)
)
genEquipMngSwFileTransferStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngSwFileTransferStatusIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferStatusEntry.setStatus("mandatory")
_GenEquipMngSwFileTransferStatusIndex_Type = Integer32
_GenEquipMngSwFileTransferStatusIndex_Object = MibTableColumn
genEquipMngSwFileTransferStatusIndex = _GenEquipMngSwFileTransferStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 19, 1, 1),
    _GenEquipMngSwFileTransferStatusIndex_Type()
)
genEquipMngSwFileTransferStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferStatusIndex.setStatus("mandatory")


class _GenEquipMngSwFileTransferStatusResult_Type(Integer32):
    """Custom type genEquipMngSwFileTransferStatusResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("allComponentsExist", 6),
          ("componentUnsupportedByHw", 9),
          ("corruptSwFiles", 10),
          ("downloadCancelled", 12),
          ("downloadFailure", 5),
          ("downloadInProgress", 3),
          ("downloadStarted", 1),
          ("downloadSuccess", 4),
          ("incompleteFileSet", 8),
          ("missingDependencies", 11),
          ("ready", 0),
          ("verifyingDownloadFiles", 2),
          ("versionIncompatibleWithSystem", 7))
    )


_GenEquipMngSwFileTransferStatusResult_Type.__name__ = "Integer32"
_GenEquipMngSwFileTransferStatusResult_Object = MibTableColumn
genEquipMngSwFileTransferStatusResult = _GenEquipMngSwFileTransferStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 19, 1, 2),
    _GenEquipMngSwFileTransferStatusResult_Type()
)
genEquipMngSwFileTransferStatusResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferStatusResult.setStatus("mandatory")


class _GenEquipMngSwFileTransferPercentageDone_Type(Integer32):
    """Custom type genEquipMngSwFileTransferPercentageDone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenEquipMngSwFileTransferPercentageDone_Type.__name__ = "Integer32"
_GenEquipMngSwFileTransferPercentageDone_Object = MibTableColumn
genEquipMngSwFileTransferPercentageDone = _GenEquipMngSwFileTransferPercentageDone_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 19, 1, 3),
    _GenEquipMngSwFileTransferPercentageDone_Type()
)
genEquipMngSwFileTransferPercentageDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferPercentageDone.setStatus("mandatory")


class _GenEquipMngSwFileTransferPercentageDoneStandBy_Type(Integer32):
    """Custom type genEquipMngSwFileTransferPercentageDoneStandBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenEquipMngSwFileTransferPercentageDoneStandBy_Type.__name__ = "Integer32"
_GenEquipMngSwFileTransferPercentageDoneStandBy_Object = MibTableColumn
genEquipMngSwFileTransferPercentageDoneStandBy = _GenEquipMngSwFileTransferPercentageDoneStandBy_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 19, 1, 4),
    _GenEquipMngSwFileTransferPercentageDoneStandBy_Type()
)
genEquipMngSwFileTransferPercentageDoneStandBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferPercentageDoneStandBy.setStatus("mandatory")


class _GenEquipMngSwFileTransferStatusResultStandBy_Type(Integer32):
    """Custom type genEquipMngSwFileTransferStatusResultStandBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download-started", 1),
          ("ready", 0),
          ("verifying-download-files", 2))
    )


_GenEquipMngSwFileTransferStatusResultStandBy_Type.__name__ = "Integer32"
_GenEquipMngSwFileTransferStatusResultStandBy_Object = MibTableColumn
genEquipMngSwFileTransferStatusResultStandBy = _GenEquipMngSwFileTransferStatusResultStandBy_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 19, 1, 5),
    _GenEquipMngSwFileTransferStatusResultStandBy_Type()
)
genEquipMngSwFileTransferStatusResultStandBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwFileTransferStatusResultStandBy.setStatus("mandatory")
_GenEquipMngSwInstallStatusTable_Object = MibTable
genEquipMngSwInstallStatusTable = _GenEquipMngSwInstallStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 20)
)
if mibBuilder.loadTexts:
    genEquipMngSwInstallStatusTable.setStatus("mandatory")
_GenEquipMngSwInstallStatusEntry_Object = MibTableRow
genEquipMngSwInstallStatusEntry = _GenEquipMngSwInstallStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 20, 1)
)
genEquipMngSwInstallStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngSwInstallStatusIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngSwInstallStatusEntry.setStatus("mandatory")
_GenEquipMngSwInstallStatusIndex_Type = Integer32
_GenEquipMngSwInstallStatusIndex_Object = MibTableColumn
genEquipMngSwInstallStatusIndex = _GenEquipMngSwInstallStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 20, 1, 1),
    _GenEquipMngSwInstallStatusIndex_Type()
)
genEquipMngSwInstallStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwInstallStatusIndex.setStatus("mandatory")


class _GenEquipMngSwInstallStatusResult_Type(Integer32):
    """Custom type genEquipMngSwInstallStatusResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("incompleteSwVersion", 7),
          ("installationCancelled", 8),
          ("installationFailure", 6),
          ("installationInProgress", 3),
          ("installationPartialSuccess", 5),
          ("installationStarted", 1),
          ("installationSuccess", 4),
          ("ready", 0),
          ("verifyingInstallationFiles", 2))
    )


_GenEquipMngSwInstallStatusResult_Type.__name__ = "Integer32"
_GenEquipMngSwInstallStatusResult_Object = MibTableColumn
genEquipMngSwInstallStatusResult = _GenEquipMngSwInstallStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 20, 1, 2),
    _GenEquipMngSwInstallStatusResult_Type()
)
genEquipMngSwInstallStatusResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwInstallStatusResult.setStatus("mandatory")


class _GenEquipMngSwInstallPercentageDone_Type(Integer32):
    """Custom type genEquipMngSwInstallPercentageDone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenEquipMngSwInstallPercentageDone_Type.__name__ = "Integer32"
_GenEquipMngSwInstallPercentageDone_Object = MibTableColumn
genEquipMngSwInstallPercentageDone = _GenEquipMngSwInstallPercentageDone_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 20, 1, 3),
    _GenEquipMngSwInstallPercentageDone_Type()
)
genEquipMngSwInstallPercentageDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwInstallPercentageDone.setStatus("mandatory")


class _GenEquipMngSwInstallStatusResultStandBy_Type(Integer32):
    """Custom type genEquipMngSwInstallStatusResultStandBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("incompleteSwVersion", 7),
          ("installationCancelled", 8),
          ("installationFailure", 6),
          ("installationInProgress", 3),
          ("installationPartialSuccess", 5),
          ("installationStarted", 1),
          ("installationSuccess", 4),
          ("ready", 0),
          ("verifyingInstallationFiles", 2))
    )


_GenEquipMngSwInstallStatusResultStandBy_Type.__name__ = "Integer32"
_GenEquipMngSwInstallStatusResultStandBy_Object = MibTableColumn
genEquipMngSwInstallStatusResultStandBy = _GenEquipMngSwInstallStatusResultStandBy_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 20, 1, 4),
    _GenEquipMngSwInstallStatusResultStandBy_Type()
)
genEquipMngSwInstallStatusResultStandBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwInstallStatusResultStandBy.setStatus("mandatory")


class _GenEquipMngSwInstallPercentageDoneStandBy_Type(Integer32):
    """Custom type genEquipMngSwInstallPercentageDoneStandBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenEquipMngSwInstallPercentageDoneStandBy_Type.__name__ = "Integer32"
_GenEquipMngSwInstallPercentageDoneStandBy_Object = MibTableColumn
genEquipMngSwInstallPercentageDoneStandBy = _GenEquipMngSwInstallPercentageDoneStandBy_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 20, 1, 5),
    _GenEquipMngSwInstallPercentageDoneStandBy_Type()
)
genEquipMngSwInstallPercentageDoneStandBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwInstallPercentageDoneStandBy.setStatus("mandatory")
_GenEquipMngSwOperationTable_Object = MibTable
genEquipMngSwOperationTable = _GenEquipMngSwOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 21)
)
if mibBuilder.loadTexts:
    genEquipMngSwOperationTable.setStatus("mandatory")
_GenEquipMngSwOperationEntry_Object = MibTableRow
genEquipMngSwOperationEntry = _GenEquipMngSwOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 21, 1)
)
genEquipMngSwOperationEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngSwOperationIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngSwOperationEntry.setStatus("mandatory")
_GenEquipMngSwOperationIndex_Type = Integer32
_GenEquipMngSwOperationIndex_Object = MibTableColumn
genEquipMngSwOperationIndex = _GenEquipMngSwOperationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 21, 1, 1),
    _GenEquipMngSwOperationIndex_Type()
)
genEquipMngSwOperationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwOperationIndex.setStatus("mandatory")


class _GenEquipMngSwOperationOperation_Type(Integer32):
    """Custom type genEquipMngSwOperationOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("abortTimer", 5),
          ("download", 1),
          ("install", 2),
          ("noAction", 0),
          ("swapBootSection", 4),
          ("updateBackup", 3))
    )


_GenEquipMngSwOperationOperation_Type.__name__ = "Integer32"
_GenEquipMngSwOperationOperation_Object = MibTableColumn
genEquipMngSwOperationOperation = _GenEquipMngSwOperationOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 21, 1, 2),
    _GenEquipMngSwOperationOperation_Type()
)
genEquipMngSwOperationOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwOperationOperation.setStatus("mandatory")
_GenEquipMngSwOperationTimedInstallation_Type = NoYes
_GenEquipMngSwOperationTimedInstallation_Object = MibTableColumn
genEquipMngSwOperationTimedInstallation = _GenEquipMngSwOperationTimedInstallation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 21, 1, 3),
    _GenEquipMngSwOperationTimedInstallation_Type()
)
genEquipMngSwOperationTimedInstallation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwOperationTimedInstallation.setStatus("mandatory")
_GenEquipMngSwSlotRunningVersionTable_Object = MibTable
genEquipMngSwSlotRunningVersionTable = _GenEquipMngSwSlotRunningVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 22)
)
if mibBuilder.loadTexts:
    genEquipMngSwSlotRunningVersionTable.setStatus("mandatory")
_GenEquipMngSwSlotRunningVersionEntry_Object = MibTableRow
genEquipMngSwSlotRunningVersionEntry = _GenEquipMngSwSlotRunningVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 22, 1)
)
genEquipMngSwSlotRunningVersionEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngSwSlotRunningVersionSlotId"),
)
if mibBuilder.loadTexts:
    genEquipMngSwSlotRunningVersionEntry.setStatus("mandatory")


class _GenEquipMngSwSlotRunningVersionSlotId_Type(Integer32):
    """Custom type genEquipMngSwSlotRunningVersionSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_GenEquipMngSwSlotRunningVersionSlotId_Type.__name__ = "Integer32"
_GenEquipMngSwSlotRunningVersionSlotId_Object = MibTableColumn
genEquipMngSwSlotRunningVersionSlotId = _GenEquipMngSwSlotRunningVersionSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 22, 1, 1),
    _GenEquipMngSwSlotRunningVersionSlotId_Type()
)
genEquipMngSwSlotRunningVersionSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwSlotRunningVersionSlotId.setStatus("mandatory")
_GenEquipMngSwSlotRunningVersionCardType_Type = InventoryCardType
_GenEquipMngSwSlotRunningVersionCardType_Object = MibTableColumn
genEquipMngSwSlotRunningVersionCardType = _GenEquipMngSwSlotRunningVersionCardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 22, 1, 2),
    _GenEquipMngSwSlotRunningVersionCardType_Type()
)
genEquipMngSwSlotRunningVersionCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwSlotRunningVersionCardType.setStatus("mandatory")
_GenEquipMngSwSlotRunningVersionComponent_Type = DisplayString
_GenEquipMngSwSlotRunningVersionComponent_Object = MibTableColumn
genEquipMngSwSlotRunningVersionComponent = _GenEquipMngSwSlotRunningVersionComponent_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 22, 1, 3),
    _GenEquipMngSwSlotRunningVersionComponent_Type()
)
genEquipMngSwSlotRunningVersionComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwSlotRunningVersionComponent.setStatus("mandatory")
_GenEquipMngSwSlotRunningVersionActualVersion_Type = DisplayString
_GenEquipMngSwSlotRunningVersionActualVersion_Object = MibTableColumn
genEquipMngSwSlotRunningVersionActualVersion = _GenEquipMngSwSlotRunningVersionActualVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 22, 1, 4),
    _GenEquipMngSwSlotRunningVersionActualVersion_Type()
)
genEquipMngSwSlotRunningVersionActualVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwSlotRunningVersionActualVersion.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByTable_Object = MibTable
genEquipMngSwIDUVersionsStandByTable = _GenEquipMngSwIDUVersionsStandByTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23)
)
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByTable.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByEntry_Object = MibTableRow
genEquipMngSwIDUVersionsStandByEntry = _GenEquipMngSwIDUVersionsStandByEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23, 1)
)
genEquipMngSwIDUVersionsStandByEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngSwIDUVersionsStandByIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByEntry.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByIndex_Type = Integer32
_GenEquipMngSwIDUVersionsStandByIndex_Object = MibTableColumn
genEquipMngSwIDUVersionsStandByIndex = _GenEquipMngSwIDUVersionsStandByIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23, 1, 1),
    _GenEquipMngSwIDUVersionsStandByIndex_Type()
)
genEquipMngSwIDUVersionsStandByIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByIndex.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByPackageName_Type = DisplayString
_GenEquipMngSwIDUVersionsStandByPackageName_Object = MibTableColumn
genEquipMngSwIDUVersionsStandByPackageName = _GenEquipMngSwIDUVersionsStandByPackageName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23, 1, 2),
    _GenEquipMngSwIDUVersionsStandByPackageName_Type()
)
genEquipMngSwIDUVersionsStandByPackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByPackageName.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByRunningVersion_Type = DisplayString
_GenEquipMngSwIDUVersionsStandByRunningVersion_Object = MibTableColumn
genEquipMngSwIDUVersionsStandByRunningVersion = _GenEquipMngSwIDUVersionsStandByRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23, 1, 3),
    _GenEquipMngSwIDUVersionsStandByRunningVersion_Type()
)
genEquipMngSwIDUVersionsStandByRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByRunningVersion.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByInstalledVersion_Type = DisplayString
_GenEquipMngSwIDUVersionsStandByInstalledVersion_Object = MibTableColumn
genEquipMngSwIDUVersionsStandByInstalledVersion = _GenEquipMngSwIDUVersionsStandByInstalledVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23, 1, 4),
    _GenEquipMngSwIDUVersionsStandByInstalledVersion_Type()
)
genEquipMngSwIDUVersionsStandByInstalledVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByInstalledVersion.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByTargetDevice_Type = InventoryCardType
_GenEquipMngSwIDUVersionsStandByTargetDevice_Object = MibTableColumn
genEquipMngSwIDUVersionsStandByTargetDevice = _GenEquipMngSwIDUVersionsStandByTargetDevice_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23, 1, 5),
    _GenEquipMngSwIDUVersionsStandByTargetDevice_Type()
)
genEquipMngSwIDUVersionsStandByTargetDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByTargetDevice.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByDownloadedPackage_Type = DisplayString
_GenEquipMngSwIDUVersionsStandByDownloadedPackage_Object = MibTableColumn
genEquipMngSwIDUVersionsStandByDownloadedPackage = _GenEquipMngSwIDUVersionsStandByDownloadedPackage_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23, 1, 6),
    _GenEquipMngSwIDUVersionsStandByDownloadedPackage_Type()
)
genEquipMngSwIDUVersionsStandByDownloadedPackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByDownloadedPackage.setStatus("mandatory")
_GenEquipMngSwIDUVersionsStandByResetType_Type = VmResetType
_GenEquipMngSwIDUVersionsStandByResetType_Object = MibTableColumn
genEquipMngSwIDUVersionsStandByResetType = _GenEquipMngSwIDUVersionsStandByResetType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 23, 1, 7),
    _GenEquipMngSwIDUVersionsStandByResetType_Type()
)
genEquipMngSwIDUVersionsStandByResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngSwIDUVersionsStandByResetType.setStatus("mandatory")
_GenEquipMngSwWatchdogAdmin_Type = EnableDisable
_GenEquipMngSwWatchdogAdmin_Object = MibScalar
genEquipMngSwWatchdogAdmin = _GenEquipMngSwWatchdogAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 1, 35),
    _GenEquipMngSwWatchdogAdmin_Type()
)
genEquipMngSwWatchdogAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngSwWatchdogAdmin.setStatus("mandatory")
_GenEquipMngCfg_ObjectIdentity = ObjectIdentity
genEquipMngCfg = _GenEquipMngCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2)
)
_GenEquipMngCfgBackupStatus_Type = ProgressStatus
_GenEquipMngCfgBackupStatus_Object = MibScalar
genEquipMngCfgBackupStatus = _GenEquipMngCfgBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 1),
    _GenEquipMngCfgBackupStatus_Type()
)
genEquipMngCfgBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgBackupStatus.setStatus("mandatory")
_GenEquipMngCfgRestoreStatus_Type = ProgressStatus
_GenEquipMngCfgRestoreStatus_Object = MibScalar
genEquipMngCfgRestoreStatus = _GenEquipMngCfgRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 2),
    _GenEquipMngCfgRestoreStatus_Type()
)
genEquipMngCfgRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgRestoreStatus.setStatus("mandatory")
_GenEquipMngCfgUploadStatus_Type = ProgressStatus
_GenEquipMngCfgUploadStatus_Object = MibScalar
genEquipMngCfgUploadStatus = _GenEquipMngCfgUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 3),
    _GenEquipMngCfgUploadStatus_Type()
)
genEquipMngCfgUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgUploadStatus.setStatus("mandatory")
_GenEquipMngCfgDownloadStatus_Type = ProgressStatus
_GenEquipMngCfgDownloadStatus_Object = MibScalar
genEquipMngCfgDownloadStatus = _GenEquipMngCfgDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 4),
    _GenEquipMngCfgDownloadStatus_Type()
)
genEquipMngCfgDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgDownloadStatus.setStatus("mandatory")


class _GenEquipMngCfgCommand_Type(Integer32):
    """Custom type genEquipMngCfgCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("download", 4),
          ("no-operation", 0),
          ("restore", 2),
          ("upload", 3))
    )


_GenEquipMngCfgCommand_Type.__name__ = "Integer32"
_GenEquipMngCfgCommand_Object = MibScalar
genEquipMngCfgCommand = _GenEquipMngCfgCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 5),
    _GenEquipMngCfgCommand_Type()
)
genEquipMngCfgCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgCommand.setStatus("mandatory")
_GenEquipMngCfgEthernetSwitchStoreConfiguration_Type = OffOn
_GenEquipMngCfgEthernetSwitchStoreConfiguration_Object = MibScalar
genEquipMngCfgEthernetSwitchStoreConfiguration = _GenEquipMngCfgEthernetSwitchStoreConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 6),
    _GenEquipMngCfgEthernetSwitchStoreConfiguration_Type()
)
genEquipMngCfgEthernetSwitchStoreConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgEthernetSwitchStoreConfiguration.setStatus("mandatory")
_GenEquipMngCfgSetToDefaultKeepIp_Type = OffOn
_GenEquipMngCfgSetToDefaultKeepIp_Object = MibScalar
genEquipMngCfgSetToDefaultKeepIp = _GenEquipMngCfgSetToDefaultKeepIp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 7),
    _GenEquipMngCfgSetToDefaultKeepIp_Type()
)
genEquipMngCfgSetToDefaultKeepIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgSetToDefaultKeepIp.setStatus("mandatory")
_GenEquipMngCfgCliScriptFileName_Type = DisplayString
_GenEquipMngCfgCliScriptFileName_Object = MibScalar
genEquipMngCfgCliScriptFileName = _GenEquipMngCfgCliScriptFileName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 8),
    _GenEquipMngCfgCliScriptFileName_Type()
)
genEquipMngCfgCliScriptFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgCliScriptFileName.setStatus("mandatory")
_GenEquipMngCfgGeneric_ObjectIdentity = ObjectIdentity
genEquipMngCfgGeneric = _GenEquipMngCfgGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 10)
)
_GenEquipMngCfgBackupProgress_Type = Integer32
_GenEquipMngCfgBackupProgress_Object = MibScalar
genEquipMngCfgBackupProgress = _GenEquipMngCfgBackupProgress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 10, 1),
    _GenEquipMngCfgBackupProgress_Type()
)
genEquipMngCfgBackupProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgBackupProgress.setStatus("mandatory")
_GenEquipMngCfgTimeToInstallation_Type = Integer32
_GenEquipMngCfgTimeToInstallation_Object = MibScalar
genEquipMngCfgTimeToInstallation = _GenEquipMngCfgTimeToInstallation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 10, 2),
    _GenEquipMngCfgTimeToInstallation_Type()
)
genEquipMngCfgTimeToInstallation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgTimeToInstallation.setStatus("mandatory")
_GenEquipMngCfgFileTransferTable_Object = MibTable
genEquipMngCfgFileTransferTable = _GenEquipMngCfgFileTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11)
)
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferTable.setStatus("mandatory")
_GenEquipMngCfgFileTransferEntry_Object = MibTableRow
genEquipMngCfgFileTransferEntry = _GenEquipMngCfgFileTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1)
)
genEquipMngCfgFileTransferEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngCfgFileTransferIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferEntry.setStatus("mandatory")
_GenEquipMngCfgFileTransferIndex_Type = Integer32
_GenEquipMngCfgFileTransferIndex_Object = MibTableColumn
genEquipMngCfgFileTransferIndex = _GenEquipMngCfgFileTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1, 1),
    _GenEquipMngCfgFileTransferIndex_Type()
)
genEquipMngCfgFileTransferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferIndex.setStatus("mandatory")
_GenEquipMngCfgFileTransferProtocol_Type = FtpProtocolType
_GenEquipMngCfgFileTransferProtocol_Object = MibTableColumn
genEquipMngCfgFileTransferProtocol = _GenEquipMngCfgFileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1, 2),
    _GenEquipMngCfgFileTransferProtocol_Type()
)
genEquipMngCfgFileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferProtocol.setStatus("mandatory")
_GenEquipMngCfgFileTransferUserName_Type = DisplayString
_GenEquipMngCfgFileTransferUserName_Object = MibTableColumn
genEquipMngCfgFileTransferUserName = _GenEquipMngCfgFileTransferUserName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1, 3),
    _GenEquipMngCfgFileTransferUserName_Type()
)
genEquipMngCfgFileTransferUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferUserName.setStatus("mandatory")
_GenEquipMngCfgFileTransferPassword_Type = DisplayString
_GenEquipMngCfgFileTransferPassword_Object = MibTableColumn
genEquipMngCfgFileTransferPassword = _GenEquipMngCfgFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1, 4),
    _GenEquipMngCfgFileTransferPassword_Type()
)
genEquipMngCfgFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferPassword.setStatus("mandatory")
_GenEquipMngCfgFileTransferAddress_Type = IpAddress
_GenEquipMngCfgFileTransferAddress_Object = MibTableColumn
genEquipMngCfgFileTransferAddress = _GenEquipMngCfgFileTransferAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1, 5),
    _GenEquipMngCfgFileTransferAddress_Type()
)
genEquipMngCfgFileTransferAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferAddress.setStatus("mandatory")
_GenEquipMngCfgFileTransferPath_Type = DisplayString
_GenEquipMngCfgFileTransferPath_Object = MibTableColumn
genEquipMngCfgFileTransferPath = _GenEquipMngCfgFileTransferPath_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1, 6),
    _GenEquipMngCfgFileTransferPath_Type()
)
genEquipMngCfgFileTransferPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferPath.setStatus("mandatory")
_GenEquipMngCfgFileTransferFileName_Type = DisplayString
_GenEquipMngCfgFileTransferFileName_Object = MibTableColumn
genEquipMngCfgFileTransferFileName = _GenEquipMngCfgFileTransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1, 7),
    _GenEquipMngCfgFileTransferFileName_Type()
)
genEquipMngCfgFileTransferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferFileName.setStatus("mandatory")


class _GenEquipMngCfgFileTransferIpv6Address_Type(OctetString):
    """Custom type genEquipMngCfgFileTransferIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipMngCfgFileTransferIpv6Address_Type.__name__ = "OctetString"
_GenEquipMngCfgFileTransferIpv6Address_Object = MibTableColumn
genEquipMngCfgFileTransferIpv6Address = _GenEquipMngCfgFileTransferIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 11, 1, 8),
    _GenEquipMngCfgFileTransferIpv6Address_Type()
)
genEquipMngCfgFileTransferIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferIpv6Address.setStatus("mandatory")
_GenEquipMngCfgFileTransferStatusTable_Object = MibTable
genEquipMngCfgFileTransferStatusTable = _GenEquipMngCfgFileTransferStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 12)
)
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferStatusTable.setStatus("mandatory")
_GenEquipMngCfgFileTransferStatusEntry_Object = MibTableRow
genEquipMngCfgFileTransferStatusEntry = _GenEquipMngCfgFileTransferStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 12, 1)
)
genEquipMngCfgFileTransferStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngCfgFileTransferStatusIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferStatusEntry.setStatus("mandatory")
_GenEquipMngCfgFileTransferStatusIndex_Type = Integer32
_GenEquipMngCfgFileTransferStatusIndex_Object = MibTableColumn
genEquipMngCfgFileTransferStatusIndex = _GenEquipMngCfgFileTransferStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 12, 1, 1),
    _GenEquipMngCfgFileTransferStatusIndex_Type()
)
genEquipMngCfgFileTransferStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferStatusIndex.setStatus("mandatory")
_GenEquipMngCfgFileTransferStatusPercentageDone_Type = Integer32
_GenEquipMngCfgFileTransferStatusPercentageDone_Object = MibTableColumn
genEquipMngCfgFileTransferStatusPercentageDone = _GenEquipMngCfgFileTransferStatusPercentageDone_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 12, 1, 2),
    _GenEquipMngCfgFileTransferStatusPercentageDone_Type()
)
genEquipMngCfgFileTransferStatusPercentageDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferStatusPercentageDone.setStatus("mandatory")
_GenEquipMngCfgFileTransferStatusResult_Type = FileTransferStatus
_GenEquipMngCfgFileTransferStatusResult_Object = MibTableColumn
genEquipMngCfgFileTransferStatusResult = _GenEquipMngCfgFileTransferStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 12, 1, 3),
    _GenEquipMngCfgFileTransferStatusResult_Type()
)
genEquipMngCfgFileTransferStatusResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferStatusResult.setStatus("mandatory")
_GenEquipMngCfgOperationTable_Object = MibTable
genEquipMngCfgOperationTable = _GenEquipMngCfgOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 13)
)
if mibBuilder.loadTexts:
    genEquipMngCfgOperationTable.setStatus("mandatory")
_GenEquipMngCfgOperationEntry_Object = MibTableRow
genEquipMngCfgOperationEntry = _GenEquipMngCfgOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 13, 1)
)
genEquipMngCfgOperationEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngCfgOperationIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngCfgOperationEntry.setStatus("mandatory")
_GenEquipMngCfgOperationIndex_Type = Integer32
_GenEquipMngCfgOperationIndex_Object = MibTableColumn
genEquipMngCfgOperationIndex = _GenEquipMngCfgOperationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 13, 1, 1),
    _GenEquipMngCfgOperationIndex_Type()
)
genEquipMngCfgOperationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgOperationIndex.setStatus("mandatory")
_GenEquipMngCfgOperationOperation_Type = CfgOper
_GenEquipMngCfgOperationOperation_Object = MibTableColumn
genEquipMngCfgOperationOperation = _GenEquipMngCfgOperationOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 13, 1, 2),
    _GenEquipMngCfgOperationOperation_Type()
)
genEquipMngCfgOperationOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgOperationOperation.setStatus("mandatory")


class _GenEquipMngCfgOperationFileNumber_Type(Integer32):
    """Custom type genEquipMngCfgOperationFileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_GenEquipMngCfgOperationFileNumber_Type.__name__ = "Integer32"
_GenEquipMngCfgOperationFileNumber_Object = MibTableColumn
genEquipMngCfgOperationFileNumber = _GenEquipMngCfgOperationFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 13, 1, 3),
    _GenEquipMngCfgOperationFileNumber_Type()
)
genEquipMngCfgOperationFileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgOperationFileNumber.setStatus("mandatory")
_GenEquipMngCfgOperationTimedInstallation_Type = NoYes
_GenEquipMngCfgOperationTimedInstallation_Object = MibTableColumn
genEquipMngCfgOperationTimedInstallation = _GenEquipMngCfgOperationTimedInstallation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 13, 1, 4),
    _GenEquipMngCfgOperationTimedInstallation_Type()
)
genEquipMngCfgOperationTimedInstallation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgOperationTimedInstallation.setStatus("mandatory")
_GenEquipMngCfgOperationTimer_Type = DisplayString
_GenEquipMngCfgOperationTimer_Object = MibTableColumn
genEquipMngCfgOperationTimer = _GenEquipMngCfgOperationTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 13, 1, 5),
    _GenEquipMngCfgOperationTimer_Type()
)
genEquipMngCfgOperationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCfgOperationTimer.setStatus("mandatory")


class _GenEquipMngCfgOperationSlotNumber_Type(Integer32):
    """Custom type genEquipMngCfgOperationSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_GenEquipMngCfgOperationSlotNumber_Type.__name__ = "Integer32"
_GenEquipMngCfgOperationSlotNumber_Object = MibTableColumn
genEquipMngCfgOperationSlotNumber = _GenEquipMngCfgOperationSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 13, 1, 6),
    _GenEquipMngCfgOperationSlotNumber_Type()
)
genEquipMngCfgOperationSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgOperationSlotNumber.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesTable_Object = MibTable
genEquipMngCfgConfigurationFilesTable = _GenEquipMngCfgConfigurationFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14)
)
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesTable.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesEntry_Object = MibTableRow
genEquipMngCfgConfigurationFilesEntry = _GenEquipMngCfgConfigurationFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1)
)
genEquipMngCfgConfigurationFilesEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngCfgConfigurationFilesIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesEntry.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesIndex_Type = Integer32
_GenEquipMngCfgConfigurationFilesIndex_Object = MibTableColumn
genEquipMngCfgConfigurationFilesIndex = _GenEquipMngCfgConfigurationFilesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1, 1),
    _GenEquipMngCfgConfigurationFilesIndex_Type()
)
genEquipMngCfgConfigurationFilesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesIndex.setStatus("mandatory")


class _GenEquipMngCfgConfigurationFilesFileNumber_Type(Integer32):
    """Custom type genEquipMngCfgConfigurationFilesFileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_GenEquipMngCfgConfigurationFilesFileNumber_Type.__name__ = "Integer32"
_GenEquipMngCfgConfigurationFilesFileNumber_Object = MibTableColumn
genEquipMngCfgConfigurationFilesFileNumber = _GenEquipMngCfgConfigurationFilesFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1, 2),
    _GenEquipMngCfgConfigurationFilesFileNumber_Type()
)
genEquipMngCfgConfigurationFilesFileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesFileNumber.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesSystemType_Type = DisplayString
_GenEquipMngCfgConfigurationFilesSystemType_Object = MibTableColumn
genEquipMngCfgConfigurationFilesSystemType = _GenEquipMngCfgConfigurationFilesSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1, 3),
    _GenEquipMngCfgConfigurationFilesSystemType_Type()
)
genEquipMngCfgConfigurationFilesSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesSystemType.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesSWVersion_Type = DisplayString
_GenEquipMngCfgConfigurationFilesSWVersion_Object = MibTableColumn
genEquipMngCfgConfigurationFilesSWVersion = _GenEquipMngCfgConfigurationFilesSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1, 4),
    _GenEquipMngCfgConfigurationFilesSWVersion_Type()
)
genEquipMngCfgConfigurationFilesSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesSWVersion.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesTimeDate_Type = Integer32
_GenEquipMngCfgConfigurationFilesTimeDate_Object = MibTableColumn
genEquipMngCfgConfigurationFilesTimeDate = _GenEquipMngCfgConfigurationFilesTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1, 5),
    _GenEquipMngCfgConfigurationFilesTimeDate_Type()
)
genEquipMngCfgConfigurationFilesTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesTimeDate.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesSystemIP_Type = IpAddress
_GenEquipMngCfgConfigurationFilesSystemIP_Object = MibTableColumn
genEquipMngCfgConfigurationFilesSystemIP = _GenEquipMngCfgConfigurationFilesSystemIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1, 6),
    _GenEquipMngCfgConfigurationFilesSystemIP_Type()
)
genEquipMngCfgConfigurationFilesSystemIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesSystemIP.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesCardsConfigured_Type = DisplayString
_GenEquipMngCfgConfigurationFilesCardsConfigured_Object = MibTableColumn
genEquipMngCfgConfigurationFilesCardsConfigured = _GenEquipMngCfgConfigurationFilesCardsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1, 7),
    _GenEquipMngCfgConfigurationFilesCardsConfigured_Type()
)
genEquipMngCfgConfigurationFilesCardsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesCardsConfigured.setStatus("mandatory")
_GenEquipMngCfgConfigurationFilesSystemID_Type = DisplayString
_GenEquipMngCfgConfigurationFilesSystemID_Object = MibTableColumn
genEquipMngCfgConfigurationFilesSystemID = _GenEquipMngCfgConfigurationFilesSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 14, 1, 8),
    _GenEquipMngCfgConfigurationFilesSystemID_Type()
)
genEquipMngCfgConfigurationFilesSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgConfigurationFilesSystemID.setStatus("mandatory")
_GenEquipMngCfgFileRestoreStatus_Type = FileRestoreStatus
_GenEquipMngCfgFileRestoreStatus_Object = MibScalar
genEquipMngCfgFileRestoreStatus = _GenEquipMngCfgFileRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 20),
    _GenEquipMngCfgFileRestoreStatus_Type()
)
genEquipMngCfgFileRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgFileRestoreStatus.setStatus("mandatory")


class _GenEquipMngCfgFileTransferStatus_Type(Integer32):
    """Custom type genEquipMngCfgFileTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("all-components-exist", 6),
          ("component-unsupported-by-hw", 9),
          ("corrupt-sw-files", 10),
          ("download-cancelled", 12),
          ("download-failure", 5),
          ("download-in-progress", 3),
          ("download-started", 1),
          ("download-success", 4),
          ("incomplete-file-set", 8),
          ("missing-dependencies", 11),
          ("ready", 0),
          ("verifying-download-files", 2),
          ("version-incompatible-with-system", 7))
    )


_GenEquipMngCfgFileTransferStatus_Type.__name__ = "Integer32"
_GenEquipMngCfgFileTransferStatus_Object = MibScalar
genEquipMngCfgFileTransferStatus = _GenEquipMngCfgFileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 2, 21),
    _GenEquipMngCfgFileTransferStatus_Type()
)
genEquipMngCfgFileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCfgFileTransferStatus.setStatus("mandatory")
_GenEquipMngFileTransfer_ObjectIdentity = ObjectIdentity
genEquipMngFileTransfer = _GenEquipMngFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3)
)


class _GenEquipMngFileTransferFileTypeOper_Type(Integer32):
    """Custom type genEquipMngFileTransferFileTypeOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("download-certificate", 2),
          ("download-cli-script", 4),
          ("download-configuration", 1),
          ("download-warning-banner", 3),
          ("no-operation", 0),
          ("upload-configuration", 5),
          ("upload-csr-file", 6),
          ("upload-unit-info", 7))
    )


_GenEquipMngFileTransferFileTypeOper_Type.__name__ = "Integer32"
_GenEquipMngFileTransferFileTypeOper_Object = MibScalar
genEquipMngFileTransferFileTypeOper = _GenEquipMngFileTransferFileTypeOper_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3, 1),
    _GenEquipMngFileTransferFileTypeOper_Type()
)
genEquipMngFileTransferFileTypeOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngFileTransferFileTypeOper.setStatus("mandatory")
_GenEquipMngFileTransferDownloadConfigStatus_Type = ProgressStatus
_GenEquipMngFileTransferDownloadConfigStatus_Object = MibScalar
genEquipMngFileTransferDownloadConfigStatus = _GenEquipMngFileTransferDownloadConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3, 2),
    _GenEquipMngFileTransferDownloadConfigStatus_Type()
)
genEquipMngFileTransferDownloadConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngFileTransferDownloadConfigStatus.setStatus("mandatory")
_GenEquipMngFileTransferDownloadCertificateStatus_Type = ProgressStatus
_GenEquipMngFileTransferDownloadCertificateStatus_Object = MibScalar
genEquipMngFileTransferDownloadCertificateStatus = _GenEquipMngFileTransferDownloadCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3, 3),
    _GenEquipMngFileTransferDownloadCertificateStatus_Type()
)
genEquipMngFileTransferDownloadCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngFileTransferDownloadCertificateStatus.setStatus("mandatory")
_GenEquipMngFileTransferDownloadWarningBannerStatus_Type = ProgressStatus
_GenEquipMngFileTransferDownloadWarningBannerStatus_Object = MibScalar
genEquipMngFileTransferDownloadWarningBannerStatus = _GenEquipMngFileTransferDownloadWarningBannerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3, 4),
    _GenEquipMngFileTransferDownloadWarningBannerStatus_Type()
)
genEquipMngFileTransferDownloadWarningBannerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngFileTransferDownloadWarningBannerStatus.setStatus("mandatory")
_GenEquipMngFileTransferDownloadCliScriptStatus_Type = ProgressStatus
_GenEquipMngFileTransferDownloadCliScriptStatus_Object = MibScalar
genEquipMngFileTransferDownloadCliScriptStatus = _GenEquipMngFileTransferDownloadCliScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3, 5),
    _GenEquipMngFileTransferDownloadCliScriptStatus_Type()
)
genEquipMngFileTransferDownloadCliScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngFileTransferDownloadCliScriptStatus.setStatus("mandatory")
_GenEquipMngFileTransferUploadConfigStatus_Type = ProgressStatus
_GenEquipMngFileTransferUploadConfigStatus_Object = MibScalar
genEquipMngFileTransferUploadConfigStatus = _GenEquipMngFileTransferUploadConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3, 6),
    _GenEquipMngFileTransferUploadConfigStatus_Type()
)
genEquipMngFileTransferUploadConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngFileTransferUploadConfigStatus.setStatus("mandatory")
_GenEquipMngFileTransferUploadCSRStatus_Type = ProgressStatus
_GenEquipMngFileTransferUploadCSRStatus_Object = MibScalar
genEquipMngFileTransferUploadCSRStatus = _GenEquipMngFileTransferUploadCSRStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3, 7),
    _GenEquipMngFileTransferUploadCSRStatus_Type()
)
genEquipMngFileTransferUploadCSRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngFileTransferUploadCSRStatus.setStatus("mandatory")
_GenEquipMngFileTransferUploadUnitInfoStatus_Type = ProgressStatus
_GenEquipMngFileTransferUploadUnitInfoStatus_Object = MibScalar
genEquipMngFileTransferUploadUnitInfoStatus = _GenEquipMngFileTransferUploadUnitInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 3, 8),
    _GenEquipMngFileTransferUploadUnitInfoStatus_Type()
)
genEquipMngFileTransferUploadUnitInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngFileTransferUploadUnitInfoStatus.setStatus("mandatory")
_GenEquipMngUnitInfo_ObjectIdentity = ObjectIdentity
genEquipMngUnitInfo = _GenEquipMngUnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4)
)
_GenEquipMngUnitInfoGeneric_ObjectIdentity = ObjectIdentity
genEquipMngUnitInfoGeneric = _GenEquipMngUnitInfoGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 1)
)
_GenEquipMngUnitInfoOperation_Type = CfgUnitInfoOper
_GenEquipMngUnitInfoOperation_Object = MibScalar
genEquipMngUnitInfoOperation = _GenEquipMngUnitInfoOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 1, 1),
    _GenEquipMngUnitInfoOperation_Type()
)
genEquipMngUnitInfoOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoOperation.setStatus("mandatory")
_GenEquipMngUnitInfoProgress_Type = Integer32
_GenEquipMngUnitInfoProgress_Object = MibScalar
genEquipMngUnitInfoProgress = _GenEquipMngUnitInfoProgress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 1, 2),
    _GenEquipMngUnitInfoProgress_Type()
)
genEquipMngUnitInfoProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoProgress.setStatus("mandatory")
_GenEquipMngUnitInfoStatus_Type = ProgressStatus
_GenEquipMngUnitInfoStatus_Object = MibScalar
genEquipMngUnitInfoStatus = _GenEquipMngUnitInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 1, 3),
    _GenEquipMngUnitInfoStatus_Type()
)
genEquipMngUnitInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoStatus.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferTable_Object = MibTable
genEquipMngUnitInfoFileTransferTable = _GenEquipMngUnitInfoFileTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2)
)
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferTable.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferEntry_Object = MibTableRow
genEquipMngUnitInfoFileTransferEntry = _GenEquipMngUnitInfoFileTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1)
)
genEquipMngUnitInfoFileTransferEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngUnitInfoFileTransferIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferEntry.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferIndex_Type = Integer32
_GenEquipMngUnitInfoFileTransferIndex_Object = MibTableColumn
genEquipMngUnitInfoFileTransferIndex = _GenEquipMngUnitInfoFileTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1, 1),
    _GenEquipMngUnitInfoFileTransferIndex_Type()
)
genEquipMngUnitInfoFileTransferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferIndex.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferProtocol_Type = FtpProtocolType
_GenEquipMngUnitInfoFileTransferProtocol_Object = MibTableColumn
genEquipMngUnitInfoFileTransferProtocol = _GenEquipMngUnitInfoFileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1, 2),
    _GenEquipMngUnitInfoFileTransferProtocol_Type()
)
genEquipMngUnitInfoFileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferProtocol.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferUserName_Type = DisplayString
_GenEquipMngUnitInfoFileTransferUserName_Object = MibTableColumn
genEquipMngUnitInfoFileTransferUserName = _GenEquipMngUnitInfoFileTransferUserName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1, 3),
    _GenEquipMngUnitInfoFileTransferUserName_Type()
)
genEquipMngUnitInfoFileTransferUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferUserName.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferPassword_Type = DisplayString
_GenEquipMngUnitInfoFileTransferPassword_Object = MibTableColumn
genEquipMngUnitInfoFileTransferPassword = _GenEquipMngUnitInfoFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1, 4),
    _GenEquipMngUnitInfoFileTransferPassword_Type()
)
genEquipMngUnitInfoFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferPassword.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferAddress_Type = IpAddress
_GenEquipMngUnitInfoFileTransferAddress_Object = MibTableColumn
genEquipMngUnitInfoFileTransferAddress = _GenEquipMngUnitInfoFileTransferAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1, 5),
    _GenEquipMngUnitInfoFileTransferAddress_Type()
)
genEquipMngUnitInfoFileTransferAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferAddress.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferPath_Type = DisplayString
_GenEquipMngUnitInfoFileTransferPath_Object = MibTableColumn
genEquipMngUnitInfoFileTransferPath = _GenEquipMngUnitInfoFileTransferPath_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1, 6),
    _GenEquipMngUnitInfoFileTransferPath_Type()
)
genEquipMngUnitInfoFileTransferPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferPath.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferFileName_Type = DisplayString
_GenEquipMngUnitInfoFileTransferFileName_Object = MibTableColumn
genEquipMngUnitInfoFileTransferFileName = _GenEquipMngUnitInfoFileTransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1, 7),
    _GenEquipMngUnitInfoFileTransferFileName_Type()
)
genEquipMngUnitInfoFileTransferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferFileName.setStatus("mandatory")


class _GenEquipMngUnitInfoFileTransferIpv6Address_Type(OctetString):
    """Custom type genEquipMngUnitInfoFileTransferIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipMngUnitInfoFileTransferIpv6Address_Type.__name__ = "OctetString"
_GenEquipMngUnitInfoFileTransferIpv6Address_Object = MibTableColumn
genEquipMngUnitInfoFileTransferIpv6Address = _GenEquipMngUnitInfoFileTransferIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 2, 1, 8),
    _GenEquipMngUnitInfoFileTransferIpv6Address_Type()
)
genEquipMngUnitInfoFileTransferIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferIpv6Address.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferStatusTable_Object = MibTable
genEquipMngUnitInfoFileTransferStatusTable = _GenEquipMngUnitInfoFileTransferStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 3)
)
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferStatusTable.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferStatusEntry_Object = MibTableRow
genEquipMngUnitInfoFileTransferStatusEntry = _GenEquipMngUnitInfoFileTransferStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 3, 1)
)
genEquipMngUnitInfoFileTransferStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipMngUnitInfoFileTransferStatusIndex"),
)
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferStatusEntry.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferStatusIndex_Type = Integer32
_GenEquipMngUnitInfoFileTransferStatusIndex_Object = MibTableColumn
genEquipMngUnitInfoFileTransferStatusIndex = _GenEquipMngUnitInfoFileTransferStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 3, 1, 1),
    _GenEquipMngUnitInfoFileTransferStatusIndex_Type()
)
genEquipMngUnitInfoFileTransferStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferStatusIndex.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferStatusPercentageDone_Type = Integer32
_GenEquipMngUnitInfoFileTransferStatusPercentageDone_Object = MibTableColumn
genEquipMngUnitInfoFileTransferStatusPercentageDone = _GenEquipMngUnitInfoFileTransferStatusPercentageDone_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 3, 1, 2),
    _GenEquipMngUnitInfoFileTransferStatusPercentageDone_Type()
)
genEquipMngUnitInfoFileTransferStatusPercentageDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferStatusPercentageDone.setStatus("mandatory")
_GenEquipMngUnitInfoFileTransferStatusResult_Type = ProgressStatus
_GenEquipMngUnitInfoFileTransferStatusResult_Object = MibTableColumn
genEquipMngUnitInfoFileTransferStatusResult = _GenEquipMngUnitInfoFileTransferStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 4, 3, 1, 3),
    _GenEquipMngUnitInfoFileTransferStatusResult_Type()
)
genEquipMngUnitInfoFileTransferStatusResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngUnitInfoFileTransferStatusResult.setStatus("mandatory")
_GenEquipMngCli_ObjectIdentity = ObjectIdentity
genEquipMngCli = _GenEquipMngCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 5)
)


class _GenEquipMngCliScriptOperation_Type(Integer32):
    """Custom type genEquipMngCliScriptOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("execute", 4),
          ("import", 1),
          ("no-operation", 0),
          ("show", 3))
    )


_GenEquipMngCliScriptOperation_Type.__name__ = "Integer32"
_GenEquipMngCliScriptOperation_Object = MibScalar
genEquipMngCliScriptOperation = _GenEquipMngCliScriptOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 5, 1),
    _GenEquipMngCliScriptOperation_Type()
)
genEquipMngCliScriptOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipMngCliScriptOperation.setStatus("mandatory")


class _GenEquipMngCliScriptOperationStatus_Type(Integer32):
    """Custom type genEquipMngCliScriptOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("executing", 1),
          ("failed", 2),
          ("ready", 0),
          ("success", 3))
    )


_GenEquipMngCliScriptOperationStatus_Type.__name__ = "Integer32"
_GenEquipMngCliScriptOperationStatus_Object = MibScalar
genEquipMngCliScriptOperationStatus = _GenEquipMngCliScriptOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 4, 5, 2),
    _GenEquipMngCliScriptOperationStatus_Type()
)
genEquipMngCliScriptOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipMngCliScriptOperationStatus.setStatus("mandatory")
_GenEquipDiagAndMaintenance_ObjectIdentity = ObjectIdentity
genEquipDiagAndMaintenance = _GenEquipDiagAndMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 10)
)


class _GenEquipDiagAndMaintenanceRadioLoopbackTimeout_Type(Integer32):
    """Custom type genEquipDiagAndMaintenanceRadioLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GenEquipDiagAndMaintenanceRadioLoopbackTimeout_Type.__name__ = "Integer32"
_GenEquipDiagAndMaintenanceRadioLoopbackTimeout_Object = MibScalar
genEquipDiagAndMaintenanceRadioLoopbackTimeout = _GenEquipDiagAndMaintenanceRadioLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 10, 1),
    _GenEquipDiagAndMaintenanceRadioLoopbackTimeout_Type()
)
genEquipDiagAndMaintenanceRadioLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiagAndMaintenanceRadioLoopbackTimeout.setStatus("mandatory")


class _GenEquipDiagAndMaintenanceLineLoopbackTimeout_Type(Integer32):
    """Custom type genEquipDiagAndMaintenanceLineLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GenEquipDiagAndMaintenanceLineLoopbackTimeout_Type.__name__ = "Integer32"
_GenEquipDiagAndMaintenanceLineLoopbackTimeout_Object = MibScalar
genEquipDiagAndMaintenanceLineLoopbackTimeout = _GenEquipDiagAndMaintenanceLineLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 10, 2),
    _GenEquipDiagAndMaintenanceLineLoopbackTimeout_Type()
)
genEquipDiagAndMaintenanceLineLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiagAndMaintenanceLineLoopbackTimeout.setStatus("mandatory")


class _GenEquipDiagAndMaintenanceSDHLoopbackTimeout_Type(Integer32):
    """Custom type genEquipDiagAndMaintenanceSDHLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GenEquipDiagAndMaintenanceSDHLoopbackTimeout_Type.__name__ = "Integer32"
_GenEquipDiagAndMaintenanceSDHLoopbackTimeout_Object = MibScalar
genEquipDiagAndMaintenanceSDHLoopbackTimeout = _GenEquipDiagAndMaintenanceSDHLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 10, 3),
    _GenEquipDiagAndMaintenanceSDHLoopbackTimeout_Type()
)
genEquipDiagAndMaintenanceSDHLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipDiagAndMaintenanceSDHLoopbackTimeout.setStatus("mandatory")
_GenEquipSecurity_ObjectIdentity = ObjectIdentity
genEquipSecurity = _GenEquipSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11)
)
_GenEquipSecurityConfiguration_ObjectIdentity = ObjectIdentity
genEquipSecurityConfiguration = _GenEquipSecurityConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1)
)
_GenEquipSecurityCfgUploadPublicKeyStatus_Type = ProgressStatus
_GenEquipSecurityCfgUploadPublicKeyStatus_Object = MibScalar
genEquipSecurityCfgUploadPublicKeyStatus = _GenEquipSecurityCfgUploadPublicKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 1),
    _GenEquipSecurityCfgUploadPublicKeyStatus_Type()
)
genEquipSecurityCfgUploadPublicKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCfgUploadPublicKeyStatus.setStatus("mandatory")
_GenEquipSecurityCfgDownloadSecurityStatus_Type = ProgressStatus
_GenEquipSecurityCfgDownloadSecurityStatus_Object = MibScalar
genEquipSecurityCfgDownloadSecurityStatus = _GenEquipSecurityCfgDownloadSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 2),
    _GenEquipSecurityCfgDownloadSecurityStatus_Type()
)
genEquipSecurityCfgDownloadSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCfgDownloadSecurityStatus.setStatus("mandatory")
_GenEquipSecurityCfgSecurityFileName_Type = DisplayString
_GenEquipSecurityCfgSecurityFileName_Object = MibScalar
genEquipSecurityCfgSecurityFileName = _GenEquipSecurityCfgSecurityFileName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 3),
    _GenEquipSecurityCfgSecurityFileName_Type()
)
genEquipSecurityCfgSecurityFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgSecurityFileName.setStatus("mandatory")


class _GenEquipSecurityCfgSecurityFileType_Type(Integer32):
    """Custom type genEquipSecurityCfgSecurityFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("target-ca-certificate", 1),
          ("target-certificate", 0))
    )


_GenEquipSecurityCfgSecurityFileType_Type.__name__ = "Integer32"
_GenEquipSecurityCfgSecurityFileType_Object = MibScalar
genEquipSecurityCfgSecurityFileType = _GenEquipSecurityCfgSecurityFileType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 4),
    _GenEquipSecurityCfgSecurityFileType_Type()
)
genEquipSecurityCfgSecurityFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgSecurityFileType.setStatus("mandatory")


class _GenEquipSecurityCfgSecurityFileFormat_Type(Integer32):
    """Custom type genEquipSecurityCfgSecurityFileFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("der", 1),
          ("pem", 0))
    )


_GenEquipSecurityCfgSecurityFileFormat_Type.__name__ = "Integer32"
_GenEquipSecurityCfgSecurityFileFormat_Object = MibScalar
genEquipSecurityCfgSecurityFileFormat = _GenEquipSecurityCfgSecurityFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 5),
    _GenEquipSecurityCfgSecurityFileFormat_Type()
)
genEquipSecurityCfgSecurityFileFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgSecurityFileFormat.setStatus("mandatory")
_GenEquipSecurityCfgSecurityWebCertificateAdmin_Type = EnableDisable
_GenEquipSecurityCfgSecurityWebCertificateAdmin_Object = MibScalar
genEquipSecurityCfgSecurityWebCertificateAdmin = _GenEquipSecurityCfgSecurityWebCertificateAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 6),
    _GenEquipSecurityCfgSecurityWebCertificateAdmin_Type()
)
genEquipSecurityCfgSecurityWebCertificateAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgSecurityWebCertificateAdmin.setStatus("mandatory")


class _GenEquipSecurityCfgWebProtocol_Type(Integer32):
    """Custom type genEquipSecurityCfgWebProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 2))
    )


_GenEquipSecurityCfgWebProtocol_Type.__name__ = "Integer32"
_GenEquipSecurityCfgWebProtocol_Object = MibScalar
genEquipSecurityCfgWebProtocol = _GenEquipSecurityCfgWebProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 7),
    _GenEquipSecurityCfgWebProtocol_Type()
)
genEquipSecurityCfgWebProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgWebProtocol.setStatus("mandatory")
_GenEquipSecurityCfgTelnetAdmin_Type = EnableDisable
_GenEquipSecurityCfgTelnetAdmin_Object = MibScalar
genEquipSecurityCfgTelnetAdmin = _GenEquipSecurityCfgTelnetAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 8),
    _GenEquipSecurityCfgTelnetAdmin_Type()
)
genEquipSecurityCfgTelnetAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgTelnetAdmin.setStatus("mandatory")


class _GenEquipSecurityCfgAutoLogOutPeriod_Type(Integer32):
    """Custom type genEquipSecurityCfgAutoLogOutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_GenEquipSecurityCfgAutoLogOutPeriod_Type.__name__ = "Integer32"
_GenEquipSecurityCfgAutoLogOutPeriod_Object = MibScalar
genEquipSecurityCfgAutoLogOutPeriod = _GenEquipSecurityCfgAutoLogOutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 9),
    _GenEquipSecurityCfgAutoLogOutPeriod_Type()
)
genEquipSecurityCfgAutoLogOutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgAutoLogOutPeriod.setStatus("mandatory")
_GenEquipSecurityXFTP_ObjectIdentity = ObjectIdentity
genEquipSecurityXFTP = _GenEquipSecurityXFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 10)
)
_GenEquipSecurityXFTPHostIP_Type = IpAddress
_GenEquipSecurityXFTPHostIP_Object = MibScalar
genEquipSecurityXFTPHostIP = _GenEquipSecurityXFTPHostIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 10, 1),
    _GenEquipSecurityXFTPHostIP_Type()
)
genEquipSecurityXFTPHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityXFTPHostIP.setStatus("mandatory")
_GenEquipSecurityXFTPHostPath_Type = DisplayString
_GenEquipSecurityXFTPHostPath_Object = MibScalar
genEquipSecurityXFTPHostPath = _GenEquipSecurityXFTPHostPath_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 10, 2),
    _GenEquipSecurityXFTPHostPath_Type()
)
genEquipSecurityXFTPHostPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityXFTPHostPath.setStatus("mandatory")


class _GenEquipSecurityXFTPProtocol_Type(Integer32):
    """Custom type genEquipSecurityXFTPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("sftp", 1))
    )


_GenEquipSecurityXFTPProtocol_Type.__name__ = "Integer32"
_GenEquipSecurityXFTPProtocol_Object = MibScalar
genEquipSecurityXFTPProtocol = _GenEquipSecurityXFTPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 10, 3),
    _GenEquipSecurityXFTPProtocol_Type()
)
genEquipSecurityXFTPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityXFTPProtocol.setStatus("mandatory")
_GenEquipSecurityXFTPUserName_Type = DisplayString
_GenEquipSecurityXFTPUserName_Object = MibScalar
genEquipSecurityXFTPUserName = _GenEquipSecurityXFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 10, 4),
    _GenEquipSecurityXFTPUserName_Type()
)
genEquipSecurityXFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityXFTPUserName.setStatus("mandatory")
_GenEquipSecurityXFTPPassword_Type = DisplayString
_GenEquipSecurityXFTPPassword_Object = MibScalar
genEquipSecurityXFTPPassword = _GenEquipSecurityXFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 10, 5),
    _GenEquipSecurityXFTPPassword_Type()
)
genEquipSecurityXFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityXFTPPassword.setStatus("mandatory")
_GenEquipSecurityCfgPassFirstLoginChange_Type = NoYes
_GenEquipSecurityCfgPassFirstLoginChange_Object = MibScalar
genEquipSecurityCfgPassFirstLoginChange = _GenEquipSecurityCfgPassFirstLoginChange_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 11),
    _GenEquipSecurityCfgPassFirstLoginChange_Type()
)
genEquipSecurityCfgPassFirstLoginChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgPassFirstLoginChange.setStatus("mandatory")


class _GenEquipSecurityCfgCSRCreation_Type(DisplayString):
    """Custom type genEquipSecurityCfgCSRCreation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_GenEquipSecurityCfgCSRCreation_Type.__name__ = "DisplayString"
_GenEquipSecurityCfgCSRCreation_Object = MibScalar
genEquipSecurityCfgCSRCreation = _GenEquipSecurityCfgCSRCreation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 12),
    _GenEquipSecurityCfgCSRCreation_Type()
)
genEquipSecurityCfgCSRCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgCSRCreation.setStatus("mandatory")
_GenEquipSecurityCfgWarningBannerFName_Type = DisplayString
_GenEquipSecurityCfgWarningBannerFName_Object = MibScalar
genEquipSecurityCfgWarningBannerFName = _GenEquipSecurityCfgWarningBannerFName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 13),
    _GenEquipSecurityCfgWarningBannerFName_Type()
)
genEquipSecurityCfgWarningBannerFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCfgWarningBannerFName.setStatus("mandatory")
_GenEquipSecurityConfigurationRadius_ObjectIdentity = ObjectIdentity
genEquipSecurityConfigurationRadius = _GenEquipSecurityConfigurationRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 14)
)
_GenEquipSecurityConfigurationRadiusAdmin_Type = EnableDisable
_GenEquipSecurityConfigurationRadiusAdmin_Object = MibScalar
genEquipSecurityConfigurationRadiusAdmin = _GenEquipSecurityConfigurationRadiusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 14, 1),
    _GenEquipSecurityConfigurationRadiusAdmin_Type()
)
genEquipSecurityConfigurationRadiusAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigurationRadiusAdmin.setStatus("mandatory")
_GenEquipSecurityConfigurationRadiusServerIP_Type = IpAddress
_GenEquipSecurityConfigurationRadiusServerIP_Object = MibScalar
genEquipSecurityConfigurationRadiusServerIP = _GenEquipSecurityConfigurationRadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 14, 2),
    _GenEquipSecurityConfigurationRadiusServerIP_Type()
)
genEquipSecurityConfigurationRadiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigurationRadiusServerIP.setStatus("mandatory")
_GenEquipSecurityConfigurationRadiusSecret_Type = DisplayString
_GenEquipSecurityConfigurationRadiusSecret_Object = MibScalar
genEquipSecurityConfigurationRadiusSecret = _GenEquipSecurityConfigurationRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 14, 3),
    _GenEquipSecurityConfigurationRadiusSecret_Type()
)
genEquipSecurityConfigurationRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigurationRadiusSecret.setStatus("mandatory")
_GenEquipSecurityConfigurationRadiusPort_Type = Integer32
_GenEquipSecurityConfigurationRadiusPort_Object = MibScalar
genEquipSecurityConfigurationRadiusPort = _GenEquipSecurityConfigurationRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 14, 4),
    _GenEquipSecurityConfigurationRadiusPort_Type()
)
genEquipSecurityConfigurationRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigurationRadiusPort.setStatus("mandatory")


class _GenEquipSecurityConfigurationRadiusRetries_Type(Integer32):
    """Custom type genEquipSecurityConfigurationRadiusRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GenEquipSecurityConfigurationRadiusRetries_Type.__name__ = "Integer32"
_GenEquipSecurityConfigurationRadiusRetries_Object = MibScalar
genEquipSecurityConfigurationRadiusRetries = _GenEquipSecurityConfigurationRadiusRetries_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 14, 5),
    _GenEquipSecurityConfigurationRadiusRetries_Type()
)
genEquipSecurityConfigurationRadiusRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigurationRadiusRetries.setStatus("mandatory")


class _GenEquipSecurityConfigurationRadiusTimeout_Type(Integer32):
    """Custom type genEquipSecurityConfigurationRadiusTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_GenEquipSecurityConfigurationRadiusTimeout_Type.__name__ = "Integer32"
_GenEquipSecurityConfigurationRadiusTimeout_Object = MibScalar
genEquipSecurityConfigurationRadiusTimeout = _GenEquipSecurityConfigurationRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 1, 14, 6),
    _GenEquipSecurityConfigurationRadiusTimeout_Type()
)
genEquipSecurityConfigurationRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigurationRadiusTimeout.setStatus("mandatory")
_GenEquipSecurityUsersAndGroups_ObjectIdentity = ObjectIdentity
genEquipSecurityUsersAndGroups = _GenEquipSecurityUsersAndGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2)
)
_GenEquipSecurityUsersTable_Object = MibTable
genEquipSecurityUsersTable = _GenEquipSecurityUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1)
)
if mibBuilder.loadTexts:
    genEquipSecurityUsersTable.setStatus("mandatory")
_GenEquipSecurityUsersEntry_Object = MibTableRow
genEquipSecurityUsersEntry = _GenEquipSecurityUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1, 1)
)
genEquipSecurityUsersEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityUsersName"),
)
if mibBuilder.loadTexts:
    genEquipSecurityUsersEntry.setStatus("mandatory")
_GenEquipSecurityUsersName_Type = DisplayString
_GenEquipSecurityUsersName_Object = MibTableColumn
genEquipSecurityUsersName = _GenEquipSecurityUsersName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1, 1, 1),
    _GenEquipSecurityUsersName_Type()
)
genEquipSecurityUsersName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityUsersName.setStatus("mandatory")
_GenEquipSecurityUsersPasswd_Type = DisplayString
_GenEquipSecurityUsersPasswd_Object = MibTableColumn
genEquipSecurityUsersPasswd = _GenEquipSecurityUsersPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1, 1, 2),
    _GenEquipSecurityUsersPasswd_Type()
)
genEquipSecurityUsersPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityUsersPasswd.setStatus("mandatory")


class _GenEquipSecurityUsersPriviledge_Type(Integer32):
    """Custom type genEquipSecurityUsersPriviledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin-user-lvl", 2),
          ("no-privilege-lvl", -1),
          ("operator-user-lvl", 1),
          ("tech-user-lvl", 3),
          ("viewer-user-lvl", 0))
    )


_GenEquipSecurityUsersPriviledge_Type.__name__ = "Integer32"
_GenEquipSecurityUsersPriviledge_Object = MibTableColumn
genEquipSecurityUsersPriviledge = _GenEquipSecurityUsersPriviledge_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1, 1, 3),
    _GenEquipSecurityUsersPriviledge_Type()
)
genEquipSecurityUsersPriviledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityUsersPriviledge.setStatus("mandatory")


class _GenEquipSecurityUsersPasswdAging_Type(Integer32):
    """Custom type genEquipSecurityUsersPasswdAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_GenEquipSecurityUsersPasswdAging_Type.__name__ = "Integer32"
_GenEquipSecurityUsersPasswdAging_Object = MibTableColumn
genEquipSecurityUsersPasswdAging = _GenEquipSecurityUsersPasswdAging_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1, 1, 4),
    _GenEquipSecurityUsersPasswdAging_Type()
)
genEquipSecurityUsersPasswdAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityUsersPasswdAging.setStatus("mandatory")
_GenEquipSecurityUsersExprDate_Type = Integer32
_GenEquipSecurityUsersExprDate_Object = MibTableColumn
genEquipSecurityUsersExprDate = _GenEquipSecurityUsersExprDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1, 1, 5),
    _GenEquipSecurityUsersExprDate_Type()
)
genEquipSecurityUsersExprDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityUsersExprDate.setStatus("mandatory")
_GenEquipSecurityUsersLastLogin_Type = Integer32
_GenEquipSecurityUsersLastLogin_Object = MibTableColumn
genEquipSecurityUsersLastLogin = _GenEquipSecurityUsersLastLogin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1, 1, 6),
    _GenEquipSecurityUsersLastLogin_Type()
)
genEquipSecurityUsersLastLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityUsersLastLogin.setStatus("mandatory")
_GenEquipSecurityUsersRowStatus_Type = RowStatus
_GenEquipSecurityUsersRowStatus_Object = MibTableColumn
genEquipSecurityUsersRowStatus = _GenEquipSecurityUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 1, 1, 30),
    _GenEquipSecurityUsersRowStatus_Type()
)
genEquipSecurityUsersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityUsersRowStatus.setStatus("mandatory")
_GenEquipSecurityUsersAndGroupsChangePasswd_Type = DisplayString
_GenEquipSecurityUsersAndGroupsChangePasswd_Object = MibScalar
genEquipSecurityUsersAndGroupsChangePasswd = _GenEquipSecurityUsersAndGroupsChangePasswd_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 2, 2),
    _GenEquipSecurityUsersAndGroupsChangePasswd_Type()
)
genEquipSecurityUsersAndGroupsChangePasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityUsersAndGroupsChangePasswd.setStatus("mandatory")
_GenEquipSecuritySNMP_ObjectIdentity = ObjectIdentity
genEquipSecuritySNMP = _GenEquipSecuritySNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3)
)
_GenEquipSecuritySNMPReadCommunity_Type = DisplayString
_GenEquipSecuritySNMPReadCommunity_Object = MibScalar
genEquipSecuritySNMPReadCommunity = _GenEquipSecuritySNMPReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 1),
    _GenEquipSecuritySNMPReadCommunity_Type()
)
genEquipSecuritySNMPReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPReadCommunity.setStatus("mandatory")
_GenEquipSecuritySNMPWriteCommunity_Type = DisplayString
_GenEquipSecuritySNMPWriteCommunity_Object = MibScalar
genEquipSecuritySNMPWriteCommunity = _GenEquipSecuritySNMPWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 2),
    _GenEquipSecuritySNMPWriteCommunity_Type()
)
genEquipSecuritySNMPWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPWriteCommunity.setStatus("mandatory")
_GenEquipSecuritySNMPV3_ObjectIdentity = ObjectIdentity
genEquipSecuritySNMPV3 = _GenEquipSecuritySNMPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10)
)
_GenEquipSecuritySNMPV3AuthTable_Object = MibTable
genEquipSecuritySNMPV3AuthTable = _GenEquipSecuritySNMPV3AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1)
)
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthTable.setStatus("mandatory")
_GenEquipSecuritySNMPV3AuthEntry_Object = MibTableRow
genEquipSecuritySNMPV3AuthEntry = _GenEquipSecuritySNMPV3AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1, 1)
)
genEquipSecuritySNMPV3AuthEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecuritySNMPV3AuthUserName"),
)
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthEntry.setStatus("mandatory")
_GenEquipSecuritySNMPV3AuthUserName_Type = DisplayString
_GenEquipSecuritySNMPV3AuthUserName_Object = MibTableColumn
genEquipSecuritySNMPV3AuthUserName = _GenEquipSecuritySNMPV3AuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1, 1, 1),
    _GenEquipSecuritySNMPV3AuthUserName_Type()
)
genEquipSecuritySNMPV3AuthUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthUserName.setStatus("mandatory")
_GenEquipSecuritySNMPV3AuthPassword_Type = DisplayString
_GenEquipSecuritySNMPV3AuthPassword_Object = MibTableColumn
genEquipSecuritySNMPV3AuthPassword = _GenEquipSecuritySNMPV3AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1, 1, 2),
    _GenEquipSecuritySNMPV3AuthPassword_Type()
)
genEquipSecuritySNMPV3AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthPassword.setStatus("mandatory")


class _GenEquipSecuritySNMPV3AuthSecurityMode_Type(Integer32):
    """Custom type genEquipSecuritySNMPV3AuthSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authNoPriv", 2),
          ("authPriv", 3),
          ("noAuthNoPriv", 1))
    )


_GenEquipSecuritySNMPV3AuthSecurityMode_Type.__name__ = "Integer32"
_GenEquipSecuritySNMPV3AuthSecurityMode_Object = MibTableColumn
genEquipSecuritySNMPV3AuthSecurityMode = _GenEquipSecuritySNMPV3AuthSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1, 1, 3),
    _GenEquipSecuritySNMPV3AuthSecurityMode_Type()
)
genEquipSecuritySNMPV3AuthSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthSecurityMode.setStatus("mandatory")


class _GenEquipSecuritySNMPV3AuthEncryptionMode_Type(Integer32):
    """Custom type genEquipSecuritySNMPV3AuthEncryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 3),
          ("des", 2),
          ("none", 1))
    )


_GenEquipSecuritySNMPV3AuthEncryptionMode_Type.__name__ = "Integer32"
_GenEquipSecuritySNMPV3AuthEncryptionMode_Object = MibTableColumn
genEquipSecuritySNMPV3AuthEncryptionMode = _GenEquipSecuritySNMPV3AuthEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1, 1, 4),
    _GenEquipSecuritySNMPV3AuthEncryptionMode_Type()
)
genEquipSecuritySNMPV3AuthEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthEncryptionMode.setStatus("mandatory")


class _GenEquipSecuritySNMPV3AuthAuthenticationAlgorithm_Type(Integer32):
    """Custom type genEquipSecuritySNMPV3AuthAuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("sha", 2))
    )


_GenEquipSecuritySNMPV3AuthAuthenticationAlgorithm_Type.__name__ = "Integer32"
_GenEquipSecuritySNMPV3AuthAuthenticationAlgorithm_Object = MibTableColumn
genEquipSecuritySNMPV3AuthAuthenticationAlgorithm = _GenEquipSecuritySNMPV3AuthAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1, 1, 5),
    _GenEquipSecuritySNMPV3AuthAuthenticationAlgorithm_Type()
)
genEquipSecuritySNMPV3AuthAuthenticationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthAuthenticationAlgorithm.setStatus("mandatory")


class _GenEquipSecuritySNMPV3AuthAccessMode_Type(Integer32):
    """Custom type genEquipSecuritySNMPV3AuthAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 2),
          ("readWrite", 1))
    )


_GenEquipSecuritySNMPV3AuthAccessMode_Type.__name__ = "Integer32"
_GenEquipSecuritySNMPV3AuthAccessMode_Object = MibTableColumn
genEquipSecuritySNMPV3AuthAccessMode = _GenEquipSecuritySNMPV3AuthAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1, 1, 6),
    _GenEquipSecuritySNMPV3AuthAccessMode_Type()
)
genEquipSecuritySNMPV3AuthAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthAccessMode.setStatus("mandatory")
_GenEquipSecuritySNMPV3AuthRowStatus_Type = RowStatus
_GenEquipSecuritySNMPV3AuthRowStatus_Object = MibTableColumn
genEquipSecuritySNMPV3AuthRowStatus = _GenEquipSecuritySNMPV3AuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 3, 10, 1, 1, 30),
    _GenEquipSecuritySNMPV3AuthRowStatus_Type()
)
genEquipSecuritySNMPV3AuthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecuritySNMPV3AuthRowStatus.setStatus("mandatory")
_GenEquipSecurityGen_ObjectIdentity = ObjectIdentity
genEquipSecurityGen = _GenEquipSecurityGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4)
)
_GenEquipSecurityGenFTConfigTable_Object = MibTable
genEquipSecurityGenFTConfigTable = _GenEquipSecurityGenFTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1)
)
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigTable.setStatus("mandatory")
_GenEquipSecurityGenFTConfigEntry_Object = MibTableRow
genEquipSecurityGenFTConfigEntry = _GenEquipSecurityGenFTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1)
)
genEquipSecurityGenFTConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityGenFTConfigIndex"),
)
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigEntry.setStatus("mandatory")
_GenEquipSecurityGenFTConfigIndex_Type = Integer32
_GenEquipSecurityGenFTConfigIndex_Object = MibTableColumn
genEquipSecurityGenFTConfigIndex = _GenEquipSecurityGenFTConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1, 1),
    _GenEquipSecurityGenFTConfigIndex_Type()
)
genEquipSecurityGenFTConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigIndex.setStatus("mandatory")


class _GenEquipSecurityGenFTConfigProtocol_Type(Integer32):
    """Custom type genEquipSecurityGenFTConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("sftp", 1))
    )


_GenEquipSecurityGenFTConfigProtocol_Type.__name__ = "Integer32"
_GenEquipSecurityGenFTConfigProtocol_Object = MibTableColumn
genEquipSecurityGenFTConfigProtocol = _GenEquipSecurityGenFTConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1, 2),
    _GenEquipSecurityGenFTConfigProtocol_Type()
)
genEquipSecurityGenFTConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigProtocol.setStatus("mandatory")
_GenEquipSecurityGenFTConfigUsername_Type = DisplayString
_GenEquipSecurityGenFTConfigUsername_Object = MibTableColumn
genEquipSecurityGenFTConfigUsername = _GenEquipSecurityGenFTConfigUsername_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1, 3),
    _GenEquipSecurityGenFTConfigUsername_Type()
)
genEquipSecurityGenFTConfigUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigUsername.setStatus("mandatory")
_GenEquipSecurityGenFTConfigPassword_Type = DisplayString
_GenEquipSecurityGenFTConfigPassword_Object = MibTableColumn
genEquipSecurityGenFTConfigPassword = _GenEquipSecurityGenFTConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1, 4),
    _GenEquipSecurityGenFTConfigPassword_Type()
)
genEquipSecurityGenFTConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigPassword.setStatus("mandatory")
_GenEquipSecurityGenFTConfigAddress_Type = IpAddress
_GenEquipSecurityGenFTConfigAddress_Object = MibTableColumn
genEquipSecurityGenFTConfigAddress = _GenEquipSecurityGenFTConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1, 5),
    _GenEquipSecurityGenFTConfigAddress_Type()
)
genEquipSecurityGenFTConfigAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigAddress.setStatus("mandatory")
_GenEquipSecurityGenFTConfigFilePath_Type = DisplayString
_GenEquipSecurityGenFTConfigFilePath_Object = MibTableColumn
genEquipSecurityGenFTConfigFilePath = _GenEquipSecurityGenFTConfigFilePath_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1, 6),
    _GenEquipSecurityGenFTConfigFilePath_Type()
)
genEquipSecurityGenFTConfigFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigFilePath.setStatus("mandatory")
_GenEquipSecurityGenFTConfigFileName_Type = DisplayString
_GenEquipSecurityGenFTConfigFileName_Object = MibTableColumn
genEquipSecurityGenFTConfigFileName = _GenEquipSecurityGenFTConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1, 7),
    _GenEquipSecurityGenFTConfigFileName_Type()
)
genEquipSecurityGenFTConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigFileName.setStatus("mandatory")


class _GenEquipSecurityGenFTConfigIpV6Address_Type(OctetString):
    """Custom type genEquipSecurityGenFTConfigIpV6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipSecurityGenFTConfigIpV6Address_Type.__name__ = "OctetString"
_GenEquipSecurityGenFTConfigIpV6Address_Object = MibTableColumn
genEquipSecurityGenFTConfigIpV6Address = _GenEquipSecurityGenFTConfigIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 1, 1, 8),
    _GenEquipSecurityGenFTConfigIpV6Address_Type()
)
genEquipSecurityGenFTConfigIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTConfigIpV6Address.setStatus("mandatory")
_GenEquipSecurityGenFTStatusTable_Object = MibTable
genEquipSecurityGenFTStatusTable = _GenEquipSecurityGenFTStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 2)
)
if mibBuilder.loadTexts:
    genEquipSecurityGenFTStatusTable.setStatus("mandatory")
_GenEquipSecurityGenFTStatusEntry_Object = MibTableRow
genEquipSecurityGenFTStatusEntry = _GenEquipSecurityGenFTStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 2, 1)
)
genEquipSecurityGenFTStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityGenFTStatusIndex"),
)
if mibBuilder.loadTexts:
    genEquipSecurityGenFTStatusEntry.setStatus("mandatory")
_GenEquipSecurityGenFTStatusIndex_Type = Integer32
_GenEquipSecurityGenFTStatusIndex_Object = MibTableColumn
genEquipSecurityGenFTStatusIndex = _GenEquipSecurityGenFTStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 2, 1, 1),
    _GenEquipSecurityGenFTStatusIndex_Type()
)
genEquipSecurityGenFTStatusIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTStatusIndex.setStatus("mandatory")
_GenEquipSecurityGenFTStatusStatus_Type = FTStatus
_GenEquipSecurityGenFTStatusStatus_Object = MibTableColumn
genEquipSecurityGenFTStatusStatus = _GenEquipSecurityGenFTStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 2, 1, 2),
    _GenEquipSecurityGenFTStatusStatus_Type()
)
genEquipSecurityGenFTStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTStatusStatus.setStatus("mandatory")
_GenEquipSecurityGenFTStatusProgress_Type = Integer32
_GenEquipSecurityGenFTStatusProgress_Object = MibTableColumn
genEquipSecurityGenFTStatusProgress = _GenEquipSecurityGenFTStatusProgress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 2, 1, 3),
    _GenEquipSecurityGenFTStatusProgress_Type()
)
genEquipSecurityGenFTStatusProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTStatusProgress.setStatus("mandatory")


class _GenEquipSecurityGenFTOperations_Type(Integer32):
    """Custom type genEquipSecurityGenFTOperations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("upload-security-log", 1))
    )


_GenEquipSecurityGenFTOperations_Type.__name__ = "Integer32"
_GenEquipSecurityGenFTOperations_Object = MibScalar
genEquipSecurityGenFTOperations = _GenEquipSecurityGenFTOperations_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 11),
    _GenEquipSecurityGenFTOperations_Type()
)
genEquipSecurityGenFTOperations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenFTOperations.setStatus("mandatory")
_GenEquipSecurityGenImportExportAdmin_Type = EnableDisable
_GenEquipSecurityGenImportExportAdmin_Object = MibScalar
genEquipSecurityGenImportExportAdmin = _GenEquipSecurityGenImportExportAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 4, 12),
    _GenEquipSecurityGenImportExportAdmin_Type()
)
genEquipSecurityGenImportExportAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityGenImportExportAdmin.setStatus("mandatory")
_GenEquipSecurityAccessControl_ObjectIdentity = ObjectIdentity
genEquipSecurityAccessControl = _GenEquipSecurityAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5)
)
_GenEquipSecurityAccessControlProfileTable_Object = MibTable
genEquipSecurityAccessControlProfileTable = _GenEquipSecurityAccessControlProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1)
)
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileTable.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileEntry_Object = MibTableRow
genEquipSecurityAccessControlProfileEntry = _GenEquipSecurityAccessControlProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1)
)
genEquipSecurityAccessControlProfileEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityAccessControlProfileName"),
)
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileEntry.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileName_Type = DisplayString
_GenEquipSecurityAccessControlProfileName_Object = MibTableColumn
genEquipSecurityAccessControlProfileName = _GenEquipSecurityAccessControlProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 1),
    _GenEquipSecurityAccessControlProfileName_Type()
)
genEquipSecurityAccessControlProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileName.setStatus("mandatory")


class _GenEquipSecurityAccessControlProfileChannel_Type(Integer32):
    """Custom type genEquipSecurityAccessControlProfileChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_GenEquipSecurityAccessControlProfileChannel_Type.__name__ = "Integer32"
_GenEquipSecurityAccessControlProfileChannel_Object = MibTableColumn
genEquipSecurityAccessControlProfileChannel = _GenEquipSecurityAccessControlProfileChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 2),
    _GenEquipSecurityAccessControlProfileChannel_Type()
)
genEquipSecurityAccessControlProfileChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileChannel.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileUsed_Type = Integer32
_GenEquipSecurityAccessControlProfileUsed_Object = MibTableColumn
genEquipSecurityAccessControlProfileUsed = _GenEquipSecurityAccessControlProfileUsed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 3),
    _GenEquipSecurityAccessControlProfileUsed_Type()
)
genEquipSecurityAccessControlProfileUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileUsed.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileSecurityWrite_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileSecurityWrite_Object = MibTableColumn
genEquipSecurityAccessControlProfileSecurityWrite = _GenEquipSecurityAccessControlProfileSecurityWrite_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 4),
    _GenEquipSecurityAccessControlProfileSecurityWrite_Type()
)
genEquipSecurityAccessControlProfileSecurityWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileSecurityWrite.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileSecurityRead_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileSecurityRead_Object = MibTableColumn
genEquipSecurityAccessControlProfileSecurityRead = _GenEquipSecurityAccessControlProfileSecurityRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 5),
    _GenEquipSecurityAccessControlProfileSecurityRead_Type()
)
genEquipSecurityAccessControlProfileSecurityRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileSecurityRead.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileMngWrite_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileMngWrite_Object = MibTableColumn
genEquipSecurityAccessControlProfileMngWrite = _GenEquipSecurityAccessControlProfileMngWrite_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 6),
    _GenEquipSecurityAccessControlProfileMngWrite_Type()
)
genEquipSecurityAccessControlProfileMngWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileMngWrite.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileMngRead_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileMngRead_Object = MibTableColumn
genEquipSecurityAccessControlProfileMngRead = _GenEquipSecurityAccessControlProfileMngRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 7),
    _GenEquipSecurityAccessControlProfileMngRead_Type()
)
genEquipSecurityAccessControlProfileMngRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileMngRead.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileRadioWrite_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileRadioWrite_Object = MibTableColumn
genEquipSecurityAccessControlProfileRadioWrite = _GenEquipSecurityAccessControlProfileRadioWrite_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 8),
    _GenEquipSecurityAccessControlProfileRadioWrite_Type()
)
genEquipSecurityAccessControlProfileRadioWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileRadioWrite.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileRadioRead_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileRadioRead_Object = MibTableColumn
genEquipSecurityAccessControlProfileRadioRead = _GenEquipSecurityAccessControlProfileRadioRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 9),
    _GenEquipSecurityAccessControlProfileRadioRead_Type()
)
genEquipSecurityAccessControlProfileRadioRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileRadioRead.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileTDMWrite_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileTDMWrite_Object = MibTableColumn
genEquipSecurityAccessControlProfileTDMWrite = _GenEquipSecurityAccessControlProfileTDMWrite_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 10),
    _GenEquipSecurityAccessControlProfileTDMWrite_Type()
)
genEquipSecurityAccessControlProfileTDMWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileTDMWrite.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileTDMRead_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileTDMRead_Object = MibTableColumn
genEquipSecurityAccessControlProfileTDMRead = _GenEquipSecurityAccessControlProfileTDMRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 11),
    _GenEquipSecurityAccessControlProfileTDMRead_Type()
)
genEquipSecurityAccessControlProfileTDMRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileTDMRead.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileEthWrite_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileEthWrite_Object = MibTableColumn
genEquipSecurityAccessControlProfileEthWrite = _GenEquipSecurityAccessControlProfileEthWrite_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 12),
    _GenEquipSecurityAccessControlProfileEthWrite_Type()
)
genEquipSecurityAccessControlProfileEthWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileEthWrite.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileEthRead_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileEthRead_Object = MibTableColumn
genEquipSecurityAccessControlProfileEthRead = _GenEquipSecurityAccessControlProfileEthRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 13),
    _GenEquipSecurityAccessControlProfileEthRead_Type()
)
genEquipSecurityAccessControlProfileEthRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileEthRead.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileSyncWrite_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileSyncWrite_Object = MibTableColumn
genEquipSecurityAccessControlProfileSyncWrite = _GenEquipSecurityAccessControlProfileSyncWrite_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 14),
    _GenEquipSecurityAccessControlProfileSyncWrite_Type()
)
genEquipSecurityAccessControlProfileSyncWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileSyncWrite.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileSyncRead_Type = RbacAccessLevel
_GenEquipSecurityAccessControlProfileSyncRead_Object = MibTableColumn
genEquipSecurityAccessControlProfileSyncRead = _GenEquipSecurityAccessControlProfileSyncRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 15),
    _GenEquipSecurityAccessControlProfileSyncRead_Type()
)
genEquipSecurityAccessControlProfileSyncRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileSyncRead.setStatus("mandatory")
_GenEquipSecurityAccessControlProfileRowStatus_Type = RowStatus
_GenEquipSecurityAccessControlProfileRowStatus_Object = MibTableColumn
genEquipSecurityAccessControlProfileRowStatus = _GenEquipSecurityAccessControlProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 1, 1, 30),
    _GenEquipSecurityAccessControlProfileRowStatus_Type()
)
genEquipSecurityAccessControlProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlProfileRowStatus.setStatus("mandatory")
_GenEquipSecurityAccessControlUserTable_Object = MibTable
genEquipSecurityAccessControlUserTable = _GenEquipSecurityAccessControlUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2)
)
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserTable.setStatus("mandatory")
_GenEquipSecurityAccessControlUserEntry_Object = MibTableRow
genEquipSecurityAccessControlUserEntry = _GenEquipSecurityAccessControlUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1)
)
genEquipSecurityAccessControlUserEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityAccessControlUserName"),
)
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserEntry.setStatus("mandatory")
_GenEquipSecurityAccessControlUserName_Type = DisplayString
_GenEquipSecurityAccessControlUserName_Object = MibTableColumn
genEquipSecurityAccessControlUserName = _GenEquipSecurityAccessControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1, 1),
    _GenEquipSecurityAccessControlUserName_Type()
)
genEquipSecurityAccessControlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserName.setStatus("mandatory")
_GenEquipSecurityAccessControlUserProfile_Type = DisplayString
_GenEquipSecurityAccessControlUserProfile_Object = MibTableColumn
genEquipSecurityAccessControlUserProfile = _GenEquipSecurityAccessControlUserProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1, 2),
    _GenEquipSecurityAccessControlUserProfile_Type()
)
genEquipSecurityAccessControlUserProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserProfile.setStatus("mandatory")
_GenEquipSecurityAccessControlUserPassword_Type = DisplayString
_GenEquipSecurityAccessControlUserPassword_Object = MibTableColumn
genEquipSecurityAccessControlUserPassword = _GenEquipSecurityAccessControlUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1, 3),
    _GenEquipSecurityAccessControlUserPassword_Type()
)
genEquipSecurityAccessControlUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserPassword.setStatus("mandatory")
_GenEquipSecurityAccessControlUserExpired_Type = Integer32
_GenEquipSecurityAccessControlUserExpired_Object = MibTableColumn
genEquipSecurityAccessControlUserExpired = _GenEquipSecurityAccessControlUserExpired_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1, 4),
    _GenEquipSecurityAccessControlUserExpired_Type()
)
genEquipSecurityAccessControlUserExpired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserExpired.setStatus("mandatory")
_GenEquipSecurityAccessControlUserBlock_Type = NoYes
_GenEquipSecurityAccessControlUserBlock_Object = MibTableColumn
genEquipSecurityAccessControlUserBlock = _GenEquipSecurityAccessControlUserBlock_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1, 5),
    _GenEquipSecurityAccessControlUserBlock_Type()
)
genEquipSecurityAccessControlUserBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserBlock.setStatus("mandatory")
_GenEquipSecurityAccessControlUserLastLogout_Type = Integer32
_GenEquipSecurityAccessControlUserLastLogout_Object = MibTableColumn
genEquipSecurityAccessControlUserLastLogout = _GenEquipSecurityAccessControlUserLastLogout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1, 6),
    _GenEquipSecurityAccessControlUserLastLogout_Type()
)
genEquipSecurityAccessControlUserLastLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserLastLogout.setStatus("mandatory")
_GenEquipSecurityAccessControlUserLoggedIn_Type = NoYes
_GenEquipSecurityAccessControlUserLoggedIn_Object = MibTableColumn
genEquipSecurityAccessControlUserLoggedIn = _GenEquipSecurityAccessControlUserLoggedIn_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1, 7),
    _GenEquipSecurityAccessControlUserLoggedIn_Type()
)
genEquipSecurityAccessControlUserLoggedIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserLoggedIn.setStatus("mandatory")
_GenEquipSecurityAccessControlUserRowStatus_Type = RowStatus
_GenEquipSecurityAccessControlUserRowStatus_Object = MibTableColumn
genEquipSecurityAccessControlUserRowStatus = _GenEquipSecurityAccessControlUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 2, 1, 30),
    _GenEquipSecurityAccessControlUserRowStatus_Type()
)
genEquipSecurityAccessControlUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlUserRowStatus.setStatus("mandatory")
_GenEquipSecurityAccessControlPassEnforceStrength_Type = NoYes
_GenEquipSecurityAccessControlPassEnforceStrength_Object = MibScalar
genEquipSecurityAccessControlPassEnforceStrength = _GenEquipSecurityAccessControlPassEnforceStrength_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 11),
    _GenEquipSecurityAccessControlPassEnforceStrength_Type()
)
genEquipSecurityAccessControlPassEnforceStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlPassEnforceStrength.setStatus("mandatory")
_GenEquipSecurityAccessControlPassFirstLoginChange_Type = NoYes
_GenEquipSecurityAccessControlPassFirstLoginChange_Object = MibScalar
genEquipSecurityAccessControlPassFirstLoginChange = _GenEquipSecurityAccessControlPassFirstLoginChange_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 12),
    _GenEquipSecurityAccessControlPassFirstLoginChange_Type()
)
genEquipSecurityAccessControlPassFirstLoginChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlPassFirstLoginChange.setStatus("mandatory")
_GenEquipSecurityAccessControlPassAging_Type = NoYes
_GenEquipSecurityAccessControlPassAging_Object = MibScalar
genEquipSecurityAccessControlPassAging = _GenEquipSecurityAccessControlPassAging_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 13),
    _GenEquipSecurityAccessControlPassAging_Type()
)
genEquipSecurityAccessControlPassAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlPassAging.setStatus("mandatory")


class _GenEquipSecurityAccessControlFailureLoginAttempt_Type(Integer32):
    """Custom type genEquipSecurityAccessControlFailureLoginAttempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GenEquipSecurityAccessControlFailureLoginAttempt_Type.__name__ = "Integer32"
_GenEquipSecurityAccessControlFailureLoginAttempt_Object = MibScalar
genEquipSecurityAccessControlFailureLoginAttempt = _GenEquipSecurityAccessControlFailureLoginAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 14),
    _GenEquipSecurityAccessControlFailureLoginAttempt_Type()
)
genEquipSecurityAccessControlFailureLoginAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlFailureLoginAttempt.setStatus("mandatory")


class _GenEquipSecurityAccessControlBlockFailureLoginPeriod_Type(Integer32):
    """Custom type genEquipSecurityAccessControlBlockFailureLoginPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_GenEquipSecurityAccessControlBlockFailureLoginPeriod_Type.__name__ = "Integer32"
_GenEquipSecurityAccessControlBlockFailureLoginPeriod_Object = MibScalar
genEquipSecurityAccessControlBlockFailureLoginPeriod = _GenEquipSecurityAccessControlBlockFailureLoginPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 15),
    _GenEquipSecurityAccessControlBlockFailureLoginPeriod_Type()
)
genEquipSecurityAccessControlBlockFailureLoginPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlBlockFailureLoginPeriod.setStatus("mandatory")


class _GenEquipSecurityAccessControlBlockunusedAccount_Type(Integer32):
    """Custom type genEquipSecurityAccessControlBlockunusedAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_GenEquipSecurityAccessControlBlockunusedAccount_Type.__name__ = "Integer32"
_GenEquipSecurityAccessControlBlockunusedAccount_Object = MibScalar
genEquipSecurityAccessControlBlockunusedAccount = _GenEquipSecurityAccessControlBlockunusedAccount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 16),
    _GenEquipSecurityAccessControlBlockunusedAccount_Type()
)
genEquipSecurityAccessControlBlockunusedAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlBlockunusedAccount.setStatus("mandatory")
_GenEquipSecurityAccessControlBlockRootRemote_Type = NoYes
_GenEquipSecurityAccessControlBlockRootRemote_Object = MibScalar
genEquipSecurityAccessControlBlockRootRemote = _GenEquipSecurityAccessControlBlockRootRemote_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 5, 17),
    _GenEquipSecurityAccessControlBlockRootRemote_Type()
)
genEquipSecurityAccessControlBlockRootRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlBlockRootRemote.setStatus("mandatory")
_GenEquipSecurityProtocolsControl_ObjectIdentity = ObjectIdentity
genEquipSecurityProtocolsControl = _GenEquipSecurityProtocolsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 6)
)


class _GenEquipSecurityProtocolsControlAutoSessionTimeOut_Type(Integer32):
    """Custom type genEquipSecurityProtocolsControlAutoSessionTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_GenEquipSecurityProtocolsControlAutoSessionTimeOut_Type.__name__ = "Integer32"
_GenEquipSecurityProtocolsControlAutoSessionTimeOut_Object = MibScalar
genEquipSecurityProtocolsControlAutoSessionTimeOut = _GenEquipSecurityProtocolsControlAutoSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 6, 1),
    _GenEquipSecurityProtocolsControlAutoSessionTimeOut_Type()
)
genEquipSecurityProtocolsControlAutoSessionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityProtocolsControlAutoSessionTimeOut.setStatus("mandatory")
_GenEquipSecurityProtocolsControlSNMPAdmin_Type = EnableDisable
_GenEquipSecurityProtocolsControlSNMPAdmin_Object = MibScalar
genEquipSecurityProtocolsControlSNMPAdmin = _GenEquipSecurityProtocolsControlSNMPAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 6, 2),
    _GenEquipSecurityProtocolsControlSNMPAdmin_Type()
)
genEquipSecurityProtocolsControlSNMPAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityProtocolsControlSNMPAdmin.setStatus("mandatory")
_GenEquipSecurityProtocolsControlSNMPOperStatus_Type = DownUp
_GenEquipSecurityProtocolsControlSNMPOperStatus_Object = MibScalar
genEquipSecurityProtocolsControlSNMPOperStatus = _GenEquipSecurityProtocolsControlSNMPOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 6, 3),
    _GenEquipSecurityProtocolsControlSNMPOperStatus_Type()
)
genEquipSecurityProtocolsControlSNMPOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityProtocolsControlSNMPOperStatus.setStatus("mandatory")


class _GenEquipSecurityProtocolsControlSNMPTrapVersion_Type(Integer32):
    """Custom type genEquipSecurityProtocolsControlSNMPTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_GenEquipSecurityProtocolsControlSNMPTrapVersion_Type.__name__ = "Integer32"
_GenEquipSecurityProtocolsControlSNMPTrapVersion_Object = MibScalar
genEquipSecurityProtocolsControlSNMPTrapVersion = _GenEquipSecurityProtocolsControlSNMPTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 6, 4),
    _GenEquipSecurityProtocolsControlSNMPTrapVersion_Type()
)
genEquipSecurityProtocolsControlSNMPTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityProtocolsControlSNMPTrapVersion.setStatus("mandatory")
_GenEquipSecurityProtocolsControlSNMPMIBVersion_Type = DisplayString
_GenEquipSecurityProtocolsControlSNMPMIBVersion_Object = MibScalar
genEquipSecurityProtocolsControlSNMPMIBVersion = _GenEquipSecurityProtocolsControlSNMPMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 6, 5),
    _GenEquipSecurityProtocolsControlSNMPMIBVersion_Type()
)
genEquipSecurityProtocolsControlSNMPMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityProtocolsControlSNMPMIBVersion.setStatus("mandatory")
_GenEquipSecurityProtocolsControlSNMPV1V2Blocked_Type = NoYes
_GenEquipSecurityProtocolsControlSNMPV1V2Blocked_Object = MibScalar
genEquipSecurityProtocolsControlSNMPV1V2Blocked = _GenEquipSecurityProtocolsControlSNMPV1V2Blocked_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 6, 6),
    _GenEquipSecurityProtocolsControlSNMPV1V2Blocked_Type()
)
genEquipSecurityProtocolsControlSNMPV1V2Blocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityProtocolsControlSNMPV1V2Blocked.setStatus("mandatory")
_GenEquipSecurityProtocolsControlHTTPAdmin_Type = EnableDisable
_GenEquipSecurityProtocolsControlHTTPAdmin_Object = MibScalar
genEquipSecurityProtocolsControlHTTPAdmin = _GenEquipSecurityProtocolsControlHTTPAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 6, 7),
    _GenEquipSecurityProtocolsControlHTTPAdmin_Type()
)
genEquipSecurityProtocolsControlHTTPAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityProtocolsControlHTTPAdmin.setStatus("mandatory")
_GenEquipSecurityMonitorAndLogs_ObjectIdentity = ObjectIdentity
genEquipSecurityMonitorAndLogs = _GenEquipSecurityMonitorAndLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7)
)
_GenEquipSecurityConfigLogUploadConfigTable_Object = MibTable
genEquipSecurityConfigLogUploadConfigTable = _GenEquipSecurityConfigLogUploadConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1)
)
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigTable.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadConfigEntry_Object = MibTableRow
genEquipSecurityConfigLogUploadConfigEntry = _GenEquipSecurityConfigLogUploadConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1)
)
genEquipSecurityConfigLogUploadConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityConfigLogUploadConfigIndex"),
)
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigEntry.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadConfigIndex_Type = Integer32
_GenEquipSecurityConfigLogUploadConfigIndex_Object = MibTableColumn
genEquipSecurityConfigLogUploadConfigIndex = _GenEquipSecurityConfigLogUploadConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1, 1),
    _GenEquipSecurityConfigLogUploadConfigIndex_Type()
)
genEquipSecurityConfigLogUploadConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigIndex.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadConfigProtocol_Type = FtpProtocolType
_GenEquipSecurityConfigLogUploadConfigProtocol_Object = MibTableColumn
genEquipSecurityConfigLogUploadConfigProtocol = _GenEquipSecurityConfigLogUploadConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1, 2),
    _GenEquipSecurityConfigLogUploadConfigProtocol_Type()
)
genEquipSecurityConfigLogUploadConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigProtocol.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadConfigUsername_Type = DisplayString
_GenEquipSecurityConfigLogUploadConfigUsername_Object = MibTableColumn
genEquipSecurityConfigLogUploadConfigUsername = _GenEquipSecurityConfigLogUploadConfigUsername_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1, 3),
    _GenEquipSecurityConfigLogUploadConfigUsername_Type()
)
genEquipSecurityConfigLogUploadConfigUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigUsername.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadConfigPassword_Type = DisplayString
_GenEquipSecurityConfigLogUploadConfigPassword_Object = MibTableColumn
genEquipSecurityConfigLogUploadConfigPassword = _GenEquipSecurityConfigLogUploadConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1, 4),
    _GenEquipSecurityConfigLogUploadConfigPassword_Type()
)
genEquipSecurityConfigLogUploadConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigPassword.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadConfigIpaddress_Type = IpAddress
_GenEquipSecurityConfigLogUploadConfigIpaddress_Object = MibTableColumn
genEquipSecurityConfigLogUploadConfigIpaddress = _GenEquipSecurityConfigLogUploadConfigIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1, 5),
    _GenEquipSecurityConfigLogUploadConfigIpaddress_Type()
)
genEquipSecurityConfigLogUploadConfigIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigIpaddress.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadConfigPath_Type = DisplayString
_GenEquipSecurityConfigLogUploadConfigPath_Object = MibTableColumn
genEquipSecurityConfigLogUploadConfigPath = _GenEquipSecurityConfigLogUploadConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1, 6),
    _GenEquipSecurityConfigLogUploadConfigPath_Type()
)
genEquipSecurityConfigLogUploadConfigPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigPath.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadConfigFilename_Type = DisplayString
_GenEquipSecurityConfigLogUploadConfigFilename_Object = MibTableColumn
genEquipSecurityConfigLogUploadConfigFilename = _GenEquipSecurityConfigLogUploadConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1, 7),
    _GenEquipSecurityConfigLogUploadConfigFilename_Type()
)
genEquipSecurityConfigLogUploadConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigFilename.setStatus("mandatory")


class _GenEquipSecurityConfigLogUploadConfigIpV6Address_Type(OctetString):
    """Custom type genEquipSecurityConfigLogUploadConfigIpV6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipSecurityConfigLogUploadConfigIpV6Address_Type.__name__ = "OctetString"
_GenEquipSecurityConfigLogUploadConfigIpV6Address_Object = MibTableColumn
genEquipSecurityConfigLogUploadConfigIpV6Address = _GenEquipSecurityConfigLogUploadConfigIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 1, 1, 8),
    _GenEquipSecurityConfigLogUploadConfigIpV6Address_Type()
)
genEquipSecurityConfigLogUploadConfigIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadConfigIpV6Address.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadStatusTable_Object = MibTable
genEquipSecurityConfigLogUploadStatusTable = _GenEquipSecurityConfigLogUploadStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 2)
)
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadStatusTable.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadStatusEntry_Object = MibTableRow
genEquipSecurityConfigLogUploadStatusEntry = _GenEquipSecurityConfigLogUploadStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 2, 1)
)
genEquipSecurityConfigLogUploadStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityConfigLogUploadStatusIndex"),
)
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadStatusEntry.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadStatusIndex_Type = Integer32
_GenEquipSecurityConfigLogUploadStatusIndex_Object = MibTableColumn
genEquipSecurityConfigLogUploadStatusIndex = _GenEquipSecurityConfigLogUploadStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 2, 1, 1),
    _GenEquipSecurityConfigLogUploadStatusIndex_Type()
)
genEquipSecurityConfigLogUploadStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadStatusIndex.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadStatusStatus_Type = FileTransferStatus
_GenEquipSecurityConfigLogUploadStatusStatus_Object = MibTableColumn
genEquipSecurityConfigLogUploadStatusStatus = _GenEquipSecurityConfigLogUploadStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 2, 1, 2),
    _GenEquipSecurityConfigLogUploadStatusStatus_Type()
)
genEquipSecurityConfigLogUploadStatusStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadStatusStatus.setStatus("mandatory")
_GenEquipSecurityConfigLogUploadStatusPrcntg_Type = Integer32
_GenEquipSecurityConfigLogUploadStatusPrcntg_Object = MibTableColumn
genEquipSecurityConfigLogUploadStatusPrcntg = _GenEquipSecurityConfigLogUploadStatusPrcntg_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 2, 1, 3),
    _GenEquipSecurityConfigLogUploadStatusPrcntg_Type()
)
genEquipSecurityConfigLogUploadStatusPrcntg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUploadStatusPrcntg.setStatus("mandatory")


class _GenEquipSecurityConfigLogUpload_Type(Integer32):
    """Custom type genEquipSecurityConfigLogUpload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("upload-security-log", 1))
    )


_GenEquipSecurityConfigLogUpload_Type.__name__ = "Integer32"
_GenEquipSecurityConfigLogUpload_Object = MibScalar
genEquipSecurityConfigLogUpload = _GenEquipSecurityConfigLogUpload_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 7, 10),
    _GenEquipSecurityConfigLogUpload_Type()
)
genEquipSecurityConfigLogUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityConfigLogUpload.setStatus("mandatory")
_GenEquipSecurityRadiusServer_ObjectIdentity = ObjectIdentity
genEquipSecurityRadiusServer = _GenEquipSecurityRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8)
)
_GenEquipSecurityRadiusServerConfigurationTable_Object = MibTable
genEquipSecurityRadiusServerConfigurationTable = _GenEquipSecurityRadiusServerConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1)
)
if mibBuilder.loadTexts:
    genEquipSecurityRadiusServerConfigurationTable.setStatus("mandatory")
_GenEquipSecurityRadiusServerConfigurationEntry_Object = MibTableRow
genEquipSecurityRadiusServerConfigurationEntry = _GenEquipSecurityRadiusServerConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1)
)
genEquipSecurityRadiusServerConfigurationEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityAccessControlRadiusServerId"),
)
if mibBuilder.loadTexts:
    genEquipSecurityRadiusServerConfigurationEntry.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusServerId_Type = Integer32
_GenEquipSecurityAccessControlRadiusServerId_Object = MibTableColumn
genEquipSecurityAccessControlRadiusServerId = _GenEquipSecurityAccessControlRadiusServerId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1, 1),
    _GenEquipSecurityAccessControlRadiusServerId_Type()
)
genEquipSecurityAccessControlRadiusServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusServerId.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusServerIpV4Address_Type = IpAddress
_GenEquipSecurityAccessControlRadiusServerIpV4Address_Object = MibTableColumn
genEquipSecurityAccessControlRadiusServerIpV4Address = _GenEquipSecurityAccessControlRadiusServerIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1, 2),
    _GenEquipSecurityAccessControlRadiusServerIpV4Address_Type()
)
genEquipSecurityAccessControlRadiusServerIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusServerIpV4Address.setStatus("mandatory")


class _GenEquipSecurityAccessControlRadiusServerIpv6Address_Type(OctetString):
    """Custom type genEquipSecurityAccessControlRadiusServerIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipSecurityAccessControlRadiusServerIpv6Address_Type.__name__ = "OctetString"
_GenEquipSecurityAccessControlRadiusServerIpv6Address_Object = MibTableColumn
genEquipSecurityAccessControlRadiusServerIpv6Address = _GenEquipSecurityAccessControlRadiusServerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1, 3),
    _GenEquipSecurityAccessControlRadiusServerIpv6Address_Type()
)
genEquipSecurityAccessControlRadiusServerIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusServerIpv6Address.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusServerPort_Type = Integer32
_GenEquipSecurityAccessControlRadiusServerPort_Object = MibTableColumn
genEquipSecurityAccessControlRadiusServerPort = _GenEquipSecurityAccessControlRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1, 4),
    _GenEquipSecurityAccessControlRadiusServerPort_Type()
)
genEquipSecurityAccessControlRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusServerPort.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusServerRetries_Type = Integer32
_GenEquipSecurityAccessControlRadiusServerRetries_Object = MibTableColumn
genEquipSecurityAccessControlRadiusServerRetries = _GenEquipSecurityAccessControlRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1, 5),
    _GenEquipSecurityAccessControlRadiusServerRetries_Type()
)
genEquipSecurityAccessControlRadiusServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusServerRetries.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusServerTimeout_Type = Integer32
_GenEquipSecurityAccessControlRadiusServerTimeout_Object = MibTableColumn
genEquipSecurityAccessControlRadiusServerTimeout = _GenEquipSecurityAccessControlRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1, 6),
    _GenEquipSecurityAccessControlRadiusServerTimeout_Type()
)
genEquipSecurityAccessControlRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusServerTimeout.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusServerSharedSecret_Type = OctetString
_GenEquipSecurityAccessControlRadiusServerSharedSecret_Object = MibTableColumn
genEquipSecurityAccessControlRadiusServerSharedSecret = _GenEquipSecurityAccessControlRadiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1, 7),
    _GenEquipSecurityAccessControlRadiusServerSharedSecret_Type()
)
genEquipSecurityAccessControlRadiusServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusServerSharedSecret.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusServerConnectivityStatus_Type = EnableDisable
_GenEquipSecurityAccessControlRadiusServerConnectivityStatus_Object = MibTableColumn
genEquipSecurityAccessControlRadiusServerConnectivityStatus = _GenEquipSecurityAccessControlRadiusServerConnectivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 1, 1, 8),
    _GenEquipSecurityAccessControlRadiusServerConnectivityStatus_Type()
)
genEquipSecurityAccessControlRadiusServerConnectivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusServerConnectivityStatus.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersTable_Object = MibTable
genEquipSecurityAccessControlRadiusUsersTable = _GenEquipSecurityAccessControlRadiusUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2)
)
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersTable.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersEntry_Object = MibTableRow
genEquipSecurityAccessControlRadiusUsersEntry = _GenEquipSecurityAccessControlRadiusUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1)
)
genEquipSecurityAccessControlRadiusUsersEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityAccessControlRadiusUsersId"),
)
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersEntry.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersId_Type = DisplayString
_GenEquipSecurityAccessControlRadiusUsersId_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersId = _GenEquipSecurityAccessControlRadiusUsersId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 1),
    _GenEquipSecurityAccessControlRadiusUsersId_Type()
)
genEquipSecurityAccessControlRadiusUsersId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersId.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUserInstances_Type = Integer32
_GenEquipSecurityAccessControlRadiusUserInstances_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUserInstances = _GenEquipSecurityAccessControlRadiusUserInstances_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 2),
    _GenEquipSecurityAccessControlRadiusUserInstances_Type()
)
genEquipSecurityAccessControlRadiusUserInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUserInstances.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersAccessChannels_Type = Integer32
_GenEquipSecurityAccessControlRadiusUsersAccessChannels_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersAccessChannels = _GenEquipSecurityAccessControlRadiusUsersAccessChannels_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 3),
    _GenEquipSecurityAccessControlRadiusUsersAccessChannels_Type()
)
genEquipSecurityAccessControlRadiusUsersAccessChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersAccessChannels.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersEthReadLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersEthReadLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersEthReadLevel = _GenEquipSecurityAccessControlRadiusUsersEthReadLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 4),
    _GenEquipSecurityAccessControlRadiusUsersEthReadLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersEthReadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersEthReadLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersEthWriteLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersEthWriteLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersEthWriteLevel = _GenEquipSecurityAccessControlRadiusUsersEthWriteLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 5),
    _GenEquipSecurityAccessControlRadiusUsersEthWriteLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersEthWriteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersEthWriteLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersMngReadLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersMngReadLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersMngReadLevel = _GenEquipSecurityAccessControlRadiusUsersMngReadLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 6),
    _GenEquipSecurityAccessControlRadiusUsersMngReadLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersMngReadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersMngReadLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersMngWriteLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersMngWriteLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersMngWriteLevel = _GenEquipSecurityAccessControlRadiusUsersMngWriteLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 7),
    _GenEquipSecurityAccessControlRadiusUsersMngWriteLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersMngWriteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersMngWriteLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersRadioReadLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersRadioReadLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersRadioReadLevel = _GenEquipSecurityAccessControlRadiusUsersRadioReadLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 8),
    _GenEquipSecurityAccessControlRadiusUsersRadioReadLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersRadioReadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersRadioReadLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersRadioWriteLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersRadioWriteLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersRadioWriteLevel = _GenEquipSecurityAccessControlRadiusUsersRadioWriteLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 9),
    _GenEquipSecurityAccessControlRadiusUsersRadioWriteLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersRadioWriteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersRadioWriteLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersSecurityReadLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersSecurityReadLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersSecurityReadLevel = _GenEquipSecurityAccessControlRadiusUsersSecurityReadLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 10),
    _GenEquipSecurityAccessControlRadiusUsersSecurityReadLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersSecurityReadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersSecurityReadLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersSecurityWriteLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersSecurityWriteLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersSecurityWriteLevel = _GenEquipSecurityAccessControlRadiusUsersSecurityWriteLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 11),
    _GenEquipSecurityAccessControlRadiusUsersSecurityWriteLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersSecurityWriteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersSecurityWriteLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersSyncReadLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersSyncReadLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersSyncReadLevel = _GenEquipSecurityAccessControlRadiusUsersSyncReadLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 12),
    _GenEquipSecurityAccessControlRadiusUsersSyncReadLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersSyncReadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersSyncReadLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersSyncWriteLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersSyncWriteLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersSyncWriteLevel = _GenEquipSecurityAccessControlRadiusUsersSyncWriteLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 13),
    _GenEquipSecurityAccessControlRadiusUsersSyncWriteLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersSyncWriteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersSyncWriteLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersTdmReadLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersTdmReadLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersTdmReadLevel = _GenEquipSecurityAccessControlRadiusUsersTdmReadLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 14),
    _GenEquipSecurityAccessControlRadiusUsersTdmReadLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersTdmReadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersTdmReadLevel.setStatus("mandatory")
_GenEquipSecurityAccessControlRadiusUsersTdmWriteLevel_Type = RaduisAcceaaLevel
_GenEquipSecurityAccessControlRadiusUsersTdmWriteLevel_Object = MibTableColumn
genEquipSecurityAccessControlRadiusUsersTdmWriteLevel = _GenEquipSecurityAccessControlRadiusUsersTdmWriteLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 2, 1, 15),
    _GenEquipSecurityAccessControlRadiusUsersTdmWriteLevel_Type()
)
genEquipSecurityAccessControlRadiusUsersTdmWriteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityAccessControlRadiusUsersTdmWriteLevel.setStatus("mandatory")
_GenEquipSecurityRadiusAdmin_Type = EnableDisable
_GenEquipSecurityRadiusAdmin_Object = MibScalar
genEquipSecurityRadiusAdmin = _GenEquipSecurityRadiusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 8, 10),
    _GenEquipSecurityRadiusAdmin_Type()
)
genEquipSecurityRadiusAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityRadiusAdmin.setStatus("mandatory")
_GenEquipSecurityCertificate_ObjectIdentity = ObjectIdentity
genEquipSecurityCertificate = _GenEquipSecurityCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9)
)
_GenEquipSecurityCsrCertificateFileTransferSet_Type = CsrCertificateFTState
_GenEquipSecurityCsrCertificateFileTransferSet_Object = MibScalar
genEquipSecurityCsrCertificateFileTransferSet = _GenEquipSecurityCsrCertificateFileTransferSet_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 1),
    _GenEquipSecurityCsrCertificateFileTransferSet_Type()
)
genEquipSecurityCsrCertificateFileTransferSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrCertificateFileTransferSet.setStatus("mandatory")
_GenEquipSecurityCsrStatus_Type = FTStatus
_GenEquipSecurityCsrStatus_Object = MibScalar
genEquipSecurityCsrStatus = _GenEquipSecurityCsrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 2),
    _GenEquipSecurityCsrStatus_Type()
)
genEquipSecurityCsrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCsrStatus.setStatus("mandatory")
_GenEquipSecurityCsrCertificateGenerateAndUploadPercentage_Type = Integer32
_GenEquipSecurityCsrCertificateGenerateAndUploadPercentage_Object = MibScalar
genEquipSecurityCsrCertificateGenerateAndUploadPercentage = _GenEquipSecurityCsrCertificateGenerateAndUploadPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 3),
    _GenEquipSecurityCsrCertificateGenerateAndUploadPercentage_Type()
)
genEquipSecurityCsrCertificateGenerateAndUploadPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCsrCertificateGenerateAndUploadPercentage.setStatus("mandatory")
_GenEquipSecurityCertificateInstallSet_Type = OffOn
_GenEquipSecurityCertificateInstallSet_Object = MibScalar
genEquipSecurityCertificateInstallSet = _GenEquipSecurityCertificateInstallSet_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 4),
    _GenEquipSecurityCertificateInstallSet_Type()
)
genEquipSecurityCertificateInstallSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateInstallSet.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadStatus_Type = FTStatus
_GenEquipSecurityCertificateDownloadStatus_Object = MibScalar
genEquipSecurityCertificateDownloadStatus = _GenEquipSecurityCertificateDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 5),
    _GenEquipSecurityCertificateDownloadStatus_Type()
)
genEquipSecurityCertificateDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadStatus.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadPercentage_Type = Integer32
_GenEquipSecurityCertificateDownloadPercentage_Object = MibScalar
genEquipSecurityCertificateDownloadPercentage = _GenEquipSecurityCertificateDownloadPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 6),
    _GenEquipSecurityCertificateDownloadPercentage_Type()
)
genEquipSecurityCertificateDownloadPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadPercentage.setStatus("mandatory")
_GenEquipSecurityCsrAttributesTable_Object = MibTable
genEquipSecurityCsrAttributesTable = _GenEquipSecurityCsrAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10)
)
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesTable.setStatus("mandatory")
_GenEquipSecurityCsrAttributesEntry_Object = MibTableRow
genEquipSecurityCsrAttributesEntry = _GenEquipSecurityCsrAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1)
)
genEquipSecurityCsrAttributesEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityCsrAttributesIndex"),
)
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesEntry.setStatus("mandatory")
_GenEquipSecurityCsrAttributesIndex_Type = Integer32
_GenEquipSecurityCsrAttributesIndex_Object = MibTableColumn
genEquipSecurityCsrAttributesIndex = _GenEquipSecurityCsrAttributesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 1),
    _GenEquipSecurityCsrAttributesIndex_Type()
)
genEquipSecurityCsrAttributesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesIndex.setStatus("mandatory")
_GenEquipSecurityCsrAttributesCountry_Type = DisplayString
_GenEquipSecurityCsrAttributesCountry_Object = MibTableColumn
genEquipSecurityCsrAttributesCountry = _GenEquipSecurityCsrAttributesCountry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 2),
    _GenEquipSecurityCsrAttributesCountry_Type()
)
genEquipSecurityCsrAttributesCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesCountry.setStatus("mandatory")
_GenEquipSecurityCsrAttributesLocality_Type = DisplayString
_GenEquipSecurityCsrAttributesLocality_Object = MibTableColumn
genEquipSecurityCsrAttributesLocality = _GenEquipSecurityCsrAttributesLocality_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 3),
    _GenEquipSecurityCsrAttributesLocality_Type()
)
genEquipSecurityCsrAttributesLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesLocality.setStatus("mandatory")
_GenEquipSecurityCsrAttributesState_Type = DisplayString
_GenEquipSecurityCsrAttributesState_Object = MibTableColumn
genEquipSecurityCsrAttributesState = _GenEquipSecurityCsrAttributesState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 4),
    _GenEquipSecurityCsrAttributesState_Type()
)
genEquipSecurityCsrAttributesState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesState.setStatus("mandatory")
_GenEquipSecurityCsrAttributesOrganization_Type = DisplayString
_GenEquipSecurityCsrAttributesOrganization_Object = MibTableColumn
genEquipSecurityCsrAttributesOrganization = _GenEquipSecurityCsrAttributesOrganization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 5),
    _GenEquipSecurityCsrAttributesOrganization_Type()
)
genEquipSecurityCsrAttributesOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesOrganization.setStatus("mandatory")
_GenEquipSecurityCsrAttributesOu_Type = DisplayString
_GenEquipSecurityCsrAttributesOu_Object = MibTableColumn
genEquipSecurityCsrAttributesOu = _GenEquipSecurityCsrAttributesOu_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 6),
    _GenEquipSecurityCsrAttributesOu_Type()
)
genEquipSecurityCsrAttributesOu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesOu.setStatus("mandatory")
_GenEquipSecurityCsrAttributesCommonName_Type = DisplayString
_GenEquipSecurityCsrAttributesCommonName_Object = MibTableColumn
genEquipSecurityCsrAttributesCommonName = _GenEquipSecurityCsrAttributesCommonName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 7),
    _GenEquipSecurityCsrAttributesCommonName_Type()
)
genEquipSecurityCsrAttributesCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesCommonName.setStatus("mandatory")
_GenEquipSecurityCsrAttributesEmail_Type = DisplayString
_GenEquipSecurityCsrAttributesEmail_Object = MibTableColumn
genEquipSecurityCsrAttributesEmail = _GenEquipSecurityCsrAttributesEmail_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 8),
    _GenEquipSecurityCsrAttributesEmail_Type()
)
genEquipSecurityCsrAttributesEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesEmail.setStatus("mandatory")
_GenEquipSecurityCsrAttributesFileFormat_Type = CsrFileFormat
_GenEquipSecurityCsrAttributesFileFormat_Object = MibTableColumn
genEquipSecurityCsrAttributesFileFormat = _GenEquipSecurityCsrAttributesFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 10, 1, 9),
    _GenEquipSecurityCsrAttributesFileFormat_Type()
)
genEquipSecurityCsrAttributesFileFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCsrAttributesFileFormat.setStatus("mandatory")
_GenEquipSecurityCsrUploadConfigTable_Object = MibTable
genEquipSecurityCsrUploadConfigTable = _GenEquipSecurityCsrUploadConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11)
)
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigTable.setStatus("mandatory")
_GenEquipSecurityCsrUploadConfigEntry_Object = MibTableRow
genEquipSecurityCsrUploadConfigEntry = _GenEquipSecurityCsrUploadConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11, 1)
)
genEquipSecurityCsrUploadConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityCsrUploadConfigIndex"),
)
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigEntry.setStatus("mandatory")
_GenEquipSecurityCsrUploadConfigIndex_Type = Integer32
_GenEquipSecurityCsrUploadConfigIndex_Object = MibTableColumn
genEquipSecurityCsrUploadConfigIndex = _GenEquipSecurityCsrUploadConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11, 1, 1),
    _GenEquipSecurityCsrUploadConfigIndex_Type()
)
genEquipSecurityCsrUploadConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigIndex.setStatus("mandatory")
_GenEquipSecurityCsrUploadConfigIpv4Address_Type = IpAddress
_GenEquipSecurityCsrUploadConfigIpv4Address_Object = MibTableColumn
genEquipSecurityCsrUploadConfigIpv4Address = _GenEquipSecurityCsrUploadConfigIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11, 1, 2),
    _GenEquipSecurityCsrUploadConfigIpv4Address_Type()
)
genEquipSecurityCsrUploadConfigIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigIpv4Address.setStatus("mandatory")


class _GenEquipSecurityCsrUploadConfigIpV6Address_Type(OctetString):
    """Custom type genEquipSecurityCsrUploadConfigIpV6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipSecurityCsrUploadConfigIpV6Address_Type.__name__ = "OctetString"
_GenEquipSecurityCsrUploadConfigIpV6Address_Object = MibTableColumn
genEquipSecurityCsrUploadConfigIpV6Address = _GenEquipSecurityCsrUploadConfigIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11, 1, 3),
    _GenEquipSecurityCsrUploadConfigIpV6Address_Type()
)
genEquipSecurityCsrUploadConfigIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigIpV6Address.setStatus("mandatory")
_GenEquipSecurityCsrUploadConfigTableUsername_Type = DisplayString
_GenEquipSecurityCsrUploadConfigTableUsername_Object = MibTableColumn
genEquipSecurityCsrUploadConfigTableUsername = _GenEquipSecurityCsrUploadConfigTableUsername_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11, 1, 4),
    _GenEquipSecurityCsrUploadConfigTableUsername_Type()
)
genEquipSecurityCsrUploadConfigTableUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigTableUsername.setStatus("mandatory")
_GenEquipSecurityCsrUploadConfigPassword_Type = DisplayString
_GenEquipSecurityCsrUploadConfigPassword_Object = MibTableColumn
genEquipSecurityCsrUploadConfigPassword = _GenEquipSecurityCsrUploadConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11, 1, 5),
    _GenEquipSecurityCsrUploadConfigPassword_Type()
)
genEquipSecurityCsrUploadConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigPassword.setStatus("mandatory")
_GenEquipSecurityCsrUploadConfigPath_Type = DisplayString
_GenEquipSecurityCsrUploadConfigPath_Object = MibTableColumn
genEquipSecurityCsrUploadConfigPath = _GenEquipSecurityCsrUploadConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11, 1, 6),
    _GenEquipSecurityCsrUploadConfigPath_Type()
)
genEquipSecurityCsrUploadConfigPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigPath.setStatus("mandatory")
_GenEquipSecurityCsrUploadConfigFilename_Type = DisplayString
_GenEquipSecurityCsrUploadConfigFilename_Object = MibTableColumn
genEquipSecurityCsrUploadConfigFilename = _GenEquipSecurityCsrUploadConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 11, 1, 7),
    _GenEquipSecurityCsrUploadConfigFilename_Type()
)
genEquipSecurityCsrUploadConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCsrUploadConfigFilename.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadConfigTable_Object = MibTable
genEquipSecurityCertificateDownloadConfigTable = _GenEquipSecurityCertificateDownloadConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12)
)
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigTable.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadConfigEntry_Object = MibTableRow
genEquipSecurityCertificateDownloadConfigEntry = _GenEquipSecurityCertificateDownloadConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12, 1)
)
genEquipSecurityCertificateDownloadConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipSecurityCertificateDownloadConfigIndex"),
)
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigEntry.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadConfigIndex_Type = Integer32
_GenEquipSecurityCertificateDownloadConfigIndex_Object = MibTableColumn
genEquipSecurityCertificateDownloadConfigIndex = _GenEquipSecurityCertificateDownloadConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12, 1, 1),
    _GenEquipSecurityCertificateDownloadConfigIndex_Type()
)
genEquipSecurityCertificateDownloadConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigIndex.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadConfigIpv4Address_Type = IpAddress
_GenEquipSecurityCertificateDownloadConfigIpv4Address_Object = MibTableColumn
genEquipSecurityCertificateDownloadConfigIpv4Address = _GenEquipSecurityCertificateDownloadConfigIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12, 1, 2),
    _GenEquipSecurityCertificateDownloadConfigIpv4Address_Type()
)
genEquipSecurityCertificateDownloadConfigIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigIpv4Address.setStatus("mandatory")


class _GenEquipSecurityCertificateDownloadConfigIpV6Address_Type(OctetString):
    """Custom type genEquipSecurityCertificateDownloadConfigIpV6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipSecurityCertificateDownloadConfigIpV6Address_Type.__name__ = "OctetString"
_GenEquipSecurityCertificateDownloadConfigIpV6Address_Object = MibTableColumn
genEquipSecurityCertificateDownloadConfigIpV6Address = _GenEquipSecurityCertificateDownloadConfigIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12, 1, 3),
    _GenEquipSecurityCertificateDownloadConfigIpV6Address_Type()
)
genEquipSecurityCertificateDownloadConfigIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigIpV6Address.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadConfigUsername_Type = DisplayString
_GenEquipSecurityCertificateDownloadConfigUsername_Object = MibTableColumn
genEquipSecurityCertificateDownloadConfigUsername = _GenEquipSecurityCertificateDownloadConfigUsername_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12, 1, 4),
    _GenEquipSecurityCertificateDownloadConfigUsername_Type()
)
genEquipSecurityCertificateDownloadConfigUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigUsername.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadConfigPassword_Type = DisplayString
_GenEquipSecurityCertificateDownloadConfigPassword_Object = MibTableColumn
genEquipSecurityCertificateDownloadConfigPassword = _GenEquipSecurityCertificateDownloadConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12, 1, 5),
    _GenEquipSecurityCertificateDownloadConfigPassword_Type()
)
genEquipSecurityCertificateDownloadConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigPassword.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadConfigPath_Type = DisplayString
_GenEquipSecurityCertificateDownloadConfigPath_Object = MibTableColumn
genEquipSecurityCertificateDownloadConfigPath = _GenEquipSecurityCertificateDownloadConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12, 1, 6),
    _GenEquipSecurityCertificateDownloadConfigPath_Type()
)
genEquipSecurityCertificateDownloadConfigPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigPath.setStatus("mandatory")
_GenEquipSecurityCertificateDownloadConfigFilename_Type = DisplayString
_GenEquipSecurityCertificateDownloadConfigFilename_Object = MibTableColumn
genEquipSecurityCertificateDownloadConfigFilename = _GenEquipSecurityCertificateDownloadConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 9, 12, 1, 7),
    _GenEquipSecurityCertificateDownloadConfigFilename_Type()
)
genEquipSecurityCertificateDownloadConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityCertificateDownloadConfigFilename.setStatus("mandatory")
_GenEquipSecurityTrafficCrypto_ObjectIdentity = ObjectIdentity
genEquipSecurityTrafficCrypto = _GenEquipSecurityTrafficCrypto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10)
)
_GenEquipSecurityFipsAdmin_Type = EnableDisable
_GenEquipSecurityFipsAdmin_Object = MibScalar
genEquipSecurityFipsAdmin = _GenEquipSecurityFipsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 1),
    _GenEquipSecurityFipsAdmin_Type()
)
genEquipSecurityFipsAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipSecurityFipsAdmin.setStatus("mandatory")
_GenEquipSecurityFipsStatus_Type = DownUp
_GenEquipSecurityFipsStatus_Object = MibScalar
genEquipSecurityFipsStatus = _GenEquipSecurityFipsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 2),
    _GenEquipSecurityFipsStatus_Type()
)
genEquipSecurityFipsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipSecurityFipsStatus.setStatus("mandatory")
_GenEquipTrafficCryptoConfigTable_Object = MibTable
genEquipTrafficCryptoConfigTable = _GenEquipTrafficCryptoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10)
)
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigTable.setStatus("mandatory")
_GenEquipTrafficCryptoConfigEntry_Object = MibTableRow
genEquipTrafficCryptoConfigEntry = _GenEquipTrafficCryptoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10, 1)
)
genEquipTrafficCryptoConfigEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipTrafficCryptoConfigId"),
)
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigEntry.setStatus("mandatory")
_GenEquipTrafficCryptoConfigId_Type = Integer32
_GenEquipTrafficCryptoConfigId_Object = MibTableColumn
genEquipTrafficCryptoConfigId = _GenEquipTrafficCryptoConfigId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10, 1, 1),
    _GenEquipTrafficCryptoConfigId_Type()
)
genEquipTrafficCryptoConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigId.setStatus("mandatory")


class _GenEquipTrafficCryptoConfigConfigAdmin_Type(Integer32):
    """Custom type genEquipTrafficCryptoConfigConfigAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aes-256", 1),
          ("disable", 0))
    )


_GenEquipTrafficCryptoConfigConfigAdmin_Type.__name__ = "Integer32"
_GenEquipTrafficCryptoConfigConfigAdmin_Object = MibTableColumn
genEquipTrafficCryptoConfigConfigAdmin = _GenEquipTrafficCryptoConfigConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10, 1, 2),
    _GenEquipTrafficCryptoConfigConfigAdmin_Type()
)
genEquipTrafficCryptoConfigConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigConfigAdmin.setStatus("mandatory")
_GenEquipTrafficCryptoConfigMkey_Type = OctetString
_GenEquipTrafficCryptoConfigMkey_Object = MibTableColumn
genEquipTrafficCryptoConfigMkey = _GenEquipTrafficCryptoConfigMkey_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10, 1, 3),
    _GenEquipTrafficCryptoConfigMkey_Type()
)
genEquipTrafficCryptoConfigMkey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigMkey.setStatus("mandatory")
_GenEquipTrafficCryptoConfigBackupMkey_Type = OctetString
_GenEquipTrafficCryptoConfigBackupMkey_Object = MibTableColumn
genEquipTrafficCryptoConfigBackupMkey = _GenEquipTrafficCryptoConfigBackupMkey_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10, 1, 4),
    _GenEquipTrafficCryptoConfigBackupMkey_Type()
)
genEquipTrafficCryptoConfigBackupMkey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigBackupMkey.setStatus("mandatory")
_GenEquipTrafficCryptoConfigMkeyPeriod_Type = Integer32
_GenEquipTrafficCryptoConfigMkeyPeriod_Object = MibTableColumn
genEquipTrafficCryptoConfigMkeyPeriod = _GenEquipTrafficCryptoConfigMkeyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10, 1, 5),
    _GenEquipTrafficCryptoConfigMkeyPeriod_Type()
)
genEquipTrafficCryptoConfigMkeyPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigMkeyPeriod.setStatus("mandatory")


class _GenEquipTrafficCryptoConfigRandKeyGen_Type(Integer32):
    """Custom type genEquipTrafficCryptoConfigRandKeyGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("random-key-clear", 1),
          ("random-key-generate", 0))
    )


_GenEquipTrafficCryptoConfigRandKeyGen_Type.__name__ = "Integer32"
_GenEquipTrafficCryptoConfigRandKeyGen_Object = MibTableColumn
genEquipTrafficCryptoConfigRandKeyGen = _GenEquipTrafficCryptoConfigRandKeyGen_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10, 1, 6),
    _GenEquipTrafficCryptoConfigRandKeyGen_Type()
)
genEquipTrafficCryptoConfigRandKeyGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigRandKeyGen.setStatus("mandatory")
_GenEquipTrafficCryptoConfigSkeyPeriod_Type = Integer32
_GenEquipTrafficCryptoConfigSkeyPeriod_Object = MibTableColumn
genEquipTrafficCryptoConfigSkeyPeriod = _GenEquipTrafficCryptoConfigSkeyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 10, 1, 7),
    _GenEquipTrafficCryptoConfigSkeyPeriod_Type()
)
genEquipTrafficCryptoConfigSkeyPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoConfigSkeyPeriod.setStatus("mandatory")
_GenEquipTrafficCryptoStatusTable_Object = MibTable
genEquipTrafficCryptoStatusTable = _GenEquipTrafficCryptoStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 11)
)
if mibBuilder.loadTexts:
    genEquipTrafficCryptoStatusTable.setStatus("mandatory")
_GenEquipTrafficCryptoStatusEntry_Object = MibTableRow
genEquipTrafficCryptoStatusEntry = _GenEquipTrafficCryptoStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 11, 1)
)
genEquipTrafficCryptoStatusEntry.setIndexNames(
    (0, "MWRM-UNIT-MIB", "genEquipTrafficCryptoStatusId"),
)
if mibBuilder.loadTexts:
    genEquipTrafficCryptoStatusEntry.setStatus("mandatory")
_GenEquipTrafficCryptoStatusId_Type = Integer32
_GenEquipTrafficCryptoStatusId_Object = MibTableColumn
genEquipTrafficCryptoStatusId = _GenEquipTrafficCryptoStatusId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 11, 1, 1),
    _GenEquipTrafficCryptoStatusId_Type()
)
genEquipTrafficCryptoStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoStatusId.setStatus("mandatory")


class _GenEquipTrafficCryptoStatusValid_Type(Integer32):
    """Custom type genEquipTrafficCryptoStatusValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", 0),
          ("valid", 1))
    )


_GenEquipTrafficCryptoStatusValid_Type.__name__ = "Integer32"
_GenEquipTrafficCryptoStatusValid_Object = MibTableColumn
genEquipTrafficCryptoStatusValid = _GenEquipTrafficCryptoStatusValid_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 11, 1, 2),
    _GenEquipTrafficCryptoStatusValid_Type()
)
genEquipTrafficCryptoStatusValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoStatusValid.setStatus("mandatory")
_GenEquipTrafficCryptoStatusMkeyTimeExpire_Type = Integer32
_GenEquipTrafficCryptoStatusMkeyTimeExpire_Object = MibTableColumn
genEquipTrafficCryptoStatusMkeyTimeExpire = _GenEquipTrafficCryptoStatusMkeyTimeExpire_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 11, 10, 11, 1, 3),
    _GenEquipTrafficCryptoStatusMkeyTimeExpire_Type()
)
genEquipTrafficCryptoStatusMkeyTimeExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipTrafficCryptoStatusMkeyTimeExpire.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MWRM-UNIT-MIB",
    **{"EnableDisable": EnableDisable,
       "EnableDisableSMI2": EnableDisableSMI2,
       "OffOn": OffOn,
       "MetricImperial": MetricImperial,
       "AllowedNotAllowed": AllowedNotAllowed,
       "NoYes": NoYes,
       "DownUp": DownUp,
       "SupportedNotsupported": SupportedNotsupported,
       "ProgressStatus": ProgressStatus,
       "Severity": Severity,
       "TrailIfType": TrailIfType,
       "PmTableType": PmTableType,
       "RateMbps": RateMbps,
       "HalfFull": HalfFull,
       "BerLevel": BerLevel,
       "SignalLevel": SignalLevel,
       "Exponent": Exponent,
       "LoopbackType": LoopbackType,
       "QueueName": QueueName,
       "RadioId": RadioId,
       "RfuId": RfuId,
       "SwCommand": SwCommand,
       "TrailProtectedType": TrailProtectedType,
       "ClockSrc": ClockSrc,
       "SlotId": SlotId,
       "Integrity": Integrity,
       "GreenYellow": GreenYellow,
       "InputSeverity": InputSeverity,
       "SwCommandTimer": SwCommandTimer,
       "FileTransferStatus": FileTransferStatus,
       "FileRestoreStatus": FileRestoreStatus,
       "RbacAccessLevel": RbacAccessLevel,
       "InventoryCardType": InventoryCardType,
       "FtpProtocolType": FtpProtocolType,
       "CfgUnitInfoOper": CfgUnitInfoOper,
       "CfgOper": CfgOper,
       "CardOccupancy": CardOccupancy,
       "OperState": OperState,
       "LicenseGeneric": LicenseGeneric,
       "RaduisAcceaaLevel": RaduisAcceaaLevel,
       "VmResetType": VmResetType,
       "FTStatus": FTStatus,
       "CsrCertificateFTState": CsrCertificateFTState,
       "CsrFileFormat": CsrFileFormat,
       "microwave-radio": microwave_radio,
       "genEquip": genEquip,
       "genEquipUnit": genEquipUnit,
       "genEquipUnitInfo": genEquipUnitInfo,
       "genEquipLastCfgTimeStamp": genEquipLastCfgTimeStamp,
       "genEquipRealTimeandDate": genEquipRealTimeandDate,
       "genEquipPMGenTime": genEquipPMGenTime,
       "genEquipInvGenTime": genEquipInvGenTime,
       "genEquipOperation": genEquipOperation,
       "genEquipMIBVersion": genEquipMIBVersion,
       "genEquipUnitCLLI": genEquipUnitCLLI,
       "genEquipUnitMeasurementSystem": genEquipUnitMeasurementSystem,
       "genEquipUnitIduTemperature": genEquipUnitIduTemperature,
       "genEquipUnitIduVoltageInput": genEquipUnitIduVoltageInput,
       "genEquipUnitInfoTime": genEquipUnitInfoTime,
       "genEquipUnitGMTHours": genEquipUnitGMTHours,
       "genEquipUnitGMTMins": genEquipUnitGMTMins,
       "genEquipUnitInfoNTP": genEquipUnitInfoNTP,
       "genEquipUnitInfoNTPAdmin": genEquipUnitInfoNTPAdmin,
       "genEquipUnitInfoNTPServerIP": genEquipUnitInfoNTPServerIP,
       "genEquipUnitInfoNTPStatus": genEquipUnitInfoNTPStatus,
       "genEquipUnitInfoNTPSync": genEquipUnitInfoNTPSync,
       "genEquipUnitInfoNTPPollInterval": genEquipUnitInfoNTPPollInterval,
       "genEquipUnitInfoNtpStatusTable": genEquipUnitInfoNtpStatusTable,
       "genEquipUnitInfoNtpStatusEntry": genEquipUnitInfoNtpStatusEntry,
       "genEquipUnitInfoNtpStatusIndex": genEquipUnitInfoNtpStatusIndex,
       "genEquipUnitInfoNtpStatusPollInterval": genEquipUnitInfoNtpStatusPollInterval,
       "genEquipUnitInfoNtpStatusSyncServerIP": genEquipUnitInfoNtpStatusSyncServerIP,
       "genEquipUnitInfoNtpStatusLockState": genEquipUnitInfoNtpStatusLockState,
       "genEquipUnitInfoNtpConfigTable": genEquipUnitInfoNtpConfigTable,
       "genEquipUnitInfoNtpConfigEntry": genEquipUnitInfoNtpConfigEntry,
       "genEquipUnitInfoNtpConfigIndex": genEquipUnitInfoNtpConfigIndex,
       "genEquipUnitInfoNtpConfigAdmin": genEquipUnitInfoNtpConfigAdmin,
       "genEquipUnitInfoNtpConfigVersion": genEquipUnitInfoNtpConfigVersion,
       "genEquipUnitInfoNtpConfigServerIPaddress1": genEquipUnitInfoNtpConfigServerIPaddress1,
       "genEquipUnitInfoNtpConfigServerIPaddress2": genEquipUnitInfoNtpConfigServerIPaddress2,
       "genEquipUnitDaylightSavingTimeStartMonth": genEquipUnitDaylightSavingTimeStartMonth,
       "genEquipUnitDaylightSavingTimeStartDay": genEquipUnitDaylightSavingTimeStartDay,
       "genEquipUnitDaylightSavingTimeEndMonth": genEquipUnitDaylightSavingTimeEndMonth,
       "genEquipUnitDaylightSavingTimeEndDay": genEquipUnitDaylightSavingTimeEndDay,
       "genEquipUnitDaylightSavingTimeOffset": genEquipUnitDaylightSavingTimeOffset,
       "genEquipUnitInfoTimeServicesTable": genEquipUnitInfoTimeServicesTable,
       "genEquipUnitInfoTimeServicesEntry": genEquipUnitInfoTimeServicesEntry,
       "genEquipUnitInfoTimeServicesIndex": genEquipUnitInfoTimeServicesIndex,
       "genEquipUnitInfoTimeServicesUtcHours": genEquipUnitInfoTimeServicesUtcHours,
       "genEquipUnitInfoTimeServicesUtcMinutes": genEquipUnitInfoTimeServicesUtcMinutes,
       "genEquipUnitInfoTimeServicesDstStartMonth": genEquipUnitInfoTimeServicesDstStartMonth,
       "genEquipUnitInfoTimeServicesDstStartDay": genEquipUnitInfoTimeServicesDstStartDay,
       "genEquipUnitInfoTimeServicesDstEndMonth": genEquipUnitInfoTimeServicesDstEndMonth,
       "genEquipUnitInfoTimeServicesDstEndDay": genEquipUnitInfoTimeServicesDstEndDay,
       "genEquipUnitInfoTimeServicesDstOffset": genEquipUnitInfoTimeServicesDstOffset,
       "genEquipUnitInfoTimeServicesUtcDateAndTime": genEquipUnitInfoTimeServicesUtcDateAndTime,
       "genEquipUnitInfoTimeServicesUtcCurrentDateAndTime": genEquipUnitInfoTimeServicesUtcCurrentDateAndTime,
       "genEquipUnitIduPowerSupply1AlarmAdmin": genEquipUnitIduPowerSupply1AlarmAdmin,
       "genEquipUnitIduPowerSupply2AlarmAdmin": genEquipUnitIduPowerSupply2AlarmAdmin,
       "genEquipUnitInfoNG": genEquipUnitInfoNG,
       "genEquipUnitName": genEquipUnitName,
       "genEquipUnitDescription": genEquipUnitDescription,
       "genEquipUnitContactPerson": genEquipUnitContactPerson,
       "genEquipUnitLocation": genEquipUnitLocation,
       "genEquipUnitLatitude": genEquipUnitLatitude,
       "genEquipUnitLongitude": genEquipUnitLongitude,
       "genEquipUnitIpAddressType": genEquipUnitIpAddressType,
       "genEquipUnitInfoNGTdmInterfaceStandard": genEquipUnitInfoNGTdmInterfaceStandard,
       "genEquipUnitInventory": genEquipUnitInventory,
       "genEquipUnitIDUSerialNumber": genEquipUnitIDUSerialNumber,
       "genEquipUnitIDUPartNumber": genEquipUnitIDUPartNumber,
       "genEquipUnitInventoryNG": genEquipUnitInventoryNG,
       "genEquipInventoryTable": genEquipInventoryTable,
       "genEquipInventoryEntry": genEquipInventoryEntry,
       "genEquipInventorySlotIndex": genEquipInventorySlotIndex,
       "genEquipInventoryCardName": genEquipInventoryCardName,
       "genEquipInventoryCardType": genEquipInventoryCardType,
       "genEquipInventoryCardSubType": genEquipInventoryCardSubType,
       "genEquipInventoryPartNumber": genEquipInventoryPartNumber,
       "genEquipInventorySerialNumber": genEquipInventorySerialNumber,
       "genEquipInventoryNumberWorkingDays": genEquipInventoryNumberWorkingDays,
       "genEquipUnitLicenseInfo": genEquipUnitLicenseInfo,
       "genEquipUnitLicenseType": genEquipUnitLicenseType,
       "genEquipUnitLicenseCode": genEquipUnitLicenseCode,
       "genEquipUnitACMLicense": genEquipUnitACMLicense,
       "genEquipUnitSwitchAppLicense": genEquipUnitSwitchAppLicense,
       "genEquipUnitCapacityLicense": genEquipUnitCapacityLicense,
       "genEquipUnitLicenseDemoAdmin": genEquipUnitLicenseDemoAdmin,
       "genEquipUnitLicenseDemoTimer": genEquipUnitLicenseDemoTimer,
       "genEquipUnitLicenseSyncU": genEquipUnitLicenseSyncU,
       "genEquipUnitLicenseNetworkResiliency": genEquipUnitLicenseNetworkResiliency,
       "genEquipUnitLicenseTDMCapacity": genEquipUnitLicenseTDMCapacity,
       "genEquipUnitLicenseTDMCapacityValue": genEquipUnitLicenseTDMCapacityValue,
       "genEquipUnitLicensePerUsage": genEquipUnitLicensePerUsage,
       "genEquipUnitLicenseAsymScripts": genEquipUnitLicenseAsymScripts,
       "genEquipUnitLicenseDateCode": genEquipUnitLicenseDateCode,
       "genEquipUnitLicenseValidationNumber": genEquipUnitLicenseValidationNumber,
       "genEquipUnitLicenseFeatureTable": genEquipUnitLicenseFeatureTable,
       "genEquipUnitLicenseFeatureEntry": genEquipUnitLicenseFeatureEntry,
       "genEquipUnitLicenseFeatureId": genEquipUnitLicenseFeatureId,
       "genEquipUnitLicenseFeatureName": genEquipUnitLicenseFeatureName,
       "genEquipUnitLicenseFeatureDescription": genEquipUnitLicenseFeatureDescription,
       "genEquipUnitLicenseFeatureIsUsed": genEquipUnitLicenseFeatureIsUsed,
       "genEquipUnitLicenseFeatureIsAllowed": genEquipUnitLicenseFeatureIsAllowed,
       "genEquipUnitLicenseViolationStatus": genEquipUnitLicenseViolationStatus,
       "genEquipUnitLicenseCutThrough": genEquipUnitLicenseCutThrough,
       "genEquipUnitLicenseTdmInterfaceStandard": genEquipUnitLicenseTdmInterfaceStandard,
       "genEquipUnitExternalAlarms": genEquipUnitExternalAlarms,
       "genEquipUnitAlarmInput": genEquipUnitAlarmInput,
       "genEquipUnitAlarmInputTable": genEquipUnitAlarmInputTable,
       "genEquipUnitAlarmInputEntry": genEquipUnitAlarmInputEntry,
       "genEquipUnitAlarmInputCounter": genEquipUnitAlarmInputCounter,
       "genEquipUnitAlarmInputAdmin": genEquipUnitAlarmInputAdmin,
       "genEquipUnitAlarmInputText": genEquipUnitAlarmInputText,
       "genEquipUnitAlarmInputSeverity": genEquipUnitAlarmInputSeverity,
       "genEquipUnitAlarmInputState": genEquipUnitAlarmInputState,
       "genEquipUnitAlarmOutput": genEquipUnitAlarmOutput,
       "genEquipUnitAlarmOutputTable": genEquipUnitAlarmOutputTable,
       "genEquipUnitAlarmOutputEntry": genEquipUnitAlarmOutputEntry,
       "genEquipUnitAlarmOutputCounter": genEquipUnitAlarmOutputCounter,
       "genEquipUnitAlarmOutputAdmin": genEquipUnitAlarmOutputAdmin,
       "genEquipUnitAlarmOutputStatus": genEquipUnitAlarmOutputStatus,
       "genEquipUnitAlarmOutputGroup": genEquipUnitAlarmOutputGroup,
       "genEquipUnitShelf": genEquipUnitShelf,
       "genEquipUnitShelfInstallation": genEquipUnitShelfInstallation,
       "genEquipUnitShelfModuleRole": genEquipUnitShelfModuleRole,
       "genEquipUnitShelfSlotLabel": genEquipUnitShelfSlotLabel,
       "genEquipUnitShelfArchivesOperationStatus": genEquipUnitShelfArchivesOperationStatus,
       "genEquipUnitShelfManagmentTable": genEquipUnitShelfManagmentTable,
       "genEquipUnitShelfManagmentEntry": genEquipUnitShelfManagmentEntry,
       "genEquipUnitShelfManagmentSlot": genEquipUnitShelfManagmentSlot,
       "genEquipUnitShelfManagmentSlotPopulation": genEquipUnitShelfManagmentSlotPopulation,
       "genEquipUnitShelfManagmentCommunicationStatus": genEquipUnitShelfManagmentCommunicationStatus,
       "genEquipUnitShelfManagmentSlotMostSevereAlarm": genEquipUnitShelfManagmentSlotMostSevereAlarm,
       "genEquipUnitShelfManagmentMngSwCommand": genEquipUnitShelfManagmentMngSwCommand,
       "genEquipUnitShelfManagmentSlotReset": genEquipUnitShelfManagmentSlotReset,
       "genEquipUnitShelfManagmentSlotIp": genEquipUnitShelfManagmentSlotIp,
       "genEquipUnitShelfReset": genEquipUnitShelfReset,
       "genEquipUnitshelfAllODUAdmin": genEquipUnitshelfAllODUAdmin,
       "genEquipUnitShelfSlotConfigTable": genEquipUnitShelfSlotConfigTable,
       "genEquipUnitShelfSlotConfigEntry": genEquipUnitShelfSlotConfigEntry,
       "genEquipUnitShelfSlotConfigSlotID": genEquipUnitShelfSlotConfigSlotID,
       "genEquipUnitShelfSlotConfigExpectedCardType": genEquipUnitShelfSlotConfigExpectedCardType,
       "genEquipUnitShelfSlotConfigLabel": genEquipUnitShelfSlotConfigLabel,
       "genEquipUnitShelfSlotConfigAdmin": genEquipUnitShelfSlotConfigAdmin,
       "genEquipUnitShelfSlotConfigSlotReset": genEquipUnitShelfSlotConfigSlotReset,
       "genEquipUnitShelfTccConfigTable": genEquipUnitShelfTccConfigTable,
       "genEquipUnitShelfTccConfigEntry": genEquipUnitShelfTccConfigEntry,
       "genEquipUnitShelfTccConfigSlotID": genEquipUnitShelfTccConfigSlotID,
       "genEquipUnitShelfTccConfigExpectedCardType": genEquipUnitShelfTccConfigExpectedCardType,
       "genEquipUnitShelfTccConfigLabel": genEquipUnitShelfTccConfigLabel,
       "genEquipUnitShelfTccConfigAdmin": genEquipUnitShelfTccConfigAdmin,
       "genEquipUnitShelfTccConfigReset": genEquipUnitShelfTccConfigReset,
       "genEquipUnitShelfSlotStatusTable": genEquipUnitShelfSlotStatusTable,
       "genEquipUnitShelfSlotStatusEntry": genEquipUnitShelfSlotStatusEntry,
       "genEquipUnitShelfSlotStatusSlotID": genEquipUnitShelfSlotStatusSlotID,
       "genEquipUnitShelfSlotStatusOccupancy": genEquipUnitShelfSlotStatusOccupancy,
       "genEquipUnitShelfSlotStatusAllowedCardTypes": genEquipUnitShelfSlotStatusAllowedCardTypes,
       "genEquipUnitShelfSlotStatusCardType": genEquipUnitShelfSlotStatusCardType,
       "genEquipUnitShelfSlotStatusOperationalState": genEquipUnitShelfSlotStatusOperationalState,
       "genEquipUnitShelfSlotStatusCommunication": genEquipUnitShelfSlotStatusCommunication,
       "genEquipUnitShelfTccStatusTable": genEquipUnitShelfTccStatusTable,
       "genEquipUnitShelfTccStatusEntry": genEquipUnitShelfTccStatusEntry,
       "genEquipUnitShelfTccStatusSlotID": genEquipUnitShelfTccStatusSlotID,
       "genEquipUnitShelfTccStatusOccupancy": genEquipUnitShelfTccStatusOccupancy,
       "genEquipUnitShelfTccStatusAllowedCardTypes": genEquipUnitShelfTccStatusAllowedCardTypes,
       "genEquipUnitShelfTccStatusCardType": genEquipUnitShelfTccStatusCardType,
       "genEquipUnitShelfTccStatusOperationalState": genEquipUnitShelfTccStatusOperationalState,
       "genEquipUnitShelfTccStatusCommunication": genEquipUnitShelfTccStatusCommunication,
       "genEquipUnitShelfManagmentSeverityTable": genEquipUnitShelfManagmentSeverityTable,
       "genEquipUnitShelfManagmentSeverityEntry": genEquipUnitShelfManagmentSeverityEntry,
       "genEquipUnitShelfManagmentSeveritySlot": genEquipUnitShelfManagmentSeveritySlot,
       "genEquipUnitShelfManagmentSeverityCritical": genEquipUnitShelfManagmentSeverityCritical,
       "genEquipUnitShelfManagmentSeverityMajor": genEquipUnitShelfManagmentSeverityMajor,
       "genEquipUnitShelfManagmentSeverityMinor": genEquipUnitShelfManagmentSeverityMinor,
       "genEquipUnitShelfManagmentSeverityWarning": genEquipUnitShelfManagmentSeverityWarning,
       "genEquipUnitShelfManagmentSeverityIndeterminate": genEquipUnitShelfManagmentSeverityIndeterminate,
       "genEquipUnitShelfPdcFanStatusTable": genEquipUnitShelfPdcFanStatusTable,
       "genEquipUnitShelfPdcFanStatusEntry": genEquipUnitShelfPdcFanStatusEntry,
       "genEquipUnitShelfPdcFanStatusPdcFanId": genEquipUnitShelfPdcFanStatusPdcFanId,
       "genEquipUnitShelfPdcFanStatusPdcFanExMonitor": genEquipUnitShelfPdcFanStatusPdcFanExMonitor,
       "genEquipUnitShelfPdcFanStatusPdcFanOccupancy": genEquipUnitShelfPdcFanStatusPdcFanOccupancy,
       "genEquipUnitShelfPdcFanStatusPdcFanCardType": genEquipUnitShelfPdcFanStatusPdcFanCardType,
       "genEquipUnitShelfAbcMuxTable": genEquipUnitShelfAbcMuxTable,
       "genEquipUnitShelfAbcMuxEntry": genEquipUnitShelfAbcMuxEntry,
       "genEquipUnitShelfAbcMuxNumber": genEquipUnitShelfAbcMuxNumber,
       "genEquipUnitShelfAbcMuxAdmin": genEquipUnitShelfAbcMuxAdmin,
       "genEquipUnitShelfMultiplexTrafficSource": genEquipUnitShelfMultiplexTrafficSource,
       "genEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed": genEquipUnitShelfMaskUnderVoltageAlarmFirstPowerFeed,
       "genEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed": genEquipUnitShelfMaskUnderVoltageAlarmSecondPowerFeed,
       "genEquipProtection": genEquipProtection,
       "genEquipProtectionAdmin": genEquipProtectionAdmin,
       "genEquipProtectionMode": genEquipProtectionMode,
       "genEquipProtectionMateIPAddr": genEquipProtectionMateIPAddr,
       "genEquipProtectionMateMACAddr": genEquipProtectionMateMACAddr,
       "genEquipProtectionRadioExcessiveBERSwitch": genEquipProtectionRadioExcessiveBERSwitch,
       "genEquipProtectionLockout": genEquipProtectionLockout,
       "genEquipProtectionForceSwitch": genEquipProtectionForceSwitch,
       "genEquipProtectionManualSwitch": genEquipProtectionManualSwitch,
       "genEquipProtectionCopyToMateComand": genEquipProtectionCopyToMateComand,
       "genEquipProtectionCopyToMateStatus": genEquipProtectionCopyToMateStatus,
       "genEquipProtectionMultiUnitLAGAdmin": genEquipProtectionMultiUnitLAGAdmin,
       "genEquipProtectionRevertiveAdmin": genEquipProtectionRevertiveAdmin,
       "genEquipProtectionRevertivePrimaryIDU": genEquipProtectionRevertivePrimaryIDU,
       "genEquipProtectionRevertiveMinTimer": genEquipProtectionRevertiveMinTimer,
       "genEquipProtectionRevertiveMaxNumOfTries": genEquipProtectionRevertiveMaxNumOfTries,
       "genEquipProtectionRevertiveTimerMultiplier": genEquipProtectionRevertiveTimerMultiplier,
       "genEquipProtectionAspRevertive": genEquipProtectionAspRevertive,
       "genEquipDiversity": genEquipDiversity,
       "genEquipDiversityType": genEquipDiversityType,
       "genEquipDiversityRevertiveMode": genEquipDiversityRevertiveMode,
       "genEquipDiversityPrimaryRadio": genEquipDiversityPrimaryRadio,
       "genEquipDiversityRevertiveTimer": genEquipDiversityRevertiveTimer,
       "genEquipDiversityForceActive": genEquipDiversityForceActive,
       "genEquipDiversitySwitchCounter": genEquipDiversitySwitchCounter,
       "genEquipDiversitySwitchCounterClear": genEquipDiversitySwitchCounterClear,
       "genEquipDiversityReceiveRadio": genEquipDiversityReceiveRadio,
       "genEquipFault": genEquipFault,
       "genEquipCurrentAlarm": genEquipCurrentAlarm,
       "genEquipCurrentAlarmLastChangeCounter": genEquipCurrentAlarmLastChangeCounter,
       "genEquipCurrentAlarmTable": genEquipCurrentAlarmTable,
       "genEquipCurrentAlarmEntry": genEquipCurrentAlarmEntry,
       "genEquipCurrentAlarmCounter": genEquipCurrentAlarmCounter,
       "genEquipCurrentAlarmRaisedTimeT": genEquipCurrentAlarmRaisedTimeT,
       "genEquipCurrentAlarmId": genEquipCurrentAlarmId,
       "genEquipCurrentAlarmName": genEquipCurrentAlarmName,
       "genEquipCurrentAlarmInstance": genEquipCurrentAlarmInstance,
       "genEquipCurrentAlarmSeverity": genEquipCurrentAlarmSeverity,
       "genEquipCurrentAlarmIfIndex": genEquipCurrentAlarmIfIndex,
       "genEquipCurrentAlarmModule": genEquipCurrentAlarmModule,
       "genEquipCurrentAlarmDesc": genEquipCurrentAlarmDesc,
       "genEquipCurrentAlarmProbableCause": genEquipCurrentAlarmProbableCause,
       "genEquipCurrentAlarmCorrectiveActions": genEquipCurrentAlarmCorrectiveActions,
       "genEquipCurrentAlarmState": genEquipCurrentAlarmState,
       "genEquipCurrentAlarmSlotId": genEquipCurrentAlarmSlotId,
       "genEquipCurrentAlarmAdditionalInfo": genEquipCurrentAlarmAdditionalInfo,
       "genEquipCurrentAlarmUserText": genEquipCurrentAlarmUserText,
       "genEquipMostSevereAlarm": genEquipMostSevereAlarm,
       "genEquipAlarmConfigDefault": genEquipAlarmConfigDefault,
       "genEquipAlarmConfigTable": genEquipAlarmConfigTable,
       "genEquipAlarmConfigEntry": genEquipAlarmConfigEntry,
       "genEquipAlarmConfigId": genEquipAlarmConfigId,
       "genEquipAlarmConfigSeverity": genEquipAlarmConfigSeverity,
       "genEquipAlarmConfigDescr": genEquipAlarmConfigDescr,
       "genEquipAlarmConfigAdditionalText": genEquipAlarmConfigAdditionalText,
       "genEquipAlarmServiceAffect": genEquipAlarmServiceAffect,
       "genEquipTrapCfg": genEquipTrapCfg,
       "genEquipTrapCfgMgrTable": genEquipTrapCfgMgrTable,
       "genEquipTrapCfgMgrEntry": genEquipTrapCfgMgrEntry,
       "genEquipTrapCfgMgrId": genEquipTrapCfgMgrId,
       "genEquipTrapCfgMgrAdmin": genEquipTrapCfgMgrAdmin,
       "genEquipTrapCfgMgrIP": genEquipTrapCfgMgrIP,
       "genEquipTrapCfgMgrPort": genEquipTrapCfgMgrPort,
       "genEquipTrapCfgMgrName": genEquipTrapCfgMgrName,
       "genEquipTrapCfgMgrCommunity": genEquipTrapCfgMgrCommunity,
       "genEquipTrapCfgMgrSeverityFilter": genEquipTrapCfgMgrSeverityFilter,
       "genEquipTrapCfgMgrStatusChangeFilter": genEquipTrapCfgMgrStatusChangeFilter,
       "genEquipTrapCfgMgrCLLI": genEquipTrapCfgMgrCLLI,
       "genEquipTrapCfgMgrHeartbeatPeriod": genEquipTrapCfgMgrHeartbeatPeriod,
       "genEquipTrapCfgMgrIPv6": genEquipTrapCfgMgrIPv6,
       "genEquipTrapCfgMgrV3User": genEquipTrapCfgMgrV3User,
       "genEquipEventLog": genEquipEventLog,
       "genEquipEventLogTable": genEquipEventLogTable,
       "genEquipEventLogEntry": genEquipEventLogEntry,
       "genEquipEventLogCounter": genEquipEventLogCounter,
       "genEquipEventLogRaisedTimeT": genEquipEventLogRaisedTimeT,
       "genEquipEventLogSeverity": genEquipEventLogSeverity,
       "genEquipEventLogModule": genEquipEventLogModule,
       "genEquipEventLogDesc": genEquipEventLogDesc,
       "genEquipEventLogState": genEquipEventLogState,
       "genEquipEventLogProbableCause": genEquipEventLogProbableCause,
       "genEquipEventLogCorrectiveActions": genEquipEventLogCorrectiveActions,
       "genEquipEventLogAdditionalInfo": genEquipEventLogAdditionalInfo,
       "genEquipEventLogUserText": genEquipEventLogUserText,
       "genEquipEventLogIfIndex": genEquipEventLogIfIndex,
       "genEquipEventLogId": genEquipEventLogId,
       "genEquipEventLogClear": genEquipEventLogClear,
       "genEquipEventLogLastChangeCounter": genEquipEventLogLastChangeCounter,
       "genEquipFaultErrno": genEquipFaultErrno,
       "genEquipFaultErrDescr": genEquipFaultErrDescr,
       "genEquipMng": genEquipMng,
       "genEquipMngSw": genEquipMngSw,
       "genEquipMngSwServerUrl": genEquipMngSwServerUrl,
       "genEquipMngSwServerLogin": genEquipMngSwServerLogin,
       "genEquipMngSwServerPassword": genEquipMngSwServerPassword,
       "genEquipMngSwProxyUrl": genEquipMngSwProxyUrl,
       "genEquipMngSwProxyLogin": genEquipMngSwProxyLogin,
       "genEquipMngSwProxyPassword": genEquipMngSwProxyPassword,
       "genEquipMngSwDownloadStatus": genEquipMngSwDownloadStatus,
       "genEquipMngSwInstallStatus": genEquipMngSwInstallStatus,
       "genEquipMngSwCommand": genEquipMngSwCommand,
       "genEquipMngSwInstalledIduVersion": genEquipMngSwInstalledIduVersion,
       "genEquipMngSwInstalledRfuVersion": genEquipMngSwInstalledRfuVersion,
       "genEquipMngSwVersions": genEquipMngSwVersions,
       "genEquipMngSwIDUVersionsTable": genEquipMngSwIDUVersionsTable,
       "genEquipMngSwIDUVersionsEntry": genEquipMngSwIDUVersionsEntry,
       "genEquipMngSwIDUVersionsCounter": genEquipMngSwIDUVersionsCounter,
       "genEquipMngSwIDUVersionsPackageName": genEquipMngSwIDUVersionsPackageName,
       "genEquipMngSwIDUVersionsTargetDevice": genEquipMngSwIDUVersionsTargetDevice,
       "genEquipMngSwIDUVersionsRunningVersion": genEquipMngSwIDUVersionsRunningVersion,
       "genEquipMngSwIDUVersionsInstalledVersion": genEquipMngSwIDUVersionsInstalledVersion,
       "genEquipMngSwIDUVersionsUpgradePackage": genEquipMngSwIDUVersionsUpgradePackage,
       "genEquipMngSwIDUVersionsDowngradePackage": genEquipMngSwIDUVersionsDowngradePackage,
       "genEquipMngSwIDUVersionsResetType": genEquipMngSwIDUVersionsResetType,
       "genEquipMngSwTimerTable": genEquipMngSwTimerTable,
       "genEquipMngSwTimerEntry": genEquipMngSwTimerEntry,
       "genEquipMngSwTimerSlotNumber": genEquipMngSwTimerSlotNumber,
       "genEquipMngSwTimerInstallationTimer": genEquipMngSwTimerInstallationTimer,
       "genEquipMngSwTimerTimeToInstall": genEquipMngSwTimerTimeToInstall,
       "genEquipMngSwTimerTimerAbort": genEquipMngSwTimerTimerAbort,
       "genEquipMngSwFTPTimer": genEquipMngSwFTPTimer,
       "genEquipMngSwInstallationTimer": genEquipMngSwInstallationTimer,
       "genEquipMngSwTimeToInstall": genEquipMngSwTimeToInstall,
       "genEquipMngSwUpgradeCommonRfuVersion": genEquipMngSwUpgradeCommonRfuVersion,
       "genEquipMngSwDowngradeCommonRfuVersion": genEquipMngSwDowngradeCommonRfuVersion,
       "genEquipMngSwFileTransferTable": genEquipMngSwFileTransferTable,
       "genEquipMngSwFileTransferEntry": genEquipMngSwFileTransferEntry,
       "genEquipMngSwFileTransferIndex": genEquipMngSwFileTransferIndex,
       "genEquipMngSwFileTransferProtocol": genEquipMngSwFileTransferProtocol,
       "genEquipMngSwFileTransferUserName": genEquipMngSwFileTransferUserName,
       "genEquipMngSwFileTransferPassword": genEquipMngSwFileTransferPassword,
       "genEquipMngSwFileTransferAddress": genEquipMngSwFileTransferAddress,
       "genEquipMngSwFileTransferPath": genEquipMngSwFileTransferPath,
       "genEquipMngSwFileTransferIpv6Address": genEquipMngSwFileTransferIpv6Address,
       "genEquipMngSwFileTransferStatusTable": genEquipMngSwFileTransferStatusTable,
       "genEquipMngSwFileTransferStatusEntry": genEquipMngSwFileTransferStatusEntry,
       "genEquipMngSwFileTransferStatusIndex": genEquipMngSwFileTransferStatusIndex,
       "genEquipMngSwFileTransferStatusResult": genEquipMngSwFileTransferStatusResult,
       "genEquipMngSwFileTransferPercentageDone": genEquipMngSwFileTransferPercentageDone,
       "genEquipMngSwFileTransferPercentageDoneStandBy": genEquipMngSwFileTransferPercentageDoneStandBy,
       "genEquipMngSwFileTransferStatusResultStandBy": genEquipMngSwFileTransferStatusResultStandBy,
       "genEquipMngSwInstallStatusTable": genEquipMngSwInstallStatusTable,
       "genEquipMngSwInstallStatusEntry": genEquipMngSwInstallStatusEntry,
       "genEquipMngSwInstallStatusIndex": genEquipMngSwInstallStatusIndex,
       "genEquipMngSwInstallStatusResult": genEquipMngSwInstallStatusResult,
       "genEquipMngSwInstallPercentageDone": genEquipMngSwInstallPercentageDone,
       "genEquipMngSwInstallStatusResultStandBy": genEquipMngSwInstallStatusResultStandBy,
       "genEquipMngSwInstallPercentageDoneStandBy": genEquipMngSwInstallPercentageDoneStandBy,
       "genEquipMngSwOperationTable": genEquipMngSwOperationTable,
       "genEquipMngSwOperationEntry": genEquipMngSwOperationEntry,
       "genEquipMngSwOperationIndex": genEquipMngSwOperationIndex,
       "genEquipMngSwOperationOperation": genEquipMngSwOperationOperation,
       "genEquipMngSwOperationTimedInstallation": genEquipMngSwOperationTimedInstallation,
       "genEquipMngSwSlotRunningVersionTable": genEquipMngSwSlotRunningVersionTable,
       "genEquipMngSwSlotRunningVersionEntry": genEquipMngSwSlotRunningVersionEntry,
       "genEquipMngSwSlotRunningVersionSlotId": genEquipMngSwSlotRunningVersionSlotId,
       "genEquipMngSwSlotRunningVersionCardType": genEquipMngSwSlotRunningVersionCardType,
       "genEquipMngSwSlotRunningVersionComponent": genEquipMngSwSlotRunningVersionComponent,
       "genEquipMngSwSlotRunningVersionActualVersion": genEquipMngSwSlotRunningVersionActualVersion,
       "genEquipMngSwIDUVersionsStandByTable": genEquipMngSwIDUVersionsStandByTable,
       "genEquipMngSwIDUVersionsStandByEntry": genEquipMngSwIDUVersionsStandByEntry,
       "genEquipMngSwIDUVersionsStandByIndex": genEquipMngSwIDUVersionsStandByIndex,
       "genEquipMngSwIDUVersionsStandByPackageName": genEquipMngSwIDUVersionsStandByPackageName,
       "genEquipMngSwIDUVersionsStandByRunningVersion": genEquipMngSwIDUVersionsStandByRunningVersion,
       "genEquipMngSwIDUVersionsStandByInstalledVersion": genEquipMngSwIDUVersionsStandByInstalledVersion,
       "genEquipMngSwIDUVersionsStandByTargetDevice": genEquipMngSwIDUVersionsStandByTargetDevice,
       "genEquipMngSwIDUVersionsStandByDownloadedPackage": genEquipMngSwIDUVersionsStandByDownloadedPackage,
       "genEquipMngSwIDUVersionsStandByResetType": genEquipMngSwIDUVersionsStandByResetType,
       "genEquipMngSwWatchdogAdmin": genEquipMngSwWatchdogAdmin,
       "genEquipMngCfg": genEquipMngCfg,
       "genEquipMngCfgBackupStatus": genEquipMngCfgBackupStatus,
       "genEquipMngCfgRestoreStatus": genEquipMngCfgRestoreStatus,
       "genEquipMngCfgUploadStatus": genEquipMngCfgUploadStatus,
       "genEquipMngCfgDownloadStatus": genEquipMngCfgDownloadStatus,
       "genEquipMngCfgCommand": genEquipMngCfgCommand,
       "genEquipMngCfgEthernetSwitchStoreConfiguration": genEquipMngCfgEthernetSwitchStoreConfiguration,
       "genEquipMngCfgSetToDefaultKeepIp": genEquipMngCfgSetToDefaultKeepIp,
       "genEquipMngCfgCliScriptFileName": genEquipMngCfgCliScriptFileName,
       "genEquipMngCfgGeneric": genEquipMngCfgGeneric,
       "genEquipMngCfgBackupProgress": genEquipMngCfgBackupProgress,
       "genEquipMngCfgTimeToInstallation": genEquipMngCfgTimeToInstallation,
       "genEquipMngCfgFileTransferTable": genEquipMngCfgFileTransferTable,
       "genEquipMngCfgFileTransferEntry": genEquipMngCfgFileTransferEntry,
       "genEquipMngCfgFileTransferIndex": genEquipMngCfgFileTransferIndex,
       "genEquipMngCfgFileTransferProtocol": genEquipMngCfgFileTransferProtocol,
       "genEquipMngCfgFileTransferUserName": genEquipMngCfgFileTransferUserName,
       "genEquipMngCfgFileTransferPassword": genEquipMngCfgFileTransferPassword,
       "genEquipMngCfgFileTransferAddress": genEquipMngCfgFileTransferAddress,
       "genEquipMngCfgFileTransferPath": genEquipMngCfgFileTransferPath,
       "genEquipMngCfgFileTransferFileName": genEquipMngCfgFileTransferFileName,
       "genEquipMngCfgFileTransferIpv6Address": genEquipMngCfgFileTransferIpv6Address,
       "genEquipMngCfgFileTransferStatusTable": genEquipMngCfgFileTransferStatusTable,
       "genEquipMngCfgFileTransferStatusEntry": genEquipMngCfgFileTransferStatusEntry,
       "genEquipMngCfgFileTransferStatusIndex": genEquipMngCfgFileTransferStatusIndex,
       "genEquipMngCfgFileTransferStatusPercentageDone": genEquipMngCfgFileTransferStatusPercentageDone,
       "genEquipMngCfgFileTransferStatusResult": genEquipMngCfgFileTransferStatusResult,
       "genEquipMngCfgOperationTable": genEquipMngCfgOperationTable,
       "genEquipMngCfgOperationEntry": genEquipMngCfgOperationEntry,
       "genEquipMngCfgOperationIndex": genEquipMngCfgOperationIndex,
       "genEquipMngCfgOperationOperation": genEquipMngCfgOperationOperation,
       "genEquipMngCfgOperationFileNumber": genEquipMngCfgOperationFileNumber,
       "genEquipMngCfgOperationTimedInstallation": genEquipMngCfgOperationTimedInstallation,
       "genEquipMngCfgOperationTimer": genEquipMngCfgOperationTimer,
       "genEquipMngCfgOperationSlotNumber": genEquipMngCfgOperationSlotNumber,
       "genEquipMngCfgConfigurationFilesTable": genEquipMngCfgConfigurationFilesTable,
       "genEquipMngCfgConfigurationFilesEntry": genEquipMngCfgConfigurationFilesEntry,
       "genEquipMngCfgConfigurationFilesIndex": genEquipMngCfgConfigurationFilesIndex,
       "genEquipMngCfgConfigurationFilesFileNumber": genEquipMngCfgConfigurationFilesFileNumber,
       "genEquipMngCfgConfigurationFilesSystemType": genEquipMngCfgConfigurationFilesSystemType,
       "genEquipMngCfgConfigurationFilesSWVersion": genEquipMngCfgConfigurationFilesSWVersion,
       "genEquipMngCfgConfigurationFilesTimeDate": genEquipMngCfgConfigurationFilesTimeDate,
       "genEquipMngCfgConfigurationFilesSystemIP": genEquipMngCfgConfigurationFilesSystemIP,
       "genEquipMngCfgConfigurationFilesCardsConfigured": genEquipMngCfgConfigurationFilesCardsConfigured,
       "genEquipMngCfgConfigurationFilesSystemID": genEquipMngCfgConfigurationFilesSystemID,
       "genEquipMngCfgFileRestoreStatus": genEquipMngCfgFileRestoreStatus,
       "genEquipMngCfgFileTransferStatus": genEquipMngCfgFileTransferStatus,
       "genEquipMngFileTransfer": genEquipMngFileTransfer,
       "genEquipMngFileTransferFileTypeOper": genEquipMngFileTransferFileTypeOper,
       "genEquipMngFileTransferDownloadConfigStatus": genEquipMngFileTransferDownloadConfigStatus,
       "genEquipMngFileTransferDownloadCertificateStatus": genEquipMngFileTransferDownloadCertificateStatus,
       "genEquipMngFileTransferDownloadWarningBannerStatus": genEquipMngFileTransferDownloadWarningBannerStatus,
       "genEquipMngFileTransferDownloadCliScriptStatus": genEquipMngFileTransferDownloadCliScriptStatus,
       "genEquipMngFileTransferUploadConfigStatus": genEquipMngFileTransferUploadConfigStatus,
       "genEquipMngFileTransferUploadCSRStatus": genEquipMngFileTransferUploadCSRStatus,
       "genEquipMngFileTransferUploadUnitInfoStatus": genEquipMngFileTransferUploadUnitInfoStatus,
       "genEquipMngUnitInfo": genEquipMngUnitInfo,
       "genEquipMngUnitInfoGeneric": genEquipMngUnitInfoGeneric,
       "genEquipMngUnitInfoOperation": genEquipMngUnitInfoOperation,
       "genEquipMngUnitInfoProgress": genEquipMngUnitInfoProgress,
       "genEquipMngUnitInfoStatus": genEquipMngUnitInfoStatus,
       "genEquipMngUnitInfoFileTransferTable": genEquipMngUnitInfoFileTransferTable,
       "genEquipMngUnitInfoFileTransferEntry": genEquipMngUnitInfoFileTransferEntry,
       "genEquipMngUnitInfoFileTransferIndex": genEquipMngUnitInfoFileTransferIndex,
       "genEquipMngUnitInfoFileTransferProtocol": genEquipMngUnitInfoFileTransferProtocol,
       "genEquipMngUnitInfoFileTransferUserName": genEquipMngUnitInfoFileTransferUserName,
       "genEquipMngUnitInfoFileTransferPassword": genEquipMngUnitInfoFileTransferPassword,
       "genEquipMngUnitInfoFileTransferAddress": genEquipMngUnitInfoFileTransferAddress,
       "genEquipMngUnitInfoFileTransferPath": genEquipMngUnitInfoFileTransferPath,
       "genEquipMngUnitInfoFileTransferFileName": genEquipMngUnitInfoFileTransferFileName,
       "genEquipMngUnitInfoFileTransferIpv6Address": genEquipMngUnitInfoFileTransferIpv6Address,
       "genEquipMngUnitInfoFileTransferStatusTable": genEquipMngUnitInfoFileTransferStatusTable,
       "genEquipMngUnitInfoFileTransferStatusEntry": genEquipMngUnitInfoFileTransferStatusEntry,
       "genEquipMngUnitInfoFileTransferStatusIndex": genEquipMngUnitInfoFileTransferStatusIndex,
       "genEquipMngUnitInfoFileTransferStatusPercentageDone": genEquipMngUnitInfoFileTransferStatusPercentageDone,
       "genEquipMngUnitInfoFileTransferStatusResult": genEquipMngUnitInfoFileTransferStatusResult,
       "genEquipMngCli": genEquipMngCli,
       "genEquipMngCliScriptOperation": genEquipMngCliScriptOperation,
       "genEquipMngCliScriptOperationStatus": genEquipMngCliScriptOperationStatus,
       "genEquipDiagAndMaintenance": genEquipDiagAndMaintenance,
       "genEquipDiagAndMaintenanceRadioLoopbackTimeout": genEquipDiagAndMaintenanceRadioLoopbackTimeout,
       "genEquipDiagAndMaintenanceLineLoopbackTimeout": genEquipDiagAndMaintenanceLineLoopbackTimeout,
       "genEquipDiagAndMaintenanceSDHLoopbackTimeout": genEquipDiagAndMaintenanceSDHLoopbackTimeout,
       "genEquipSecurity": genEquipSecurity,
       "genEquipSecurityConfiguration": genEquipSecurityConfiguration,
       "genEquipSecurityCfgUploadPublicKeyStatus": genEquipSecurityCfgUploadPublicKeyStatus,
       "genEquipSecurityCfgDownloadSecurityStatus": genEquipSecurityCfgDownloadSecurityStatus,
       "genEquipSecurityCfgSecurityFileName": genEquipSecurityCfgSecurityFileName,
       "genEquipSecurityCfgSecurityFileType": genEquipSecurityCfgSecurityFileType,
       "genEquipSecurityCfgSecurityFileFormat": genEquipSecurityCfgSecurityFileFormat,
       "genEquipSecurityCfgSecurityWebCertificateAdmin": genEquipSecurityCfgSecurityWebCertificateAdmin,
       "genEquipSecurityCfgWebProtocol": genEquipSecurityCfgWebProtocol,
       "genEquipSecurityCfgTelnetAdmin": genEquipSecurityCfgTelnetAdmin,
       "genEquipSecurityCfgAutoLogOutPeriod": genEquipSecurityCfgAutoLogOutPeriod,
       "genEquipSecurityXFTP": genEquipSecurityXFTP,
       "genEquipSecurityXFTPHostIP": genEquipSecurityXFTPHostIP,
       "genEquipSecurityXFTPHostPath": genEquipSecurityXFTPHostPath,
       "genEquipSecurityXFTPProtocol": genEquipSecurityXFTPProtocol,
       "genEquipSecurityXFTPUserName": genEquipSecurityXFTPUserName,
       "genEquipSecurityXFTPPassword": genEquipSecurityXFTPPassword,
       "genEquipSecurityCfgPassFirstLoginChange": genEquipSecurityCfgPassFirstLoginChange,
       "genEquipSecurityCfgCSRCreation": genEquipSecurityCfgCSRCreation,
       "genEquipSecurityCfgWarningBannerFName": genEquipSecurityCfgWarningBannerFName,
       "genEquipSecurityConfigurationRadius": genEquipSecurityConfigurationRadius,
       "genEquipSecurityConfigurationRadiusAdmin": genEquipSecurityConfigurationRadiusAdmin,
       "genEquipSecurityConfigurationRadiusServerIP": genEquipSecurityConfigurationRadiusServerIP,
       "genEquipSecurityConfigurationRadiusSecret": genEquipSecurityConfigurationRadiusSecret,
       "genEquipSecurityConfigurationRadiusPort": genEquipSecurityConfigurationRadiusPort,
       "genEquipSecurityConfigurationRadiusRetries": genEquipSecurityConfigurationRadiusRetries,
       "genEquipSecurityConfigurationRadiusTimeout": genEquipSecurityConfigurationRadiusTimeout,
       "genEquipSecurityUsersAndGroups": genEquipSecurityUsersAndGroups,
       "genEquipSecurityUsersTable": genEquipSecurityUsersTable,
       "genEquipSecurityUsersEntry": genEquipSecurityUsersEntry,
       "genEquipSecurityUsersName": genEquipSecurityUsersName,
       "genEquipSecurityUsersPasswd": genEquipSecurityUsersPasswd,
       "genEquipSecurityUsersPriviledge": genEquipSecurityUsersPriviledge,
       "genEquipSecurityUsersPasswdAging": genEquipSecurityUsersPasswdAging,
       "genEquipSecurityUsersExprDate": genEquipSecurityUsersExprDate,
       "genEquipSecurityUsersLastLogin": genEquipSecurityUsersLastLogin,
       "genEquipSecurityUsersRowStatus": genEquipSecurityUsersRowStatus,
       "genEquipSecurityUsersAndGroupsChangePasswd": genEquipSecurityUsersAndGroupsChangePasswd,
       "genEquipSecuritySNMP": genEquipSecuritySNMP,
       "genEquipSecuritySNMPReadCommunity": genEquipSecuritySNMPReadCommunity,
       "genEquipSecuritySNMPWriteCommunity": genEquipSecuritySNMPWriteCommunity,
       "genEquipSecuritySNMPV3": genEquipSecuritySNMPV3,
       "genEquipSecuritySNMPV3AuthTable": genEquipSecuritySNMPV3AuthTable,
       "genEquipSecuritySNMPV3AuthEntry": genEquipSecuritySNMPV3AuthEntry,
       "genEquipSecuritySNMPV3AuthUserName": genEquipSecuritySNMPV3AuthUserName,
       "genEquipSecuritySNMPV3AuthPassword": genEquipSecuritySNMPV3AuthPassword,
       "genEquipSecuritySNMPV3AuthSecurityMode": genEquipSecuritySNMPV3AuthSecurityMode,
       "genEquipSecuritySNMPV3AuthEncryptionMode": genEquipSecuritySNMPV3AuthEncryptionMode,
       "genEquipSecuritySNMPV3AuthAuthenticationAlgorithm": genEquipSecuritySNMPV3AuthAuthenticationAlgorithm,
       "genEquipSecuritySNMPV3AuthAccessMode": genEquipSecuritySNMPV3AuthAccessMode,
       "genEquipSecuritySNMPV3AuthRowStatus": genEquipSecuritySNMPV3AuthRowStatus,
       "genEquipSecurityGen": genEquipSecurityGen,
       "genEquipSecurityGenFTConfigTable": genEquipSecurityGenFTConfigTable,
       "genEquipSecurityGenFTConfigEntry": genEquipSecurityGenFTConfigEntry,
       "genEquipSecurityGenFTConfigIndex": genEquipSecurityGenFTConfigIndex,
       "genEquipSecurityGenFTConfigProtocol": genEquipSecurityGenFTConfigProtocol,
       "genEquipSecurityGenFTConfigUsername": genEquipSecurityGenFTConfigUsername,
       "genEquipSecurityGenFTConfigPassword": genEquipSecurityGenFTConfigPassword,
       "genEquipSecurityGenFTConfigAddress": genEquipSecurityGenFTConfigAddress,
       "genEquipSecurityGenFTConfigFilePath": genEquipSecurityGenFTConfigFilePath,
       "genEquipSecurityGenFTConfigFileName": genEquipSecurityGenFTConfigFileName,
       "genEquipSecurityGenFTConfigIpV6Address": genEquipSecurityGenFTConfigIpV6Address,
       "genEquipSecurityGenFTStatusTable": genEquipSecurityGenFTStatusTable,
       "genEquipSecurityGenFTStatusEntry": genEquipSecurityGenFTStatusEntry,
       "genEquipSecurityGenFTStatusIndex": genEquipSecurityGenFTStatusIndex,
       "genEquipSecurityGenFTStatusStatus": genEquipSecurityGenFTStatusStatus,
       "genEquipSecurityGenFTStatusProgress": genEquipSecurityGenFTStatusProgress,
       "genEquipSecurityGenFTOperations": genEquipSecurityGenFTOperations,
       "genEquipSecurityGenImportExportAdmin": genEquipSecurityGenImportExportAdmin,
       "genEquipSecurityAccessControl": genEquipSecurityAccessControl,
       "genEquipSecurityAccessControlProfileTable": genEquipSecurityAccessControlProfileTable,
       "genEquipSecurityAccessControlProfileEntry": genEquipSecurityAccessControlProfileEntry,
       "genEquipSecurityAccessControlProfileName": genEquipSecurityAccessControlProfileName,
       "genEquipSecurityAccessControlProfileChannel": genEquipSecurityAccessControlProfileChannel,
       "genEquipSecurityAccessControlProfileUsed": genEquipSecurityAccessControlProfileUsed,
       "genEquipSecurityAccessControlProfileSecurityWrite": genEquipSecurityAccessControlProfileSecurityWrite,
       "genEquipSecurityAccessControlProfileSecurityRead": genEquipSecurityAccessControlProfileSecurityRead,
       "genEquipSecurityAccessControlProfileMngWrite": genEquipSecurityAccessControlProfileMngWrite,
       "genEquipSecurityAccessControlProfileMngRead": genEquipSecurityAccessControlProfileMngRead,
       "genEquipSecurityAccessControlProfileRadioWrite": genEquipSecurityAccessControlProfileRadioWrite,
       "genEquipSecurityAccessControlProfileRadioRead": genEquipSecurityAccessControlProfileRadioRead,
       "genEquipSecurityAccessControlProfileTDMWrite": genEquipSecurityAccessControlProfileTDMWrite,
       "genEquipSecurityAccessControlProfileTDMRead": genEquipSecurityAccessControlProfileTDMRead,
       "genEquipSecurityAccessControlProfileEthWrite": genEquipSecurityAccessControlProfileEthWrite,
       "genEquipSecurityAccessControlProfileEthRead": genEquipSecurityAccessControlProfileEthRead,
       "genEquipSecurityAccessControlProfileSyncWrite": genEquipSecurityAccessControlProfileSyncWrite,
       "genEquipSecurityAccessControlProfileSyncRead": genEquipSecurityAccessControlProfileSyncRead,
       "genEquipSecurityAccessControlProfileRowStatus": genEquipSecurityAccessControlProfileRowStatus,
       "genEquipSecurityAccessControlUserTable": genEquipSecurityAccessControlUserTable,
       "genEquipSecurityAccessControlUserEntry": genEquipSecurityAccessControlUserEntry,
       "genEquipSecurityAccessControlUserName": genEquipSecurityAccessControlUserName,
       "genEquipSecurityAccessControlUserProfile": genEquipSecurityAccessControlUserProfile,
       "genEquipSecurityAccessControlUserPassword": genEquipSecurityAccessControlUserPassword,
       "genEquipSecurityAccessControlUserExpired": genEquipSecurityAccessControlUserExpired,
       "genEquipSecurityAccessControlUserBlock": genEquipSecurityAccessControlUserBlock,
       "genEquipSecurityAccessControlUserLastLogout": genEquipSecurityAccessControlUserLastLogout,
       "genEquipSecurityAccessControlUserLoggedIn": genEquipSecurityAccessControlUserLoggedIn,
       "genEquipSecurityAccessControlUserRowStatus": genEquipSecurityAccessControlUserRowStatus,
       "genEquipSecurityAccessControlPassEnforceStrength": genEquipSecurityAccessControlPassEnforceStrength,
       "genEquipSecurityAccessControlPassFirstLoginChange": genEquipSecurityAccessControlPassFirstLoginChange,
       "genEquipSecurityAccessControlPassAging": genEquipSecurityAccessControlPassAging,
       "genEquipSecurityAccessControlFailureLoginAttempt": genEquipSecurityAccessControlFailureLoginAttempt,
       "genEquipSecurityAccessControlBlockFailureLoginPeriod": genEquipSecurityAccessControlBlockFailureLoginPeriod,
       "genEquipSecurityAccessControlBlockunusedAccount": genEquipSecurityAccessControlBlockunusedAccount,
       "genEquipSecurityAccessControlBlockRootRemote": genEquipSecurityAccessControlBlockRootRemote,
       "genEquipSecurityProtocolsControl": genEquipSecurityProtocolsControl,
       "genEquipSecurityProtocolsControlAutoSessionTimeOut": genEquipSecurityProtocolsControlAutoSessionTimeOut,
       "genEquipSecurityProtocolsControlSNMPAdmin": genEquipSecurityProtocolsControlSNMPAdmin,
       "genEquipSecurityProtocolsControlSNMPOperStatus": genEquipSecurityProtocolsControlSNMPOperStatus,
       "genEquipSecurityProtocolsControlSNMPTrapVersion": genEquipSecurityProtocolsControlSNMPTrapVersion,
       "genEquipSecurityProtocolsControlSNMPMIBVersion": genEquipSecurityProtocolsControlSNMPMIBVersion,
       "genEquipSecurityProtocolsControlSNMPV1V2Blocked": genEquipSecurityProtocolsControlSNMPV1V2Blocked,
       "genEquipSecurityProtocolsControlHTTPAdmin": genEquipSecurityProtocolsControlHTTPAdmin,
       "genEquipSecurityMonitorAndLogs": genEquipSecurityMonitorAndLogs,
       "genEquipSecurityConfigLogUploadConfigTable": genEquipSecurityConfigLogUploadConfigTable,
       "genEquipSecurityConfigLogUploadConfigEntry": genEquipSecurityConfigLogUploadConfigEntry,
       "genEquipSecurityConfigLogUploadConfigIndex": genEquipSecurityConfigLogUploadConfigIndex,
       "genEquipSecurityConfigLogUploadConfigProtocol": genEquipSecurityConfigLogUploadConfigProtocol,
       "genEquipSecurityConfigLogUploadConfigUsername": genEquipSecurityConfigLogUploadConfigUsername,
       "genEquipSecurityConfigLogUploadConfigPassword": genEquipSecurityConfigLogUploadConfigPassword,
       "genEquipSecurityConfigLogUploadConfigIpaddress": genEquipSecurityConfigLogUploadConfigIpaddress,
       "genEquipSecurityConfigLogUploadConfigPath": genEquipSecurityConfigLogUploadConfigPath,
       "genEquipSecurityConfigLogUploadConfigFilename": genEquipSecurityConfigLogUploadConfigFilename,
       "genEquipSecurityConfigLogUploadConfigIpV6Address": genEquipSecurityConfigLogUploadConfigIpV6Address,
       "genEquipSecurityConfigLogUploadStatusTable": genEquipSecurityConfigLogUploadStatusTable,
       "genEquipSecurityConfigLogUploadStatusEntry": genEquipSecurityConfigLogUploadStatusEntry,
       "genEquipSecurityConfigLogUploadStatusIndex": genEquipSecurityConfigLogUploadStatusIndex,
       "genEquipSecurityConfigLogUploadStatusStatus": genEquipSecurityConfigLogUploadStatusStatus,
       "genEquipSecurityConfigLogUploadStatusPrcntg": genEquipSecurityConfigLogUploadStatusPrcntg,
       "genEquipSecurityConfigLogUpload": genEquipSecurityConfigLogUpload,
       "genEquipSecurityRadiusServer": genEquipSecurityRadiusServer,
       "genEquipSecurityRadiusServerConfigurationTable": genEquipSecurityRadiusServerConfigurationTable,
       "genEquipSecurityRadiusServerConfigurationEntry": genEquipSecurityRadiusServerConfigurationEntry,
       "genEquipSecurityAccessControlRadiusServerId": genEquipSecurityAccessControlRadiusServerId,
       "genEquipSecurityAccessControlRadiusServerIpV4Address": genEquipSecurityAccessControlRadiusServerIpV4Address,
       "genEquipSecurityAccessControlRadiusServerIpv6Address": genEquipSecurityAccessControlRadiusServerIpv6Address,
       "genEquipSecurityAccessControlRadiusServerPort": genEquipSecurityAccessControlRadiusServerPort,
       "genEquipSecurityAccessControlRadiusServerRetries": genEquipSecurityAccessControlRadiusServerRetries,
       "genEquipSecurityAccessControlRadiusServerTimeout": genEquipSecurityAccessControlRadiusServerTimeout,
       "genEquipSecurityAccessControlRadiusServerSharedSecret": genEquipSecurityAccessControlRadiusServerSharedSecret,
       "genEquipSecurityAccessControlRadiusServerConnectivityStatus": genEquipSecurityAccessControlRadiusServerConnectivityStatus,
       "genEquipSecurityAccessControlRadiusUsersTable": genEquipSecurityAccessControlRadiusUsersTable,
       "genEquipSecurityAccessControlRadiusUsersEntry": genEquipSecurityAccessControlRadiusUsersEntry,
       "genEquipSecurityAccessControlRadiusUsersId": genEquipSecurityAccessControlRadiusUsersId,
       "genEquipSecurityAccessControlRadiusUserInstances": genEquipSecurityAccessControlRadiusUserInstances,
       "genEquipSecurityAccessControlRadiusUsersAccessChannels": genEquipSecurityAccessControlRadiusUsersAccessChannels,
       "genEquipSecurityAccessControlRadiusUsersEthReadLevel": genEquipSecurityAccessControlRadiusUsersEthReadLevel,
       "genEquipSecurityAccessControlRadiusUsersEthWriteLevel": genEquipSecurityAccessControlRadiusUsersEthWriteLevel,
       "genEquipSecurityAccessControlRadiusUsersMngReadLevel": genEquipSecurityAccessControlRadiusUsersMngReadLevel,
       "genEquipSecurityAccessControlRadiusUsersMngWriteLevel": genEquipSecurityAccessControlRadiusUsersMngWriteLevel,
       "genEquipSecurityAccessControlRadiusUsersRadioReadLevel": genEquipSecurityAccessControlRadiusUsersRadioReadLevel,
       "genEquipSecurityAccessControlRadiusUsersRadioWriteLevel": genEquipSecurityAccessControlRadiusUsersRadioWriteLevel,
       "genEquipSecurityAccessControlRadiusUsersSecurityReadLevel": genEquipSecurityAccessControlRadiusUsersSecurityReadLevel,
       "genEquipSecurityAccessControlRadiusUsersSecurityWriteLevel": genEquipSecurityAccessControlRadiusUsersSecurityWriteLevel,
       "genEquipSecurityAccessControlRadiusUsersSyncReadLevel": genEquipSecurityAccessControlRadiusUsersSyncReadLevel,
       "genEquipSecurityAccessControlRadiusUsersSyncWriteLevel": genEquipSecurityAccessControlRadiusUsersSyncWriteLevel,
       "genEquipSecurityAccessControlRadiusUsersTdmReadLevel": genEquipSecurityAccessControlRadiusUsersTdmReadLevel,
       "genEquipSecurityAccessControlRadiusUsersTdmWriteLevel": genEquipSecurityAccessControlRadiusUsersTdmWriteLevel,
       "genEquipSecurityRadiusAdmin": genEquipSecurityRadiusAdmin,
       "genEquipSecurityCertificate": genEquipSecurityCertificate,
       "genEquipSecurityCsrCertificateFileTransferSet": genEquipSecurityCsrCertificateFileTransferSet,
       "genEquipSecurityCsrStatus": genEquipSecurityCsrStatus,
       "genEquipSecurityCsrCertificateGenerateAndUploadPercentage": genEquipSecurityCsrCertificateGenerateAndUploadPercentage,
       "genEquipSecurityCertificateInstallSet": genEquipSecurityCertificateInstallSet,
       "genEquipSecurityCertificateDownloadStatus": genEquipSecurityCertificateDownloadStatus,
       "genEquipSecurityCertificateDownloadPercentage": genEquipSecurityCertificateDownloadPercentage,
       "genEquipSecurityCsrAttributesTable": genEquipSecurityCsrAttributesTable,
       "genEquipSecurityCsrAttributesEntry": genEquipSecurityCsrAttributesEntry,
       "genEquipSecurityCsrAttributesIndex": genEquipSecurityCsrAttributesIndex,
       "genEquipSecurityCsrAttributesCountry": genEquipSecurityCsrAttributesCountry,
       "genEquipSecurityCsrAttributesLocality": genEquipSecurityCsrAttributesLocality,
       "genEquipSecurityCsrAttributesState": genEquipSecurityCsrAttributesState,
       "genEquipSecurityCsrAttributesOrganization": genEquipSecurityCsrAttributesOrganization,
       "genEquipSecurityCsrAttributesOu": genEquipSecurityCsrAttributesOu,
       "genEquipSecurityCsrAttributesCommonName": genEquipSecurityCsrAttributesCommonName,
       "genEquipSecurityCsrAttributesEmail": genEquipSecurityCsrAttributesEmail,
       "genEquipSecurityCsrAttributesFileFormat": genEquipSecurityCsrAttributesFileFormat,
       "genEquipSecurityCsrUploadConfigTable": genEquipSecurityCsrUploadConfigTable,
       "genEquipSecurityCsrUploadConfigEntry": genEquipSecurityCsrUploadConfigEntry,
       "genEquipSecurityCsrUploadConfigIndex": genEquipSecurityCsrUploadConfigIndex,
       "genEquipSecurityCsrUploadConfigIpv4Address": genEquipSecurityCsrUploadConfigIpv4Address,
       "genEquipSecurityCsrUploadConfigIpV6Address": genEquipSecurityCsrUploadConfigIpV6Address,
       "genEquipSecurityCsrUploadConfigTableUsername": genEquipSecurityCsrUploadConfigTableUsername,
       "genEquipSecurityCsrUploadConfigPassword": genEquipSecurityCsrUploadConfigPassword,
       "genEquipSecurityCsrUploadConfigPath": genEquipSecurityCsrUploadConfigPath,
       "genEquipSecurityCsrUploadConfigFilename": genEquipSecurityCsrUploadConfigFilename,
       "genEquipSecurityCertificateDownloadConfigTable": genEquipSecurityCertificateDownloadConfigTable,
       "genEquipSecurityCertificateDownloadConfigEntry": genEquipSecurityCertificateDownloadConfigEntry,
       "genEquipSecurityCertificateDownloadConfigIndex": genEquipSecurityCertificateDownloadConfigIndex,
       "genEquipSecurityCertificateDownloadConfigIpv4Address": genEquipSecurityCertificateDownloadConfigIpv4Address,
       "genEquipSecurityCertificateDownloadConfigIpV6Address": genEquipSecurityCertificateDownloadConfigIpV6Address,
       "genEquipSecurityCertificateDownloadConfigUsername": genEquipSecurityCertificateDownloadConfigUsername,
       "genEquipSecurityCertificateDownloadConfigPassword": genEquipSecurityCertificateDownloadConfigPassword,
       "genEquipSecurityCertificateDownloadConfigPath": genEquipSecurityCertificateDownloadConfigPath,
       "genEquipSecurityCertificateDownloadConfigFilename": genEquipSecurityCertificateDownloadConfigFilename,
       "genEquipSecurityTrafficCrypto": genEquipSecurityTrafficCrypto,
       "genEquipSecurityFipsAdmin": genEquipSecurityFipsAdmin,
       "genEquipSecurityFipsStatus": genEquipSecurityFipsStatus,
       "genEquipTrafficCryptoConfigTable": genEquipTrafficCryptoConfigTable,
       "genEquipTrafficCryptoConfigEntry": genEquipTrafficCryptoConfigEntry,
       "genEquipTrafficCryptoConfigId": genEquipTrafficCryptoConfigId,
       "genEquipTrafficCryptoConfigConfigAdmin": genEquipTrafficCryptoConfigConfigAdmin,
       "genEquipTrafficCryptoConfigMkey": genEquipTrafficCryptoConfigMkey,
       "genEquipTrafficCryptoConfigBackupMkey": genEquipTrafficCryptoConfigBackupMkey,
       "genEquipTrafficCryptoConfigMkeyPeriod": genEquipTrafficCryptoConfigMkeyPeriod,
       "genEquipTrafficCryptoConfigRandKeyGen": genEquipTrafficCryptoConfigRandKeyGen,
       "genEquipTrafficCryptoConfigSkeyPeriod": genEquipTrafficCryptoConfigSkeyPeriod,
       "genEquipTrafficCryptoStatusTable": genEquipTrafficCryptoStatusTable,
       "genEquipTrafficCryptoStatusEntry": genEquipTrafficCryptoStatusEntry,
       "genEquipTrafficCryptoStatusId": genEquipTrafficCryptoStatusId,
       "genEquipTrafficCryptoStatusValid": genEquipTrafficCryptoStatusValid,
       "genEquipTrafficCryptoStatusMkeyTimeExpire": genEquipTrafficCryptoStatusMkeyTimeExpire}
)
