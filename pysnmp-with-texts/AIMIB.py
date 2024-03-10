"""SNMP MIB module (AIMIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIMIB
Produced by pysmi-1.3.3 at Sun Mar 10 10:13:00 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(ObjectGroup,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ObjectGroup",
    "ModuleCompliance",
    "NotificationGroup")

(ObjectIdentity,
 Counter64,
 MibIdentifier,
 IpAddress,
 TimeTicks,
 NotificationType,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ModuleIdentity,
 Gauge32,
 iso,
 enterprises,
 Unsigned32,
 Bits,
 Counter32,
 Integer32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "ObjectIdentity",
    "Counter64",
    "MibIdentifier",
    "IpAddress",
    "TimeTicks",
    "NotificationType",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ModuleIdentity",
    "Gauge32",
    "iso",
    "enterprises",
    "Unsigned32",
    "Bits",
    "Counter32",
    "Integer32")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")


# MODULE-IDENTITY

aiHub = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 3)
)
aiHub.setLastUpdated("9505081700Z")
if mibBuilder.loadTexts:
    aiHub.setOrganization("""\
Applied Innovation Incorporated
""")
aiHub.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiHub.setDescription("""\
The MIB Module for Ethernet hubs
""")

aiCLC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 9)
)
aiCLC.setLastUpdated("9505081700Z")
if mibBuilder.loadTexts:
    aiCLC.setOrganization("""\
Applied Innovation Incorporated
""")
aiCLC.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiCLC.setDescription("""\
The MIB Module for the Common Logic Controller (CLC)
""")

aiSLC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 10)
)
aiSLC.setLastUpdated("9505081700Z")
if mibBuilder.loadTexts:
    aiSLC.setOrganization("""\
Applied Innovation Incorporated
""")
aiSLC.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSLC.setDescription("""\
The MIB Module for Smart Line Cards (SLC)
""")

aiSLC1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 11)
)
aiSLC1.setLastUpdated("9505081700Z")
if mibBuilder.loadTexts:
    aiSLC1.setOrganization("""\
Applied Innovation Incorporated
""")
aiSLC1.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSLC1.setDescription("""\
The MIB Module for Series One Smart Line Cards (SLC)
""")

aiX1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12)
)
aiX1.setLastUpdated("9505081700Z")
if mibBuilder.loadTexts:
    aiX1.setOrganization("""\
Applied Innovation Incorporated
""")
aiX1.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiX1.setDescription("""\
The MIB Module for Series One X.25 Smart Line Cards (SLC)
""")

aiTX1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 14)
)
aiTX1.setLastUpdated("9505081700Z")
if mibBuilder.loadTexts:
    aiTX1.setOrganization("""\
Applied Innovation Incorporated
""")
aiTX1.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiTX1.setDescription("""\
The MIB Module for Series One TCP/IP Smart Line Cards (SLC)
""")

aiTTL1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 15)
)
aiTTL1.setLastUpdated("9505081700Z")
if mibBuilder.loadTexts:
    aiTTL1.setOrganization("""\
Applied Innovation Incorporated
""")
aiTTL1.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiTTL1.setDescription("""\
The MIB Module for TTL1-196
""")

aiSLC2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16)
)
aiSLC2.setLastUpdated("9702211700Z")
if mibBuilder.loadTexts:
    aiSLC2.setOrganization("""\
Applied Innovation Incorporated
""")
aiSLC2.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSLC2.setDescription("""\
The MIB Module for Series Two Smart Line Cards (SLC)
""")

aiEts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 17)
)
aiEts.setLastUpdated("9702211700Z")
if mibBuilder.loadTexts:
    aiEts.setOrganization("""\
Applied Innovation Incorporated
""")
aiEts.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiEts.setDescription("""\
The MIB Module for E2A cards
""")

aiLpt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 18)
)
aiLpt.setLastUpdated("9804081700Z")
if mibBuilder.loadTexts:
    aiLpt.setOrganization("""\
