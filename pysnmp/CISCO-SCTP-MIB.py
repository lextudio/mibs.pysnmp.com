# SNMP MIB module (CISCO-SCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SCTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:00 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ceSctpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 74)
)
ceSctpMIB.setRevisions(
        ("2005-12-21 00:00",
         "2001-06-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InetAddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv6", 2),
          ("unknown", 0))
    )



class InetAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CeSctpObjects_ObjectIdentity = ObjectIdentity
ceSctpObjects = _CeSctpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1)
)
_CeSctpScalars_ObjectIdentity = ObjectIdentity
ceSctpScalars = _CeSctpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1)
)


class _CeSctpRtoAlgorithm_Type(Integer32):
    """Custom type ceSctpRtoAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("vanj", 2))
    )


_CeSctpRtoAlgorithm_Type.__name__ = "Integer32"
_CeSctpRtoAlgorithm_Object = MibScalar
ceSctpRtoAlgorithm = _CeSctpRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 1),
    _CeSctpRtoAlgorithm_Type()
)
ceSctpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpRtoAlgorithm.setStatus("current")


class _CeSctpMaxAssociations_Type(Unsigned32):
    """Custom type ceSctpMaxAssociations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CeSctpMaxAssociations_Type.__name__ = "Unsigned32"
_CeSctpMaxAssociations_Object = MibScalar
ceSctpMaxAssociations = _CeSctpMaxAssociations_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 2),
    _CeSctpMaxAssociations_Type()
)
ceSctpMaxAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpMaxAssociations.setStatus("current")
_CeSctpCurrEstab_Type = Counter32
_CeSctpCurrEstab_Object = MibScalar
ceSctpCurrEstab = _CeSctpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 3),
    _CeSctpCurrEstab_Type()
)
ceSctpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpCurrEstab.setStatus("current")
_CeSctpActiveEstab_Type = Counter32
_CeSctpActiveEstab_Object = MibScalar
ceSctpActiveEstab = _CeSctpActiveEstab_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 4),
    _CeSctpActiveEstab_Type()
)
ceSctpActiveEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpActiveEstab.setStatus("current")
_CeSctpPassiveEstab_Type = Counter32
_CeSctpPassiveEstab_Object = MibScalar
ceSctpPassiveEstab = _CeSctpPassiveEstab_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 5),
    _CeSctpPassiveEstab_Type()
)
ceSctpPassiveEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpPassiveEstab.setStatus("current")
_CeSctpAborted_Type = Counter32
_CeSctpAborted_Object = MibScalar
ceSctpAborted = _CeSctpAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 6),
    _CeSctpAborted_Type()
)
ceSctpAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAborted.setStatus("current")
_CeSctpShutdowns_Type = Counter32
_CeSctpShutdowns_Object = MibScalar
ceSctpShutdowns = _CeSctpShutdowns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 7),
    _CeSctpShutdowns_Type()
)
ceSctpShutdowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpShutdowns.setStatus("current")
_CeSctpStatBytesRec_Type = Counter64
_CeSctpStatBytesRec_Object = MibScalar
ceSctpStatBytesRec = _CeSctpStatBytesRec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 8),
    _CeSctpStatBytesRec_Type()
)
ceSctpStatBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatBytesRec.setStatus("current")
_CeSctpStatBytesSent_Type = Counter64
_CeSctpStatBytesSent_Object = MibScalar
ceSctpStatBytesSent = _CeSctpStatBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 9),
    _CeSctpStatBytesSent_Type()
)
ceSctpStatBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatBytesSent.setStatus("current")
_CeSctpStatChunksDiscard_Type = Counter64
_CeSctpStatChunksDiscard_Object = MibScalar
ceSctpStatChunksDiscard = _CeSctpStatChunksDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 10),
    _CeSctpStatChunksDiscard_Type()
)
ceSctpStatChunksDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksDiscard.setStatus("current")
_CeSctpStatChunksSent_Type = Counter64
_CeSctpStatChunksSent_Object = MibScalar
ceSctpStatChunksSent = _CeSctpStatChunksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 11),
    _CeSctpStatChunksSent_Type()
)
ceSctpStatChunksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksSent.setStatus("current")
_CeSctpStatChunksSentControl_Type = Counter64
_CeSctpStatChunksSentControl_Object = MibScalar
ceSctpStatChunksSentControl = _CeSctpStatChunksSentControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 12),
    _CeSctpStatChunksSentControl_Type()
)
ceSctpStatChunksSentControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksSentControl.setStatus("current")
_CeSctpStatChunksSentOrdered_Type = Counter64
_CeSctpStatChunksSentOrdered_Object = MibScalar
ceSctpStatChunksSentOrdered = _CeSctpStatChunksSentOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 13),
    _CeSctpStatChunksSentOrdered_Type()
)
ceSctpStatChunksSentOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksSentOrdered.setStatus("current")
_CeSctpStatChunksSentUnOrdered_Type = Counter64
_CeSctpStatChunksSentUnOrdered_Object = MibScalar
ceSctpStatChunksSentUnOrdered = _CeSctpStatChunksSentUnOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 14),
    _CeSctpStatChunksSentUnOrdered_Type()
)
ceSctpStatChunksSentUnOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksSentUnOrdered.setStatus("current")
_CeSctpStatChunksRec_Type = Counter64
_CeSctpStatChunksRec_Object = MibScalar
ceSctpStatChunksRec = _CeSctpStatChunksRec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 15),
    _CeSctpStatChunksRec_Type()
)
ceSctpStatChunksRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksRec.setStatus("current")
_CeSctpStatChunksRecControl_Type = Counter64
_CeSctpStatChunksRecControl_Object = MibScalar
ceSctpStatChunksRecControl = _CeSctpStatChunksRecControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 16),
    _CeSctpStatChunksRecControl_Type()
)
ceSctpStatChunksRecControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksRecControl.setStatus("current")
_CeSctpStatChunksRecOrdered_Type = Counter64
_CeSctpStatChunksRecOrdered_Object = MibScalar
ceSctpStatChunksRecOrdered = _CeSctpStatChunksRecOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 17),
    _CeSctpStatChunksRecOrdered_Type()
)
ceSctpStatChunksRecOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksRecOrdered.setStatus("current")
_CeSctpStatChunksRecUnOrdered_Type = Counter64
_CeSctpStatChunksRecUnOrdered_Object = MibScalar
ceSctpStatChunksRecUnOrdered = _CeSctpStatChunksRecUnOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 18),
    _CeSctpStatChunksRecUnOrdered_Type()
)
ceSctpStatChunksRecUnOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksRecUnOrdered.setStatus("current")
_CeSctpStatDatagramsRec_Type = Counter64
_CeSctpStatDatagramsRec_Object = MibScalar
ceSctpStatDatagramsRec = _CeSctpStatDatagramsRec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 19),
    _CeSctpStatDatagramsRec_Type()
)
ceSctpStatDatagramsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatDatagramsRec.setStatus("current")
_CeSctpStatDatagramsSent_Type = Counter64
_CeSctpStatDatagramsSent_Object = MibScalar
ceSctpStatDatagramsSent = _CeSctpStatDatagramsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 20),
    _CeSctpStatDatagramsSent_Type()
)
ceSctpStatDatagramsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatDatagramsSent.setStatus("current")
_CeSctpStatFragmentedUsrMessages_Type = Counter64
_CeSctpStatFragmentedUsrMessages_Object = MibScalar
ceSctpStatFragmentedUsrMessages = _CeSctpStatFragmentedUsrMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 21),
    _CeSctpStatFragmentedUsrMessages_Type()
)
ceSctpStatFragmentedUsrMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatFragmentedUsrMessages.setStatus("current")
_CeSctpStatReassembledUsrMessages_Type = Counter64
_CeSctpStatReassembledUsrMessages_Object = MibScalar
ceSctpStatReassembledUsrMessages = _CeSctpStatReassembledUsrMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 22),
    _CeSctpStatReassembledUsrMessages_Type()
)
ceSctpStatReassembledUsrMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatReassembledUsrMessages.setStatus("current")
_CeSctpStatChunksReTrans_Type = Counter64
_CeSctpStatChunksReTrans_Object = MibScalar
ceSctpStatChunksReTrans = _CeSctpStatChunksReTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 23),
    _CeSctpStatChunksReTrans_Type()
)
ceSctpStatChunksReTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatChunksReTrans.setStatus("current")
_CeSctpStatOutOfBlue_Type = Counter64
_CeSctpStatOutOfBlue_Object = MibScalar
ceSctpStatOutOfBlue = _CeSctpStatOutOfBlue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 24),
    _CeSctpStatOutOfBlue_Type()
)
ceSctpStatOutOfBlue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatOutOfBlue.setStatus("current")
_CeSctpStatT1expired_Type = Counter32
_CeSctpStatT1expired_Object = MibScalar
ceSctpStatT1expired = _CeSctpStatT1expired_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 25),
    _CeSctpStatT1expired_Type()
)
ceSctpStatT1expired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatT1expired.setStatus("current")
_CeSctpStatT2expired_Type = Counter32
_CeSctpStatT2expired_Object = MibScalar
ceSctpStatT2expired = _CeSctpStatT2expired_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 1, 26),
    _CeSctpStatT2expired_Type()
)
ceSctpStatT2expired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpStatT2expired.setStatus("current")
_CeSctpTables_ObjectIdentity = ObjectIdentity
ceSctpTables = _CeSctpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2)
)
_CeSctpAssocTable_Object = MibTable
ceSctpAssocTable = _CeSctpAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ceSctpAssocTable.setStatus("current")
_CeSctpAssocEntry_Object = MibTableRow
ceSctpAssocEntry = _CeSctpAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1)
)
ceSctpAssocEntry.setIndexNames(
    (0, "CISCO-SCTP-MIB", "ceSctpAssocId"),
)
if mibBuilder.loadTexts:
    ceSctpAssocEntry.setStatus("current")


