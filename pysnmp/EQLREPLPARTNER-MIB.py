# SNMP MIB module (EQLREPLPARTNER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLREPLPARTNER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:10 2024
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

(SiteIndex,
 eqliscsiVolumeReplSiteIndex) = mibBuilder.importSymbols(
    "EQLVOLUME-MIB",
    "SiteIndex",
    "eqliscsiVolumeReplSiteIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

eqlReplPartnerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 26)
)
eqlReplPartnerModule.setRevisions(
        ("2013-03-28 00:00",)
)


# Types definitions



class EqlReplPartnerTestStatus(Integer32):
    """Custom type EqlReplPartnerTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("remote-partner-not-configured", 3),
          ("unknown", 0),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlReplPartnerObjects_ObjectIdentity = ObjectIdentity
eqlReplPartnerObjects = _EqlReplPartnerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1)
)
_EqlReplPartnerTestTable_Object = MibTable
eqlReplPartnerTestTable = _EqlReplPartnerTestTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1)
)
if mibBuilder.loadTexts:
    eqlReplPartnerTestTable.setStatus("current")
_EqlReplPartnerTestEntry_Object = MibTableRow
eqlReplPartnerTestEntry = _EqlReplPartnerTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1)
)
eqlReplPartnerTestEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
)
if mibBuilder.loadTexts:
    eqlReplPartnerTestEntry.setStatus("current")
_EqlReplPartnerTestRowStatus_Type = RowStatus
_EqlReplPartnerTestRowStatus_Object = MibTableColumn
eqlReplPartnerTestRowStatus = _EqlReplPartnerTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 1),
    _EqlReplPartnerTestRowStatus_Type()
)
eqlReplPartnerTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlReplPartnerTestRowStatus.setStatus("current")
_EqlReplPartnerTestIPAddrStatus_Type = EqlReplPartnerTestStatus
_EqlReplPartnerTestIPAddrStatus_Object = MibTableColumn
eqlReplPartnerTestIPAddrStatus = _EqlReplPartnerTestIPAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 2),
    _EqlReplPartnerTestIPAddrStatus_Type()
)
eqlReplPartnerTestIPAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlReplPartnerTestIPAddrStatus.setStatus("current")
_EqlReplPartnerTestAuthStatus_Type = EqlReplPartnerTestStatus
_EqlReplPartnerTestAuthStatus_Object = MibTableColumn
eqlReplPartnerTestAuthStatus = _EqlReplPartnerTestAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 3),
    _EqlReplPartnerTestAuthStatus_Type()
)
eqlReplPartnerTestAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlReplPartnerTestAuthStatus.setStatus("current")


class _EqlReplPartnerTestAction_Type(Integer32):
    """Custom type eqlReplPartnerTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("start", 1))
    )


_EqlReplPartnerTestAction_Type.__name__ = "Integer32"
_EqlReplPartnerTestAction_Object = MibTableColumn
eqlReplPartnerTestAction = _EqlReplPartnerTestAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 4),
    _EqlReplPartnerTestAction_Type()
)
eqlReplPartnerTestAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlReplPartnerTestAction.setStatus("current")


