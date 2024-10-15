# SNMP MIB module (CTRON-SSR-SERVICE-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SSR-SERVICE-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:43 2024
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

(ssrMibs,) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

serviceStatusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 700)
)
serviceStatusMIB.setRevisions(
        ("2000-07-15 00:00",
         "1998-08-04 00:00",
         "1998-04-08 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ServiceStatus(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notWorking", 3),
          ("started", 1),
          ("stopped", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ServiceStatusGroup_ObjectIdentity = ObjectIdentity
serviceStatusGroup = _ServiceStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4)
)
_ServiceStatusRip_Type = ServiceStatus
_ServiceStatusRip_Object = MibScalar
serviceStatusRip = _ServiceStatusRip_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 1),
    _ServiceStatusRip_Type()
)
serviceStatusRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusRip.setStatus("current")
_ServiceStatusOspf_Type = ServiceStatus
_ServiceStatusOspf_Object = MibScalar
serviceStatusOspf = _ServiceStatusOspf_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 2),
    _ServiceStatusOspf_Type()
)
serviceStatusOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusOspf.setStatus("current")
_ServiceStatusBgp_Type = ServiceStatus
_ServiceStatusBgp_Object = MibScalar
serviceStatusBgp = _ServiceStatusBgp_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 3),
    _ServiceStatusBgp_Type()
)
serviceStatusBgp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusBgp.setStatus("current")
_ServiceStatusDvmrp_Type = ServiceStatus
_ServiceStatusDvmrp_Object = MibScalar
serviceStatusDvmrp = _ServiceStatusDvmrp_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 4),
    _ServiceStatusDvmrp_Type()
)
serviceStatusDvmrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusDvmrp.setStatus("current")
_ServiceStatusIgmp_Type = ServiceStatus
_ServiceStatusIgmp_Object = MibScalar
serviceStatusIgmp = _ServiceStatusIgmp_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 5),
    _ServiceStatusIgmp_Type()
)
serviceStatusIgmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusIgmp.setStatus("current")
_ServiceStatusPim_Type = ServiceStatus
_ServiceStatusPim_Object = MibScalar
serviceStatusPim = _ServiceStatusPim_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 6),
    _ServiceStatusPim_Type()
)
serviceStatusPim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusPim.setStatus("current")
_ServiceStatusStp_Type = ServiceStatus
_ServiceStatusStp_Object = MibScalar
serviceStatusStp = _ServiceStatusStp_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 7),
    _ServiceStatusStp_Type()
)
serviceStatusStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusStp.setStatus("current")
_ServiceStatusIpxRip_Type = ServiceStatus
_ServiceStatusIpxRip_Object = MibScalar
serviceStatusIpxRip = _ServiceStatusIpxRip_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 8),
    _ServiceStatusIpxRip_Type()
)
serviceStatusIpxRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusIpxRip.setStatus("current")
_ServiceStatusIpxSap_Type = ServiceStatus
_ServiceStatusIpxSap_Object = MibScalar
serviceStatusIpxSap = _ServiceStatusIpxSap_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 9),
    _ServiceStatusIpxSap_Type()
)
serviceStatusIpxSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusIpxSap.setStatus("current")
_ServiceStatusLfap_Type = ServiceStatus
_ServiceStatusLfap_Object = MibScalar
serviceStatusLfap = _ServiceStatusLfap_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 10),
    _ServiceStatusLfap_Type()
)
serviceStatusLfap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusLfap.setStatus("current")
_ServiceStatusRmon_Type = ServiceStatus
_ServiceStatusRmon_Object = MibScalar
serviceStatusRmon = _ServiceStatusRmon_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 4, 11),
    _ServiceStatusRmon_Type()
)
serviceStatusRmon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatusRmon.setStatus("current")
_SsConformance_ObjectIdentity = ObjectIdentity
ssConformance = _SsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2)
)
_SsCompliances_ObjectIdentity = ObjectIdentity
ssCompliances = _SsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 1)
)
_SsGroups_ObjectIdentity = ObjectIdentity
ssGroups = _SsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2)
)

# Managed Objects groups

ssConfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1)
)
ssConfGroupV10.setObjects(
      *(("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRip"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusOspf"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusBgp"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusDvmrp"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIgmp"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusPim"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusStp"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxRip"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxSap"))
)
if mibBuilder.loadTexts:
    ssConfGroupV10.setStatus("obsolete")

ssConfGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 2)
)
ssConfGroupV11.setObjects(
      *(("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRip"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusOspf"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusBgp"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusDvmrp"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIgmp"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusPim"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusStp"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxRip"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusIpxSap"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusLfap"),
        ("CTRON-SSR-SERVICE-STATUS-MIB", "serviceStatusRmon"))
)
if mibBuilder.loadTexts:
    ssConfGroupV11.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ssComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ssComplianceV10.setStatus(
        "obsolete"
    )

ssComplianceV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 700, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ssComplianceV11.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-SERVICE-STATUS-MIB",
    **{"ServiceStatus": ServiceStatus,
       "serviceStatusGroup": serviceStatusGroup,
       "serviceStatusRip": serviceStatusRip,
       "serviceStatusOspf": serviceStatusOspf,
       "serviceStatusBgp": serviceStatusBgp,
       "serviceStatusDvmrp": serviceStatusDvmrp,
       "serviceStatusIgmp": serviceStatusIgmp,
       "serviceStatusPim": serviceStatusPim,
       "serviceStatusStp": serviceStatusStp,
       "serviceStatusIpxRip": serviceStatusIpxRip,
       "serviceStatusIpxSap": serviceStatusIpxSap,
       "serviceStatusLfap": serviceStatusLfap,
       "serviceStatusRmon": serviceStatusRmon,
       "serviceStatusMIB": serviceStatusMIB,
       "ssConformance": ssConformance,
       "ssCompliances": ssCompliances,
       "ssGroups": ssGroups,
       "ssConfGroupV10": ssConfGroupV10,
       "ssComplianceV10": ssComplianceV10,
       "ssComplianceV11": ssComplianceV11,
       "ssConfGroupV11": ssConfGroupV11}
)