class _CeSctpAssocId_Type(Unsigned32):
    """Custom type ceSctpAssocId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CeSctpAssocId_Type.__name__ = "Unsigned32"
_CeSctpAssocId_Object = MibTableColumn
ceSctpAssocId = _CeSctpAssocId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 1),
    _CeSctpAssocId_Type()
)
ceSctpAssocId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceSctpAssocId.setStatus("current")


class _CeSctpAssocState_Type(Integer32):
    """Custom type ceSctpAssocState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("cookieEchoed", 3),
          ("cookieWait", 2),
          ("deleteTCB", 9),
          ("established", 4),
          ("retrieval", 10),
          ("shutdownAckSent", 8),
          ("shutdownPending", 5),
          ("shutdownReceived", 7),
          ("shutdownSent", 6))
    )


_CeSctpAssocState_Type.__name__ = "Integer32"
_CeSctpAssocState_Object = MibTableColumn
ceSctpAssocState = _CeSctpAssocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 2),
    _CeSctpAssocState_Type()
)
ceSctpAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocState.setStatus("current")
_CeSctpAssocUpTime_Type = TimeTicks
_CeSctpAssocUpTime_Object = MibTableColumn
ceSctpAssocUpTime = _CeSctpAssocUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 3),
    _CeSctpAssocUpTime_Type()
)
ceSctpAssocUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocUpTime.setStatus("current")


class _CeSctpAssocRtoMin_Type(Unsigned32):
    """Custom type ceSctpAssocRtoMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_CeSctpAssocRtoMin_Type.__name__ = "Unsigned32"
_CeSctpAssocRtoMin_Object = MibTableColumn
ceSctpAssocRtoMin = _CeSctpAssocRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 4),
    _CeSctpAssocRtoMin_Type()
)
ceSctpAssocRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRtoMin.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocRtoMin.setUnits("milliseconds")


class _CeSctpAssocRtoMax_Type(Unsigned32):
    """Custom type ceSctpAssocRtoMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_CeSctpAssocRtoMax_Type.__name__ = "Unsigned32"
_CeSctpAssocRtoMax_Object = MibTableColumn
ceSctpAssocRtoMax = _CeSctpAssocRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 5),
    _CeSctpAssocRtoMax_Type()
)
ceSctpAssocRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocRtoMax.setUnits("milliseconds")


class _CeSctpAssocRtoInitial_Type(Unsigned32):
    """Custom type ceSctpAssocRtoInitial based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_CeSctpAssocRtoInitial_Type.__name__ = "Unsigned32"
_CeSctpAssocRtoInitial_Object = MibTableColumn
ceSctpAssocRtoInitial = _CeSctpAssocRtoInitial_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 6),
    _CeSctpAssocRtoInitial_Type()
)
ceSctpAssocRtoInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRtoInitial.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocRtoInitial.setUnits("milliseconds")


class _CeSctpAssocValCookieLife_Type(Unsigned32):
    """Custom type ceSctpAssocValCookieLife based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_CeSctpAssocValCookieLife_Type.__name__ = "Unsigned32"
_CeSctpAssocValCookieLife_Object = MibTableColumn
ceSctpAssocValCookieLife = _CeSctpAssocValCookieLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 7),
    _CeSctpAssocValCookieLife_Type()
)
ceSctpAssocValCookieLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocValCookieLife.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocValCookieLife.setUnits("milliseconds")


class _CeSctpAssocMaxInitRetr_Type(Unsigned32):
    """Custom type ceSctpAssocMaxInitRetr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_CeSctpAssocMaxInitRetr_Type.__name__ = "Unsigned32"
_CeSctpAssocMaxInitRetr_Object = MibTableColumn
ceSctpAssocMaxInitRetr = _CeSctpAssocMaxInitRetr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 8),
    _CeSctpAssocMaxInitRetr_Type()
)
ceSctpAssocMaxInitRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocMaxInitRetr.setStatus("current")


class _CeSctpAssocInitialT1_Type(Unsigned32):
    """Custom type ceSctpAssocInitialT1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_CeSctpAssocInitialT1_Type.__name__ = "Unsigned32"
_CeSctpAssocInitialT1_Object = MibTableColumn
ceSctpAssocInitialT1 = _CeSctpAssocInitialT1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 9),
    _CeSctpAssocInitialT1_Type()
)
ceSctpAssocInitialT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocInitialT1.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocInitialT1.setUnits("milliseconds")


