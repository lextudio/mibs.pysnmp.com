# SNMP MIB module (MEMOTECADMIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MEMOTECADMIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:57 2024
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

(Alias,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias")

(memotecAdmin,) = mibBuilder.importSymbols(
    "MEMOTEC-SMI",
    "memotecAdmin")

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



class _MemotecAdminCommunity_Type(DisplayString):
    """Custom type memotecAdminCommunity based on DisplayString"""
    defaultValue = OctetString("memotec")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MemotecAdminCommunity_Type.__name__ = "DisplayString"
_MemotecAdminCommunity_Object = MibScalar
memotecAdminCommunity = _MemotecAdminCommunity_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 1),
    _MemotecAdminCommunity_Type()
)
memotecAdminCommunity.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    memotecAdminCommunity.setStatus("mandatory")


class _MemotecAdminViewInacTimer_Type(Integer32):
    """Custom type memotecAdminViewInacTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_MemotecAdminViewInacTimer_Type.__name__ = "Integer32"
_MemotecAdminViewInacTimer_Object = MibScalar
memotecAdminViewInacTimer = _MemotecAdminViewInacTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 2),
    _MemotecAdminViewInacTimer_Type()
)
memotecAdminViewInacTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecAdminViewInacTimer.setStatus("mandatory")
_MemotecAdminAgentInterfaceAlias_Type = Alias
_MemotecAdminAgentInterfaceAlias_Object = MibScalar
memotecAdminAgentInterfaceAlias = _MemotecAdminAgentInterfaceAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 3),
    _MemotecAdminAgentInterfaceAlias_Type()
)
memotecAdminAgentInterfaceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecAdminAgentInterfaceAlias.setStatus("mandatory")


class _MemotecAdminStatisticsHeartBeat_Type(Integer32):
    """Custom type memotecAdminStatisticsHeartBeat based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MemotecAdminStatisticsHeartBeat_Type.__name__ = "Integer32"
_MemotecAdminStatisticsHeartBeat_Object = MibScalar
memotecAdminStatisticsHeartBeat = _MemotecAdminStatisticsHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 4),
    _MemotecAdminStatisticsHeartBeat_Type()
)
memotecAdminStatisticsHeartBeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecAdminStatisticsHeartBeat.setStatus("mandatory")


class _MemotecAdminCardAliveHeartBeat_Type(Integer32):
    """Custom type memotecAdminCardAliveHeartBeat based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MemotecAdminCardAliveHeartBeat_Type.__name__ = "Integer32"
_MemotecAdminCardAliveHeartBeat_Object = MibScalar
memotecAdminCardAliveHeartBeat = _MemotecAdminCardAliveHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 5),
    _MemotecAdminCardAliveHeartBeat_Type()
)
memotecAdminCardAliveHeartBeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecAdminCardAliveHeartBeat.setStatus("mandatory")
_MemotecAdminSecurity_ObjectIdentity = ObjectIdentity
memotecAdminSecurity = _MemotecAdminSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 3, 6)
)
_MemotecCommunityTable_Object = MibTable
memotecCommunityTable = _MemotecCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 1)
)
if mibBuilder.loadTexts:
    memotecCommunityTable.setStatus("mandatory")
_MemotecCommunityEntry_Object = MibTableRow
memotecCommunityEntry = _MemotecCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 1, 1)
)
memotecCommunityEntry.setIndexNames(
    (0, "MEMOTECADMIN-MIB", "memotecCommunityIndex"),
)
if mibBuilder.loadTexts:
    memotecCommunityEntry.setStatus("mandatory")


class _MemotecCommunityIndex_Type(Integer32):
    """Custom type memotecCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MemotecCommunityIndex_Type.__name__ = "Integer32"
_MemotecCommunityIndex_Object = MibTableColumn
memotecCommunityIndex = _MemotecCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 1, 1, 1),
    _MemotecCommunityIndex_Type()
)
memotecCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memotecCommunityIndex.setStatus("mandatory")


