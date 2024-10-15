# SNMP MIB module (EQLISCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLISCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:06 2024
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

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(iscsiSessionAttributesEntry,
 iscsiSessionStatsEntry) = mibBuilder.importSymbols(
    "ISCSI-MIB",
    "iscsiSessionAttributesEntry",
    "iscsiSessionStatsEntry")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
 experimental,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "experimental",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqliscsiExtModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 11)
)
eqliscsiExtModule.setRevisions(
        ("2002-06-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqliscsiExtObjects_ObjectIdentity = ObjectIdentity
eqliscsiExtObjects = _EqliscsiExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1)
)
_EqliscsiSessionStatsTable_Object = MibTable
eqliscsiSessionStatsTable = _EqliscsiSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1)
)
if mibBuilder.loadTexts:
    eqliscsiSessionStatsTable.setStatus("current")
_EqliscsiSessionStatsEntry_Object = MibTableRow
eqliscsiSessionStatsEntry = _EqliscsiSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eqliscsiSessionStatsEntry.setStatus("current")
_EqliscsiSsnErrorCount_Type = Counter32
_EqliscsiSsnErrorCount_Object = MibTableColumn
eqliscsiSsnErrorCount = _EqliscsiSsnErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 1),
    _EqliscsiSsnErrorCount_Type()
)
eqliscsiSsnErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSsnErrorCount.setStatus("current")
_EqliscsiSsnTimeUp_Type = Counter32
_EqliscsiSsnTimeUp_Object = MibTableColumn
eqliscsiSsnTimeUp = _EqliscsiSsnTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 2),
    _EqliscsiSsnTimeUp_Type()
)
eqliscsiSsnTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSsnTimeUp.setStatus("current")
_EqliscsiSsnTotalDataTrnsfrd_Type = Counter32
_EqliscsiSsnTotalDataTrnsfrd_Object = MibTableColumn
eqliscsiSsnTotalDataTrnsfrd = _EqliscsiSsnTotalDataTrnsfrd_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 3),
    _EqliscsiSsnTotalDataTrnsfrd_Type()
)
eqliscsiSsnTotalDataTrnsfrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSsnTotalDataTrnsfrd.setStatus("deprecated")
if mibBuilder.loadTexts:
    eqliscsiSsnTotalDataTrnsfrd.setUnits("KB")


class _EqliscsiNodeUuid_Type(OctetString):
    """Custom type eqliscsiNodeUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiNodeUuid_Type.__name__ = "OctetString"
_EqliscsiNodeUuid_Object = MibTableColumn
eqliscsiNodeUuid = _EqliscsiNodeUuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 4),
    _EqliscsiNodeUuid_Type()
)
eqliscsiNodeUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiNodeUuid.setStatus("current")
_EqliscsiSsnTotalDataTrnsfrd64_Type = Counter64
_EqliscsiSsnTotalDataTrnsfrd64_Object = MibTableColumn
eqliscsiSsnTotalDataTrnsfrd64 = _EqliscsiSsnTotalDataTrnsfrd64_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 5),
    _EqliscsiSsnTotalDataTrnsfrd64_Type()
)
eqliscsiSsnTotalDataTrnsfrd64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSsnTotalDataTrnsfrd64.setStatus("deprecated")
if mibBuilder.loadTexts:
    eqliscsiSsnTotalDataTrnsfrd64.setUnits("KB")


class _EqliscsiSsnMembers_Type(Opaque):
    """Custom type eqliscsiSsnMembers based on Opaque"""
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_EqliscsiSsnMembers_Type.__name__ = "Opaque"
_EqliscsiSsnMembers_Object = MibTableColumn
eqliscsiSsnMembers = _EqliscsiSsnMembers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 6),
    _EqliscsiSsnMembers_Type()
)
eqliscsiSsnMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSsnMembers.setStatus("current")


class _EqliscsiSsnRouteStats_Type(Opaque):
    """Custom type eqliscsiSsnRouteStats based on Opaque"""
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_EqliscsiSsnRouteStats_Type.__name__ = "Opaque"
_EqliscsiSsnRouteStats_Object = MibTableColumn
eqliscsiSsnRouteStats = _EqliscsiSsnRouteStats_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 7),
    _EqliscsiSsnRouteStats_Type()
)
eqliscsiSsnRouteStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSsnRouteStats.setStatus("current")


class _EqliscsiSsnLoadValue_Type(Unsigned32):
    """Custom type eqliscsiSsnLoadValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqliscsiSsnLoadValue_Type.__name__ = "Unsigned32"