class _CeSctpAssocInitialT2_Type(Unsigned32):
    """Custom type ceSctpAssocInitialT2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_CeSctpAssocInitialT2_Type.__name__ = "Unsigned32"
_CeSctpAssocInitialT2_Object = MibTableColumn
ceSctpAssocInitialT2 = _CeSctpAssocInitialT2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 10),
    _CeSctpAssocInitialT2_Type()
)
ceSctpAssocInitialT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocInitialT2.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocInitialT2.setUnits("milliseconds")


class _CeSctpAssocRemHostName_Type(OctetString):
    """Custom type ceSctpAssocRemHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CeSctpAssocRemHostName_Type.__name__ = "OctetString"
_CeSctpAssocRemHostName_Object = MibTableColumn
ceSctpAssocRemHostName = _CeSctpAssocRemHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 11),
    _CeSctpAssocRemHostName_Type()
)
ceSctpAssocRemHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemHostName.setStatus("current")


class _CeSctpAssocLocalSCTPPort_Type(Unsigned32):
    """Custom type ceSctpAssocLocalSCTPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 32767),
    )


_CeSctpAssocLocalSCTPPort_Type.__name__ = "Unsigned32"
_CeSctpAssocLocalSCTPPort_Object = MibTableColumn
ceSctpAssocLocalSCTPPort = _CeSctpAssocLocalSCTPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 12),
    _CeSctpAssocLocalSCTPPort_Type()
)
ceSctpAssocLocalSCTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocLocalSCTPPort.setStatus("current")


class _CeSctpAssocRemSCTPPort_Type(Unsigned32):
    """Custom type ceSctpAssocRemSCTPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 32767),
    )


_CeSctpAssocRemSCTPPort_Type.__name__ = "Unsigned32"
_CeSctpAssocRemSCTPPort_Object = MibTableColumn
ceSctpAssocRemSCTPPort = _CeSctpAssocRemSCTPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 13),
    _CeSctpAssocRemSCTPPort_Type()
)
ceSctpAssocRemSCTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemSCTPPort.setStatus("current")
_CeSctpAssocRemPrimaryAddressType_Type = InetAddressType
_CeSctpAssocRemPrimaryAddressType_Object = MibTableColumn
ceSctpAssocRemPrimaryAddressType = _CeSctpAssocRemPrimaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 14),
    _CeSctpAssocRemPrimaryAddressType_Type()
)
ceSctpAssocRemPrimaryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemPrimaryAddressType.setStatus("current")
_CeSctpAssocRemPrimaryAddress_Type = InetAddress
_CeSctpAssocRemPrimaryAddress_Object = MibTableColumn
ceSctpAssocRemPrimaryAddress = _CeSctpAssocRemPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 15),
    _CeSctpAssocRemPrimaryAddress_Type()
)
ceSctpAssocRemPrimaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemPrimaryAddress.setStatus("current")


class _CeSctpAssocCongestionLevels_Type(Unsigned32):
    """Custom type ceSctpAssocCongestionLevels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CeSctpAssocCongestionLevels_Type.__name__ = "Unsigned32"
_CeSctpAssocCongestionLevels_Object = MibTableColumn
ceSctpAssocCongestionLevels = _CeSctpAssocCongestionLevels_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 16),
    _CeSctpAssocCongestionLevels_Type()
)
ceSctpAssocCongestionLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocCongestionLevels.setStatus("current")


class _CeSctpAssocCongestionLevelsCur_Type(Unsigned32):
    """Custom type ceSctpAssocCongestionLevelsCur based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CeSctpAssocCongestionLevelsCur_Type.__name__ = "Unsigned32"
_CeSctpAssocCongestionLevelsCur_Object = MibTableColumn
ceSctpAssocCongestionLevelsCur = _CeSctpAssocCongestionLevelsCur_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 17),
    _CeSctpAssocCongestionLevelsCur_Type()
)
ceSctpAssocCongestionLevelsCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocCongestionLevelsCur.setStatus("current")


class _CeSctpAssocCongestionAbate1_Type(Unsigned32):
    """Custom type ceSctpAssocCongestionAbate1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CeSctpAssocCongestionAbate1_Type.__name__ = "Unsigned32"
_CeSctpAssocCongestionAbate1_Object = MibTableColumn
ceSctpAssocCongestionAbate1 = _CeSctpAssocCongestionAbate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 18),
    _CeSctpAssocCongestionAbate1_Type()
)
ceSctpAssocCongestionAbate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocCongestionAbate1.setStatus("current")


class _CeSctpAssocCongestionAbate2_Type(Unsigned32):
    """Custom type ceSctpAssocCongestionAbate2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CeSctpAssocCongestionAbate2_Type.__name__ = "Unsigned32"
_CeSctpAssocCongestionAbate2_Object = MibTableColumn
ceSctpAssocCongestionAbate2 = _CeSctpAssocCongestionAbate2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 19),
    _CeSctpAssocCongestionAbate2_Type()
)
ceSctpAssocCongestionAbate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocCongestionAbate2.setStatus("current")


class _CeSctpAssocCongestionAbate3_Type(Unsigned32):
    """Custom type ceSctpAssocCongestionAbate3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CeSctpAssocCongestionAbate3_Type.__name__ = "Unsigned32"
_CeSctpAssocCongestionAbate3_Object = MibTableColumn
ceSctpAssocCongestionAbate3 = _CeSctpAssocCongestionAbate3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 20),
    _CeSctpAssocCongestionAbate3_Type()
)
ceSctpAssocCongestionAbate3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocCongestionAbate3.setStatus("current")


class _CeSctpAssocCongestionOnset1_Type(Unsigned32):
    """Custom type ceSctpAssocCongestionOnset1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CeSctpAssocCongestionOnset1_Type.__name__ = "Unsigned32"
_CeSctpAssocCongestionOnset1_Object = MibTableColumn
ceSctpAssocCongestionOnset1 = _CeSctpAssocCongestionOnset1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 21),
    _CeSctpAssocCongestionOnset1_Type()
)
ceSctpAssocCongestionOnset1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocCongestionOnset1.setStatus("current")


class _CeSctpAssocCongestionOnset2_Type(Unsigned32):
    """Custom type ceSctpAssocCongestionOnset2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CeSctpAssocCongestionOnset2_Type.__name__ = "Unsigned32"
_CeSctpAssocCongestionOnset2_Object = MibTableColumn
ceSctpAssocCongestionOnset2 = _CeSctpAssocCongestionOnset2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 22),
    _CeSctpAssocCongestionOnset2_Type()
)
ceSctpAssocCongestionOnset2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocCongestionOnset2.setStatus("current")


class _CeSctpAssocCongestionOnset3_Type(Unsigned32):
    """Custom type ceSctpAssocCongestionOnset3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CeSctpAssocCongestionOnset3_Type.__name__ = "Unsigned32"
_CeSctpAssocCongestionOnset3_Object = MibTableColumn
ceSctpAssocCongestionOnset3 = _CeSctpAssocCongestionOnset3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 23),
    _CeSctpAssocCongestionOnset3_Type()
)
ceSctpAssocCongestionOnset3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocCongestionOnset3.setStatus("current")


