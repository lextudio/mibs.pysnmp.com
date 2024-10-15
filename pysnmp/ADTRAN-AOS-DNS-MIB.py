# SNMP MIB module (ADTRAN-AOS-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:05 2024
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

(adGenAOSApplications,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSApplications",
    "adGenAOSConformance")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenAOSDns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1)
)
adGenAOSDns.setRevisions(
        ("2012-04-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdDnsRequestErrorConditionTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("emptyResponse", 20),
          ("formatError", 1),
          ("malformedResponse", 17),
          ("nameError", 3),
          ("noError", 0),
          ("noServerCOnfigured", 24),
          ("notImplemented", 4),
          ("onlyRootAnswer", 22),
          ("parseError", 18),
          ("portDeficiency", 23),
          ("refused", 5),
          ("serverFailure", 2),
          ("timeoutWaitingForResponse", 19),
          ("udpSendError", 25),
          ("unsuportedRCode", 16),
          ("unsupportedType", 21))
    )



class AdDnsResourceRecordTypeTC(Integer32, TextualConvention):
    status = "current"
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
              28,
              33,
              65537)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("aaaa", 28),
          ("aplusaaaa", 65537),
          ("cname", 5),
          ("hinfo", 13),
          ("mb", 7),
          ("md", 3),
          ("mf", 4),
          ("mg", 8),
          ("minfo", 14),
          ("mr", 9),
          ("mx", 15),
          ("ns", 2),
          ("null", 10),
          ("ptr", 12),
          ("soa", 6),
          ("srv", 33),
          ("txt", 16),
          ("wks", 11))
    )



# MIB Managed Objects in the order of their OIDs

_AdDnsTraps_ObjectIdentity = ObjectIdentity
adDnsTraps = _AdDnsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 0)
)
_AdDnsTimestamp_Type = Unsigned32
_AdDnsTimestamp_Object = MibScalar
adDnsTimestamp = _AdDnsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 1),
    _AdDnsTimestamp_Type()
)
adDnsTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adDnsTimestamp.setStatus("current")
_AdDnsNameserverInetAddressType_Type = InetAddressType
_AdDnsNameserverInetAddressType_Object = MibScalar
adDnsNameserverInetAddressType = _AdDnsNameserverInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 2),
    _AdDnsNameserverInetAddressType_Type()
)
adDnsNameserverInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adDnsNameserverInetAddressType.setStatus("current")
_AdDnsNameserverInetAddress_Type = InetAddress
_AdDnsNameserverInetAddress_Object = MibScalar
adDnsNameserverInetAddress = _AdDnsNameserverInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 3),
    _AdDnsNameserverInetAddress_Type()
)
adDnsNameserverInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adDnsNameserverInetAddress.setStatus("current")
_AdDnsRequestErrorCondition_Type = AdDnsRequestErrorConditionTC
_AdDnsRequestErrorCondition_Object = MibScalar
adDnsRequestErrorCondition = _AdDnsRequestErrorCondition_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 4),
    _AdDnsRequestErrorCondition_Type()
)
adDnsRequestErrorCondition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adDnsRequestErrorCondition.setStatus("current")
_AdDnsDomainName_Type = DisplayString
_AdDnsDomainName_Object = MibScalar
adDnsDomainName = _AdDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 5),
    _AdDnsDomainName_Type()
)
adDnsDomainName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adDnsDomainName.setStatus("current")
_AdDnsResourceRecordType_Type = AdDnsResourceRecordTypeTC
_AdDnsResourceRecordType_Object = MibScalar
adDnsResourceRecordType = _AdDnsResourceRecordType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 6),
    _AdDnsResourceRecordType_Type()
)
adDnsResourceRecordType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adDnsResourceRecordType.setStatus("current")
_AdGenAOSDnsConformance_ObjectIdentity = ObjectIdentity
adGenAOSDnsConformance = _AdGenAOSDnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13)
)
_AdGenAOSDnsGroup_ObjectIdentity = ObjectIdentity
adGenAOSDnsGroup = _AdGenAOSDnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1)
)
_AdGenAOSDnsCompliances_ObjectIdentity = ObjectIdentity
adGenAOSDnsCompliances = _AdGenAOSDnsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 2)
)

# Managed Objects groups

adGenAOSDnsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1, 1)
)
adGenAOSDnsInfoGroup.setObjects(
      *(("ADTRAN-AOS-DNS-MIB", "adDnsTimestamp"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddressType"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddress"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsRequestErrorCondition"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsDomainName"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsResourceRecordType"))
)
if mibBuilder.loadTexts:
    adGenAOSDnsInfoGroup.setStatus("current")


# Notification objects

adDnsIndividualResolutionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 0, 1)
)
adDnsIndividualResolutionFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsTimestamp"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddressType"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddress"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsRequestErrorCondition"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsDomainName"),
        ("ADTRAN-AOS-DNS-MIB", "adDnsResourceRecordType"))
)
if mibBuilder.loadTexts:
    adDnsIndividualResolutionFailure.setStatus(
        "current"
    )


# Notifications groups

adGenAOSDnsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1, 2)
)
adGenAOSDnsNotificationGroup.setObjects(
    ("ADTRAN-AOS-DNS-MIB", "adDnsIndividualResolutionFailure")
)
if mibBuilder.loadTexts:
    adGenAOSDnsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSDnsFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSDnsFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-DNS-MIB",
    **{"AdDnsRequestErrorConditionTC": AdDnsRequestErrorConditionTC,
       "AdDnsResourceRecordTypeTC": AdDnsResourceRecordTypeTC,
       "adGenAOSDns": adGenAOSDns,
       "adDnsTraps": adDnsTraps,
       "adDnsIndividualResolutionFailure": adDnsIndividualResolutionFailure,
       "adDnsTimestamp": adDnsTimestamp,
       "adDnsNameserverInetAddressType": adDnsNameserverInetAddressType,
       "adDnsNameserverInetAddress": adDnsNameserverInetAddress,
       "adDnsRequestErrorCondition": adDnsRequestErrorCondition,
       "adDnsDomainName": adDnsDomainName,
       "adDnsResourceRecordType": adDnsResourceRecordType,
       "adGenAOSDnsConformance": adGenAOSDnsConformance,
       "adGenAOSDnsGroup": adGenAOSDnsGroup,
       "adGenAOSDnsInfoGroup": adGenAOSDnsInfoGroup,
       "adGenAOSDnsNotificationGroup": adGenAOSDnsNotificationGroup,
       "adGenAOSDnsCompliances": adGenAOSDnsCompliances,
       "adGenAOSDnsFullCompliance": adGenAOSDnsFullCompliance}
)