Applied Innovation Incorporated
""")
aiLpt.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiLpt.setDescription("""\
The MIB Module for ILEG cards
""")

aiSpy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20)
)
aiSpy.setLastUpdated("9905101700Z")
if mibBuilder.loadTexts:
    aiSpy.setOrganization("""\
Applied Innovation Incorporated
""")
aiSpy.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, OH 43016-3271 Tel: 614/798-2000 Fax: 614/798-1770 E-mail:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSpy.setDescription("""\
The MIB Module for the AISpy
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiProxy_ObjectIdentity = ObjectIdentity
aiProxy = _AiProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 1)
)
_AiSystemOID_ObjectIdentity = ObjectIdentity
aiSystemOID = _AiSystemOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2)
)
_AiMgrSysOID_ObjectIdentity = ObjectIdentity
aiMgrSysOID = _AiMgrSysOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 1)
)
_AiMgrSysOIDVer1_ObjectIdentity = ObjectIdentity
aiMgrSysOIDVer1 = _AiMgrSysOIDVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 1, 1)
)
_AiMgrSysOIDVer2_ObjectIdentity = ObjectIdentity
aiMgrSysOIDVer2 = _AiMgrSysOIDVer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 1, 2)
)
_AiUProxy_ObjectIdentity = ObjectIdentity
aiUProxy = _AiUProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 2)
)
_AiUProxyVer1_ObjectIdentity = ObjectIdentity
aiUProxyVer1 = _AiUProxyVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 2, 1)
)
_Ai196IEGB_ObjectIdentity = ObjectIdentity
ai196IEGB = _Ai196IEGB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 3)
)
_Ai196IEGBVer1_ObjectIdentity = ObjectIdentity
ai196IEGBVer1 = _Ai196IEGBVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 3, 1)
)
_Ai196IEGBVer10_ObjectIdentity = ObjectIdentity
ai196IEGBVer10 = _Ai196IEGBVer10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 3, 1, 0)
)
_Ai196IEGBVer100_ObjectIdentity = ObjectIdentity
ai196IEGBVer100 = _Ai196IEGBVer100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 3, 1, 0, 0)
)
_Ai196IEGBVer101_ObjectIdentity = ObjectIdentity
ai196IEGBVer101 = _Ai196IEGBVer101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 3, 1, 0, 1)
)
_Ai196IEGBVer102_ObjectIdentity = ObjectIdentity
ai196IEGBVer102 = _Ai196IEGBVer102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 3, 1, 0, 2)
)
_Ai196E2A_ObjectIdentity = ObjectIdentity
ai196E2A = _Ai196E2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 4)
)
_Ai196E2AVer1_ObjectIdentity = ObjectIdentity
ai196E2AVer1 = _Ai196E2AVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 4, 1)
)
_Ai196E2AVer10_ObjectIdentity = ObjectIdentity
ai196E2AVer10 = _Ai196E2AVer10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 4, 1, 0)
)
_Ai196E2AVer100_ObjectIdentity = ObjectIdentity
ai196E2AVer100 = _Ai196E2AVer100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 4, 1, 0, 0)
)
_Ai196E2AVer101_ObjectIdentity = ObjectIdentity
ai196E2AVer101 = _Ai196E2AVer101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 4, 1, 0, 1)
)
_Ai196ILEG_ObjectIdentity = ObjectIdentity
ai196ILEG = _Ai196ILEG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 5)
)
_Ai193FT_ObjectIdentity = ObjectIdentity
ai193FT = _Ai193FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 6)
)
_Ai296_ObjectIdentity = ObjectIdentity
ai296 = _Ai296_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 7)
)
_Ai285_ObjectIdentity = ObjectIdentity
ai285 = _Ai285_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 9)
)
_AiScout_ObjectIdentity = ObjectIdentity
aiScout = _AiScout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 10)
)
_AiSpyOid_ObjectIdentity = ObjectIdentity
aiSpyOid = _AiSpyOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 11)
)
_Ai192_ObjectIdentity = ObjectIdentity
ai192 = _Ai192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192)
)
_Ai192Ver7_ObjectIdentity = ObjectIdentity
ai192Ver7 = _Ai192Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7)
)
_Ai192Ver70_ObjectIdentity = ObjectIdentity
ai192Ver70 = _Ai192Ver70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 0)
)
_Ai192Ver708_ObjectIdentity = ObjectIdentity
ai192Ver708 = _Ai192Ver708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 0, 8)
)
_Ai192Ver709_ObjectIdentity = ObjectIdentity
ai192Ver709 = _Ai192Ver709_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 0, 9)
)
_Ai192Ver71_ObjectIdentity = ObjectIdentity
ai192Ver71 = _Ai192Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 1)
)
_Ai192Ver710_ObjectIdentity = ObjectIdentity
ai192Ver710 = _Ai192Ver710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 1, 0)
)
_Ai192Ver72_ObjectIdentity = ObjectIdentity
ai192Ver72 = _Ai192Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 2)
)
_Ai192Ver720_ObjectIdentity = ObjectIdentity
ai192Ver720 = _Ai192Ver720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 2, 0)
)
_Ai192Ver77_ObjectIdentity = ObjectIdentity
ai192Ver77 = _Ai192Ver77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 7)
)
_Ai193_ObjectIdentity = ObjectIdentity
ai193 = _Ai193_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193)
)
_Ai193ES_ObjectIdentity = ObjectIdentity
ai193ES = _Ai193ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 2)
)
_Ai193ESVer7_ObjectIdentity = ObjectIdentity
ai193ESVer7 = _Ai193ESVer7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 2, 7)
)
_Ai193ESVer70_ObjectIdentity = ObjectIdentity
ai193ESVer70 = _Ai193ESVer70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 2, 7, 0)
)
_Ai193ESVer702_ObjectIdentity = ObjectIdentity
ai193ESVer702 = _Ai193ESVer702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 2, 7, 0, 2)
)
_Ai193ESVer703_ObjectIdentity = ObjectIdentity
ai193ESVer703 = _Ai193ESVer703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 2, 7, 0, 3)
)
_Ai193Ver7_ObjectIdentity = ObjectIdentity
ai193Ver7 = _Ai193Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7)
)
_Ai193Ver71_ObjectIdentity = ObjectIdentity
ai193Ver71 = _Ai193Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 1)
)
_Ai193Ver72_ObjectIdentity = ObjectIdentity
ai193Ver72 = _Ai193Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 2)
)
_Ai193Ver73_ObjectIdentity = ObjectIdentity
ai193Ver73 = _Ai193Ver73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 3)
)
_Ai193Ver74_ObjectIdentity = ObjectIdentity
ai193Ver74 = _Ai193Ver74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 4)
)
_Ai193Ver75_ObjectIdentity = ObjectIdentity
ai193Ver75 = _Ai193Ver75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 5)
)
_Ai193Ver76_ObjectIdentity = ObjectIdentity
ai193Ver76 = _Ai193Ver76_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 6)
)
_Ai193Ver77_ObjectIdentity = ObjectIdentity
ai193Ver77 = _Ai193Ver77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 7)
)
_Ai194_ObjectIdentity = ObjectIdentity
ai194 = _Ai194_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 194)
)
_Ai194Ver7_ObjectIdentity = ObjectIdentity
ai194Ver7 = _Ai194Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 194, 7)
)
_Ai194Ver71_ObjectIdentity = ObjectIdentity
ai194Ver71 = _Ai194Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 194, 7, 1)
)
_Ai194Ver72_ObjectIdentity = ObjectIdentity
ai194Ver72 = _Ai194Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 194, 7, 2)
)
_Ai194Ver73_ObjectIdentity = ObjectIdentity
ai194Ver73 = _Ai194Ver73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 194, 7, 3)
)
_Ai194Ver74_ObjectIdentity = ObjectIdentity
ai194Ver74 = _Ai194Ver74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 194, 7, 4)
)
_Ai195_ObjectIdentity = ObjectIdentity
ai195 = _Ai195_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 195)
)
_AiRTR_ObjectIdentity = ObjectIdentity
aiRTR = _AiRTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 195, 1)
)
_AiMPR_ObjectIdentity = ObjectIdentity
aiMPR = _AiMPR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 195, 2)
)
_AiMPRVer1_ObjectIdentity = ObjectIdentity
aiMPRVer1 = _AiMPRVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 195, 2, 1)
)
_Ai196_ObjectIdentity = ObjectIdentity
ai196 = _Ai196_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196)
)
_Ai196Ver7_ObjectIdentity = ObjectIdentity
ai196Ver7 = _Ai196Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7)
)
_Ai196Ver70_ObjectIdentity = ObjectIdentity
ai196Ver70 = _Ai196Ver70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 0)
)
_Ai196Ver708_ObjectIdentity = ObjectIdentity
ai196Ver708 = _Ai196Ver708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 0, 8)
)
_Ai196Ver709_ObjectIdentity = ObjectIdentity
ai196Ver709 = _Ai196Ver709_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 0, 9)
)
_Ai196Ver71_ObjectIdentity = ObjectIdentity
ai196Ver71 = _Ai196Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 1)
)
_Ai196Ver710_ObjectIdentity = ObjectIdentity
ai196Ver710 = _Ai196Ver710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 1, 0)
)
_Ai196Ver72_ObjectIdentity = ObjectIdentity
ai196Ver72 = _Ai196Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 2)
)
_Ai196Ver720_ObjectIdentity = ObjectIdentity
ai196Ver720 = _Ai196Ver720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 2, 0)
)
_Ai196Ver77_ObjectIdentity = ObjectIdentity
ai196Ver77 = _Ai196Ver77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 7)
)
_Ai196IVer8_ObjectIdentity = ObjectIdentity
ai196IVer8 = _Ai196IVer8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8)
)
_Ai196IVer80_ObjectIdentity = ObjectIdentity
ai196IVer80 = _Ai196IVer80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 0)
)
_Ai196IVer800_ObjectIdentity = ObjectIdentity
ai196IVer800 = _Ai196IVer800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 0, 0)
)
_Ai196IVer801_ObjectIdentity = ObjectIdentity
ai196IVer801 = _Ai196IVer801_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 0, 1)
)
_Ai196IVer802_ObjectIdentity = ObjectIdentity
ai196IVer802 = _Ai196IVer802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 0, 2)
)
_Ai196IVer81_ObjectIdentity = ObjectIdentity
ai196IVer81 = _Ai196IVer81_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 1)
)
_Ai196IVer810_ObjectIdentity = ObjectIdentity
ai196IVer810 = _Ai196IVer810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 1, 0)
)
_Ai196IVer82_ObjectIdentity = ObjectIdentity
ai196IVer82 = _Ai196IVer82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 2)
)
_Ai196IVer820_ObjectIdentity = ObjectIdentity
ai196IVer820 = _Ai196IVer820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 2, 0)
)
_Ai196IVer83_ObjectIdentity = ObjectIdentity
ai196IVer83 = _Ai196IVer83_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 3)
)
_Ai196IVer830_ObjectIdentity = ObjectIdentity
ai196IVer830 = _Ai196IVer830_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 3, 0)
)
_Ai196IVer831_ObjectIdentity = ObjectIdentity
ai196IVer831 = _Ai196IVer831_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 8, 3, 1)
)
_Ai198_ObjectIdentity = ObjectIdentity
ai198 = _Ai198_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198)
)
_Ai198Ver1_ObjectIdentity = ObjectIdentity
ai198Ver1 = _Ai198Ver1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1)
)
_Ai198Ver10_ObjectIdentity = ObjectIdentity
ai198Ver10 = _Ai198Ver10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0)
)
_Ai198Ver101_ObjectIdentity = ObjectIdentity
ai198Ver101 = _Ai198Ver101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0, 1)
)
_Ai198Ver102_ObjectIdentity = ObjectIdentity
ai198Ver102 = _Ai198Ver102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0, 2)
)
_Ai198Ver103_ObjectIdentity = ObjectIdentity
ai198Ver103 = _Ai198Ver103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0, 3)
)
_Ai198Ver104_ObjectIdentity = ObjectIdentity
ai198Ver104 = _Ai198Ver104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0, 4)
)
_Ai198Ver11_ObjectIdentity = ObjectIdentity
ai198Ver11 = _Ai198Ver11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 1)
)
_Ai198Ver12_ObjectIdentity = ObjectIdentity
ai198Ver12 = _Ai198Ver12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 2)
)
_Ai198Ver120_ObjectIdentity = ObjectIdentity
ai198Ver120 = _Ai198Ver120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 2, 0)
)
_Ai198Ver122_ObjectIdentity = ObjectIdentity
ai198Ver122 = _Ai198Ver122_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 2, 2)
)
_AiGroup_ObjectIdentity = ObjectIdentity
aiGroup = _AiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4)
)
_AiGroup194_ObjectIdentity = ObjectIdentity
aiGroup194 = _AiGroup194_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194)
)
_AiGroup194Ver7_ObjectIdentity = ObjectIdentity
aiGroup194Ver7 = _AiGroup194Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7)
)
_AiGroup194Ver71_ObjectIdentity = ObjectIdentity
aiGroup194Ver71 = _AiGroup194Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7, 1)
)
_AiGroup194Ver72_ObjectIdentity = ObjectIdentity
aiGroup194Ver72 = _AiGroup194Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7, 2)
)
_AiGroup194Ver73_ObjectIdentity = ObjectIdentity
aiGroup194Ver73 = _AiGroup194Ver73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7, 3)
)
_AiGroup194Ver74_ObjectIdentity = ObjectIdentity
aiGroup194Ver74 = _AiGroup194Ver74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 4, 194, 7, 4)
)
_AiISISGre_ObjectIdentity = ObjectIdentity
aiISISGre = _AiISISGre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 5)
)
_AiManager_ObjectIdentity = ObjectIdentity
aiManager = _AiManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 6)
)
_AiManagerTrapString_Type = DisplayString
_AiManagerTrapString_Object = MibScalar
aiManagerTrapString = _AiManagerTrapString_Object(
    (1, 3, 6, 1, 4, 1, 539, 6, 1),
    _AiManagerTrapString_Type()
)
aiManagerTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiManagerTrapString.setStatus("mandatory")
if mibBuilder.loadTexts:
    aiManagerTrapString.setDescription("""\
The string that is sent to xnmevents by aidaemon
""")
_AiManagerEnterprise_Type = ObjectIdentifier
_AiManagerEnterprise_Object = MibScalar
aiManagerEnterprise = _AiManagerEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 539, 6, 2),
    _AiManagerEnterprise_Type()
)
aiManagerEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiManagerEnterprise.setStatus("mandatory")
if mibBuilder.loadTexts:
    aiManagerEnterprise.setDescription("""\
The agent's system object ID.
""")
_AiManagerCommunity_Type = DisplayString
_AiManagerCommunity_Object = MibScalar
aiManagerCommunity = _AiManagerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 539, 6, 3),
    _AiManagerCommunity_Type()
)
aiManagerCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiManagerCommunity.setStatus("mandatory")
if mibBuilder.loadTexts:
    aiManagerCommunity.setDescription("""\
The agent's community string.
""")
_AiSoftware_ObjectIdentity = ObjectIdentity
aiSoftware = _AiSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 7)
)
_AiSystem_ObjectIdentity = ObjectIdentity
aiSystem = _AiSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 8)
)
_AiSLCSystem_ObjectIdentity = ObjectIdentity
aiSLCSystem = _AiSLCSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 10, 1)
)
_AiSLC1System_ObjectIdentity = ObjectIdentity
aiSLC1System = _AiSLC1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 11, 1)
)
_AiX1System_ObjectIdentity = ObjectIdentity
aiX1System = _AiX1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 1)
)
_AiX1Appl_ObjectIdentity = ObjectIdentity
aiX1Appl = _AiX1Appl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 2)
)
_AiX1Pkt_ObjectIdentity = ObjectIdentity
aiX1Pkt = _AiX1Pkt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 3)
)
_AiX1Frm_ObjectIdentity = ObjectIdentity
aiX1Frm = _AiX1Frm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 4)
)
_AiX1Phys_ObjectIdentity = ObjectIdentity
aiX1Phys = _AiX1Phys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 5)
)
_AiX1VC_ObjectIdentity = ObjectIdentity
aiX1VC = _AiX1VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 6)
)
_AiTX1System_ObjectIdentity = ObjectIdentity
aiTX1System = _AiTX1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 14, 1)
)
_AiTX1Calls_ObjectIdentity = ObjectIdentity
aiTX1Calls = _AiTX1Calls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 14, 2)
)
_AiPVC_ObjectIdentity = ObjectIdentity
aiPVC = _AiPVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 1)
)
_AiLink_ObjectIdentity = ObjectIdentity
aiLink = _AiLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 2)
)
_AiiSubnet_ObjectIdentity = ObjectIdentity
aiiSubnet = _AiiSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 3)
)
_Streams_ObjectIdentity = ObjectIdentity
streams = _Streams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIMIB",
    **{"aii": aii,
       "aiProxy": aiProxy,
       "aiSystemOID": aiSystemOID,
       "aiMgrSysOID": aiMgrSysOID,
       "aiMgrSysOIDVer1": aiMgrSysOIDVer1,
       "aiMgrSysOIDVer2": aiMgrSysOIDVer2,
       "aiUProxy": aiUProxy,
       "aiUProxyVer1": aiUProxyVer1,
       "ai196IEGB": ai196IEGB,
       "ai196IEGBVer1": ai196IEGBVer1,
       "ai196IEGBVer10": ai196IEGBVer10,
       "ai196IEGBVer100": ai196IEGBVer100,
       "ai196IEGBVer101": ai196IEGBVer101,
       "ai196IEGBVer102": ai196IEGBVer102,
       "ai196E2A": ai196E2A,
       "ai196E2AVer1": ai196E2AVer1,
       "ai196E2AVer10": ai196E2AVer10,
       "ai196E2AVer100": ai196E2AVer100,
       "ai196E2AVer101": ai196E2AVer101,
       "ai196ILEG": ai196ILEG,
       "ai193FT": ai193FT,
       "ai296": ai296,
       "ai285": ai285,
       "aiScout": aiScout,
       "aiSpyOid": aiSpyOid,
       "ai192": ai192,
       "ai192Ver7": ai192Ver7,
       "ai192Ver70": ai192Ver70,
       "ai192Ver708": ai192Ver708,
       "ai192Ver709": ai192Ver709,
       "ai192Ver71": ai192Ver71,
       "ai192Ver710": ai192Ver710,
       "ai192Ver72": ai192Ver72,
       "ai192Ver720": ai192Ver720,
       "ai192Ver77": ai192Ver77,
       "ai193": ai193,
       "ai193ES": ai193ES,
       "ai193ESVer7": ai193ESVer7,
       "ai193ESVer70": ai193ESVer70,
       "ai193ESVer702": ai193ESVer702,
       "ai193ESVer703": ai193ESVer703,
       "ai193Ver7": ai193Ver7,
       "ai193Ver71": ai193Ver71,
       "ai193Ver72": ai193Ver72,
       "ai193Ver73": ai193Ver73,
       "ai193Ver74": ai193Ver74,
       "ai193Ver75": ai193Ver75,
       "ai193Ver76": ai193Ver76,
       "ai193Ver77": ai193Ver77,
       "ai194": ai194,
       "ai194Ver7": ai194Ver7,
       "ai194Ver71": ai194Ver71,
       "ai194Ver72": ai194Ver72,
       "ai194Ver73": ai194Ver73,
       "ai194Ver74": ai194Ver74,
       "ai195": ai195,
       "aiRTR": aiRTR,
       "aiMPR": aiMPR,
       "aiMPRVer1": aiMPRVer1,
       "ai196": ai196,
       "ai196Ver7": ai196Ver7,
       "ai196Ver70": ai196Ver70,
       "ai196Ver708": ai196Ver708,
       "ai196Ver709": ai196Ver709,
       "ai196Ver71": ai196Ver71,
       "ai196Ver710": ai196Ver710,
       "ai196Ver72": ai196Ver72,
       "ai196Ver720": ai196Ver720,
       "ai196Ver77": ai196Ver77,
       "ai196IVer8": ai196IVer8,
       "ai196IVer80": ai196IVer80,
       "ai196IVer800": ai196IVer800,
       "ai196IVer801": ai196IVer801,
       "ai196IVer802": ai196IVer802,
       "ai196IVer81": ai196IVer81,
       "ai196IVer810": ai196IVer810,
       "ai196IVer82": ai196IVer82,
       "ai196IVer820": ai196IVer820,
       "ai196IVer83": ai196IVer83,
       "ai196IVer830": ai196IVer830,
       "ai196IVer831": ai196IVer831,
       "ai198": ai198,
       "ai198Ver1": ai198Ver1,
       "ai198Ver10": ai198Ver10,
       "ai198Ver101": ai198Ver101,
       "ai198Ver102": ai198Ver102,
       "ai198Ver103": ai198Ver103,
       "ai198Ver104": ai198Ver104,
       "ai198Ver11": ai198Ver11,
       "ai198Ver12": ai198Ver12,
       "ai198Ver120": ai198Ver120,
       "ai198Ver122": ai198Ver122,
       "aiHub": aiHub,
       "aiGroup": aiGroup,
       "aiGroup194": aiGroup194,
       "aiGroup194Ver7": aiGroup194Ver7,
       "aiGroup194Ver71": aiGroup194Ver71,
       "aiGroup194Ver72": aiGroup194Ver72,
       "aiGroup194Ver73": aiGroup194Ver73,
       "aiGroup194Ver74": aiGroup194Ver74,
       "aiISISGre": aiISISGre,
       "aiManager": aiManager,
       "aiManagerTrapString": aiManagerTrapString,
       "aiManagerEnterprise": aiManagerEnterprise,
       "aiManagerCommunity": aiManagerCommunity,
       "aiSoftware": aiSoftware,
       "aiSystem": aiSystem,
       "aiCLC": aiCLC,
       "aiSLC": aiSLC,
       "aiSLCSystem": aiSLCSystem,
       "aiSLC1": aiSLC1,
       "aiSLC1System": aiSLC1System,
       "aiX1": aiX1,
       "aiX1System": aiX1System,
       "aiX1Appl": aiX1Appl,
       "aiX1Pkt": aiX1Pkt,
       "aiX1Frm": aiX1Frm,
       "aiX1Phys": aiX1Phys,
       "aiX1VC": aiX1VC,
       "aiTX1": aiTX1,
       "aiTX1System": aiTX1System,
       "aiTX1Calls": aiTX1Calls,
       "aiTTL1": aiTTL1,
       "aiSLC2": aiSLC2,
       "aiPVC": aiPVC,
       "aiLink": aiLink,
       "aiiSubnet": aiiSubnet,
       "streams": streams,
       "aiEts": aiEts,
       "aiLpt": aiLpt,
       "aiSpy": aiSpy}
)