class _CeSctpAssocInStreams_Type(Unsigned32):
    """Custom type ceSctpAssocInStreams based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CeSctpAssocInStreams_Type.__name__ = "Unsigned32"
_CeSctpAssocInStreams_Object = MibTableColumn
ceSctpAssocInStreams = _CeSctpAssocInStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 24),
    _CeSctpAssocInStreams_Type()
)
ceSctpAssocInStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocInStreams.setStatus("current")


class _CeSctpAssocOutStreams_Type(Unsigned32):
    """Custom type ceSctpAssocOutStreams based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CeSctpAssocOutStreams_Type.__name__ = "Unsigned32"
_CeSctpAssocOutStreams_Object = MibTableColumn
ceSctpAssocOutStreams = _CeSctpAssocOutStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 25),
    _CeSctpAssocOutStreams_Type()
)
ceSctpAssocOutStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocOutStreams.setStatus("current")


class _CeSctpAssocMaxRetr_Type(Unsigned32):
    """Custom type ceSctpAssocMaxRetr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_CeSctpAssocMaxRetr_Type.__name__ = "Unsigned32"
_CeSctpAssocMaxRetr_Object = MibTableColumn
ceSctpAssocMaxRetr = _CeSctpAssocMaxRetr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 26),
    _CeSctpAssocMaxRetr_Type()
)
ceSctpAssocMaxRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocMaxRetr.setStatus("current")


class _CeSctpAssocMTU_Type(Unsigned32):
    """Custom type ceSctpAssocMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CeSctpAssocMTU_Type.__name__ = "Unsigned32"
_CeSctpAssocMTU_Object = MibTableColumn
ceSctpAssocMTU = _CeSctpAssocMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 27),
    _CeSctpAssocMTU_Type()
)
ceSctpAssocMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocMTU.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocMTU.setUnits("bytes")


class _CeSctpAssocLocRecWnd_Type(Unsigned32):
    """Custom type ceSctpAssocLocRecWnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CeSctpAssocLocRecWnd_Type.__name__ = "Unsigned32"
_CeSctpAssocLocRecWnd_Object = MibTableColumn
ceSctpAssocLocRecWnd = _CeSctpAssocLocRecWnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 28),
    _CeSctpAssocLocRecWnd_Type()
)
ceSctpAssocLocRecWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocLocRecWnd.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocLocRecWnd.setUnits("bytes")


class _CeSctpAssocLocRecWndLowMark_Type(Unsigned32):
    """Custom type ceSctpAssocLocRecWndLowMark based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocLocRecWndLowMark_Type.__name__ = "Unsigned32"
_CeSctpAssocLocRecWndLowMark_Object = MibTableColumn
ceSctpAssocLocRecWndLowMark = _CeSctpAssocLocRecWndLowMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 29),
    _CeSctpAssocLocRecWndLowMark_Type()
)
ceSctpAssocLocRecWndLowMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocLocRecWndLowMark.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocLocRecWndLowMark.setUnits("bytes")
_CeSctpAssocLocRecWndZeroCnt_Type = Counter64
_CeSctpAssocLocRecWndZeroCnt_Object = MibTableColumn
ceSctpAssocLocRecWndZeroCnt = _CeSctpAssocLocRecWndZeroCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 30),
    _CeSctpAssocLocRecWndZeroCnt_Type()
)
ceSctpAssocLocRecWndZeroCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocLocRecWndZeroCnt.setStatus("current")


class _CeSctpAssocRemRecWnd_Type(Unsigned32):
    """Custom type ceSctpAssocRemRecWnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocRemRecWnd_Type.__name__ = "Unsigned32"
_CeSctpAssocRemRecWnd_Object = MibTableColumn
ceSctpAssocRemRecWnd = _CeSctpAssocRemRecWnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 31),
    _CeSctpAssocRemRecWnd_Type()
)
ceSctpAssocRemRecWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemRecWnd.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocRemRecWnd.setUnits("bytes")


class _CeSctpAssocRemRecWndLowMark_Type(Unsigned32):
    """Custom type ceSctpAssocRemRecWndLowMark based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocRemRecWndLowMark_Type.__name__ = "Unsigned32"
_CeSctpAssocRemRecWndLowMark_Object = MibTableColumn
ceSctpAssocRemRecWndLowMark = _CeSctpAssocRemRecWndLowMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 32),
    _CeSctpAssocRemRecWndLowMark_Type()
)
ceSctpAssocRemRecWndLowMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemRecWndLowMark.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocRemRecWndLowMark.setUnits("bytes")
_CeSctpAssocRemRecWndZeroCnt_Type = Counter64
_CeSctpAssocRemRecWndZeroCnt_Object = MibTableColumn
ceSctpAssocRemRecWndZeroCnt = _CeSctpAssocRemRecWndZeroCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 33),
    _CeSctpAssocRemRecWndZeroCnt_Type()
)
ceSctpAssocRemRecWndZeroCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemRecWndZeroCnt.setStatus("current")


class _CeSctpAssocULPDatagramsQueued_Type(Unsigned32):
    """Custom type ceSctpAssocULPDatagramsQueued based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocULPDatagramsQueued_Type.__name__ = "Unsigned32"
_CeSctpAssocULPDatagramsQueued_Object = MibTableColumn
ceSctpAssocULPDatagramsQueued = _CeSctpAssocULPDatagramsQueued_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 34),
    _CeSctpAssocULPDatagramsQueued_Type()
)
ceSctpAssocULPDatagramsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocULPDatagramsQueued.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocULPDatagramsQueued.setUnits("DataGrams")


class _CeSctpAssocULPDatagramsQueuedHigh_Type(Unsigned32):
    """Custom type ceSctpAssocULPDatagramsQueuedHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocULPDatagramsQueuedHigh_Type.__name__ = "Unsigned32"
