# SNMP MIB module (XEROX-PRODUCT-ID-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-PRODUCT-ID-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:31 2024
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

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmPidTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmPidProductIdentifiers_ObjectIdentity = ObjectIdentity
xcmPidProductIdentifiers = _XcmPidProductIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1)
)
if mibBuilder.loadTexts:
    xcmPidProductIdentifiers.setStatus("current")
_XcmPidDocuCentreSystems_ObjectIdentity = ObjectIdentity
xcmPidDocuCentreSystems = _XcmPidDocuCentreSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuCentreSystems.setStatus("current")
_XcmPidDCS20_ObjectIdentity = ObjectIdentity
xcmPidDCS20 = _XcmPidDCS20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDCS20.setStatus("current")
_XcmPidDCS20M1_ObjectIdentity = ObjectIdentity
xcmPidDCS20M1 = _XcmPidDCS20M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDCS20M1.setStatus("current")
_XcmPidDCS20M1V1_ObjectIdentity = ObjectIdentity
xcmPidDCS20M1V1 = _XcmPidDCS20M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDCS20M1V1.setStatus("current")
_XcmPidDCS35_ObjectIdentity = ObjectIdentity
xcmPidDCS35 = _XcmPidDCS35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDCS35.setStatus("current")
_XcmPidDCS35M1_ObjectIdentity = ObjectIdentity
xcmPidDCS35M1 = _XcmPidDCS35M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDCS35M1.setStatus("current")
_XcmPidDCS35M1V1_ObjectIdentity = ObjectIdentity
xcmPidDCS35M1V1 = _XcmPidDCS35M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDCS35M1V1.setStatus("current")
_XcmPidDC230_ObjectIdentity = ObjectIdentity
xcmPidDC230 = _XcmPidDC230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC230.setStatus("current")
_XcmPidDC230ST_ObjectIdentity = ObjectIdentity
xcmPidDC230ST = _XcmPidDC230ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC230ST.setStatus("current")
_XcmPidDC230STV1_ObjectIdentity = ObjectIdentity
xcmPidDC230STV1 = _XcmPidDC230STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC230STV1.setStatus("current")
_XcmPidDC230STV2_ObjectIdentity = ObjectIdentity
xcmPidDC230STV2 = _XcmPidDC230STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC230STV2.setStatus("current")
_XcmPidDC230STV3_ObjectIdentity = ObjectIdentity
xcmPidDC230STV3 = _XcmPidDC230STV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC230STV3.setStatus("current")
_XcmPidDC230STV4_ObjectIdentity = ObjectIdentity
xcmPidDC230STV4 = _XcmPidDC230STV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidDC230STV4.setStatus("current")
_XcmPidDC230STV5_ObjectIdentity = ObjectIdentity
xcmPidDC230STV5 = _XcmPidDC230STV5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidDC230STV5.setStatus("current")
_XcmPidDC230LP_ObjectIdentity = ObjectIdentity
xcmPidDC230LP = _XcmPidDC230LP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC230LP.setStatus("current")
_XcmPidDC230LPV1_ObjectIdentity = ObjectIdentity
xcmPidDC230LPV1 = _XcmPidDC230LPV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC230LPV1.setStatus("current")
_XcmPidDC230LPV2_ObjectIdentity = ObjectIdentity
xcmPidDC230LPV2 = _XcmPidDC230LPV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC230LPV2.setStatus("current")
_XcmPidDC230LPV3_ObjectIdentity = ObjectIdentity
xcmPidDC230LPV3 = _XcmPidDC230LPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC230LPV3.setStatus("current")
_XcmPidDC230LPV4_ObjectIdentity = ObjectIdentity
xcmPidDC230LPV4 = _XcmPidDC230LPV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    xcmPidDC230LPV4.setStatus("current")
_XcmPidDC230LPV5_ObjectIdentity = ObjectIdentity
xcmPidDC230LPV5 = _XcmPidDC230LPV5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    xcmPidDC230LPV5.setStatus("current")
_XcmPidDC265_ObjectIdentity = ObjectIdentity
xcmPidDC265 = _XcmPidDC265_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidDC265.setStatus("current")
_XcmPidDC265ST_ObjectIdentity = ObjectIdentity
xcmPidDC265ST = _XcmPidDC265ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC265ST.setStatus("current")
_XcmPidDC265STV1_ObjectIdentity = ObjectIdentity
xcmPidDC265STV1 = _XcmPidDC265STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC265STV1.setStatus("current")
_XcmPidDC265STV2_ObjectIdentity = ObjectIdentity
xcmPidDC265STV2 = _XcmPidDC265STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC265STV2.setStatus("current")
_XcmPidDC265STV3_ObjectIdentity = ObjectIdentity
xcmPidDC265STV3 = _XcmPidDC265STV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC265STV3.setStatus("current")
_XcmPidDC265LP_ObjectIdentity = ObjectIdentity
xcmPidDC265LP = _XcmPidDC265LP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC265LP.setStatus("current")
_XcmPidDC265LPV1_ObjectIdentity = ObjectIdentity
xcmPidDC265LPV1 = _XcmPidDC265LPV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC265LPV1.setStatus("current")
_XcmPidDC265LPV2_ObjectIdentity = ObjectIdentity
xcmPidDC265LPV2 = _XcmPidDC265LPV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC265LPV2.setStatus("current")
_XcmPidDC265LPV3_ObjectIdentity = ObjectIdentity
xcmPidDC265LPV3 = _XcmPidDC265LPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC265LPV3.setStatus("current")
_XcmPidDC240_ObjectIdentity = ObjectIdentity
xcmPidDC240 = _XcmPidDC240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidDC240.setStatus("current")
_XcmPidDC240ST_ObjectIdentity = ObjectIdentity
xcmPidDC240ST = _XcmPidDC240ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC240ST.setStatus("current")
_XcmPidDC240STV1_ObjectIdentity = ObjectIdentity
xcmPidDC240STV1 = _XcmPidDC240STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC240STV1.setStatus("current")
_XcmPidDC240STV2_ObjectIdentity = ObjectIdentity
xcmPidDC240STV2 = _XcmPidDC240STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC240STV2.setStatus("current")
_XcmPidDC240STV3_ObjectIdentity = ObjectIdentity
xcmPidDC240STV3 = _XcmPidDC240STV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC240STV3.setStatus("current")
_XcmPidDC340_ObjectIdentity = ObjectIdentity
xcmPidDC340 = _XcmPidDC340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 6)
)
if mibBuilder.loadTexts:
    xcmPidDC340.setStatus("current")
_XcmPidDC340ST_ObjectIdentity = ObjectIdentity
xcmPidDC340ST = _XcmPidDC340ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC340ST.setStatus("current")
_XcmPidDC340STV1_ObjectIdentity = ObjectIdentity
xcmPidDC340STV1 = _XcmPidDC340STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC340STV1.setStatus("current")
_XcmPidDC340STV2_ObjectIdentity = ObjectIdentity
xcmPidDC340STV2 = _XcmPidDC340STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC340STV2.setStatus("current")
_XcmPidDC255_ObjectIdentity = ObjectIdentity
xcmPidDC255 = _XcmPidDC255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7)
)
if mibBuilder.loadTexts:
    xcmPidDC255.setStatus("current")
_XcmPidDC255ST_ObjectIdentity = ObjectIdentity
xcmPidDC255ST = _XcmPidDC255ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC255ST.setStatus("current")
_XcmPidDC255STV1_ObjectIdentity = ObjectIdentity
xcmPidDC255STV1 = _XcmPidDC255STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC255STV1.setStatus("current")
_XcmPidDC255STV2_ObjectIdentity = ObjectIdentity
xcmPidDC255STV2 = _XcmPidDC255STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC255STV2.setStatus("current")
_XcmPidDC255STV3_ObjectIdentity = ObjectIdentity
xcmPidDC255STV3 = _XcmPidDC255STV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC255STV3.setStatus("current")
_XcmPidDC255LP_ObjectIdentity = ObjectIdentity
xcmPidDC255LP = _XcmPidDC255LP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC255LP.setStatus("current")
_XcmPidDC255LPV1_ObjectIdentity = ObjectIdentity
xcmPidDC255LPV1 = _XcmPidDC255LPV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC255LPV1.setStatus("current")
_XcmPidDC255LPV2_ObjectIdentity = ObjectIdentity
xcmPidDC255LPV2 = _XcmPidDC255LPV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC255LPV2.setStatus("current")
_XcmPidDC255LPV3_ObjectIdentity = ObjectIdentity
xcmPidDC255LPV3 = _XcmPidDC255LPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC255LPV3.setStatus("current")
_XcmPidDC220_ObjectIdentity = ObjectIdentity
xcmPidDC220 = _XcmPidDC220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 8)
)
if mibBuilder.loadTexts:
    xcmPidDC220.setStatus("current")
_XcmPidDC220ST_ObjectIdentity = ObjectIdentity
xcmPidDC220ST = _XcmPidDC220ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC220ST.setStatus("current")
_XcmPidDC220STV3_ObjectIdentity = ObjectIdentity
xcmPidDC220STV3 = _XcmPidDC220STV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC220STV3.setStatus("current")
_XcmPidDC220STV4_ObjectIdentity = ObjectIdentity
xcmPidDC220STV4 = _XcmPidDC220STV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 8, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidDC220STV4.setStatus("current")
_XcmPidDC332_ObjectIdentity = ObjectIdentity
xcmPidDC332 = _XcmPidDC332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 9)
)
if mibBuilder.loadTexts:
    xcmPidDC332.setStatus("current")
_XcmPidDC332ST_ObjectIdentity = ObjectIdentity
xcmPidDC332ST = _XcmPidDC332ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC332ST.setStatus("current")
_XcmPidDC332STV1_ObjectIdentity = ObjectIdentity
xcmPidDC332STV1 = _XcmPidDC332STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC332STV1.setStatus("current")
_XcmPidDC332STV2_ObjectIdentity = ObjectIdentity
xcmPidDC332STV2 = _XcmPidDC332STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC332STV2.setStatus("current")
_XcmPidDC4XX_ObjectIdentity = ObjectIdentity
xcmPidDC4XX = _XcmPidDC4XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 17)
)
if mibBuilder.loadTexts:
    xcmPidDC4XX.setStatus("current")
_XcmPidDC460_ObjectIdentity = ObjectIdentity
xcmPidDC460 = _XcmPidDC460_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 17, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC460.setStatus("current")
_XcmPidDC460V1_ObjectIdentity = ObjectIdentity
xcmPidDC460V1 = _XcmPidDC460V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC460V1.setStatus("current")
_XcmPidDC470_ObjectIdentity = ObjectIdentity
xcmPidDC470 = _XcmPidDC470_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 17, 4)
)
if mibBuilder.loadTexts:
    xcmPidDC470.setStatus("current")
_XcmPidDC470V1_ObjectIdentity = ObjectIdentity
xcmPidDC470V1 = _XcmPidDC470V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 17, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC470V1.setStatus("current")
_XcmPidDC420_ObjectIdentity = ObjectIdentity
xcmPidDC420 = _XcmPidDC420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 19)
)
if mibBuilder.loadTexts:
    xcmPidDC420.setStatus("current")
_XcmPidDC420ST_ObjectIdentity = ObjectIdentity
xcmPidDC420ST = _XcmPidDC420ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC420ST.setStatus("current")
_XcmPidDC420STV1_ObjectIdentity = ObjectIdentity
xcmPidDC420STV1 = _XcmPidDC420STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC420STV1.setStatus("current")
_XcmPidDC420STV2_ObjectIdentity = ObjectIdentity
xcmPidDC420STV2 = _XcmPidDC420STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 19, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC420STV2.setStatus("current")
_XcmPidDC426_ObjectIdentity = ObjectIdentity
xcmPidDC426 = _XcmPidDC426_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC426.setStatus("current")
_XcmPidDC426V1_ObjectIdentity = ObjectIdentity
xcmPidDC426V1 = _XcmPidDC426V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC426V1.setStatus("current")
_XcmPidDC432_ObjectIdentity = ObjectIdentity
xcmPidDC432 = _XcmPidDC432_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20)
)
if mibBuilder.loadTexts:
    xcmPidDC432.setStatus("current")
_XcmPidDC432ST_ObjectIdentity = ObjectIdentity
xcmPidDC432ST = _XcmPidDC432ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC432ST.setStatus("current")
_XcmPidDC432STV1_ObjectIdentity = ObjectIdentity
xcmPidDC432STV1 = _XcmPidDC432STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC432STV1.setStatus("current")
_XcmPidDC432STV2_ObjectIdentity = ObjectIdentity
xcmPidDC432STV2 = _XcmPidDC432STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC432STV2.setStatus("current")
_XcmPidDC432STV3_ObjectIdentity = ObjectIdentity
xcmPidDC432STV3 = _XcmPidDC432STV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC432STV3.setStatus("current")
_XcmPidDC432STV4_ObjectIdentity = ObjectIdentity
xcmPidDC432STV4 = _XcmPidDC432STV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidDC432STV4.setStatus("current")
_XcmPidDC432STV5_ObjectIdentity = ObjectIdentity
xcmPidDC432STV5 = _XcmPidDC432STV5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidDC432STV5.setStatus("current")
_XcmPidDC430_ObjectIdentity = ObjectIdentity
xcmPidDC430 = _XcmPidDC430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC430.setStatus("current")
_XcmPidDC430V1_ObjectIdentity = ObjectIdentity
xcmPidDC430V1 = _XcmPidDC430V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 20, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC430V1.setStatus("current")
_XcmPidDC440_ObjectIdentity = ObjectIdentity
xcmPidDC440 = _XcmPidDC440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 21)
)
if mibBuilder.loadTexts:
    xcmPidDC440.setStatus("current")
_XcmPidDC440ST_ObjectIdentity = ObjectIdentity
xcmPidDC440ST = _XcmPidDC440ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 21, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC440ST.setStatus("current")
_XcmPidDC440STV1_ObjectIdentity = ObjectIdentity
xcmPidDC440STV1 = _XcmPidDC440STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 21, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC440STV1.setStatus("current")
_XcmPidDC440STV2_ObjectIdentity = ObjectIdentity
xcmPidDC440STV2 = _XcmPidDC440STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 21, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC440STV2.setStatus("current")
_XcmPidDC440STV3_ObjectIdentity = ObjectIdentity
xcmPidDC440STV3 = _XcmPidDC440STV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 21, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidDC440STV3.setStatus("current")
_XcmPidDC230i_ObjectIdentity = ObjectIdentity
xcmPidDC230i = _XcmPidDC230i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 22)
)
if mibBuilder.loadTexts:
    xcmPidDC230i.setStatus("current")
_XcmPidDC230iST_ObjectIdentity = ObjectIdentity
xcmPidDC230iST = _XcmPidDC230iST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 22, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC230iST.setStatus("current")
_XcmPidDC230iSTV1_ObjectIdentity = ObjectIdentity
xcmPidDC230iSTV1 = _XcmPidDC230iSTV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 22, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC230iSTV1.setStatus("current")
_XcmPidDC230iSTV2_ObjectIdentity = ObjectIdentity
xcmPidDC230iSTV2 = _XcmPidDC230iSTV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 22, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC230iSTV2.setStatus("current")
_XcmPidDC4YY_ObjectIdentity = ObjectIdentity
xcmPidDC4YY = _XcmPidDC4YY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 23)
)
if mibBuilder.loadTexts:
    xcmPidDC4YY.setStatus("current")
_XcmPidDC480_ObjectIdentity = ObjectIdentity
xcmPidDC480 = _XcmPidDC480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 23, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC480.setStatus("current")
_XcmPidDC480V1_ObjectIdentity = ObjectIdentity
xcmPidDC480V1 = _XcmPidDC480V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC480V1.setStatus("current")
_XcmPidDC425_ObjectIdentity = ObjectIdentity
xcmPidDC425 = _XcmPidDC425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 24)
)
if mibBuilder.loadTexts:
    xcmPidDC425.setStatus("current")
_XcmPidDC425ST_ObjectIdentity = ObjectIdentity
xcmPidDC425ST = _XcmPidDC425ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 24, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC425ST.setStatus("current")
_XcmPidDC425STV1_ObjectIdentity = ObjectIdentity
xcmPidDC425STV1 = _XcmPidDC425STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC425STV1.setStatus("current")
_XcmPidDC555_ObjectIdentity = ObjectIdentity
xcmPidDC555 = _XcmPidDC555_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 27)
)
if mibBuilder.loadTexts:
    xcmPidDC555.setStatus("current")
_XcmPidDC555ST_ObjectIdentity = ObjectIdentity
xcmPidDC555ST = _XcmPidDC555ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 27, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC555ST.setStatus("current")
_XcmPidDC555STV1_ObjectIdentity = ObjectIdentity
xcmPidDC555STV1 = _XcmPidDC555STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 27, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC555STV1.setStatus("current")
_XcmPidDC555STV2_ObjectIdentity = ObjectIdentity
xcmPidDC555STV2 = _XcmPidDC555STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 27, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC555STV2.setStatus("current")
_XcmPidDC535_ObjectIdentity = ObjectIdentity
xcmPidDC535 = _XcmPidDC535_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 30)
)
if mibBuilder.loadTexts:
    xcmPidDC535.setStatus("current")
_XcmPidDC535ST_ObjectIdentity = ObjectIdentity
xcmPidDC535ST = _XcmPidDC535ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 30, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC535ST.setStatus("current")
_XcmPidDC535STV1_ObjectIdentity = ObjectIdentity
xcmPidDC535STV1 = _XcmPidDC535STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 30, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC535STV1.setStatus("current")
_XcmPidDC535STV2_ObjectIdentity = ObjectIdentity
xcmPidDC535STV2 = _XcmPidDC535STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 30, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC535STV2.setStatus("current")
_XcmPidDC545_ObjectIdentity = ObjectIdentity
xcmPidDC545 = _XcmPidDC545_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 31)
)
if mibBuilder.loadTexts:
    xcmPidDC545.setStatus("current")
_XcmPidDC545ST_ObjectIdentity = ObjectIdentity
xcmPidDC545ST = _XcmPidDC545ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC545ST.setStatus("current")
_XcmPidDC545STV1_ObjectIdentity = ObjectIdentity
xcmPidDC545STV1 = _XcmPidDC545STV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 31, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDC545STV1.setStatus("current")
_XcmPidDC545STV2_ObjectIdentity = ObjectIdentity
xcmPidDC545STV2 = _XcmPidDC545STV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 1, 31, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDC545STV2.setStatus("current")
_XcmPidDesktopDocuPrintPrinters_ObjectIdentity = ObjectIdentity
xcmPidDesktopDocuPrintPrinters = _XcmPidDesktopDocuPrintPrinters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDesktopDocuPrintPrinters.setStatus("current")
_XcmPid4517_ObjectIdentity = ObjectIdentity
xcmPid4517 = _XcmPid4517_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPid4517.setStatus("current")
_XcmPid4517PlusM1_ObjectIdentity = ObjectIdentity
xcmPid4517PlusM1 = _XcmPid4517PlusM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPid4517PlusM1.setStatus("current")
_XcmPid4517PlusM1V1_ObjectIdentity = ObjectIdentity
xcmPid4517PlusM1V1 = _XcmPid4517PlusM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPid4517PlusM1V1.setStatus("current")
_XcmPidDocuPrintN17_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN17 = _XcmPidDocuPrintN17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN17.setStatus("current")
_XcmPidDocuPrintN17V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN17V1 = _XcmPidDocuPrintN17V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN17V1.setStatus("current")
_XcmPidDocuPrintC55_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintC55 = _XcmPidDocuPrintC55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintC55.setStatus("current")
_XcmPidDocuPrintC55M1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintC55M1 = _XcmPidDocuPrintC55M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintC55M1.setStatus("current")
_XcmPidDocuPrintC55M1V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintC55M1V1 = _XcmPidDocuPrintC55M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintC55M1V1.setStatus("current")
_XcmPidDocuPrintC55M1V2_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintC55M1V2 = _XcmPidDocuPrintC55M1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintC55M1V2.setStatus("current")
_XcmPidDocuPrintNC60_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNC60 = _XcmPidDocuPrintNC60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNC60.setStatus("current")
_XcmPidDocuPrintNC60V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNC60V1 = _XcmPidDocuPrintNC60V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNC60V1.setStatus("current")
_XcmPidP1210_ObjectIdentity = ObjectIdentity
xcmPidP1210 = _XcmPidP1210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 4)
)
if mibBuilder.loadTexts:
    xcmPidP1210.setStatus("current")
_XcmPidP1210M1_ObjectIdentity = ObjectIdentity
xcmPidP1210M1 = _XcmPidP1210M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidP1210M1.setStatus("current")
_XcmPidP1210M1V1_ObjectIdentity = ObjectIdentity
xcmPidP1210M1V1 = _XcmPidP1210M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidP1210M1V1.setStatus("current")
_XcmPidP3400_ObjectIdentity = ObjectIdentity
xcmPidP3400 = _XcmPidP3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 5)
)
if mibBuilder.loadTexts:
    xcmPidP3400.setStatus("current")
_XcmPidP3400M1_ObjectIdentity = ObjectIdentity
xcmPidP3400M1 = _XcmPidP3400M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidP3400M1.setStatus("current")
_XcmPidP3400M1V1_ObjectIdentity = ObjectIdentity
xcmPidP3400M1V1 = _XcmPidP3400M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidP3400M1V1.setStatus("current")
_XcmPidWorkGroupDocuPrintPrinters_ObjectIdentity = ObjectIdentity
xcmPidWorkGroupDocuPrintPrinters = _XcmPidWorkGroupDocuPrintPrinters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidWorkGroupDocuPrintPrinters.setStatus("current")
_XcmPidDocuPrintNnn_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNnn = _XcmPidDocuPrintNnn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNnn.setStatus("current")
_XcmPidDocuPrintN32_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN32 = _XcmPidDocuPrintN32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN32.setStatus("current")
_XcmPidDocuPrintN32V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN32V1 = _XcmPidDocuPrintN32V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN32V1.setStatus("current")
_XcmPidDocuPrintN32V2_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN32V2 = _XcmPidDocuPrintN32V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN32V2.setStatus("current")
_XcmPidDocuPrintN24_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN24 = _XcmPidDocuPrintN24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN24.setStatus("current")
_XcmPidDocuPrintN24V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN24V1 = _XcmPidDocuPrintN24V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN24V1.setStatus("current")
_XcmPidDocuPrintN24V2_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN24V2 = _XcmPidDocuPrintN24V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN24V2.setStatus("current")
_XcmPidDocuPrintN40_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN40 = _XcmPidDocuPrintN40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN40.setStatus("current")
_XcmPidDocuPrintN40V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN40V1 = _XcmPidDocuPrintN40V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN40V1.setStatus("current")
_XcmPidDocuPrintN2025_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2025 = _XcmPidDocuPrintN2025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 17)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2025.setStatus("current")
_XcmPidDocuPrintN2025V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2025V1 = _XcmPidDocuPrintN2025V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2025V1.setStatus("current")
_XcmPidDocuPrintN2025V2_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2025V2 = _XcmPidDocuPrintN2025V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 17, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2025V2.setStatus("current")
_XcmPidDocuPrintN2125_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2125 = _XcmPidDocuPrintN2125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 18)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2125.setStatus("current")
_XcmPidDocuPrintN2125V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2125V1 = _XcmPidDocuPrintN2125V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2125V1.setStatus("current")
_XcmPidDocuPrintN2425_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2425 = _XcmPidDocuPrintN2425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 19)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2425.setStatus("current")
_XcmPidDocuPrintN2425V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2425V1 = _XcmPidDocuPrintN2425V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2425V1.setStatus("current")
_XcmPidDocuPrintN2825_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2825 = _XcmPidDocuPrintN2825_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 20)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2825.setStatus("current")
_XcmPidDocuPrintN2825V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN2825V1 = _XcmPidDocuPrintN2825V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN2825V1.setStatus("current")
_XcmPidDocuPrintN3225_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN3225 = _XcmPidDocuPrintN3225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 21)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN3225.setStatus("current")
_XcmPidDocuPrintN3225V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN3225V1 = _XcmPidDocuPrintN3225V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 21, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN3225V1.setStatus("current")
_XcmPidDocuPrintN4025_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN4025 = _XcmPidDocuPrintN4025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 22)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN4025.setStatus("current")
_XcmPidDocuPrintN4025V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN4025V1 = _XcmPidDocuPrintN4025V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 22, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN4025V1.setStatus("current")
_XcmPidDocuPrintN4025V2_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN4025V2 = _XcmPidDocuPrintN4025V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 22, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN4025V2.setStatus("current")
_XcmPidDocuPrintAyame35_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintAyame35 = _XcmPidDocuPrintAyame35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 35)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintAyame35.setStatus("current")
_XcmPidDocuPrintAyame35V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintAyame35V1 = _XcmPidDocuPrintAyame35V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 35, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintAyame35V1.setStatus("current")
_XcmPidDocuPrintN4525_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN4525 = _XcmPidDocuPrintN4525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 36)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN4525.setStatus("current")
_XcmPidDocuPrintN4525V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintN4525V1 = _XcmPidDocuPrintN4525V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 36, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintN4525V1.setStatus("current")
_XcmPidPhaser5400_ObjectIdentity = ObjectIdentity
xcmPidPhaser5400 = _XcmPidPhaser5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 37)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5400.setStatus("current")
_XcmPidPhaser5400V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser5400V1 = _XcmPidPhaser5400V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 2, 37, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5400V1.setStatus("current")
_XcmPidDocuPrintNCnn_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNCnn = _XcmPidDocuPrintNCnn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 3)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNCnn.setStatus("current")
_XcmPidDocuPrintNC70_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNC70 = _XcmPidDocuPrintNC70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNC70.setStatus("current")
_XcmPidDocuPrintNC70V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNC70V1 = _XcmPidDocuPrintNC70V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNC70V1.setStatus("current")
_XcmPidDocuPrintNC80_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNC80 = _XcmPidDocuPrintNC80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNC80.setStatus("current")
_XcmPidDocuPrintNC80V1_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNC80V1 = _XcmPidDocuPrintNC80V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNC80V1.setStatus("current")
_XcmPidMidRangeColorPrinters_ObjectIdentity = ObjectIdentity
xcmPidMidRangeColorPrinters = _XcmPidMidRangeColorPrinters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidMidRangeColorPrinters.setStatus("current")
_XcmPidDCColorSeries50_ObjectIdentity = ObjectIdentity
xcmPidDCColorSeries50 = _XcmPidDCColorSeries50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 4, 2)
)
if mibBuilder.loadTexts:
    xcmPidDCColorSeries50.setStatus("current")
