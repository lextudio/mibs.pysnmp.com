# SNMP MIB module (IB-DNSONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IB-DNSONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:15 2024
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

(IbString,
 ibDNSOne) = mibBuilder.importSymbols(
    "IB-SMI-MIB",
    "IbString",
    "ibDNSOne")

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

ibDnsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1)
)
ibDnsModule.setRevisions(
        ("2010-03-23 00:00",
         "2005-06-09 00:00",
         "2005-01-10 00:00",
         "2004-05-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbZoneStatisticsTable_Object = MibTable
ibZoneStatisticsTable = _IbZoneStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibZoneStatisticsTable.setStatus("current")
_IbZoneStatisticsEntry_Object = MibTableRow
ibZoneStatisticsEntry = _IbZoneStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1)
)
ibZoneStatisticsEntry.setIndexNames(
    (0, "IB-DNSONE-MIB", "ibBindZoneName"),
)
if mibBuilder.loadTexts:
    ibZoneStatisticsEntry.setStatus("current")
_IbBindZoneName_Type = IbString
_IbBindZoneName_Object = MibTableColumn
ibBindZoneName = _IbBindZoneName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 1),
    _IbBindZoneName_Type()
)
ibBindZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZoneName.setStatus("current")
_IbBindZoneSuccess_Type = Counter64
_IbBindZoneSuccess_Object = MibTableColumn
ibBindZoneSuccess = _IbBindZoneSuccess_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 2),
    _IbBindZoneSuccess_Type()
)
ibBindZoneSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZoneSuccess.setStatus("current")
_IbBindZoneReferral_Type = Counter64
_IbBindZoneReferral_Object = MibTableColumn
ibBindZoneReferral = _IbBindZoneReferral_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 3),
    _IbBindZoneReferral_Type()
)
ibBindZoneReferral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZoneReferral.setStatus("current")
_IbBindZoneNxRRset_Type = Counter64
_IbBindZoneNxRRset_Object = MibTableColumn
ibBindZoneNxRRset = _IbBindZoneNxRRset_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 4),
    _IbBindZoneNxRRset_Type()
)
ibBindZoneNxRRset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZoneNxRRset.setStatus("current")
_IbBindZoneNxDomain_Type = Counter64
_IbBindZoneNxDomain_Object = MibTableColumn
ibBindZoneNxDomain = _IbBindZoneNxDomain_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 5),
    _IbBindZoneNxDomain_Type()
)
ibBindZoneNxDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZoneNxDomain.setStatus("current")
_IbBindZoneRecursion_Type = Counter64
_IbBindZoneRecursion_Object = MibTableColumn
ibBindZoneRecursion = _IbBindZoneRecursion_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 6),
    _IbBindZoneRecursion_Type()
)
ibBindZoneRecursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZoneRecursion.setStatus("current")
_IbBindZoneFailure_Type = Counter64
_IbBindZoneFailure_Object = MibTableColumn
ibBindZoneFailure = _IbBindZoneFailure_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 7),
    _IbBindZoneFailure_Type()
)
ibBindZoneFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZoneFailure.setStatus("current")
_IbZonePlusViewStatisticsTable_Object = MibTable
ibZonePlusViewStatisticsTable = _IbZonePlusViewStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ibZonePlusViewStatisticsTable.setStatus("current")
_IbZonePlusViewStatisticsEntry_Object = MibTableRow
ibZonePlusViewStatisticsEntry = _IbZonePlusViewStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1)
)
ibZonePlusViewStatisticsEntry.setIndexNames(
    (0, "IB-DNSONE-MIB", "ibBindViewName"),
    (0, "IB-DNSONE-MIB", "ibBindZonePlusViewName"),
)
if mibBuilder.loadTexts:
    ibZonePlusViewStatisticsEntry.setStatus("current")