_CeSctpAssocULPDatagramsQueuedHigh_Object = MibTableColumn
ceSctpAssocULPDatagramsQueuedHigh = _CeSctpAssocULPDatagramsQueuedHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 35),
    _CeSctpAssocULPDatagramsQueuedHigh_Type()
)
ceSctpAssocULPDatagramsQueuedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocULPDatagramsQueuedHigh.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocULPDatagramsQueuedHigh.setUnits("DataGrams")
_CeSctpAssocChecksumErrorCounter_Type = Counter64
_CeSctpAssocChecksumErrorCounter_Object = MibTableColumn
ceSctpAssocChecksumErrorCounter = _CeSctpAssocChecksumErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 36),
    _CeSctpAssocChecksumErrorCounter_Type()
)
ceSctpAssocChecksumErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChecksumErrorCounter.setStatus("current")
_CeSctpAssocBytesSent_Type = Counter64
_CeSctpAssocBytesSent_Object = MibTableColumn
ceSctpAssocBytesSent = _CeSctpAssocBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 37),
    _CeSctpAssocBytesSent_Type()
)
ceSctpAssocBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocBytesSent.setStatus("current")
_CeSctpAssocBytesRec_Type = Counter64
_CeSctpAssocBytesRec_Object = MibTableColumn
ceSctpAssocBytesRec = _CeSctpAssocBytesRec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 38),
    _CeSctpAssocBytesRec_Type()
)
ceSctpAssocBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocBytesRec.setStatus("current")
_CeSctpAssocChunksDiscarded_Type = Counter64
_CeSctpAssocChunksDiscarded_Object = MibTableColumn
ceSctpAssocChunksDiscarded = _CeSctpAssocChunksDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 39),
    _CeSctpAssocChunksDiscarded_Type()
)
ceSctpAssocChunksDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksDiscarded.setStatus("current")
_CeSctpAssocChunksRec_Type = Counter64
_CeSctpAssocChunksRec_Object = MibTableColumn
ceSctpAssocChunksRec = _CeSctpAssocChunksRec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 40),
    _CeSctpAssocChunksRec_Type()
)
ceSctpAssocChunksRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksRec.setStatus("current")
_CeSctpAssocChunksRecControl_Type = Counter64
_CeSctpAssocChunksRecControl_Object = MibTableColumn
ceSctpAssocChunksRecControl = _CeSctpAssocChunksRecControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 41),
    _CeSctpAssocChunksRecControl_Type()
)
ceSctpAssocChunksRecControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksRecControl.setStatus("current")
_CeSctpAssocChunksRecOrdered_Type = Counter64
_CeSctpAssocChunksRecOrdered_Object = MibTableColumn
ceSctpAssocChunksRecOrdered = _CeSctpAssocChunksRecOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 42),
    _CeSctpAssocChunksRecOrdered_Type()
)
ceSctpAssocChunksRecOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksRecOrdered.setStatus("current")
_CeSctpAssocChunksRecUnOrdered_Type = Counter64
_CeSctpAssocChunksRecUnOrdered_Object = MibTableColumn
ceSctpAssocChunksRecUnOrdered = _CeSctpAssocChunksRecUnOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 43),
    _CeSctpAssocChunksRecUnOrdered_Type()
)
ceSctpAssocChunksRecUnOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksRecUnOrdered.setStatus("current")
_CeSctpAssocChunksRecOutOrder_Type = Counter64
_CeSctpAssocChunksRecOutOrder_Object = MibTableColumn
ceSctpAssocChunksRecOutOrder = _CeSctpAssocChunksRecOutOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 44),
    _CeSctpAssocChunksRecOutOrder_Type()
)
ceSctpAssocChunksRecOutOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksRecOutOrder.setStatus("current")
_CeSctpAssocChunksReTrans_Type = Counter64
_CeSctpAssocChunksReTrans_Object = MibTableColumn
ceSctpAssocChunksReTrans = _CeSctpAssocChunksReTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 45),
    _CeSctpAssocChunksReTrans_Type()
)
ceSctpAssocChunksReTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksReTrans.setStatus("current")
_CeSctpAssocChunksSent_Type = Counter64
_CeSctpAssocChunksSent_Object = MibTableColumn
ceSctpAssocChunksSent = _CeSctpAssocChunksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 46),
    _CeSctpAssocChunksSent_Type()
)
ceSctpAssocChunksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksSent.setStatus("current")
_CeSctpAssocChunksSentControl_Type = Counter64
_CeSctpAssocChunksSentControl_Object = MibTableColumn
ceSctpAssocChunksSentControl = _CeSctpAssocChunksSentControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 47),
    _CeSctpAssocChunksSentControl_Type()
)
ceSctpAssocChunksSentControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksSentControl.setStatus("current")
_CeSctpAssocChunksSentOrdered_Type = Counter64
_CeSctpAssocChunksSentOrdered_Object = MibTableColumn
ceSctpAssocChunksSentOrdered = _CeSctpAssocChunksSentOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 48),
    _CeSctpAssocChunksSentOrdered_Type()
)
ceSctpAssocChunksSentOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksSentOrdered.setStatus("current")
_CeSctpAssocChunksSentUnOrdered_Type = Counter64
_CeSctpAssocChunksSentUnOrdered_Object = MibTableColumn
ceSctpAssocChunksSentUnOrdered = _CeSctpAssocChunksSentUnOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 49),
    _CeSctpAssocChunksSentUnOrdered_Type()
)
ceSctpAssocChunksSentUnOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocChunksSentUnOrdered.setStatus("current")
_CeSctpAssocDatagramsRec_Type = Counter64
_CeSctpAssocDatagramsRec_Object = MibTableColumn
ceSctpAssocDatagramsRec = _CeSctpAssocDatagramsRec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 50),
    _CeSctpAssocDatagramsRec_Type()
)
ceSctpAssocDatagramsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocDatagramsRec.setStatus("current")
_CeSctpAssocDatagramsSent_Type = Counter64
_CeSctpAssocDatagramsSent_Object = MibTableColumn
ceSctpAssocDatagramsSent = _CeSctpAssocDatagramsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 51),
    _CeSctpAssocDatagramsSent_Type()
)
ceSctpAssocDatagramsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocDatagramsSent.setStatus("current")
_CeSctpAssocRowStatus_Type = RowStatus
_CeSctpAssocRowStatus_Object = MibTableColumn
ceSctpAssocRowStatus = _CeSctpAssocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 1, 1, 52),
    _CeSctpAssocRowStatus_Type()
)
ceSctpAssocRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRowStatus.setStatus("current")
_CeSctpAssocLocalAddressTable_Object = MibTable
ceSctpAssocLocalAddressTable = _CeSctpAssocLocalAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ceSctpAssocLocalAddressTable.setStatus("current")
_CeSctpAssocLocalAddressEntry_Object = MibTableRow
ceSctpAssocLocalAddressEntry = _CeSctpAssocLocalAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 2, 1)
)
ceSctpAssocLocalAddressEntry.setIndexNames(
    (0, "CISCO-SCTP-MIB", "ceSctpAssocId"),
    (0, "CISCO-SCTP-MIB", "ceSctpAssocLocalAddressIPType"),
    (0, "CISCO-SCTP-MIB", "ceSctpAssocLocalAddressIP"),
)
if mibBuilder.loadTexts:
    ceSctpAssocLocalAddressEntry.setStatus("current")
_CeSctpAssocLocalAddressIPType_Type = InetAddressType
_CeSctpAssocLocalAddressIPType_Object = MibTableColumn
ceSctpAssocLocalAddressIPType = _CeSctpAssocLocalAddressIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 2, 1, 1),
    _CeSctpAssocLocalAddressIPType_Type()
)
ceSctpAssocLocalAddressIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceSctpAssocLocalAddressIPType.setStatus("current")
_CeSctpAssocLocalAddressIP_Type = InetAddress
_CeSctpAssocLocalAddressIP_Object = MibTableColumn
ceSctpAssocLocalAddressIP = _CeSctpAssocLocalAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 2, 1, 2),
    _CeSctpAssocLocalAddressIP_Type()
)
ceSctpAssocLocalAddressIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceSctpAssocLocalAddressIP.setStatus("current")
_CeSctpAssocLocalAddressRowStatus_Type = RowStatus
_CeSctpAssocLocalAddressRowStatus_Object = MibTableColumn
ceSctpAssocLocalAddressRowStatus = _CeSctpAssocLocalAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 2, 1, 3),
    _CeSctpAssocLocalAddressRowStatus_Type()
)
ceSctpAssocLocalAddressRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocLocalAddressRowStatus.setStatus("current")
_CeSctpAssocRemAddressTable_Object = MibTable
ceSctpAssocRemAddressTable = _CeSctpAssocRemAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressTable.setStatus("current")
_CeSctpAssocRemAddressEntry_Object = MibTableRow
ceSctpAssocRemAddressEntry = _CeSctpAssocRemAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1)
)
ceSctpAssocRemAddressEntry.setIndexNames(
    (0, "CISCO-SCTP-MIB", "ceSctpAssocId"),
    (0, "CISCO-SCTP-MIB", "ceSctpAssocRemAddressIPType"),
    (0, "CISCO-SCTP-MIB", "ceSctpAssocRemAddressIP"),
)
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressEntry.setStatus("current")
_CeSctpAssocRemAddressIPType_Type = InetAddressType
_CeSctpAssocRemAddressIPType_Object = MibTableColumn
ceSctpAssocRemAddressIPType = _CeSctpAssocRemAddressIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 1),
    _CeSctpAssocRemAddressIPType_Type()
)
ceSctpAssocRemAddressIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressIPType.setStatus("current")
_CeSctpAssocRemAddressIP_Type = InetAddress
_CeSctpAssocRemAddressIP_Object = MibTableColumn
ceSctpAssocRemAddressIP = _CeSctpAssocRemAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 2),
    _CeSctpAssocRemAddressIP_Type()
)
ceSctpAssocRemAddressIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressIP.setStatus("current")


