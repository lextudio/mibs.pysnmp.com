# SNMP MIB module (HH3C-AFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-AFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:28 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cAFC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85)
)
hh3cAFC.setRevisions(
        ("2008-07-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cAFCLeaf_ObjectIdentity = ObjectIdentity
hh3cAFCLeaf = _Hh3cAFCLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1)
)
_Hh3cDDosAttackTargetIP_Type = IpAddress
_Hh3cDDosAttackTargetIP_Object = MibScalar
hh3cDDosAttackTargetIP = _Hh3cDDosAttackTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 1),
    _Hh3cDDosAttackTargetIP_Type()
)
hh3cDDosAttackTargetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackTargetIP.setStatus("current")


class _Hh3cDDosAttackType_Type(Integer32):
    """Custom type hh3cDDosAttackType based on Integer32"""
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


_Hh3cDDosAttackType_Type.__name__ = "Integer32"
_Hh3cDDosAttackType_Object = MibScalar
hh3cDDosAttackType = _Hh3cDDosAttackType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 2),
    _Hh3cDDosAttackType_Type()
)
hh3cDDosAttackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackType.setStatus("current")


class _Hh3cDDosAttackPolicy_Type(OctetString):
    """Custom type hh3cDDosAttackPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hh3cDDosAttackPolicy_Type.__name__ = "OctetString"
_Hh3cDDosAttackPolicy_Object = MibScalar
hh3cDDosAttackPolicy = _Hh3cDDosAttackPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 3),
    _Hh3cDDosAttackPolicy_Type()
)
hh3cDDosAttackPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackPolicy.setStatus("current")
_Hh3cDDosAttackThreshold_Type = Integer32
_Hh3cDDosAttackThreshold_Object = MibScalar
hh3cDDosAttackThreshold = _Hh3cDDosAttackThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 4),
    _Hh3cDDosAttackThreshold_Type()
)
hh3cDDosAttackThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackThreshold.setStatus("current")
_Hh3cDDosAttackSpeed_Type = Integer32
_Hh3cDDosAttackSpeed_Object = MibScalar
hh3cDDosAttackSpeed = _Hh3cDDosAttackSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 5),
    _Hh3cDDosAttackSpeed_Type()
)
hh3cDDosAttackSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackSpeed.setStatus("current")
_Hh3cAFCNotify_ObjectIdentity = ObjectIdentity
hh3cAFCNotify = _Hh3cAFCNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 2)
)
_Hh3cAFCNotifyPrefix_ObjectIdentity = ObjectIdentity
hh3cAFCNotifyPrefix = _Hh3cAFCNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cDDosAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0, 1)
)
hh3cDDosAttackStart.setObjects(
      *(("HH3C-AFC-MIB", "hh3cDDosAttackTargetIP"),
        ("HH3C-AFC-MIB", "hh3cDDosAttackType"),
        ("HH3C-AFC-MIB", "hh3cDDosAttackPolicy"),
        ("HH3C-AFC-MIB", "hh3cDDosAttackThreshold"),
        ("HH3C-AFC-MIB", "hh3cDDosAttackSpeed"))
)
if mibBuilder.loadTexts:
    hh3cDDosAttackStart.setStatus(
        "current"
    )

hh3cDDosAttackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0, 2)
)
hh3cDDosAttackEnd.setObjects(
    ("HH3C-AFC-MIB", "hh3cDDosAttackTargetIP")
)
if mibBuilder.loadTexts:
    hh3cDDosAttackEnd.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-AFC-MIB",
    **{"hh3cAFC": hh3cAFC,
       "hh3cAFCLeaf": hh3cAFCLeaf,
       "hh3cDDosAttackTargetIP": hh3cDDosAttackTargetIP,
       "hh3cDDosAttackType": hh3cDDosAttackType,
       "hh3cDDosAttackPolicy": hh3cDDosAttackPolicy,
       "hh3cDDosAttackThreshold": hh3cDDosAttackThreshold,
       "hh3cDDosAttackSpeed": hh3cDDosAttackSpeed,
       "hh3cAFCNotify": hh3cAFCNotify,
       "hh3cAFCNotifyPrefix": hh3cAFCNotifyPrefix,
       "hh3cDDosAttackStart": hh3cDDosAttackStart,
       "hh3cDDosAttackEnd": hh3cDDosAttackEnd}
)
