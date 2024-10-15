# SNMP MIB module (HPN-ICF-AFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-AFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:27 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfAFC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85)
)
hpnicfAFC.setRevisions(
        ("2008-07-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfAFCLeaf_ObjectIdentity = ObjectIdentity
hpnicfAFCLeaf = _HpnicfAFCLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 1)
)
_HpnicfDDosAttackTargetIP_Type = IpAddress
_HpnicfDDosAttackTargetIP_Object = MibScalar
hpnicfDDosAttackTargetIP = _HpnicfDDosAttackTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 1, 1),
    _HpnicfDDosAttackTargetIP_Type()
)
hpnicfDDosAttackTargetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDDosAttackTargetIP.setStatus("current")


class _HpnicfDDosAttackType_Type(Integer32):
    """Custom type hpnicfDDosAttackType based on Integer32"""
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


_HpnicfDDosAttackType_Type.__name__ = "Integer32"
_HpnicfDDosAttackType_Object = MibScalar
hpnicfDDosAttackType = _HpnicfDDosAttackType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 1, 2),
    _HpnicfDDosAttackType_Type()
)
hpnicfDDosAttackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDDosAttackType.setStatus("current")


class _HpnicfDDosAttackPolicy_Type(OctetString):
    """Custom type hpnicfDDosAttackPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpnicfDDosAttackPolicy_Type.__name__ = "OctetString"
_HpnicfDDosAttackPolicy_Object = MibScalar
hpnicfDDosAttackPolicy = _HpnicfDDosAttackPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 1, 3),
    _HpnicfDDosAttackPolicy_Type()
)
hpnicfDDosAttackPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDDosAttackPolicy.setStatus("current")
_HpnicfDDosAttackThreshold_Type = Integer32
_HpnicfDDosAttackThreshold_Object = MibScalar
hpnicfDDosAttackThreshold = _HpnicfDDosAttackThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 1, 4),
    _HpnicfDDosAttackThreshold_Type()
)
hpnicfDDosAttackThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDDosAttackThreshold.setStatus("current")
_HpnicfDDosAttackSpeed_Type = Integer32
_HpnicfDDosAttackSpeed_Object = MibScalar
hpnicfDDosAttackSpeed = _HpnicfDDosAttackSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 1, 5),
    _HpnicfDDosAttackSpeed_Type()
)
hpnicfDDosAttackSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDDosAttackSpeed.setStatus("current")
_HpnicfAFCNotify_ObjectIdentity = ObjectIdentity
hpnicfAFCNotify = _HpnicfAFCNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 2)
)
_HpnicfAFCNotifyPrefix_ObjectIdentity = ObjectIdentity
hpnicfAFCNotifyPrefix = _HpnicfAFCNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfDDosAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 2, 0, 1)
)
hpnicfDDosAttackStart.setObjects(
      *(("HPN-ICF-AFC-MIB", "hpnicfDDosAttackTargetIP"),
        ("HPN-ICF-AFC-MIB", "hpnicfDDosAttackType"),
        ("HPN-ICF-AFC-MIB", "hpnicfDDosAttackPolicy"),
        ("HPN-ICF-AFC-MIB", "hpnicfDDosAttackThreshold"),
        ("HPN-ICF-AFC-MIB", "hpnicfDDosAttackSpeed"))
)
if mibBuilder.loadTexts:
    hpnicfDDosAttackStart.setStatus(
        "current"
    )

hpnicfDDosAttackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85, 2, 0, 2)
)
hpnicfDDosAttackEnd.setObjects(
    ("HPN-ICF-AFC-MIB", "hpnicfDDosAttackTargetIP")
)
if mibBuilder.loadTexts:
    hpnicfDDosAttackEnd.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-AFC-MIB",
    **{"hpnicfAFC": hpnicfAFC,
       "hpnicfAFCLeaf": hpnicfAFCLeaf,
       "hpnicfDDosAttackTargetIP": hpnicfDDosAttackTargetIP,
       "hpnicfDDosAttackType": hpnicfDDosAttackType,
       "hpnicfDDosAttackPolicy": hpnicfDDosAttackPolicy,
       "hpnicfDDosAttackThreshold": hpnicfDDosAttackThreshold,
       "hpnicfDDosAttackSpeed": hpnicfDDosAttackSpeed,
       "hpnicfAFCNotify": hpnicfAFCNotify,
       "hpnicfAFCNotifyPrefix": hpnicfAFCNotifyPrefix,
       "hpnicfDDosAttackStart": hpnicfDDosAttackStart,
       "hpnicfDDosAttackEnd": hpnicfDDosAttackEnd}
)
