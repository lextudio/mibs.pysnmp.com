# SNMP MIB module (ATT-CNM-SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATT-CNM-SIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:18 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class SMDSAddress(OctetString):
    """Custom type SMDSAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Att_2_ObjectIdentity = ObjectIdentity
att_2 = _Att_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74)
)
_Att_products_ObjectIdentity = ObjectIdentity
att_products = _Att_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1)
)
_Att_cnmAgent_ObjectIdentity = ObjectIdentity
att_cnmAgent = _Att_cnmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 9)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Att_cnm_ObjectIdentity = ObjectIdentity
att_cnm = _Att_cnm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15)
)
_Att_cnm_sip_ObjectIdentity = ObjectIdentity
att_cnm_sip = _Att_cnm_sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5)
)
_AttCNMsipConfigTable_Object = MibTable
attCNMsipConfigTable = _AttCNMsipConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 1)
)
if mibBuilder.loadTexts:
    attCNMsipConfigTable.setStatus("mandatory")
_AttCNMsipConfigEntry_Object = MibTableRow
attCNMsipConfigEntry = _AttCNMsipConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 1, 1)
)
attCNMsipConfigEntry.setIndexNames(
    (0, "ATT-CNM-SIP-MIB", "attCNMsipConfigIndex"),
)
if mibBuilder.loadTexts:
    attCNMsipConfigEntry.setStatus("mandatory")
_AttCNMsipConfigIndex_Type = Integer32
_AttCNMsipConfigIndex_Object = MibTableColumn
attCNMsipConfigIndex = _AttCNMsipConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 1, 1, 1),
    _AttCNMsipConfigIndex_Type()
)
attCNMsipConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipConfigIndex.setStatus("mandatory")
_AttCNMsipMeasMaxIntervals_Type = Integer32
_AttCNMsipMeasMaxIntervals_Object = MibTableColumn
attCNMsipMeasMaxIntervals = _AttCNMsipMeasMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 1, 1, 2),
    _AttCNMsipMeasMaxIntervals_Type()
)
attCNMsipMeasMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipMeasMaxIntervals.setStatus("mandatory")
_AttCNMsipMeasIntervalLen_Type = Integer32
_AttCNMsipMeasIntervalLen_Object = MibTableColumn
attCNMsipMeasIntervalLen = _AttCNMsipMeasIntervalLen_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 1, 1, 3),
    _AttCNMsipMeasIntervalLen_Type()
)
attCNMsipMeasIntervalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipMeasIntervalLen.setStatus("mandatory")
_AttCNMsipMeasTable_Object = MibTable
attCNMsipMeasTable = _AttCNMsipMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2)
)
if mibBuilder.loadTexts:
    attCNMsipMeasTable.setStatus("mandatory")
_AttCNMsipMeasEntry_Object = MibTableRow
attCNMsipMeasEntry = _AttCNMsipMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1)
)
attCNMsipMeasEntry.setIndexNames(
    (0, "ATT-CNM-SIP-MIB", "attCNMsipMeasIndex"),
    (0, "ATT-CNM-SIP-MIB", "attCNMsipMeasInterval"),
)
if mibBuilder.loadTexts:
    attCNMsipMeasEntry.setStatus("mandatory")
_AttCNMsipMeasIndex_Type = Integer32
_AttCNMsipMeasIndex_Object = MibTableColumn
attCNMsipMeasIndex = _AttCNMsipMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 1),
    _AttCNMsipMeasIndex_Type()
)
attCNMsipMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipMeasIndex.setStatus("mandatory")
_AttCNMsipMeasInterval_Type = Integer32
_AttCNMsipMeasInterval_Object = MibTableColumn
attCNMsipMeasInterval = _AttCNMsipMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 2),
    _AttCNMsipMeasInterval_Type()
)
attCNMsipMeasInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipMeasInterval.setStatus("mandatory")
_AttCNMsipMeasTimeStamp_Type = Integer32
_AttCNMsipMeasTimeStamp_Object = MibTableColumn
attCNMsipMeasTimeStamp = _AttCNMsipMeasTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 3),
    _AttCNMsipMeasTimeStamp_Type()
)
attCNMsipMeasTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipMeasTimeStamp.setStatus("mandatory")


class _AttCNMsipMeasLocalTime_Type(DisplayString):
    """Custom type attCNMsipMeasLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsipMeasLocalTime_Type.__name__ = "DisplayString"