_XcmPidDCColorSeries50M1_ObjectIdentity = ObjectIdentity
xcmPidDCColorSeries50M1 = _XcmPidDCColorSeries50M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDCColorSeries50M1.setStatus("current")
_XcmPidDCColorSeries50M1V1_ObjectIdentity = ObjectIdentity
xcmPidDCColorSeries50M1V1 = _XcmPidDCColorSeries50M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDCColorSeries50M1V1.setStatus("current")
_XcmPidDocuTechs_ObjectIdentity = ObjectIdentity
xcmPidDocuTechs = _XcmPidDocuTechs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidDocuTechs.setStatus("current")
_XcmPidDocuTech6135_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6135 = _XcmPidDocuTech6135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6135.setStatus("current")
_XcmPidDocuTech6135M1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6135M1 = _XcmPidDocuTech6135M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6135M1.setStatus("current")
_XcmPidDocuTech6135M1V1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6135M1V1 = _XcmPidDocuTech6135M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6135M1V1.setStatus("current")
_XcmPidDocuTech6135M1V2_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6135M1V2 = _XcmPidDocuTech6135M1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6135M1V2.setStatus("current")
_XcmPidDocuTech6180_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6180 = _XcmPidDocuTech6180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 3)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6180.setStatus("current")
_XcmPidDocuTech6180M1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6180M1 = _XcmPidDocuTech6180M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6180M1.setStatus("current")
_XcmPidDocuTech6180M1V1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6180M1V1 = _XcmPidDocuTech6180M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6180M1V1.setStatus("current")
_XcmPidDocuTech6180M1V2_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6180M1V2 = _XcmPidDocuTech6180M1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6180M1V2.setStatus("current")
_XcmPidDocuTech6100_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6100 = _XcmPidDocuTech6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 4)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6100.setStatus("current")
_XcmPidDocuTech6100M1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6100M1 = _XcmPidDocuTech6100M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6100M1.setStatus("current")
_XcmPidDocuTech6100M1V1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6100M1V1 = _XcmPidDocuTech6100M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6100M1V1.setStatus("current")
_XcmPidDocuTech6100M1V2_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6100M1V2 = _XcmPidDocuTech6100M1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6100M1V2.setStatus("current")
_XcmPidDocuTech6115_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6115 = _XcmPidDocuTech6115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 5)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6115.setStatus("current")
_XcmPidDocuTech6115M1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6115M1 = _XcmPidDocuTech6115M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6115M1.setStatus("current")
_XcmPidDocuTech6115M1V1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6115M1V1 = _XcmPidDocuTech6115M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6115M1V1.setStatus("current")
_XcmPidDocuTech6115M1V2_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6115M1V2 = _XcmPidDocuTech6115M1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 5, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6115M1V2.setStatus("current")
_XcmPidDocuTech6155_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6155 = _XcmPidDocuTech6155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 6)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6155.setStatus("current")
_XcmPidDocuTech6155M1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6155M1 = _XcmPidDocuTech6155M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6155M1.setStatus("current")
_XcmPidDocuTech6155M1V1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6155M1V1 = _XcmPidDocuTech6155M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6155M1V1.setStatus("current")
_XcmPidDocuTech6155M1V2_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6155M1V2 = _XcmPidDocuTech6155M1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 6, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6155M1V2.setStatus("current")
_XcmPidDocuTech6075_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6075 = _XcmPidDocuTech6075_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 7)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6075.setStatus("current")
_XcmPidDocuTech6075M1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6075M1 = _XcmPidDocuTech6075M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 7, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6075M1.setStatus("current")
_XcmPidDocuTech6075M1V1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6075M1V1 = _XcmPidDocuTech6075M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 7, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6075M1V1.setStatus("current")
_XcmPidDocuTech6090_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6090 = _XcmPidDocuTech6090_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 8)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6090.setStatus("current")
_XcmPidDocuTech6090M1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6090M1 = _XcmPidDocuTech6090M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 8, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6090M1.setStatus("current")
_XcmPidDocuTech6090M1V1_ObjectIdentity = ObjectIdentity
xcmPidDocuTech6090M1V1 = _XcmPidDocuTech6090M1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 8, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuTech6090M1V1.setStatus("current")
_XcmPidDocuTechHiColorEPS_ObjectIdentity = ObjectIdentity
xcmPidDocuTechHiColorEPS = _XcmPidDocuTechHiColorEPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 19)
)
if mibBuilder.loadTexts:
    xcmPidDocuTechHiColorEPS.setStatus("current")
_XcmPidDocuSPDFE_ObjectIdentity = ObjectIdentity
xcmPidDocuSPDFE = _XcmPidDocuSPDFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 20)
)
if mibBuilder.loadTexts:
    xcmPidDocuSPDFE.setStatus("current")
_XcmPidDocuSPDFEColor_ObjectIdentity = ObjectIdentity
xcmPidDocuSPDFEColor = _XcmPidDocuSPDFEColor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 21)
)
if mibBuilder.loadTexts:
    xcmPidDocuSPDFEColor.setStatus("current")
_XcmPidDocuSPTEAK_ObjectIdentity = ObjectIdentity
xcmPidDocuSPTEAK = _XcmPidDocuSPTEAK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 5, 22)
)
if mibBuilder.loadTexts:
    xcmPidDocuSPTEAK.setStatus("current")
_XcmPidDedPrintServers_ObjectIdentity = ObjectIdentity
xcmPidDedPrintServers = _XcmPidDedPrintServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 8)
)
if mibBuilder.loadTexts:
    xcmPidDedPrintServers.setStatus("current")
_XcmPidPhaserPrintServer_ObjectIdentity = ObjectIdentity
xcmPidPhaserPrintServer = _XcmPidPhaserPrintServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 8, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaserPrintServer.setStatus("current")
_XcmPidPhaserEX7750_ObjectIdentity = ObjectIdentity
xcmPidPhaserEX7750 = _XcmPidPhaserEX7750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaserEX7750.setStatus("current")
_XcmPidPhaserEX7750GX_ObjectIdentity = ObjectIdentity
xcmPidPhaserEX7750GX = _XcmPidPhaserEX7750GX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaserEX7750GX.setStatus("current")
_XcmPidPhaserEX7750DXF_ObjectIdentity = ObjectIdentity
xcmPidPhaserEX7750DXF = _XcmPidPhaserEX7750DXF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaserEX7750DXF.setStatus("current")
_XcmPidDocuPrintNPS_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintNPS = _XcmPidDocuPrintNPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintNPS.setStatus("current")
_XcmPidDP4050NPS_ObjectIdentity = ObjectIdentity
xcmPidDP4050NPS = _XcmPidDP4050NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4050NPS.setStatus("current")
_XcmPidDP4050NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP4050NPSM1 = _XcmPidDP4050NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4050NPSM1.setStatus("current")
_XcmPidDP4050NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP4050NPSM1V1 = _XcmPidDP4050NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4050NPSM1V1.setStatus("current")
_XcmPidDP4090NPS_ObjectIdentity = ObjectIdentity
xcmPidDP4090NPS = _XcmPidDP4090NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP4090NPS.setStatus("current")
_XcmPidDP4090NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP4090NPSM1 = _XcmPidDP4090NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4090NPSM1.setStatus("current")
_XcmPidDP4090NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP4090NPSM1V1 = _XcmPidDP4090NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4090NPSM1V1.setStatus("current")
_XcmPidDP4850NPS_ObjectIdentity = ObjectIdentity
xcmPidDP4850NPS = _XcmPidDP4850NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 3)
)
if mibBuilder.loadTexts:
    xcmPidDP4850NPS.setStatus("current")
_XcmPidDP4850NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP4850NPSM1 = _XcmPidDP4850NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4850NPSM1.setStatus("current")
_XcmPidDP4850NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP4850NPSM1V1 = _XcmPidDP4850NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4850NPSM1V1.setStatus("current")
_XcmPidDP4890NPS_ObjectIdentity = ObjectIdentity
xcmPidDP4890NPS = _XcmPidDP4890NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 4)
)
if mibBuilder.loadTexts:
    xcmPidDP4890NPS.setStatus("current")
_XcmPidDP4890NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP4890NPSM1 = _XcmPidDP4890NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4890NPSM1.setStatus("current")
_XcmPidDP4890NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP4890NPSM1V1 = _XcmPidDP4890NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4890NPSM1V1.setStatus("current")
_XcmPidDP4635NPS_ObjectIdentity = ObjectIdentity
xcmPidDP4635NPS = _XcmPidDP4635NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 5)
)
if mibBuilder.loadTexts:
    xcmPidDP4635NPS.setStatus("current")
_XcmPidDP4635NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP4635NPSM1 = _XcmPidDP4635NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4635NPSM1.setStatus("current")
_XcmPidDP4635NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP4635NPSM1V1 = _XcmPidDP4635NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4635NPSM1V1.setStatus("current")
_XcmPidDP4635NPSMicr_ObjectIdentity = ObjectIdentity
xcmPidDP4635NPSMicr = _XcmPidDP4635NPSMicr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 5, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP4635NPSMicr.setStatus("current")
_XcmPidDP4635NPSMicrV1_ObjectIdentity = ObjectIdentity
xcmPidDP4635NPSMicrV1 = _XcmPidDP4635NPSMicrV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 5, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP4635NPSMicrV1.setStatus("current")
_XcmPidDP180NPS_ObjectIdentity = ObjectIdentity
xcmPidDP180NPS = _XcmPidDP180NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 6)
)
if mibBuilder.loadTexts:
    xcmPidDP180NPS.setStatus("current")
_XcmPidDP180NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP180NPSM1 = _XcmPidDP180NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP180NPSM1.setStatus("current")
_XcmPidDP180NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP180NPSM1V1 = _XcmPidDP180NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 6, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP180NPSM1V1.setStatus("current")
_XcmPidDP180NPSMicr_ObjectIdentity = ObjectIdentity
xcmPidDP180NPSMicr = _XcmPidDP180NPSMicr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 6, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP180NPSMicr.setStatus("current")
_XcmPidDP180NPSMicrV1_ObjectIdentity = ObjectIdentity
xcmPidDP180NPSMicrV1 = _XcmPidDP180NPSMicrV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 6, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP180NPSMicrV1.setStatus("current")
_XcmPidDP96NPS_ObjectIdentity = ObjectIdentity
xcmPidDP96NPS = _XcmPidDP96NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 7)
)
if mibBuilder.loadTexts:
    xcmPidDP96NPS.setStatus("current")
_XcmPidDP96NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP96NPSM1 = _XcmPidDP96NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 7, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP96NPSM1.setStatus("current")
_XcmPidDP96NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP96NPSM1V1 = _XcmPidDP96NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 7, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP96NPSM1V1.setStatus("current")
_XcmPidDP96NPSMicr_ObjectIdentity = ObjectIdentity
xcmPidDP96NPSMicr = _XcmPidDP96NPSMicr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 7, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP96NPSMicr.setStatus("current")
_XcmPidDP96NPSMicrV1_ObjectIdentity = ObjectIdentity
xcmPidDP96NPSMicrV1 = _XcmPidDP96NPSMicrV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 7, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP96NPSMicrV1.setStatus("current")
_XcmPidDP92cNPS_ObjectIdentity = ObjectIdentity
xcmPidDP92cNPS = _XcmPidDP92cNPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 8)
)
if mibBuilder.loadTexts:
    xcmPidDP92cNPS.setStatus("current")
_XcmPidDP92cNPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP92cNPSM1 = _XcmPidDP92cNPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 8, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP92cNPSM1.setStatus("current")
_XcmPidDP92cNPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP92cNPSM1V1 = _XcmPidDP92cNPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 8, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP92cNPSM1V1.setStatus("current")
_XcmPidDP155NPS_ObjectIdentity = ObjectIdentity
xcmPidDP155NPS = _XcmPidDP155NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 9)
)
if mibBuilder.loadTexts:
    xcmPidDP155NPS.setStatus("current")
_XcmPidDP155NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP155NPSM1 = _XcmPidDP155NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP155NPSM1.setStatus("current")
_XcmPidDP155NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP155NPSM1V1 = _XcmPidDP155NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 9, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP155NPSM1V1.setStatus("current")
_XcmPidDP155NPSMicr_ObjectIdentity = ObjectIdentity
xcmPidDP155NPSMicr = _XcmPidDP155NPSMicr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 9, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP155NPSMicr.setStatus("current")
_XcmPidDP155NPSMicrV1_ObjectIdentity = ObjectIdentity
xcmPidDP155NPSMicrV1 = _XcmPidDP155NPSMicrV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 9, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP155NPSMicrV1.setStatus("current")
_XcmPidDP115NPS_ObjectIdentity = ObjectIdentity
xcmPidDP115NPS = _XcmPidDP115NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 17)
)
if mibBuilder.loadTexts:
    xcmPidDP115NPS.setStatus("current")
_XcmPidDP115NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP115NPSM1 = _XcmPidDP115NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP115NPSM1.setStatus("current")
_XcmPidDP115NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP115NPSM1V1 = _XcmPidDP115NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 17, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP115NPSM1V1.setStatus("current")
_XcmPidDP115NPSMicr_ObjectIdentity = ObjectIdentity
xcmPidDP115NPSMicr = _XcmPidDP115NPSMicr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 17, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP115NPSMicr.setStatus("current")
_XcmPidDP115NPSMicrV1_ObjectIdentity = ObjectIdentity
xcmPidDP115NPSMicrV1 = _XcmPidDP115NPSMicrV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 17, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP115NPSMicrV1.setStatus("current")
_XcmPidDP100NPS_ObjectIdentity = ObjectIdentity
xcmPidDP100NPS = _XcmPidDP100NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 18)
)
if mibBuilder.loadTexts:
    xcmPidDP100NPS.setStatus("current")
_XcmPidDP100NPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP100NPSM1 = _XcmPidDP100NPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP100NPSM1.setStatus("current")
_XcmPidDP100NPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP100NPSM1V1 = _XcmPidDP100NPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 18, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP100NPSM1V1.setStatus("current")
_XcmPidDP100NPSMicr_ObjectIdentity = ObjectIdentity
xcmPidDP100NPSMicr = _XcmPidDP100NPSMicr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 18, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP100NPSMicr.setStatus("current")
_XcmPidDP100NPSMicrV1_ObjectIdentity = ObjectIdentity
xcmPidDP100NPSMicrV1 = _XcmPidDP100NPSMicrV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 18, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP100NPSMicrV1.setStatus("current")
_XcmPidDC2000FamilyNPS_ObjectIdentity = ObjectIdentity
xcmPidDC2000FamilyNPS = _XcmPidDC2000FamilyNPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 19)
)
if mibBuilder.loadTexts:
    xcmPidDC2000FamilyNPS.setStatus("current")
_XcmPidDocuColor2045NPS_ObjectIdentity = ObjectIdentity
xcmPidDocuColor2045NPS = _XcmPidDocuColor2045NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor2045NPS.setStatus("current")
_XcmPidDocuColor2045NPSV1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor2045NPSV1 = _XcmPidDocuColor2045NPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 19, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor2045NPSV1.setStatus("current")
_XcmPidDocuColor2060NPS_ObjectIdentity = ObjectIdentity
xcmPidDocuColor2060NPS = _XcmPidDocuColor2060NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 19, 2)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor2060NPS.setStatus("current")
_XcmPidDocuColor2060NPSV1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor2060NPSV1 = _XcmPidDocuColor2060NPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 19, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor2060NPSV1.setStatus("current")
_XcmPidDocuColor5252NPS_ObjectIdentity = ObjectIdentity
xcmPidDocuColor5252NPS = _XcmPidDocuColor5252NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 19, 3)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor5252NPS.setStatus("current")
_XcmPidDocuColor5252NPSV1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor5252NPSV1 = _XcmPidDocuColor5252NPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 19, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor5252NPSV1.setStatus("current")
_XcmPidDC6000FamilyNPS_ObjectIdentity = ObjectIdentity
xcmPidDC6000FamilyNPS = _XcmPidDC6000FamilyNPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 20)
)
if mibBuilder.loadTexts:
    xcmPidDC6000FamilyNPS.setStatus("current")
_XcmPidDocuColor6060NPS_ObjectIdentity = ObjectIdentity
xcmPidDocuColor6060NPS = _XcmPidDocuColor6060NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor6060NPS.setStatus("current")
_XcmPidDocuColor6060NPSV1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor6060NPSV1 = _XcmPidDocuColor6060NPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 9, 20, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor6060NPSV1.setStatus("current")
_XcmPidDocuColor2000Series_ObjectIdentity = ObjectIdentity
xcmPidDocuColor2000Series = _XcmPidDocuColor2000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor2000Series.setStatus("current")
_XcmPidDocuColor3000series_ObjectIdentity = ObjectIdentity
xcmPidDocuColor3000series = _XcmPidDocuColor3000series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor3000series.setStatus("current")
_XcmPidDocuColor240SPLASH_ObjectIdentity = ObjectIdentity
xcmPidDocuColor240SPLASH = _XcmPidDocuColor240SPLASH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 8)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor240SPLASH.setStatus("current")
_XcmPidDocuColor240SPLASHv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor240SPLASHv1 = _XcmPidDocuColor240SPLASHv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 8, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor240SPLASHv1.setStatus("current")
_XcmPidDocuColor250SPLASH_ObjectIdentity = ObjectIdentity
xcmPidDocuColor250SPLASH = _XcmPidDocuColor250SPLASH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 9)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor250SPLASH.setStatus("current")
_XcmPidDocuColor250SPLASHv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor250SPLASHv1 = _XcmPidDocuColor250SPLASHv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor250SPLASHv1.setStatus("current")
_XcmPidDocuColor242EFI_ObjectIdentity = ObjectIdentity
xcmPidDocuColor242EFI = _XcmPidDocuColor242EFI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 17)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor242EFI.setStatus("current")
_XcmPidDocuColor242EFIv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor242EFIv1 = _XcmPidDocuColor242EFIv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor242EFIv1.setStatus("current")
_XcmPidDocuColor242_ObjectIdentity = ObjectIdentity
xcmPidDocuColor242 = _XcmPidDocuColor242_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 18)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor242.setStatus("current")
_XcmPidDocuColor242v1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor242v1 = _XcmPidDocuColor242v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor242v1.setStatus("current")
_XcmPidDocuColor252EFI_ObjectIdentity = ObjectIdentity
xcmPidDocuColor252EFI = _XcmPidDocuColor252EFI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 19)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor252EFI.setStatus("current")
_XcmPidDocuColor252EFIv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor252EFIv1 = _XcmPidDocuColor252EFIv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor252EFIv1.setStatus("current")
_XcmPidDocuColor252_ObjectIdentity = ObjectIdentity
xcmPidDocuColor252 = _XcmPidDocuColor252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 20)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor252.setStatus("current")
_XcmPidDocuColor252v1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor252v1 = _XcmPidDocuColor252v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor252v1.setStatus("current")
_XcmPidDocuColor260EFI_ObjectIdentity = ObjectIdentity
xcmPidDocuColor260EFI = _XcmPidDocuColor260EFI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 21)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor260EFI.setStatus("current")
_XcmPidDocuColor260EFIv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor260EFIv1 = _XcmPidDocuColor260EFIv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 21, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor260EFIv1.setStatus("current")
_XcmPidDocuColor260_ObjectIdentity = ObjectIdentity
xcmPidDocuColor260 = _XcmPidDocuColor260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 22)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor260.setStatus("current")
_XcmPidDocuColor260v1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor260v1 = _XcmPidDocuColor260v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 22, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor260v1.setStatus("current")
_XcmPidDocuColor242C_ObjectIdentity = ObjectIdentity
xcmPidDocuColor242C = _XcmPidDocuColor242C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 23)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor242C.setStatus("current")
_XcmPidDocuColor242Cv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor242Cv1 = _XcmPidDocuColor242Cv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 23, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor242Cv1.setStatus("current")
_XcmPidDocuColor242S_ObjectIdentity = ObjectIdentity
xcmPidDocuColor242S = _XcmPidDocuColor242S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 24)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor242S.setStatus("current")
_XcmPidDocuColor242Sv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor242Sv1 = _XcmPidDocuColor242Sv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 24, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor242Sv1.setStatus("current")
_XcmPidDocuColor252C_ObjectIdentity = ObjectIdentity
xcmPidDocuColor252C = _XcmPidDocuColor252C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 25)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor252C.setStatus("current")
_XcmPidDocuColor252Cv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor252Cv1 = _XcmPidDocuColor252Cv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 25, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor252Cv1.setStatus("current")
_XcmPidDocuColor252S_ObjectIdentity = ObjectIdentity
xcmPidDocuColor252S = _XcmPidDocuColor252S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 26)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor252S.setStatus("current")
_XcmPidDocuColor252Sv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor252Sv1 = _XcmPidDocuColor252Sv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 26, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor252Sv1.setStatus("current")
_XcmPidDocuColor260C_ObjectIdentity = ObjectIdentity
xcmPidDocuColor260C = _XcmPidDocuColor260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 27)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor260C.setStatus("current")
_XcmPidDocuColor260Cv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor260Cv1 = _XcmPidDocuColor260Cv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 27, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor260Cv1.setStatus("current")
_XcmPidDocuColor260S_ObjectIdentity = ObjectIdentity
xcmPidDocuColor260S = _XcmPidDocuColor260S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 28)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor260S.setStatus("current")
_XcmPidDocuColor260Sv1_ObjectIdentity = ObjectIdentity
xcmPidDocuColor260Sv1 = _XcmPidDocuColor260Sv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 17, 7, 28, 1)
)
if mibBuilder.loadTexts:
    xcmPidDocuColor260Sv1.setStatus("current")
