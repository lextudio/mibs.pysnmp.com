# SNMP MIB module (PLEXCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PLEXCOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:00 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Plexcom_ObjectIdentity = ObjectIdentity
plexcom = _Plexcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465)
)
_PlxNode_ObjectIdentity = ObjectIdentity
plxNode = _PlxNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1)
)
_PlxAgent_ObjectIdentity = ObjectIdentity
plxAgent = _PlxAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1)
)
_PlxStBridgeagent_ObjectIdentity = ObjectIdentity
plxStBridgeagent = _PlxStBridgeagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 1)
)
_PlxStBridgesnmpd_ObjectIdentity = ObjectIdentity
plxStBridgesnmpd = _PlxStBridgesnmpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 1, 1)
)
_PlxPlexcomHub8091_ObjectIdentity = ObjectIdentity
plxPlexcomHub8091 = _PlxPlexcomHub8091_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 1, 1, 4)
)
_PlxPlexcomHub8039_ObjectIdentity = ObjectIdentity
plxPlexcomHub8039 = _PlxPlexcomHub8039_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 1, 1, 5)
)
_PlxPlexcomHub8029_ObjectIdentity = ObjectIdentity
plxPlexcomHub8029 = _PlxPlexcomHub8029_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 1, 1, 6)
)
_PlxPlexcomHub8093_ObjectIdentity = ObjectIdentity
plxPlexcomHub8093 = _PlxPlexcomHub8093_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 1, 1, 7)
)
_PlxRepeaterAgent_ObjectIdentity = ObjectIdentity
plxRepeaterAgent = _PlxRepeaterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2)
)
_PlxPlexcom8025_ObjectIdentity = ObjectIdentity
plxPlexcom8025 = _PlxPlexcom8025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 1)
)
_PlxPlexcom8025SX_ObjectIdentity = ObjectIdentity
plxPlexcom8025SX = _PlxPlexcom8025SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 1, 1)
)
_PlxPlexcom8025SXT_ObjectIdentity = ObjectIdentity
plxPlexcom8025SXT = _PlxPlexcom8025SXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 1, 2)
)
_PlxPlexcomH8025SXT_ObjectIdentity = ObjectIdentity
plxPlexcomH8025SXT = _PlxPlexcomH8025SXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 1, 3)
)
_PlxPlexcomH8025SX_ObjectIdentity = ObjectIdentity
plxPlexcomH8025SX = _PlxPlexcomH8025SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 1, 4)
)
_PlxPlexcomS8025SXT_ObjectIdentity = ObjectIdentity
plxPlexcomS8025SXT = _PlxPlexcomS8025SXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 1, 5)
)
_PlxPlexcomS8025SX_ObjectIdentity = ObjectIdentity
plxPlexcomS8025SX = _PlxPlexcomS8025SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 1, 6)
)
_PlxPlexcomPlexSTACK_ObjectIdentity = ObjectIdentity
plxPlexcomPlexSTACK = _PlxPlexcomPlexSTACK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 2)
)
_PlxPlexcom4000i_ObjectIdentity = ObjectIdentity
plxPlexcom4000i = _PlxPlexcom4000i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 2, 1)
)
_PlxPlexcom4000iR_ObjectIdentity = ObjectIdentity
plxPlexcom4000iR = _PlxPlexcom4000iR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 2, 2, 2)
)
_PlxSwitchAgent_ObjectIdentity = ObjectIdentity
plxSwitchAgent = _PlxSwitchAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 3)
)
_PlxPlexcom5108_ObjectIdentity = ObjectIdentity
plxPlexcom5108 = _PlxPlexcom5108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 1, 3, 1)
)
_PlxModule_ObjectIdentity = ObjectIdentity
plxModule = _PlxModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2)
)
_PlxModuleUnknown_ObjectIdentity = ObjectIdentity
plxModuleUnknown = _PlxModuleUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 1)
)
_PlxModule8010_ObjectIdentity = ObjectIdentity
plxModule8010 = _PlxModule8010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 2)
)
_PlxModule8011_ObjectIdentity = ObjectIdentity
plxModule8011 = _PlxModule8011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 3)
)
_PlxModule8023A_ObjectIdentity = ObjectIdentity
plxModule8023A = _PlxModule8023A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 4)
)
_PlxModule8024A_ObjectIdentity = ObjectIdentity
plxModule8024A = _PlxModule8024A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 5)
)
_PlxModule8024T_ObjectIdentity = ObjectIdentity
plxModule8024T = _PlxModule8024T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 6)
)
_PlxModule8026A_ObjectIdentity = ObjectIdentity
plxModule8026A = _PlxModule8026A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 7)
)
_PlxModule8026T_ObjectIdentity = ObjectIdentity
plxModule8026T = _PlxModule8026T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 8)
)
_PlxModule8029M_ObjectIdentity = ObjectIdentity
plxModule8029M = _PlxModule8029M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 9)
)
_PlxModule8091M_ObjectIdentity = ObjectIdentity
plxModule8091M = _PlxModule8091M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 10)
)
_PlxModule8023_ObjectIdentity = ObjectIdentity
plxModule8023 = _PlxModule8023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 11)
)
_PlxModule8031_ObjectIdentity = ObjectIdentity
plxModule8031 = _PlxModule8031_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 13)
)
_PlxModule8031A_ObjectIdentity = ObjectIdentity
plxModule8031A = _PlxModule8031A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 14)
)
_PlxModule8033_ObjectIdentity = ObjectIdentity
plxModule8033 = _PlxModule8033_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 15)
)
_PlxModule8034_ObjectIdentity = ObjectIdentity
plxModule8034 = _PlxModule8034_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 16)
)
_PlxModule8033A_ObjectIdentity = ObjectIdentity
plxModule8033A = _PlxModule8033A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 17)
)
_PlxModule8024FO_ObjectIdentity = ObjectIdentity
plxModule8024FO = _PlxModule8024FO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 24)
)
_PlxModule8039M_ObjectIdentity = ObjectIdentity
plxModule8039M = _PlxModule8039M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 32)
)
_PlxModule8039S_ObjectIdentity = ObjectIdentity
plxModule8039S = _PlxModule8039S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 33)
)
_PlxModule8026FO_ObjectIdentity = ObjectIdentity
plxModule8026FO = _PlxModule8026FO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 34)
)
_PlxModule8408_ObjectIdentity = ObjectIdentity
plxModule8408 = _PlxModule8408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 35)
)
_PlxModule8400FO_ObjectIdentity = ObjectIdentity
plxModule8400FO = _PlxModule8400FO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 36)
)
_PlxModule8032_R_ObjectIdentity = ObjectIdentity
plxModule8032_R = _PlxModule8032_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 43)
)
_PlxModule8032_1P_ObjectIdentity = ObjectIdentity
plxModule8032_1P = _PlxModule8032_1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 45)
)
_PlxModule8032_2P_ObjectIdentity = ObjectIdentity
plxModule8032_2P = _PlxModule8032_2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 47)
)
_PlxModule8032_4P_ObjectIdentity = ObjectIdentity
plxModule8032_4P = _PlxModule8032_4P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 51)
)
_PlxModule8032_6P_ObjectIdentity = ObjectIdentity
plxModule8032_6P = _PlxModule8032_6P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 55)
)
_PlxModule2008SX_ObjectIdentity = ObjectIdentity
plxModule2008SX = _PlxModule2008SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 56)
)
_PlxModule8035_ObjectIdentity = ObjectIdentity
plxModule8035 = _PlxModule8035_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 58)
)
_PlxModule8035STP_ObjectIdentity = ObjectIdentity
plxModule8035STP = _PlxModule8035STP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 59)
)
_PlxModule8036_ObjectIdentity = ObjectIdentity
plxModule8036 = _PlxModule8036_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 60)
)
_PlxModule8023SX_ObjectIdentity = ObjectIdentity
plxModule8023SX = _PlxModule8023SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 70)
)
_PlxModule8012SX_1_ObjectIdentity = ObjectIdentity
plxModule8012SX_1 = _PlxModule8012SX_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 71)
)
_PlxModule8012SX_6_ObjectIdentity = ObjectIdentity
plxModule8012SX_6 = _PlxModule8012SX_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 72)
)
_PlxModule8024SX_ObjectIdentity = ObjectIdentity
plxModule8024SX = _PlxModule8024SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 73)
)
_PlxModule8027SX_ObjectIdentity = ObjectIdentity
plxModule8027SX = _PlxModule8027SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 74)
)
_PlxModule8091SXM_ObjectIdentity = ObjectIdentity
plxModule8091SXM = _PlxModule8091SXM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 75)
)
_PlxModule8029SX_3M_ObjectIdentity = ObjectIdentity
plxModule8029SX_3M = _PlxModule8029SX_3M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 76)
)
_PlxModule8029SX_3S_ObjectIdentity = ObjectIdentity
plxModule8029SX_3S = _PlxModule8029SX_3S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 77)
)
_PlxModule8025SX_ObjectIdentity = ObjectIdentity
plxModule8025SX = _PlxModule8025SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 78)
)
_PlxModule8025SXT_ObjectIdentity = ObjectIdentity
plxModule8025SXT = _PlxModule8025SXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 79)
)
_PlxModuleH8025SX_ObjectIdentity = ObjectIdentity
plxModuleH8025SX = _PlxModuleH8025SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 81)
)
_PlxModuleS8025SXT_ObjectIdentity = ObjectIdentity
plxModuleS8025SXT = _PlxModuleS8025SXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 82)
)
_PlxModuleS8025SX_ObjectIdentity = ObjectIdentity
plxModuleS8025SX = _PlxModuleS8025SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 83)
)
_PlxModule8408FO_ObjectIdentity = ObjectIdentity
plxModule8408FO = _PlxModule8408FO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 84)
)
_PlxModule8012SX_2_ObjectIdentity = ObjectIdentity
plxModule8012SX_2 = _PlxModule8012SX_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 85)
)
_PlxModule8012SX_4_ObjectIdentity = ObjectIdentity
plxModule8012SX_4 = _PlxModule8012SX_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 86)
)
_PlxModule8026SX_ObjectIdentity = ObjectIdentity
plxModule8026SX = _PlxModule8026SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 88)
)
_PlxModule8035SX_ObjectIdentity = ObjectIdentity
plxModule8035SX = _PlxModule8035SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 89)
)
_PlxModuleP8035SX_ObjectIdentity = ObjectIdentity
plxModuleP8035SX = _PlxModuleP8035SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 90)
)
_PlxModule8093SXM_ObjectIdentity = ObjectIdentity
plxModule8093SXM = _PlxModule8093SXM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 91)
)
_PlxModule8093SXS_ObjectIdentity = ObjectIdentity
plxModule8093SXS = _PlxModule8093SXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 92)
)
_PlxModule8039SXM_ObjectIdentity = ObjectIdentity
plxModule8039SXM = _PlxModule8039SXM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 93)
)
_PlxModule8039SXS_ObjectIdentity = ObjectIdentity
plxModule8039SXS = _PlxModule8039SXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 1, 2, 94)
)
_PlxFilterTable_ObjectIdentity = ObjectIdentity
plxFilterTable = _PlxFilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 2)
)
_PlxFtConfig_ObjectIdentity = ObjectIdentity
plxFtConfig = _PlxFtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 2, 1)
)
_PlxFtMaxAge_Type = Integer32
_PlxFtMaxAge_Object = MibScalar
plxFtMaxAge = _PlxFtMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 1, 1),
    _PlxFtMaxAge_Type()
)
plxFtMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFtMaxAge.setStatus("mandatory")
_PlxFtMaxRemove_Type = Integer32
_PlxFtMaxRemove_Object = MibScalar
plxFtMaxRemove = _PlxFtMaxRemove_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 1, 2),
    _PlxFtMaxRemove_Type()
)
plxFtMaxRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFtMaxRemove.setStatus("mandatory")
_PlxFtMaxFilter_Type = Integer32
_PlxFtMaxFilter_Object = MibScalar
plxFtMaxFilter = _PlxFtMaxFilter_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 1, 3),
    _PlxFtMaxFilter_Type()
)
plxFtMaxFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxFtMaxFilter.setStatus("mandatory")
_PlxFtAgeTime_Type = Integer32
_PlxFtAgeTime_Object = MibScalar
plxFtAgeTime = _PlxFtAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 1, 4),
    _PlxFtAgeTime_Type()
)
plxFtAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFtAgeTime.setStatus("mandatory")
_PlxFtMaxPerm_Type = Integer32
_PlxFtMaxPerm_Object = MibScalar
plxFtMaxPerm = _PlxFtMaxPerm_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 1, 5),
    _PlxFtMaxPerm_Type()
)
plxFtMaxPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFtMaxPerm.setStatus("mandatory")


