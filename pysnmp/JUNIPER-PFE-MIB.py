# SNMP MIB module (JUNIPER-PFE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-PFE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:00 2024
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

(jnxPfeMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxPfeMibRoot")

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

jnxPfeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1)
)
jnxPfeMib.setRevisions(
        ("2014-11-14 00:00",
         "2014-03-12 00:00",
         "2011-09-09 00:00",
         "2010-02-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxPfeMemoryTypeEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("encap", 3),
          ("fw", 2),
          ("nh", 1))
    )



# MIB Managed Objects in the order of their OIDs

_JnxPfeNotification_ObjectIdentity = ObjectIdentity
jnxPfeNotification = _JnxPfeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1)
)
_PfeMemoryErrorsNotificationPrefix_ObjectIdentity = ObjectIdentity
pfeMemoryErrorsNotificationPrefix = _PfeMemoryErrorsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 0)
)
_JnxPfeNotifyGlTable_Object = MibTable
jnxPfeNotifyGlTable = _JnxPfeNotifyGlTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxPfeNotifyGlTable.setStatus("current")
_JnxPfeNotifyGlEntry_Object = MibTableRow
jnxPfeNotifyGlEntry = _JnxPfeNotifyGlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1)
)
jnxPfeNotifyGlEntry.setIndexNames(
    (0, "JUNIPER-PFE-MIB", "jnxPfeNotifyGlSlot"),
)
if mibBuilder.loadTexts:
    jnxPfeNotifyGlEntry.setStatus("current")