_XcmPidDocuPrintEPS_ObjectIdentity = ObjectIdentity
xcmPidDocuPrintEPS = _XcmPidDocuPrintEPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18)
)
if mibBuilder.loadTexts:
    xcmPidDocuPrintEPS.setStatus("current")
_XcmPidDP180EPS_ObjectIdentity = ObjectIdentity
xcmPidDP180EPS = _XcmPidDP180EPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP180EPS.setStatus("current")
_XcmPidDP180EPSM1_ObjectIdentity = ObjectIdentity
xcmPidDP180EPSM1 = _XcmPidDP180EPSM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP180EPSM1.setStatus("current")
_XcmPidDP180EPSM1V1_ObjectIdentity = ObjectIdentity
xcmPidDP180EPSM1V1 = _XcmPidDP180EPSM1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP180EPSM1V1.setStatus("current")
_XcmPidDP180EPSMicr_ObjectIdentity = ObjectIdentity
xcmPidDP180EPSMicr = _XcmPidDP180EPSMicr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP180EPSMicr.setStatus("current")
_XcmPidDP180EPSMicrV1_ObjectIdentity = ObjectIdentity
xcmPidDP180EPSMicrV1 = _XcmPidDP180EPSMicrV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP180EPSMicrV1.setStatus("current")
_XcmPidDP2000EPS_ObjectIdentity = ObjectIdentity
xcmPidDP2000EPS = _XcmPidDP2000EPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP2000EPS.setStatus("current")
_XcmPidDP2000S100EPS_ObjectIdentity = ObjectIdentity
xcmPidDP2000S100EPS = _XcmPidDP2000S100EPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S100EPS.setStatus("current")
_XcmPidDP2000S100EPSV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S100EPSV1 = _XcmPidDP2000S100EPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S100EPSV1.setStatus("current")
_XcmPidDP2000S115EPS_ObjectIdentity = ObjectIdentity
xcmPidDP2000S115EPS = _XcmPidDP2000S115EPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S115EPS.setStatus("current")
_XcmPidDP2000S115EPSV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S115EPSV1 = _XcmPidDP2000S115EPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S115EPSV1.setStatus("current")
_XcmPidDP2000S135EPS_ObjectIdentity = ObjectIdentity
xcmPidDP2000S135EPS = _XcmPidDP2000S135EPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S135EPS.setStatus("current")
_XcmPidDP2000S135EPSV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S135EPSV1 = _XcmPidDP2000S135EPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S135EPSV1.setStatus("current")
_XcmPidDP2000S155EPS_ObjectIdentity = ObjectIdentity
xcmPidDP2000S155EPS = _XcmPidDP2000S155EPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 4)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S155EPS.setStatus("current")
_XcmPidDP2000S155EPSV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S155EPSV1 = _XcmPidDP2000S155EPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S155EPSV1.setStatus("current")
_XcmPidDP2000S180EPS_ObjectIdentity = ObjectIdentity
xcmPidDP2000S180EPS = _XcmPidDP2000S180EPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 5)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S180EPS.setStatus("current")
_XcmPidDP2000S180EPSV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S180EPSV1 = _XcmPidDP2000S180EPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S180EPSV1.setStatus("current")
_XcmPidDP2000S6075_ObjectIdentity = ObjectIdentity
xcmPidDP2000S6075 = _XcmPidDP2000S6075_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 6)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S6075.setStatus("current")
_XcmPidDP2000S6075V1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S6075V1 = _XcmPidDP2000S6075V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S6075V1.setStatus("current")
_XcmPidDP2000S6090_ObjectIdentity = ObjectIdentity
xcmPidDP2000S6090 = _XcmPidDP2000S6090_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 7)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S6090.setStatus("current")
_XcmPidDP2000S6090V1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S6090V1 = _XcmPidDP2000S6090V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 7, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S6090V1.setStatus("current")
_XcmPidDP2000S100EPSMX_ObjectIdentity = ObjectIdentity
xcmPidDP2000S100EPSMX = _XcmPidDP2000S100EPSMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 8)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S100EPSMX.setStatus("current")
_XcmPidDP2000S100EPSMXV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S100EPSMXV1 = _XcmPidDP2000S100EPSMXV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 8, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S100EPSMXV1.setStatus("current")
_XcmPidDP2000S115EPSMX_ObjectIdentity = ObjectIdentity
xcmPidDP2000S115EPSMX = _XcmPidDP2000S115EPSMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 9)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S115EPSMX.setStatus("current")
_XcmPidDP2000S115EPSMXV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S115EPSMXV1 = _XcmPidDP2000S115EPSMXV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S115EPSMXV1.setStatus("current")
_XcmPidDP2000S135EPSMX_ObjectIdentity = ObjectIdentity
xcmPidDP2000S135EPSMX = _XcmPidDP2000S135EPSMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 17)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S135EPSMX.setStatus("current")
_XcmPidDP2000S135EPSMXV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S135EPSMXV1 = _XcmPidDP2000S135EPSMXV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S135EPSMXV1.setStatus("current")
_XcmPidDP2000S155EPSMX_ObjectIdentity = ObjectIdentity
xcmPidDP2000S155EPSMX = _XcmPidDP2000S155EPSMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 18)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S155EPSMX.setStatus("current")
_XcmPidDP2000S155EPSMXV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S155EPSMXV1 = _XcmPidDP2000S155EPSMXV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S155EPSMXV1.setStatus("current")
_XcmPidDP2000S180EPSMX_ObjectIdentity = ObjectIdentity
xcmPidDP2000S180EPSMX = _XcmPidDP2000S180EPSMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 19)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S180EPSMX.setStatus("current")
_XcmPidDP2000S180EPSMXV1_ObjectIdentity = ObjectIdentity
xcmPidDP2000S180EPSMXV1 = _XcmPidDP2000S180EPSMXV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 18, 2, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidDP2000S180EPSMXV1.setStatus("current")
_XcmPidXeroxPhaserPrinters_ObjectIdentity = ObjectIdentity
xcmPidXeroxPhaserPrinters = _XcmPidXeroxPhaserPrinters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19)
)
if mibBuilder.loadTexts:
    xcmPidXeroxPhaserPrinters.setStatus("current")
_XcmPidPhaser3yyyFamily_ObjectIdentity = ObjectIdentity
xcmPidPhaser3yyyFamily = _XcmPidPhaser3yyyFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3yyyFamily.setStatus("current")
_XcmPidPhaser3450_ObjectIdentity = ObjectIdentity
xcmPidPhaser3450 = _XcmPidPhaser3450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3450.setStatus("current")
_XcmPidPhaser3450D_ObjectIdentity = ObjectIdentity
xcmPidPhaser3450D = _XcmPidPhaser3450D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3450D.setStatus("current")
_XcmPidPhaser3450DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser3450DN = _XcmPidPhaser3450DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3450DN.setStatus("current")
_XcmPidPhaser3450B_ObjectIdentity = ObjectIdentity
xcmPidPhaser3450B = _XcmPidPhaser3450B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3450B.setStatus("current")
_XcmPidPhaser3500_ObjectIdentity = ObjectIdentity
xcmPidPhaser3500 = _XcmPidPhaser3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3500.setStatus("current")
_XcmPidPhaser3500b_ObjectIdentity = ObjectIdentity
xcmPidPhaser3500b = _XcmPidPhaser3500b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3500b.setStatus("current")
_XcmPidPhaser3500n_ObjectIdentity = ObjectIdentity
xcmPidPhaser3500n = _XcmPidPhaser3500n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3500n.setStatus("current")
_XcmPidPhaser3150_ObjectIdentity = ObjectIdentity
xcmPidPhaser3150 = _XcmPidPhaser3150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3150.setStatus("current")
_XcmPidPhaser3150b_ObjectIdentity = ObjectIdentity
xcmPidPhaser3150b = _XcmPidPhaser3150b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3150b.setStatus("current")
_XcmPidPhaser3150n_ObjectIdentity = ObjectIdentity
xcmPidPhaser3150n = _XcmPidPhaser3150n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3150n.setStatus("current")
_XcmPidPhaser3428_ObjectIdentity = ObjectIdentity
xcmPidPhaser3428 = _XcmPidPhaser3428_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3428.setStatus("current")
_XcmPidPhaser3428v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3428v1 = _XcmPidPhaser3428v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3428v1.setStatus("current")
_XcmPidPhaser3124_ObjectIdentity = ObjectIdentity
xcmPidPhaser3124 = _XcmPidPhaser3124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3124.setStatus("current")
_XcmPidPhaser3124v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3124v1 = _XcmPidPhaser3124v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3124v1.setStatus("current")
_XcmPidPhaser3125_ObjectIdentity = ObjectIdentity
xcmPidPhaser3125 = _XcmPidPhaser3125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 6)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3125.setStatus("current")
_XcmPidPhaser3125v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3125v1 = _XcmPidPhaser3125v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3125v1.setStatus("current")
_XcmPidPhaser3250_ObjectIdentity = ObjectIdentity
xcmPidPhaser3250 = _XcmPidPhaser3250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 8)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3250.setStatus("current")
_XcmPidPhaser3250v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3250v1 = _XcmPidPhaser3250v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 8, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3250v1.setStatus("current")
_XcmPidPhaser3600_ObjectIdentity = ObjectIdentity
xcmPidPhaser3600 = _XcmPidPhaser3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 9)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3600.setStatus("current")
_XcmPidPhaser3600v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3600v1 = _XcmPidPhaser3600v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3600v1.setStatus("current")
_XcmPidPhaser3100MFP_ObjectIdentity = ObjectIdentity
xcmPidPhaser3100MFP = _XcmPidPhaser3100MFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 17)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3100MFP.setStatus("current")
_XcmPidPhaser3100MFPv1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3100MFPv1 = _XcmPidPhaser3100MFPv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3100MFPv1.setStatus("current")
_XcmPidPhaser3100_ObjectIdentity = ObjectIdentity
xcmPidPhaser3100 = _XcmPidPhaser3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 18)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3100.setStatus("current")
_XcmPidPhaser3100v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3100v1 = _XcmPidPhaser3100v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3100v1.setStatus("current")
_XcmPidPhaser3435_ObjectIdentity = ObjectIdentity
xcmPidPhaser3435 = _XcmPidPhaser3435_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 19)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3435.setStatus("current")
_XcmPidPhaser3435v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3435v1 = _XcmPidPhaser3435v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3435v1.setStatus("current")
_XcmPidPhaser3300MFP_ObjectIdentity = ObjectIdentity
xcmPidPhaser3300MFP = _XcmPidPhaser3300MFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 20)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3300MFP.setStatus("current")
_XcmPidPhaser3300MFPc1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3300MFPc1 = _XcmPidPhaser3300MFPc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3300MFPc1.setStatus("current")
_XcmPidPhaser3300MFPc1v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3300MFPc1v1 = _XcmPidPhaser3300MFPc1v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3300MFPc1v1.setStatus("current")
_XcmPidPhaser3010_ObjectIdentity = ObjectIdentity
xcmPidPhaser3010 = _XcmPidPhaser3010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 26)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3010.setStatus("current")
_XcmPidPhaser3010C1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3010C1 = _XcmPidPhaser3010C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 26, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3010C1.setStatus("current")
_XcmPidPhaser3010C1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3010C1V1 = _XcmPidPhaser3010C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 26, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3010C1V1.setStatus("current")
_XcmPidPhaser3040_ObjectIdentity = ObjectIdentity
xcmPidPhaser3040 = _XcmPidPhaser3040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 28)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3040.setStatus("current")
_XcmPidPhaser3040C1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3040C1 = _XcmPidPhaser3040C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 28, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3040C1.setStatus("current")
_XcmPidPhaser3040C1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser3040C1V1 = _XcmPidPhaser3040C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 1, 28, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser3040C1V1.setStatus("current")
_XcmPidPhaser4yyyFamily_ObjectIdentity = ObjectIdentity
xcmPidPhaser4yyyFamily = _XcmPidPhaser4yyyFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4yyyFamily.setStatus("current")
_XcmPidPhaser4400_ObjectIdentity = ObjectIdentity
xcmPidPhaser4400 = _XcmPidPhaser4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4400.setStatus("current")
_XcmPidPhaser4400N_ObjectIdentity = ObjectIdentity
xcmPidPhaser4400N = _XcmPidPhaser4400N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4400N.setStatus("current")
_XcmPidPhaser4400DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser4400DT = _XcmPidPhaser4400DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4400DT.setStatus("current")
_XcmPidPhaser4400DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser4400DX = _XcmPidPhaser4400DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4400DX.setStatus("current")
_XcmPidPhaser4400B_ObjectIdentity = ObjectIdentity
xcmPidPhaser4400B = _XcmPidPhaser4400B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4400B.setStatus("current")
_XcmPidPhaser4500_ObjectIdentity = ObjectIdentity
xcmPidPhaser4500 = _XcmPidPhaser4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4500.setStatus("current")
_XcmPidPhaser4500N_ObjectIdentity = ObjectIdentity
xcmPidPhaser4500N = _XcmPidPhaser4500N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4500N.setStatus("current")
_XcmPidPhaser4500DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser4500DT = _XcmPidPhaser4500DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4500DT.setStatus("current")
_XcmPidPhaser4500DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser4500DX = _XcmPidPhaser4500DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4500DX.setStatus("current")
_XcmPidPhaser4500B_ObjectIdentity = ObjectIdentity
xcmPidPhaser4500B = _XcmPidPhaser4500B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 2, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4500B.setStatus("current")
_XcmPidPhaser4510_ObjectIdentity = ObjectIdentity
xcmPidPhaser4510 = _XcmPidPhaser4510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4510.setStatus("current")
_XcmPidPhaser4510B_ObjectIdentity = ObjectIdentity
xcmPidPhaser4510B = _XcmPidPhaser4510B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4510B.setStatus("current")
_XcmPidPhaser4510N_ObjectIdentity = ObjectIdentity
xcmPidPhaser4510N = _XcmPidPhaser4510N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4510N.setStatus("current")
_XcmPidPhaser4510DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser4510DT = _XcmPidPhaser4510DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 3, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4510DT.setStatus("current")
_XcmPidPhaser4510DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser4510DX = _XcmPidPhaser4510DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 2, 3, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser4510DX.setStatus("current")
_XcmPidPhaser5yyyFamily_ObjectIdentity = ObjectIdentity
xcmPidPhaser5yyyFamily = _XcmPidPhaser5yyyFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5yyyFamily.setStatus("current")
_XcmPidPhaser5500_ObjectIdentity = ObjectIdentity
xcmPidPhaser5500 = _XcmPidPhaser5500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5500.setStatus("current")
_XcmPidPhaser5500B_ObjectIdentity = ObjectIdentity
xcmPidPhaser5500B = _XcmPidPhaser5500B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5500B.setStatus("current")
_XcmPidPhaser5500N_ObjectIdentity = ObjectIdentity
xcmPidPhaser5500N = _XcmPidPhaser5500N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5500N.setStatus("current")
_XcmPidPhaser5500DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser5500DN = _XcmPidPhaser5500DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5500DN.setStatus("current")
_XcmPidPhaser5500DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser5500DT = _XcmPidPhaser5500DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5500DT.setStatus("current")
_XcmPidPhaser5500DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser5500DX = _XcmPidPhaser5500DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5500DX.setStatus("current")
_XcmPidPhaser5550_ObjectIdentity = ObjectIdentity
xcmPidPhaser5550 = _XcmPidPhaser5550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5550.setStatus("current")
_XcmPidPhaser5550B_ObjectIdentity = ObjectIdentity
xcmPidPhaser5550B = _XcmPidPhaser5550B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5550B.setStatus("current")
_XcmPidPhaser5550N_ObjectIdentity = ObjectIdentity
xcmPidPhaser5550N = _XcmPidPhaser5550N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5550N.setStatus("current")
_XcmPidPhaser5550DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser5550DN = _XcmPidPhaser5550DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5550DN.setStatus("current")
_XcmPidPhaser5550DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser5550DT = _XcmPidPhaser5550DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 2, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5550DT.setStatus("current")
_XcmPidPhaser5335_ObjectIdentity = ObjectIdentity
xcmPidPhaser5335 = _XcmPidPhaser5335_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5335.setStatus("current")
_XcmPidPhaser5335v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser5335v1 = _XcmPidPhaser5335v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 3, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser5335v1.setStatus("current")
_XcmPidPhaser6yyyFamily_ObjectIdentity = ObjectIdentity
xcmPidPhaser6yyyFamily = _XcmPidPhaser6yyyFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6yyyFamily.setStatus("current")
_XcmPidPhaser6200_ObjectIdentity = ObjectIdentity
xcmPidPhaser6200 = _XcmPidPhaser6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6200.setStatus("current")
_XcmPidPhaser6200B_ObjectIdentity = ObjectIdentity
xcmPidPhaser6200B = _XcmPidPhaser6200B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6200B.setStatus("current")
_XcmPidPhaser6200N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6200N = _XcmPidPhaser6200N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6200N.setStatus("current")
_XcmPidPhaser6200DP_ObjectIdentity = ObjectIdentity
xcmPidPhaser6200DP = _XcmPidPhaser6200DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6200DP.setStatus("current")
_XcmPidPhaser6200DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser6200DX = _XcmPidPhaser6200DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6200DX.setStatus("current")
_XcmPidPhaser6100_ObjectIdentity = ObjectIdentity
xcmPidPhaser6100 = _XcmPidPhaser6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6100.setStatus("current")
_XcmPidPhaser6100n_ObjectIdentity = ObjectIdentity
xcmPidPhaser6100n = _XcmPidPhaser6100n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6100n.setStatus("current")
_XcmPidPhaser6250_ObjectIdentity = ObjectIdentity
xcmPidPhaser6250 = _XcmPidPhaser6250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6250.setStatus("current")
_XcmPidPhaser6250B_ObjectIdentity = ObjectIdentity
xcmPidPhaser6250B = _XcmPidPhaser6250B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6250B.setStatus("current")
_XcmPidPhaser6250N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6250N = _XcmPidPhaser6250N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6250N.setStatus("current")
_XcmPidPhaser6250DP_ObjectIdentity = ObjectIdentity
xcmPidPhaser6250DP = _XcmPidPhaser6250DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 3, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6250DP.setStatus("current")
_XcmPidPhaser6250DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser6250DX = _XcmPidPhaser6250DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 3, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6250DX.setStatus("current")
_XcmPidPhaser6250DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser6250DT = _XcmPidPhaser6250DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 3, 5)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6250DT.setStatus("current")
_XcmPidPhaser6300_ObjectIdentity = ObjectIdentity
xcmPidPhaser6300 = _XcmPidPhaser6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6300.setStatus("current")
_XcmPidPhaser6300B_ObjectIdentity = ObjectIdentity
xcmPidPhaser6300B = _XcmPidPhaser6300B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6300B.setStatus("current")
_XcmPidPhaser6300N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6300N = _XcmPidPhaser6300N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 4, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6300N.setStatus("current")
_XcmPidPhaser6300DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser6300DN = _XcmPidPhaser6300DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 4, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6300DN.setStatus("current")
_XcmPidPhaser6350_ObjectIdentity = ObjectIdentity
xcmPidPhaser6350 = _XcmPidPhaser6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 6)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6350.setStatus("current")
_XcmPidPhaser6350DP_ObjectIdentity = ObjectIdentity
xcmPidPhaser6350DP = _XcmPidPhaser6350DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6350DP.setStatus("current")
_XcmPidPhaser6350DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser6350DT = _XcmPidPhaser6350DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 6, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6350DT.setStatus("current")
_XcmPidPhaser6350DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser6350DX = _XcmPidPhaser6350DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 6, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6350DX.setStatus("current")
_XcmPidPhaser6120_ObjectIdentity = ObjectIdentity
xcmPidPhaser6120 = _XcmPidPhaser6120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 7)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6120.setStatus("current")
_XcmPidPhaser6120b_ObjectIdentity = ObjectIdentity
xcmPidPhaser6120b = _XcmPidPhaser6120b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 7, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6120b.setStatus("current")
_XcmPidPhaser6120n_ObjectIdentity = ObjectIdentity
xcmPidPhaser6120n = _XcmPidPhaser6120n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 7, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6120n.setStatus("current")
_XcmPidPhaser6360_ObjectIdentity = ObjectIdentity
xcmPidPhaser6360 = _XcmPidPhaser6360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 8)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6360.setStatus("current")
_XcmPidPhaser6360N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6360N = _XcmPidPhaser6360N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 8, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6360N.setStatus("current")
_XcmPidPhaser6360DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser6360DN = _XcmPidPhaser6360DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 8, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6360DN.setStatus("current")
_XcmPidPhaser6360DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser6360DT = _XcmPidPhaser6360DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 8, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6360DT.setStatus("current")
_XcmPidPhaser6360DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser6360DX = _XcmPidPhaser6360DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 8, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6360DX.setStatus("current")
_XcmPidPhaser6180_ObjectIdentity = ObjectIdentity
xcmPidPhaser6180 = _XcmPidPhaser6180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 9)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6180.setStatus("current")
_XcmPidPhaser6180N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6180N = _XcmPidPhaser6180N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6180N.setStatus("current")
_XcmPidPhaser6180DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser6180DN = _XcmPidPhaser6180DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 9, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6180DN.setStatus("current")
_XcmPidPhaser6110N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6110N = _XcmPidPhaser6110N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 17)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6110N.setStatus("current")
_XcmPidPhaser6110Nv1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6110Nv1 = _XcmPidPhaser6110Nv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6110Nv1.setStatus("current")
_XcmPidPhaser6115_ObjectIdentity = ObjectIdentity
xcmPidPhaser6115 = _XcmPidPhaser6115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 18)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6115.setStatus("current")
_XcmPidPhaser6115N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6115N = _XcmPidPhaser6115N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6115N.setStatus("current")
_XcmPidPhaser6115DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser6115DN = _XcmPidPhaser6115DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 18, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6115DN.setStatus("current")
_XcmPidPhaser6110MFP3_ObjectIdentity = ObjectIdentity
xcmPidPhaser6110MFP3 = _XcmPidPhaser6110MFP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 19)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6110MFP3.setStatus("current")
_XcmPidPhaser6110MFP3v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6110MFP3v1 = _XcmPidPhaser6110MFP3v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6110MFP3v1.setStatus("current")
_XcmPidPhaser6110MFP4_ObjectIdentity = ObjectIdentity
xcmPidPhaser6110MFP4 = _XcmPidPhaser6110MFP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 20)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6110MFP4.setStatus("current")
_XcmPidPhaser6110MFP4v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6110MFP4v1 = _XcmPidPhaser6110MFP4v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6110MFP4v1.setStatus("current")
_XcmPidPhaser6180MFP_ObjectIdentity = ObjectIdentity
xcmPidPhaser6180MFP = _XcmPidPhaser6180MFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 21)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6180MFP.setStatus("current")
_XcmPidPhaser6180MFPN_ObjectIdentity = ObjectIdentity
xcmPidPhaser6180MFPN = _XcmPidPhaser6180MFPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 21, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6180MFPN.setStatus("current")
_XcmPidPhaser6180MFPDN_ObjectIdentity = ObjectIdentity
xcmPidPhaser6180MFPDN = _XcmPidPhaser6180MFPDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 21, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6180MFPDN.setStatus("current")
_XcmPidPhaser6130_ObjectIdentity = ObjectIdentity
xcmPidPhaser6130 = _XcmPidPhaser6130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 23)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6130.setStatus("current")
_XcmPidPhaser6130N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6130N = _XcmPidPhaser6130N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 23, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6130N.setStatus("current")
_XcmPidPhaser6125_ObjectIdentity = ObjectIdentity
xcmPidPhaser6125 = _XcmPidPhaser6125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 24)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6125.setStatus("current")
_XcmPidPhaser6125N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6125N = _XcmPidPhaser6125N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 24, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6125N.setStatus("current")
_XcmPidPhaser6280_ObjectIdentity = ObjectIdentity
xcmPidPhaser6280 = _XcmPidPhaser6280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 25)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6280.setStatus("current")
_XcmPidPhaser6280N_ObjectIdentity = ObjectIdentity
xcmPidPhaser6280N = _XcmPidPhaser6280N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 25, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6280N.setStatus("current")
_XcmPidPhaser6280Nv1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6280Nv1 = _XcmPidPhaser6280Nv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 25, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6280Nv1.setStatus("current")
_XcmPidPhaser6280DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser6280DN = _XcmPidPhaser6280DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 25, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6280DN.setStatus("current")
_XcmPidPhaser6280DNv1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6280DNv1 = _XcmPidPhaser6280DNv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 25, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6280DNv1.setStatus("current")
_XcmPidPhaser6280DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser6280DT = _XcmPidPhaser6280DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 25, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6280DT.setStatus("current")
_XcmPidPhaser6280DTv1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6280DTv1 = _XcmPidPhaser6280DTv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 25, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6280DTv1.setStatus("current")
_XcmPidPhaser6700_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700 = _XcmPidPhaser6700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700.setStatus("current")
_XcmPidPhaser6700C1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700C1 = _XcmPidPhaser6700C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700C1.setStatus("current")
_XcmPidPhaser6700C1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700C1V1 = _XcmPidPhaser6700C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700C1V1.setStatus("current")
_XcmPidPhaser6700C2_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700C2 = _XcmPidPhaser6700C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700C2.setStatus("current")
_XcmPidPhaser6700C2V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700C2V1 = _XcmPidPhaser6700C2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700C2V1.setStatus("current")
_XcmPidPhaser6700C3_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700C3 = _XcmPidPhaser6700C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700C3.setStatus("current")
_XcmPidPhaser6700C3V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700C3V1 = _XcmPidPhaser6700C3V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700C3V1.setStatus("current")
_XcmPidPhaser6700C4_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700C4 = _XcmPidPhaser6700C4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700C4.setStatus("current")
_XcmPidPhaser6700C4V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6700C4V1 = _XcmPidPhaser6700C4V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 30, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6700C4V1.setStatus("current")
_XcmPidWorkCentre6015B_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6015B = _XcmPidWorkCentre6015B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 32)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6015B.setStatus("current")
_XcmPidWorkCentre6015BC1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6015BC1 = _XcmPidWorkCentre6015BC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 32, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6015BC1.setStatus("current")
_XcmPidWorkCentre6015BC1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6015BC1V1 = _XcmPidWorkCentre6015BC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 32, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6015BC1V1.setStatus("current")
_XcmPidPhaser6500_ObjectIdentity = ObjectIdentity
xcmPidPhaser6500 = _XcmPidPhaser6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 33)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6500.setStatus("current")
_XcmPidPhaser6500C1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6500C1 = _XcmPidPhaser6500C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 33, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6500C1.setStatus("current")
_XcmPidPhaser6500C1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6500C1V1 = _XcmPidPhaser6500C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 33, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6500C1V1.setStatus("current")
_XcmPidPhaser6500C2_ObjectIdentity = ObjectIdentity
xcmPidPhaser6500C2 = _XcmPidPhaser6500C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 33, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6500C2.setStatus("current")
_XcmPidPhaser6500C2V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6500C2V1 = _XcmPidPhaser6500C2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 33, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6500C2V1.setStatus("current")
_XcmPidWorkCentre6505_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6505 = _XcmPidWorkCentre6505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 34)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6505.setStatus("current")
_XcmPidWorkCentre6505C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6505C1 = _XcmPidWorkCentre6505C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 34, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6505C1.setStatus("current")
_XcmPidWorkCentre6505C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6505C1V1 = _XcmPidWorkCentre6505C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 34, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6505C1V1.setStatus("current")
_XcmPidWorkCentre6505C2_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6505C2 = _XcmPidWorkCentre6505C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 34, 2)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6505C2.setStatus("current")
_XcmPidWorkCentre6505C2V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6505C2V1 = _XcmPidWorkCentre6505C2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 34, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6505C2V1.setStatus("current")
_XcmPidPhaser6000_ObjectIdentity = ObjectIdentity
xcmPidPhaser6000 = _XcmPidPhaser6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 35)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6000.setStatus("current")
_XcmPidPhaser6000C1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6000C1 = _XcmPidPhaser6000C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 35, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6000C1.setStatus("current")
_XcmPidPhaser6000C1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6000C1V1 = _XcmPidPhaser6000C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 35, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6000C1V1.setStatus("current")
_XcmPidWorkCentre6015_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6015 = _XcmPidWorkCentre6015_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 36)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6015.setStatus("current")
_XcmPidWorkCentre6015C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6015C1 = _XcmPidWorkCentre6015C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 36, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6015C1.setStatus("current")
_XcmPidWorkCentre6015C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6015C1V1 = _XcmPidWorkCentre6015C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 36, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6015C1V1.setStatus("current")
_XcmPidWorkCentre6015C2_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6015C2 = _XcmPidWorkCentre6015C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 36, 2)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6015C2.setStatus("current")
_XcmPidWorkCentre6015C2V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6015C2V1 = _XcmPidWorkCentre6015C2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 36, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6015C2V1.setStatus("current")
_XcmPidPhaser6600_ObjectIdentity = ObjectIdentity
xcmPidPhaser6600 = _XcmPidPhaser6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 37)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6600.setStatus("current")
_XcmPidPhaser6600NC1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6600NC1 = _XcmPidPhaser6600NC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 37, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6600NC1.setStatus("current")
_XcmPidPhaser6600NC1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6600NC1V1 = _XcmPidPhaser6600NC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 37, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6600NC1V1.setStatus("current")
_XcmPidPhaser6600DNC2_ObjectIdentity = ObjectIdentity
xcmPidPhaser6600DNC2 = _XcmPidPhaser6600DNC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 37, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6600DNC2.setStatus("current")
_XcmPidPhaser6600DNC2V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser6600DNC2V1 = _XcmPidPhaser6600DNC2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 4, 37, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser6600DNC2V1.setStatus("current")
_XcmPidPhaser7yyyFamily_ObjectIdentity = ObjectIdentity
xcmPidPhaser7yyyFamily = _XcmPidPhaser7yyyFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7yyyFamily.setStatus("current")
_XcmPidPhaser7300_ObjectIdentity = ObjectIdentity
xcmPidPhaser7300 = _XcmPidPhaser7300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7300.setStatus("current")
_XcmPidPhaser7300DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser7300DN = _XcmPidPhaser7300DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7300DN.setStatus("current")
_XcmPidPhaser7300N_ObjectIdentity = ObjectIdentity
xcmPidPhaser7300N = _XcmPidPhaser7300N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7300N.setStatus("current")
_XcmPidPhaser7300DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser7300DT = _XcmPidPhaser7300DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7300DT.setStatus("current")
_XcmPidPhaser7300DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser7300DX = _XcmPidPhaser7300DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7300DX.setStatus("current")
_XcmPidPhaser7300B_ObjectIdentity = ObjectIdentity
xcmPidPhaser7300B = _XcmPidPhaser7300B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7300B.setStatus("current")
_XcmPidPhaser7400_ObjectIdentity = ObjectIdentity
xcmPidPhaser7400 = _XcmPidPhaser7400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7400.setStatus("current")
_XcmPidPhaser7400B_ObjectIdentity = ObjectIdentity
xcmPidPhaser7400B = _XcmPidPhaser7400B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7400B.setStatus("current")
_XcmPidPhaser7400N_ObjectIdentity = ObjectIdentity
xcmPidPhaser7400N = _XcmPidPhaser7400N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7400N.setStatus("current")
_XcmPidPhaser7400DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser7400DN = _XcmPidPhaser7400DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7400DN.setStatus("current")
_XcmPidPhaser7400DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser7400DT = _XcmPidPhaser7400DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 2, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7400DT.setStatus("current")
_XcmPidPhaser7400DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser7400DX = _XcmPidPhaser7400DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 2, 5)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7400DX.setStatus("current")
_XcmPidPhaser7400DXF_ObjectIdentity = ObjectIdentity
xcmPidPhaser7400DXF = _XcmPidPhaser7400DXF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 2, 6)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7400DXF.setStatus("current")
_XcmPidPhaser7750_ObjectIdentity = ObjectIdentity
xcmPidPhaser7750 = _XcmPidPhaser7750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7750.setStatus("current")
_XcmPidPhaser7750B_ObjectIdentity = ObjectIdentity
xcmPidPhaser7750B = _XcmPidPhaser7750B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7750B.setStatus("current")
_XcmPidPhaser7750DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser7750DN = _XcmPidPhaser7750DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7750DN.setStatus("current")
_XcmPidPhaser7750GX_ObjectIdentity = ObjectIdentity
xcmPidPhaser7750GX = _XcmPidPhaser7750GX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 3, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7750GX.setStatus("current")
_XcmPidPhaser7750DXF_ObjectIdentity = ObjectIdentity
xcmPidPhaser7750DXF = _XcmPidPhaser7750DXF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 3, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7750DXF.setStatus("current")
_XcmPidPhaser7760_ObjectIdentity = ObjectIdentity
xcmPidPhaser7760 = _XcmPidPhaser7760_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7760.setStatus("current")
_XcmPidPhaser7760B_ObjectIdentity = ObjectIdentity
xcmPidPhaser7760B = _XcmPidPhaser7760B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7760B.setStatus("current")
_XcmPidPhaser7760DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser7760DN = _XcmPidPhaser7760DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 4, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7760DN.setStatus("current")
_XcmPidPhaser7760GX_ObjectIdentity = ObjectIdentity
xcmPidPhaser7760GX = _XcmPidPhaser7760GX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 4, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7760GX.setStatus("current")
_XcmPidPhaser7760DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser7760DX = _XcmPidPhaser7760DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 4, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7760DX.setStatus("current")
_XcmPidPhaser7800_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800 = _XcmPidPhaser7800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800.setStatus("current")
_XcmPidPhaser7800NC1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800NC1 = _XcmPidPhaser7800NC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800NC1.setStatus("current")
_XcmPidPhaser7800NC1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800NC1V1 = _XcmPidPhaser7800NC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800NC1V1.setStatus("current")
_XcmPidPhaser7800DNC1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800DNC1 = _XcmPidPhaser7800DNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800DNC1.setStatus("current")
_XcmPidPhaser7800DNC1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800DNC1V1 = _XcmPidPhaser7800DNC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800DNC1V1.setStatus("current")
_XcmPidPhaser7800GXC1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800GXC1 = _XcmPidPhaser7800GXC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800GXC1.setStatus("current")
_XcmPidPhaser7800GXC1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800GXC1V1 = _XcmPidPhaser7800GXC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800GXC1V1.setStatus("current")
_XcmPidPhaser7800DXC1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800DXC1 = _XcmPidPhaser7800DXC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800DXC1.setStatus("current")
_XcmPidPhaser7800DXC1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7800DXC1V1 = _XcmPidPhaser7800DXC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 6, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7800DXC1V1.setStatus("current")
_XcmPidPhaser7100_ObjectIdentity = ObjectIdentity
xcmPidPhaser7100 = _XcmPidPhaser7100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 7)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7100.setStatus("current")
_XcmPidPhaser7100NC1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7100NC1 = _XcmPidPhaser7100NC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 7, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7100NC1.setStatus("current")
_XcmPidPhaser7100NC1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7100NC1V1 = _XcmPidPhaser7100NC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 7, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7100NC1V1.setStatus("current")
_XcmPidPhaser7100DNC1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7100DNC1 = _XcmPidPhaser7100DNC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 7, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7100DNC1.setStatus("current")
_XcmPidPhaser7100DNC1V1_ObjectIdentity = ObjectIdentity
xcmPidPhaser7100DNC1V1 = _XcmPidPhaser7100DNC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 5, 7, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser7100DNC1V1.setStatus("current")
_XcmPidPhaser8yyyFamily_ObjectIdentity = ObjectIdentity
xcmPidPhaser8yyyFamily = _XcmPidPhaser8yyyFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8yyyFamily.setStatus("current")
_XcmPidPhaser8400_ObjectIdentity = ObjectIdentity
xcmPidPhaser8400 = _XcmPidPhaser8400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8400.setStatus("current")
_XcmPidPhaser8400B_ObjectIdentity = ObjectIdentity
xcmPidPhaser8400B = _XcmPidPhaser8400B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8400B.setStatus("current")
_XcmPidPhaser8400N_ObjectIdentity = ObjectIdentity
xcmPidPhaser8400N = _XcmPidPhaser8400N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8400N.setStatus("current")
_XcmPidPhaser8400DP_ObjectIdentity = ObjectIdentity
xcmPidPhaser8400DP = _XcmPidPhaser8400DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8400DP.setStatus("current")
_XcmPidPhaser8400DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser8400DX = _XcmPidPhaser8400DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8400DX.setStatus("current")
_XcmPidPhaser8400BD_ObjectIdentity = ObjectIdentity
xcmPidPhaser8400BD = _XcmPidPhaser8400BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8400BD.setStatus("current")
_XcmPidPhaser8560_ObjectIdentity = ObjectIdentity
xcmPidPhaser8560 = _XcmPidPhaser8560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 7)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8560.setStatus("current")
_XcmPidPhaser8560v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser8560v1 = _XcmPidPhaser8560v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 7, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8560v1.setStatus("current")
_XcmPidPhaser8560p_ObjectIdentity = ObjectIdentity
xcmPidPhaser8560p = _XcmPidPhaser8560p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 9)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8560p.setStatus("current")
_XcmPidPhaser8560N_ObjectIdentity = ObjectIdentity
xcmPidPhaser8560N = _XcmPidPhaser8560N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8560N.setStatus("current")
_XcmPidPhaser8560DN_ObjectIdentity = ObjectIdentity
xcmPidPhaser8560DN = _XcmPidPhaser8560DN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 9, 2)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8560DN.setStatus("current")
_XcmPidPhaser8560DT_ObjectIdentity = ObjectIdentity
xcmPidPhaser8560DT = _XcmPidPhaser8560DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 9, 3)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8560DT.setStatus("current")
_XcmPidPhaser8560DX_ObjectIdentity = ObjectIdentity
xcmPidPhaser8560DX = _XcmPidPhaser8560DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 9, 4)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8560DX.setStatus("current")
_XcmPidPhaser8560PP_ObjectIdentity = ObjectIdentity
xcmPidPhaser8560PP = _XcmPidPhaser8560PP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 9, 6)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8560PP.setStatus("current")
_XcmPidPhaser8860_ObjectIdentity = ObjectIdentity
xcmPidPhaser8860 = _XcmPidPhaser8860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 17)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8860.setStatus("current")
_XcmPidPhaser8860v1_ObjectIdentity = ObjectIdentity
xcmPidPhaser8860v1 = _XcmPidPhaser8860v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8860v1.setStatus("current")
_XcmPidPhaser8860MFP_ObjectIdentity = ObjectIdentity
xcmPidPhaser8860MFP = _XcmPidPhaser8860MFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 18)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8860MFP.setStatus("current")
_XcmPidPhaser8860MFPv1_ObjectIdentity = ObjectIdentity
xcmPidPhaser8860MFPv1 = _XcmPidPhaser8860MFPv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidPhaser8860MFPv1.setStatus("current")
_XcmPidP3200MFP_ObjectIdentity = ObjectIdentity
xcmPidP3200MFP = _XcmPidP3200MFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 19)
)
if mibBuilder.loadTexts:
    xcmPidP3200MFP.setStatus("current")