class _PlxFtForwMBcast_Type(Integer32):
    """Custom type plxFtForwMBcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("noForward", 0))
    )


_PlxFtForwMBcast_Type.__name__ = "Integer32"
_PlxFtForwMBcast_Object = MibScalar
plxFtForwMBcast = _PlxFtForwMBcast_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 1, 6),
    _PlxFtForwMBcast_Type()
)
plxFtForwMBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFtForwMBcast.setStatus("mandatory")


class _PlxFtSecureMode_Type(Integer32):
    """Custom type plxFtSecureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("secure", 1))
    )


_PlxFtSecureMode_Type.__name__ = "Integer32"
_PlxFtSecureMode_Object = MibScalar
plxFtSecureMode = _PlxFtSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 1, 7),
    _PlxFtSecureMode_Type()
)
plxFtSecureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFtSecureMode.setStatus("mandatory")
_PlxFtEntry_ObjectIdentity = ObjectIdentity
plxFtEntry = _PlxFtEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 2, 2)
)
_PlxFtAge_Type = Integer32
_PlxFtAge_Object = MibScalar
plxFtAge = _PlxFtAge_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 2, 1),
    _PlxFtAge_Type()
)
plxFtAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFtAge.setStatus("mandatory")


class _PlxFtDisp_Type(Integer32):
    """Custom type plxFtDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              8,
              9,
              16,
              17,
              32,
              33,
              35,
              67,
              83)
        )
    )
    namedValues = NamedValues(
        *(("dynamdiscard", 32),
          ("dynamflood", 16),
          ("dynamforw1", 4),
          ("dynamforw2", 8),
          ("statdiscard", 33),
          ("statflood", 17),
          ("statforw1", 5),
          ("statforw2", 9),
          ("sysdiscard", 35),
          ("sysflood", 83),
          ("syssendup", 67))
    )


_PlxFtDisp_Type.__name__ = "Integer32"
_PlxFtDisp_Object = MibScalar
plxFtDisp = _PlxFtDisp_Object(
    (1, 3, 6, 1, 4, 1, 465, 2, 2, 2),
    _PlxFtDisp_Type()
)
plxFtDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFtDisp.setStatus("mandatory")
_PlxInterfaceErrors_ObjectIdentity = ObjectIdentity
plxInterfaceErrors = _PlxInterfaceErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 3)
)
_PlxIfeInBusErr_Type = Counter32
_PlxIfeInBusErr_Object = MibScalar
plxIfeInBusErr = _PlxIfeInBusErr_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 1),
    _PlxIfeInBusErr_Type()
)
plxIfeInBusErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeInBusErr.setStatus("mandatory")
_PlxIfeInShortPkt_Type = Counter32
_PlxIfeInShortPkt_Object = MibScalar
plxIfeInShortPkt = _PlxIfeInShortPkt_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 2),
    _PlxIfeInShortPkt_Type()
)
plxIfeInShortPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeInShortPkt.setStatus("mandatory")
_PlxIfeInAlgError_Type = Counter32
_PlxIfeInAlgError_Object = MibScalar
plxIfeInAlgError = _PlxIfeInAlgError_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 3),
    _PlxIfeInAlgError_Type()
)
plxIfeInAlgError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeInAlgError.setStatus("mandatory")
_PlxIfeInBadSize_Type = Counter32
_PlxIfeInBadSize_Object = MibScalar
plxIfeInBadSize = _PlxIfeInBadSize_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 4),
    _PlxIfeInBadSize_Type()
)
plxIfeInBadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeInBadSize.setStatus("mandatory")
_PlxIfeInOverflow_Type = Counter32
_PlxIfeInOverflow_Object = MibScalar
plxIfeInOverflow = _PlxIfeInOverflow_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 5),
    _PlxIfeInOverflow_Type()
)
plxIfeInOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeInOverflow.setStatus("mandatory")
_PlxIfeInCRCErr_Type = Counter32
_PlxIfeInCRCErr_Object = MibScalar
plxIfeInCRCErr = _PlxIfeInCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 6),
    _PlxIfeInCRCErr_Type()
)
plxIfeInCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeInCRCErr.setStatus("mandatory")
_PlxIfeOutCol16_Type = Counter32
_PlxIfeOutCol16_Object = MibScalar
plxIfeOutCol16 = _PlxIfeOutCol16_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 7),
    _PlxIfeOutCol16_Type()
)
plxIfeOutCol16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeOutCol16.setStatus("mandatory")
_PlxIfeOutCol_Type = Counter32
_PlxIfeOutCol_Object = MibScalar
plxIfeOutCol = _PlxIfeOutCol_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 8),
    _PlxIfeOutCol_Type()
)
plxIfeOutCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeOutCol.setStatus("mandatory")
_PlxIfeOutShortPkt_Type = Counter32
_PlxIfeOutShortPkt_Object = MibScalar
plxIfeOutShortPkt = _PlxIfeOutShortPkt_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 9),
    _PlxIfeOutShortPkt_Type()
)
plxIfeOutShortPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeOutShortPkt.setStatus("mandatory")
_PlxIfeOutUnderflow_Type = Counter32
_PlxIfeOutUnderflow_Object = MibScalar
plxIfeOutUnderflow = _PlxIfeOutUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 10),
    _PlxIfeOutUnderflow_Type()
)
plxIfeOutUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeOutUnderflow.setStatus("mandatory")
_PlxIfeOutBusErr_Type = Counter32
_PlxIfeOutBusErr_Object = MibScalar
plxIfeOutBusErr = _PlxIfeOutBusErr_Object(
    (1, 3, 6, 1, 4, 1, 465, 3, 11),
    _PlxIfeOutBusErr_Type()
)
plxIfeOutBusErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIfeOutBusErr.setStatus("mandatory")
_PlxForwardCounters_ObjectIdentity = ObjectIdentity
plxForwardCounters = _PlxForwardCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 4)
)
_PlxFcInOctets_Type = Counter32
_PlxFcInOctets_Object = MibScalar
plxFcInOctets = _PlxFcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 465, 4, 1),
    _PlxFcInOctets_Type()
)
plxFcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxFcInOctets.setStatus("mandatory")
_PlxFcInPkts_Type = Counter32
_PlxFcInPkts_Object = MibScalar
plxFcInPkts = _PlxFcInPkts_Object(
    (1, 3, 6, 1, 4, 1, 465, 4, 2),
    _PlxFcInPkts_Type()
)
plxFcInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxFcInPkts.setStatus("mandatory")
_PlxFcInNUcastPkts_Type = Counter32
_PlxFcInNUcastPkts_Object = MibScalar
plxFcInNUcastPkts = _PlxFcInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 465, 4, 3),
    _PlxFcInNUcastPkts_Type()
)
plxFcInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxFcInNUcastPkts.setStatus("mandatory")
_PlxFcForwOctets_Type = Counter32
_PlxFcForwOctets_Object = MibScalar
plxFcForwOctets = _PlxFcForwOctets_Object(
    (1, 3, 6, 1, 4, 1, 465, 4, 4),
    _PlxFcForwOctets_Type()
)
plxFcForwOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxFcForwOctets.setStatus("mandatory")
_PlxFcForwPkts_Type = Counter32
_PlxFcForwPkts_Object = MibScalar
plxFcForwPkts = _PlxFcForwPkts_Object(
    (1, 3, 6, 1, 4, 1, 465, 4, 5),
    _PlxFcForwPkts_Type()
)
plxFcForwPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxFcForwPkts.setStatus("mandatory")
_PlxFcFiltOctets_Type = Counter32
_PlxFcFiltOctets_Object = MibScalar
plxFcFiltOctets = _PlxFcFiltOctets_Object(
    (1, 3, 6, 1, 4, 1, 465, 4, 6),
    _PlxFcFiltOctets_Type()
)
plxFcFiltOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxFcFiltOctets.setStatus("mandatory")
_PlxFcFiltPkts_Type = Counter32
_PlxFcFiltPkts_Object = MibScalar
plxFcFiltPkts = _PlxFcFiltPkts_Object(
    (1, 3, 6, 1, 4, 1, 465, 4, 7),
    _PlxFcFiltPkts_Type()
)
plxFcFiltPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxFcFiltPkts.setStatus("mandatory")
_PlxSystemCounters_ObjectIdentity = ObjectIdentity
plxSystemCounters = _PlxSystemCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 5)
)
_PlxSysMemFree_Type = Counter32
_PlxSysMemFree_Object = MibScalar
plxSysMemFree = _PlxSysMemFree_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 1),
    _PlxSysMemFree_Type()
)
plxSysMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxSysMemFree.setStatus("mandatory")
_PlxSysMemAllocFail_Type = Counter32
_PlxSysMemAllocFail_Object = MibScalar
plxSysMemAllocFail = _PlxSysMemAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 2),
    _PlxSysMemAllocFail_Type()
)
plxSysMemAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxSysMemAllocFail.setStatus("mandatory")
_PlxSysMemTotAllocFail_Type = Counter32
_PlxSysMemTotAllocFail_Object = MibScalar
plxSysMemTotAllocFail = _PlxSysMemTotAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 3),
    _PlxSysMemTotAllocFail_Type()
)
plxSysMemTotAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxSysMemTotAllocFail.setStatus("mandatory")
_PlxSysMemFreeFail_Type = Counter32
_PlxSysMemFreeFail_Object = MibScalar
plxSysMemFreeFail = _PlxSysMemFreeFail_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 4),
    _PlxSysMemFreeFail_Type()
)
plxSysMemFreeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxSysMemFreeFail.setStatus("mandatory")
_PlxSysMemAllocTooBig_Type = Counter32
_PlxSysMemAllocTooBig_Object = MibScalar
plxSysMemAllocTooBig = _PlxSysMemAllocTooBig_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 5),
    _PlxSysMemAllocTooBig_Type()
)
plxSysMemAllocTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxSysMemAllocTooBig.setStatus("mandatory")
_PlxSysTimeToReset_Type = Counter32
_PlxSysTimeToReset_Object = MibScalar
plxSysTimeToReset = _PlxSysTimeToReset_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 6),
    _PlxSysTimeToReset_Type()
)
plxSysTimeToReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxSysTimeToReset.setStatus("mandatory")


class _PlxSysPanicMesg_Type(DisplayString):
    """Custom type plxSysPanicMesg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PlxSysPanicMesg_Type.__name__ = "DisplayString"