class _MemotecCommunityName_Type(DisplayString):
    """Custom type memotecCommunityName based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MemotecCommunityName_Type.__name__ = "DisplayString"
_MemotecCommunityName_Object = MibTableColumn
memotecCommunityName = _MemotecCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 1, 1, 2),
    _MemotecCommunityName_Type()
)
memotecCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecCommunityName.setStatus("mandatory")


class _MemotecCommunityNetAddress_Type(IpAddress):
    """Custom type memotecCommunityNetAddress based on IpAddress"""
    defaultValue = 0


_MemotecCommunityNetAddress_Object = MibTableColumn
memotecCommunityNetAddress = _MemotecCommunityNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 1, 1, 3),
    _MemotecCommunityNetAddress_Type()
)
memotecCommunityNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecCommunityNetAddress.setStatus("mandatory")


class _MemotecCommunityAccess_Type(Integer32):
    """Custom type memotecCommunityAccess based on Integer32"""
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
        *(("notAccess", 4),
          ("readOnly", 1),
          ("readWrite", 3),
          ("writeOnly", 2))
    )


_MemotecCommunityAccess_Type.__name__ = "Integer32"
_MemotecCommunityAccess_Object = MibTableColumn
memotecCommunityAccess = _MemotecCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 1, 1, 4),
    _MemotecCommunityAccess_Type()
)
memotecCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecCommunityAccess.setStatus("mandatory")


class _MemotecCommunitySecurityLevel_Type(Integer32):
    """Custom type memotecCommunitySecurityLevel based on Integer32"""
    defaultValue = 1


_MemotecCommunitySecurityLevel_Object = MibTableColumn
memotecCommunitySecurityLevel = _MemotecCommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 1, 1, 5),
    _MemotecCommunitySecurityLevel_Type()
)
memotecCommunitySecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecCommunitySecurityLevel.setStatus("mandatory")


class _MemotecCommunityRowStatus_Type(Integer32):
    """Custom type memotecCommunityRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MemotecCommunityRowStatus_Type.__name__ = "Integer32"
_MemotecCommunityRowStatus_Object = MibTableColumn
memotecCommunityRowStatus = _MemotecCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 1, 1, 6),
    _MemotecCommunityRowStatus_Type()
)
memotecCommunityRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecCommunityRowStatus.setStatus("mandatory")
_MemotecSecurityTable_Object = MibTable
memotecSecurityTable = _MemotecSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 2)
)
if mibBuilder.loadTexts:
    memotecSecurityTable.setStatus("mandatory")
_MemotecSecurityEntry_Object = MibTableRow
memotecSecurityEntry = _MemotecSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 2, 1)
)
memotecSecurityEntry.setIndexNames(
    (0, "MEMOTECADMIN-MIB", "memotecSecurityLevelIndex"),
    (0, "MEMOTECADMIN-MIB", "memotecSecurityViewIndex"),
)
if mibBuilder.loadTexts:
    memotecSecurityEntry.setStatus("mandatory")


class _MemotecSecurityLevelIndex_Type(Integer32):
    """Custom type memotecSecurityLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MemotecSecurityLevelIndex_Type.__name__ = "Integer32"
_MemotecSecurityLevelIndex_Object = MibTableColumn
memotecSecurityLevelIndex = _MemotecSecurityLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 2, 1, 1),
    _MemotecSecurityLevelIndex_Type()
)
memotecSecurityLevelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memotecSecurityLevelIndex.setStatus("mandatory")


class _MemotecSecurityViewIndex_Type(Integer32):
    """Custom type memotecSecurityViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MemotecSecurityViewIndex_Type.__name__ = "Integer32"
_MemotecSecurityViewIndex_Object = MibTableColumn
memotecSecurityViewIndex = _MemotecSecurityViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 2, 1, 2),
    _MemotecSecurityViewIndex_Type()
)
memotecSecurityViewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memotecSecurityViewIndex.setStatus("mandatory")
_MemotecSecurityView_Type = ObjectIdentifier
_MemotecSecurityView_Object = MibTableColumn
memotecSecurityView = _MemotecSecurityView_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 2, 1, 3),
    _MemotecSecurityView_Type()
)
memotecSecurityView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecSecurityView.setStatus("mandatory")


class _MemotecSecurityRowStatus_Type(Integer32):
    """Custom type memotecSecurityRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MemotecSecurityRowStatus_Type.__name__ = "Integer32"
_MemotecSecurityRowStatus_Object = MibTableColumn
memotecSecurityRowStatus = _MemotecSecurityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 2, 1, 5),
    _MemotecSecurityRowStatus_Type()
)
memotecSecurityRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecSecurityRowStatus.setStatus("mandatory")
_MemotecTrapTable_Object = MibTable
memotecTrapTable = _MemotecTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 3)
)
if mibBuilder.loadTexts:
    memotecTrapTable.setStatus("mandatory")
_MemotecTrapEntry_Object = MibTableRow
memotecTrapEntry = _MemotecTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 3, 1)
)
memotecTrapEntry.setIndexNames(
    (0, "MEMOTECADMIN-MIB", "memotecTrapIndex"),
)
if mibBuilder.loadTexts:
    memotecTrapEntry.setStatus("mandatory")


class _MemotecTrapIndex_Type(Integer32):
    """Custom type memotecTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MemotecTrapIndex_Type.__name__ = "Integer32"
