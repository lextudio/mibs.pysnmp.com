# SNMP MIB module (A3COM-HUAWEI-AFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-AFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:19 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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


# MODULE-IDENTITY

h3cAFC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85)
)
h3cAFC.setRevisions(
        ("2008-07-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cAFCLeaf_ObjectIdentity = ObjectIdentity
h3cAFCLeaf = _H3cAFCLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1)
)
_H3cDDosAttackTargetIP_Type = IpAddress
_H3cDDosAttackTargetIP_Object = MibScalar
h3cDDosAttackTargetIP = _H3cDDosAttackTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 1),
    _H3cDDosAttackTargetIP_Type()
)
h3cDDosAttackTargetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackTargetIP.setStatus("current")


class _H3cDDosAttackType_Type(Integer32):
    """Custom type h3cDDosAttackType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              18,
              19,
              20,
              24,
              27,
              29,
              30,
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
              1024)
        )
    )
    namedValues = NamedValues(
        *(("ackabnormal", 42),
          ("appstreamalarm", 29),
          ("cc", 43),
          ("dnsabnormal", 35),
          ("fragflood", 24),
          ("fraggle", 3),
          ("ftpabnormal", 38),
          ("httpabnormal", 36),
          ("icmpflood", 6),
          ("icmpredirect", 8),
          ("icmpunreachable", 9),
          ("ipfragabnormal", 33),
          ("ipfragment", 15),
          ("land", 1),
          ("largeicmp", 18),
          ("otherabnormal", 1024),
          ("pingofdeath", 13),
          ("pop3abnormal", 40),
          ("routerecord", 20),
          ("scan", 27),
          ("sessionstreamalarm", 30),
          ("smtpabnormal", 39),
          ("smurf", 2),
          ("snmpabnormal", 41),
          ("sourceroute", 19),
          ("synflood", 5),
          ("tcpabnormal", 32),
          ("tcpflag", 12),
          ("teardrop", 14),
          ("telnetabnormal", 37),
          ("tftpabnormal", 34),
          ("tracert", 11),
          ("udpflood", 7),
          ("winnuke", 4))
    )


_H3cDDosAttackType_Type.__name__ = "Integer32"
_H3cDDosAttackType_Object = MibScalar
h3cDDosAttackType = _H3cDDosAttackType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 2),
    _H3cDDosAttackType_Type()
)
h3cDDosAttackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackType.setStatus("current")


class _H3cDDosAttackPolicy_Type(OctetString):
    """Custom type h3cDDosAttackPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_H3cDDosAttackPolicy_Type.__name__ = "OctetString"
_H3cDDosAttackPolicy_Object = MibScalar
h3cDDosAttackPolicy = _H3cDDosAttackPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 3),
    _H3cDDosAttackPolicy_Type()
)
h3cDDosAttackPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackPolicy.setStatus("current")
_H3cDDosAttackThreshold_Type = Integer32
_H3cDDosAttackThreshold_Object = MibScalar
h3cDDosAttackThreshold = _H3cDDosAttackThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 4),
    _H3cDDosAttackThreshold_Type()
)
h3cDDosAttackThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackThreshold.setStatus("current")
_H3cDDosAttackSpeed_Type = Integer32
_H3cDDosAttackSpeed_Object = MibScalar
h3cDDosAttackSpeed = _H3cDDosAttackSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 5),
    _H3cDDosAttackSpeed_Type()
)
h3cDDosAttackSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackSpeed.setStatus("current")
_H3cAFCNotify_ObjectIdentity = ObjectIdentity
h3cAFCNotify = _H3cAFCNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2)
)
_H3cAFCNotifyPrefix_ObjectIdentity = ObjectIdentity
h3cAFCNotifyPrefix = _H3cAFCNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cDDosAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0, 1)
)
h3cDDosAttackStart.setObjects(
      *(("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackTargetIP"),
        ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackType"),
        ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackPolicy"),
        ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackThreshold"),
        ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackSpeed"))
)
if mibBuilder.loadTexts:
    h3cDDosAttackStart.setStatus(
        "current"
    )

h3cDDosAttackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0, 2)
)
h3cDDosAttackEnd.setObjects(
    ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackTargetIP")
)
if mibBuilder.loadTexts:
    h3cDDosAttackEnd.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-AFC-MIB",
    **{"h3cAFC": h3cAFC,
       "h3cAFCLeaf": h3cAFCLeaf,
       "h3cDDosAttackTargetIP": h3cDDosAttackTargetIP,
       "h3cDDosAttackType": h3cDDosAttackType,
       "h3cDDosAttackPolicy": h3cDDosAttackPolicy,
       "h3cDDosAttackThreshold": h3cDDosAttackThreshold,
       "h3cDDosAttackSpeed": h3cDDosAttackSpeed,
       "h3cAFCNotify": h3cAFCNotify,
       "h3cAFCNotifyPrefix": h3cAFCNotifyPrefix,
       "h3cDDosAttackStart": h3cDDosAttackStart,
       "h3cDDosAttackEnd": h3cDDosAttackEnd}
)