_IbBindZonePlusViewName_Type = IbString
_IbBindZonePlusViewName_Object = MibTableColumn
ibBindZonePlusViewName = _IbBindZonePlusViewName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 1),
    _IbBindZonePlusViewName_Type()
)
ibBindZonePlusViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZonePlusViewName.setStatus("current")
_IbBindZonePlusViewSuccess_Type = Counter64
_IbBindZonePlusViewSuccess_Object = MibTableColumn
ibBindZonePlusViewSuccess = _IbBindZonePlusViewSuccess_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 2),
    _IbBindZonePlusViewSuccess_Type()
)
ibBindZonePlusViewSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZonePlusViewSuccess.setStatus("current")
_IbBindZonePlusViewReferral_Type = Counter64
_IbBindZonePlusViewReferral_Object = MibTableColumn
ibBindZonePlusViewReferral = _IbBindZonePlusViewReferral_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 3),
    _IbBindZonePlusViewReferral_Type()
)
ibBindZonePlusViewReferral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZonePlusViewReferral.setStatus("current")
_IbBindZonePlusViewNxRRset_Type = Counter64
_IbBindZonePlusViewNxRRset_Object = MibTableColumn
ibBindZonePlusViewNxRRset = _IbBindZonePlusViewNxRRset_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 4),
    _IbBindZonePlusViewNxRRset_Type()
)
ibBindZonePlusViewNxRRset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZonePlusViewNxRRset.setStatus("current")
_IbBindZonePlusViewNxDomain_Type = Counter64
_IbBindZonePlusViewNxDomain_Object = MibTableColumn
ibBindZonePlusViewNxDomain = _IbBindZonePlusViewNxDomain_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 5),
    _IbBindZonePlusViewNxDomain_Type()
)
ibBindZonePlusViewNxDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZonePlusViewNxDomain.setStatus("current")
_IbBindZonePlusViewRecursion_Type = Counter64
_IbBindZonePlusViewRecursion_Object = MibTableColumn
ibBindZonePlusViewRecursion = _IbBindZonePlusViewRecursion_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 6),
    _IbBindZonePlusViewRecursion_Type()
)
ibBindZonePlusViewRecursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZonePlusViewRecursion.setStatus("current")
_IbBindZonePlusViewFailure_Type = Counter64
_IbBindZonePlusViewFailure_Object = MibTableColumn
ibBindZonePlusViewFailure = _IbBindZonePlusViewFailure_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 7),
    _IbBindZonePlusViewFailure_Type()
)
ibBindZonePlusViewFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZonePlusViewFailure.setStatus("current")
_IbBindViewName_Type = IbString
_IbBindViewName_Object = MibTableColumn
ibBindViewName = _IbBindViewName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 8),
    _IbBindViewName_Type()
)
ibBindViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindViewName.setStatus("current")
_IbDDNSUpdateStatistics_ObjectIdentity = ObjectIdentity
ibDDNSUpdateStatistics = _IbDDNSUpdateStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3)
)
_IbDDNSUpdateSuccess_Type = Counter64
_IbDDNSUpdateSuccess_Object = MibScalar
ibDDNSUpdateSuccess = _IbDDNSUpdateSuccess_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 1),
    _IbDDNSUpdateSuccess_Type()
)
ibDDNSUpdateSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDDNSUpdateSuccess.setStatus("current")
_IbDDNSUpdateFailure_Type = Counter64
_IbDDNSUpdateFailure_Object = MibScalar
ibDDNSUpdateFailure = _IbDDNSUpdateFailure_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 2),
    _IbDDNSUpdateFailure_Type()
)
ibDDNSUpdateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDDNSUpdateFailure.setStatus("current")
_IbDDNSUpdateReject_Type = Counter64
_IbDDNSUpdateReject_Object = MibScalar
ibDDNSUpdateReject = _IbDDNSUpdateReject_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 3),
    _IbDDNSUpdateReject_Type()
)
ibDDNSUpdateReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDDNSUpdateReject.setStatus("current")
_IbDDNSUpdatePrerequisiteReject_Type = Counter64
_IbDDNSUpdatePrerequisiteReject_Object = MibScalar
ibDDNSUpdatePrerequisiteReject = _IbDDNSUpdatePrerequisiteReject_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 4),
    _IbDDNSUpdatePrerequisiteReject_Type()
)
ibDDNSUpdatePrerequisiteReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDDNSUpdatePrerequisiteReject.setStatus("current")
_IbBindZoneTransferCount_Type = Counter64
_IbBindZoneTransferCount_Object = MibScalar
ibBindZoneTransferCount = _IbBindZoneTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 4),
    _IbBindZoneTransferCount_Type()
)
ibBindZoneTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBindZoneTransferCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-DNSONE-MIB",
    **{"ibDnsModule": ibDnsModule,
       "ibZoneStatisticsTable": ibZoneStatisticsTable,
       "ibZoneStatisticsEntry": ibZoneStatisticsEntry,
       "ibBindZoneName": ibBindZoneName,
       "ibBindZoneSuccess": ibBindZoneSuccess,
       "ibBindZoneReferral": ibBindZoneReferral,
       "ibBindZoneNxRRset": ibBindZoneNxRRset,
       "ibBindZoneNxDomain": ibBindZoneNxDomain,
       "ibBindZoneRecursion": ibBindZoneRecursion,
       "ibBindZoneFailure": ibBindZoneFailure,
       "ibZonePlusViewStatisticsTable": ibZonePlusViewStatisticsTable,
       "ibZonePlusViewStatisticsEntry": ibZonePlusViewStatisticsEntry,
       "ibBindZonePlusViewName": ibBindZonePlusViewName,
       "ibBindZonePlusViewSuccess": ibBindZonePlusViewSuccess,
       "ibBindZonePlusViewReferral": ibBindZonePlusViewReferral,
       "ibBindZonePlusViewNxRRset": ibBindZonePlusViewNxRRset,
       "ibBindZonePlusViewNxDomain": ibBindZonePlusViewNxDomain,
       "ibBindZonePlusViewRecursion": ibBindZonePlusViewRecursion,
       "ibBindZonePlusViewFailure": ibBindZonePlusViewFailure,
       "ibBindViewName": ibBindViewName,
       "ibDDNSUpdateStatistics": ibDDNSUpdateStatistics,
       "ibDDNSUpdateSuccess": ibDDNSUpdateSuccess,
       "ibDDNSUpdateFailure": ibDDNSUpdateFailure,
       "ibDDNSUpdateReject": ibDDNSUpdateReject,
       "ibDDNSUpdatePrerequisiteReject": ibDDNSUpdatePrerequisiteReject,
       "ibBindZoneTransferCount": ibBindZoneTransferCount}
)