class _JnxPfeNotifyGlSlot_Type(Integer32):
    """Custom type jnxPfeNotifyGlSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxPfeNotifyGlSlot_Type.__name__ = "Integer32"
_JnxPfeNotifyGlSlot_Object = MibTableColumn
jnxPfeNotifyGlSlot = _JnxPfeNotifyGlSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 1),
    _JnxPfeNotifyGlSlot_Type()
)
jnxPfeNotifyGlSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlSlot.setStatus("current")
_JnxPfeNotifyGlParsed_Type = Counter32
_JnxPfeNotifyGlParsed_Object = MibTableColumn
jnxPfeNotifyGlParsed = _JnxPfeNotifyGlParsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 2),
    _JnxPfeNotifyGlParsed_Type()
)
jnxPfeNotifyGlParsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlParsed.setStatus("current")
_JnxPfeNotifyGlAged_Type = Counter32
_JnxPfeNotifyGlAged_Object = MibTableColumn
jnxPfeNotifyGlAged = _JnxPfeNotifyGlAged_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 3),
    _JnxPfeNotifyGlAged_Type()
)
jnxPfeNotifyGlAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlAged.setStatus("current")
_JnxPfeNotifyGlCorrupt_Type = Counter32
_JnxPfeNotifyGlCorrupt_Object = MibTableColumn
jnxPfeNotifyGlCorrupt = _JnxPfeNotifyGlCorrupt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 4),
    _JnxPfeNotifyGlCorrupt_Type()
)
jnxPfeNotifyGlCorrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlCorrupt.setStatus("current")
_JnxPfeNotifyGlIllegal_Type = Counter32
_JnxPfeNotifyGlIllegal_Object = MibTableColumn
jnxPfeNotifyGlIllegal = _JnxPfeNotifyGlIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 5),
    _JnxPfeNotifyGlIllegal_Type()
)
jnxPfeNotifyGlIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlIllegal.setStatus("current")
_JnxPfeNotifyGlSample_Type = Counter32
_JnxPfeNotifyGlSample_Object = MibTableColumn
jnxPfeNotifyGlSample = _JnxPfeNotifyGlSample_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 6),
    _JnxPfeNotifyGlSample_Type()
)
jnxPfeNotifyGlSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlSample.setStatus("current")
_JnxPfeNotifyGlGiants_Type = Counter32
_JnxPfeNotifyGlGiants_Object = MibTableColumn
jnxPfeNotifyGlGiants = _JnxPfeNotifyGlGiants_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 7),
    _JnxPfeNotifyGlGiants_Type()
)
jnxPfeNotifyGlGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlGiants.setStatus("current")
_JnxPfeNotifyGlTtlExceeded_Type = Counter32
_JnxPfeNotifyGlTtlExceeded_Object = MibTableColumn
jnxPfeNotifyGlTtlExceeded = _JnxPfeNotifyGlTtlExceeded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 8),
    _JnxPfeNotifyGlTtlExceeded_Type()
)
jnxPfeNotifyGlTtlExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlTtlExceeded.setStatus("current")
_JnxPfeNotifyGlTtlExcErrors_Type = Counter32
_JnxPfeNotifyGlTtlExcErrors_Object = MibTableColumn
jnxPfeNotifyGlTtlExcErrors = _JnxPfeNotifyGlTtlExcErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 9),
    _JnxPfeNotifyGlTtlExcErrors_Type()
)
jnxPfeNotifyGlTtlExcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlTtlExcErrors.setStatus("current")
_JnxPfeNotifyGlSvcOptAsp_Type = Counter32
_JnxPfeNotifyGlSvcOptAsp_Object = MibTableColumn
jnxPfeNotifyGlSvcOptAsp = _JnxPfeNotifyGlSvcOptAsp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 10),
    _JnxPfeNotifyGlSvcOptAsp_Type()
)
jnxPfeNotifyGlSvcOptAsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlSvcOptAsp.setStatus("current")
_JnxPfeNotifyGlSvcOptRe_Type = Counter32
_JnxPfeNotifyGlSvcOptRe_Object = MibTableColumn
jnxPfeNotifyGlSvcOptRe = _JnxPfeNotifyGlSvcOptRe_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 11),
    _JnxPfeNotifyGlSvcOptRe_Type()
)
jnxPfeNotifyGlSvcOptRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlSvcOptRe.setStatus("current")
_JnxPfeNotifyGlPostSvcOptOut_Type = Counter32
_JnxPfeNotifyGlPostSvcOptOut_Object = MibTableColumn
jnxPfeNotifyGlPostSvcOptOut = _JnxPfeNotifyGlPostSvcOptOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 12),
    _JnxPfeNotifyGlPostSvcOptOut_Type()
)
jnxPfeNotifyGlPostSvcOptOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlPostSvcOptOut.setStatus("current")
_JnxPfeNotifyGlOptTtlExp_Type = Counter32
_JnxPfeNotifyGlOptTtlExp_Object = MibTableColumn
jnxPfeNotifyGlOptTtlExp = _JnxPfeNotifyGlOptTtlExp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 13),
    _JnxPfeNotifyGlOptTtlExp_Type()
)
jnxPfeNotifyGlOptTtlExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlOptTtlExp.setStatus("current")
_JnxPfeNotifyGlDiscSample_Type = Counter32
_JnxPfeNotifyGlDiscSample_Object = MibTableColumn
jnxPfeNotifyGlDiscSample = _JnxPfeNotifyGlDiscSample_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 14),
    _JnxPfeNotifyGlDiscSample_Type()
)
jnxPfeNotifyGlDiscSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlDiscSample.setStatus("current")
_JnxPfeNotifyGlRateLimited_Type = Counter32
_JnxPfeNotifyGlRateLimited_Object = MibTableColumn
jnxPfeNotifyGlRateLimited = _JnxPfeNotifyGlRateLimited_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 15),
    _JnxPfeNotifyGlRateLimited_Type()
)
jnxPfeNotifyGlRateLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlRateLimited.setStatus("current")
_JnxPfeNotifyGlPktGetFails_Type = Counter32
_JnxPfeNotifyGlPktGetFails_Object = MibTableColumn
jnxPfeNotifyGlPktGetFails = _JnxPfeNotifyGlPktGetFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 16),
    _JnxPfeNotifyGlPktGetFails_Type()
)
jnxPfeNotifyGlPktGetFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlPktGetFails.setStatus("current")
_JnxPfeNotifyGlDmaFails_Type = Counter32
_JnxPfeNotifyGlDmaFails_Object = MibTableColumn
jnxPfeNotifyGlDmaFails = _JnxPfeNotifyGlDmaFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 17),
    _JnxPfeNotifyGlDmaFails_Type()
)
jnxPfeNotifyGlDmaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlDmaFails.setStatus("current")
_JnxPfeNotifyGlDmaTotals_Type = Counter32
_JnxPfeNotifyGlDmaTotals_Object = MibTableColumn
jnxPfeNotifyGlDmaTotals = _JnxPfeNotifyGlDmaTotals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 18),
    _JnxPfeNotifyGlDmaTotals_Type()
)
jnxPfeNotifyGlDmaTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlDmaTotals.setStatus("current")
_JnxPfeNotifyGlUnknowns_Type = Counter32
_JnxPfeNotifyGlUnknowns_Object = MibTableColumn
jnxPfeNotifyGlUnknowns = _JnxPfeNotifyGlUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 19),
    _JnxPfeNotifyGlUnknowns_Type()
)
jnxPfeNotifyGlUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlUnknowns.setStatus("current")
_JnxPfeNotifyGlParAccSec_Type = Counter32
_JnxPfeNotifyGlParAccSec_Object = MibTableColumn
jnxPfeNotifyGlParAccSec = _JnxPfeNotifyGlParAccSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 1, 1, 20),
    _JnxPfeNotifyGlParAccSec_Type()
)
jnxPfeNotifyGlParAccSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyGlParAccSec.setStatus("current")
_JnxPfeNotifyTypeTable_Object = MibTable
jnxPfeNotifyTypeTable = _JnxPfeNotifyTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxPfeNotifyTypeTable.setStatus("current")
_JnxPfeNotifyTypeEntry_Object = MibTableRow
jnxPfeNotifyTypeEntry = _JnxPfeNotifyTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 2, 1)
)
jnxPfeNotifyTypeEntry.setIndexNames(
    (0, "JUNIPER-PFE-MIB", "jnxPfeNotifyGlSlot"),
    (0, "JUNIPER-PFE-MIB", "jnxPfeNotifyTypeId"),
)
if mibBuilder.loadTexts:
    jnxPfeNotifyTypeEntry.setStatus("current")


class _JnxPfeNotifyTypeId_Type(Integer32):
    """Custom type jnxPfeNotifyTypeId based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("autoConfig", 13),
          ("cfdf", 9),
          ("discard", 5),
          ("dontFragment", 8),
          ("illegal", 1),
          ("nextHop", 4),
          ("option", 3),
          ("poison", 10),
          ("redirect", 7),
          ("reject", 14),
          ("sample", 6),
          ("specialMemPkt", 12),
          ("unclassified", 2),
          ("unknown", 11))
    )