_PlxSysPanicMesg_Object = MibScalar
plxSysPanicMesg = _PlxSysPanicMesg_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 7),
    _PlxSysPanicMesg_Type()
)
plxSysPanicMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxSysPanicMesg.setStatus("mandatory")
_PlxSysResetCount_Type = Counter32
_PlxSysResetCount_Object = MibScalar
plxSysResetCount = _PlxSysResetCount_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 8),
    _PlxSysResetCount_Type()
)
plxSysResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxSysResetCount.setStatus("mandatory")


class _PlxSysSoftwareVersion_Type(DisplayString):
    """Custom type plxSysSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PlxSysSoftwareVersion_Type.__name__ = "DisplayString"
_PlxSysSoftwareVersion_Object = MibScalar
plxSysSoftwareVersion = _PlxSysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 465, 5, 10),
    _PlxSysSoftwareVersion_Type()
)
plxSysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxSysSoftwareVersion.setStatus("mandatory")
_PlxSpanningTree_ObjectIdentity = ObjectIdentity
plxSpanningTree = _PlxSpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 6)
)
_PlxStBridge_ObjectIdentity = ObjectIdentity
plxStBridge = _PlxStBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 6, 1)
)
_PlxStBrName_Type = OctetString
_PlxStBrName_Object = MibScalar
plxStBrName = _PlxStBrName_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 1),
    _PlxStBrName_Type()
)
plxStBrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxStBrName.setStatus("mandatory")
_PlxStBrIdent_Type = OctetString
_PlxStBrIdent_Object = MibScalar
plxStBrIdent = _PlxStBrIdent_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 2),
    _PlxStBrIdent_Type()
)
plxStBrIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxStBrIdent.setStatus("mandatory")
_PlxStBrMaxAge_Type = Integer32
_PlxStBrMaxAge_Object = MibScalar
plxStBrMaxAge = _PlxStBrMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 3),
    _PlxStBrMaxAge_Type()
)
plxStBrMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxStBrMaxAge.setStatus("mandatory")
_PlxStBrHelloTime_Type = Integer32
_PlxStBrHelloTime_Object = MibScalar
plxStBrHelloTime = _PlxStBrHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 4),
    _PlxStBrHelloTime_Type()
)
plxStBrHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxStBrHelloTime.setStatus("mandatory")
_PlxStBrForwDelay_Type = Integer32
_PlxStBrForwDelay_Object = MibScalar
plxStBrForwDelay = _PlxStBrForwDelay_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 5),
    _PlxStBrForwDelay_Type()
)
plxStBrForwDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxStBrForwDelay.setStatus("mandatory")


class _PlxStBrIsRoot_Type(Integer32):
    """Custom type plxStBrIsRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isroot", 1),
          ("notroot", 0))
    )


_PlxStBrIsRoot_Type.__name__ = "Integer32"
_PlxStBrIsRoot_Object = MibScalar
plxStBrIsRoot = _PlxStBrIsRoot_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 6),
    _PlxStBrIsRoot_Type()
)
plxStBrIsRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStBrIsRoot.setStatus("mandatory")


class _PlxStBrIsDesig_Type(Integer32):
    """Custom type plxStBrIsDesig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isdesig", 1),
          ("notdesig", 0))
    )


_PlxStBrIsDesig_Type.__name__ = "Integer32"
_PlxStBrIsDesig_Object = MibScalar
plxStBrIsDesig = _PlxStBrIsDesig_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 7),
    _PlxStBrIsDesig_Type()
)
plxStBrIsDesig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStBrIsDesig.setStatus("mandatory")


class _PlxStBrSpanAddr_Type(OctetString):
    """Custom type plxStBrSpanAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PlxStBrSpanAddr_Type.__name__ = "OctetString"
_PlxStBrSpanAddr_Object = MibScalar
plxStBrSpanAddr = _PlxStBrSpanAddr_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 8),
    _PlxStBrSpanAddr_Type()
)
plxStBrSpanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStBrSpanAddr.setStatus("mandatory")
_PlxStBrPriority_Type = Integer32
_PlxStBrPriority_Object = MibScalar
plxStBrPriority = _PlxStBrPriority_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 9),
    _PlxStBrPriority_Type()
)
plxStBrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxStBrPriority.setStatus("mandatory")


class _PlxStBrSTPDisabled_Type(Integer32):
    """Custom type plxStBrSTPDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_PlxStBrSTPDisabled_Type.__name__ = "Integer32"
_PlxStBrSTPDisabled_Object = MibScalar
plxStBrSTPDisabled = _PlxStBrSTPDisabled_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 1, 10),
    _PlxStBrSTPDisabled_Type()
)
plxStBrSTPDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxStBrSTPDisabled.setStatus("mandatory")
_PlxStRoot_ObjectIdentity = ObjectIdentity
plxStRoot = _PlxStRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 6, 2)
)
_PlxStRtIdent_Type = OctetString
_PlxStRtIdent_Object = MibScalar
plxStRtIdent = _PlxStRtIdent_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 2, 1),
    _PlxStRtIdent_Type()
)
plxStRtIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStRtIdent.setStatus("mandatory")
_PlxStRtCost_Type = Integer32
_PlxStRtCost_Object = MibScalar
plxStRtCost = _PlxStRtCost_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 2, 2),
    _PlxStRtCost_Type()
)
plxStRtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStRtCost.setStatus("mandatory")


class _PlxStRtPort_Type(Integer32):
    """Custom type plxStRtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rootPort1", 1),
          ("rootPort2", 2))
    )


_PlxStRtPort_Type.__name__ = "Integer32"
_PlxStRtPort_Object = MibScalar
plxStRtPort = _PlxStRtPort_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 2, 3),
    _PlxStRtPort_Type()
)
plxStRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStRtPort.setStatus("mandatory")
_PlxStRtMaxAge_Type = Integer32
_PlxStRtMaxAge_Object = MibScalar
plxStRtMaxAge = _PlxStRtMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 2, 4),
    _PlxStRtMaxAge_Type()
)
plxStRtMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStRtMaxAge.setStatus("mandatory")
_PlxStRtHelloTime_Type = Integer32
_PlxStRtHelloTime_Object = MibScalar
plxStRtHelloTime = _PlxStRtHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 2, 5),
    _PlxStRtHelloTime_Type()
)
plxStRtHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStRtHelloTime.setStatus("mandatory")
_PlxStRtForwDelay_Type = Integer32
_PlxStRtForwDelay_Object = MibScalar
plxStRtForwDelay = _PlxStRtForwDelay_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 2, 6),
    _PlxStRtForwDelay_Type()
)
plxStRtForwDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStRtForwDelay.setStatus("mandatory")
_PlxStPort_ObjectIdentity = ObjectIdentity
plxStPort = _PlxStPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 6, 3)
)


class _PlxStPrtState_Type(Integer32):
    """Custom type plxStPrtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("disabled", 0),
          ("forwarding", 8),
          ("learning", 4),
          ("listening", 2))
    )


_PlxStPrtState_Type.__name__ = "Integer32"
_PlxStPrtState_Object = MibScalar
plxStPrtState = _PlxStPrtState_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 1),
    _PlxStPrtState_Type()
)
plxStPrtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxStPrtState.setStatus("mandatory")
_PlxStPrtCost_Type = Integer32
_PlxStPrtCost_Object = MibScalar
plxStPrtCost = _PlxStPrtCost_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 2),
    _PlxStPrtCost_Type()
)
plxStPrtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStPrtCost.setStatus("mandatory")


class _PlxStPrtIsDesig_Type(Integer32):
    """Custom type plxStPrtIsDesig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isdesig", 1),
          ("notdesig", 0))
    )


_PlxStPrtIsDesig_Type.__name__ = "Integer32"
_PlxStPrtIsDesig_Object = MibScalar
plxStPrtIsDesig = _PlxStPrtIsDesig_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 3),
    _PlxStPrtIsDesig_Type()
)
plxStPrtIsDesig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStPrtIsDesig.setStatus("mandatory")