_EqliscsiSsnLoadValue_Object = MibTableColumn
eqliscsiSsnLoadValue = _EqliscsiSsnLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 8),
    _EqliscsiSsnLoadValue_Type()
)
eqliscsiSsnLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSsnLoadValue.setStatus("current")
_EqliscsiSessionAttributesTable_Object = MibTable
eqliscsiSessionAttributesTable = _EqliscsiSessionAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 2)
)
if mibBuilder.loadTexts:
    eqliscsiSessionAttributesTable.setStatus("current")
_EqliscsiSessionAttributesEntry_Object = MibTableRow
eqliscsiSessionAttributesEntry = _EqliscsiSessionAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eqliscsiSessionAttributesEntry.setStatus("current")


class _EqliscsiSessionAttributesType_Type(Integer32):
    """Custom type eqliscsiSessionAttributesType based on Integer32"""
    defaultValue = 1

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
        *(("external", 1),
          ("replica", 4),
          ("syncrepl", 2),
          ("xcopy", 3))
    )


_EqliscsiSessionAttributesType_Type.__name__ = "Integer32"
_EqliscsiSessionAttributesType_Object = MibTableColumn
eqliscsiSessionAttributesType = _EqliscsiSessionAttributesType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 11, 1, 2, 1, 1),
    _EqliscsiSessionAttributesType_Type()
)
eqliscsiSessionAttributesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSessionAttributesType.setStatus("current")
iscsiSessionStatsEntry.registerAugmentions(
    ("EQLISCSI-MIB",
     "eqliscsiSessionStatsEntry")
)
eqliscsiSessionStatsEntry.setIndexNames(*iscsiSessionStatsEntry.getIndexNames())
iscsiSessionAttributesEntry.registerAugmentions(
    ("EQLISCSI-MIB",
     "eqliscsiSessionAttributesEntry")
)
eqliscsiSessionAttributesEntry.setIndexNames(*iscsiSessionAttributesEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLISCSI-MIB",
    **{"eqliscsiExtModule": eqliscsiExtModule,
       "eqliscsiExtObjects": eqliscsiExtObjects,
       "eqliscsiSessionStatsTable": eqliscsiSessionStatsTable,
       "eqliscsiSessionStatsEntry": eqliscsiSessionStatsEntry,
       "eqliscsiSsnErrorCount": eqliscsiSsnErrorCount,
       "eqliscsiSsnTimeUp": eqliscsiSsnTimeUp,
       "eqliscsiSsnTotalDataTrnsfrd": eqliscsiSsnTotalDataTrnsfrd,
       "eqliscsiNodeUuid": eqliscsiNodeUuid,
       "eqliscsiSsnTotalDataTrnsfrd64": eqliscsiSsnTotalDataTrnsfrd64,
       "eqliscsiSsnMembers": eqliscsiSsnMembers,
       "eqliscsiSsnRouteStats": eqliscsiSsnRouteStats,
       "eqliscsiSsnLoadValue": eqliscsiSsnLoadValue,
       "eqliscsiSessionAttributesTable": eqliscsiSessionAttributesTable,
       "eqliscsiSessionAttributesEntry": eqliscsiSessionAttributesEntry,
       "eqliscsiSessionAttributesType": eqliscsiSessionAttributesType}
)
