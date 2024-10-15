# SNMP MIB module (ACC-PROFILE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-PROFILE
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:48 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccProfile_ObjectIdentity = ObjectIdentity
accProfile = _AccProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46)
)
_AccProfileFilterTable_Object = MibTable
accProfileFilterTable = _AccProfileFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 1)
)
if mibBuilder.loadTexts:
    accProfileFilterTable.setStatus("mandatory")
_AccProfileFilterEntry_Object = MibTableRow
accProfileFilterEntry = _AccProfileFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 1, 1)
)
accProfileFilterEntry.setIndexNames(
    (0, "ACC-PROFILE", "accProfileName"),
)
if mibBuilder.loadTexts:
    accProfileFilterEntry.setStatus("mandatory")
_AccProfileName_Type = OctetString
_AccProfileName_Object = MibTableColumn
accProfileName = _AccProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 1, 1, 1),
    _AccProfileName_Type()
)
accProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProfileName.setStatus("mandatory")


class _AccProfileAction_Type(Integer32):
    """Custom type accProfileAction based on Integer32"""
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
        *(("add-element", 3),
          ("add-profile", 1),
          ("delete-element", 4),
          ("delete-profile", 2))
    )


_AccProfileAction_Type.__name__ = "Integer32"
_AccProfileAction_Object = MibTableColumn
accProfileAction = _AccProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 1, 1, 2),
    _AccProfileAction_Type()
)
accProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProfileAction.setStatus("mandatory")
_AccProfileFiltList_Type = OctetString
_AccProfileFiltList_Object = MibTableColumn
accProfileFiltList = _AccProfileFiltList_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 1, 1, 3),
    _AccProfileFiltList_Type()
)
accProfileFiltList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProfileFiltList.setStatus("mandatory")
_AccProfilePortTable_Object = MibTable
accProfilePortTable = _AccProfilePortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 2)
)
if mibBuilder.loadTexts:
    accProfilePortTable.setStatus("mandatory")
_AccProfilePortEntry_Object = MibTableRow
accProfilePortEntry = _AccProfilePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 2, 1)
)
accProfilePortEntry.setIndexNames(
    (0, "ACC-PROFILE", "accProfilePort"),
)
if mibBuilder.loadTexts:
    accProfilePortEntry.setStatus("mandatory")
_AccProfilePort_Type = Integer32
_AccProfilePort_Object = MibTableColumn
accProfilePort = _AccProfilePort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 2, 1, 1),
    _AccProfilePort_Type()
)
accProfilePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProfilePort.setStatus("mandatory")


class _AccProfilePortAction_Type(Integer32):
    """Custom type accProfilePortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add-profiles", 1),
          ("delete-profiles", 2))
    )


_AccProfilePortAction_Type.__name__ = "Integer32"
_AccProfilePortAction_Object = MibTableColumn
accProfilePortAction = _AccProfilePortAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 2, 1, 2),
    _AccProfilePortAction_Type()
)
accProfilePortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProfilePortAction.setStatus("mandatory")
_AccProfileList_Type = OctetString
_AccProfileList_Object = MibTableColumn
accProfileList = _AccProfileList_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 2, 1, 3),
    _AccProfileList_Type()
)
accProfileList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProfileList.setStatus("mandatory")
_AccProfileGlobalList_ObjectIdentity = ObjectIdentity
accProfileGlobalList = _AccProfileGlobalList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 3)
)
_AccProfileGlobalProfiles_Type = OctetString
_AccProfileGlobalProfiles_Object = MibScalar
accProfileGlobalProfiles = _AccProfileGlobalProfiles_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 3, 1),
    _AccProfileGlobalProfiles_Type()
)
accProfileGlobalProfiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProfileGlobalProfiles.setStatus("mandatory")


class _AccProfileGlobalAction_Type(Integer32):
    """Custom type accProfileGlobalAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add-profiles", 1),
          ("delete-profiles", 2))
    )


_AccProfileGlobalAction_Type.__name__ = "Integer32"
_AccProfileGlobalAction_Object = MibScalar
accProfileGlobalAction = _AccProfileGlobalAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 46, 3, 2),
    _AccProfileGlobalAction_Type()
)
accProfileGlobalAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProfileGlobalAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-PROFILE",
    **{"accProfile": accProfile,
       "accProfileFilterTable": accProfileFilterTable,
       "accProfileFilterEntry": accProfileFilterEntry,
       "accProfileName": accProfileName,
       "accProfileAction": accProfileAction,
       "accProfileFiltList": accProfileFiltList,
       "accProfilePortTable": accProfilePortTable,
       "accProfilePortEntry": accProfilePortEntry,
       "accProfilePort": accProfilePort,
       "accProfilePortAction": accProfilePortAction,
       "accProfileList": accProfileList,
       "accProfileGlobalList": accProfileGlobalList,
       "accProfileGlobalProfiles": accProfileGlobalProfiles,
       "accProfileGlobalAction": accProfileGlobalAction}
)