class _PlxStPrtIsRoot_Type(Integer32):
    """Custom type plxStPrtIsRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isroot", 1),
          ("notroot", 0))
    )


_PlxStPrtIsRoot_Type.__name__ = "Integer32"
_PlxStPrtIsRoot_Object = MibScalar
plxStPrtIsRoot = _PlxStPrtIsRoot_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 4),
    _PlxStPrtIsRoot_Type()
)
plxStPrtIsRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStPrtIsRoot.setStatus("mandatory")
_PlxStPrtDesigRoot_Type = OctetString
_PlxStPrtDesigRoot_Object = MibScalar
plxStPrtDesigRoot = _PlxStPrtDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 5),
    _PlxStPrtDesigRoot_Type()
)
plxStPrtDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStPrtDesigRoot.setStatus("mandatory")
_PlxStPrtDesigCost_Type = Integer32
_PlxStPrtDesigCost_Object = MibScalar
plxStPrtDesigCost = _PlxStPrtDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 6),
    _PlxStPrtDesigCost_Type()
)
plxStPrtDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStPrtDesigCost.setStatus("mandatory")
_PlxStPrtDesigBridge_Type = OctetString
_PlxStPrtDesigBridge_Object = MibScalar
plxStPrtDesigBridge = _PlxStPrtDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 7),
    _PlxStPrtDesigBridge_Type()
)
plxStPrtDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStPrtDesigBridge.setStatus("mandatory")
_PlxStPrtDesigPort_Type = Integer32
_PlxStPrtDesigPort_Object = MibScalar
plxStPrtDesigPort = _PlxStPrtDesigPort_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 8),
    _PlxStPrtDesigPort_Type()
)
plxStPrtDesigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStPrtDesigPort.setStatus("mandatory")
_PlxStPrtPriority_Type = Integer32
_PlxStPrtPriority_Object = MibScalar
plxStPrtPriority = _PlxStPrtPriority_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 3, 9),
    _PlxStPrtPriority_Type()
)
plxStPrtPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStPrtPriority.setStatus("mandatory")
_PlxSpanTreeStats_ObjectIdentity = ObjectIdentity
plxSpanTreeStats = _PlxSpanTreeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 6, 4)
)
_PlxStsTopoChanges_Type = Counter32
_PlxStsTopoChanges_Object = MibScalar
plxStsTopoChanges = _PlxStsTopoChanges_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 1),
    _PlxStsTopoChanges_Type()
)
plxStsTopoChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsTopoChanges.setStatus("mandatory")
_PlxStsConfigTimeout_Type = Counter32
_PlxStsConfigTimeout_Object = MibScalar
plxStsConfigTimeout = _PlxStsConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 2),
    _PlxStsConfigTimeout_Type()
)
plxStsConfigTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsConfigTimeout.setStatus("mandatory")
_PlxStsPortDisable_Type = Counter32
_PlxStsPortDisable_Object = MibScalar
plxStsPortDisable = _PlxStsPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 3),
    _PlxStsPortDisable_Type()
)
plxStsPortDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsPortDisable.setStatus("mandatory")
_PlxStsPortEnable_Type = Counter32
_PlxStsPortEnable_Object = MibScalar
plxStsPortEnable = _PlxStsPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 4),
    _PlxStsPortEnable_Type()
)
plxStsPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsPortEnable.setStatus("mandatory")
_PlxStsInBadLen_Type = Counter32
_PlxStsInBadLen_Object = MibScalar
plxStsInBadLen = _PlxStsInBadLen_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 5),
    _PlxStsInBadLen_Type()
)
plxStsInBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsInBadLen.setStatus("mandatory")
_PlxStsInUnknown_Type = Counter32
_PlxStsInUnknown_Object = MibScalar
plxStsInUnknown = _PlxStsInUnknown_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 6),
    _PlxStsInUnknown_Type()
)
plxStsInUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsInUnknown.setStatus("mandatory")
_PlxStsIn8021Man_Type = Counter32
_PlxStsIn8021Man_Object = MibScalar
plxStsIn8021Man = _PlxStsIn8021Man_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 7),
    _PlxStsIn8021Man_Type()
)
plxStsIn8021Man.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsIn8021Man.setStatus("mandatory")
_PlxStsInConfig_Type = Counter32
_PlxStsInConfig_Object = MibScalar
plxStsInConfig = _PlxStsInConfig_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 8),
    _PlxStsInConfig_Type()
)
plxStsInConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsInConfig.setStatus("mandatory")
_PlxStsInTopoChg_Type = Counter32
_PlxStsInTopoChg_Object = MibScalar
plxStsInTopoChg = _PlxStsInTopoChg_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 9),
    _PlxStsInTopoChg_Type()
)
plxStsInTopoChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsInTopoChg.setStatus("mandatory")
_PlxStsOutConfig_Type = Counter32
_PlxStsOutConfig_Object = MibScalar
plxStsOutConfig = _PlxStsOutConfig_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 10),
    _PlxStsOutConfig_Type()
)
plxStsOutConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsOutConfig.setStatus("mandatory")
_PlxStsOutTopoChg_Type = Counter32
_PlxStsOutTopoChg_Object = MibScalar
plxStsOutTopoChg = _PlxStsOutTopoChg_Object(
    (1, 3, 6, 1, 4, 1, 465, 6, 4, 11),
    _PlxStsOutTopoChg_Type()
)
plxStsOutTopoChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxStsOutTopoChg.setStatus("mandatory")
_PlxFilterRange_ObjectIdentity = ObjectIdentity
plxFilterRange = _PlxFilterRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 7)
)
_PlxFrNumRange_Type = Integer32
_PlxFrNumRange_Object = MibScalar
plxFrNumRange = _PlxFrNumRange_Object(
    (1, 3, 6, 1, 4, 1, 465, 7, 1),
    _PlxFrNumRange_Type()
)
plxFrNumRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFrNumRange.setStatus("mandatory")
_PlxFrEntry_Type = OctetString
_PlxFrEntry_Object = MibScalar
plxFrEntry = _PlxFrEntry_Object(
    (1, 3, 6, 1, 4, 1, 465, 7, 2),
    _PlxFrEntry_Type()
)
plxFrEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxFrEntry.setStatus("mandatory")
_PlxPlexcomProp_ObjectIdentity = ObjectIdentity
plxPlexcomProp = _PlxPlexcomProp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 9)
)
_PlxPlexAsync_Type = OctetString
_PlxPlexAsync_Object = MibScalar
plxPlexAsync = _PlxPlexAsync_Object(
    (1, 3, 6, 1, 4, 1, 465, 9, 1),
    _PlxPlexAsync_Type()
)
plxPlexAsync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxPlexAsync.setStatus("mandatory")


class _PlxPlexStat_Type(Integer32):
    """Custom type plxPlexStat based on Integer32"""
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


_PlxPlexStat_Type.__name__ = "Integer32"
_PlxPlexStat_Object = MibScalar
plxPlexStat = _PlxPlexStat_Object(
    (1, 3, 6, 1, 4, 1, 465, 9, 2),
    _PlxPlexStat_Type()
)
plxPlexStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxPlexStat.setStatus("mandatory")
_PlxPlexBkBits_Type = OctetString
_PlxPlexBkBits_Object = MibScalar
plxPlexBkBits = _PlxPlexBkBits_Object(
    (1, 3, 6, 1, 4, 1, 465, 9, 3),
    _PlxPlexBkBits_Type()
)
plxPlexBkBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxPlexBkBits.setStatus("mandatory")
_PlxPlexBkDef_Type = OctetString
_PlxPlexBkDef_Object = MibScalar
plxPlexBkDef = _PlxPlexBkDef_Object(
    (1, 3, 6, 1, 4, 1, 465, 9, 4),
    _PlxPlexBkDef_Type()
)
plxPlexBkDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxPlexBkDef.setStatus("mandatory")
_PlxHub_ObjectIdentity = ObjectIdentity
plxHub = _PlxHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 10)
)
_PlxHmBasicHubTable_Object = MibTable
plxHmBasicHubTable = _PlxHmBasicHubTable_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 1)
)
if mibBuilder.loadTexts:
    plxHmBasicHubTable.setStatus("mandatory")
_PlxHmBasicHubEntry_Object = MibTableRow
plxHmBasicHubEntry = _PlxHmBasicHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 1, 1)
)
plxHmBasicHubEntry.setIndexNames(
    (0, "PLEXCOM-MIB", "plxHubBasicID"),
)
if mibBuilder.loadTexts:
    plxHmBasicHubEntry.setStatus("mandatory")


class _PlxHubBasicID_Type(OctetString):
    """Custom type plxHubBasicID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PlxHubBasicID_Type.__name__ = "OctetString"
_PlxHubBasicID_Object = MibTableColumn
plxHubBasicID = _PlxHubBasicID_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 1, 1, 1),
    _PlxHubBasicID_Type()
)
plxHubBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxHubBasicID.setStatus("mandatory")


class _PlxHubGroupCapacity_Type(Integer32):
    """Custom type plxHubGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PlxHubGroupCapacity_Type.__name__ = "Integer32"
_PlxHubGroupCapacity_Object = MibTableColumn
plxHubGroupCapacity = _PlxHubGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 1, 1, 2),
    _PlxHubGroupCapacity_Type()
)
plxHubGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxHubGroupCapacity.setStatus("mandatory")
_PlxHubGroupMap_Type = OctetString
_PlxHubGroupMap_Object = MibTableColumn
plxHubGroupMap = _PlxHubGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 1, 1, 3),
    _PlxHubGroupMap_Type()
)
plxHubGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxHubGroupMap.setStatus("mandatory")


class _PlxHubGroupCount_Type(Integer32):
    """Custom type plxHubGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PlxHubGroupCount_Type.__name__ = "Integer32"
_PlxHubGroupCount_Object = MibTableColumn
plxHubGroupCount = _PlxHubGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 1, 1, 4),
    _PlxHubGroupCount_Type()
)
plxHubGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxHubGroupCount.setStatus("mandatory")
_PlxHmBasicGroupTable_Object = MibTable
plxHmBasicGroupTable = _PlxHmBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2)
)
if mibBuilder.loadTexts:
    plxHmBasicGroupTable.setStatus("mandatory")
_PlxHmBasicGroupEntry_Object = MibTableRow
plxHmBasicGroupEntry = _PlxHmBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1)
)
plxHmBasicGroupEntry.setIndexNames(
    (0, "PLEXCOM-MIB", "plxGroupBasicID"),
)
if mibBuilder.loadTexts:
    plxHmBasicGroupEntry.setStatus("mandatory")


class _PlxGroupHubBasicID_Type(OctetString):
    """Custom type plxGroupHubBasicID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PlxGroupHubBasicID_Type.__name__ = "OctetString"
_PlxGroupHubBasicID_Object = MibTableColumn
plxGroupHubBasicID = _PlxGroupHubBasicID_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 1),
    _PlxGroupHubBasicID_Type()
)
plxGroupHubBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupHubBasicID.setStatus("mandatory")


class _PlxGroupBasicID_Type(Integer32):
    """Custom type plxGroupBasicID based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("slot1", 1),
          ("slot10", 10),
          ("slot11", 11),
          ("slot12", 12),
          ("slot13", 13),
          ("slot14", 14),
          ("slot15", 15),
          ("slot16", 16),
          ("slot2", 2),
          ("slot3", 3),
          ("slot4", 4),
          ("slot5", 5),
          ("slot6", 6),
          ("slot7", 7),
          ("slot8", 8),
          ("slot9", 9))
    )


_PlxGroupBasicID_Type.__name__ = "Integer32"
_PlxGroupBasicID_Object = MibTableColumn
plxGroupBasicID = _PlxGroupBasicID_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 2),
    _PlxGroupBasicID_Type()
)
plxGroupBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupBasicID.setStatus("mandatory")