_AttCNMsipMeasLocalTime_Object = MibTableColumn
attCNMsipMeasLocalTime = _AttCNMsipMeasLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 4),
    _AttCNMsipMeasLocalTime_Type()
)
attCNMsipMeasLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipMeasLocalTime.setStatus("mandatory")
_AttCNMsipReceivedL3PDUs_Type = Gauge32
_AttCNMsipReceivedL3PDUs_Object = MibTableColumn
attCNMsipReceivedL3PDUs = _AttCNMsipReceivedL3PDUs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 5),
    _AttCNMsipReceivedL3PDUs_Type()
)
attCNMsipReceivedL3PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipReceivedL3PDUs.setStatus("mandatory")
_AttCNMsipSentL3PDUs_Type = Gauge32
_AttCNMsipSentL3PDUs_Object = MibTableColumn
attCNMsipSentL3PDUs = _AttCNMsipSentL3PDUs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 6),
    _AttCNMsipSentL3PDUs_Type()
)
attCNMsipSentL3PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipSentL3PDUs.setStatus("mandatory")
_AttCNMsipReceivedGroupL3PDUs_Type = Gauge32
_AttCNMsipReceivedGroupL3PDUs_Object = MibTableColumn
attCNMsipReceivedGroupL3PDUs = _AttCNMsipReceivedGroupL3PDUs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 7),
    _AttCNMsipReceivedGroupL3PDUs_Type()
)
attCNMsipReceivedGroupL3PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipReceivedGroupL3PDUs.setStatus("mandatory")
_AttCNMsipSentGroupL3PDUs_Type = Gauge32
_AttCNMsipSentGroupL3PDUs_Object = MibTableColumn
attCNMsipSentGroupL3PDUs = _AttCNMsipSentGroupL3PDUs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 8),
    _AttCNMsipSentGroupL3PDUs_Type()
)
attCNMsipSentGroupL3PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipSentGroupL3PDUs.setStatus("mandatory")
_AttCNMsipReceivedL2PDUs_Type = Gauge32
_AttCNMsipReceivedL2PDUs_Object = MibTableColumn
attCNMsipReceivedL2PDUs = _AttCNMsipReceivedL2PDUs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 9),
    _AttCNMsipReceivedL2PDUs_Type()
)
attCNMsipReceivedL2PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipReceivedL2PDUs.setStatus("mandatory")
_AttCNMsipSentL2PDUs_Type = Gauge32
_AttCNMsipSentL2PDUs_Object = MibTableColumn
attCNMsipSentL2PDUs = _AttCNMsipSentL2PDUs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 2, 1, 10),
    _AttCNMsipSentL2PDUs_Type()
)
attCNMsipSentL2PDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipSentL2PDUs.setStatus("mandatory")
_AttCNMsipL3ErrorLogTable_Object = MibTable
attCNMsipL3ErrorLogTable = _AttCNMsipL3ErrorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 3)
)
if mibBuilder.loadTexts:
    attCNMsipL3ErrorLogTable.setStatus("mandatory")
_AttCNMsipL3ErrorLogEntry_Object = MibTableRow
attCNMsipL3ErrorLogEntry = _AttCNMsipL3ErrorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 3, 1)
)
attCNMsipL3ErrorLogEntry.setIndexNames(
    (0, "ATT-CNM-SIP-MIB", "attCNMsipL3ErrorLogIndex"),
    (0, "ATT-CNM-SIP-MIB", "attCNMsipL3ErrorLogType"),
)
if mibBuilder.loadTexts:
    attCNMsipL3ErrorLogEntry.setStatus("mandatory")
_AttCNMsipL3ErrorLogIndex_Type = Integer32
_AttCNMsipL3ErrorLogIndex_Object = MibTableColumn
attCNMsipL3ErrorLogIndex = _AttCNMsipL3ErrorLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 3, 1, 1),
    _AttCNMsipL3ErrorLogIndex_Type()
)
attCNMsipL3ErrorLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipL3ErrorLogIndex.setStatus("mandatory")


