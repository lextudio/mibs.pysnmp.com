# SNMP MIB module (ASCEND-MULTI-SHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MULTI-SHELF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:38 2024
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

(multiShelf,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "multiShelf")

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

_MyShelfNumber_Type = Integer32
_MyShelfNumber_Object = MibScalar
myShelfNumber = _MyShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 1),
    _MyShelfNumber_Type()
)
myShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myShelfNumber.setStatus("mandatory")


class _MyShelfOperation_Type(Integer32):
    """Custom type myShelfOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 3),
          ("other", 1),
          ("slave", 2))
    )


_MyShelfOperation_Type.__name__ = "Integer32"
_MyShelfOperation_Object = MibScalar
myShelfOperation = _MyShelfOperation_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 2),
    _MyShelfOperation_Type()
)
myShelfOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myShelfOperation.setStatus("mandatory")
_MasterShelfNumber_Type = Integer32
_MasterShelfNumber_Object = MibScalar
masterShelfNumber = _MasterShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 3),
    _MasterShelfNumber_Type()
)
masterShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterShelfNumber.setStatus("mandatory")
_MultiShelfTableSize_Type = Integer32
_MultiShelfTableSize_Object = MibScalar
multiShelfTableSize = _MultiShelfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 4),
    _MultiShelfTableSize_Type()
)
multiShelfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfTableSize.setStatus("mandatory")
_MultiShelfTable_Object = MibTable
multiShelfTable = _MultiShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5)
)
if mibBuilder.loadTexts:
    multiShelfTable.setStatus("mandatory")
_MultiShelfEntry_Object = MibTableRow
multiShelfEntry = _MultiShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1)
)
multiShelfEntry.setIndexNames(
    (0, "ASCEND-MULTI-SHELF-MIB", "multiShelfIndex"),
)
if mibBuilder.loadTexts:
    multiShelfEntry.setStatus("mandatory")
_MultiShelfIndex_Type = Integer32
_MultiShelfIndex_Object = MibTableColumn
multiShelfIndex = _MultiShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 1),
    _MultiShelfIndex_Type()
)
multiShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfIndex.setStatus("mandatory")


class _MultiShelfState_Type(Integer32):
    """Custom type multiShelfState based on Integer32"""
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
        *(("idle", 1),
          ("inComing", 3),
          ("outGoing", 2),
          ("up", 4))
    )


_MultiShelfState_Type.__name__ = "Integer32"
_MultiShelfState_Object = MibTableColumn
multiShelfState = _MultiShelfState_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 2),
    _MultiShelfState_Type()
)
multiShelfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfState.setStatus("mandatory")
_MultiShelfResentFrames_Type = Counter32
_MultiShelfResentFrames_Object = MibTableColumn
multiShelfResentFrames = _MultiShelfResentFrames_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 3),
    _MultiShelfResentFrames_Type()
)
multiShelfResentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfResentFrames.setStatus("mandatory")
_MultiShelfNLinkUp_Type = Counter32
_MultiShelfNLinkUp_Object = MibTableColumn
multiShelfNLinkUp = _MultiShelfNLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 4),
    _MultiShelfNLinkUp_Type()
)
multiShelfNLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfNLinkUp.setStatus("mandatory")
_MultiShelfTxQs_Type = Integer32
_MultiShelfTxQs_Object = MibTableColumn
multiShelfTxQs = _MultiShelfTxQs_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 5),
    _MultiShelfTxQs_Type()
)
multiShelfTxQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfTxQs.setStatus("mandatory")
_MultiShelfTxSeq_Type = Integer32
_MultiShelfTxSeq_Object = MibTableColumn
multiShelfTxSeq = _MultiShelfTxSeq_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 6),
    _MultiShelfTxSeq_Type()
)
multiShelfTxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfTxSeq.setStatus("mandatory")
_MultiShelfRxSeq_Type = Integer32
_MultiShelfRxSeq_Object = MibTableColumn
multiShelfRxSeq = _MultiShelfRxSeq_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 7),
    _MultiShelfRxSeq_Type()
)
multiShelfRxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfRxSeq.setStatus("mandatory")
_MultiShelfTimerValue_Type = Integer32
_MultiShelfTimerValue_Object = MibTableColumn
multiShelfTimerValue = _MultiShelfTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 8),
    _MultiShelfTimerValue_Type()
)
multiShelfTimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiShelfTimerValue.setStatus("mandatory")


class _MultiShelfStateTrapState_Type(Integer32):
    """Custom type multiShelfStateTrapState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MultiShelfStateTrapState_Type.__name__ = "Integer32"
_MultiShelfStateTrapState_Object = MibScalar
multiShelfStateTrapState = _MultiShelfStateTrapState_Object(
    (1, 3, 6, 1, 4, 1, 529, 19, 6),
    _MultiShelfStateTrapState_Type()
)
multiShelfStateTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiShelfStateTrapState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MULTI-SHELF-MIB",
    **{"myShelfNumber": myShelfNumber,
       "myShelfOperation": myShelfOperation,
       "masterShelfNumber": masterShelfNumber,
       "multiShelfTableSize": multiShelfTableSize,
       "multiShelfTable": multiShelfTable,
       "multiShelfEntry": multiShelfEntry,
       "multiShelfIndex": multiShelfIndex,
       "multiShelfState": multiShelfState,
       "multiShelfResentFrames": multiShelfResentFrames,
       "multiShelfNLinkUp": multiShelfNLinkUp,
       "multiShelfTxQs": multiShelfTxQs,
       "multiShelfTxSeq": multiShelfTxSeq,
       "multiShelfRxSeq": multiShelfRxSeq,
       "multiShelfTimerValue": multiShelfTimerValue,
       "multiShelfStateTrapState": multiShelfStateTrapState}
)