_XcmPidP3200MFPv1_ObjectIdentity = ObjectIdentity
xcmPidP3200MFPv1 = _XcmPidP3200MFPv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 6, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidP3200MFPv1.setStatus("current")
_XcmPidPhaser9yyyFamily_ObjectIdentity = ObjectIdentity
xcmPidPhaser9yyyFamily = _XcmPidPhaser9yyyFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 19, 9)
)
if mibBuilder.loadTexts:
    xcmPidPhaser9yyyFamily.setStatus("current")
_XcmPidWorkCentreMFSystems_ObjectIdentity = ObjectIdentity
xcmPidWorkCentreMFSystems = _XcmPidWorkCentreMFSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentreMFSystems.setStatus("current")
_XcmPidWCPro_ObjectIdentity = ObjectIdentity
xcmPidWCPro = _XcmPidWCPro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPro.setStatus("current")
_XcmPidWCP32C_ObjectIdentity = ObjectIdentity
xcmPidWCP32C = _XcmPidWCP32C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP32C.setStatus("current")
_XcmPidWCP32CV1_ObjectIdentity = ObjectIdentity
xcmPidWCP32CV1 = _XcmPidWCP32CV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP32CV1.setStatus("current")
_XcmPidWCP32CV2_ObjectIdentity = ObjectIdentity
xcmPidWCP32CV2 = _XcmPidWCP32CV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCP32CV2.setStatus("current")
_XcmPidWCP35_ObjectIdentity = ObjectIdentity
xcmPidWCP35 = _XcmPidWCP35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCP35.setStatus("current")
_XcmPidWCP35V1_ObjectIdentity = ObjectIdentity
xcmPidWCP35V1 = _XcmPidWCP35V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP35V1.setStatus("current")
_XcmPidWCP35V2_ObjectIdentity = ObjectIdentity
xcmPidWCP35V2 = _XcmPidWCP35V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCP35V2.setStatus("current")
_XcmPidWCP40C_ObjectIdentity = ObjectIdentity
xcmPidWCP40C = _XcmPidWCP40C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidWCP40C.setStatus("current")
_XcmPidWCP40CV1_ObjectIdentity = ObjectIdentity
xcmPidWCP40CV1 = _XcmPidWCP40CV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP40CV1.setStatus("current")
_XcmPidWCP40CV2_ObjectIdentity = ObjectIdentity
xcmPidWCP40CV2 = _XcmPidWCP40CV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCP40CV2.setStatus("current")
_XcmPidWCP45_ObjectIdentity = ObjectIdentity
xcmPidWCP45 = _XcmPidWCP45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 4)
)
if mibBuilder.loadTexts:
    xcmPidWCP45.setStatus("current")
_XcmPidWCP45V1_ObjectIdentity = ObjectIdentity
xcmPidWCP45V1 = _XcmPidWCP45V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP45V1.setStatus("current")
_XcmPidWCP45V2_ObjectIdentity = ObjectIdentity
xcmPidWCP45V2 = _XcmPidWCP45V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 4, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCP45V2.setStatus("current")
_XcmPidWCP55_ObjectIdentity = ObjectIdentity
xcmPidWCP55 = _XcmPidWCP55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 5)
)
if mibBuilder.loadTexts:
    xcmPidWCP55.setStatus("current")
_XcmPidWCP55V1_ObjectIdentity = ObjectIdentity
xcmPidWCP55V1 = _XcmPidWCP55V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP55V1.setStatus("current")
_XcmPidWCP55V2_ObjectIdentity = ObjectIdentity
xcmPidWCP55V2 = _XcmPidWCP55V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 5, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCP55V2.setStatus("current")
_XcmPidWCP165_ObjectIdentity = ObjectIdentity
xcmPidWCP165 = _XcmPidWCP165_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 9)
)
if mibBuilder.loadTexts:
    xcmPidWCP165.setStatus("current")
_XcmPidWCP165V1_ObjectIdentity = ObjectIdentity
xcmPidWCP165V1 = _XcmPidWCP165V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP165V1.setStatus("current")
_XcmPidWCP175_ObjectIdentity = ObjectIdentity
xcmPidWCP175 = _XcmPidWCP175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 17)
)
if mibBuilder.loadTexts:
    xcmPidWCP175.setStatus("current")
_XcmPidWCP175V1_ObjectIdentity = ObjectIdentity
xcmPidWCP175V1 = _XcmPidWCP175V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP175V1.setStatus("current")
_XcmPidWCPC2128_ObjectIdentity = ObjectIdentity
xcmPidWCPC2128 = _XcmPidWCPC2128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 19)
)
if mibBuilder.loadTexts:
    xcmPidWCPC2128.setStatus("current")
_XcmPidWCPC2128V1_ObjectIdentity = ObjectIdentity
xcmPidWCPC2128V1 = _XcmPidWCPC2128V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPC2128V1.setStatus("current")
_XcmPidWCPC2636_ObjectIdentity = ObjectIdentity
xcmPidWCPC2636 = _XcmPidWCPC2636_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 20)
)
if mibBuilder.loadTexts:
    xcmPidWCPC2636.setStatus("current")
_XcmPidWCPC2636V1_ObjectIdentity = ObjectIdentity
xcmPidWCPC2636V1 = _XcmPidWCPC2636V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPC2636V1.setStatus("current")
_XcmPidWCPC3545_ObjectIdentity = ObjectIdentity
xcmPidWCPC3545 = _XcmPidWCPC3545_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 21)
)
if mibBuilder.loadTexts:
    xcmPidWCPC3545.setStatus("current")
_XcmPidWCPC3545V1_ObjectIdentity = ObjectIdentity
xcmPidWCPC3545V1 = _XcmPidWCPC3545V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 21, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPC3545V1.setStatus("current")
_XcmPidWC265_ObjectIdentity = ObjectIdentity
xcmPidWC265 = _XcmPidWC265_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 22)
)
if mibBuilder.loadTexts:
    xcmPidWC265.setStatus("current")
_XcmPidWC265V1_ObjectIdentity = ObjectIdentity
xcmPidWC265V1 = _XcmPidWC265V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 22, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC265V1.setStatus("current")
_XcmPidWC275_ObjectIdentity = ObjectIdentity
xcmPidWC275 = _XcmPidWC275_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 23)
)
if mibBuilder.loadTexts:
    xcmPidWC275.setStatus("current")
_XcmPidWC275V1_ObjectIdentity = ObjectIdentity
xcmPidWC275V1 = _XcmPidWC275V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 23, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC275V1.setStatus("current")
_XcmPidWCP265_ObjectIdentity = ObjectIdentity
xcmPidWCP265 = _XcmPidWCP265_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 24)
)
if mibBuilder.loadTexts:
    xcmPidWCP265.setStatus("current")
_XcmPidWCP265V1_ObjectIdentity = ObjectIdentity
xcmPidWCP265V1 = _XcmPidWCP265V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 24, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP265V1.setStatus("current")
_XcmPidWCP275_ObjectIdentity = ObjectIdentity
xcmPidWCP275 = _XcmPidWCP275_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 25)
)
if mibBuilder.loadTexts:
    xcmPidWCP275.setStatus("current")
_XcmPidWCP275V1_ObjectIdentity = ObjectIdentity
xcmPidWCP275V1 = _XcmPidWCP275V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 25, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP275V1.setStatus("current")
_XcmPidWCPS265_ObjectIdentity = ObjectIdentity
xcmPidWCPS265 = _XcmPidWCPS265_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 26)
)
if mibBuilder.loadTexts:
    xcmPidWCPS265.setStatus("current")
_XcmPidWCPS265V1_ObjectIdentity = ObjectIdentity
xcmPidWCPS265V1 = _XcmPidWCPS265V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 26, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPS265V1.setStatus("current")
_XcmPidWCPS275_ObjectIdentity = ObjectIdentity
xcmPidWCPS275 = _XcmPidWCPS275_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 27)
)
if mibBuilder.loadTexts:
    xcmPidWCPS275.setStatus("current")
_XcmPidWCPS275V1_ObjectIdentity = ObjectIdentity
xcmPidWCPS275V1 = _XcmPidWCPS275V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 27, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPS275V1.setStatus("current")
_XcmPidWC7655_ObjectIdentity = ObjectIdentity
xcmPidWC7655 = _XcmPidWC7655_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 28)
)
if mibBuilder.loadTexts:
    xcmPidWC7655.setStatus("current")
_XcmPidWC7655V1_ObjectIdentity = ObjectIdentity
xcmPidWC7655V1 = _XcmPidWC7655V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 28, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC7655V1.setStatus("current")
_XcmPidWC7665_ObjectIdentity = ObjectIdentity
xcmPidWC7665 = _XcmPidWC7665_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 29)
)
if mibBuilder.loadTexts:
    xcmPidWC7665.setStatus("current")
_XcmPidWC7665V1_ObjectIdentity = ObjectIdentity
xcmPidWC7665V1 = _XcmPidWC7665V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 29, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC7665V1.setStatus("current")
_XcmPidWC7675_ObjectIdentity = ObjectIdentity
xcmPidWC7675 = _XcmPidWC7675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 36)
)
if mibBuilder.loadTexts:
    xcmPidWC7675.setStatus("current")