_JnxPfeNotifyTypeId_Type.__name__ = "Integer32"
_JnxPfeNotifyTypeId_Object = MibTableColumn
jnxPfeNotifyTypeId = _JnxPfeNotifyTypeId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 2, 1, 1),
    _JnxPfeNotifyTypeId_Type()
)
jnxPfeNotifyTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPfeNotifyTypeId.setStatus("current")


class _JnxPfeNotifyTypeDescr_Type(DisplayString):
    """Custom type jnxPfeNotifyTypeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxPfeNotifyTypeDescr_Type.__name__ = "DisplayString"
_JnxPfeNotifyTypeDescr_Object = MibTableColumn
jnxPfeNotifyTypeDescr = _JnxPfeNotifyTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 2, 1, 2),
    _JnxPfeNotifyTypeDescr_Type()
)
jnxPfeNotifyTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyTypeDescr.setStatus("current")
_JnxPfeNotifyTypeParsed_Type = Counter32
_JnxPfeNotifyTypeParsed_Object = MibTableColumn
jnxPfeNotifyTypeParsed = _JnxPfeNotifyTypeParsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 2, 1, 3),
    _JnxPfeNotifyTypeParsed_Type()
)
jnxPfeNotifyTypeParsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyTypeParsed.setStatus("current")
_JnxPfeNotifyTypeInput_Type = Counter32
_JnxPfeNotifyTypeInput_Object = MibTableColumn
jnxPfeNotifyTypeInput = _JnxPfeNotifyTypeInput_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 2, 1, 4),
    _JnxPfeNotifyTypeInput_Type()
)
jnxPfeNotifyTypeInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyTypeInput.setStatus("current")
_JnxPfeNotifyTypeFailed_Type = Counter32
_JnxPfeNotifyTypeFailed_Object = MibTableColumn
jnxPfeNotifyTypeFailed = _JnxPfeNotifyTypeFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 2, 1, 5),
    _JnxPfeNotifyTypeFailed_Type()
)
jnxPfeNotifyTypeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyTypeFailed.setStatus("current")
_JnxPfeNotifyTypeIgnored_Type = Counter32
_JnxPfeNotifyTypeIgnored_Object = MibTableColumn
jnxPfeNotifyTypeIgnored = _JnxPfeNotifyTypeIgnored_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 2, 1, 6),
    _JnxPfeNotifyTypeIgnored_Type()
)
jnxPfeNotifyTypeIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeNotifyTypeIgnored.setStatus("current")
_JnxPfeMemoryErrorsTable_Object = MibTable
jnxPfeMemoryErrorsTable = _JnxPfeMemoryErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxPfeMemoryErrorsTable.setStatus("current")
_JnxPfeMemoryErrorsEntry_Object = MibTableRow
jnxPfeMemoryErrorsEntry = _JnxPfeMemoryErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 3, 1)
)
jnxPfeMemoryErrorsEntry.setIndexNames(
    (0, "JUNIPER-PFE-MIB", "jnxPfeFpcSlot"),
    (0, "JUNIPER-PFE-MIB", "jnxPfeSlot"),
)
if mibBuilder.loadTexts:
    jnxPfeMemoryErrorsEntry.setStatus("current")


class _JnxPfeFpcSlot_Type(Integer32):
    """Custom type jnxPfeFpcSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxPfeFpcSlot_Type.__name__ = "Integer32"
