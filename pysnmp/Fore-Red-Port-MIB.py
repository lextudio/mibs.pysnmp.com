# SNMP MIB module (Fore-Red-Port-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Red-Port-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:11 2024
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

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

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

redPortConfModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RedPortConfTable_Object = MibTable
redPortConfTable = _RedPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    redPortConfTable.setStatus("current")
_RedPortConfEntry_Object = MibTableRow
redPortConfEntry = _RedPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1, 1)
)
redPortConfEntry.setIndexNames(
    (0, "Fore-Red-Port-MIB", "redPortBoard"),
    (0, "Fore-Red-Port-MIB", "redPortModule"),
    (0, "Fore-Red-Port-MIB", "redPortPort"),
)
if mibBuilder.loadTexts:
    redPortConfEntry.setStatus("current")
_RedPortBoard_Type = Integer32
_RedPortBoard_Object = MibTableColumn
redPortBoard = _RedPortBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1, 1, 1),
    _RedPortBoard_Type()
)
redPortBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redPortBoard.setStatus("current")
_RedPortModule_Type = Integer32
_RedPortModule_Object = MibTableColumn
redPortModule = _RedPortModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1, 1, 2),
    _RedPortModule_Type()
)
redPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redPortModule.setStatus("current")
_RedPortPort_Type = Integer32
_RedPortPort_Object = MibTableColumn
redPortPort = _RedPortPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1, 1, 3),
    _RedPortPort_Type()
)
redPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redPortPort.setStatus("current")


class _RedPortPendingAdminMode_Type(Integer32):
    """Custom type redPortPendingAdminMode based on Integer32"""
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
        *(("none", 4),
          ("protection", 2),
          ("unprotected", 3),
          ("working", 1))
    )


_RedPortPendingAdminMode_Type.__name__ = "Integer32"
_RedPortPendingAdminMode_Object = MibTableColumn
redPortPendingAdminMode = _RedPortPendingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1, 1, 4),
    _RedPortPendingAdminMode_Type()
)
redPortPendingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redPortPendingAdminMode.setStatus("current")


class _RedPortPendingCommitState_Type(Integer32):
    """Custom type redPortPendingCommitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RedPortPendingCommitState_Type.__name__ = "Integer32"
_RedPortPendingCommitState_Object = MibTableColumn
redPortPendingCommitState = _RedPortPendingCommitState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1, 1, 5),
    _RedPortPendingCommitState_Type()
)
redPortPendingCommitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redPortPendingCommitState.setStatus("current")


class _RedPortAdminMode_Type(Integer32):
    """Custom type redPortAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protection", 2),
          ("unprotected", 3),
          ("working", 1))
    )


_RedPortAdminMode_Type.__name__ = "Integer32"
_RedPortAdminMode_Object = MibTableColumn
redPortAdminMode = _RedPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1, 1, 6),
    _RedPortAdminMode_Type()
)
redPortAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redPortAdminMode.setStatus("current")


class _RedPortOperState_Type(Integer32):
    """Custom type redPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("loopbackoff", 5),
          ("loopbackon", 4),
          ("standby", 2),
          ("unprotected", 3))
    )


_RedPortOperState_Type.__name__ = "Integer32"
_RedPortOperState_Object = MibTableColumn
redPortOperState = _RedPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 1, 1, 7),
    _RedPortOperState_Type()
)
redPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redPortOperState.setStatus("current")


class _RedPortCommit_Type(Integer32):
    """Custom type redPortCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_RedPortCommit_Type.__name__ = "Integer32"
_RedPortCommit_Object = MibScalar
redPortCommit = _RedPortCommit_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 17, 2),
    _RedPortCommit_Type()
)
redPortCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redPortCommit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Red-Port-MIB",
    **{"redPortConfModule": redPortConfModule,
       "redPortConfTable": redPortConfTable,
       "redPortConfEntry": redPortConfEntry,
       "redPortBoard": redPortBoard,
       "redPortModule": redPortModule,
       "redPortPort": redPortPort,
       "redPortPendingAdminMode": redPortPendingAdminMode,
       "redPortPendingCommitState": redPortPendingCommitState,
       "redPortAdminMode": redPortAdminMode,
       "redPortOperState": redPortOperState,
       "redPortCommit": redPortCommit}
)