_XcmPidWC7675V1_ObjectIdentity = ObjectIdentity
xcmPidWC7675V1 = _XcmPidWC7675V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 1, 36, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC7675V1.setStatus("current")
_XcmPidWCMF_ObjectIdentity = ObjectIdentity
xcmPidWCMF = _XcmPidWCMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCMF.setStatus("current")
_XcmPidWCM35_ObjectIdentity = ObjectIdentity
xcmPidWCM35 = _XcmPidWCM35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCM35.setStatus("current")
_XcmPidWCM35V1_ObjectIdentity = ObjectIdentity
xcmPidWCM35V1 = _XcmPidWCM35V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCM35V1.setStatus("current")
_XcmPidWCM35V2_ObjectIdentity = ObjectIdentity
xcmPidWCM35V2 = _XcmPidWCM35V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCM35V2.setStatus("current")
_XcmPidWCM45_ObjectIdentity = ObjectIdentity
xcmPidWCM45 = _XcmPidWCM45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidWCM45.setStatus("current")
_XcmPidWCM45V1_ObjectIdentity = ObjectIdentity
xcmPidWCM45V1 = _XcmPidWCM45V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCM45V1.setStatus("current")
_XcmPidWCM45V2_ObjectIdentity = ObjectIdentity
xcmPidWCM45V2 = _XcmPidWCM45V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCM45V2.setStatus("current")
_XcmPidWCM55_ObjectIdentity = ObjectIdentity
xcmPidWCM55 = _XcmPidWCM55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 4)
)
if mibBuilder.loadTexts:
    xcmPidWCM55.setStatus("current")
_XcmPidWCM55V1_ObjectIdentity = ObjectIdentity
xcmPidWCM55V1 = _XcmPidWCM55V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCM55V1.setStatus("current")
_XcmPidWCM55V2_ObjectIdentity = ObjectIdentity
xcmPidWCM55V2 = _XcmPidWCM55V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 4, 2)
)
if mibBuilder.loadTexts:
    xcmPidWCM55V2.setStatus("current")
_XcmPidWCM165_ObjectIdentity = ObjectIdentity
xcmPidWCM165 = _XcmPidWCM165_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 5)
)
if mibBuilder.loadTexts:
    xcmPidWCM165.setStatus("current")
_XcmPidWCM165V1_ObjectIdentity = ObjectIdentity
xcmPidWCM165V1 = _XcmPidWCM165V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCM165V1.setStatus("current")
_XcmPidWCM175_ObjectIdentity = ObjectIdentity
xcmPidWCM175 = _XcmPidWCM175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 6)
)
if mibBuilder.loadTexts:
    xcmPidWCM175.setStatus("current")
_XcmPidWCM175V1_ObjectIdentity = ObjectIdentity
xcmPidWCM175V1 = _XcmPidWCM175V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 6, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCM175V1.setStatus("current")
_XcmPidWCMPS35_ObjectIdentity = ObjectIdentity
xcmPidWCMPS35 = _XcmPidWCMPS35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 9)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS35.setStatus("current")
_XcmPidWCMPS35V1_ObjectIdentity = ObjectIdentity
xcmPidWCMPS35V1 = _XcmPidWCMPS35V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS35V1.setStatus("current")
_XcmPidWCMPS45_ObjectIdentity = ObjectIdentity
xcmPidWCMPS45 = _XcmPidWCMPS45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 17)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS45.setStatus("current")
_XcmPidWCMPS45V1_ObjectIdentity = ObjectIdentity
xcmPidWCMPS45V1 = _XcmPidWCMPS45V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS45V1.setStatus("current")
_XcmPidWCMPS55_ObjectIdentity = ObjectIdentity
xcmPidWCMPS55 = _XcmPidWCMPS55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 18)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS55.setStatus("current")
_XcmPidWCMPS55V1_ObjectIdentity = ObjectIdentity
xcmPidWCMPS55V1 = _XcmPidWCMPS55V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS55V1.setStatus("current")
_XcmPidWCMPS165_ObjectIdentity = ObjectIdentity
xcmPidWCMPS165 = _XcmPidWCMPS165_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 19)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS165.setStatus("current")
_XcmPidWCMPS165V1_ObjectIdentity = ObjectIdentity
xcmPidWCMPS165V1 = _XcmPidWCMPS165V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS165V1.setStatus("current")
_XcmPidWCMPS175_ObjectIdentity = ObjectIdentity
xcmPidWCMPS175 = _XcmPidWCMPS175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 20)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS175.setStatus("current")
_XcmPidWCMPS175V1_ObjectIdentity = ObjectIdentity
xcmPidWCMPS175V1 = _XcmPidWCMPS175V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCMPS175V1.setStatus("current")
_XcmPidWCMF28_ObjectIdentity = ObjectIdentity
xcmPidWCMF28 = _XcmPidWCMF28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 23)
)
if mibBuilder.loadTexts:
    xcmPidWCMF28.setStatus("current")
_XcmPidWCMFM28_ObjectIdentity = ObjectIdentity
xcmPidWCMFM28 = _XcmPidWCMFM28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 23, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCMFM28.setStatus("current")
_XcmPidWCPS232_ObjectIdentity = ObjectIdentity
xcmPidWCPS232 = _XcmPidWCPS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 26)
)
if mibBuilder.loadTexts:
    xcmPidWCPS232.setStatus("current")
_XcmPidWCPS232V1_ObjectIdentity = ObjectIdentity
xcmPidWCPS232V1 = _XcmPidWCPS232V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 26, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPS232V1.setStatus("current")
_XcmPidWCPS238_ObjectIdentity = ObjectIdentity
xcmPidWCPS238 = _XcmPidWCPS238_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 27)
)
if mibBuilder.loadTexts:
    xcmPidWCPS238.setStatus("current")
_XcmPidWCPS238V1_ObjectIdentity = ObjectIdentity
xcmPidWCPS238V1 = _XcmPidWCPS238V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 27, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPS238V1.setStatus("current")
_XcmPidWCPS245_ObjectIdentity = ObjectIdentity
xcmPidWCPS245 = _XcmPidWCPS245_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 28)
)
if mibBuilder.loadTexts:
    xcmPidWCPS245.setStatus("current")
_XcmPidWCPS245V1_ObjectIdentity = ObjectIdentity
xcmPidWCPS245V1 = _XcmPidWCPS245V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 28, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPS245V1.setStatus("current")
_XcmPidWCPS255_ObjectIdentity = ObjectIdentity
xcmPidWCPS255 = _XcmPidWCPS255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 29)
)
if mibBuilder.loadTexts:
    xcmPidWCPS255.setStatus("current")
_XcmPidWCPS255V1_ObjectIdentity = ObjectIdentity
xcmPidWCPS255V1 = _XcmPidWCPS255V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 29, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCPS255V1.setStatus("current")
_XcmPidWCP232_ObjectIdentity = ObjectIdentity
xcmPidWCP232 = _XcmPidWCP232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 30)
)
if mibBuilder.loadTexts:
    xcmPidWCP232.setStatus("current")
_XcmPidWCP232V1_ObjectIdentity = ObjectIdentity
xcmPidWCP232V1 = _XcmPidWCP232V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 30, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP232V1.setStatus("current")
_XcmPidWCP238_ObjectIdentity = ObjectIdentity
xcmPidWCP238 = _XcmPidWCP238_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 31)
)
if mibBuilder.loadTexts:
    xcmPidWCP238.setStatus("current")
_XcmPidWCP238V1_ObjectIdentity = ObjectIdentity
xcmPidWCP238V1 = _XcmPidWCP238V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 31, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP238V1.setStatus("current")
_XcmPidWCP245_ObjectIdentity = ObjectIdentity
xcmPidWCP245 = _XcmPidWCP245_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 32)
)
if mibBuilder.loadTexts:
    xcmPidWCP245.setStatus("current")
_XcmPidWCP245V1_ObjectIdentity = ObjectIdentity
xcmPidWCP245V1 = _XcmPidWCP245V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 32, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP245V1.setStatus("current")
_XcmPidWCP255_ObjectIdentity = ObjectIdentity
xcmPidWCP255 = _XcmPidWCP255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 33)
)
if mibBuilder.loadTexts:
    xcmPidWCP255.setStatus("current")
_XcmPidWCP255V1_ObjectIdentity = ObjectIdentity
xcmPidWCP255V1 = _XcmPidWCP255V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 33, 1)
)
if mibBuilder.loadTexts:
    xcmPidWCP255V1.setStatus("current")
_XcmPidWC232_ObjectIdentity = ObjectIdentity
xcmPidWC232 = _XcmPidWC232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 34)
)
if mibBuilder.loadTexts:
    xcmPidWC232.setStatus("current")
_XcmPidWC232V1_ObjectIdentity = ObjectIdentity
xcmPidWC232V1 = _XcmPidWC232V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 34, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC232V1.setStatus("current")
_XcmPidWC238_ObjectIdentity = ObjectIdentity
xcmPidWC238 = _XcmPidWC238_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 35)
)
if mibBuilder.loadTexts:
    xcmPidWC238.setStatus("current")
_XcmPidWC238V1_ObjectIdentity = ObjectIdentity
xcmPidWC238V1 = _XcmPidWC238V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 35, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC238V1.setStatus("current")
_XcmPidWC245_ObjectIdentity = ObjectIdentity
xcmPidWC245 = _XcmPidWC245_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 36)
)
if mibBuilder.loadTexts:
    xcmPidWC245.setStatus("current")
_XcmPidWC245V1_ObjectIdentity = ObjectIdentity
xcmPidWC245V1 = _XcmPidWC245V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 36, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC245V1.setStatus("current")
_XcmPidWC255_ObjectIdentity = ObjectIdentity
xcmPidWC255 = _XcmPidWC255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 37)
)
if mibBuilder.loadTexts:
    xcmPidWC255.setStatus("current")
_XcmPidWC255V1_ObjectIdentity = ObjectIdentity
xcmPidWC255V1 = _XcmPidWC255V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 37, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC255V1.setStatus("current")
_XcmPidWorkCentre5135_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5135 = _XcmPidWorkCentre5135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 40)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5135.setStatus("current")
_XcmPidWorkCentre5135C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5135C1 = _XcmPidWorkCentre5135C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 40, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5135C1.setStatus("current")
_XcmPidWorkCentre5135C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5135C1V1 = _XcmPidWorkCentre5135C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5135C1V1.setStatus("current")
_XcmPidWorkCentre5135C1V2_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5135C1V2 = _XcmPidWorkCentre5135C1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 40, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5135C1V2.setStatus("current")
_XcmPidWorkCentre5150_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5150 = _XcmPidWorkCentre5150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 41)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5150.setStatus("current")
_XcmPidWorkCentre5150C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5150C1 = _XcmPidWorkCentre5150C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 41, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5150C1.setStatus("current")
_XcmPidWorkCentre5150C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5150C1V1 = _XcmPidWorkCentre5150C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 41, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5150C1V1.setStatus("current")
_XcmPidWorkCentre5150C1V2_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5150C1V2 = _XcmPidWorkCentre5150C1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 2, 41, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5150C1V2.setStatus("current")
_XcmPidWCMF3_ObjectIdentity = ObjectIdentity
xcmPidWCMF3 = _XcmPidWCMF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3)
)
if mibBuilder.loadTexts:
    xcmPidWCMF3.setStatus("current")
_XcmPidWC5632_ObjectIdentity = ObjectIdentity
xcmPidWC5632 = _XcmPidWC5632_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 35)
)
if mibBuilder.loadTexts:
    xcmPidWC5632.setStatus("current")
_XcmPidWC5632V1_ObjectIdentity = ObjectIdentity
xcmPidWC5632V1 = _XcmPidWC5632V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 35, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5632V1.setStatus("current")
_XcmPidWC5638_ObjectIdentity = ObjectIdentity
xcmPidWC5638 = _XcmPidWC5638_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 37)
)
if mibBuilder.loadTexts:
    xcmPidWC5638.setStatus("current")
_XcmPidWC5638V1_ObjectIdentity = ObjectIdentity
xcmPidWC5638V1 = _XcmPidWC5638V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 37, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5638V1.setStatus("current")
_XcmPidWC5645_ObjectIdentity = ObjectIdentity
xcmPidWC5645 = _XcmPidWC5645_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 38)
)
if mibBuilder.loadTexts:
    xcmPidWC5645.setStatus("current")
_XcmPidWC5645V1_ObjectIdentity = ObjectIdentity
xcmPidWC5645V1 = _XcmPidWC5645V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 38, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5645V1.setStatus("current")
_XcmPidWC5655_ObjectIdentity = ObjectIdentity
xcmPidWC5655 = _XcmPidWC5655_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 39)
)
if mibBuilder.loadTexts:
    xcmPidWC5655.setStatus("current")
_XcmPidWC5655V1_ObjectIdentity = ObjectIdentity
xcmPidWC5655V1 = _XcmPidWC5655V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 39, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5655V1.setStatus("current")
_XcmPidWC5665_ObjectIdentity = ObjectIdentity
xcmPidWC5665 = _XcmPidWC5665_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 40)
)
if mibBuilder.loadTexts:
    xcmPidWC5665.setStatus("current")
_XcmPidWC5665V1_ObjectIdentity = ObjectIdentity
xcmPidWC5665V1 = _XcmPidWC5665V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 40, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5665V1.setStatus("current")
_XcmPidWC5675_ObjectIdentity = ObjectIdentity
xcmPidWC5675 = _XcmPidWC5675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 41)
)
if mibBuilder.loadTexts:
    xcmPidWC5675.setStatus("current")
_XcmPidWC5675V1_ObjectIdentity = ObjectIdentity
xcmPidWC5675V1 = _XcmPidWC5675V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 3, 41, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5675V1.setStatus("current")
_XcmPidWCMF4_ObjectIdentity = ObjectIdentity
xcmPidWCMF4 = _XcmPidWCMF4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4)
)
if mibBuilder.loadTexts:
    xcmPidWCMF4.setStatus("current")
_XcmPidWC5687_ObjectIdentity = ObjectIdentity
xcmPidWC5687 = _XcmPidWC5687_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4, 9)
)
if mibBuilder.loadTexts:
    xcmPidWC5687.setStatus("current")
_XcmPidWC5687V1_ObjectIdentity = ObjectIdentity
xcmPidWC5687V1 = _XcmPidWC5687V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5687V1.setStatus("current")
_XcmPidWC5030_ObjectIdentity = ObjectIdentity
xcmPidWC5030 = _XcmPidWC5030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4, 17)
)
if mibBuilder.loadTexts:
    xcmPidWC5030.setStatus("current")
_XcmPidWC5030V1_ObjectIdentity = ObjectIdentity
xcmPidWC5030V1 = _XcmPidWC5030V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5030V1.setStatus("current")
_XcmPidWC5030V2_ObjectIdentity = ObjectIdentity
xcmPidWC5030V2 = _XcmPidWC5030V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4, 17, 2)
)
if mibBuilder.loadTexts:
    xcmPidWC5030V2.setStatus("current")
_XcmPidWC5050_ObjectIdentity = ObjectIdentity
xcmPidWC5050 = _XcmPidWC5050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4, 18)
)
if mibBuilder.loadTexts:
    xcmPidWC5050.setStatus("current")
_XcmPidWC5050V1_ObjectIdentity = ObjectIdentity
xcmPidWC5050V1 = _XcmPidWC5050V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC5050V1.setStatus("current")
_XcmPidWC5050V2_ObjectIdentity = ObjectIdentity
xcmPidWC5050V2 = _XcmPidWC5050V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 4, 18, 2)
)
if mibBuilder.loadTexts:
    xcmPidWC5050V2.setStatus("current")
_XcmPidWCMF5_ObjectIdentity = ObjectIdentity
xcmPidWCMF5 = _XcmPidWCMF5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5)
)
if mibBuilder.loadTexts:
    xcmPidWCMF5.setStatus("current")
_XcmPidWC6400_ObjectIdentity = ObjectIdentity
xcmPidWC6400 = _XcmPidWC6400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5)
)
if mibBuilder.loadTexts:
    xcmPidWC6400.setStatus("current")
_XcmPidWC6400S_ObjectIdentity = ObjectIdentity
xcmPidWC6400S = _XcmPidWC6400S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC6400S.setStatus("current")
_XcmPidWC6400Sv1_ObjectIdentity = ObjectIdentity
xcmPidWC6400Sv1 = _XcmPidWC6400Sv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC6400Sv1.setStatus("current")
_XcmPidWC6400Sv2_ObjectIdentity = ObjectIdentity
xcmPidWC6400Sv2 = _XcmPidWC6400Sv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidWC6400Sv2.setStatus("current")
_XcmPidWC6400X_ObjectIdentity = ObjectIdentity
xcmPidWC6400X = _XcmPidWC6400X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 2)
)
if mibBuilder.loadTexts:
    xcmPidWC6400X.setStatus("current")
_XcmPidWC6400Xv1_ObjectIdentity = ObjectIdentity
xcmPidWC6400Xv1 = _XcmPidWC6400Xv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC6400Xv1.setStatus("current")
_XcmPidWC6400Xv2_ObjectIdentity = ObjectIdentity
xcmPidWC6400Xv2 = _XcmPidWC6400Xv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidWC6400Xv2.setStatus("current")
_XcmPidWC6400XF_ObjectIdentity = ObjectIdentity
xcmPidWC6400XF = _XcmPidWC6400XF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 3)
)
if mibBuilder.loadTexts:
    xcmPidWC6400XF.setStatus("current")
_XcmPidWC6400XFv1_ObjectIdentity = ObjectIdentity
xcmPidWC6400XFv1 = _XcmPidWC6400XFv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidWC6400XFv1.setStatus("current")
_XcmPidWC6400XFv2_ObjectIdentity = ObjectIdentity
xcmPidWC6400XFv2 = _XcmPidWC6400XFv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 5, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidWC6400XFv2.setStatus("current")
_XcmPidWorkCentre5735_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5735 = _XcmPidWorkCentre5735_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 29)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5735.setStatus("current")
_XcmPidWorkCentre5735C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5735C1 = _XcmPidWorkCentre5735C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 29, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5735C1.setStatus("current")
_XcmPidWorkCentre5735C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5735C1V1 = _XcmPidWorkCentre5735C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 29, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5735C1V1.setStatus("current")
_XcmPidWorkCentre5740_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5740 = _XcmPidWorkCentre5740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 30)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5740.setStatus("current")
_XcmPidWorkCentre5740C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5740C1 = _XcmPidWorkCentre5740C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 30, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5740C1.setStatus("current")
_XcmPidWorkCentre5740C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5740C1V1 = _XcmPidWorkCentre5740C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 30, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5740C1V1.setStatus("current")
_XcmPidWorkCentre5745_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5745 = _XcmPidWorkCentre5745_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 31)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5745.setStatus("current")
_XcmPidWorkCentre5745C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5745C1 = _XcmPidWorkCentre5745C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 31, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5745C1.setStatus("current")
_XcmPidWorkCentre5745C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5745C1V1 = _XcmPidWorkCentre5745C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 31, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5745C1V1.setStatus("current")
_XcmPidWorkCentre5755_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5755 = _XcmPidWorkCentre5755_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 32)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5755.setStatus("current")
_XcmPidWorkCentre5755C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5755C1 = _XcmPidWorkCentre5755C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 32, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5755C1.setStatus("current")
_XcmPidWorkCentre5755C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5755C1V1 = _XcmPidWorkCentre5755C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 32, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5755C1V1.setStatus("current")
_XcmPidWorkCentre5765_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5765 = _XcmPidWorkCentre5765_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 33)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5765.setStatus("current")
_XcmPidWorkCentre5765C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5765C1 = _XcmPidWorkCentre5765C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 33, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5765C1.setStatus("current")
_XcmPidWorkCentre5765C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5765C1V1 = _XcmPidWorkCentre5765C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 33, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5765C1V1.setStatus("current")
_XcmPidWorkCentre5775_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5775 = _XcmPidWorkCentre5775_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 34)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5775.setStatus("current")
_XcmPidWorkCentre5775C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5775C1 = _XcmPidWorkCentre5775C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 34, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5775C1.setStatus("current")
_XcmPidWorkCentre5775C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5775C1V1 = _XcmPidWorkCentre5775C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 34, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5775C1V1.setStatus("current")
_XcmPidWorkCentre5790_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5790 = _XcmPidWorkCentre5790_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 35)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5790.setStatus("current")
_XcmPidWorkCentre5790C1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5790C1 = _XcmPidWorkCentre5790C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 35, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5790C1.setStatus("current")
_XcmPidWorkCentre5790C1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre5790C1V1 = _XcmPidWorkCentre5790C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 5, 35, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre5790C1V1.setStatus("current")
_XcmPidWCMF6_ObjectIdentity = ObjectIdentity
xcmPidWCMF6 = _XcmPidWCMF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6)
)
if mibBuilder.loadTexts:
    xcmPidWCMF6.setStatus("current")
_XcmPidWorkCentre3045B_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre3045B = _XcmPidWorkCentre3045B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 7)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre3045B.setStatus("current")
_XcmPidWorkCentre3045BC1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre3045BC1 = _XcmPidWorkCentre3045BC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 7, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre3045BC1.setStatus("current")
_XcmPidWorkCentre3045BC1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre3045BC1V1 = _XcmPidWorkCentre3045BC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 7, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre3045BC1V1.setStatus("current")
_XcmPidWorkCentre3045NI_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre3045NI = _XcmPidWorkCentre3045NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 9)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre3045NI.setStatus("current")
_XcmPidWorkCentre3045NIC1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre3045NIC1 = _XcmPidWorkCentre3045NIC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre3045NIC1.setStatus("current")
_XcmPidWorkCentre3045NIC1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre3045NIC1V1 = _XcmPidWorkCentre3045NIC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 9, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre3045NIC1V1.setStatus("current")
_XcmPidWorkCentre6605_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6605 = _XcmPidWorkCentre6605_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 34)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6605.setStatus("current")
_XcmPidWorkCentre6605NC1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6605NC1 = _XcmPidWorkCentre6605NC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 34, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6605NC1.setStatus("current")
_XcmPidWorkCentre6605NC1V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6605NC1V1 = _XcmPidWorkCentre6605NC1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 34, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6605NC1V1.setStatus("current")
_XcmPidWorkCentre6605DNC2_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6605DNC2 = _XcmPidWorkCentre6605DNC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 34, 2)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6605DNC2.setStatus("current")
_XcmPidWorkCentre6605DNC2V1_ObjectIdentity = ObjectIdentity
xcmPidWorkCentre6605DNC2V1 = _XcmPidWorkCentre6605DNC2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 6, 34, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidWorkCentre6605DNC2V1.setStatus("current")
_XcmPidWCMF7_ObjectIdentity = ObjectIdentity
xcmPidWCMF7 = _XcmPidWCMF7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 20, 7)
)
if mibBuilder.loadTexts:
    xcmPidWCMF7.setStatus("current")
_XcmPidXeroxWideFormat_ObjectIdentity = ObjectIdentity
xcmPidXeroxWideFormat = _XcmPidXeroxWideFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 22)
)
if mibBuilder.loadTexts:
    xcmPidXeroxWideFormat.setStatus("current")
_XcmPidNuveraProductLine_ObjectIdentity = ObjectIdentity
xcmPidNuveraProductLine = _XcmPidNuveraProductLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23)
)
if mibBuilder.loadTexts:
    xcmPidNuveraProductLine.setStatus("current")
_XcmPidNuveraEAProductionSystemFamily_ObjectIdentity = ObjectIdentity
xcmPidNuveraEAProductionSystemFamily = _XcmPidNuveraEAProductionSystemFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 17)
)
if mibBuilder.loadTexts:
    xcmPidNuveraEAProductionSystemFamily.setStatus("current")