class _PlxGroupNumberOfPorts_Type(Integer32):
    """Custom type plxGroupNumberOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PlxGroupNumberOfPorts_Type.__name__ = "Integer32"
_PlxGroupNumberOfPorts_Object = MibTableColumn
plxGroupNumberOfPorts = _PlxGroupNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 3),
    _PlxGroupNumberOfPorts_Type()
)
plxGroupNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupNumberOfPorts.setStatus("mandatory")


class _PlxGroupType_Type(Integer32):
    """Custom type plxGroupType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              24,
              32,
              33,
              34,
              35,
              36,
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
              56,
              58,
              59,
              60,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              1000,
              1001,
              1010,
              1011,
              1012,
              1020,
              1021,
              1022,
              1030,
              1031,
              1032,
              1110,
              1111,
              1112,
              1120,
              1121,
              1122,
              1130,
              1131,
              1132)
        )
    )
    namedValues = NamedValues(
        *(("m2008SX", 56),
          ("m4000i", 1000),
          ("m4000iR", 1001),
          ("m4012", 1010),
          ("m4012i", 1011),
          ("m4012iR", 1012),
          ("m4024", 1020),
          ("m4024i", 1021),
          ("m4024iR", 1022),
          ("m4036", 1030),
          ("m4036i", 1031),
          ("m4036iR", 1032),
          ("m4112", 1110),
          ("m4112i", 1111),
          ("m4112iR", 1112),
          ("m4124", 1120),
          ("m4124i", 1121),
          ("m4124iR", 1122),
          ("m4136", 1130),
          ("m4136i", 1131),
          ("m4136iR", 1132),
          ("m8010", 2),
          ("m8011", 3),
          ("m8012SX-1", 71),
          ("m8012SX-12", 87),
          ("m8012SX-2", 85),
          ("m8012SX-4", 86),
          ("m8012SX-6", 72),
          ("m8023", 11),
          ("m8023A", 4),
          ("m8023SX", 70),
          ("m8024A", 5),
          ("m8024FO", 24),
          ("m8024SX", 73),
          ("m8024T", 6),
          ("m8025SX", 78),
          ("m8025SXT", 79),
          ("m8026A", 7),
          ("m8026FO", 34),
          ("m8026SX", 88),
          ("m8026T", 8),
          ("m8027SX", 74),
          ("m8029M", 9),
          ("m8029SX-3M", 76),
          ("m8029SX-3S", 77),
          ("m8031", 13),
          ("m8031A", 14),
          ("m8032-1P", 44),
          ("m8032-1PR", 45),
          ("m8032-2P", 46),
          ("m8032-2PR", 47),
          ("m8032-3P", 48),
          ("m8032-3PR", 49),
          ("m8032-4P", 50),
          ("m8032-4PR", 51),
          ("m8032-5P", 52),
          ("m8032-5PR", 53),
          ("m8032-6P", 54),
          ("m8032-6PR", 55),
          ("m8032-R", 43),
          ("m8033", 15),
          ("m8033A", 17),
          ("m8034", 16),
          ("m8035", 58),
          ("m8035STP", 59),
          ("m8035SX", 89),
          ("m8036", 60),
          ("m8039M", 32),
          ("m8039S", 33),
          ("m8039SXM", 93),
          ("m8039SXS", 94),
          ("m8091M", 10),
          ("m8091SXM", 75),
          ("m8093SXM", 91),
          ("m8093SXS", 92),
          ("m8400FO", 36),
          ("m8408", 35),
          ("m8408FO", 84),
          ("mH8025SX", 81),
          ("mP8035SX", 90),
          ("mS8025SX", 83),
          ("mS8025SXT", 82),
          ("removed", 0),
          ("unknown", 1))
    )


_PlxGroupType_Type.__name__ = "Integer32"
_PlxGroupType_Object = MibTableColumn
plxGroupType = _PlxGroupType_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 4),
    _PlxGroupType_Type()
)
plxGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupType.setStatus("mandatory")
_PlxGroupAutoPartState_Type = OctetString
_PlxGroupAutoPartState_Object = MibTableColumn
plxGroupAutoPartState = _PlxGroupAutoPartState_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 5),
    _PlxGroupAutoPartState_Type()
)
plxGroupAutoPartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupAutoPartState.setStatus("mandatory")
_PlxGroupAdminState_Type = OctetString
_PlxGroupAdminState_Object = MibTableColumn
plxGroupAdminState = _PlxGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 6),
    _PlxGroupAdminState_Type()
)
plxGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxGroupAdminState.setStatus("mandatory")


class _PlxGroupCascadeConfig_Type(Integer32):
    """Custom type plxGroupCascadeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("remote", 3),
          ("unknown", 1))
    )


_PlxGroupCascadeConfig_Type.__name__ = "Integer32"
_PlxGroupCascadeConfig_Object = MibTableColumn
plxGroupCascadeConfig = _PlxGroupCascadeConfig_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 7),
    _PlxGroupCascadeConfig_Type()
)
plxGroupCascadeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupCascadeConfig.setStatus("mandatory")
_PlxGroupCascadeNetwork_Type = OctetString
_PlxGroupCascadeNetwork_Object = MibTableColumn
plxGroupCascadeNetwork = _PlxGroupCascadeNetwork_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 8),
    _PlxGroupCascadeNetwork_Type()
)
plxGroupCascadeNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxGroupCascadeNetwork.setStatus("mandatory")
_PlxGroupLinkState_Type = OctetString
_PlxGroupLinkState_Object = MibTableColumn
plxGroupLinkState = _PlxGroupLinkState_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 9),
    _PlxGroupLinkState_Type()
)
plxGroupLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupLinkState.setStatus("mandatory")
_PlxGroupLinkPartTrapEnable_Type = OctetString
_PlxGroupLinkPartTrapEnable_Object = MibTableColumn
plxGroupLinkPartTrapEnable = _PlxGroupLinkPartTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 10),
    _PlxGroupLinkPartTrapEnable_Type()
)
plxGroupLinkPartTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxGroupLinkPartTrapEnable.setStatus("mandatory")
_PlxGroupNetworkSegment_Type = OctetString
_PlxGroupNetworkSegment_Object = MibTableColumn
plxGroupNetworkSegment = _PlxGroupNetworkSegment_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 11),
    _PlxGroupNetworkSegment_Type()
)
plxGroupNetworkSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupNetworkSegment.setStatus("mandatory")
_PlxGroupChassisNo_Type = Integer32
_PlxGroupChassisNo_Object = MibTableColumn
plxGroupChassisNo = _PlxGroupChassisNo_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 2, 1, 12),
    _PlxGroupChassisNo_Type()
)
plxGroupChassisNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxGroupChassisNo.setStatus("mandatory")
_PlxHmBasicPortTable_Object = MibTable
plxHmBasicPortTable = _PlxHmBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3)
)
if mibBuilder.loadTexts:
    plxHmBasicPortTable.setStatus("mandatory")
_PlxHmBasicPortEntry_Object = MibTableRow
plxHmBasicPortEntry = _PlxHmBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3, 1)
)
plxHmBasicPortEntry.setIndexNames(
    (0, "PLEXCOM-MIB", "plxPortGroupBasicID"),
    (0, "PLEXCOM-MIB", "plxPortBasicID"),
)
if mibBuilder.loadTexts:
    plxHmBasicPortEntry.setStatus("mandatory")


class _PlxPortHubBasicID_Type(OctetString):
    """Custom type plxPortHubBasicID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PlxPortHubBasicID_Type.__name__ = "OctetString"
_PlxPortHubBasicID_Object = MibTableColumn
plxPortHubBasicID = _PlxPortHubBasicID_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3, 1, 1),
    _PlxPortHubBasicID_Type()
)
plxPortHubBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxPortHubBasicID.setStatus("mandatory")


class _PlxPortGroupBasicID_Type(Integer32):
    """Custom type plxPortGroupBasicID based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("slot1", 1),
          ("slot10", 10),
          ("slot11", 11),
          ("slot12", 12),
          ("slot13", 13),
          ("slot14", 14),
          ("slot15", 15),
          ("slot16", 16),
          ("slot2", 2),
          ("slot3", 3),
          ("slot4", 4),
          ("slot5", 5),
          ("slot6", 6),
          ("slot7", 7),
          ("slot8", 8),
          ("slot9", 9))
    )


_PlxPortGroupBasicID_Type.__name__ = "Integer32"
_PlxPortGroupBasicID_Object = MibTableColumn
plxPortGroupBasicID = _PlxPortGroupBasicID_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3, 1, 2),
    _PlxPortGroupBasicID_Type()
)
plxPortGroupBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxPortGroupBasicID.setStatus("mandatory")


class _PlxPortBasicID_Type(Integer32):
    """Custom type plxPortBasicID based on Integer32"""
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
              18,
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port10", 10),
          ("port11", 11),
          ("port12", 12),
          ("port13", 13),
          ("port14", 14),
          ("port15", 15),
          ("port16", 16),
          ("port17", 17),
          ("port18", 18),
          ("port19", 19),
          ("port2", 2),
          ("port20", 20),
          ("port21", 21),
          ("port22", 22),
          ("port23", 23),
          ("port24", 24),
          ("port25", 25),
          ("port26", 26),
          ("port27", 27),
          ("port28", 28),
          ("port29", 29),
          ("port3", 3),
          ("port30", 30),
          ("port31", 31),
          ("port32", 32),
          ("port33", 33),
          ("port34", 34),
          ("port35", 35),
          ("port36", 36),
          ("port37", 37),
          ("port38", 38),
          ("port4", 4),
          ("port5", 5),
          ("port6", 6),
          ("port7", 7),
          ("port8", 8),
          ("port9", 9))
    )


_PlxPortBasicID_Type.__name__ = "Integer32"
_PlxPortBasicID_Object = MibTableColumn
plxPortBasicID = _PlxPortBasicID_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3, 1, 3),
    _PlxPortBasicID_Type()
)
plxPortBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxPortBasicID.setStatus("mandatory")


class _PlxPortMauType_Type(Integer32):
    """Custom type plxPortMauType based on Integer32"""
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
        *(("as400fiber", 18),
          ("as400utp", 17),
          ("foirl", 6),
          ("ieee10base2", 5),
          ("ieee10baseT", 4),
          ("ieeeAui", 2),
          ("ieeeThin", 3),
          ("internalNet", 15),
          ("serial", 16),
          ("telco50", 7),
          ("tokenringcoax", 12),
          ("tokenringfiber", 13),
          ("tokenringstp", 11),
          ("tokenringtelco50", 14),
          ("tokenringutp", 10),
          ("unknown", 1))
    )


_PlxPortMauType_Type.__name__ = "Integer32"
_PlxPortMauType_Object = MibTableColumn
plxPortMauType = _PlxPortMauType_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3, 1, 4),
    _PlxPortMauType_Type()
)
plxPortMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxPortMauType.setStatus("mandatory")


class _PlxPortAdminState_Type(Integer32):
    """Custom type plxPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("unknown", 1))
    )


_PlxPortAdminState_Type.__name__ = "Integer32"
_PlxPortAdminState_Object = MibTableColumn
plxPortAdminState = _PlxPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3, 1, 5),
    _PlxPortAdminState_Type()
)
plxPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxPortAdminState.setStatus("mandatory")


