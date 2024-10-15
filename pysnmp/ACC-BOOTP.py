# SNMP MIB module (ACC-BOOTP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-BOOTP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:55 2024
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

_AccBootp_ObjectIdentity = ObjectIdentity
accBootp = _AccBootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29)
)
_AccBootServerOld_ObjectIdentity = ObjectIdentity
accBootServerOld = _AccBootServerOld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 1)
)
_AccBootpServerOld_Type = IpAddress
_AccBootpServerOld_Object = MibScalar
accBootpServerOld = _AccBootpServerOld_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 1, 1),
    _AccBootpServerOld_Type()
)
accBootpServerOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootpServerOld.setStatus("mandatory")


class _AccBootMode_Type(Integer32):
    """Custom type accBootMode based on Integer32"""
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
        *(("automatic", 1),
          ("default", 4),
          ("forced", 2),
          ("off", 3))
    )


_AccBootMode_Type.__name__ = "Integer32"
_AccBootMode_Object = MibScalar
accBootMode = _AccBootMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 2),
    _AccBootMode_Type()
)
accBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootMode.setStatus("mandatory")


class _AccBootState_Type(Integer32):
    """Custom type accBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("complete", 6),
          ("configuring", 5),
          ("disabled", 2),
          ("failed", 7),
          ("initial", 1),
          ("requesting", 3),
          ("waiting", 4))
    )


_AccBootState_Type.__name__ = "Integer32"
_AccBootState_Object = MibScalar
accBootState = _AccBootState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 3),
    _AccBootState_Type()
)
accBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootState.setStatus("mandatory")
_AccBootyiaddr_Type = IpAddress
_AccBootyiaddr_Object = MibScalar
accBootyiaddr = _AccBootyiaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 4),
    _AccBootyiaddr_Type()
)
accBootyiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootyiaddr.setStatus("mandatory")
_AccBootsiaddr_Type = IpAddress
_AccBootsiaddr_Object = MibScalar
accBootsiaddr = _AccBootsiaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 5),
    _AccBootsiaddr_Type()
)
accBootsiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootsiaddr.setStatus("mandatory")
_AccBootsname_Type = DisplayString
_AccBootsname_Object = MibScalar
accBootsname = _AccBootsname_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 6),
    _AccBootsname_Type()
)
accBootsname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootsname.setStatus("mandatory")
_AccBootgiaddr_Type = IpAddress
_AccBootgiaddr_Object = MibScalar
accBootgiaddr = _AccBootgiaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 7),
    _AccBootgiaddr_Type()
)
accBootgiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootgiaddr.setStatus("deprecated")
_AccBootfile_Type = DisplayString
_AccBootfile_Object = MibScalar
accBootfile = _AccBootfile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 8),
    _AccBootfile_Type()
)
accBootfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootfile.setStatus("mandatory")
_AccBootInterface_Type = Integer32
_AccBootInterface_Object = MibScalar
accBootInterface = _AccBootInterface_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 9),
    _AccBootInterface_Type()
)
accBootInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootInterface.setStatus("mandatory")
_AccBootSentRequests_Type = Counter32
_AccBootSentRequests_Object = MibScalar
accBootSentRequests = _AccBootSentRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 10),
    _AccBootSentRequests_Type()
)
accBootSentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootSentRequests.setStatus("mandatory")
_AccBootReceivedReplies_Type = Counter32
_AccBootReceivedReplies_Object = MibScalar
accBootReceivedReplies = _AccBootReceivedReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 11),
    _AccBootReceivedReplies_Type()
)
accBootReceivedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootReceivedReplies.setStatus("mandatory")
_AccBootDiscardedReplies_Type = Counter32
_AccBootDiscardedReplies_Object = MibScalar
accBootDiscardedReplies = _AccBootDiscardedReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 12),
    _AccBootDiscardedReplies_Type()
)
accBootDiscardedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootDiscardedReplies.setStatus("mandatory")
_AccBootServerTable_Object = MibTable
accBootServerTable = _AccBootServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 13)
)
if mibBuilder.loadTexts:
    accBootServerTable.setStatus("mandatory")
_AccBootServerEntry_Object = MibTableRow
accBootServerEntry = _AccBootServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 13, 1)
)
accBootServerEntry.setIndexNames(
    (0, "ACC-BOOTP", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    accBootServerEntry.setStatus("mandatory")
_AccBootServerIPAddr_Type = IpAddress
_AccBootServerIPAddr_Object = MibTableColumn
accBootServerIPAddr = _AccBootServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 13, 1, 1),
    _AccBootServerIPAddr_Type()
)
accBootServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBootServerIPAddr.setStatus("mandatory")
_PysmiFakeCol1_Type = IpAddress
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 13, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_AccBootg1iaddr_Type = IpAddress
_AccBootg1iaddr_Object = MibScalar
accBootg1iaddr = _AccBootg1iaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 14),
    _AccBootg1iaddr_Type()
)
accBootg1iaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootg1iaddr.setStatus("mandatory")
_AccBootg2iaddr_Type = IpAddress
_AccBootg2iaddr_Object = MibScalar
accBootg2iaddr = _AccBootg2iaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 15),
    _AccBootg2iaddr_Type()
)
accBootg2iaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootg2iaddr.setStatus("mandatory")
_AccBootg3iaddr_Type = IpAddress
_AccBootg3iaddr_Object = MibScalar
accBootg3iaddr = _AccBootg3iaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 16),
    _AccBootg3iaddr_Type()
)
accBootg3iaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootg3iaddr.setStatus("mandatory")


class _AccBootpServerMode_Type(Integer32):
    """Custom type accBootpServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccBootpServerMode_Type.__name__ = "Integer32"
_AccBootpServerMode_Object = MibScalar
accBootpServerMode = _AccBootpServerMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 17),
    _AccBootpServerMode_Type()
)
accBootpServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBootpServerMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-BOOTP",
    **{"accBootp": accBootp,
       "accBootServerOld": accBootServerOld,
       "accBootpServerOld": accBootpServerOld,
       "accBootMode": accBootMode,
       "accBootState": accBootState,
       "accBootyiaddr": accBootyiaddr,
       "accBootsiaddr": accBootsiaddr,
       "accBootsname": accBootsname,
       "accBootgiaddr": accBootgiaddr,
       "accBootfile": accBootfile,
       "accBootInterface": accBootInterface,
       "accBootSentRequests": accBootSentRequests,
       "accBootReceivedReplies": accBootReceivedReplies,
       "accBootDiscardedReplies": accBootDiscardedReplies,
       "accBootServerTable": accBootServerTable,
       "accBootServerEntry": accBootServerEntry,
       "accBootServerIPAddr": accBootServerIPAddr,
       "pysmiFakeCol1": pysmiFakeCol1,
       "accBootg1iaddr": accBootg1iaddr,
       "accBootg2iaddr": accBootg2iaddr,
       "accBootg3iaddr": accBootg3iaddr,
       "accBootpServerMode": accBootpServerMode}
)