class _CeSctpAssocRemAddressStatus_Type(Integer32):
    """Custom type ceSctpAssocRemAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("failed", 2),
          ("inactive", 1))
    )


_CeSctpAssocRemAddressStatus_Type.__name__ = "Integer32"
_CeSctpAssocRemAddressStatus_Object = MibTableColumn
ceSctpAssocRemAddressStatus = _CeSctpAssocRemAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 3),
    _CeSctpAssocRemAddressStatus_Type()
)
ceSctpAssocRemAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressStatus.setStatus("current")


class _CeSctpAssocRemAddressRTO_Type(Unsigned32):
    """Custom type ceSctpAssocRemAddressRTO based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocRemAddressRTO_Type.__name__ = "Unsigned32"
_CeSctpAssocRemAddressRTO_Object = MibTableColumn
ceSctpAssocRemAddressRTO = _CeSctpAssocRemAddressRTO_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 4),
    _CeSctpAssocRemAddressRTO_Type()
)
ceSctpAssocRemAddressRTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressRTO.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressRTO.setUnits("milliseconds")


class _CeSctpAssocRemAddressHtBtFlag_Type(Integer32):
    """Custom type ceSctpAssocRemAddressHtBtFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_CeSctpAssocRemAddressHtBtFlag_Type.__name__ = "Integer32"
_CeSctpAssocRemAddressHtBtFlag_Object = MibTableColumn
ceSctpAssocRemAddressHtBtFlag = _CeSctpAssocRemAddressHtBtFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 5),
    _CeSctpAssocRemAddressHtBtFlag_Type()
)
ceSctpAssocRemAddressHtBtFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressHtBtFlag.setStatus("current")


class _CeSctpAssocRemAddressHtBtTime_Type(Unsigned32):
    """Custom type ceSctpAssocRemAddressHtBtTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocRemAddressHtBtTime_Type.__name__ = "Unsigned32"
_CeSctpAssocRemAddressHtBtTime_Object = MibTableColumn
ceSctpAssocRemAddressHtBtTime = _CeSctpAssocRemAddressHtBtTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 6),
    _CeSctpAssocRemAddressHtBtTime_Type()
)
ceSctpAssocRemAddressHtBtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressHtBtTime.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressHtBtTime.setUnits("milliseconds")


class _CeSctpAssocRemAddressMaxRetran_Type(Unsigned32):
    """Custom type ceSctpAssocRemAddressMaxRetran based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocRemAddressMaxRetran_Type.__name__ = "Unsigned32"
_CeSctpAssocRemAddressMaxRetran_Object = MibTableColumn
ceSctpAssocRemAddressMaxRetran = _CeSctpAssocRemAddressMaxRetran_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 7),
    _CeSctpAssocRemAddressMaxRetran_Type()
)
ceSctpAssocRemAddressMaxRetran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressMaxRetran.setStatus("current")
_CeSctpAssocRemAddressRetransCnt_Type = Counter64
_CeSctpAssocRemAddressRetransCnt_Object = MibTableColumn
ceSctpAssocRemAddressRetransCnt = _CeSctpAssocRemAddressRetransCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 8),
    _CeSctpAssocRemAddressRetransCnt_Type()
)
ceSctpAssocRemAddressRetransCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressRetransCnt.setStatus("current")


class _CeSctpAssocRemAddressSRTT_Type(Unsigned32):
    """Custom type ceSctpAssocRemAddressSRTT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CeSctpAssocRemAddressSRTT_Type.__name__ = "Unsigned32"
_CeSctpAssocRemAddressSRTT_Object = MibTableColumn
ceSctpAssocRemAddressSRTT = _CeSctpAssocRemAddressSRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 9),
    _CeSctpAssocRemAddressSRTT_Type()
)
ceSctpAssocRemAddressSRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressSRTT.setStatus("current")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressSRTT.setUnits("milliseconds")
_CeSctpAssocRemAddressRowStatus_Type = RowStatus
_CeSctpAssocRemAddressRowStatus_Object = MibTableColumn
ceSctpAssocRemAddressRowStatus = _CeSctpAssocRemAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 1, 2, 3, 1, 10),
    _CeSctpAssocRemAddressRowStatus_Type()
)
ceSctpAssocRemAddressRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSctpAssocRemAddressRowStatus.setStatus("current")
_CeSctpConformance_ObjectIdentity = ObjectIdentity
ceSctpConformance = _CeSctpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2)
)
_CeSctpGroups_ObjectIdentity = ObjectIdentity
ceSctpGroups = _CeSctpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2, 1)
)
_CeSctpCompliances_ObjectIdentity = ObjectIdentity
ceSctpCompliances = _CeSctpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2, 2)
)

# Managed Objects groups

ceSctpGeneralVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2, 1, 1)
)
ceSctpGeneralVariablesGroup.setObjects(
      *(("CISCO-SCTP-MIB", "ceSctpRtoAlgorithm"),
        ("CISCO-SCTP-MIB", "ceSctpMaxAssociations"))
)
if mibBuilder.loadTexts:
    ceSctpGeneralVariablesGroup.setStatus("current")

ceSctpStateStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2, 1, 2)
)
ceSctpStateStatGroup.setObjects(
      *(("CISCO-SCTP-MIB", "ceSctpCurrEstab"),
        ("CISCO-SCTP-MIB", "ceSctpActiveEstab"),
        ("CISCO-SCTP-MIB", "ceSctpPassiveEstab"),
        ("CISCO-SCTP-MIB", "ceSctpAborted"),
        ("CISCO-SCTP-MIB", "ceSctpShutdowns"))
)
if mibBuilder.loadTexts:
    ceSctpStateStatGroup.setStatus("current")

ceSctpOtherStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2, 1, 3)
)
ceSctpOtherStatGroup.setObjects(
      *(("CISCO-SCTP-MIB", "ceSctpStatBytesRec"),
        ("CISCO-SCTP-MIB", "ceSctpStatBytesSent"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksDiscard"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksSent"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksSentControl"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksSentOrdered"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksSentUnOrdered"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksRec"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksRecControl"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksRecOrdered"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksRecUnOrdered"),
        ("CISCO-SCTP-MIB", "ceSctpStatChunksReTrans"),
        ("CISCO-SCTP-MIB", "ceSctpStatDatagramsRec"),
        ("CISCO-SCTP-MIB", "ceSctpStatDatagramsSent"),
        ("CISCO-SCTP-MIB", "ceSctpStatFragmentedUsrMessages"),
        ("CISCO-SCTP-MIB", "ceSctpStatReassembledUsrMessages"),
        ("CISCO-SCTP-MIB", "ceSctpStatOutOfBlue"),
        ("CISCO-SCTP-MIB", "ceSctpStatT1expired"),
        ("CISCO-SCTP-MIB", "ceSctpStatT2expired"))
)
if mibBuilder.loadTexts:
    ceSctpOtherStatGroup.setStatus("current")

ceSctpAssocTablesVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2, 1, 4)
)
ceSctpAssocTablesVariablesGroup.setObjects(
      *(("CISCO-SCTP-MIB", "ceSctpAssocState"),
        ("CISCO-SCTP-MIB", "ceSctpAssocUpTime"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRtoMin"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRtoMax"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRtoInitial"),
        ("CISCO-SCTP-MIB", "ceSctpAssocValCookieLife"),
        ("CISCO-SCTP-MIB", "ceSctpAssocMaxInitRetr"),
        ("CISCO-SCTP-MIB", "ceSctpAssocInitialT1"),
        ("CISCO-SCTP-MIB", "ceSctpAssocInitialT2"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemHostName"),
        ("CISCO-SCTP-MIB", "ceSctpAssocLocalSCTPPort"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemSCTPPort"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemPrimaryAddressType"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemPrimaryAddress"),
        ("CISCO-SCTP-MIB", "ceSctpAssocCongestionLevels"),
        ("CISCO-SCTP-MIB", "ceSctpAssocCongestionLevelsCur"),
        ("CISCO-SCTP-MIB", "ceSctpAssocCongestionAbate1"),
        ("CISCO-SCTP-MIB", "ceSctpAssocCongestionAbate2"),
        ("CISCO-SCTP-MIB", "ceSctpAssocCongestionAbate3"),
        ("CISCO-SCTP-MIB", "ceSctpAssocCongestionOnset1"),
        ("CISCO-SCTP-MIB", "ceSctpAssocCongestionOnset2"),
        ("CISCO-SCTP-MIB", "ceSctpAssocCongestionOnset3"),
        ("CISCO-SCTP-MIB", "ceSctpAssocInStreams"),
        ("CISCO-SCTP-MIB", "ceSctpAssocOutStreams"),
        ("CISCO-SCTP-MIB", "ceSctpAssocMaxRetr"),
        ("CISCO-SCTP-MIB", "ceSctpAssocMTU"),
        ("CISCO-SCTP-MIB", "ceSctpAssocLocRecWnd"),
        ("CISCO-SCTP-MIB", "ceSctpAssocLocRecWndLowMark"),
        ("CISCO-SCTP-MIB", "ceSctpAssocLocRecWndZeroCnt"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemRecWnd"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemRecWndLowMark"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemRecWndZeroCnt"),
        ("CISCO-SCTP-MIB", "ceSctpAssocULPDatagramsQueued"),
        ("CISCO-SCTP-MIB", "ceSctpAssocULPDatagramsQueuedHigh"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChecksumErrorCounter"),
        ("CISCO-SCTP-MIB", "ceSctpAssocBytesRec"),
        ("CISCO-SCTP-MIB", "ceSctpAssocBytesSent"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksDiscarded"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksRec"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksRecControl"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksRecOrdered"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksRecUnOrdered"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksRecOutOrder"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksReTrans"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksSent"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksSentControl"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksSentOrdered"),
        ("CISCO-SCTP-MIB", "ceSctpAssocChunksSentUnOrdered"),
        ("CISCO-SCTP-MIB", "ceSctpAssocDatagramsRec"),
        ("CISCO-SCTP-MIB", "ceSctpAssocDatagramsSent"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRowStatus"),
        ("CISCO-SCTP-MIB", "ceSctpAssocLocalAddressRowStatus"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemAddressStatus"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemAddressRTO"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemAddressHtBtFlag"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemAddressHtBtTime"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemAddressMaxRetran"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemAddressSRTT"),
        ("CISCO-SCTP-MIB", "ceSctpAssocRemAddressRowStatus"))
)
if mibBuilder.loadTexts:
    ceSctpAssocTablesVariablesGroup.setStatus("current")

ceSctpAssocStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2, 1, 5)
)
ceSctpAssocStatGroup.setObjects(
    ("CISCO-SCTP-MIB", "ceSctpAssocRemAddressRetransCnt")
)
if mibBuilder.loadTexts:
    ceSctpAssocStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ceSctpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 74, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ceSctpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SCTP-MIB",
    **{"InetAddressType": InetAddressType,
       "InetAddress": InetAddress,
       "ceSctpMIB": ceSctpMIB,
       "ceSctpObjects": ceSctpObjects,
       "ceSctpScalars": ceSctpScalars,
       "ceSctpRtoAlgorithm": ceSctpRtoAlgorithm,
       "ceSctpMaxAssociations": ceSctpMaxAssociations,
       "ceSctpCurrEstab": ceSctpCurrEstab,
       "ceSctpActiveEstab": ceSctpActiveEstab,
       "ceSctpPassiveEstab": ceSctpPassiveEstab,
       "ceSctpAborted": ceSctpAborted,
       "ceSctpShutdowns": ceSctpShutdowns,
       "ceSctpStatBytesRec": ceSctpStatBytesRec,
       "ceSctpStatBytesSent": ceSctpStatBytesSent,
       "ceSctpStatChunksDiscard": ceSctpStatChunksDiscard,
       "ceSctpStatChunksSent": ceSctpStatChunksSent,
       "ceSctpStatChunksSentControl": ceSctpStatChunksSentControl,
       "ceSctpStatChunksSentOrdered": ceSctpStatChunksSentOrdered,
       "ceSctpStatChunksSentUnOrdered": ceSctpStatChunksSentUnOrdered,
       "ceSctpStatChunksRec": ceSctpStatChunksRec,
       "ceSctpStatChunksRecControl": ceSctpStatChunksRecControl,
       "ceSctpStatChunksRecOrdered": ceSctpStatChunksRecOrdered,
       "ceSctpStatChunksRecUnOrdered": ceSctpStatChunksRecUnOrdered,
       "ceSctpStatDatagramsRec": ceSctpStatDatagramsRec,
       "ceSctpStatDatagramsSent": ceSctpStatDatagramsSent,
       "ceSctpStatFragmentedUsrMessages": ceSctpStatFragmentedUsrMessages,
       "ceSctpStatReassembledUsrMessages": ceSctpStatReassembledUsrMessages,
       "ceSctpStatChunksReTrans": ceSctpStatChunksReTrans,
       "ceSctpStatOutOfBlue": ceSctpStatOutOfBlue,
       "ceSctpStatT1expired": ceSctpStatT1expired,
       "ceSctpStatT2expired": ceSctpStatT2expired,
       "ceSctpTables": ceSctpTables,
       "ceSctpAssocTable": ceSctpAssocTable,
       "ceSctpAssocEntry": ceSctpAssocEntry,
       "ceSctpAssocId": ceSctpAssocId,
       "ceSctpAssocState": ceSctpAssocState,
       "ceSctpAssocUpTime": ceSctpAssocUpTime,
       "ceSctpAssocRtoMin": ceSctpAssocRtoMin,
       "ceSctpAssocRtoMax": ceSctpAssocRtoMax,
       "ceSctpAssocRtoInitial": ceSctpAssocRtoInitial,
       "ceSctpAssocValCookieLife": ceSctpAssocValCookieLife,
       "ceSctpAssocMaxInitRetr": ceSctpAssocMaxInitRetr,
       "ceSctpAssocInitialT1": ceSctpAssocInitialT1,
       "ceSctpAssocInitialT2": ceSctpAssocInitialT2,
       "ceSctpAssocRemHostName": ceSctpAssocRemHostName,
       "ceSctpAssocLocalSCTPPort": ceSctpAssocLocalSCTPPort,
       "ceSctpAssocRemSCTPPort": ceSctpAssocRemSCTPPort,
       "ceSctpAssocRemPrimaryAddressType": ceSctpAssocRemPrimaryAddressType,
       "ceSctpAssocRemPrimaryAddress": ceSctpAssocRemPrimaryAddress,
       "ceSctpAssocCongestionLevels": ceSctpAssocCongestionLevels,
       "ceSctpAssocCongestionLevelsCur": ceSctpAssocCongestionLevelsCur,
       "ceSctpAssocCongestionAbate1": ceSctpAssocCongestionAbate1,
       "ceSctpAssocCongestionAbate2": ceSctpAssocCongestionAbate2,
       "ceSctpAssocCongestionAbate3": ceSctpAssocCongestionAbate3,
       "ceSctpAssocCongestionOnset1": ceSctpAssocCongestionOnset1,
       "ceSctpAssocCongestionOnset2": ceSctpAssocCongestionOnset2,
       "ceSctpAssocCongestionOnset3": ceSctpAssocCongestionOnset3,
       "ceSctpAssocInStreams": ceSctpAssocInStreams,
       "ceSctpAssocOutStreams": ceSctpAssocOutStreams,
       "ceSctpAssocMaxRetr": ceSctpAssocMaxRetr,
       "ceSctpAssocMTU": ceSctpAssocMTU,
       "ceSctpAssocLocRecWnd": ceSctpAssocLocRecWnd,
       "ceSctpAssocLocRecWndLowMark": ceSctpAssocLocRecWndLowMark,
       "ceSctpAssocLocRecWndZeroCnt": ceSctpAssocLocRecWndZeroCnt,
       "ceSctpAssocRemRecWnd": ceSctpAssocRemRecWnd,
       "ceSctpAssocRemRecWndLowMark": ceSctpAssocRemRecWndLowMark,
       "ceSctpAssocRemRecWndZeroCnt": ceSctpAssocRemRecWndZeroCnt,
       "ceSctpAssocULPDatagramsQueued": ceSctpAssocULPDatagramsQueued,
       "ceSctpAssocULPDatagramsQueuedHigh": ceSctpAssocULPDatagramsQueuedHigh,
       "ceSctpAssocChecksumErrorCounter": ceSctpAssocChecksumErrorCounter,
       "ceSctpAssocBytesSent": ceSctpAssocBytesSent,
       "ceSctpAssocBytesRec": ceSctpAssocBytesRec,
       "ceSctpAssocChunksDiscarded": ceSctpAssocChunksDiscarded,
       "ceSctpAssocChunksRec": ceSctpAssocChunksRec,
       "ceSctpAssocChunksRecControl": ceSctpAssocChunksRecControl,
       "ceSctpAssocChunksRecOrdered": ceSctpAssocChunksRecOrdered,
       "ceSctpAssocChunksRecUnOrdered": ceSctpAssocChunksRecUnOrdered,
       "ceSctpAssocChunksRecOutOrder": ceSctpAssocChunksRecOutOrder,
       "ceSctpAssocChunksReTrans": ceSctpAssocChunksReTrans,
       "ceSctpAssocChunksSent": ceSctpAssocChunksSent,
       "ceSctpAssocChunksSentControl": ceSctpAssocChunksSentControl,
       "ceSctpAssocChunksSentOrdered": ceSctpAssocChunksSentOrdered,
       "ceSctpAssocChunksSentUnOrdered": ceSctpAssocChunksSentUnOrdered,
       "ceSctpAssocDatagramsRec": ceSctpAssocDatagramsRec,
       "ceSctpAssocDatagramsSent": ceSctpAssocDatagramsSent,
       "ceSctpAssocRowStatus": ceSctpAssocRowStatus,
       "ceSctpAssocLocalAddressTable": ceSctpAssocLocalAddressTable,
       "ceSctpAssocLocalAddressEntry": ceSctpAssocLocalAddressEntry,
       "ceSctpAssocLocalAddressIPType": ceSctpAssocLocalAddressIPType,
       "ceSctpAssocLocalAddressIP": ceSctpAssocLocalAddressIP,
       "ceSctpAssocLocalAddressRowStatus": ceSctpAssocLocalAddressRowStatus,
       "ceSctpAssocRemAddressTable": ceSctpAssocRemAddressTable,
       "ceSctpAssocRemAddressEntry": ceSctpAssocRemAddressEntry,
       "ceSctpAssocRemAddressIPType": ceSctpAssocRemAddressIPType,
       "ceSctpAssocRemAddressIP": ceSctpAssocRemAddressIP,
       "ceSctpAssocRemAddressStatus": ceSctpAssocRemAddressStatus,
       "ceSctpAssocRemAddressRTO": ceSctpAssocRemAddressRTO,
       "ceSctpAssocRemAddressHtBtFlag": ceSctpAssocRemAddressHtBtFlag,
       "ceSctpAssocRemAddressHtBtTime": ceSctpAssocRemAddressHtBtTime,
       "ceSctpAssocRemAddressMaxRetran": ceSctpAssocRemAddressMaxRetran,
       "ceSctpAssocRemAddressRetransCnt": ceSctpAssocRemAddressRetransCnt,
       "ceSctpAssocRemAddressSRTT": ceSctpAssocRemAddressSRTT,
       "ceSctpAssocRemAddressRowStatus": ceSctpAssocRemAddressRowStatus,
       "ceSctpConformance": ceSctpConformance,
       "ceSctpGroups": ceSctpGroups,
       "ceSctpGeneralVariablesGroup": ceSctpGeneralVariablesGroup,
       "ceSctpStateStatGroup": ceSctpStateStatGroup,
       "ceSctpOtherStatGroup": ceSctpOtherStatGroup,
       "ceSctpAssocTablesVariablesGroup": ceSctpAssocTablesVariablesGroup,
       "ceSctpAssocStatGroup": ceSctpAssocStatGroup,
       "ceSctpCompliances": ceSctpCompliances,
       "ceSctpCompliance": ceSctpCompliance}
)