class _PlxPortAutoPartState_Type(Integer32):
    """Custom type plxPortAutoPartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPart", 2),
          ("part", 3),
          ("unknown", 1))
    )


_PlxPortAutoPartState_Type.__name__ = "Integer32"
_PlxPortAutoPartState_Object = MibTableColumn
plxPortAutoPartState = _PlxPortAutoPartState_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3, 1, 6),
    _PlxPortAutoPartState_Type()
)
plxPortAutoPartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxPortAutoPartState.setStatus("mandatory")


class _PlxPortLinkState_Type(Integer32):
    """Custom type plxPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_PlxPortLinkState_Type.__name__ = "Integer32"
_PlxPortLinkState_Object = MibTableColumn
plxPortLinkState = _PlxPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 465, 10, 3, 1, 7),
    _PlxPortLinkState_Type()
)
plxPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxPortLinkState.setStatus("mandatory")
_PlxSystemAdmin_ObjectIdentity = ObjectIdentity
plxSystemAdmin = _PlxSystemAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 11)
)
_PlxSysAdmCommunityTable_Object = MibTable
plxSysAdmCommunityTable = _PlxSysAdmCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 1)
)
if mibBuilder.loadTexts:
    plxSysAdmCommunityTable.setStatus("mandatory")
_PlxSysAdmCommunityEntry_Object = MibTableRow
plxSysAdmCommunityEntry = _PlxSysAdmCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 1, 1)
)
plxSysAdmCommunityEntry.setIndexNames(
    (0, "PLEXCOM-MIB", "plxCommunityIndex"),
)
if mibBuilder.loadTexts:
    plxSysAdmCommunityEntry.setStatus("mandatory")


class _PlxCommunityIndex_Type(Integer32):
    """Custom type plxCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PlxCommunityIndex_Type.__name__ = "Integer32"
_PlxCommunityIndex_Object = MibTableColumn
plxCommunityIndex = _PlxCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 1, 1, 1),
    _PlxCommunityIndex_Type()
)
plxCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxCommunityIndex.setStatus("mandatory")


class _PlxCommunityName_Type(DisplayString):
    """Custom type plxCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PlxCommunityName_Type.__name__ = "DisplayString"
_PlxCommunityName_Object = MibTableColumn
plxCommunityName = _PlxCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 1, 1, 2),
    _PlxCommunityName_Type()
)
plxCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxCommunityName.setStatus("mandatory")


class _PlxCommunityAccess_Type(Integer32):
    """Custom type plxCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 100),
          ("readOnly", 1),
          ("readWrite", 2),
          ("superUser", 3))
    )


_PlxCommunityAccess_Type.__name__ = "Integer32"
_PlxCommunityAccess_Object = MibTableColumn
plxCommunityAccess = _PlxCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 1, 1, 3),
    _PlxCommunityAccess_Type()
)
plxCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxCommunityAccess.setStatus("mandatory")
_PlxSysAdmDownload_ObjectIdentity = ObjectIdentity
plxSysAdmDownload = _PlxSysAdmDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 11, 2)
)


class _PlxDownloadFileName_Type(DisplayString):
    """Custom type plxDownloadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PlxDownloadFileName_Type.__name__ = "DisplayString"
_PlxDownloadFileName_Object = MibScalar
plxDownloadFileName = _PlxDownloadFileName_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 2, 1),
    _PlxDownloadFileName_Type()
)
plxDownloadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxDownloadFileName.setStatus("mandatory")


class _PlxDownloadServerAddress_Type(DisplayString):
    """Custom type plxDownloadServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PlxDownloadServerAddress_Type.__name__ = "DisplayString"
_PlxDownloadServerAddress_Object = MibScalar
plxDownloadServerAddress = _PlxDownloadServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 2, 2),
    _PlxDownloadServerAddress_Type()
)
plxDownloadServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxDownloadServerAddress.setStatus("mandatory")


class _PlxDownloadAction_Type(Integer32):
    """Custom type plxDownloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("noDownload", 1))
    )


_PlxDownloadAction_Type.__name__ = "Integer32"
_PlxDownloadAction_Object = MibScalar
plxDownloadAction = _PlxDownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 2, 3),
    _PlxDownloadAction_Type()
)
plxDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxDownloadAction.setStatus("mandatory")


class _PlxDownloadStatus_Type(Integer32):
    """Custom type plxDownloadStatus based on Integer32"""
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
              10,
              11,
              14)
        )
    )
    namedValues = NamedValues(
        *(("badFile", 5),
          ("badFlash", 3),
          ("badServerAddress", 4),
          ("downloadInProgress", 14),
          ("downloadNotOccurred", 2),
          ("downloadSuccess", 1),
          ("tftpAccessViolation", 8),
          ("tftpFileNotFound", 7),
          ("tftpIllegalOperation", 10),
          ("tftpUndefined", 6),
          ("tftpUnknownTransferID", 11))
    )


_PlxDownloadStatus_Type.__name__ = "Integer32"
_PlxDownloadStatus_Object = MibScalar
plxDownloadStatus = _PlxDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 2, 4),
    _PlxDownloadStatus_Type()
)
plxDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxDownloadStatus.setStatus("mandatory")
_PlxSysAdmTrapTable_Object = MibTable
plxSysAdmTrapTable = _PlxSysAdmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 3)
)
if mibBuilder.loadTexts:
    plxSysAdmTrapTable.setStatus("mandatory")
_PlxSysAdmTrapEntry_Object = MibTableRow
plxSysAdmTrapEntry = _PlxSysAdmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 3, 1)
)
plxSysAdmTrapEntry.setIndexNames(
    (0, "PLEXCOM-MIB", "plxTrapIndex"),
)
if mibBuilder.loadTexts:
    plxSysAdmTrapEntry.setStatus("mandatory")
_PlxTrapIndex_Type = Integer32
_PlxTrapIndex_Object = MibTableColumn
plxTrapIndex = _PlxTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 3, 1, 1),
    _PlxTrapIndex_Type()
)
plxTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxTrapIndex.setStatus("mandatory")


class _PlxTrapStandardEnable_Type(Integer32):
    """Custom type plxTrapStandardEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_PlxTrapStandardEnable_Type.__name__ = "Integer32"
_PlxTrapStandardEnable_Object = MibTableColumn
plxTrapStandardEnable = _PlxTrapStandardEnable_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 3, 1, 4),
    _PlxTrapStandardEnable_Type()
)
plxTrapStandardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxTrapStandardEnable.setStatus("mandatory")


class _PlxTrapPlexcomEnable_Type(Integer32):
    """Custom type plxTrapPlexcomEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_PlxTrapPlexcomEnable_Type.__name__ = "Integer32"
_PlxTrapPlexcomEnable_Object = MibTableColumn
plxTrapPlexcomEnable = _PlxTrapPlexcomEnable_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 3, 1, 5),
    _PlxTrapPlexcomEnable_Type()
)
plxTrapPlexcomEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxTrapPlexcomEnable.setStatus("mandatory")


class _PlxTrapRepeaterEnable_Type(Integer32):
    """Custom type plxTrapRepeaterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_PlxTrapRepeaterEnable_Type.__name__ = "Integer32"
_PlxTrapRepeaterEnable_Object = MibTableColumn
plxTrapRepeaterEnable = _PlxTrapRepeaterEnable_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 3, 1, 6),
    _PlxTrapRepeaterEnable_Type()
)
plxTrapRepeaterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxTrapRepeaterEnable.setStatus("mandatory")


class _PlxTrapNovellEnable_Type(Integer32):
    """Custom type plxTrapNovellEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_PlxTrapNovellEnable_Type.__name__ = "Integer32"
_PlxTrapNovellEnable_Object = MibTableColumn
plxTrapNovellEnable = _PlxTrapNovellEnable_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 3, 1, 7),
    _PlxTrapNovellEnable_Type()
)
plxTrapNovellEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxTrapNovellEnable.setStatus("mandatory")
_PlxSysAdmMibControl_ObjectIdentity = ObjectIdentity
plxSysAdmMibControl = _PlxSysAdmMibControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 11, 4)
)


class _PlxMcZeroStatCounters_Type(Integer32):
    """Custom type plxMcZeroStatCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noZero", 1),
          ("zeroCounters", 2))
    )


_PlxMcZeroStatCounters_Type.__name__ = "Integer32"
_PlxMcZeroStatCounters_Object = MibScalar
plxMcZeroStatCounters = _PlxMcZeroStatCounters_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 4, 1),
    _PlxMcZeroStatCounters_Type()
)
plxMcZeroStatCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxMcZeroStatCounters.setStatus("mandatory")
_PlxMcNetworkSelectRptrMib_Type = Integer32
_PlxMcNetworkSelectRptrMib_Object = MibScalar
plxMcNetworkSelectRptrMib = _PlxMcNetworkSelectRptrMib_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 4, 2),
    _PlxMcNetworkSelectRptrMib_Type()
)
plxMcNetworkSelectRptrMib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxMcNetworkSelectRptrMib.setStatus("mandatory")
_PlxMcNetworkSelectRmonMib_Type = Integer32
_PlxMcNetworkSelectRmonMib_Object = MibScalar
plxMcNetworkSelectRmonMib = _PlxMcNetworkSelectRmonMib_Object(
    (1, 3, 6, 1, 4, 1, 465, 11, 4, 3),
    _PlxMcNetworkSelectRmonMib_Type()
)
plxMcNetworkSelectRmonMib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxMcNetworkSelectRmonMib.setStatus("mandatory")
_PlxSecurity_ObjectIdentity = ObjectIdentity
plxSecurity = _PlxSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 465, 12)
)
_PlxIntruderControlGroupTable_Object = MibTable
plxIntruderControlGroupTable = _PlxIntruderControlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 1)
)
if mibBuilder.loadTexts:
    plxIntruderControlGroupTable.setStatus("mandatory")
_PlxIntruderControlGroupEntry_Object = MibTableRow
plxIntruderControlGroupEntry = _PlxIntruderControlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 1, 1)
)
plxIntruderControlGroupEntry.setIndexNames(
    (0, "PLEXCOM-MIB", "plxIcGroupGroupIndex"),
)
if mibBuilder.loadTexts:
    plxIntruderControlGroupEntry.setStatus("mandatory")
_PlxIcGroupGroupIndex_Type = Integer32
_PlxIcGroupGroupIndex_Object = MibTableColumn
plxIcGroupGroupIndex = _PlxIcGroupGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 1, 1, 1),
    _PlxIcGroupGroupIndex_Type()
)
plxIcGroupGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIcGroupGroupIndex.setStatus("mandatory")


class _PlxIcGroupAuthorizationType_Type(Integer32):
    """Custom type plxIcGroupAuthorizationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("multiValue", 9),
          ("noUser", 1),
          ("singleUser", 2))
    )