_XcmPidNuvera100x120x144x157EAPS_ObjectIdentity = ObjectIdentity
xcmPidNuvera100x120x144x157EAPS = _XcmPidNuvera100x120x144x157EAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 17, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera100x120x144x157EAPS.setStatus("current")
_XcmPidNuvera100x120x144x157EAPSEmbeddedFFPS_ObjectIdentity = ObjectIdentity
xcmPidNuvera100x120x144x157EAPSEmbeddedFFPS = _XcmPidNuvera100x120x144x157EAPSEmbeddedFFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 17, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera100x120x144x157EAPSEmbeddedFFPS.setStatus("current")
_XcmPidNuvera100x120x144x157EAPSEmbeddedFFPSV1_ObjectIdentity = ObjectIdentity
xcmPidNuvera100x120x144x157EAPSEmbeddedFFPSV1 = _XcmPidNuvera100x120x144x157EAPSEmbeddedFFPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera100x120x144x157EAPSEmbeddedFFPSV1.setStatus("current")
_XcmPidNuveraEAPerfectingProductionSystemFamily_ObjectIdentity = ObjectIdentity
xcmPidNuveraEAPerfectingProductionSystemFamily = _XcmPidNuveraEAPerfectingProductionSystemFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 18)
)
if mibBuilder.loadTexts:
    xcmPidNuveraEAPerfectingProductionSystemFamily.setStatus("current")
_XcmPidNuvera200x288x314EAPPS_ObjectIdentity = ObjectIdentity
xcmPidNuvera200x288x314EAPPS = _XcmPidNuvera200x288x314EAPPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 18, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera200x288x314EAPPS.setStatus("current")
_XcmPidNuvera200x288x314EAPPSEmbeddedFFPS_ObjectIdentity = ObjectIdentity
xcmPidNuvera200x288x314EAPPSEmbeddedFFPS = _XcmPidNuvera200x288x314EAPPSEmbeddedFFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 18, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera200x288x314EAPPSEmbeddedFFPS.setStatus("current")
_XcmPidNuvera200x288x314EAPPSEmbeddedFFPSv1_ObjectIdentity = ObjectIdentity
xcmPidNuvera200x288x314EAPPSEmbeddedFFPSv1 = _XcmPidNuvera200x288x314EAPPSEmbeddedFFPSv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera200x288x314EAPPSEmbeddedFFPSv1.setStatus("current")
_XcmPidNuveraMXProductionSystemFamily_ObjectIdentity = ObjectIdentity
xcmPidNuveraMXProductionSystemFamily = _XcmPidNuveraMXProductionSystemFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 19)
)
if mibBuilder.loadTexts:
    xcmPidNuveraMXProductionSystemFamily.setStatus("current")
_XcmPidNuvera100x120x144MXPS_ObjectIdentity = ObjectIdentity
xcmPidNuvera100x120x144MXPS = _XcmPidNuvera100x120x144MXPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 19, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera100x120x144MXPS.setStatus("current")
_XcmPidNuvera100x120x144MXPSEmbeddedFFPS_ObjectIdentity = ObjectIdentity
xcmPidNuvera100x120x144MXPSEmbeddedFFPS = _XcmPidNuvera100x120x144MXPSEmbeddedFFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 19, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera100x120x144MXPSEmbeddedFFPS.setStatus("current")
_XcmPidNuvera100x120x144MXPSEmbeddedFFPSV1_ObjectIdentity = ObjectIdentity
xcmPidNuvera100x120x144MXPSEmbeddedFFPSV1 = _XcmPidNuvera100x120x144MXPSEmbeddedFFPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 19, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera100x120x144MXPSEmbeddedFFPSV1.setStatus("current")
_XcmPidNuveraMXPerfectingProductionSystemFamily_ObjectIdentity = ObjectIdentity
xcmPidNuveraMXPerfectingProductionSystemFamily = _XcmPidNuveraMXPerfectingProductionSystemFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 20)
)
if mibBuilder.loadTexts:
    xcmPidNuveraMXPerfectingProductionSystemFamily.setStatus("current")
_XcmPidNuvera200x288MXPPS_ObjectIdentity = ObjectIdentity
xcmPidNuvera200x288MXPPS = _XcmPidNuvera200x288MXPPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 20, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera200x288MXPPS.setStatus("current")
_XcmPidNuvera200x288MXPPSEmbeddedFFPS_ObjectIdentity = ObjectIdentity
xcmPidNuvera200x288MXPPSEmbeddedFFPS = _XcmPidNuvera200x288MXPPSEmbeddedFFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 20, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera200x288MXPPSEmbeddedFFPS.setStatus("current")
_XcmPidNuvera200x288MXPPSEmbeddedFFPSV1_ObjectIdentity = ObjectIdentity
xcmPidNuvera200x288MXPPSEmbeddedFFPSV1 = _XcmPidNuvera200x288MXPPSEmbeddedFFPSV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 23, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidNuvera200x288MXPPSEmbeddedFFPSV1.setStatus("current")
_XcmPidColorQube_ObjectIdentity = ObjectIdentity
xcmPidColorQube = _XcmPidColorQube_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24)
)
if mibBuilder.loadTexts:
    xcmPidColorQube.setStatus("current")
_XcmPidColorQube9200_ObjectIdentity = ObjectIdentity
xcmPidColorQube9200 = _XcmPidColorQube9200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9200.setStatus("current")
_XcmPidColorQube9201_ObjectIdentity = ObjectIdentity
xcmPidColorQube9201 = _XcmPidColorQube9201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9201.setStatus("current")
_XcmPidColorQube9201C1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9201C1 = _XcmPidColorQube9201C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9201C1.setStatus("current")
_XcmPidColorQube9201C1V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9201C1V1 = _XcmPidColorQube9201C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9201C1V1.setStatus("current")
_XcmPidColorQube9201C1V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9201C1V2 = _XcmPidColorQube9201C1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9201C1V2.setStatus("current")
_XcmPidColorQube9201C1V3_ObjectIdentity = ObjectIdentity
xcmPidColorQube9201C1V3 = _XcmPidColorQube9201C1V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9201C1V3.setStatus("current")
_XcmPidColorQube9201C2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9201C2 = _XcmPidColorQube9201C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9201C2.setStatus("current")
_XcmPidColorQube9201C2V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9201C2V1 = _XcmPidColorQube9201C2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9201C2V1.setStatus("current")
_XcmPidColorQube9201C2V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9201C2V2 = _XcmPidColorQube9201C2V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9201C2V2.setStatus("current")
_XcmPidColorQube9202_ObjectIdentity = ObjectIdentity
xcmPidColorQube9202 = _XcmPidColorQube9202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9202.setStatus("current")
_XcmPidColorQube9202C1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9202C1 = _XcmPidColorQube9202C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9202C1.setStatus("current")
_XcmPidColorQube9202C1V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9202C1V1 = _XcmPidColorQube9202C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9202C1V1.setStatus("current")
_XcmPidColorQube9202C1V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9202C1V2 = _XcmPidColorQube9202C1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9202C1V2.setStatus("current")
_XcmPidColorQube9202C1V3_ObjectIdentity = ObjectIdentity
xcmPidColorQube9202C1V3 = _XcmPidColorQube9202C1V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9202C1V3.setStatus("current")
_XcmPidColorQube9202C2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9202C2 = _XcmPidColorQube9202C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9202C2.setStatus("current")
_XcmPidColorQube9202C2V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9202C2V1 = _XcmPidColorQube9202C2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9202C2V1.setStatus("current")
_XcmPidColorQube9202C2V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9202C2V2 = _XcmPidColorQube9202C2V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9202C2V2.setStatus("current")
_XcmPidColorQube9203_ObjectIdentity = ObjectIdentity
xcmPidColorQube9203 = _XcmPidColorQube9203_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9203.setStatus("current")
_XcmPidColorQube9203C1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9203C1 = _XcmPidColorQube9203C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9203C1.setStatus("current")
_XcmPidColorQube9203C1V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9203C1V1 = _XcmPidColorQube9203C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9203C1V1.setStatus("current")
_XcmPidColorQube9203C1V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9203C1V2 = _XcmPidColorQube9203C1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9203C1V2.setStatus("current")
_XcmPidColorQube9203C1V3_ObjectIdentity = ObjectIdentity
xcmPidColorQube9203C1V3 = _XcmPidColorQube9203C1V3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9203C1V3.setStatus("current")
_XcmPidColorQube9203C2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9203C2 = _XcmPidColorQube9203C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9203C2.setStatus("current")
_XcmPidColorQube9203C2V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9203C2V1 = _XcmPidColorQube9203C2V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9203C2V1.setStatus("current")
_XcmPidColorQube9203C2V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9203C2V2 = _XcmPidColorQube9203C2V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9203C2V2.setStatus("current")
_XcmPidColorQube8x00_ObjectIdentity = ObjectIdentity
xcmPidColorQube8x00 = _XcmPidColorQube8x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8x00.setStatus("current")
_XcmPidColorQube8700_ObjectIdentity = ObjectIdentity
xcmPidColorQube8700 = _XcmPidColorQube8700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8700.setStatus("current")
_XcmPidColorQube8700S_ObjectIdentity = ObjectIdentity
xcmPidColorQube8700S = _XcmPidColorQube8700S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8700S.setStatus("current")
_XcmPidColorQube8700Sv1_ObjectIdentity = ObjectIdentity
xcmPidColorQube8700Sv1 = _XcmPidColorQube8700Sv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8700Sv1.setStatus("current")
_XcmPidColorQube8700X_ObjectIdentity = ObjectIdentity
xcmPidColorQube8700X = _XcmPidColorQube8700X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8700X.setStatus("current")
_XcmPidColorQube8700Xv1_ObjectIdentity = ObjectIdentity
xcmPidColorQube8700Xv1 = _XcmPidColorQube8700Xv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8700Xv1.setStatus("current")
_XcmPidColorQube8700XF_ObjectIdentity = ObjectIdentity
xcmPidColorQube8700XF = _XcmPidColorQube8700XF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 1, 3)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8700XF.setStatus("current")
_XcmPidColorQube8700XFv1_ObjectIdentity = ObjectIdentity
xcmPidColorQube8700XFv1 = _XcmPidColorQube8700XFv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8700XFv1.setStatus("current")
_XcmPidColorQube8900_ObjectIdentity = ObjectIdentity
xcmPidColorQube8900 = _XcmPidColorQube8900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8900.setStatus("current")
_XcmPidColorQube8900X_ObjectIdentity = ObjectIdentity
xcmPidColorQube8900X = _XcmPidColorQube8900X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 2, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8900X.setStatus("current")
_XcmPidColorQube8900Xv1_ObjectIdentity = ObjectIdentity
xcmPidColorQube8900Xv1 = _XcmPidColorQube8900Xv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8900Xv1.setStatus("current")
_XcmPidColorQube8900S_ObjectIdentity = ObjectIdentity
xcmPidColorQube8900S = _XcmPidColorQube8900S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 2, 3)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8900S.setStatus("current")
_XcmPidColorQube8900Sv1_ObjectIdentity = ObjectIdentity
xcmPidColorQube8900Sv1 = _XcmPidColorQube8900Sv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube8900Sv1.setStatus("current")
_XcmPidColorQube9300_ObjectIdentity = ObjectIdentity
xcmPidColorQube9300 = _XcmPidColorQube9300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9300.setStatus("current")
_XcmPidColorQube9301_ObjectIdentity = ObjectIdentity
xcmPidColorQube9301 = _XcmPidColorQube9301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9301.setStatus("current")
_XcmPidColorQube9301C1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9301C1 = _XcmPidColorQube9301C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9301C1.setStatus("current")
_XcmPidColorQube9301C1V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9301C1V1 = _XcmPidColorQube9301C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9301C1V1.setStatus("current")
_XcmPidColorQube9301C1V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9301C1V2 = _XcmPidColorQube9301C1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9301C1V2.setStatus("current")
_XcmPidColorQube9302_ObjectIdentity = ObjectIdentity
xcmPidColorQube9302 = _XcmPidColorQube9302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9302.setStatus("current")
_XcmPidColorQube9302C1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9302C1 = _XcmPidColorQube9302C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9302C1.setStatus("current")
_XcmPidColorQube9302C1V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9302C1V1 = _XcmPidColorQube9302C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9302C1V1.setStatus("current")
_XcmPidColorQube9302C1V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9302C1V2 = _XcmPidColorQube9302C1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9302C1V2.setStatus("current")
_XcmPidColorQube9303_ObjectIdentity = ObjectIdentity
xcmPidColorQube9303 = _XcmPidColorQube9303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 3)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9303.setStatus("current")
_XcmPidColorQube9303C1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9303C1 = _XcmPidColorQube9303C1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 3, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9303C1.setStatus("current")
_XcmPidColorQube9303C1V1_ObjectIdentity = ObjectIdentity
xcmPidColorQube9303C1V1 = _XcmPidColorQube9303C1V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9303C1V1.setStatus("current")
_XcmPidColorQube9303C1V2_ObjectIdentity = ObjectIdentity
xcmPidColorQube9303C1V2 = _XcmPidColorQube9303C1V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 24, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPidColorQube9303C1V2.setStatus("current")
_XcmPidFXSystems_ObjectIdentity = ObjectIdentity
xcmPidFXSystems = _XcmPidFXSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 30)
)
if mibBuilder.loadTexts:
    xcmPidFXSystems.setStatus("current")
_XcmPidEPCProductLine_ObjectIdentity = ObjectIdentity
xcmPidEPCProductLine = _XcmPidEPCProductLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 31)
)
if mibBuilder.loadTexts:
    xcmPidEPCProductLine.setStatus("current")
_XcmPidLPMProductLine_ObjectIdentity = ObjectIdentity
xcmPidLPMProductLine = _XcmPidLPMProductLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 32)
)
if mibBuilder.loadTexts:
    xcmPidLPMProductLine.setStatus("current")
