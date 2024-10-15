# SNMP MIB module (ASCEND-MIBCLTMACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBCLTMACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:21 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibcltmAccess_ObjectIdentity = ObjectIdentity
mibcltmAccess = _MibcltmAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 67)
)
_MibcltmAccessTable_Object = MibTable
mibcltmAccessTable = _MibcltmAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1)
)
if mibBuilder.loadTexts:
    mibcltmAccessTable.setStatus("mandatory")
_MibcltmAccessEntry_Object = MibTableRow
mibcltmAccessEntry = _MibcltmAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1)
)
mibcltmAccessEntry.setIndexNames(
    (0, "ASCEND-MIBCLTMACCESS-MIB", "cltmAccess-Index-o"),
)
if mibBuilder.loadTexts:
    mibcltmAccessEntry.setStatus("mandatory")
_CltmAccess_Index_o_Type = Integer32
_CltmAccess_Index_o_Object = MibScalar
cltmAccess_Index_o = _CltmAccess_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 1),
    _CltmAccess_Index_o_Type()
)
cltmAccess_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmAccess_Index_o.setStatus("mandatory")


class _CltmAccess_CltmSlot_Type(Integer32):
    """Custom type cltmAccess_CltmSlot based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("anySlot", 1),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot2", 3),
          ("slot3", 4),
          ("slot4", 5),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8))
    )


_CltmAccess_CltmSlot_Type.__name__ = "Integer32"
_CltmAccess_CltmSlot_Object = MibScalar
cltmAccess_CltmSlot = _CltmAccess_CltmSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 2),
    _CltmAccess_CltmSlot_Type()
)
cltmAccess_CltmSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmAccess_CltmSlot.setStatus("mandatory")


class _CltmAccess_AccessSlot_Type(Integer32):
    """Custom type cltmAccess_AccessSlot based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("anySlot", 1),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot2", 3),
          ("slot3", 4),
          ("slot4", 5),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8))
    )


_CltmAccess_AccessSlot_Type.__name__ = "Integer32"
_CltmAccess_AccessSlot_Object = MibScalar
cltmAccess_AccessSlot = _CltmAccess_AccessSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 3),
    _CltmAccess_AccessSlot_Type()
)
cltmAccess_AccessSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmAccess_AccessSlot.setStatus("mandatory")
_CltmAccess_AccessPort_Type = Integer32
_CltmAccess_AccessPort_Object = MibScalar
cltmAccess_AccessPort = _CltmAccess_AccessPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 4),
    _CltmAccess_AccessPort_Type()
)
cltmAccess_AccessPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmAccess_AccessPort.setStatus("mandatory")


class _CltmAccess_AccessMode_Type(Integer32):
    """Custom type cltmAccess_AccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 2),
          ("lookingOut", 1))
    )


_CltmAccess_AccessMode_Type.__name__ = "Integer32"
_CltmAccess_AccessMode_Object = MibScalar
cltmAccess_AccessMode = _CltmAccess_AccessMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 5),
    _CltmAccess_AccessMode_Type()
)
cltmAccess_AccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmAccess_AccessMode.setStatus("mandatory")


class _CltmAccess_AccessTerminal_Type(Integer32):
    """Custom type cltmAccess_AccessTerminal based on Integer32"""
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
        *(("auxiliaryTesterTerminal", 3),
          ("externalLoop", 4),
          ("externalTesterTerminal", 2),
          ("internalTesterTerminal", 1))
    )


_CltmAccess_AccessTerminal_Type.__name__ = "Integer32"
_CltmAccess_AccessTerminal_Object = MibScalar
cltmAccess_AccessTerminal = _CltmAccess_AccessTerminal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 6),
    _CltmAccess_AccessTerminal_Type()
)
cltmAccess_AccessTerminal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmAccess_AccessTerminal.setStatus("mandatory")


class _CltmAccess_ActivateAccess_Type(Integer32):
    """Custom type cltmAccess_ActivateAccess based on Integer32"""
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


_CltmAccess_ActivateAccess_Type.__name__ = "Integer32"
_CltmAccess_ActivateAccess_Object = MibScalar
cltmAccess_ActivateAccess = _CltmAccess_ActivateAccess_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 7),
    _CltmAccess_ActivateAccess_Type()
)
cltmAccess_ActivateAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmAccess_ActivateAccess.setStatus("mandatory")


class _CltmAccess_AccessResult_Type(Integer32):
    """Custom type cltmAccess_AccessResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessActivated", 2),
          ("idle", 1),
          ("resourceBusy", 3))
    )


_CltmAccess_AccessResult_Type.__name__ = "Integer32"
_CltmAccess_AccessResult_Object = MibScalar
cltmAccess_AccessResult = _CltmAccess_AccessResult_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 8),
    _CltmAccess_AccessResult_Type()
)
cltmAccess_AccessResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmAccess_AccessResult.setStatus("mandatory")


class _CltmAccess_Action_o_Type(Integer32):
    """Custom type cltmAccess_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_CltmAccess_Action_o_Type.__name__ = "Integer32"
_CltmAccess_Action_o_Object = MibScalar
cltmAccess_Action_o = _CltmAccess_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 9),
    _CltmAccess_Action_o_Type()
)
cltmAccess_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmAccess_Action_o.setStatus("mandatory")
_CltmAccess_AccessLoop_Type = Integer32
_CltmAccess_AccessLoop_Object = MibScalar
cltmAccess_AccessLoop = _CltmAccess_AccessLoop_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 67, 1, 1, 10),
    _CltmAccess_AccessLoop_Type()
)
cltmAccess_AccessLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmAccess_AccessLoop.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBCLTMACCESS-MIB",
    **{"DisplayString": DisplayString,
       "mibcltmAccess": mibcltmAccess,
       "mibcltmAccessTable": mibcltmAccessTable,
       "mibcltmAccessEntry": mibcltmAccessEntry,
       "cltmAccess-Index-o": cltmAccess_Index_o,
       "cltmAccess-CltmSlot": cltmAccess_CltmSlot,
       "cltmAccess-AccessSlot": cltmAccess_AccessSlot,
       "cltmAccess-AccessPort": cltmAccess_AccessPort,
       "cltmAccess-AccessMode": cltmAccess_AccessMode,
       "cltmAccess-AccessTerminal": cltmAccess_AccessTerminal,
       "cltmAccess-ActivateAccess": cltmAccess_ActivateAccess,
       "cltmAccess-AccessResult": cltmAccess_AccessResult,
       "cltmAccess-Action-o": cltmAccess_Action_o,
       "cltmAccess-AccessLoop": cltmAccess_AccessLoop}
)