_JnxPfeFpcSlot_Object = MibTableColumn
jnxPfeFpcSlot = _JnxPfeFpcSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 3, 1, 1),
    _JnxPfeFpcSlot_Type()
)
jnxPfeFpcSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPfeFpcSlot.setStatus("current")


class _JnxPfeSlot_Type(Integer32):
    """Custom type jnxPfeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxPfeSlot_Type.__name__ = "Integer32"
_JnxPfeSlot_Object = MibTableColumn
jnxPfeSlot = _JnxPfeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 3, 1, 2),
    _JnxPfeSlot_Type()
)
jnxPfeSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPfeSlot.setStatus("current")
_JnxPfeParityErrors_Type = Counter64
_JnxPfeParityErrors_Object = MibTableColumn
jnxPfeParityErrors = _JnxPfeParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 3, 1, 3),
    _JnxPfeParityErrors_Type()
)
jnxPfeParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeParityErrors.setStatus("current")
_JnxPfeEccErrors_Type = Counter64
_JnxPfeEccErrors_Object = MibTableColumn
jnxPfeEccErrors = _JnxPfeEccErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 3, 1, 4),
    _JnxPfeEccErrors_Type()
)
jnxPfeEccErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeEccErrors.setStatus("current")
_JnxPfeMemory_ObjectIdentity = ObjectIdentity
jnxPfeMemory = _JnxPfeMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2)
)
_JnxPfeMemoryUkernTable_Object = MibTable
jnxPfeMemoryUkernTable = _JnxPfeMemoryUkernTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxPfeMemoryUkernTable.setStatus("current")
_JnxPfeMemoryUkernEntry_Object = MibTableRow
jnxPfeMemoryUkernEntry = _JnxPfeMemoryUkernEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 1, 1)
)
jnxPfeMemoryUkernEntry.setIndexNames(
    (0, "JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
)
if mibBuilder.loadTexts:
    jnxPfeMemoryUkernEntry.setStatus("current")


class _JnxPfeMemoryUkernFreePercent_Type(Unsigned32):
    """Custom type jnxPfeMemoryUkernFreePercent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxPfeMemoryUkernFreePercent_Type.__name__ = "Unsigned32"