_PlxIcGroupAuthorizationType_Type.__name__ = "Integer32"
_PlxIcGroupAuthorizationType_Object = MibTableColumn
plxIcGroupAuthorizationType = _PlxIcGroupAuthorizationType_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 1, 1, 2),
    _PlxIcGroupAuthorizationType_Type()
)
plxIcGroupAuthorizationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcGroupAuthorizationType.setStatus("mandatory")


class _PlxIcGroupAlarmAction_Type(Integer32):
    """Custom type plxIcGroupAlarmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disableOnly", 3),
          ("multiValue", 9),
          ("none", 1),
          ("trapAndDisable", 4),
          ("trapOnly", 2))
    )


_PlxIcGroupAlarmAction_Type.__name__ = "Integer32"
_PlxIcGroupAlarmAction_Object = MibTableColumn
plxIcGroupAlarmAction = _PlxIcGroupAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 1, 1, 3),
    _PlxIcGroupAlarmAction_Type()
)
plxIcGroupAlarmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcGroupAlarmAction.setStatus("mandatory")


class _PlxIcGroupAuthorizedAddressMode_Type(Integer32):
    """Custom type plxIcGroupAuthorizedAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("autoLearn", 1),
          ("multiValue", 9),
          ("useAuthorized", 2))
    )


_PlxIcGroupAuthorizedAddressMode_Type.__name__ = "Integer32"
_PlxIcGroupAuthorizedAddressMode_Object = MibTableColumn
plxIcGroupAuthorizedAddressMode = _PlxIcGroupAuthorizedAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 1, 1, 4),
    _PlxIcGroupAuthorizedAddressMode_Type()
)
plxIcGroupAuthorizedAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcGroupAuthorizedAddressMode.setStatus("mandatory")


class _PlxIcGroupDetectionStatus_Type(Integer32):
    """Custom type plxIcGroupDetectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("multiValue", 9),
          ("triggered", 3))
    )


_PlxIcGroupDetectionStatus_Type.__name__ = "Integer32"
_PlxIcGroupDetectionStatus_Object = MibTableColumn
plxIcGroupDetectionStatus = _PlxIcGroupDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 1, 1, 5),
    _PlxIcGroupDetectionStatus_Type()
)
plxIcGroupDetectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcGroupDetectionStatus.setStatus("mandatory")
_PlxIntruderControlTable_Object = MibTable
plxIntruderControlTable = _PlxIntruderControlTable_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2)
)
if mibBuilder.loadTexts:
    plxIntruderControlTable.setStatus("mandatory")
_PlxIntruderControlEntry_Object = MibTableRow
plxIntruderControlEntry = _PlxIntruderControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1)
)
plxIntruderControlEntry.setIndexNames(
    (0, "PLEXCOM-MIB", "plxIcGroupIndex"),
    (0, "PLEXCOM-MIB", "plxIcPortIndex"),
)
if mibBuilder.loadTexts:
    plxIntruderControlEntry.setStatus("mandatory")
_PlxIcGroupIndex_Type = Integer32
_PlxIcGroupIndex_Object = MibTableColumn
plxIcGroupIndex = _PlxIcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1, 1),
    _PlxIcGroupIndex_Type()
)
plxIcGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIcGroupIndex.setStatus("mandatory")
_PlxIcPortIndex_Type = Integer32
_PlxIcPortIndex_Object = MibTableColumn
plxIcPortIndex = _PlxIcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1, 2),
    _PlxIcPortIndex_Type()
)
plxIcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIcPortIndex.setStatus("mandatory")


class _PlxIcAuthorizationType_Type(Integer32):
    """Custom type plxIcAuthorizationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUser", 1),
          ("singleUser", 2))
    )


_PlxIcAuthorizationType_Type.__name__ = "Integer32"
_PlxIcAuthorizationType_Object = MibTableColumn
plxIcAuthorizationType = _PlxIcAuthorizationType_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1, 3),
    _PlxIcAuthorizationType_Type()
)
plxIcAuthorizationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcAuthorizationType.setStatus("mandatory")


class _PlxIcAlarmAction_Type(Integer32):
    """Custom type plxIcAlarmAction based on Integer32"""
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
        *(("disableOnly", 3),
          ("none", 1),
          ("trapAndDisable", 4),
          ("trapOnly", 2))
    )


_PlxIcAlarmAction_Type.__name__ = "Integer32"
_PlxIcAlarmAction_Object = MibTableColumn
plxIcAlarmAction = _PlxIcAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1, 4),
    _PlxIcAlarmAction_Type()
)
plxIcAlarmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcAlarmAction.setStatus("mandatory")


class _PlxIcAuthorizedAddressMode_Type(Integer32):
    """Custom type plxIcAuthorizedAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoLearn", 1),
          ("useAuthorized", 2))
    )


_PlxIcAuthorizedAddressMode_Type.__name__ = "Integer32"
_PlxIcAuthorizedAddressMode_Object = MibTableColumn
plxIcAuthorizedAddressMode = _PlxIcAuthorizedAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1, 5),
    _PlxIcAuthorizedAddressMode_Type()
)
plxIcAuthorizedAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcAuthorizedAddressMode.setStatus("mandatory")


class _PlxIcAuthorizedSourceAddress_Type(OctetString):
    """Custom type plxIcAuthorizedSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PlxIcAuthorizedSourceAddress_Type.__name__ = "OctetString"
_PlxIcAuthorizedSourceAddress_Object = MibTableColumn
plxIcAuthorizedSourceAddress = _PlxIcAuthorizedSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1, 6),
    _PlxIcAuthorizedSourceAddress_Type()
)
plxIcAuthorizedSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcAuthorizedSourceAddress.setStatus("mandatory")


class _PlxIcCurrentSourceAddress_Type(OctetString):
    """Custom type plxIcCurrentSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PlxIcCurrentSourceAddress_Type.__name__ = "OctetString"
_PlxIcCurrentSourceAddress_Object = MibTableColumn
plxIcCurrentSourceAddress = _PlxIcCurrentSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1, 7),
    _PlxIcCurrentSourceAddress_Type()
)
plxIcCurrentSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plxIcCurrentSourceAddress.setStatus("mandatory")


class _PlxIcDetectionStatus_Type(Integer32):
    """Custom type plxIcDetectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("triggered", 3))
    )


_PlxIcDetectionStatus_Type.__name__ = "Integer32"
_PlxIcDetectionStatus_Object = MibTableColumn
plxIcDetectionStatus = _PlxIcDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 465, 12, 2, 1, 8),
    _PlxIcDetectionStatus_Type()
)
plxIcDetectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plxIcDetectionStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

plxPanicMesgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 465, 0, 4)
)
plxPanicMesgTrap.setObjects(
    ("PLEXCOM-MIB", "plxSysPanicMesg")
)
if mibBuilder.loadTexts:
    plxPanicMesgTrap.setStatus(
        ""
    )

plxGenericHubTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 465, 0, 5)
)
plxGenericHubTrap.setObjects(
      *(("PLEXCOM-MIB", "plxPortLinkState"),
        ("PLEXCOM-MIB", "plxPortAutoPartState"),
        ("PLEXCOM-MIB", "plxGroupType"))
)
if mibBuilder.loadTexts:
    plxGenericHubTrap.setStatus(
        ""
    )

plxSecurityViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 465, 0, 6)
)
plxSecurityViolationTrap.setObjects(
    ("PLEXCOM-MIB", "plxIcCurrentSourceAddress")
)
if mibBuilder.loadTexts:
    plxSecurityViolationTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PLEXCOM-MIB",
    **{"plexcom": plexcom,
       "plxPanicMesgTrap": plxPanicMesgTrap,
       "plxGenericHubTrap": plxGenericHubTrap,
       "plxSecurityViolationTrap": plxSecurityViolationTrap,
       "plxNode": plxNode,
       "plxAgent": plxAgent,
       "plxStBridgeagent": plxStBridgeagent,
       "plxStBridgesnmpd": plxStBridgesnmpd,
       "plxPlexcomHub8091": plxPlexcomHub8091,
       "plxPlexcomHub8039": plxPlexcomHub8039,
       "plxPlexcomHub8029": plxPlexcomHub8029,
       "plxPlexcomHub8093": plxPlexcomHub8093,
       "plxRepeaterAgent": plxRepeaterAgent,
       "plxPlexcom8025": plxPlexcom8025,
       "plxPlexcom8025SX": plxPlexcom8025SX,
       "plxPlexcom8025SXT": plxPlexcom8025SXT,
       "plxPlexcomH8025SXT": plxPlexcomH8025SXT,
       "plxPlexcomH8025SX": plxPlexcomH8025SX,
       "plxPlexcomS8025SXT": plxPlexcomS8025SXT,
       "plxPlexcomS8025SX": plxPlexcomS8025SX,
       "plxPlexcomPlexSTACK": plxPlexcomPlexSTACK,
       "plxPlexcom4000i": plxPlexcom4000i,
       "plxPlexcom4000iR": plxPlexcom4000iR,
       "plxSwitchAgent": plxSwitchAgent,
       "plxPlexcom5108": plxPlexcom5108,
       "plxModule": plxModule,
       "plxModuleUnknown": plxModuleUnknown,
       "plxModule8010": plxModule8010,
       "plxModule8011": plxModule8011,
       "plxModule8023A": plxModule8023A,
       "plxModule8024A": plxModule8024A,
       "plxModule8024T": plxModule8024T,
       "plxModule8026A": plxModule8026A,
       "plxModule8026T": plxModule8026T,
       "plxModule8029M": plxModule8029M,
       "plxModule8091M": plxModule8091M,
       "plxModule8023": plxModule8023,
       "plxModule8031": plxModule8031,
       "plxModule8031A": plxModule8031A,
       "plxModule8033": plxModule8033,
       "plxModule8034": plxModule8034,
       "plxModule8033A": plxModule8033A,
       "plxModule8024FO": plxModule8024FO,
       "plxModule8039M": plxModule8039M,
       "plxModule8039S": plxModule8039S,
       "plxModule8026FO": plxModule8026FO,
       "plxModule8408": plxModule8408,
       "plxModule8400FO": plxModule8400FO,
       "plxModule8032-R": plxModule8032_R,
       "plxModule8032-1P": plxModule8032_1P,
       "plxModule8032-2P": plxModule8032_2P,
       "plxModule8032-4P": plxModule8032_4P,
       "plxModule8032-6P": plxModule8032_6P,
       "plxModule2008SX": plxModule2008SX,
       "plxModule8035": plxModule8035,
       "plxModule8035STP": plxModule8035STP,
       "plxModule8036": plxModule8036,
       "plxModule8023SX": plxModule8023SX,
       "plxModule8012SX-1": plxModule8012SX_1,
       "plxModule8012SX-6": plxModule8012SX_6,
       "plxModule8024SX": plxModule8024SX,
       "plxModule8027SX": plxModule8027SX,
       "plxModule8091SXM": plxModule8091SXM,
       "plxModule8029SX-3M": plxModule8029SX_3M,
       "plxModule8029SX-3S": plxModule8029SX_3S,
       "plxModule8025SX": plxModule8025SX,
       "plxModule8025SXT": plxModule8025SXT,
       "plxModuleH8025SX": plxModuleH8025SX,
       "plxModuleS8025SXT": plxModuleS8025SXT,
       "plxModuleS8025SX": plxModuleS8025SX,
       "plxModule8408FO": plxModule8408FO,
       "plxModule8012SX-2": plxModule8012SX_2,
       "plxModule8012SX-4": plxModule8012SX_4,
       "plxModule8026SX": plxModule8026SX,
       "plxModule8035SX": plxModule8035SX,
       "plxModuleP8035SX": plxModuleP8035SX,
       "plxModule8093SXM": plxModule8093SXM,
       "plxModule8093SXS": plxModule8093SXS,
       "plxModule8039SXM": plxModule8039SXM,
       "plxModule8039SXS": plxModule8039SXS,
       "plxFilterTable": plxFilterTable,
       "plxFtConfig": plxFtConfig,
       "plxFtMaxAge": plxFtMaxAge,
       "plxFtMaxRemove": plxFtMaxRemove,
       "plxFtMaxFilter": plxFtMaxFilter,
       "plxFtAgeTime": plxFtAgeTime,
       "plxFtMaxPerm": plxFtMaxPerm,
       "plxFtForwMBcast": plxFtForwMBcast,
       "plxFtSecureMode": plxFtSecureMode,
       "plxFtEntry": plxFtEntry,
       "plxFtAge": plxFtAge,
       "plxFtDisp": plxFtDisp,
       "plxInterfaceErrors": plxInterfaceErrors,
       "plxIfeInBusErr": plxIfeInBusErr,
       "plxIfeInShortPkt": plxIfeInShortPkt,
       "plxIfeInAlgError": plxIfeInAlgError,
       "plxIfeInBadSize": plxIfeInBadSize,
       "plxIfeInOverflow": plxIfeInOverflow,
       "plxIfeInCRCErr": plxIfeInCRCErr,
       "plxIfeOutCol16": plxIfeOutCol16,
       "plxIfeOutCol": plxIfeOutCol,
       "plxIfeOutShortPkt": plxIfeOutShortPkt,
       "plxIfeOutUnderflow": plxIfeOutUnderflow,
       "plxIfeOutBusErr": plxIfeOutBusErr,
       "plxForwardCounters": plxForwardCounters,
       "plxFcInOctets": plxFcInOctets,
       "plxFcInPkts": plxFcInPkts,
       "plxFcInNUcastPkts": plxFcInNUcastPkts,
       "plxFcForwOctets": plxFcForwOctets,
       "plxFcForwPkts": plxFcForwPkts,
       "plxFcFiltOctets": plxFcFiltOctets,
       "plxFcFiltPkts": plxFcFiltPkts,
       "plxSystemCounters": plxSystemCounters,
       "plxSysMemFree": plxSysMemFree,
       "plxSysMemAllocFail": plxSysMemAllocFail,
       "plxSysMemTotAllocFail": plxSysMemTotAllocFail,
       "plxSysMemFreeFail": plxSysMemFreeFail,
       "plxSysMemAllocTooBig": plxSysMemAllocTooBig,
       "plxSysTimeToReset": plxSysTimeToReset,
       "plxSysPanicMesg": plxSysPanicMesg,
       "plxSysResetCount": plxSysResetCount,
       "plxSysSoftwareVersion": plxSysSoftwareVersion,
       "plxSpanningTree": plxSpanningTree,
       "plxStBridge": plxStBridge,
       "plxStBrName": plxStBrName,
       "plxStBrIdent": plxStBrIdent,
       "plxStBrMaxAge": plxStBrMaxAge,
       "plxStBrHelloTime": plxStBrHelloTime,
       "plxStBrForwDelay": plxStBrForwDelay,
       "plxStBrIsRoot": plxStBrIsRoot,
       "plxStBrIsDesig": plxStBrIsDesig,
       "plxStBrSpanAddr": plxStBrSpanAddr,
       "plxStBrPriority": plxStBrPriority,
       "plxStBrSTPDisabled": plxStBrSTPDisabled,
       "plxStRoot": plxStRoot,
       "plxStRtIdent": plxStRtIdent,
       "plxStRtCost": plxStRtCost,
       "plxStRtPort": plxStRtPort,
       "plxStRtMaxAge": plxStRtMaxAge,
       "plxStRtHelloTime": plxStRtHelloTime,
       "plxStRtForwDelay": plxStRtForwDelay,
       "plxStPort": plxStPort,
       "plxStPrtState": plxStPrtState,
       "plxStPrtCost": plxStPrtCost,
       "plxStPrtIsDesig": plxStPrtIsDesig,
       "plxStPrtIsRoot": plxStPrtIsRoot,
       "plxStPrtDesigRoot": plxStPrtDesigRoot,
       "plxStPrtDesigCost": plxStPrtDesigCost,
       "plxStPrtDesigBridge": plxStPrtDesigBridge,
       "plxStPrtDesigPort": plxStPrtDesigPort,
       "plxStPrtPriority": plxStPrtPriority,
       "plxSpanTreeStats": plxSpanTreeStats,
       "plxStsTopoChanges": plxStsTopoChanges,
       "plxStsConfigTimeout": plxStsConfigTimeout,
       "plxStsPortDisable": plxStsPortDisable,
       "plxStsPortEnable": plxStsPortEnable,
       "plxStsInBadLen": plxStsInBadLen,
       "plxStsInUnknown": plxStsInUnknown,
       "plxStsIn8021Man": plxStsIn8021Man,
       "plxStsInConfig": plxStsInConfig,
       "plxStsInTopoChg": plxStsInTopoChg,
       "plxStsOutConfig": plxStsOutConfig,
       "plxStsOutTopoChg": plxStsOutTopoChg,
       "plxFilterRange": plxFilterRange,
       "plxFrNumRange": plxFrNumRange,
       "plxFrEntry": plxFrEntry,
       "plxPlexcomProp": plxPlexcomProp,
       "plxPlexAsync": plxPlexAsync,
       "plxPlexStat": plxPlexStat,
       "plxPlexBkBits": plxPlexBkBits,
       "plxPlexBkDef": plxPlexBkDef,
       "plxHub": plxHub,
       "plxHmBasicHubTable": plxHmBasicHubTable,
       "plxHmBasicHubEntry": plxHmBasicHubEntry,
       "plxHubBasicID": plxHubBasicID,
       "plxHubGroupCapacity": plxHubGroupCapacity,
       "plxHubGroupMap": plxHubGroupMap,
       "plxHubGroupCount": plxHubGroupCount,
       "plxHmBasicGroupTable": plxHmBasicGroupTable,
       "plxHmBasicGroupEntry": plxHmBasicGroupEntry,
       "plxGroupHubBasicID": plxGroupHubBasicID,
       "plxGroupBasicID": plxGroupBasicID,
       "plxGroupNumberOfPorts": plxGroupNumberOfPorts,
       "plxGroupType": plxGroupType,
       "plxGroupAutoPartState": plxGroupAutoPartState,
       "plxGroupAdminState": plxGroupAdminState,
       "plxGroupCascadeConfig": plxGroupCascadeConfig,
       "plxGroupCascadeNetwork": plxGroupCascadeNetwork,
       "plxGroupLinkState": plxGroupLinkState,
       "plxGroupLinkPartTrapEnable": plxGroupLinkPartTrapEnable,
       "plxGroupNetworkSegment": plxGroupNetworkSegment,
       "plxGroupChassisNo": plxGroupChassisNo,
       "plxHmBasicPortTable": plxHmBasicPortTable,
       "plxHmBasicPortEntry": plxHmBasicPortEntry,
       "plxPortHubBasicID": plxPortHubBasicID,
       "plxPortGroupBasicID": plxPortGroupBasicID,
       "plxPortBasicID": plxPortBasicID,
       "plxPortMauType": plxPortMauType,
       "plxPortAdminState": plxPortAdminState,
       "plxPortAutoPartState": plxPortAutoPartState,
       "plxPortLinkState": plxPortLinkState,
       "plxSystemAdmin": plxSystemAdmin,
       "plxSysAdmCommunityTable": plxSysAdmCommunityTable,
       "plxSysAdmCommunityEntry": plxSysAdmCommunityEntry,
       "plxCommunityIndex": plxCommunityIndex,
       "plxCommunityName": plxCommunityName,
       "plxCommunityAccess": plxCommunityAccess,
       "plxSysAdmDownload": plxSysAdmDownload,
       "plxDownloadFileName": plxDownloadFileName,
       "plxDownloadServerAddress": plxDownloadServerAddress,
       "plxDownloadAction": plxDownloadAction,
       "plxDownloadStatus": plxDownloadStatus,
       "plxSysAdmTrapTable": plxSysAdmTrapTable,
       "plxSysAdmTrapEntry": plxSysAdmTrapEntry,
       "plxTrapIndex": plxTrapIndex,
       "plxTrapStandardEnable": plxTrapStandardEnable,
       "plxTrapPlexcomEnable": plxTrapPlexcomEnable,
       "plxTrapRepeaterEnable": plxTrapRepeaterEnable,
       "plxTrapNovellEnable": plxTrapNovellEnable,
       "plxSysAdmMibControl": plxSysAdmMibControl,
       "plxMcZeroStatCounters": plxMcZeroStatCounters,
       "plxMcNetworkSelectRptrMib": plxMcNetworkSelectRptrMib,
       "plxMcNetworkSelectRmonMib": plxMcNetworkSelectRmonMib,
       "plxSecurity": plxSecurity,
       "plxIntruderControlGroupTable": plxIntruderControlGroupTable,
       "plxIntruderControlGroupEntry": plxIntruderControlGroupEntry,
       "plxIcGroupGroupIndex": plxIcGroupGroupIndex,
       "plxIcGroupAuthorizationType": plxIcGroupAuthorizationType,
       "plxIcGroupAlarmAction": plxIcGroupAlarmAction,
       "plxIcGroupAuthorizedAddressMode": plxIcGroupAuthorizedAddressMode,
       "plxIcGroupDetectionStatus": plxIcGroupDetectionStatus,
       "plxIntruderControlTable": plxIntruderControlTable,
       "plxIntruderControlEntry": plxIntruderControlEntry,
       "plxIcGroupIndex": plxIcGroupIndex,
       "plxIcPortIndex": plxIcPortIndex,
       "plxIcAuthorizationType": plxIcAuthorizationType,
       "plxIcAlarmAction": plxIcAlarmAction,
       "plxIcAuthorizedAddressMode": plxIcAuthorizedAddressMode,
       "plxIcAuthorizedSourceAddress": plxIcAuthorizedSourceAddress,
       "plxIcCurrentSourceAddress": plxIcCurrentSourceAddress,
       "plxIcDetectionStatus": plxIcDetectionStatus}
)