_MemotecTrapIndex_Object = MibTableColumn
memotecTrapIndex = _MemotecTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 3, 1, 1),
    _MemotecTrapIndex_Type()
)
memotecTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memotecTrapIndex.setStatus("mandatory")


class _MemotecTrapNetAddress_Type(IpAddress):
    """Custom type memotecTrapNetAddress based on IpAddress"""
    defaultValue = 0


_MemotecTrapNetAddress_Object = MibTableColumn
memotecTrapNetAddress = _MemotecTrapNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 3, 1, 2),
    _MemotecTrapNetAddress_Type()
)
memotecTrapNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecTrapNetAddress.setStatus("mandatory")


class _MemotecTrapCommunity_Type(DisplayString):
    """Custom type memotecTrapCommunity based on DisplayString"""
    defaultValue = OctetString("public")


_MemotecTrapCommunity_Object = MibTableColumn
memotecTrapCommunity = _MemotecTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 3, 1, 3),
    _MemotecTrapCommunity_Type()
)
memotecTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecTrapCommunity.setStatus("mandatory")


class _MemotecTrapRowStatus_Type(Integer32):
    """Custom type memotecTrapRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MemotecTrapRowStatus_Type.__name__ = "Integer32"
_MemotecTrapRowStatus_Object = MibTableColumn
memotecTrapRowStatus = _MemotecTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 6, 3, 1, 4),
    _MemotecTrapRowStatus_Type()
)
memotecTrapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memotecTrapRowStatus.setStatus("mandatory")
_MemotecAdminMibs_ObjectIdentity = ObjectIdentity
memotecAdminMibs = _MemotecAdminMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 3, 7)
)


class _MemotecAdminMibModules_Type(OctetString):
    """Custom type memotecAdminMibModules based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_MemotecAdminMibModules_Type.__name__ = "OctetString"
_MemotecAdminMibModules_Object = MibScalar
memotecAdminMibModules = _MemotecAdminMibModules_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 7, 1),
    _MemotecAdminMibModules_Type()
)
memotecAdminMibModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memotecAdminMibModules.setStatus("mandatory")


class _MemotecAdminMibLevel_Type(Integer32):
    """Custom type memotecAdminMibLevel based on Integer32"""
    defaultValue = 0


_MemotecAdminMibLevel_Object = MibScalar
memotecAdminMibLevel = _MemotecAdminMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 3, 8),
    _MemotecAdminMibLevel_Type()
)
memotecAdminMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memotecAdminMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEMOTECADMIN-MIB",
    **{"memotecAdminCommunity": memotecAdminCommunity,
       "memotecAdminViewInacTimer": memotecAdminViewInacTimer,
       "memotecAdminAgentInterfaceAlias": memotecAdminAgentInterfaceAlias,
       "memotecAdminStatisticsHeartBeat": memotecAdminStatisticsHeartBeat,
       "memotecAdminCardAliveHeartBeat": memotecAdminCardAliveHeartBeat,
       "memotecAdminSecurity": memotecAdminSecurity,
       "memotecCommunityTable": memotecCommunityTable,
       "memotecCommunityEntry": memotecCommunityEntry,
       "memotecCommunityIndex": memotecCommunityIndex,
       "memotecCommunityName": memotecCommunityName,
       "memotecCommunityNetAddress": memotecCommunityNetAddress,
       "memotecCommunityAccess": memotecCommunityAccess,
       "memotecCommunitySecurityLevel": memotecCommunitySecurityLevel,
       "memotecCommunityRowStatus": memotecCommunityRowStatus,
       "memotecSecurityTable": memotecSecurityTable,
       "memotecSecurityEntry": memotecSecurityEntry,
       "memotecSecurityLevelIndex": memotecSecurityLevelIndex,
       "memotecSecurityViewIndex": memotecSecurityViewIndex,
       "memotecSecurityView": memotecSecurityView,
       "memotecSecurityRowStatus": memotecSecurityRowStatus,
       "memotecTrapTable": memotecTrapTable,
       "memotecTrapEntry": memotecTrapEntry,
       "memotecTrapIndex": memotecTrapIndex,
       "memotecTrapNetAddress": memotecTrapNetAddress,
       "memotecTrapCommunity": memotecTrapCommunity,
       "memotecTrapRowStatus": memotecTrapRowStatus,
       "memotecAdminMibs": memotecAdminMibs,
       "memotecAdminMibModules": memotecAdminMibModules,
       "memotecAdminMibLevel": memotecAdminMibLevel}
)