_JnxPfeMemoryUkernFreePercent_Object = MibTableColumn
jnxPfeMemoryUkernFreePercent = _JnxPfeMemoryUkernFreePercent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 1, 1, 2),
    _JnxPfeMemoryUkernFreePercent_Type()
)
jnxPfeMemoryUkernFreePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeMemoryUkernFreePercent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPfeMemoryUkernFreePercent.setUnits("percent")
_JnxPfeMemoryForwardingTable_Object = MibTable
jnxPfeMemoryForwardingTable = _JnxPfeMemoryForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxPfeMemoryForwardingTable.setStatus("current")
_JnxPfeMemoryForwardingEntry_Object = MibTableRow
jnxPfeMemoryForwardingEntry = _JnxPfeMemoryForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 2, 1)
)
jnxPfeMemoryForwardingEntry.setIndexNames(
    (0, "JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
    (0, "JUNIPER-PFE-MIB", "jnxPfeMemoryForwardingChipSlot"),
    (0, "JUNIPER-PFE-MIB", "jnxPfeMemoryType"),
)
if mibBuilder.loadTexts:
    jnxPfeMemoryForwardingEntry.setStatus("current")


class _JnxPfeMemoryForwardingChipSlot_Type(Integer32):
    """Custom type jnxPfeMemoryForwardingChipSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_JnxPfeMemoryForwardingChipSlot_Type.__name__ = "Integer32"
_JnxPfeMemoryForwardingChipSlot_Object = MibTableColumn
jnxPfeMemoryForwardingChipSlot = _JnxPfeMemoryForwardingChipSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 2, 1, 1),
    _JnxPfeMemoryForwardingChipSlot_Type()
)
jnxPfeMemoryForwardingChipSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPfeMemoryForwardingChipSlot.setStatus("current")
_JnxPfeMemoryType_Type = JnxPfeMemoryTypeEnum
_JnxPfeMemoryType_Object = MibTableColumn
jnxPfeMemoryType = _JnxPfeMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 2, 1, 2),
    _JnxPfeMemoryType_Type()
)
jnxPfeMemoryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPfeMemoryType.setStatus("current")


class _JnxPfeMemoryForwardingPercentFree_Type(Unsigned32):
    """Custom type jnxPfeMemoryForwardingPercentFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxPfeMemoryForwardingPercentFree_Type.__name__ = "Unsigned32"
_JnxPfeMemoryForwardingPercentFree_Object = MibTableColumn
jnxPfeMemoryForwardingPercentFree = _JnxPfeMemoryForwardingPercentFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 2, 1, 3),
    _JnxPfeMemoryForwardingPercentFree_Type()
)
jnxPfeMemoryForwardingPercentFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPfeMemoryForwardingPercentFree.setStatus("current")
if mibBuilder.loadTexts:
    jnxPfeMemoryForwardingPercentFree.setUnits("percent")
_JnxPfeMemoryTrapVars_ObjectIdentity = ObjectIdentity
jnxPfeMemoryTrapVars = _JnxPfeMemoryTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxPfeMemoryTrapVars.setStatus("current")


class _JnxPfeGlSlot_Type(Unsigned32):
    """Custom type jnxPfeGlSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxPfeGlSlot_Type.__name__ = "Unsigned32"
_JnxPfeGlSlot_Object = MibTableColumn
jnxPfeGlSlot = _JnxPfeGlSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 3, 1),
    _JnxPfeGlSlot_Type()
)
jnxPfeGlSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPfeGlSlot.setStatus("current")


class _JnxPfeInstanceNumber_Type(Integer32):
    """Custom type jnxPfeInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_JnxPfeInstanceNumber_Type.__name__ = "Integer32"
_JnxPfeInstanceNumber_Object = MibScalar
jnxPfeInstanceNumber = _JnxPfeInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 3, 2),
    _JnxPfeInstanceNumber_Type()
)
jnxPfeInstanceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPfeInstanceNumber.setStatus("current")