class _EqlReplPartnerTestState_Type(Integer32):
    """Custom type eqlReplPartnerTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("error", 3),
          ("in-progress", 1),
          ("restarted", 4),
          ("unknown", 0))
    )


_EqlReplPartnerTestState_Type.__name__ = "Integer32"
_EqlReplPartnerTestState_Object = MibTableColumn
eqlReplPartnerTestState = _EqlReplPartnerTestState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 5),
    _EqlReplPartnerTestState_Type()
)
eqlReplPartnerTestState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlReplPartnerTestState.setStatus("current")


class _EqlReplPartnerTestMajorVersion_Type(Integer32):
    """Custom type eqlReplPartnerTestMajorVersion based on Integer32"""
    defaultValue = 0


_EqlReplPartnerTestMajorVersion_Object = MibTableColumn
eqlReplPartnerTestMajorVersion = _EqlReplPartnerTestMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 6),
    _EqlReplPartnerTestMajorVersion_Type()
)
eqlReplPartnerTestMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlReplPartnerTestMajorVersion.setStatus("current")


class _EqlReplPartnerTestMinorVersion_Type(Integer32):
    """Custom type eqlReplPartnerTestMinorVersion based on Integer32"""
    defaultValue = 0


_EqlReplPartnerTestMinorVersion_Object = MibTableColumn
eqlReplPartnerTestMinorVersion = _EqlReplPartnerTestMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 7),
    _EqlReplPartnerTestMinorVersion_Type()
)
eqlReplPartnerTestMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlReplPartnerTestMinorVersion.setStatus("current")


class _EqlReplPartnerTestMaintVersion_Type(Integer32):
    """Custom type eqlReplPartnerTestMaintVersion based on Integer32"""
    defaultValue = 0


_EqlReplPartnerTestMaintVersion_Object = MibTableColumn
eqlReplPartnerTestMaintVersion = _EqlReplPartnerTestMaintVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 8),
    _EqlReplPartnerTestMaintVersion_Type()
)
eqlReplPartnerTestMaintVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlReplPartnerTestMaintVersion.setStatus("current")
_EqlReplPartnerTestDelegatedSpace_Type = Counter64
_EqlReplPartnerTestDelegatedSpace_Object = MibTableColumn
eqlReplPartnerTestDelegatedSpace = _EqlReplPartnerTestDelegatedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 9),
    _EqlReplPartnerTestDelegatedSpace_Type()
)
eqlReplPartnerTestDelegatedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlReplPartnerTestDelegatedSpace.setStatus("current")
_EqlReplPartnerTestDelegatedSpaceUsed_Type = Counter64
_EqlReplPartnerTestDelegatedSpaceUsed_Object = MibTableColumn
eqlReplPartnerTestDelegatedSpaceUsed = _EqlReplPartnerTestDelegatedSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 10),
    _EqlReplPartnerTestDelegatedSpaceUsed_Type()
)
eqlReplPartnerTestDelegatedSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlReplPartnerTestDelegatedSpaceUsed.setStatus("current")
_EqlReplPartnerTestTimestamp_Type = Counter32
_EqlReplPartnerTestTimestamp_Object = MibTableColumn
eqlReplPartnerTestTimestamp = _EqlReplPartnerTestTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 26, 1, 1, 1, 11),
    _EqlReplPartnerTestTimestamp_Type()
)
eqlReplPartnerTestTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlReplPartnerTestTimestamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLREPLPARTNER-MIB",
    **{"EqlReplPartnerTestStatus": EqlReplPartnerTestStatus,
       "eqlReplPartnerModule": eqlReplPartnerModule,
       "eqlReplPartnerObjects": eqlReplPartnerObjects,
       "eqlReplPartnerTestTable": eqlReplPartnerTestTable,
       "eqlReplPartnerTestEntry": eqlReplPartnerTestEntry,
       "eqlReplPartnerTestRowStatus": eqlReplPartnerTestRowStatus,
       "eqlReplPartnerTestIPAddrStatus": eqlReplPartnerTestIPAddrStatus,
       "eqlReplPartnerTestAuthStatus": eqlReplPartnerTestAuthStatus,
       "eqlReplPartnerTestAction": eqlReplPartnerTestAction,
       "eqlReplPartnerTestState": eqlReplPartnerTestState,
       "eqlReplPartnerTestMajorVersion": eqlReplPartnerTestMajorVersion,
       "eqlReplPartnerTestMinorVersion": eqlReplPartnerTestMinorVersion,
       "eqlReplPartnerTestMaintVersion": eqlReplPartnerTestMaintVersion,
       "eqlReplPartnerTestDelegatedSpace": eqlReplPartnerTestDelegatedSpace,
       "eqlReplPartnerTestDelegatedSpaceUsed": eqlReplPartnerTestDelegatedSpaceUsed,
       "eqlReplPartnerTestTimestamp": eqlReplPartnerTestTimestamp}
)