_XcmPidDigitalPrintingPressProductLine_ObjectIdentity = ObjectIdentity
xcmPidDigitalPrintingPressProductLine = _XcmPidDigitalPrintingPressProductLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 62, 1, 33)
)
if mibBuilder.loadTexts:
    xcmPidDigitalPrintingPressProductLine.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-PRODUCT-ID-TC",
    **{"xcmPidTC": xcmPidTC,
       "xcmPidProductIdentifiers": xcmPidProductIdentifiers,
       "xcmPidDocuCentreSystems": xcmPidDocuCentreSystems,
       "xcmPidDCS20": xcmPidDCS20,
       "xcmPidDCS20M1": xcmPidDCS20M1,
       "xcmPidDCS20M1V1": xcmPidDCS20M1V1,
       "xcmPidDCS35": xcmPidDCS35,
       "xcmPidDCS35M1": xcmPidDCS35M1,
       "xcmPidDCS35M1V1": xcmPidDCS35M1V1,
       "xcmPidDC230": xcmPidDC230,
       "xcmPidDC230ST": xcmPidDC230ST,
       "xcmPidDC230STV1": xcmPidDC230STV1,
       "xcmPidDC230STV2": xcmPidDC230STV2,
       "xcmPidDC230STV3": xcmPidDC230STV3,
       "xcmPidDC230STV4": xcmPidDC230STV4,
       "xcmPidDC230STV5": xcmPidDC230STV5,
       "xcmPidDC230LP": xcmPidDC230LP,
       "xcmPidDC230LPV1": xcmPidDC230LPV1,
       "xcmPidDC230LPV2": xcmPidDC230LPV2,
       "xcmPidDC230LPV3": xcmPidDC230LPV3,
       "xcmPidDC230LPV4": xcmPidDC230LPV4,
       "xcmPidDC230LPV5": xcmPidDC230LPV5,
       "xcmPidDC265": xcmPidDC265,
       "xcmPidDC265ST": xcmPidDC265ST,
       "xcmPidDC265STV1": xcmPidDC265STV1,
       "xcmPidDC265STV2": xcmPidDC265STV2,
       "xcmPidDC265STV3": xcmPidDC265STV3,
       "xcmPidDC265LP": xcmPidDC265LP,
       "xcmPidDC265LPV1": xcmPidDC265LPV1,
       "xcmPidDC265LPV2": xcmPidDC265LPV2,
       "xcmPidDC265LPV3": xcmPidDC265LPV3,
       "xcmPidDC240": xcmPidDC240,
       "xcmPidDC240ST": xcmPidDC240ST,
       "xcmPidDC240STV1": xcmPidDC240STV1,
       "xcmPidDC240STV2": xcmPidDC240STV2,
       "xcmPidDC240STV3": xcmPidDC240STV3,
       "xcmPidDC340": xcmPidDC340,
       "xcmPidDC340ST": xcmPidDC340ST,
       "xcmPidDC340STV1": xcmPidDC340STV1,
       "xcmPidDC340STV2": xcmPidDC340STV2,
       "xcmPidDC255": xcmPidDC255,
       "xcmPidDC255ST": xcmPidDC255ST,
       "xcmPidDC255STV1": xcmPidDC255STV1,
       "xcmPidDC255STV2": xcmPidDC255STV2,
       "xcmPidDC255STV3": xcmPidDC255STV3,
       "xcmPidDC255LP": xcmPidDC255LP,
       "xcmPidDC255LPV1": xcmPidDC255LPV1,
       "xcmPidDC255LPV2": xcmPidDC255LPV2,
       "xcmPidDC255LPV3": xcmPidDC255LPV3,
       "xcmPidDC220": xcmPidDC220,
       "xcmPidDC220ST": xcmPidDC220ST,
       "xcmPidDC220STV3": xcmPidDC220STV3,
       "xcmPidDC220STV4": xcmPidDC220STV4,
       "xcmPidDC332": xcmPidDC332,
       "xcmPidDC332ST": xcmPidDC332ST,
       "xcmPidDC332STV1": xcmPidDC332STV1,
       "xcmPidDC332STV2": xcmPidDC332STV2,
       "xcmPidDC4XX": xcmPidDC4XX,
       "xcmPidDC460": xcmPidDC460,
       "xcmPidDC460V1": xcmPidDC460V1,
       "xcmPidDC470": xcmPidDC470,
       "xcmPidDC470V1": xcmPidDC470V1,
       "xcmPidDC420": xcmPidDC420,
       "xcmPidDC420ST": xcmPidDC420ST,
       "xcmPidDC420STV1": xcmPidDC420STV1,
       "xcmPidDC420STV2": xcmPidDC420STV2,
       "xcmPidDC426": xcmPidDC426,
       "xcmPidDC426V1": xcmPidDC426V1,
       "xcmPidDC432": xcmPidDC432,
       "xcmPidDC432ST": xcmPidDC432ST,
       "xcmPidDC432STV1": xcmPidDC432STV1,
       "xcmPidDC432STV2": xcmPidDC432STV2,
       "xcmPidDC432STV3": xcmPidDC432STV3,
       "xcmPidDC432STV4": xcmPidDC432STV4,
       "xcmPidDC432STV5": xcmPidDC432STV5,
       "xcmPidDC430": xcmPidDC430,
       "xcmPidDC430V1": xcmPidDC430V1,
       "xcmPidDC440": xcmPidDC440,
       "xcmPidDC440ST": xcmPidDC440ST,
       "xcmPidDC440STV1": xcmPidDC440STV1,
       "xcmPidDC440STV2": xcmPidDC440STV2,
       "xcmPidDC440STV3": xcmPidDC440STV3,
       "xcmPidDC230i": xcmPidDC230i,
       "xcmPidDC230iST": xcmPidDC230iST,
       "xcmPidDC230iSTV1": xcmPidDC230iSTV1,
       "xcmPidDC230iSTV2": xcmPidDC230iSTV2,
       "xcmPidDC4YY": xcmPidDC4YY,
       "xcmPidDC480": xcmPidDC480,
       "xcmPidDC480V1": xcmPidDC480V1,
       "xcmPidDC425": xcmPidDC425,
       "xcmPidDC425ST": xcmPidDC425ST,
       "xcmPidDC425STV1": xcmPidDC425STV1,
       "xcmPidDC555": xcmPidDC555,
       "xcmPidDC555ST": xcmPidDC555ST,
       "xcmPidDC555STV1": xcmPidDC555STV1,
       "xcmPidDC555STV2": xcmPidDC555STV2,
       "xcmPidDC535": xcmPidDC535,
       "xcmPidDC535ST": xcmPidDC535ST,
       "xcmPidDC535STV1": xcmPidDC535STV1,
       "xcmPidDC535STV2": xcmPidDC535STV2,
       "xcmPidDC545": xcmPidDC545,
       "xcmPidDC545ST": xcmPidDC545ST,
       "xcmPidDC545STV1": xcmPidDC545STV1,
       "xcmPidDC545STV2": xcmPidDC545STV2,
       "xcmPidDesktopDocuPrintPrinters": xcmPidDesktopDocuPrintPrinters,
       "xcmPid4517": xcmPid4517,
       "xcmPid4517PlusM1": xcmPid4517PlusM1,
       "xcmPid4517PlusM1V1": xcmPid4517PlusM1V1,
       "xcmPidDocuPrintN17": xcmPidDocuPrintN17,
       "xcmPidDocuPrintN17V1": xcmPidDocuPrintN17V1,
       "xcmPidDocuPrintC55": xcmPidDocuPrintC55,
       "xcmPidDocuPrintC55M1": xcmPidDocuPrintC55M1,
       "xcmPidDocuPrintC55M1V1": xcmPidDocuPrintC55M1V1,
       "xcmPidDocuPrintC55M1V2": xcmPidDocuPrintC55M1V2,
       "xcmPidDocuPrintNC60": xcmPidDocuPrintNC60,
       "xcmPidDocuPrintNC60V1": xcmPidDocuPrintNC60V1,
       "xcmPidP1210": xcmPidP1210,
       "xcmPidP1210M1": xcmPidP1210M1,
       "xcmPidP1210M1V1": xcmPidP1210M1V1,
       "xcmPidP3400": xcmPidP3400,
       "xcmPidP3400M1": xcmPidP3400M1,
       "xcmPidP3400M1V1": xcmPidP3400M1V1,
       "xcmPidWorkGroupDocuPrintPrinters": xcmPidWorkGroupDocuPrintPrinters,
       "xcmPidDocuPrintNnn": xcmPidDocuPrintNnn,
       "xcmPidDocuPrintN32": xcmPidDocuPrintN32,
       "xcmPidDocuPrintN32V1": xcmPidDocuPrintN32V1,
       "xcmPidDocuPrintN32V2": xcmPidDocuPrintN32V2,
       "xcmPidDocuPrintN24": xcmPidDocuPrintN24,
       "xcmPidDocuPrintN24V1": xcmPidDocuPrintN24V1,
       "xcmPidDocuPrintN24V2": xcmPidDocuPrintN24V2,
       "xcmPidDocuPrintN40": xcmPidDocuPrintN40,
       "xcmPidDocuPrintN40V1": xcmPidDocuPrintN40V1,
       "xcmPidDocuPrintN2025": xcmPidDocuPrintN2025,
       "xcmPidDocuPrintN2025V1": xcmPidDocuPrintN2025V1,
       "xcmPidDocuPrintN2025V2": xcmPidDocuPrintN2025V2,
       "xcmPidDocuPrintN2125": xcmPidDocuPrintN2125,
       "xcmPidDocuPrintN2125V1": xcmPidDocuPrintN2125V1,
       "xcmPidDocuPrintN2425": xcmPidDocuPrintN2425,
       "xcmPidDocuPrintN2425V1": xcmPidDocuPrintN2425V1,
       "xcmPidDocuPrintN2825": xcmPidDocuPrintN2825,
       "xcmPidDocuPrintN2825V1": xcmPidDocuPrintN2825V1,
       "xcmPidDocuPrintN3225": xcmPidDocuPrintN3225,
       "xcmPidDocuPrintN3225V1": xcmPidDocuPrintN3225V1,
       "xcmPidDocuPrintN4025": xcmPidDocuPrintN4025,
       "xcmPidDocuPrintN4025V1": xcmPidDocuPrintN4025V1,
       "xcmPidDocuPrintN4025V2": xcmPidDocuPrintN4025V2,
       "xcmPidDocuPrintAyame35": xcmPidDocuPrintAyame35,
       "xcmPidDocuPrintAyame35V1": xcmPidDocuPrintAyame35V1,
       "xcmPidDocuPrintN4525": xcmPidDocuPrintN4525,
       "xcmPidDocuPrintN4525V1": xcmPidDocuPrintN4525V1,
       "xcmPidPhaser5400": xcmPidPhaser5400,
       "xcmPidPhaser5400V1": xcmPidPhaser5400V1,
       "xcmPidDocuPrintNCnn": xcmPidDocuPrintNCnn,
       "xcmPidDocuPrintNC70": xcmPidDocuPrintNC70,
       "xcmPidDocuPrintNC70V1": xcmPidDocuPrintNC70V1,
       "xcmPidDocuPrintNC80": xcmPidDocuPrintNC80,
       "xcmPidDocuPrintNC80V1": xcmPidDocuPrintNC80V1,
       "xcmPidMidRangeColorPrinters": xcmPidMidRangeColorPrinters,
       "xcmPidDCColorSeries50": xcmPidDCColorSeries50,
       "xcmPidDCColorSeries50M1": xcmPidDCColorSeries50M1,
       "xcmPidDCColorSeries50M1V1": xcmPidDCColorSeries50M1V1,
       "xcmPidDocuTechs": xcmPidDocuTechs,
       "xcmPidDocuTech6135": xcmPidDocuTech6135,
       "xcmPidDocuTech6135M1": xcmPidDocuTech6135M1,
       "xcmPidDocuTech6135M1V1": xcmPidDocuTech6135M1V1,
       "xcmPidDocuTech6135M1V2": xcmPidDocuTech6135M1V2,
       "xcmPidDocuTech6180": xcmPidDocuTech6180,
       "xcmPidDocuTech6180M1": xcmPidDocuTech6180M1,
       "xcmPidDocuTech6180M1V1": xcmPidDocuTech6180M1V1,
       "xcmPidDocuTech6180M1V2": xcmPidDocuTech6180M1V2,
       "xcmPidDocuTech6100": xcmPidDocuTech6100,
       "xcmPidDocuTech6100M1": xcmPidDocuTech6100M1,
       "xcmPidDocuTech6100M1V1": xcmPidDocuTech6100M1V1,
       "xcmPidDocuTech6100M1V2": xcmPidDocuTech6100M1V2,
       "xcmPidDocuTech6115": xcmPidDocuTech6115,
       "xcmPidDocuTech6115M1": xcmPidDocuTech6115M1,
       "xcmPidDocuTech6115M1V1": xcmPidDocuTech6115M1V1,
       "xcmPidDocuTech6115M1V2": xcmPidDocuTech6115M1V2,
       "xcmPidDocuTech6155": xcmPidDocuTech6155,
       "xcmPidDocuTech6155M1": xcmPidDocuTech6155M1,
       "xcmPidDocuTech6155M1V1": xcmPidDocuTech6155M1V1,
       "xcmPidDocuTech6155M1V2": xcmPidDocuTech6155M1V2,
       "xcmPidDocuTech6075": xcmPidDocuTech6075,
       "xcmPidDocuTech6075M1": xcmPidDocuTech6075M1,
       "xcmPidDocuTech6075M1V1": xcmPidDocuTech6075M1V1,
       "xcmPidDocuTech6090": xcmPidDocuTech6090,
       "xcmPidDocuTech6090M1": xcmPidDocuTech6090M1,
       "xcmPidDocuTech6090M1V1": xcmPidDocuTech6090M1V1,
       "xcmPidDocuTechHiColorEPS": xcmPidDocuTechHiColorEPS,
       "xcmPidDocuSPDFE": xcmPidDocuSPDFE,
       "xcmPidDocuSPDFEColor": xcmPidDocuSPDFEColor,
       "xcmPidDocuSPTEAK": xcmPidDocuSPTEAK,
       "xcmPidDedPrintServers": xcmPidDedPrintServers,
       "xcmPidPhaserPrintServer": xcmPidPhaserPrintServer,
       "xcmPidPhaserEX7750": xcmPidPhaserEX7750,
       "xcmPidPhaserEX7750GX": xcmPidPhaserEX7750GX,
       "xcmPidPhaserEX7750DXF": xcmPidPhaserEX7750DXF,
       "xcmPidDocuPrintNPS": xcmPidDocuPrintNPS,
       "xcmPidDP4050NPS": xcmPidDP4050NPS,
       "xcmPidDP4050NPSM1": xcmPidDP4050NPSM1,
       "xcmPidDP4050NPSM1V1": xcmPidDP4050NPSM1V1,
       "xcmPidDP4090NPS": xcmPidDP4090NPS,
       "xcmPidDP4090NPSM1": xcmPidDP4090NPSM1,
       "xcmPidDP4090NPSM1V1": xcmPidDP4090NPSM1V1,
       "xcmPidDP4850NPS": xcmPidDP4850NPS,
       "xcmPidDP4850NPSM1": xcmPidDP4850NPSM1,
       "xcmPidDP4850NPSM1V1": xcmPidDP4850NPSM1V1,
       "xcmPidDP4890NPS": xcmPidDP4890NPS,
       "xcmPidDP4890NPSM1": xcmPidDP4890NPSM1,
       "xcmPidDP4890NPSM1V1": xcmPidDP4890NPSM1V1,
       "xcmPidDP4635NPS": xcmPidDP4635NPS,
       "xcmPidDP4635NPSM1": xcmPidDP4635NPSM1,
       "xcmPidDP4635NPSM1V1": xcmPidDP4635NPSM1V1,
       "xcmPidDP4635NPSMicr": xcmPidDP4635NPSMicr,
       "xcmPidDP4635NPSMicrV1": xcmPidDP4635NPSMicrV1,
       "xcmPidDP180NPS": xcmPidDP180NPS,
       "xcmPidDP180NPSM1": xcmPidDP180NPSM1,
       "xcmPidDP180NPSM1V1": xcmPidDP180NPSM1V1,
       "xcmPidDP180NPSMicr": xcmPidDP180NPSMicr,
       "xcmPidDP180NPSMicrV1": xcmPidDP180NPSMicrV1,
       "xcmPidDP96NPS": xcmPidDP96NPS,
       "xcmPidDP96NPSM1": xcmPidDP96NPSM1,
       "xcmPidDP96NPSM1V1": xcmPidDP96NPSM1V1,
       "xcmPidDP96NPSMicr": xcmPidDP96NPSMicr,
       "xcmPidDP96NPSMicrV1": xcmPidDP96NPSMicrV1,
       "xcmPidDP92cNPS": xcmPidDP92cNPS,
       "xcmPidDP92cNPSM1": xcmPidDP92cNPSM1,
       "xcmPidDP92cNPSM1V1": xcmPidDP92cNPSM1V1,
       "xcmPidDP155NPS": xcmPidDP155NPS,
       "xcmPidDP155NPSM1": xcmPidDP155NPSM1,
       "xcmPidDP155NPSM1V1": xcmPidDP155NPSM1V1,
       "xcmPidDP155NPSMicr": xcmPidDP155NPSMicr,
       "xcmPidDP155NPSMicrV1": xcmPidDP155NPSMicrV1,
       "xcmPidDP115NPS": xcmPidDP115NPS,
       "xcmPidDP115NPSM1": xcmPidDP115NPSM1,
       "xcmPidDP115NPSM1V1": xcmPidDP115NPSM1V1,
       "xcmPidDP115NPSMicr": xcmPidDP115NPSMicr,
       "xcmPidDP115NPSMicrV1": xcmPidDP115NPSMicrV1,
       "xcmPidDP100NPS": xcmPidDP100NPS,
       "xcmPidDP100NPSM1": xcmPidDP100NPSM1,
       "xcmPidDP100NPSM1V1": xcmPidDP100NPSM1V1,
       "xcmPidDP100NPSMicr": xcmPidDP100NPSMicr,
       "xcmPidDP100NPSMicrV1": xcmPidDP100NPSMicrV1,
       "xcmPidDC2000FamilyNPS": xcmPidDC2000FamilyNPS,
       "xcmPidDocuColor2045NPS": xcmPidDocuColor2045NPS,
       "xcmPidDocuColor2045NPSV1": xcmPidDocuColor2045NPSV1,
       "xcmPidDocuColor2060NPS": xcmPidDocuColor2060NPS,
       "xcmPidDocuColor2060NPSV1": xcmPidDocuColor2060NPSV1,
       "xcmPidDocuColor5252NPS": xcmPidDocuColor5252NPS,
       "xcmPidDocuColor5252NPSV1": xcmPidDocuColor5252NPSV1,
       "xcmPidDC6000FamilyNPS": xcmPidDC6000FamilyNPS,
       "xcmPidDocuColor6060NPS": xcmPidDocuColor6060NPS,
       "xcmPidDocuColor6060NPSV1": xcmPidDocuColor6060NPSV1,
       "xcmPidDocuColor2000Series": xcmPidDocuColor2000Series,
       "xcmPidDocuColor3000series": xcmPidDocuColor3000series,
       "xcmPidDocuColor240SPLASH": xcmPidDocuColor240SPLASH,
       "xcmPidDocuColor240SPLASHv1": xcmPidDocuColor240SPLASHv1,
       "xcmPidDocuColor250SPLASH": xcmPidDocuColor250SPLASH,
       "xcmPidDocuColor250SPLASHv1": xcmPidDocuColor250SPLASHv1,
       "xcmPidDocuColor242EFI": xcmPidDocuColor242EFI,
       "xcmPidDocuColor242EFIv1": xcmPidDocuColor242EFIv1,
       "xcmPidDocuColor242": xcmPidDocuColor242,
       "xcmPidDocuColor242v1": xcmPidDocuColor242v1,
       "xcmPidDocuColor252EFI": xcmPidDocuColor252EFI,
       "xcmPidDocuColor252EFIv1": xcmPidDocuColor252EFIv1,
       "xcmPidDocuColor252": xcmPidDocuColor252,
       "xcmPidDocuColor252v1": xcmPidDocuColor252v1,
       "xcmPidDocuColor260EFI": xcmPidDocuColor260EFI,
       "xcmPidDocuColor260EFIv1": xcmPidDocuColor260EFIv1,
       "xcmPidDocuColor260": xcmPidDocuColor260,
       "xcmPidDocuColor260v1": xcmPidDocuColor260v1,
       "xcmPidDocuColor242C": xcmPidDocuColor242C,
       "xcmPidDocuColor242Cv1": xcmPidDocuColor242Cv1,
       "xcmPidDocuColor242S": xcmPidDocuColor242S,
       "xcmPidDocuColor242Sv1": xcmPidDocuColor242Sv1,
       "xcmPidDocuColor252C": xcmPidDocuColor252C,
       "xcmPidDocuColor252Cv1": xcmPidDocuColor252Cv1,
       "xcmPidDocuColor252S": xcmPidDocuColor252S,
       "xcmPidDocuColor252Sv1": xcmPidDocuColor252Sv1,
       "xcmPidDocuColor260C": xcmPidDocuColor260C,
       "xcmPidDocuColor260Cv1": xcmPidDocuColor260Cv1,
       "xcmPidDocuColor260S": xcmPidDocuColor260S,
       "xcmPidDocuColor260Sv1": xcmPidDocuColor260Sv1,
       "xcmPidDocuPrintEPS": xcmPidDocuPrintEPS,
       "xcmPidDP180EPS": xcmPidDP180EPS,
       "xcmPidDP180EPSM1": xcmPidDP180EPSM1,
       "xcmPidDP180EPSM1V1": xcmPidDP180EPSM1V1,
       "xcmPidDP180EPSMicr": xcmPidDP180EPSMicr,
       "xcmPidDP180EPSMicrV1": xcmPidDP180EPSMicrV1,
       "xcmPidDP2000EPS": xcmPidDP2000EPS,
       "xcmPidDP2000S100EPS": xcmPidDP2000S100EPS,
       "xcmPidDP2000S100EPSV1": xcmPidDP2000S100EPSV1,
       "xcmPidDP2000S115EPS": xcmPidDP2000S115EPS,
       "xcmPidDP2000S115EPSV1": xcmPidDP2000S115EPSV1,
       "xcmPidDP2000S135EPS": xcmPidDP2000S135EPS,
       "xcmPidDP2000S135EPSV1": xcmPidDP2000S135EPSV1,
       "xcmPidDP2000S155EPS": xcmPidDP2000S155EPS,
       "xcmPidDP2000S155EPSV1": xcmPidDP2000S155EPSV1,
       "xcmPidDP2000S180EPS": xcmPidDP2000S180EPS,
       "xcmPidDP2000S180EPSV1": xcmPidDP2000S180EPSV1,
       "xcmPidDP2000S6075": xcmPidDP2000S6075,
       "xcmPidDP2000S6075V1": xcmPidDP2000S6075V1,
       "xcmPidDP2000S6090": xcmPidDP2000S6090,
       "xcmPidDP2000S6090V1": xcmPidDP2000S6090V1,
       "xcmPidDP2000S100EPSMX": xcmPidDP2000S100EPSMX,
       "xcmPidDP2000S100EPSMXV1": xcmPidDP2000S100EPSMXV1,
       "xcmPidDP2000S115EPSMX": xcmPidDP2000S115EPSMX,
       "xcmPidDP2000S115EPSMXV1": xcmPidDP2000S115EPSMXV1,
       "xcmPidDP2000S135EPSMX": xcmPidDP2000S135EPSMX,
       "xcmPidDP2000S135EPSMXV1": xcmPidDP2000S135EPSMXV1,
       "xcmPidDP2000S155EPSMX": xcmPidDP2000S155EPSMX,
       "xcmPidDP2000S155EPSMXV1": xcmPidDP2000S155EPSMXV1,
       "xcmPidDP2000S180EPSMX": xcmPidDP2000S180EPSMX,
       "xcmPidDP2000S180EPSMXV1": xcmPidDP2000S180EPSMXV1,
       "xcmPidXeroxPhaserPrinters": xcmPidXeroxPhaserPrinters,
       "xcmPidPhaser3yyyFamily": xcmPidPhaser3yyyFamily,
       "xcmPidPhaser3450": xcmPidPhaser3450,
       "xcmPidPhaser3450D": xcmPidPhaser3450D,
       "xcmPidPhaser3450DN": xcmPidPhaser3450DN,
       "xcmPidPhaser3450B": xcmPidPhaser3450B,
       "xcmPidPhaser3500": xcmPidPhaser3500,
       "xcmPidPhaser3500b": xcmPidPhaser3500b,
       "xcmPidPhaser3500n": xcmPidPhaser3500n,
       "xcmPidPhaser3150": xcmPidPhaser3150,
       "xcmPidPhaser3150b": xcmPidPhaser3150b,
       "xcmPidPhaser3150n": xcmPidPhaser3150n,
       "xcmPidPhaser3428": xcmPidPhaser3428,
       "xcmPidPhaser3428v1": xcmPidPhaser3428v1,
       "xcmPidPhaser3124": xcmPidPhaser3124,
       "xcmPidPhaser3124v1": xcmPidPhaser3124v1,
       "xcmPidPhaser3125": xcmPidPhaser3125,
       "xcmPidPhaser3125v1": xcmPidPhaser3125v1,
       "xcmPidPhaser3250": xcmPidPhaser3250,
       "xcmPidPhaser3250v1": xcmPidPhaser3250v1,
       "xcmPidPhaser3600": xcmPidPhaser3600,
       "xcmPidPhaser3600v1": xcmPidPhaser3600v1,
       "xcmPidPhaser3100MFP": xcmPidPhaser3100MFP,
       "xcmPidPhaser3100MFPv1": xcmPidPhaser3100MFPv1,
       "xcmPidPhaser3100": xcmPidPhaser3100,
       "xcmPidPhaser3100v1": xcmPidPhaser3100v1,
       "xcmPidPhaser3435": xcmPidPhaser3435,
       "xcmPidPhaser3435v1": xcmPidPhaser3435v1,
       "xcmPidPhaser3300MFP": xcmPidPhaser3300MFP,
       "xcmPidPhaser3300MFPc1": xcmPidPhaser3300MFPc1,
       "xcmPidPhaser3300MFPc1v1": xcmPidPhaser3300MFPc1v1,
       "xcmPidPhaser3010": xcmPidPhaser3010,
       "xcmPidPhaser3010C1": xcmPidPhaser3010C1,
       "xcmPidPhaser3010C1V1": xcmPidPhaser3010C1V1,
       "xcmPidPhaser3040": xcmPidPhaser3040,
       "xcmPidPhaser3040C1": xcmPidPhaser3040C1,
       "xcmPidPhaser3040C1V1": xcmPidPhaser3040C1V1,
       "xcmPidPhaser4yyyFamily": xcmPidPhaser4yyyFamily,
       "xcmPidPhaser4400": xcmPidPhaser4400,
       "xcmPidPhaser4400N": xcmPidPhaser4400N,
       "xcmPidPhaser4400DT": xcmPidPhaser4400DT,
       "xcmPidPhaser4400DX": xcmPidPhaser4400DX,
       "xcmPidPhaser4400B": xcmPidPhaser4400B,
       "xcmPidPhaser4500": xcmPidPhaser4500,
       "xcmPidPhaser4500N": xcmPidPhaser4500N,
       "xcmPidPhaser4500DT": xcmPidPhaser4500DT,
       "xcmPidPhaser4500DX": xcmPidPhaser4500DX,
       "xcmPidPhaser4500B": xcmPidPhaser4500B,
       "xcmPidPhaser4510": xcmPidPhaser4510,
       "xcmPidPhaser4510B": xcmPidPhaser4510B,
       "xcmPidPhaser4510N": xcmPidPhaser4510N,
       "xcmPidPhaser4510DT": xcmPidPhaser4510DT,
       "xcmPidPhaser4510DX": xcmPidPhaser4510DX,
       "xcmPidPhaser5yyyFamily": xcmPidPhaser5yyyFamily,
       "xcmPidPhaser5500": xcmPidPhaser5500,
       "xcmPidPhaser5500B": xcmPidPhaser5500B,
       "xcmPidPhaser5500N": xcmPidPhaser5500N,
       "xcmPidPhaser5500DN": xcmPidPhaser5500DN,
       "xcmPidPhaser5500DT": xcmPidPhaser5500DT,
       "xcmPidPhaser5500DX": xcmPidPhaser5500DX,
       "xcmPidPhaser5550": xcmPidPhaser5550,
       "xcmPidPhaser5550B": xcmPidPhaser5550B,
       "xcmPidPhaser5550N": xcmPidPhaser5550N,
       "xcmPidPhaser5550DN": xcmPidPhaser5550DN,
       "xcmPidPhaser5550DT": xcmPidPhaser5550DT,
       "xcmPidPhaser5335": xcmPidPhaser5335,
       "xcmPidPhaser5335v1": xcmPidPhaser5335v1,
       "xcmPidPhaser6yyyFamily": xcmPidPhaser6yyyFamily,
       "xcmPidPhaser6200": xcmPidPhaser6200,
       "xcmPidPhaser6200B": xcmPidPhaser6200B,
       "xcmPidPhaser6200N": xcmPidPhaser6200N,
       "xcmPidPhaser6200DP": xcmPidPhaser6200DP,
       "xcmPidPhaser6200DX": xcmPidPhaser6200DX,
       "xcmPidPhaser6100": xcmPidPhaser6100,
       "xcmPidPhaser6100n": xcmPidPhaser6100n,
       "xcmPidPhaser6250": xcmPidPhaser6250,
       "xcmPidPhaser6250B": xcmPidPhaser6250B,
       "xcmPidPhaser6250N": xcmPidPhaser6250N,
       "xcmPidPhaser6250DP": xcmPidPhaser6250DP,
       "xcmPidPhaser6250DX": xcmPidPhaser6250DX,
       "xcmPidPhaser6250DT": xcmPidPhaser6250DT,
       "xcmPidPhaser6300": xcmPidPhaser6300,
       "xcmPidPhaser6300B": xcmPidPhaser6300B,
       "xcmPidPhaser6300N": xcmPidPhaser6300N,
       "xcmPidPhaser6300DN": xcmPidPhaser6300DN,
       "xcmPidPhaser6350": xcmPidPhaser6350,
       "xcmPidPhaser6350DP": xcmPidPhaser6350DP,
       "xcmPidPhaser6350DT": xcmPidPhaser6350DT,
       "xcmPidPhaser6350DX": xcmPidPhaser6350DX,
       "xcmPidPhaser6120": xcmPidPhaser6120,
       "xcmPidPhaser6120b": xcmPidPhaser6120b,
       "xcmPidPhaser6120n": xcmPidPhaser6120n,
       "xcmPidPhaser6360": xcmPidPhaser6360,
       "xcmPidPhaser6360N": xcmPidPhaser6360N,
       "xcmPidPhaser6360DN": xcmPidPhaser6360DN,
       "xcmPidPhaser6360DT": xcmPidPhaser6360DT,
       "xcmPidPhaser6360DX": xcmPidPhaser6360DX,
       "xcmPidPhaser6180": xcmPidPhaser6180,
       "xcmPidPhaser6180N": xcmPidPhaser6180N,
       "xcmPidPhaser6180DN": xcmPidPhaser6180DN,
       "xcmPidPhaser6110N": xcmPidPhaser6110N,
       "xcmPidPhaser6110Nv1": xcmPidPhaser6110Nv1,
       "xcmPidPhaser6115": xcmPidPhaser6115,
       "xcmPidPhaser6115N": xcmPidPhaser6115N,
       "xcmPidPhaser6115DN": xcmPidPhaser6115DN,
       "xcmPidPhaser6110MFP3": xcmPidPhaser6110MFP3,
       "xcmPidPhaser6110MFP3v1": xcmPidPhaser6110MFP3v1,
       "xcmPidPhaser6110MFP4": xcmPidPhaser6110MFP4,
       "xcmPidPhaser6110MFP4v1": xcmPidPhaser6110MFP4v1,
       "xcmPidPhaser6180MFP": xcmPidPhaser6180MFP,
       "xcmPidPhaser6180MFPN": xcmPidPhaser6180MFPN,
       "xcmPidPhaser6180MFPDN": xcmPidPhaser6180MFPDN,
       "xcmPidPhaser6130": xcmPidPhaser6130,
       "xcmPidPhaser6130N": xcmPidPhaser6130N,
       "xcmPidPhaser6125": xcmPidPhaser6125,
       "xcmPidPhaser6125N": xcmPidPhaser6125N,
       "xcmPidPhaser6280": xcmPidPhaser6280,
       "xcmPidPhaser6280N": xcmPidPhaser6280N,
       "xcmPidPhaser6280Nv1": xcmPidPhaser6280Nv1,
       "xcmPidPhaser6280DN": xcmPidPhaser6280DN,
       "xcmPidPhaser6280DNv1": xcmPidPhaser6280DNv1,
       "xcmPidPhaser6280DT": xcmPidPhaser6280DT,
       "xcmPidPhaser6280DTv1": xcmPidPhaser6280DTv1,
       "xcmPidPhaser6700": xcmPidPhaser6700,
       "xcmPidPhaser6700C1": xcmPidPhaser6700C1,
       "xcmPidPhaser6700C1V1": xcmPidPhaser6700C1V1,
       "xcmPidPhaser6700C2": xcmPidPhaser6700C2,
       "xcmPidPhaser6700C2V1": xcmPidPhaser6700C2V1,
       "xcmPidPhaser6700C3": xcmPidPhaser6700C3,
       "xcmPidPhaser6700C3V1": xcmPidPhaser6700C3V1,
       "xcmPidPhaser6700C4": xcmPidPhaser6700C4,
       "xcmPidPhaser6700C4V1": xcmPidPhaser6700C4V1,
       "xcmPidWorkCentre6015B": xcmPidWorkCentre6015B,
       "xcmPidWorkCentre6015BC1": xcmPidWorkCentre6015BC1,
       "xcmPidWorkCentre6015BC1V1": xcmPidWorkCentre6015BC1V1,
       "xcmPidPhaser6500": xcmPidPhaser6500,
       "xcmPidPhaser6500C1": xcmPidPhaser6500C1,
       "xcmPidPhaser6500C1V1": xcmPidPhaser6500C1V1,
       "xcmPidPhaser6500C2": xcmPidPhaser6500C2,
       "xcmPidPhaser6500C2V1": xcmPidPhaser6500C2V1,
       "xcmPidWorkCentre6505": xcmPidWorkCentre6505,
       "xcmPidWorkCentre6505C1": xcmPidWorkCentre6505C1,
       "xcmPidWorkCentre6505C1V1": xcmPidWorkCentre6505C1V1,
       "xcmPidWorkCentre6505C2": xcmPidWorkCentre6505C2,
       "xcmPidWorkCentre6505C2V1": xcmPidWorkCentre6505C2V1,
       "xcmPidPhaser6000": xcmPidPhaser6000,
       "xcmPidPhaser6000C1": xcmPidPhaser6000C1,
       "xcmPidPhaser6000C1V1": xcmPidPhaser6000C1V1,
       "xcmPidWorkCentre6015": xcmPidWorkCentre6015,
       "xcmPidWorkCentre6015C1": xcmPidWorkCentre6015C1,
       "xcmPidWorkCentre6015C1V1": xcmPidWorkCentre6015C1V1,
       "xcmPidWorkCentre6015C2": xcmPidWorkCentre6015C2,
       "xcmPidWorkCentre6015C2V1": xcmPidWorkCentre6015C2V1,
       "xcmPidPhaser6600": xcmPidPhaser6600,
       "xcmPidPhaser6600NC1": xcmPidPhaser6600NC1,
       "xcmPidPhaser6600NC1V1": xcmPidPhaser6600NC1V1,
       "xcmPidPhaser6600DNC2": xcmPidPhaser6600DNC2,
       "xcmPidPhaser6600DNC2V1": xcmPidPhaser6600DNC2V1,
       "xcmPidPhaser7yyyFamily": xcmPidPhaser7yyyFamily,
       "xcmPidPhaser7300": xcmPidPhaser7300,
       "xcmPidPhaser7300DN": xcmPidPhaser7300DN,
       "xcmPidPhaser7300N": xcmPidPhaser7300N,
       "xcmPidPhaser7300DT": xcmPidPhaser7300DT,
       "xcmPidPhaser7300DX": xcmPidPhaser7300DX,
       "xcmPidPhaser7300B": xcmPidPhaser7300B,
       "xcmPidPhaser7400": xcmPidPhaser7400,
       "xcmPidPhaser7400B": xcmPidPhaser7400B,
       "xcmPidPhaser7400N": xcmPidPhaser7400N,
       "xcmPidPhaser7400DN": xcmPidPhaser7400DN,
       "xcmPidPhaser7400DT": xcmPidPhaser7400DT,
       "xcmPidPhaser7400DX": xcmPidPhaser7400DX,
       "xcmPidPhaser7400DXF": xcmPidPhaser7400DXF,
       "xcmPidPhaser7750": xcmPidPhaser7750,
       "xcmPidPhaser7750B": xcmPidPhaser7750B,
       "xcmPidPhaser7750DN": xcmPidPhaser7750DN,
       "xcmPidPhaser7750GX": xcmPidPhaser7750GX,
       "xcmPidPhaser7750DXF": xcmPidPhaser7750DXF,
       "xcmPidPhaser7760": xcmPidPhaser7760,
       "xcmPidPhaser7760B": xcmPidPhaser7760B,
       "xcmPidPhaser7760DN": xcmPidPhaser7760DN,
       "xcmPidPhaser7760GX": xcmPidPhaser7760GX,
       "xcmPidPhaser7760DX": xcmPidPhaser7760DX,
       "xcmPidPhaser7800": xcmPidPhaser7800,
       "xcmPidPhaser7800NC1": xcmPidPhaser7800NC1,
       "xcmPidPhaser7800NC1V1": xcmPidPhaser7800NC1V1,
       "xcmPidPhaser7800DNC1": xcmPidPhaser7800DNC1,
       "xcmPidPhaser7800DNC1V1": xcmPidPhaser7800DNC1V1,
       "xcmPidPhaser7800GXC1": xcmPidPhaser7800GXC1,
       "xcmPidPhaser7800GXC1V1": xcmPidPhaser7800GXC1V1,
       "xcmPidPhaser7800DXC1": xcmPidPhaser7800DXC1,
       "xcmPidPhaser7800DXC1V1": xcmPidPhaser7800DXC1V1,
       "xcmPidPhaser7100": xcmPidPhaser7100,
       "xcmPidPhaser7100NC1": xcmPidPhaser7100NC1,
       "xcmPidPhaser7100NC1V1": xcmPidPhaser7100NC1V1,
       "xcmPidPhaser7100DNC1": xcmPidPhaser7100DNC1,
       "xcmPidPhaser7100DNC1V1": xcmPidPhaser7100DNC1V1,
       "xcmPidPhaser8yyyFamily": xcmPidPhaser8yyyFamily,
       "xcmPidPhaser8400": xcmPidPhaser8400,
       "xcmPidPhaser8400B": xcmPidPhaser8400B,
       "xcmPidPhaser8400N": xcmPidPhaser8400N,
       "xcmPidPhaser8400DP": xcmPidPhaser8400DP,
       "xcmPidPhaser8400DX": xcmPidPhaser8400DX,
       "xcmPidPhaser8400BD": xcmPidPhaser8400BD,
       "xcmPidPhaser8560": xcmPidPhaser8560,
       "xcmPidPhaser8560v1": xcmPidPhaser8560v1,
       "xcmPidPhaser8560p": xcmPidPhaser8560p,
       "xcmPidPhaser8560N": xcmPidPhaser8560N,
       "xcmPidPhaser8560DN": xcmPidPhaser8560DN,
       "xcmPidPhaser8560DT": xcmPidPhaser8560DT,
       "xcmPidPhaser8560DX": xcmPidPhaser8560DX,
       "xcmPidPhaser8560PP": xcmPidPhaser8560PP,
       "xcmPidPhaser8860": xcmPidPhaser8860,
       "xcmPidPhaser8860v1": xcmPidPhaser8860v1,
       "xcmPidPhaser8860MFP": xcmPidPhaser8860MFP,
       "xcmPidPhaser8860MFPv1": xcmPidPhaser8860MFPv1,
       "xcmPidP3200MFP": xcmPidP3200MFP,
       "xcmPidP3200MFPv1": xcmPidP3200MFPv1,
       "xcmPidPhaser9yyyFamily": xcmPidPhaser9yyyFamily,
       "xcmPidWorkCentreMFSystems": xcmPidWorkCentreMFSystems,
       "xcmPidWCPro": xcmPidWCPro,
       "xcmPidWCP32C": xcmPidWCP32C,
       "xcmPidWCP32CV1": xcmPidWCP32CV1,
       "xcmPidWCP32CV2": xcmPidWCP32CV2,
       "xcmPidWCP35": xcmPidWCP35,
       "xcmPidWCP35V1": xcmPidWCP35V1,
       "xcmPidWCP35V2": xcmPidWCP35V2,
       "xcmPidWCP40C": xcmPidWCP40C,
       "xcmPidWCP40CV1": xcmPidWCP40CV1,
       "xcmPidWCP40CV2": xcmPidWCP40CV2,
       "xcmPidWCP45": xcmPidWCP45,
       "xcmPidWCP45V1": xcmPidWCP45V1,
       "xcmPidWCP45V2": xcmPidWCP45V2,
       "xcmPidWCP55": xcmPidWCP55,
       "xcmPidWCP55V1": xcmPidWCP55V1,
       "xcmPidWCP55V2": xcmPidWCP55V2,
       "xcmPidWCP165": xcmPidWCP165,
       "xcmPidWCP165V1": xcmPidWCP165V1,
       "xcmPidWCP175": xcmPidWCP175,
       "xcmPidWCP175V1": xcmPidWCP175V1,
       "xcmPidWCPC2128": xcmPidWCPC2128,
       "xcmPidWCPC2128V1": xcmPidWCPC2128V1,
       "xcmPidWCPC2636": xcmPidWCPC2636,
       "xcmPidWCPC2636V1": xcmPidWCPC2636V1,
       "xcmPidWCPC3545": xcmPidWCPC3545,
       "xcmPidWCPC3545V1": xcmPidWCPC3545V1,
       "xcmPidWC265": xcmPidWC265,
       "xcmPidWC265V1": xcmPidWC265V1,
       "xcmPidWC275": xcmPidWC275,
       "xcmPidWC275V1": xcmPidWC275V1,
       "xcmPidWCP265": xcmPidWCP265,
       "xcmPidWCP265V1": xcmPidWCP265V1,
       "xcmPidWCP275": xcmPidWCP275,
       "xcmPidWCP275V1": xcmPidWCP275V1,
       "xcmPidWCPS265": xcmPidWCPS265,
       "xcmPidWCPS265V1": xcmPidWCPS265V1,
       "xcmPidWCPS275": xcmPidWCPS275,
       "xcmPidWCPS275V1": xcmPidWCPS275V1,
       "xcmPidWC7655": xcmPidWC7655,
       "xcmPidWC7655V1": xcmPidWC7655V1,
       "xcmPidWC7665": xcmPidWC7665,
       "xcmPidWC7665V1": xcmPidWC7665V1,
       "xcmPidWC7675": xcmPidWC7675,
       "xcmPidWC7675V1": xcmPidWC7675V1,
       "xcmPidWCMF": xcmPidWCMF,
       "xcmPidWCM35": xcmPidWCM35,
       "xcmPidWCM35V1": xcmPidWCM35V1,
       "xcmPidWCM35V2": xcmPidWCM35V2,
       "xcmPidWCM45": xcmPidWCM45,
       "xcmPidWCM45V1": xcmPidWCM45V1,
       "xcmPidWCM45V2": xcmPidWCM45V2,
       "xcmPidWCM55": xcmPidWCM55,
       "xcmPidWCM55V1": xcmPidWCM55V1,
       "xcmPidWCM55V2": xcmPidWCM55V2,
       "xcmPidWCM165": xcmPidWCM165,
       "xcmPidWCM165V1": xcmPidWCM165V1,
       "xcmPidWCM175": xcmPidWCM175,
       "xcmPidWCM175V1": xcmPidWCM175V1,
       "xcmPidWCMPS35": xcmPidWCMPS35,
       "xcmPidWCMPS35V1": xcmPidWCMPS35V1,
       "xcmPidWCMPS45": xcmPidWCMPS45,
       "xcmPidWCMPS45V1": xcmPidWCMPS45V1,
       "xcmPidWCMPS55": xcmPidWCMPS55,
       "xcmPidWCMPS55V1": xcmPidWCMPS55V1,
       "xcmPidWCMPS165": xcmPidWCMPS165,
       "xcmPidWCMPS165V1": xcmPidWCMPS165V1,
       "xcmPidWCMPS175": xcmPidWCMPS175,
       "xcmPidWCMPS175V1": xcmPidWCMPS175V1,
       "xcmPidWCMF28": xcmPidWCMF28,
       "xcmPidWCMFM28": xcmPidWCMFM28,
       "xcmPidWCPS232": xcmPidWCPS232,
       "xcmPidWCPS232V1": xcmPidWCPS232V1,
       "xcmPidWCPS238": xcmPidWCPS238,
       "xcmPidWCPS238V1": xcmPidWCPS238V1,
       "xcmPidWCPS245": xcmPidWCPS245,
       "xcmPidWCPS245V1": xcmPidWCPS245V1,
       "xcmPidWCPS255": xcmPidWCPS255,
       "xcmPidWCPS255V1": xcmPidWCPS255V1,
       "xcmPidWCP232": xcmPidWCP232,
       "xcmPidWCP232V1": xcmPidWCP232V1,
       "xcmPidWCP238": xcmPidWCP238,
       "xcmPidWCP238V1": xcmPidWCP238V1,
       "xcmPidWCP245": xcmPidWCP245,
       "xcmPidWCP245V1": xcmPidWCP245V1,
       "xcmPidWCP255": xcmPidWCP255,
       "xcmPidWCP255V1": xcmPidWCP255V1,
       "xcmPidWC232": xcmPidWC232,
       "xcmPidWC232V1": xcmPidWC232V1,
       "xcmPidWC238": xcmPidWC238,
       "xcmPidWC238V1": xcmPidWC238V1,
       "xcmPidWC245": xcmPidWC245,
       "xcmPidWC245V1": xcmPidWC245V1,
       "xcmPidWC255": xcmPidWC255,
       "xcmPidWC255V1": xcmPidWC255V1,
       "xcmPidWorkCentre5135": xcmPidWorkCentre5135,
       "xcmPidWorkCentre5135C1": xcmPidWorkCentre5135C1,
       "xcmPidWorkCentre5135C1V1": xcmPidWorkCentre5135C1V1,
       "xcmPidWorkCentre5135C1V2": xcmPidWorkCentre5135C1V2,
       "xcmPidWorkCentre5150": xcmPidWorkCentre5150,
       "xcmPidWorkCentre5150C1": xcmPidWorkCentre5150C1,
       "xcmPidWorkCentre5150C1V1": xcmPidWorkCentre5150C1V1,
       "xcmPidWorkCentre5150C1V2": xcmPidWorkCentre5150C1V2,
       "xcmPidWCMF3": xcmPidWCMF3,
       "xcmPidWC5632": xcmPidWC5632,
       "xcmPidWC5632V1": xcmPidWC5632V1,
       "xcmPidWC5638": xcmPidWC5638,
       "xcmPidWC5638V1": xcmPidWC5638V1,
       "xcmPidWC5645": xcmPidWC5645,
       "xcmPidWC5645V1": xcmPidWC5645V1,
       "xcmPidWC5655": xcmPidWC5655,
       "xcmPidWC5655V1": xcmPidWC5655V1,
       "xcmPidWC5665": xcmPidWC5665,
       "xcmPidWC5665V1": xcmPidWC5665V1,
       "xcmPidWC5675": xcmPidWC5675,
       "xcmPidWC5675V1": xcmPidWC5675V1,
       "xcmPidWCMF4": xcmPidWCMF4,
       "xcmPidWC5687": xcmPidWC5687,
       "xcmPidWC5687V1": xcmPidWC5687V1,
       "xcmPidWC5030": xcmPidWC5030,
       "xcmPidWC5030V1": xcmPidWC5030V1,
       "xcmPidWC5030V2": xcmPidWC5030V2,
       "xcmPidWC5050": xcmPidWC5050,
       "xcmPidWC5050V1": xcmPidWC5050V1,
       "xcmPidWC5050V2": xcmPidWC5050V2,
       "xcmPidWCMF5": xcmPidWCMF5,
       "xcmPidWC6400": xcmPidWC6400,
       "xcmPidWC6400S": xcmPidWC6400S,
       "xcmPidWC6400Sv1": xcmPidWC6400Sv1,
       "xcmPidWC6400Sv2": xcmPidWC6400Sv2,
       "xcmPidWC6400X": xcmPidWC6400X,
       "xcmPidWC6400Xv1": xcmPidWC6400Xv1,
       "xcmPidWC6400Xv2": xcmPidWC6400Xv2,
       "xcmPidWC6400XF": xcmPidWC6400XF,
       "xcmPidWC6400XFv1": xcmPidWC6400XFv1,
       "xcmPidWC6400XFv2": xcmPidWC6400XFv2,
       "xcmPidWorkCentre5735": xcmPidWorkCentre5735,
       "xcmPidWorkCentre5735C1": xcmPidWorkCentre5735C1,
       "xcmPidWorkCentre5735C1V1": xcmPidWorkCentre5735C1V1,
       "xcmPidWorkCentre5740": xcmPidWorkCentre5740,
       "xcmPidWorkCentre5740C1": xcmPidWorkCentre5740C1,
       "xcmPidWorkCentre5740C1V1": xcmPidWorkCentre5740C1V1,
       "xcmPidWorkCentre5745": xcmPidWorkCentre5745,
       "xcmPidWorkCentre5745C1": xcmPidWorkCentre5745C1,
       "xcmPidWorkCentre5745C1V1": xcmPidWorkCentre5745C1V1,
       "xcmPidWorkCentre5755": xcmPidWorkCentre5755,
       "xcmPidWorkCentre5755C1": xcmPidWorkCentre5755C1,
       "xcmPidWorkCentre5755C1V1": xcmPidWorkCentre5755C1V1,
       "xcmPidWorkCentre5765": xcmPidWorkCentre5765,
       "xcmPidWorkCentre5765C1": xcmPidWorkCentre5765C1,
       "xcmPidWorkCentre5765C1V1": xcmPidWorkCentre5765C1V1,
       "xcmPidWorkCentre5775": xcmPidWorkCentre5775,
       "xcmPidWorkCentre5775C1": xcmPidWorkCentre5775C1,
       "xcmPidWorkCentre5775C1V1": xcmPidWorkCentre5775C1V1,
       "xcmPidWorkCentre5790": xcmPidWorkCentre5790,
       "xcmPidWorkCentre5790C1": xcmPidWorkCentre5790C1,
       "xcmPidWorkCentre5790C1V1": xcmPidWorkCentre5790C1V1,
       "xcmPidWCMF6": xcmPidWCMF6,
       "xcmPidWorkCentre3045B": xcmPidWorkCentre3045B,
       "xcmPidWorkCentre3045BC1": xcmPidWorkCentre3045BC1,
       "xcmPidWorkCentre3045BC1V1": xcmPidWorkCentre3045BC1V1,
       "xcmPidWorkCentre3045NI": xcmPidWorkCentre3045NI,
       "xcmPidWorkCentre3045NIC1": xcmPidWorkCentre3045NIC1,
       "xcmPidWorkCentre3045NIC1V1": xcmPidWorkCentre3045NIC1V1,
       "xcmPidWorkCentre6605": xcmPidWorkCentre6605,
       "xcmPidWorkCentre6605NC1": xcmPidWorkCentre6605NC1,
       "xcmPidWorkCentre6605NC1V1": xcmPidWorkCentre6605NC1V1,
       "xcmPidWorkCentre6605DNC2": xcmPidWorkCentre6605DNC2,
       "xcmPidWorkCentre6605DNC2V1": xcmPidWorkCentre6605DNC2V1,
       "xcmPidWCMF7": xcmPidWCMF7,
       "xcmPidXeroxWideFormat": xcmPidXeroxWideFormat,
       "xcmPidNuveraProductLine": xcmPidNuveraProductLine,
       "xcmPidNuveraEAProductionSystemFamily": xcmPidNuveraEAProductionSystemFamily,
       "xcmPidNuvera100x120x144x157EAPS": xcmPidNuvera100x120x144x157EAPS,
       "xcmPidNuvera100x120x144x157EAPSEmbeddedFFPS": xcmPidNuvera100x120x144x157EAPSEmbeddedFFPS,
       "xcmPidNuvera100x120x144x157EAPSEmbeddedFFPSV1": xcmPidNuvera100x120x144x157EAPSEmbeddedFFPSV1,
       "xcmPidNuveraEAPerfectingProductionSystemFamily": xcmPidNuveraEAPerfectingProductionSystemFamily,
       "xcmPidNuvera200x288x314EAPPS": xcmPidNuvera200x288x314EAPPS,
       "xcmPidNuvera200x288x314EAPPSEmbeddedFFPS": xcmPidNuvera200x288x314EAPPSEmbeddedFFPS,
       "xcmPidNuvera200x288x314EAPPSEmbeddedFFPSv1": xcmPidNuvera200x288x314EAPPSEmbeddedFFPSv1,
       "xcmPidNuveraMXProductionSystemFamily": xcmPidNuveraMXProductionSystemFamily,
       "xcmPidNuvera100x120x144MXPS": xcmPidNuvera100x120x144MXPS,
       "xcmPidNuvera100x120x144MXPSEmbeddedFFPS": xcmPidNuvera100x120x144MXPSEmbeddedFFPS,
       "xcmPidNuvera100x120x144MXPSEmbeddedFFPSV1": xcmPidNuvera100x120x144MXPSEmbeddedFFPSV1,
       "xcmPidNuveraMXPerfectingProductionSystemFamily": xcmPidNuveraMXPerfectingProductionSystemFamily,
       "xcmPidNuvera200x288MXPPS": xcmPidNuvera200x288MXPPS,
       "xcmPidNuvera200x288MXPPSEmbeddedFFPS": xcmPidNuvera200x288MXPPSEmbeddedFFPS,
       "xcmPidNuvera200x288MXPPSEmbeddedFFPSV1": xcmPidNuvera200x288MXPPSEmbeddedFFPSV1,
       "xcmPidColorQube": xcmPidColorQube,
       "xcmPidColorQube9200": xcmPidColorQube9200,
       "xcmPidColorQube9201": xcmPidColorQube9201,
       "xcmPidColorQube9201C1": xcmPidColorQube9201C1,
       "xcmPidColorQube9201C1V1": xcmPidColorQube9201C1V1,
       "xcmPidColorQube9201C1V2": xcmPidColorQube9201C1V2,
       "xcmPidColorQube9201C1V3": xcmPidColorQube9201C1V3,
       "xcmPidColorQube9201C2": xcmPidColorQube9201C2,
       "xcmPidColorQube9201C2V1": xcmPidColorQube9201C2V1,
       "xcmPidColorQube9201C2V2": xcmPidColorQube9201C2V2,
       "xcmPidColorQube9202": xcmPidColorQube9202,
       "xcmPidColorQube9202C1": xcmPidColorQube9202C1,
       "xcmPidColorQube9202C1V1": xcmPidColorQube9202C1V1,
       "xcmPidColorQube9202C1V2": xcmPidColorQube9202C1V2,
       "xcmPidColorQube9202C1V3": xcmPidColorQube9202C1V3,
       "xcmPidColorQube9202C2": xcmPidColorQube9202C2,
       "xcmPidColorQube9202C2V1": xcmPidColorQube9202C2V1,
       "xcmPidColorQube9202C2V2": xcmPidColorQube9202C2V2,
       "xcmPidColorQube9203": xcmPidColorQube9203,
       "xcmPidColorQube9203C1": xcmPidColorQube9203C1,
       "xcmPidColorQube9203C1V1": xcmPidColorQube9203C1V1,
       "xcmPidColorQube9203C1V2": xcmPidColorQube9203C1V2,
       "xcmPidColorQube9203C1V3": xcmPidColorQube9203C1V3,
       "xcmPidColorQube9203C2": xcmPidColorQube9203C2,
       "xcmPidColorQube9203C2V1": xcmPidColorQube9203C2V1,
       "xcmPidColorQube9203C2V2": xcmPidColorQube9203C2V2,
       "xcmPidColorQube8x00": xcmPidColorQube8x00,
       "xcmPidColorQube8700": xcmPidColorQube8700,
       "xcmPidColorQube8700S": xcmPidColorQube8700S,
       "xcmPidColorQube8700Sv1": xcmPidColorQube8700Sv1,
       "xcmPidColorQube8700X": xcmPidColorQube8700X,
       "xcmPidColorQube8700Xv1": xcmPidColorQube8700Xv1,
       "xcmPidColorQube8700XF": xcmPidColorQube8700XF,
       "xcmPidColorQube8700XFv1": xcmPidColorQube8700XFv1,
       "xcmPidColorQube8900": xcmPidColorQube8900,
       "xcmPidColorQube8900X": xcmPidColorQube8900X,
       "xcmPidColorQube8900Xv1": xcmPidColorQube8900Xv1,
       "xcmPidColorQube8900S": xcmPidColorQube8900S,
       "xcmPidColorQube8900Sv1": xcmPidColorQube8900Sv1,
       "xcmPidColorQube9300": xcmPidColorQube9300,
       "xcmPidColorQube9301": xcmPidColorQube9301,
       "xcmPidColorQube9301C1": xcmPidColorQube9301C1,
       "xcmPidColorQube9301C1V1": xcmPidColorQube9301C1V1,
       "xcmPidColorQube9301C1V2": xcmPidColorQube9301C1V2,
       "xcmPidColorQube9302": xcmPidColorQube9302,
       "xcmPidColorQube9302C1": xcmPidColorQube9302C1,
       "xcmPidColorQube9302C1V1": xcmPidColorQube9302C1V1,
       "xcmPidColorQube9302C1V2": xcmPidColorQube9302C1V2,
       "xcmPidColorQube9303": xcmPidColorQube9303,
       "xcmPidColorQube9303C1": xcmPidColorQube9303C1,
       "xcmPidColorQube9303C1V1": xcmPidColorQube9303C1V1,
       "xcmPidColorQube9303C1V2": xcmPidColorQube9303C1V2,
       "xcmPidFXSystems": xcmPidFXSystems,
       "xcmPidEPCProductLine": xcmPidEPCProductLine,
       "xcmPidLPMProductLine": xcmPidLPMProductLine,
       "xcmPidDigitalPrintingPressProductLine": xcmPidDigitalPrintingPressProductLine}
)