class _JnxPfeMemoryThreshold_Type(Unsigned32):
    """Custom type jnxPfeMemoryThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxPfeMemoryThreshold_Type.__name__ = "Unsigned32"
_JnxPfeMemoryThreshold_Object = MibScalar
jnxPfeMemoryThreshold = _JnxPfeMemoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 3, 3),
    _JnxPfeMemoryThreshold_Type()
)
jnxPfeMemoryThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPfeMemoryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPfeMemoryThreshold.setUnits("percent")
_JnxPfeMemoryNotificationsPrefix_ObjectIdentity = ObjectIdentity
jnxPfeMemoryNotificationsPrefix = _JnxPfeMemoryNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4)
)
_JnxPfeMemoryNotifications_ObjectIdentity = ObjectIdentity
jnxPfeMemoryNotifications = _JnxPfeMemoryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0)
)

# Managed Objects groups


# Notification objects

pfeMemoryErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 1, 0, 1)
)
pfeMemoryErrors.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeParityErrors"),
        ("JUNIPER-PFE-MIB", "jnxPfeEccErrors"))
)
if mibBuilder.loadTexts:
    pfeMemoryErrors.setStatus(
        "current"
    )

jnxPfeHeapMemoryThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0, 1)
)
jnxPfeHeapMemoryThresholdExceeded.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
        ("JUNIPER-PFE-MIB", "jnxPfeMemoryThreshold"))
)
if mibBuilder.loadTexts:
    jnxPfeHeapMemoryThresholdExceeded.setStatus(
        "current"
    )

jnxPfeHeapMemoryThresholdAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0, 2)
)
jnxPfeHeapMemoryThresholdAbated.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
        ("JUNIPER-PFE-MIB", "jnxPfeMemoryThreshold"))
)
if mibBuilder.loadTexts:
    jnxPfeHeapMemoryThresholdAbated.setStatus(
        "current"
    )

jnxPfeNextHopMemoryThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0, 3)
)
jnxPfeNextHopMemoryThresholdExceeded.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
        ("JUNIPER-PFE-MIB", "jnxPfeInstanceNumber"),
        ("JUNIPER-PFE-MIB", "jnxPfeMemoryThreshold"))
)
if mibBuilder.loadTexts:
    jnxPfeNextHopMemoryThresholdExceeded.setStatus(
        "current"
    )

jnxPfeNextHopMemoryThresholdAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0, 4)
)
jnxPfeNextHopMemoryThresholdAbated.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
        ("JUNIPER-PFE-MIB", "jnxPfeInstanceNumber"),
        ("JUNIPER-PFE-MIB", "jnxPfeMemoryThreshold"))
)
if mibBuilder.loadTexts:
    jnxPfeNextHopMemoryThresholdAbated.setStatus(
        "current"
    )

jnxPfeFilterMemoryThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0, 5)
)
jnxPfeFilterMemoryThresholdExceeded.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
        ("JUNIPER-PFE-MIB", "jnxPfeInstanceNumber"),
        ("JUNIPER-PFE-MIB", "jnxPfeMemoryThreshold"))
)
if mibBuilder.loadTexts:
    jnxPfeFilterMemoryThresholdExceeded.setStatus(
        "current"
    )

jnxPfeFilterMemoryThresholdAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0, 6)
)
jnxPfeFilterMemoryThresholdAbated.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
        ("JUNIPER-PFE-MIB", "jnxPfeInstanceNumber"),
        ("JUNIPER-PFE-MIB", "jnxPfeMemoryThreshold"))
)
if mibBuilder.loadTexts:
    jnxPfeFilterMemoryThresholdAbated.setStatus(
        "current"
    )

jnxPfeEncapMemoryThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0, 7)
)
jnxPfeEncapMemoryThresholdExceeded.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
        ("JUNIPER-PFE-MIB", "jnxPfeInstanceNumber"),
        ("JUNIPER-PFE-MIB", "jnxPfeMemoryThreshold"))
)
if mibBuilder.loadTexts:
    jnxPfeEncapMemoryThresholdExceeded.setStatus(
        "current"
    )

jnxPfeEncapMemoryThresholdAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44, 1, 2, 4, 0, 8)
)
jnxPfeEncapMemoryThresholdAbated.setObjects(
      *(("JUNIPER-PFE-MIB", "jnxPfeGlSlot"),
        ("JUNIPER-PFE-MIB", "jnxPfeInstanceNumber"),
        ("JUNIPER-PFE-MIB", "jnxPfeMemoryThreshold"))
)
if mibBuilder.loadTexts:
    jnxPfeEncapMemoryThresholdAbated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-PFE-MIB",
    **{"JnxPfeMemoryTypeEnum": JnxPfeMemoryTypeEnum,
       "jnxPfeMib": jnxPfeMib,
       "jnxPfeNotification": jnxPfeNotification,
       "pfeMemoryErrorsNotificationPrefix": pfeMemoryErrorsNotificationPrefix,
       "pfeMemoryErrors": pfeMemoryErrors,
       "jnxPfeNotifyGlTable": jnxPfeNotifyGlTable,
       "jnxPfeNotifyGlEntry": jnxPfeNotifyGlEntry,
       "jnxPfeNotifyGlSlot": jnxPfeNotifyGlSlot,
       "jnxPfeNotifyGlParsed": jnxPfeNotifyGlParsed,
       "jnxPfeNotifyGlAged": jnxPfeNotifyGlAged,
       "jnxPfeNotifyGlCorrupt": jnxPfeNotifyGlCorrupt,
       "jnxPfeNotifyGlIllegal": jnxPfeNotifyGlIllegal,
       "jnxPfeNotifyGlSample": jnxPfeNotifyGlSample,
       "jnxPfeNotifyGlGiants": jnxPfeNotifyGlGiants,
       "jnxPfeNotifyGlTtlExceeded": jnxPfeNotifyGlTtlExceeded,
       "jnxPfeNotifyGlTtlExcErrors": jnxPfeNotifyGlTtlExcErrors,
       "jnxPfeNotifyGlSvcOptAsp": jnxPfeNotifyGlSvcOptAsp,
       "jnxPfeNotifyGlSvcOptRe": jnxPfeNotifyGlSvcOptRe,
       "jnxPfeNotifyGlPostSvcOptOut": jnxPfeNotifyGlPostSvcOptOut,
       "jnxPfeNotifyGlOptTtlExp": jnxPfeNotifyGlOptTtlExp,
       "jnxPfeNotifyGlDiscSample": jnxPfeNotifyGlDiscSample,
       "jnxPfeNotifyGlRateLimited": jnxPfeNotifyGlRateLimited,
       "jnxPfeNotifyGlPktGetFails": jnxPfeNotifyGlPktGetFails,
       "jnxPfeNotifyGlDmaFails": jnxPfeNotifyGlDmaFails,
       "jnxPfeNotifyGlDmaTotals": jnxPfeNotifyGlDmaTotals,
       "jnxPfeNotifyGlUnknowns": jnxPfeNotifyGlUnknowns,
       "jnxPfeNotifyGlParAccSec": jnxPfeNotifyGlParAccSec,
       "jnxPfeNotifyTypeTable": jnxPfeNotifyTypeTable,
       "jnxPfeNotifyTypeEntry": jnxPfeNotifyTypeEntry,
       "jnxPfeNotifyTypeId": jnxPfeNotifyTypeId,
       "jnxPfeNotifyTypeDescr": jnxPfeNotifyTypeDescr,
       "jnxPfeNotifyTypeParsed": jnxPfeNotifyTypeParsed,
       "jnxPfeNotifyTypeInput": jnxPfeNotifyTypeInput,
       "jnxPfeNotifyTypeFailed": jnxPfeNotifyTypeFailed,
       "jnxPfeNotifyTypeIgnored": jnxPfeNotifyTypeIgnored,
       "jnxPfeMemoryErrorsTable": jnxPfeMemoryErrorsTable,
       "jnxPfeMemoryErrorsEntry": jnxPfeMemoryErrorsEntry,
       "jnxPfeFpcSlot": jnxPfeFpcSlot,
       "jnxPfeSlot": jnxPfeSlot,
       "jnxPfeParityErrors": jnxPfeParityErrors,
       "jnxPfeEccErrors": jnxPfeEccErrors,
       "jnxPfeMemory": jnxPfeMemory,
       "jnxPfeMemoryUkernTable": jnxPfeMemoryUkernTable,
       "jnxPfeMemoryUkernEntry": jnxPfeMemoryUkernEntry,
       "jnxPfeMemoryUkernFreePercent": jnxPfeMemoryUkernFreePercent,
       "jnxPfeMemoryForwardingTable": jnxPfeMemoryForwardingTable,
       "jnxPfeMemoryForwardingEntry": jnxPfeMemoryForwardingEntry,
       "jnxPfeMemoryForwardingChipSlot": jnxPfeMemoryForwardingChipSlot,
       "jnxPfeMemoryType": jnxPfeMemoryType,
       "jnxPfeMemoryForwardingPercentFree": jnxPfeMemoryForwardingPercentFree,
       "jnxPfeMemoryTrapVars": jnxPfeMemoryTrapVars,
       "jnxPfeGlSlot": jnxPfeGlSlot,
       "jnxPfeInstanceNumber": jnxPfeInstanceNumber,
       "jnxPfeMemoryThreshold": jnxPfeMemoryThreshold,
       "jnxPfeMemoryNotificationsPrefix": jnxPfeMemoryNotificationsPrefix,
       "jnxPfeMemoryNotifications": jnxPfeMemoryNotifications,
       "jnxPfeHeapMemoryThresholdExceeded": jnxPfeHeapMemoryThresholdExceeded,
       "jnxPfeHeapMemoryThresholdAbated": jnxPfeHeapMemoryThresholdAbated,
       "jnxPfeNextHopMemoryThresholdExceeded": jnxPfeNextHopMemoryThresholdExceeded,
       "jnxPfeNextHopMemoryThresholdAbated": jnxPfeNextHopMemoryThresholdAbated,
       "jnxPfeFilterMemoryThresholdExceeded": jnxPfeFilterMemoryThresholdExceeded,
       "jnxPfeFilterMemoryThresholdAbated": jnxPfeFilterMemoryThresholdAbated,
       "jnxPfeEncapMemoryThresholdExceeded": jnxPfeEncapMemoryThresholdExceeded,
       "jnxPfeEncapMemoryThresholdAbated": jnxPfeEncapMemoryThresholdAbated}
)