class _AttCNMsipL3ErrorLogType_Type(Integer32):
    """Custom type attCNMsipL3ErrorLogType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("baSizeFieldNotEqualLengthField", 10),
          ("baSizeFieldValueInvalid", 3),
          ("beTagMismatch", 9),
          ("daFieldFormatError", 1),
          ("heCarrierSelectionElementInvalid", 7),
          ("heElementLengthInvalid", 5),
          ("heLengthInvalid", 4),
          ("hePADInvalid", 8),
          ("heVersionElementInvalid", 6),
          ("incorrectLength", 11),
          ("mriTimeout", 12),
          ("saFieldFormatError", 2))
    )


_AttCNMsipL3ErrorLogType_Type.__name__ = "Integer32"
_AttCNMsipL3ErrorLogType_Object = MibTableColumn
attCNMsipL3ErrorLogType = _AttCNMsipL3ErrorLogType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 3, 1, 2),
    _AttCNMsipL3ErrorLogType_Type()
)
attCNMsipL3ErrorLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipL3ErrorLogType.setStatus("mandatory")
_AttCNMsipL3ErrorLogSA_Type = SMDSAddress
_AttCNMsipL3ErrorLogSA_Object = MibTableColumn
attCNMsipL3ErrorLogSA = _AttCNMsipL3ErrorLogSA_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 3, 1, 3),
    _AttCNMsipL3ErrorLogSA_Type()
)
attCNMsipL3ErrorLogSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipL3ErrorLogSA.setStatus("mandatory")
_AttCNMsipL3ErrorLogDA_Type = SMDSAddress
_AttCNMsipL3ErrorLogDA_Object = MibTableColumn
attCNMsipL3ErrorLogDA = _AttCNMsipL3ErrorLogDA_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 3, 1, 4),
    _AttCNMsipL3ErrorLogDA_Type()
)
attCNMsipL3ErrorLogDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipL3ErrorLogDA.setStatus("mandatory")
_AttCNMsipL3ErrorLogTimeStamp_Type = Integer32
_AttCNMsipL3ErrorLogTimeStamp_Object = MibTableColumn
attCNMsipL3ErrorLogTimeStamp = _AttCNMsipL3ErrorLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 3, 1, 5),
    _AttCNMsipL3ErrorLogTimeStamp_Type()
)
attCNMsipL3ErrorLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipL3ErrorLogTimeStamp.setStatus("mandatory")


class _AttCNMsipL3ErrorLogLocalTime_Type(DisplayString):
    """Custom type attCNMsipL3ErrorLogLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsipL3ErrorLogLocalTime_Type.__name__ = "DisplayString"
_AttCNMsipL3ErrorLogLocalTime_Object = MibTableColumn
attCNMsipL3ErrorLogLocalTime = _AttCNMsipL3ErrorLogLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 5, 3, 1, 6),
    _AttCNMsipL3ErrorLogLocalTime_Type()
)
attCNMsipL3ErrorLogLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsipL3ErrorLogLocalTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATT-CNM-SIP-MIB",
    **{"SMDSAddress": SMDSAddress,
       "att-2": att_2,
       "att-products": att_products,
       "att-cnmAgent": att_cnmAgent,
       "att-mgmt": att_mgmt,
       "att-cnm": att_cnm,
       "att-cnm-sip": att_cnm_sip,
       "attCNMsipConfigTable": attCNMsipConfigTable,
       "attCNMsipConfigEntry": attCNMsipConfigEntry,
       "attCNMsipConfigIndex": attCNMsipConfigIndex,
       "attCNMsipMeasMaxIntervals": attCNMsipMeasMaxIntervals,
       "attCNMsipMeasIntervalLen": attCNMsipMeasIntervalLen,
       "attCNMsipMeasTable": attCNMsipMeasTable,
       "attCNMsipMeasEntry": attCNMsipMeasEntry,
       "attCNMsipMeasIndex": attCNMsipMeasIndex,
       "attCNMsipMeasInterval": attCNMsipMeasInterval,
       "attCNMsipMeasTimeStamp": attCNMsipMeasTimeStamp,
       "attCNMsipMeasLocalTime": attCNMsipMeasLocalTime,
       "attCNMsipReceivedL3PDUs": attCNMsipReceivedL3PDUs,
       "attCNMsipSentL3PDUs": attCNMsipSentL3PDUs,
       "attCNMsipReceivedGroupL3PDUs": attCNMsipReceivedGroupL3PDUs,
       "attCNMsipSentGroupL3PDUs": attCNMsipSentGroupL3PDUs,
       "attCNMsipReceivedL2PDUs": attCNMsipReceivedL2PDUs,
       "attCNMsipSentL2PDUs": attCNMsipSentL2PDUs,
       "attCNMsipL3ErrorLogTable": attCNMsipL3ErrorLogTable,
       "attCNMsipL3ErrorLogEntry": attCNMsipL3ErrorLogEntry,
       "attCNMsipL3ErrorLogIndex": attCNMsipL3ErrorLogIndex,
       "attCNMsipL3ErrorLogType": attCNMsipL3ErrorLogType,
       "attCNMsipL3ErrorLogSA": attCNMsipL3ErrorLogSA,
       "attCNMsipL3ErrorLogDA": attCNMsipL3ErrorLogDA,
       "attCNMsipL3ErrorLogTimeStamp": attCNMsipL3ErrorLogTimeStamp,
       "attCNMsipL3ErrorLogLocalTime": attCNMsipL3ErrorLogLocalTime}
)
