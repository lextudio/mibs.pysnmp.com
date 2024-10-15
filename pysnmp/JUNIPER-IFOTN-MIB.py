# SNMP MIB module (JUNIPER-IFOTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IFOTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:08 2024
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(JnxoptIfOTNOChAlarms,
 JnxoptIfOTNODUkTcmAlarms) = mibBuilder.importSymbols(
    "JNX-OPT-IF-EXT-MIB",
    "JnxoptIfOTNOChAlarms",
    "JnxoptIfOTNODUkTcmAlarms")

(jnxIfOtnMibRoot,
 jnxIfOtnNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxIfOtnMibRoot",
    "jnxIfOtnNotifications")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxIfOtnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1)
)
jnxIfOtnMib.setRevisions(
        ("2016-09-12 20:15",
         "2015-06-24 12:27",
         "2012-01-27 00:00",
         "2012-01-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxIfAdminStates(Integer32, TextualConvention):
    status = "current"
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
        *(("jnxAdminStateInService", 1),
          ("jnxAdminStateInServiceMA", 2),
          ("jnxAdminStateOutofService", 3),
          ("jnxAdminStateOutofServiceMA", 4))
    )



class JnxIfOperStates(Integer32, TextualConvention):
    status = "current"
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
        *(("jnxOperStateDegraded", 4),
          ("jnxOperStateFault", 3),
          ("jnxOperStateInit", 1),
          ("jnxOperStateNormal", 2))
    )



class JnxIfOtnRate(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("otu0", 1),
          ("otu1", 2),
          ("otu1e", 7),
          ("otu2", 3),
          ("otu2e", 4),
          ("otu3", 5),
          ("otu4", 6),
          ("otu5", 8))
    )



class JnxIfOtnFecType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("efecI2", 2),
          ("efecI3", 3),
          ("efecI4", 4),
          ("efecI5", 5),
          ("efecI6", 6),
          ("efecI7", 7),
          ("efecI8", 8),
          ("efecI9", 9),
          ("gfec", 1),
          ("gfecandsdfec", 10),
          ("hgfec", 12),
          ("nofec", 0),
          ("sdfec", 11))
    )



class JnxIfOtnLayer(Integer32, TextualConvention):
    status = "current"
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
        *(("jnxODUk", 3),
          ("jnxOTUk", 2),
          ("jnxOch", 1),
          ("jnxTCM", 4))
    )



class JnxIfOtnType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jnxFarEnd", 2),
          ("jnxNearEnd", 1))
    )



class JnxIfOtnDirection(Integer32, TextualConvention):
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
        *(("jnxBiDir", 3),
          ("jnxRxDir", 2),
          ("jnxTxDir", 1))
    )



class JnxIfOtnSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("jnxCritical", 1),
          ("jnxInfo", 4),
          ("jnxMajor", 2),
          ("jnxMinor", 3))
    )



class JnxIfOtnServiceStateAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jnxNonServiceAffecting", 1),
          ("jnxNotSupported", 0),
          ("jnxServiceAffecting", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JnxIfOtn_ObjectIdentity = ObjectIdentity
jnxIfOtn = _JnxIfOtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1)
)
_JnxIfOtnOChCfgTable_Object = MibTable
jnxIfOtnOChCfgTable = _JnxIfOtnOChCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxIfOtnOChCfgTable.setStatus("current")
_JnxIfOtnOChCfgEntry_Object = MibTableRow
jnxIfOtnOChCfgEntry = _JnxIfOtnOChCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1)
)
jnxIfOtnOChCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOChCfgContainerIndex"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOChCfgL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOChCfgL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOChCfgL3Index"),
)
if mibBuilder.loadTexts:
    jnxIfOtnOChCfgEntry.setStatus("current")


class _JnxIfOtnOChCfgContainerIndex_Type(Integer32):
    """Custom type jnxIfOtnOChCfgContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOChCfgContainerIndex_Type.__name__ = "Integer32"
_JnxIfOtnOChCfgContainerIndex_Object = MibTableColumn
jnxIfOtnOChCfgContainerIndex = _JnxIfOtnOChCfgContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 1),
    _JnxIfOtnOChCfgContainerIndex_Type()
)
jnxIfOtnOChCfgContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOChCfgContainerIndex.setStatus("current")


class _JnxIfOtnOChCfgL1Index_Type(Integer32):
    """Custom type jnxIfOtnOChCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOChCfgL1Index_Type.__name__ = "Integer32"
_JnxIfOtnOChCfgL1Index_Object = MibTableColumn
jnxIfOtnOChCfgL1Index = _JnxIfOtnOChCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 2),
    _JnxIfOtnOChCfgL1Index_Type()
)
jnxIfOtnOChCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOChCfgL1Index.setStatus("current")


class _JnxIfOtnOChCfgL2Index_Type(Integer32):
    """Custom type jnxIfOtnOChCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOChCfgL2Index_Type.__name__ = "Integer32"
_JnxIfOtnOChCfgL2Index_Object = MibTableColumn
jnxIfOtnOChCfgL2Index = _JnxIfOtnOChCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 3),
    _JnxIfOtnOChCfgL2Index_Type()
)
jnxIfOtnOChCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOChCfgL2Index.setStatus("current")


class _JnxIfOtnOChCfgL3Index_Type(Integer32):
    """Custom type jnxIfOtnOChCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOChCfgL3Index_Type.__name__ = "Integer32"
_JnxIfOtnOChCfgL3Index_Object = MibTableColumn
jnxIfOtnOChCfgL3Index = _JnxIfOtnOChCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 4),
    _JnxIfOtnOChCfgL3Index_Type()
)
jnxIfOtnOChCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOChCfgL3Index.setStatus("current")
_JnxIfOtnLocalLoopback_Type = TruthValue
_JnxIfOtnLocalLoopback_Object = MibTableColumn
jnxIfOtnLocalLoopback = _JnxIfOtnLocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 5),
    _JnxIfOtnLocalLoopback_Type()
)
jnxIfOtnLocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnLocalLoopback.setStatus("current")
_JnxIfOtnLineLoopback_Type = TruthValue
_JnxIfOtnLineLoopback_Object = MibTableColumn
jnxIfOtnLineLoopback = _JnxIfOtnLineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 6),
    _JnxIfOtnLineLoopback_Type()
)
jnxIfOtnLineLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnLineLoopback.setStatus("current")
_JnxIfOtnPayloadLoopback_Type = TruthValue
_JnxIfOtnPayloadLoopback_Object = MibTableColumn
jnxIfOtnPayloadLoopback = _JnxIfOtnPayloadLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 7),
    _JnxIfOtnPayloadLoopback_Type()
)
jnxIfOtnPayloadLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnPayloadLoopback.setStatus("current")
_JnxIfOtnAdminState_Type = JnxIfAdminStates
_JnxIfOtnAdminState_Object = MibTableColumn
jnxIfOtnAdminState = _JnxIfOtnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 8),
    _JnxIfOtnAdminState_Type()
)
jnxIfOtnAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnAdminState.setStatus("current")
_JnxIfOtnOperState_Type = JnxIfOperStates
_JnxIfOtnOperState_Object = MibTableColumn
jnxIfOtnOperState = _JnxIfOtnOperState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 9),
    _JnxIfOtnOperState_Type()
)
jnxIfOtnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOperState.setStatus("current")
_JnxIfOtnIndex_Type = Unsigned32
_JnxIfOtnIndex_Object = MibTableColumn
jnxIfOtnIndex = _JnxIfOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 10),
    _JnxIfOtnIndex_Type()
)
jnxIfOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnIndex.setStatus("current")


class _JnxIfOtnOChStatus_Type(Bits):
    """Custom type jnxIfOtnOChStatus based on Bits"""
    namedValues = NamedValues(
        *(("lof", 1),
          ("lom", 2),
          ("los", 0),
          ("wavelengthlockerr", 3))
    )

_JnxIfOtnOChStatus_Type.__name__ = "Bits"
_JnxIfOtnOChStatus_Object = MibTableColumn
jnxIfOtnOChStatus = _JnxIfOtnOChStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 11),
    _JnxIfOtnOChStatus_Type()
)
jnxIfOtnOChStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOChStatus.setStatus("current")
_JnxIfOtnOChPortMode_Type = Unsigned32
_JnxIfOtnOChPortMode_Object = MibTableColumn
jnxIfOtnOChPortMode = _JnxIfOtnOChPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 1, 1, 12),
    _JnxIfOtnOChPortMode_Type()
)
jnxIfOtnOChPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOChPortMode.setStatus("current")
_JnxIfOtnOTUkCfgTable_Object = MibTable
jnxIfOtnOTUkCfgTable = _JnxIfOtnOTUkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxIfOtnOTUkCfgTable.setStatus("current")
_JnxIfOtnOTUkCfgEntry_Object = MibTableRow
jnxIfOtnOTUkCfgEntry = _JnxIfOtnOTUkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1)
)
jnxIfOtnOTUkCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOTUkCfgContainerIndex"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOTUkCfgL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOTUkCfgL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOTUkCfgL3Index"),
)
if mibBuilder.loadTexts:
    jnxIfOtnOTUkCfgEntry.setStatus("current")


class _JnxIfOtnOTUkCfgContainerIndex_Type(Integer32):
    """Custom type jnxIfOtnOTUkCfgContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOTUkCfgContainerIndex_Type.__name__ = "Integer32"
_JnxIfOtnOTUkCfgContainerIndex_Object = MibTableColumn
jnxIfOtnOTUkCfgContainerIndex = _JnxIfOtnOTUkCfgContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 1),
    _JnxIfOtnOTUkCfgContainerIndex_Type()
)
jnxIfOtnOTUkCfgContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkCfgContainerIndex.setStatus("current")


class _JnxIfOtnOTUkCfgL1Index_Type(Integer32):
    """Custom type jnxIfOtnOTUkCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOTUkCfgL1Index_Type.__name__ = "Integer32"
_JnxIfOtnOTUkCfgL1Index_Object = MibTableColumn
jnxIfOtnOTUkCfgL1Index = _JnxIfOtnOTUkCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 2),
    _JnxIfOtnOTUkCfgL1Index_Type()
)
jnxIfOtnOTUkCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkCfgL1Index.setStatus("current")


class _JnxIfOtnOTUkCfgL2Index_Type(Integer32):
    """Custom type jnxIfOtnOTUkCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOTUkCfgL2Index_Type.__name__ = "Integer32"
_JnxIfOtnOTUkCfgL2Index_Object = MibTableColumn
jnxIfOtnOTUkCfgL2Index = _JnxIfOtnOTUkCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 3),
    _JnxIfOtnOTUkCfgL2Index_Type()
)
jnxIfOtnOTUkCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkCfgL2Index.setStatus("current")


class _JnxIfOtnOTUkCfgL3Index_Type(Integer32):
    """Custom type jnxIfOtnOTUkCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOTUkCfgL3Index_Type.__name__ = "Integer32"
_JnxIfOtnOTUkCfgL3Index_Object = MibTableColumn
jnxIfOtnOTUkCfgL3Index = _JnxIfOtnOTUkCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 4),
    _JnxIfOtnOTUkCfgL3Index_Type()
)
jnxIfOtnOTUkCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkCfgL3Index.setStatus("current")
_JnxIfOtnOTUkCfgRate_Type = JnxIfOtnRate
_JnxIfOtnOTUkCfgRate_Object = MibTableColumn
jnxIfOtnOTUkCfgRate = _JnxIfOtnOTUkCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 5),
    _JnxIfOtnOTUkCfgRate_Type()
)
jnxIfOtnOTUkCfgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkCfgRate.setStatus("current")
_JnxIfOtnOTUkCfgFecMode_Type = JnxIfOtnFecType
_JnxIfOtnOTUkCfgFecMode_Object = MibTableColumn
jnxIfOtnOTUkCfgFecMode = _JnxIfOtnOTUkCfgFecMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 6),
    _JnxIfOtnOTUkCfgFecMode_Type()
)
jnxIfOtnOTUkCfgFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkCfgFecMode.setStatus("current")
_JnxIfOtnOTUkEnableAutoFrrByteInsert_Type = TruthValue
_JnxIfOtnOTUkEnableAutoFrrByteInsert_Object = MibTableColumn
jnxIfOtnOTUkEnableAutoFrrByteInsert = _JnxIfOtnOTUkEnableAutoFrrByteInsert_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 7),
    _JnxIfOtnOTUkEnableAutoFrrByteInsert_Type()
)
jnxIfOtnOTUkEnableAutoFrrByteInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkEnableAutoFrrByteInsert.setStatus("current")
_JnxIfOtnOTUkEnableBERFrrSupport_Type = TruthValue
_JnxIfOtnOTUkEnableBERFrrSupport_Object = MibTableColumn
jnxIfOtnOTUkEnableBERFrrSupport = _JnxIfOtnOTUkEnableBERFrrSupport_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 8),
    _JnxIfOtnOTUkEnableBERFrrSupport_Type()
)
jnxIfOtnOTUkEnableBERFrrSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkEnableBERFrrSupport.setStatus("current")
_JnxIfOtnOTUkPreFecBERThresholdMantissa_Type = Integer32
_JnxIfOtnOTUkPreFecBERThresholdMantissa_Object = MibTableColumn
jnxIfOtnOTUkPreFecBERThresholdMantissa = _JnxIfOtnOTUkPreFecBERThresholdMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 9),
    _JnxIfOtnOTUkPreFecBERThresholdMantissa_Type()
)
jnxIfOtnOTUkPreFecBERThresholdMantissa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkPreFecBERThresholdMantissa.setStatus("current")
_JnxIfOtnOTUkPreFecBERThresholdExponent_Type = Integer32
_JnxIfOtnOTUkPreFecBERThresholdExponent_Object = MibTableColumn
jnxIfOtnOTUkPreFecBERThresholdExponent = _JnxIfOtnOTUkPreFecBERThresholdExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 10),
    _JnxIfOtnOTUkPreFecBERThresholdExponent_Type()
)
jnxIfOtnOTUkPreFecBERThresholdExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkPreFecBERThresholdExponent.setStatus("current")
_JnxIfOtnOTUkPreFecBERThresholdTime_Type = Integer32
_JnxIfOtnOTUkPreFecBERThresholdTime_Object = MibTableColumn
jnxIfOtnOTUkPreFecBERThresholdTime = _JnxIfOtnOTUkPreFecBERThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 11),
    _JnxIfOtnOTUkPreFecBERThresholdTime_Type()
)
jnxIfOtnOTUkPreFecBERThresholdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkPreFecBERThresholdTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkPreFecBERThresholdTime.setUnits("ms")
_JnxIfOtnOTUkTIMActEnabled_Type = TruthValue
_JnxIfOtnOTUkTIMActEnabled_Object = MibTableColumn
jnxIfOtnOTUkTIMActEnabled = _JnxIfOtnOTUkTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 12),
    _JnxIfOtnOTUkTIMActEnabled_Type()
)
jnxIfOtnOTUkTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkTIMActEnabled.setStatus("current")


class _JnxIfOtnOTUkTxTTI_Type(OctetString):
    """Custom type jnxIfOtnOTUkTxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxIfOtnOTUkTxTTI_Type.__name__ = "OctetString"
_JnxIfOtnOTUkTxTTI_Object = MibTableColumn
jnxIfOtnOTUkTxTTI = _JnxIfOtnOTUkTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 13),
    _JnxIfOtnOTUkTxTTI_Type()
)
jnxIfOtnOTUkTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkTxTTI.setStatus("current")


class _JnxIfOtnOTUkRxTTI_Type(OctetString):
    """Custom type jnxIfOtnOTUkRxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_JnxIfOtnOTUkRxTTI_Type.__name__ = "OctetString"
_JnxIfOtnOTUkRxTTI_Object = MibTableColumn
jnxIfOtnOTUkRxTTI = _JnxIfOtnOTUkRxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 14),
    _JnxIfOtnOTUkRxTTI_Type()
)
jnxIfOtnOTUkRxTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkRxTTI.setStatus("current")


class _JnxIfOtnOTUkExpectedRxSapi_Type(OctetString):
    """Custom type jnxIfOtnOTUkExpectedRxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnOTUkExpectedRxSapi_Type.__name__ = "OctetString"
_JnxIfOtnOTUkExpectedRxSapi_Object = MibTableColumn
jnxIfOtnOTUkExpectedRxSapi = _JnxIfOtnOTUkExpectedRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 15),
    _JnxIfOtnOTUkExpectedRxSapi_Type()
)
jnxIfOtnOTUkExpectedRxSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkExpectedRxSapi.setStatus("current")


class _JnxIfOtnOTUkExpectedRxDapi_Type(OctetString):
    """Custom type jnxIfOtnOTUkExpectedRxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnOTUkExpectedRxDapi_Type.__name__ = "OctetString"
_JnxIfOtnOTUkExpectedRxDapi_Object = MibTableColumn
jnxIfOtnOTUkExpectedRxDapi = _JnxIfOtnOTUkExpectedRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 16),
    _JnxIfOtnOTUkExpectedRxDapi_Type()
)
jnxIfOtnOTUkExpectedRxDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkExpectedRxDapi.setStatus("current")


class _JnxIfOtnOTUkStatus_Type(Bits):
    """Custom type jnxIfOtnOTUkStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 0),
          ("bdi", 1),
          ("biae", 6),
          ("fecdegrade", 10),
          ("fecexcessive", 9),
          ("iae", 2),
          ("sd", 5),
          ("sf", 4),
          ("ssf", 8),
          ("tsf", 7),
          ("ttim", 3))
    )

_JnxIfOtnOTUkStatus_Type.__name__ = "Bits"
_JnxIfOtnOTUkStatus_Object = MibTableColumn
jnxIfOtnOTUkStatus = _JnxIfOtnOTUkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 17),
    _JnxIfOtnOTUkStatus_Type()
)
jnxIfOtnOTUkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkStatus.setStatus("current")
_JnxIfOtnOTUkPreFecBERThresholdClearMantissa_Type = Integer32
_JnxIfOtnOTUkPreFecBERThresholdClearMantissa_Object = MibTableColumn
jnxIfOtnOTUkPreFecBERThresholdClearMantissa = _JnxIfOtnOTUkPreFecBERThresholdClearMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 18),
    _JnxIfOtnOTUkPreFecBERThresholdClearMantissa_Type()
)
jnxIfOtnOTUkPreFecBERThresholdClearMantissa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkPreFecBERThresholdClearMantissa.setStatus("current")
_JnxIfOtnOTUkPreFecBERThresholdClearExponent_Type = Integer32
_JnxIfOtnOTUkPreFecBERThresholdClearExponent_Object = MibTableColumn
jnxIfOtnOTUkPreFecBERThresholdClearExponent = _JnxIfOtnOTUkPreFecBERThresholdClearExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 2, 1, 19),
    _JnxIfOtnOTUkPreFecBERThresholdClearExponent_Type()
)
jnxIfOtnOTUkPreFecBERThresholdClearExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOTUkPreFecBERThresholdClearExponent.setStatus("current")
_JnxIfOtnODUkCfgTable_Object = MibTable
jnxIfOtnODUkCfgTable = _JnxIfOtnODUkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxIfOtnODUkCfgTable.setStatus("current")
_JnxIfOtnODUkCfgEntry_Object = MibTableRow
jnxIfOtnODUkCfgEntry = _JnxIfOtnODUkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1)
)
jnxIfOtnODUkCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnODUkCfgContainerIndex"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnODUkCfgL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnODUkCfgL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnODUkCfgL3Index"),
)
if mibBuilder.loadTexts:
    jnxIfOtnODUkCfgEntry.setStatus("current")


class _JnxIfOtnODUkCfgContainerIndex_Type(Integer32):
    """Custom type jnxIfOtnODUkCfgContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnODUkCfgContainerIndex_Type.__name__ = "Integer32"
_JnxIfOtnODUkCfgContainerIndex_Object = MibTableColumn
jnxIfOtnODUkCfgContainerIndex = _JnxIfOtnODUkCfgContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 1),
    _JnxIfOtnODUkCfgContainerIndex_Type()
)
jnxIfOtnODUkCfgContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnODUkCfgContainerIndex.setStatus("current")


class _JnxIfOtnODUkCfgL1Index_Type(Integer32):
    """Custom type jnxIfOtnODUkCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnODUkCfgL1Index_Type.__name__ = "Integer32"
_JnxIfOtnODUkCfgL1Index_Object = MibTableColumn
jnxIfOtnODUkCfgL1Index = _JnxIfOtnODUkCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 2),
    _JnxIfOtnODUkCfgL1Index_Type()
)
jnxIfOtnODUkCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnODUkCfgL1Index.setStatus("current")


class _JnxIfOtnODUkCfgL2Index_Type(Integer32):
    """Custom type jnxIfOtnODUkCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnODUkCfgL2Index_Type.__name__ = "Integer32"
_JnxIfOtnODUkCfgL2Index_Object = MibTableColumn
jnxIfOtnODUkCfgL2Index = _JnxIfOtnODUkCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 3),
    _JnxIfOtnODUkCfgL2Index_Type()
)
jnxIfOtnODUkCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnODUkCfgL2Index.setStatus("current")


class _JnxIfOtnODUkCfgL3Index_Type(Integer32):
    """Custom type jnxIfOtnODUkCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnODUkCfgL3Index_Type.__name__ = "Integer32"
_JnxIfOtnODUkCfgL3Index_Object = MibTableColumn
jnxIfOtnODUkCfgL3Index = _JnxIfOtnODUkCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 4),
    _JnxIfOtnODUkCfgL3Index_Type()
)
jnxIfOtnODUkCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnODUkCfgL3Index.setStatus("current")


class _JnxIfOtnODUkAPSPCC0_Type(Integer32):
    """Custom type jnxIfOtnODUkAPSPCC0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnODUkAPSPCC0_Type.__name__ = "Integer32"
_JnxIfOtnODUkAPSPCC0_Object = MibTableColumn
jnxIfOtnODUkAPSPCC0 = _JnxIfOtnODUkAPSPCC0_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 5),
    _JnxIfOtnODUkAPSPCC0_Type()
)
jnxIfOtnODUkAPSPCC0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkAPSPCC0.setStatus("current")


class _JnxIfOtnODUkAPSPCC1_Type(Integer32):
    """Custom type jnxIfOtnODUkAPSPCC1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnODUkAPSPCC1_Type.__name__ = "Integer32"
_JnxIfOtnODUkAPSPCC1_Object = MibTableColumn
jnxIfOtnODUkAPSPCC1 = _JnxIfOtnODUkAPSPCC1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 6),
    _JnxIfOtnODUkAPSPCC1_Type()
)
jnxIfOtnODUkAPSPCC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkAPSPCC1.setStatus("current")


class _JnxIfOtnODUkAPSPCC2_Type(Integer32):
    """Custom type jnxIfOtnODUkAPSPCC2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnODUkAPSPCC2_Type.__name__ = "Integer32"
_JnxIfOtnODUkAPSPCC2_Object = MibTableColumn
jnxIfOtnODUkAPSPCC2 = _JnxIfOtnODUkAPSPCC2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 7),
    _JnxIfOtnODUkAPSPCC2_Type()
)
jnxIfOtnODUkAPSPCC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkAPSPCC2.setStatus("current")


class _JnxIfOtnODUkAPSPCC3_Type(Integer32):
    """Custom type jnxIfOtnODUkAPSPCC3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnODUkAPSPCC3_Type.__name__ = "Integer32"
_JnxIfOtnODUkAPSPCC3_Object = MibTableColumn
jnxIfOtnODUkAPSPCC3 = _JnxIfOtnODUkAPSPCC3_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 8),
    _JnxIfOtnODUkAPSPCC3_Type()
)
jnxIfOtnODUkAPSPCC3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkAPSPCC3.setStatus("current")


class _JnxIfOtnODUkPayloadType_Type(Integer32):
    """Custom type jnxIfOtnODUkPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnODUkPayloadType_Type.__name__ = "Integer32"
_JnxIfOtnODUkPayloadType_Object = MibTableColumn
jnxIfOtnODUkPayloadType = _JnxIfOtnODUkPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 9),
    _JnxIfOtnODUkPayloadType_Type()
)
jnxIfOtnODUkPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkPayloadType.setStatus("current")
_JnxIfOtnODUkTIMActEnabled_Type = TruthValue
_JnxIfOtnODUkTIMActEnabled_Object = MibTableColumn
jnxIfOtnODUkTIMActEnabled = _JnxIfOtnODUkTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 10),
    _JnxIfOtnODUkTIMActEnabled_Type()
)
jnxIfOtnODUkTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTIMActEnabled.setStatus("current")


class _JnxIfOtnODUkTxTTI_Type(OctetString):
    """Custom type jnxIfOtnODUkTxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxIfOtnODUkTxTTI_Type.__name__ = "OctetString"
_JnxIfOtnODUkTxTTI_Object = MibTableColumn
jnxIfOtnODUkTxTTI = _JnxIfOtnODUkTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 11),
    _JnxIfOtnODUkTxTTI_Type()
)
jnxIfOtnODUkTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTxTTI.setStatus("current")


class _JnxIfOtnODUkRxTTI_Type(OctetString):
    """Custom type jnxIfOtnODUkRxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_JnxIfOtnODUkRxTTI_Type.__name__ = "OctetString"
_JnxIfOtnODUkRxTTI_Object = MibTableColumn
jnxIfOtnODUkRxTTI = _JnxIfOtnODUkRxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 12),
    _JnxIfOtnODUkRxTTI_Type()
)
jnxIfOtnODUkRxTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnODUkRxTTI.setStatus("current")


class _JnxIfOtnODUkExpectedRxSapi_Type(OctetString):
    """Custom type jnxIfOtnODUkExpectedRxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnODUkExpectedRxSapi_Type.__name__ = "OctetString"
_JnxIfOtnODUkExpectedRxSapi_Object = MibTableColumn
jnxIfOtnODUkExpectedRxSapi = _JnxIfOtnODUkExpectedRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 13),
    _JnxIfOtnODUkExpectedRxSapi_Type()
)
jnxIfOtnODUkExpectedRxSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkExpectedRxSapi.setStatus("current")


class _JnxIfOtnODUkExpectedRxDapi_Type(OctetString):
    """Custom type jnxIfOtnODUkExpectedRxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnODUkExpectedRxDapi_Type.__name__ = "OctetString"
_JnxIfOtnODUkExpectedRxDapi_Object = MibTableColumn
jnxIfOtnODUkExpectedRxDapi = _JnxIfOtnODUkExpectedRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 14),
    _JnxIfOtnODUkExpectedRxDapi_Type()
)
jnxIfOtnODUkExpectedRxDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkExpectedRxDapi.setStatus("current")


class _JnxIfOtnODUkStatus_Type(Bits):
    """Custom type jnxIfOtnODUkStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 0),
          ("bdi", 1),
          ("biae", 6),
          ("csf", 9),
          ("iae", 2),
          ("lck", 11),
          ("ltc", 12),
          ("oci", 10),
          ("ptm", 13),
          ("sd", 5),
          ("sf", 4),
          ("ssf", 8),
          ("tsf", 7),
          ("ttim", 3))
    )

_JnxIfOtnODUkStatus_Type.__name__ = "Bits"
_JnxIfOtnODUkStatus_Object = MibTableColumn
jnxIfOtnODUkStatus = _JnxIfOtnODUkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 15),
    _JnxIfOtnODUkStatus_Type()
)
jnxIfOtnODUkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnODUkStatus.setStatus("current")


class _JnxIfOtnODUkRxPayloadType_Type(Integer32):
    """Custom type jnxIfOtnODUkRxPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnODUkRxPayloadType_Type.__name__ = "Integer32"
_JnxIfOtnODUkRxPayloadType_Object = MibTableColumn
jnxIfOtnODUkRxPayloadType = _JnxIfOtnODUkRxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 3, 1, 16),
    _JnxIfOtnODUkRxPayloadType_Type()
)
jnxIfOtnODUkRxPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnODUkRxPayloadType.setStatus("current")
_JnxIfOtnTcmCfgTable_Object = MibTable
jnxIfOtnTcmCfgTable = _JnxIfOtnTcmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxIfOtnTcmCfgTable.setStatus("current")
_JnxIfOtnTcmCfgEntry_Object = MibTableRow
jnxIfOtnTcmCfgEntry = _JnxIfOtnTcmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1)
)
jnxIfOtnTcmCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnTcmCfgContainerIndex"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnTcmCfgL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnTcmCfgL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnTcmCfgL3Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnTcmCfgLevel"),
)
if mibBuilder.loadTexts:
    jnxIfOtnTcmCfgEntry.setStatus("current")


class _JnxIfOtnTcmCfgContainerIndex_Type(Integer32):
    """Custom type jnxIfOtnTcmCfgContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnTcmCfgContainerIndex_Type.__name__ = "Integer32"
_JnxIfOtnTcmCfgContainerIndex_Object = MibTableColumn
jnxIfOtnTcmCfgContainerIndex = _JnxIfOtnTcmCfgContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 1),
    _JnxIfOtnTcmCfgContainerIndex_Type()
)
jnxIfOtnTcmCfgContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnTcmCfgContainerIndex.setStatus("current")


class _JnxIfOtnTcmCfgL1Index_Type(Integer32):
    """Custom type jnxIfOtnTcmCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnTcmCfgL1Index_Type.__name__ = "Integer32"
_JnxIfOtnTcmCfgL1Index_Object = MibTableColumn
jnxIfOtnTcmCfgL1Index = _JnxIfOtnTcmCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 2),
    _JnxIfOtnTcmCfgL1Index_Type()
)
jnxIfOtnTcmCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnTcmCfgL1Index.setStatus("current")


class _JnxIfOtnTcmCfgL2Index_Type(Integer32):
    """Custom type jnxIfOtnTcmCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnTcmCfgL2Index_Type.__name__ = "Integer32"
_JnxIfOtnTcmCfgL2Index_Object = MibTableColumn
jnxIfOtnTcmCfgL2Index = _JnxIfOtnTcmCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 3),
    _JnxIfOtnTcmCfgL2Index_Type()
)
jnxIfOtnTcmCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnTcmCfgL2Index.setStatus("current")


class _JnxIfOtnTcmCfgL3Index_Type(Integer32):
    """Custom type jnxIfOtnTcmCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnTcmCfgL3Index_Type.__name__ = "Integer32"
_JnxIfOtnTcmCfgL3Index_Object = MibTableColumn
jnxIfOtnTcmCfgL3Index = _JnxIfOtnTcmCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 4),
    _JnxIfOtnTcmCfgL3Index_Type()
)
jnxIfOtnTcmCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnTcmCfgL3Index.setStatus("current")


class _JnxIfOtnTcmCfgLevel_Type(Integer32):
    """Custom type jnxIfOtnTcmCfgLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_JnxIfOtnTcmCfgLevel_Type.__name__ = "Integer32"
_JnxIfOtnTcmCfgLevel_Object = MibTableColumn
jnxIfOtnTcmCfgLevel = _JnxIfOtnTcmCfgLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 5),
    _JnxIfOtnTcmCfgLevel_Type()
)
jnxIfOtnTcmCfgLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnTcmCfgLevel.setStatus("current")
_JnxIfOtnTCMEnable_Type = TruthValue
_JnxIfOtnTCMEnable_Object = MibTableColumn
jnxIfOtnTCMEnable = _JnxIfOtnTCMEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 6),
    _JnxIfOtnTCMEnable_Type()
)
jnxIfOtnTCMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnTCMEnable.setStatus("current")


class _JnxIfOtnTcmTxTTI_Type(OctetString):
    """Custom type jnxIfOtnTcmTxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxIfOtnTcmTxTTI_Type.__name__ = "OctetString"
_JnxIfOtnTcmTxTTI_Object = MibTableColumn
jnxIfOtnTcmTxTTI = _JnxIfOtnTcmTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 7),
    _JnxIfOtnTcmTxTTI_Type()
)
jnxIfOtnTcmTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnTcmTxTTI.setStatus("current")


class _JnxIfOtnTcmRxTTI_Type(OctetString):
    """Custom type jnxIfOtnTcmRxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_JnxIfOtnTcmRxTTI_Type.__name__ = "OctetString"
_JnxIfOtnTcmRxTTI_Object = MibTableColumn
jnxIfOtnTcmRxTTI = _JnxIfOtnTcmRxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 8),
    _JnxIfOtnTcmRxTTI_Type()
)
jnxIfOtnTcmRxTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnTcmRxTTI.setStatus("current")


class _JnxIfOtnTcmExpectedRxSapi_Type(OctetString):
    """Custom type jnxIfOtnTcmExpectedRxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnTcmExpectedRxSapi_Type.__name__ = "OctetString"
_JnxIfOtnTcmExpectedRxSapi_Object = MibTableColumn
jnxIfOtnTcmExpectedRxSapi = _JnxIfOtnTcmExpectedRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 9),
    _JnxIfOtnTcmExpectedRxSapi_Type()
)
jnxIfOtnTcmExpectedRxSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnTcmExpectedRxSapi.setStatus("current")


class _JnxIfOtnTcmExpectedRxDapi_Type(OctetString):
    """Custom type jnxIfOtnTcmExpectedRxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnTcmExpectedRxDapi_Type.__name__ = "OctetString"
_JnxIfOtnTcmExpectedRxDapi_Object = MibTableColumn
jnxIfOtnTcmExpectedRxDapi = _JnxIfOtnTcmExpectedRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 10),
    _JnxIfOtnTcmExpectedRxDapi_Type()
)
jnxIfOtnTcmExpectedRxDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnTcmExpectedRxDapi.setStatus("current")


class _JnxIfOtnTcmStatus_Type(Bits):
    """Custom type jnxIfOtnTcmStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 0),
          ("bdi", 1),
          ("biae", 6),
          ("iae", 2),
          ("ltc", 9),
          ("ssf", 8),
          ("tsf", 7),
          ("ttim", 3))
    )

_JnxIfOtnTcmStatus_Type.__name__ = "Bits"
_JnxIfOtnTcmStatus_Object = MibTableColumn
jnxIfOtnTcmStatus = _JnxIfOtnTcmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 4, 1, 11),
    _JnxIfOtnTcmStatus_Type()
)
jnxIfOtnTcmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnTcmStatus.setStatus("current")
_JnxIfOtnODUkTcmTestTable_Object = MibTable
jnxIfOtnODUkTcmTestTable = _JnxIfOtnODUkTcmTestTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmTestTable.setStatus("current")
_JnxIfOtnODUkTcmTestEntry_Object = MibTableRow
jnxIfOtnODUkTcmTestEntry = _JnxIfOtnODUkTcmTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5, 1)
)
jnxIfOtnODUkTcmTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnODUkTcmTestLayer"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnODUkTcmTestTCMLevel"),
)
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmTestEntry.setStatus("current")
_JnxIfOtnODUkTcmTestLayer_Type = JnxIfOtnLayer
_JnxIfOtnODUkTcmTestLayer_Object = MibTableColumn
jnxIfOtnODUkTcmTestLayer = _JnxIfOtnODUkTcmTestLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5, 1, 1),
    _JnxIfOtnODUkTcmTestLayer_Type()
)
jnxIfOtnODUkTcmTestLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmTestLayer.setStatus("current")


class _JnxIfOtnODUkTcmTestTCMLevel_Type(Integer32):
    """Custom type jnxIfOtnODUkTcmTestTCMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_JnxIfOtnODUkTcmTestTCMLevel_Type.__name__ = "Integer32"
_JnxIfOtnODUkTcmTestTCMLevel_Object = MibTableColumn
jnxIfOtnODUkTcmTestTCMLevel = _JnxIfOtnODUkTcmTestTCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5, 1, 2),
    _JnxIfOtnODUkTcmTestTCMLevel_Type()
)
jnxIfOtnODUkTcmTestTCMLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmTestTCMLevel.setStatus("current")
_JnxIfOtnODUkTcmInsertAis_Type = TruthValue
_JnxIfOtnODUkTcmInsertAis_Object = MibTableColumn
jnxIfOtnODUkTcmInsertAis = _JnxIfOtnODUkTcmInsertAis_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5, 1, 3),
    _JnxIfOtnODUkTcmInsertAis_Type()
)
jnxIfOtnODUkTcmInsertAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmInsertAis.setStatus("current")
_JnxIfOtnODUkTcmInsertLck_Type = TruthValue
_JnxIfOtnODUkTcmInsertLck_Object = MibTableColumn
jnxIfOtnODUkTcmInsertLck = _JnxIfOtnODUkTcmInsertLck_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5, 1, 4),
    _JnxIfOtnODUkTcmInsertLck_Type()
)
jnxIfOtnODUkTcmInsertLck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmInsertLck.setStatus("current")
_JnxIfOtnODUkTcmInsertOci_Type = TruthValue
_JnxIfOtnODUkTcmInsertOci_Object = MibTableColumn
jnxIfOtnODUkTcmInsertOci = _JnxIfOtnODUkTcmInsertOci_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5, 1, 5),
    _JnxIfOtnODUkTcmInsertOci_Type()
)
jnxIfOtnODUkTcmInsertOci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmInsertOci.setStatus("current")
_JnxIfOtnODUkPayloadPRBS_Type = TruthValue
_JnxIfOtnODUkPayloadPRBS_Object = MibTableColumn
jnxIfOtnODUkPayloadPRBS = _JnxIfOtnODUkPayloadPRBS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5, 1, 6),
    _JnxIfOtnODUkPayloadPRBS_Type()
)
jnxIfOtnODUkPayloadPRBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnODUkPayloadPRBS.setStatus("current")
_JnxIfOtnODUkPayloadPRBSResult_Type = OctetString
_JnxIfOtnODUkPayloadPRBSResult_Object = MibTableColumn
jnxIfOtnODUkPayloadPRBSResult = _JnxIfOtnODUkPayloadPRBSResult_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 5, 1, 7),
    _JnxIfOtnODUkPayloadPRBSResult_Type()
)
jnxIfOtnODUkPayloadPRBSResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnODUkPayloadPRBSResult.setStatus("current")
_JnxIfOtnODUkTcmDMTable_Object = MibTable
jnxIfOtnODUkTcmDMTable = _JnxIfOtnODUkTcmDMTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmDMTable.setStatus("current")
_JnxIfOtnODUkTcmDMEntry_Object = MibTableRow
jnxIfOtnODUkTcmDMEntry = _JnxIfOtnODUkTcmDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 6, 1)
)
jnxIfOtnODUkTcmDMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnODUkTcmDMLayer"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnODUkTcmDMLevel"),
)
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmDMEntry.setStatus("current")
_JnxIfOtnODUkTcmDMLayer_Type = JnxIfOtnLayer
_JnxIfOtnODUkTcmDMLayer_Object = MibTableColumn
jnxIfOtnODUkTcmDMLayer = _JnxIfOtnODUkTcmDMLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 6, 1, 1),
    _JnxIfOtnODUkTcmDMLayer_Type()
)
jnxIfOtnODUkTcmDMLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmDMLayer.setStatus("current")


class _JnxIfOtnODUkTcmDMLevel_Type(Integer32):
    """Custom type jnxIfOtnODUkTcmDMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_JnxIfOtnODUkTcmDMLevel_Type.__name__ = "Integer32"
_JnxIfOtnODUkTcmDMLevel_Object = MibTableColumn
jnxIfOtnODUkTcmDMLevel = _JnxIfOtnODUkTcmDMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 6, 1, 2),
    _JnxIfOtnODUkTcmDMLevel_Type()
)
jnxIfOtnODUkTcmDMLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnODUkTcmDMLevel.setStatus("current")
_JnxIfOtnDMConnectionMonitoringEndpoint_Type = TruthValue
_JnxIfOtnDMConnectionMonitoringEndpoint_Object = MibTableColumn
jnxIfOtnDMConnectionMonitoringEndpoint = _JnxIfOtnDMConnectionMonitoringEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 6, 1, 3),
    _JnxIfOtnDMConnectionMonitoringEndpoint_Type()
)
jnxIfOtnDMConnectionMonitoringEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnDMConnectionMonitoringEndpoint.setStatus("current")
_JnxIfOtnDMBypass_Type = TruthValue
_JnxIfOtnDMBypass_Object = MibTableColumn
jnxIfOtnDMBypass = _JnxIfOtnDMBypass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 6, 1, 4),
    _JnxIfOtnDMBypass_Type()
)
jnxIfOtnDMBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnDMBypass.setStatus("current")
_JnxIfOtnDMPersistFrames_Type = Integer32
_JnxIfOtnDMPersistFrames_Object = MibTableColumn
jnxIfOtnDMPersistFrames = _JnxIfOtnDMPersistFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 6, 1, 5),
    _JnxIfOtnDMPersistFrames_Type()
)
jnxIfOtnDMPersistFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnDMPersistFrames.setStatus("current")
_JnxIfOtnDMEnable_Type = TruthValue
_JnxIfOtnDMEnable_Object = MibTableColumn
jnxIfOtnDMEnable = _JnxIfOtnDMEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 6, 1, 6),
    _JnxIfOtnDMEnable_Type()
)
jnxIfOtnDMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnDMEnable.setStatus("current")
_JnxIfOtnNotificationTrigDefaultHoldtimeUp_Type = Integer32
_JnxIfOtnNotificationTrigDefaultHoldtimeUp_Object = MibScalar
jnxIfOtnNotificationTrigDefaultHoldtimeUp = _JnxIfOtnNotificationTrigDefaultHoldtimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 7),
    _JnxIfOtnNotificationTrigDefaultHoldtimeUp_Type()
)
jnxIfOtnNotificationTrigDefaultHoldtimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigDefaultHoldtimeUp.setStatus("current")
_JnxIfOtnNotificationTrigDefaultHoldtimeDown_Type = Integer32
_JnxIfOtnNotificationTrigDefaultHoldtimeDown_Object = MibScalar
jnxIfOtnNotificationTrigDefaultHoldtimeDown = _JnxIfOtnNotificationTrigDefaultHoldtimeDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 8),
    _JnxIfOtnNotificationTrigDefaultHoldtimeDown_Type()
)
jnxIfOtnNotificationTrigDefaultHoldtimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigDefaultHoldtimeDown.setStatus("current")
_JnxIfOtnNotificationTrigTable_Object = MibTable
jnxIfOtnNotificationTrigTable = _JnxIfOtnNotificationTrigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9)
)
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigTable.setStatus("current")
_JnxIfOtnNotificationTrigEntry_Object = MibTableRow
jnxIfOtnNotificationTrigEntry = _JnxIfOtnNotificationTrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1)
)
jnxIfOtnNotificationTrigEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnNotificationTrigContainerIndex"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnNotificationTrigL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnNotificationTrigL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnNotificationTrigL3Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnNotificationTrigLayer"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnNotificationTrigTCMLevel"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnNotificationTrigAlmId"),
)
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigEntry.setStatus("current")


class _JnxIfOtnNotificationTrigContainerIndex_Type(Integer32):
    """Custom type jnxIfOtnNotificationTrigContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnNotificationTrigContainerIndex_Type.__name__ = "Integer32"
_JnxIfOtnNotificationTrigContainerIndex_Object = MibTableColumn
jnxIfOtnNotificationTrigContainerIndex = _JnxIfOtnNotificationTrigContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 1),
    _JnxIfOtnNotificationTrigContainerIndex_Type()
)
jnxIfOtnNotificationTrigContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigContainerIndex.setStatus("current")


class _JnxIfOtnNotificationTrigL1Index_Type(Integer32):
    """Custom type jnxIfOtnNotificationTrigL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnNotificationTrigL1Index_Type.__name__ = "Integer32"
_JnxIfOtnNotificationTrigL1Index_Object = MibTableColumn
jnxIfOtnNotificationTrigL1Index = _JnxIfOtnNotificationTrigL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 2),
    _JnxIfOtnNotificationTrigL1Index_Type()
)
jnxIfOtnNotificationTrigL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigL1Index.setStatus("current")


class _JnxIfOtnNotificationTrigL2Index_Type(Integer32):
    """Custom type jnxIfOtnNotificationTrigL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnNotificationTrigL2Index_Type.__name__ = "Integer32"
_JnxIfOtnNotificationTrigL2Index_Object = MibTableColumn
jnxIfOtnNotificationTrigL2Index = _JnxIfOtnNotificationTrigL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 3),
    _JnxIfOtnNotificationTrigL2Index_Type()
)
jnxIfOtnNotificationTrigL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigL2Index.setStatus("current")


class _JnxIfOtnNotificationTrigL3Index_Type(Integer32):
    """Custom type jnxIfOtnNotificationTrigL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnNotificationTrigL3Index_Type.__name__ = "Integer32"
_JnxIfOtnNotificationTrigL3Index_Object = MibTableColumn
jnxIfOtnNotificationTrigL3Index = _JnxIfOtnNotificationTrigL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 4),
    _JnxIfOtnNotificationTrigL3Index_Type()
)
jnxIfOtnNotificationTrigL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigL3Index.setStatus("current")
_JnxIfOtnNotificationTrigLayer_Type = JnxIfOtnLayer
_JnxIfOtnNotificationTrigLayer_Object = MibTableColumn
jnxIfOtnNotificationTrigLayer = _JnxIfOtnNotificationTrigLayer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 5),
    _JnxIfOtnNotificationTrigLayer_Type()
)
jnxIfOtnNotificationTrigLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigLayer.setStatus("current")


class _JnxIfOtnNotificationTrigTCMLevel_Type(Integer32):
    """Custom type jnxIfOtnNotificationTrigTCMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_JnxIfOtnNotificationTrigTCMLevel_Type.__name__ = "Integer32"
_JnxIfOtnNotificationTrigTCMLevel_Object = MibTableColumn
jnxIfOtnNotificationTrigTCMLevel = _JnxIfOtnNotificationTrigTCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 6),
    _JnxIfOtnNotificationTrigTCMLevel_Type()
)
jnxIfOtnNotificationTrigTCMLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigTCMLevel.setStatus("current")


class _JnxIfOtnNotificationTrigAlmId_Type(Integer32):
    """Custom type jnxIfOtnNotificationTrigAlmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnNotificationTrigAlmId_Type.__name__ = "Integer32"
_JnxIfOtnNotificationTrigAlmId_Object = MibTableColumn
jnxIfOtnNotificationTrigAlmId = _JnxIfOtnNotificationTrigAlmId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 7),
    _JnxIfOtnNotificationTrigAlmId_Type()
)
jnxIfOtnNotificationTrigAlmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigAlmId.setStatus("current")
_JnxIfOtnNotificationTrigSeverity_Type = JnxIfOtnSeverity
_JnxIfOtnNotificationTrigSeverity_Object = MibTableColumn
jnxIfOtnNotificationTrigSeverity = _JnxIfOtnNotificationTrigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 8),
    _JnxIfOtnNotificationTrigSeverity_Type()
)
jnxIfOtnNotificationTrigSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigSeverity.setStatus("current")
_JnxIfOtnNotificationTrigIgnore_Type = TruthValue
_JnxIfOtnNotificationTrigIgnore_Object = MibTableColumn
jnxIfOtnNotificationTrigIgnore = _JnxIfOtnNotificationTrigIgnore_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 9),
    _JnxIfOtnNotificationTrigIgnore_Type()
)
jnxIfOtnNotificationTrigIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigIgnore.setStatus("current")
_JnxIfOtnNotificationTrigHoldtimeUp_Type = Integer32
_JnxIfOtnNotificationTrigHoldtimeUp_Object = MibTableColumn
jnxIfOtnNotificationTrigHoldtimeUp = _JnxIfOtnNotificationTrigHoldtimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 10),
    _JnxIfOtnNotificationTrigHoldtimeUp_Type()
)
jnxIfOtnNotificationTrigHoldtimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigHoldtimeUp.setStatus("current")
_JnxIfOtnNotificationTrigHoldtimeDown_Type = Integer32
_JnxIfOtnNotificationTrigHoldtimeDown_Object = MibTableColumn
jnxIfOtnNotificationTrigHoldtimeDown = _JnxIfOtnNotificationTrigHoldtimeDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 11),
    _JnxIfOtnNotificationTrigHoldtimeDown_Type()
)
jnxIfOtnNotificationTrigHoldtimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnNotificationTrigHoldtimeDown.setStatus("current")
_JnxIfOtnTrigServiceStateAction_Type = JnxIfOtnServiceStateAction
_JnxIfOtnTrigServiceStateAction_Object = MibTableColumn
jnxIfOtnTrigServiceStateAction = _JnxIfOtnTrigServiceStateAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 9, 1, 12),
    _JnxIfOtnTrigServiceStateAction_Type()
)
jnxIfOtnTrigServiceStateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnTrigServiceStateAction.setStatus("current")
_JnxOtnClearAllPMs_Type = TruthValue
_JnxOtnClearAllPMs_Object = MibScalar
jnxOtnClearAllPMs = _JnxOtnClearAllPMs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 10),
    _JnxOtnClearAllPMs_Type()
)
jnxOtnClearAllPMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOtnClearAllPMs.setStatus("current")
_JnxOtnClearInterfacePMs_Type = TruthValue
_JnxOtnClearInterfacePMs_Object = MibScalar
jnxOtnClearInterfacePMs = _JnxOtnClearInterfacePMs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 11),
    _JnxOtnClearInterfacePMs_Type()
)
jnxOtnClearInterfacePMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOtnClearInterfacePMs.setStatus("current")
_JnxOtnClearInterfaceCurrentPM_Type = TruthValue
_JnxOtnClearInterfaceCurrentPM_Object = MibScalar
jnxOtnClearInterfaceCurrentPM = _JnxOtnClearInterfaceCurrentPM_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 12),
    _JnxOtnClearInterfaceCurrentPM_Type()
)
jnxOtnClearInterfaceCurrentPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOtnClearInterfaceCurrentPM.setStatus("current")
_JnxOtnClearIfPMsTable_Object = MibTable
jnxOtnClearIfPMsTable = _JnxOtnClearIfPMsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 13)
)
if mibBuilder.loadTexts:
    jnxOtnClearIfPMsTable.setStatus("current")
_JnxOtnClearIfPMsEntry_Object = MibTableRow
jnxOtnClearIfPMsEntry = _JnxOtnClearIfPMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 13, 1)
)
jnxOtnClearIfPMsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOtnClearIfPMsEntry.setStatus("current")
_JnxOtnClearCurrent_Type = TruthValue
_JnxOtnClearCurrent_Object = MibTableColumn
jnxOtnClearCurrent = _JnxOtnClearCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 13, 1, 1),
    _JnxOtnClearCurrent_Type()
)
jnxOtnClearCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOtnClearCurrent.setStatus("current")
_JnxOtnClearInterfaceInterval_Type = TruthValue
_JnxOtnClearInterfaceInterval_Object = MibTableColumn
jnxOtnClearInterfaceInterval = _JnxOtnClearInterfaceInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 13, 1, 2),
    _JnxOtnClearInterfaceInterval_Type()
)
jnxOtnClearInterfaceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOtnClearInterfaceInterval.setStatus("current")
_JnxOtnClearInterfaceDay_Type = TruthValue
_JnxOtnClearInterfaceDay_Object = MibTableColumn
jnxOtnClearInterfaceDay = _JnxOtnClearInterfaceDay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 13, 1, 3),
    _JnxOtnClearInterfaceDay_Type()
)
jnxOtnClearInterfaceDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOtnClearInterfaceDay.setStatus("current")
_JnxOtnClearInterfaceAll_Type = TruthValue
_JnxOtnClearInterfaceAll_Object = MibTableColumn
jnxOtnClearInterfaceAll = _JnxOtnClearInterfaceAll_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 1, 13, 1, 4),
    _JnxOtnClearInterfaceAll_Type()
)
jnxOtnClearInterfaceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOtnClearInterfaceAll.setStatus("current")
_JnxIfOtnOCh2_ObjectIdentity = ObjectIdentity
jnxIfOtnOCh2 = _JnxIfOtnOCh2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2)
)
_JnxIfOtnOCh2CfgTable_Object = MibTable
jnxIfOtnOCh2CfgTable = _JnxIfOtnOCh2CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxIfOtnOCh2CfgTable.setStatus("obsolete")
_JnxIfOtnOCh2CfgEntry_Object = MibTableRow
jnxIfOtnOCh2CfgEntry = _JnxIfOtnOCh2CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1)
)
jnxIfOtnOCh2CfgEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2CfgContainerIndex"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2CfgL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2CfgL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2CfgL3Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2CfgL4Index"),
)
if mibBuilder.loadTexts:
    jnxIfOtnOCh2CfgEntry.setStatus("obsolete")


class _JnxIfOtnOCh2CfgContainerIndex_Type(Integer32):
    """Custom type jnxIfOtnOCh2CfgContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2CfgContainerIndex_Type.__name__ = "Integer32"
_JnxIfOtnOCh2CfgContainerIndex_Object = MibTableColumn
jnxIfOtnOCh2CfgContainerIndex = _JnxIfOtnOCh2CfgContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 1),
    _JnxIfOtnOCh2CfgContainerIndex_Type()
)
jnxIfOtnOCh2CfgContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2CfgContainerIndex.setStatus("obsolete")


class _JnxIfOtnOCh2CfgL1Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2CfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2CfgL1Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2CfgL1Index_Object = MibTableColumn
jnxIfOtnOCh2CfgL1Index = _JnxIfOtnOCh2CfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 2),
    _JnxIfOtnOCh2CfgL1Index_Type()
)
jnxIfOtnOCh2CfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2CfgL1Index.setStatus("obsolete")


class _JnxIfOtnOCh2CfgL2Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2CfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2CfgL2Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2CfgL2Index_Object = MibTableColumn
jnxIfOtnOCh2CfgL2Index = _JnxIfOtnOCh2CfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 3),
    _JnxIfOtnOCh2CfgL2Index_Type()
)
jnxIfOtnOCh2CfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2CfgL2Index.setStatus("obsolete")


class _JnxIfOtnOCh2CfgL3Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2CfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2CfgL3Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2CfgL3Index_Object = MibTableColumn
jnxIfOtnOCh2CfgL3Index = _JnxIfOtnOCh2CfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 4),
    _JnxIfOtnOCh2CfgL3Index_Type()
)
jnxIfOtnOCh2CfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2CfgL3Index.setStatus("obsolete")


class _JnxIfOtnOCh2CfgL4Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2CfgL4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2CfgL4Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2CfgL4Index_Object = MibTableColumn
jnxIfOtnOCh2CfgL4Index = _JnxIfOtnOCh2CfgL4Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 5),
    _JnxIfOtnOCh2CfgL4Index_Type()
)
jnxIfOtnOCh2CfgL4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2CfgL4Index.setStatus("obsolete")
_JnxIfOtnOCh2LocalLoopback_Type = TruthValue
_JnxIfOtnOCh2LocalLoopback_Object = MibTableColumn
jnxIfOtnOCh2LocalLoopback = _JnxIfOtnOCh2LocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 6),
    _JnxIfOtnOCh2LocalLoopback_Type()
)
jnxIfOtnOCh2LocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2LocalLoopback.setStatus("obsolete")
_JnxIfOtnOCh2LineLoopback_Type = TruthValue
_JnxIfOtnOCh2LineLoopback_Object = MibTableColumn
jnxIfOtnOCh2LineLoopback = _JnxIfOtnOCh2LineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 7),
    _JnxIfOtnOCh2LineLoopback_Type()
)
jnxIfOtnOCh2LineLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2LineLoopback.setStatus("obsolete")
_JnxIfOtnOCh2PayloadLoopback_Type = TruthValue
_JnxIfOtnOCh2PayloadLoopback_Object = MibTableColumn
jnxIfOtnOCh2PayloadLoopback = _JnxIfOtnOCh2PayloadLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 8),
    _JnxIfOtnOCh2PayloadLoopback_Type()
)
jnxIfOtnOCh2PayloadLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2PayloadLoopback.setStatus("obsolete")
_JnxIfOtnOCh2AdminState_Type = JnxIfAdminStates
_JnxIfOtnOCh2AdminState_Object = MibTableColumn
jnxIfOtnOCh2AdminState = _JnxIfOtnOCh2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 9),
    _JnxIfOtnOCh2AdminState_Type()
)
jnxIfOtnOCh2AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2AdminState.setStatus("obsolete")
_JnxIfOtnOCh2OperState_Type = JnxIfOperStates
_JnxIfOtnOCh2OperState_Object = MibTableColumn
jnxIfOtnOCh2OperState = _JnxIfOtnOCh2OperState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 10),
    _JnxIfOtnOCh2OperState_Type()
)
jnxIfOtnOCh2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OperState.setStatus("obsolete")
_JnxIfOtnOCh2Index_Type = Unsigned32
_JnxIfOtnOCh2Index_Object = MibTableColumn
jnxIfOtnOCh2Index = _JnxIfOtnOCh2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 11),
    _JnxIfOtnOCh2Index_Type()
)
jnxIfOtnOCh2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2Index.setStatus("obsolete")


class _JnxIfOtnOCh2Status_Type(Bits):
    """Custom type jnxIfOtnOCh2Status based on Bits"""
    namedValues = NamedValues(
        *(("lof", 1),
          ("lom", 2),
          ("los", 0),
          ("wavelengthlockerr", 3))
    )

_JnxIfOtnOCh2Status_Type.__name__ = "Bits"
_JnxIfOtnOCh2Status_Object = MibTableColumn
jnxIfOtnOCh2Status = _JnxIfOtnOCh2Status_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 12),
    _JnxIfOtnOCh2Status_Type()
)
jnxIfOtnOCh2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2Status.setStatus("current")
_JnxIfOtnOCh2PortMode_Type = Unsigned32
_JnxIfOtnOCh2PortMode_Object = MibTableColumn
jnxIfOtnOCh2PortMode = _JnxIfOtnOCh2PortMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 1, 1, 13),
    _JnxIfOtnOCh2PortMode_Type()
)
jnxIfOtnOCh2PortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2PortMode.setStatus("obsolete")
_JnxIfOtnOCh2OTUkCfgTable_Object = MibTable
jnxIfOtnOCh2OTUkCfgTable = _JnxIfOtnOCh2OTUkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgTable.setStatus("obsolete")
_JnxIfOtnOCh2OTUkCfgEntry_Object = MibTableRow
jnxIfOtnOCh2OTUkCfgEntry = _JnxIfOtnOCh2OTUkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1)
)
jnxIfOtnOCh2OTUkCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2OTUkCfgContIndx"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2OTUkCfgL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2OTUkCfgL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2OTUkCfgL3Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2OTUkCfgL4Index"),
)
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgEntry.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkCfgContIndx_Type(Integer32):
    """Custom type jnxIfOtnOCh2OTUkCfgContIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2OTUkCfgContIndx_Type.__name__ = "Integer32"
_JnxIfOtnOCh2OTUkCfgContIndx_Object = MibTableColumn
jnxIfOtnOCh2OTUkCfgContIndx = _JnxIfOtnOCh2OTUkCfgContIndx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 1),
    _JnxIfOtnOCh2OTUkCfgContIndx_Type()
)
jnxIfOtnOCh2OTUkCfgContIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgContIndx.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkCfgL1Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2OTUkCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2OTUkCfgL1Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2OTUkCfgL1Index_Object = MibTableColumn
jnxIfOtnOCh2OTUkCfgL1Index = _JnxIfOtnOCh2OTUkCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 2),
    _JnxIfOtnOCh2OTUkCfgL1Index_Type()
)
jnxIfOtnOCh2OTUkCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgL1Index.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkCfgL2Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2OTUkCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2OTUkCfgL2Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2OTUkCfgL2Index_Object = MibTableColumn
jnxIfOtnOCh2OTUkCfgL2Index = _JnxIfOtnOCh2OTUkCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 3),
    _JnxIfOtnOCh2OTUkCfgL2Index_Type()
)
jnxIfOtnOCh2OTUkCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgL2Index.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkCfgL3Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2OTUkCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2OTUkCfgL3Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2OTUkCfgL3Index_Object = MibTableColumn
jnxIfOtnOCh2OTUkCfgL3Index = _JnxIfOtnOCh2OTUkCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 4),
    _JnxIfOtnOCh2OTUkCfgL3Index_Type()
)
jnxIfOtnOCh2OTUkCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgL3Index.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkCfgL4Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2OTUkCfgL4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIfOtnOCh2OTUkCfgL4Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2OTUkCfgL4Index_Object = MibTableColumn
jnxIfOtnOCh2OTUkCfgL4Index = _JnxIfOtnOCh2OTUkCfgL4Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 5),
    _JnxIfOtnOCh2OTUkCfgL4Index_Type()
)
jnxIfOtnOCh2OTUkCfgL4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgL4Index.setStatus("obsolete")
_JnxIfOtnOCh2OTUkCfgRate_Type = JnxIfOtnRate
_JnxIfOtnOCh2OTUkCfgRate_Object = MibTableColumn
jnxIfOtnOCh2OTUkCfgRate = _JnxIfOtnOCh2OTUkCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 6),
    _JnxIfOtnOCh2OTUkCfgRate_Type()
)
jnxIfOtnOCh2OTUkCfgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgRate.setStatus("obsolete")
_JnxIfOtnOCh2OTUkCfgFecMode_Type = JnxIfOtnFecType
_JnxIfOtnOCh2OTUkCfgFecMode_Object = MibTableColumn
jnxIfOtnOCh2OTUkCfgFecMode = _JnxIfOtnOCh2OTUkCfgFecMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 7),
    _JnxIfOtnOCh2OTUkCfgFecMode_Type()
)
jnxIfOtnOCh2OTUkCfgFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkCfgFecMode.setStatus("obsolete")
_JnxIfOtnOCh2OTUkEnAutoFrrByteIns_Type = TruthValue
_JnxIfOtnOCh2OTUkEnAutoFrrByteIns_Object = MibTableColumn
jnxIfOtnOCh2OTUkEnAutoFrrByteIns = _JnxIfOtnOCh2OTUkEnAutoFrrByteIns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 8),
    _JnxIfOtnOCh2OTUkEnAutoFrrByteIns_Type()
)
jnxIfOtnOCh2OTUkEnAutoFrrByteIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkEnAutoFrrByteIns.setStatus("obsolete")
_JnxIfOtnOCh2OTUkEnBERFrrSupport_Type = TruthValue
_JnxIfOtnOCh2OTUkEnBERFrrSupport_Object = MibTableColumn
jnxIfOtnOCh2OTUkEnBERFrrSupport = _JnxIfOtnOCh2OTUkEnBERFrrSupport_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 9),
    _JnxIfOtnOCh2OTUkEnBERFrrSupport_Type()
)
jnxIfOtnOCh2OTUkEnBERFrrSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkEnBERFrrSupport.setStatus("obsolete")
_JnxIfOtnOCh2OTUkPreFecBERThMant_Type = Integer32
_JnxIfOtnOCh2OTUkPreFecBERThMant_Object = MibTableColumn
jnxIfOtnOCh2OTUkPreFecBERThMant = _JnxIfOtnOCh2OTUkPreFecBERThMant_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 10),
    _JnxIfOtnOCh2OTUkPreFecBERThMant_Type()
)
jnxIfOtnOCh2OTUkPreFecBERThMant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkPreFecBERThMant.setStatus("obsolete")
_JnxIfOtnOCh2OTUkPreFecBERThExpo_Type = Integer32
_JnxIfOtnOCh2OTUkPreFecBERThExpo_Object = MibTableColumn
jnxIfOtnOCh2OTUkPreFecBERThExpo = _JnxIfOtnOCh2OTUkPreFecBERThExpo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 11),
    _JnxIfOtnOCh2OTUkPreFecBERThExpo_Type()
)
jnxIfOtnOCh2OTUkPreFecBERThExpo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkPreFecBERThExpo.setStatus("obsolete")
_JnxIfOtnOCh2OTUkPreFecBERThTime_Type = Integer32
_JnxIfOtnOCh2OTUkPreFecBERThTime_Object = MibTableColumn
jnxIfOtnOCh2OTUkPreFecBERThTime = _JnxIfOtnOCh2OTUkPreFecBERThTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 12),
    _JnxIfOtnOCh2OTUkPreFecBERThTime_Type()
)
jnxIfOtnOCh2OTUkPreFecBERThTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkPreFecBERThTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkPreFecBERThTime.setUnits("ms")
_JnxIfOtnOCh2OTUkTIMActEnabled_Type = TruthValue
_JnxIfOtnOCh2OTUkTIMActEnabled_Object = MibTableColumn
jnxIfOtnOCh2OTUkTIMActEnabled = _JnxIfOtnOCh2OTUkTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 13),
    _JnxIfOtnOCh2OTUkTIMActEnabled_Type()
)
jnxIfOtnOCh2OTUkTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkTIMActEnabled.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkTxTTI_Type(OctetString):
    """Custom type jnxIfOtnOCh2OTUkTxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxIfOtnOCh2OTUkTxTTI_Type.__name__ = "OctetString"
_JnxIfOtnOCh2OTUkTxTTI_Object = MibTableColumn
jnxIfOtnOCh2OTUkTxTTI = _JnxIfOtnOCh2OTUkTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 14),
    _JnxIfOtnOCh2OTUkTxTTI_Type()
)
jnxIfOtnOCh2OTUkTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkTxTTI.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkRxTTI_Type(OctetString):
    """Custom type jnxIfOtnOCh2OTUkRxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_JnxIfOtnOCh2OTUkRxTTI_Type.__name__ = "OctetString"
_JnxIfOtnOCh2OTUkRxTTI_Object = MibTableColumn
jnxIfOtnOCh2OTUkRxTTI = _JnxIfOtnOCh2OTUkRxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 15),
    _JnxIfOtnOCh2OTUkRxTTI_Type()
)
jnxIfOtnOCh2OTUkRxTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkRxTTI.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkExpectedRxSapi_Type(OctetString):
    """Custom type jnxIfOtnOCh2OTUkExpectedRxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnOCh2OTUkExpectedRxSapi_Type.__name__ = "OctetString"
_JnxIfOtnOCh2OTUkExpectedRxSapi_Object = MibTableColumn
jnxIfOtnOCh2OTUkExpectedRxSapi = _JnxIfOtnOCh2OTUkExpectedRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 16),
    _JnxIfOtnOCh2OTUkExpectedRxSapi_Type()
)
jnxIfOtnOCh2OTUkExpectedRxSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkExpectedRxSapi.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkExpectedRxDapi_Type(OctetString):
    """Custom type jnxIfOtnOCh2OTUkExpectedRxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnOCh2OTUkExpectedRxDapi_Type.__name__ = "OctetString"
_JnxIfOtnOCh2OTUkExpectedRxDapi_Object = MibTableColumn
jnxIfOtnOCh2OTUkExpectedRxDapi = _JnxIfOtnOCh2OTUkExpectedRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 17),
    _JnxIfOtnOCh2OTUkExpectedRxDapi_Type()
)
jnxIfOtnOCh2OTUkExpectedRxDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkExpectedRxDapi.setStatus("obsolete")


class _JnxIfOtnOCh2OTUkStatus_Type(Bits):
    """Custom type jnxIfOtnOCh2OTUkStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 0),
          ("bdi", 1),
          ("biae", 6),
          ("fecdegrade", 10),
          ("fecexcessive", 9),
          ("iae", 2),
          ("sd", 5),
          ("sf", 4),
          ("ssf", 8),
          ("tsf", 7),
          ("ttim", 3))
    )

_JnxIfOtnOCh2OTUkStatus_Type.__name__ = "Bits"
_JnxIfOtnOCh2OTUkStatus_Object = MibTableColumn
jnxIfOtnOCh2OTUkStatus = _JnxIfOtnOCh2OTUkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 18),
    _JnxIfOtnOCh2OTUkStatus_Type()
)
jnxIfOtnOCh2OTUkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkStatus.setStatus("obsolete")
_JnxIfOtnOCh2OTUkPreFecBERThClrMn_Type = Integer32
_JnxIfOtnOCh2OTUkPreFecBERThClrMn_Object = MibTableColumn
jnxIfOtnOCh2OTUkPreFecBERThClrMn = _JnxIfOtnOCh2OTUkPreFecBERThClrMn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 19),
    _JnxIfOtnOCh2OTUkPreFecBERThClrMn_Type()
)
jnxIfOtnOCh2OTUkPreFecBERThClrMn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkPreFecBERThClrMn.setStatus("obsolete")
_JnxIfOtnOCh2OTUkPreFecBERThClrEx_Type = Integer32
_JnxIfOtnOCh2OTUkPreFecBERThClrEx_Object = MibTableColumn
jnxIfOtnOCh2OTUkPreFecBERThClrEx = _JnxIfOtnOCh2OTUkPreFecBERThClrEx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 2, 1, 20),
    _JnxIfOtnOCh2OTUkPreFecBERThClrEx_Type()
)
jnxIfOtnOCh2OTUkPreFecBERThClrEx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2OTUkPreFecBERThClrEx.setStatus("obsolete")
_JnxIfOtnOCh2ODUkCfgTable_Object = MibTable
jnxIfOtnOCh2ODUkCfgTable = _JnxIfOtnOCh2ODUkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkCfgTable.setStatus("obsolete")
_JnxIfOtnOCh2ODUkCfgEntry_Object = MibTableRow
jnxIfOtnOCh2ODUkCfgEntry = _JnxIfOtnOCh2ODUkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1)
)
jnxIfOtnOCh2ODUkCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2ODUkCfgContIndx"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2ODUkCfgL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2ODUkCfgL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2ODUkCfgL3Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2ODUkCfgL4Index"),
)
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkCfgEntry.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkCfgContIndx_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkCfgContIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkCfgContIndx_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkCfgContIndx_Object = MibTableColumn
jnxIfOtnOCh2ODUkCfgContIndx = _JnxIfOtnOCh2ODUkCfgContIndx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 1),
    _JnxIfOtnOCh2ODUkCfgContIndx_Type()
)
jnxIfOtnOCh2ODUkCfgContIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkCfgContIndx.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkCfgL1Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkCfgL1Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkCfgL1Index_Object = MibTableColumn
jnxIfOtnOCh2ODUkCfgL1Index = _JnxIfOtnOCh2ODUkCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 2),
    _JnxIfOtnOCh2ODUkCfgL1Index_Type()
)
jnxIfOtnOCh2ODUkCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkCfgL1Index.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkCfgL2Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkCfgL2Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkCfgL2Index_Object = MibTableColumn
jnxIfOtnOCh2ODUkCfgL2Index = _JnxIfOtnOCh2ODUkCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 3),
    _JnxIfOtnOCh2ODUkCfgL2Index_Type()
)
jnxIfOtnOCh2ODUkCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkCfgL2Index.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkCfgL3Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkCfgL3Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkCfgL3Index_Object = MibTableColumn
jnxIfOtnOCh2ODUkCfgL3Index = _JnxIfOtnOCh2ODUkCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 4),
    _JnxIfOtnOCh2ODUkCfgL3Index_Type()
)
jnxIfOtnOCh2ODUkCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkCfgL3Index.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkCfgL4Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkCfgL4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkCfgL4Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkCfgL4Index_Object = MibTableColumn
jnxIfOtnOCh2ODUkCfgL4Index = _JnxIfOtnOCh2ODUkCfgL4Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 5),
    _JnxIfOtnOCh2ODUkCfgL4Index_Type()
)
jnxIfOtnOCh2ODUkCfgL4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkCfgL4Index.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkAPSPCC0_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkAPSPCC0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkAPSPCC0_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkAPSPCC0_Object = MibTableColumn
jnxIfOtnOCh2ODUkAPSPCC0 = _JnxIfOtnOCh2ODUkAPSPCC0_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 6),
    _JnxIfOtnOCh2ODUkAPSPCC0_Type()
)
jnxIfOtnOCh2ODUkAPSPCC0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkAPSPCC0.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkAPSPCC1_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkAPSPCC1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkAPSPCC1_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkAPSPCC1_Object = MibTableColumn
jnxIfOtnOCh2ODUkAPSPCC1 = _JnxIfOtnOCh2ODUkAPSPCC1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 7),
    _JnxIfOtnOCh2ODUkAPSPCC1_Type()
)
jnxIfOtnOCh2ODUkAPSPCC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkAPSPCC1.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkAPSPCC2_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkAPSPCC2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkAPSPCC2_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkAPSPCC2_Object = MibTableColumn
jnxIfOtnOCh2ODUkAPSPCC2 = _JnxIfOtnOCh2ODUkAPSPCC2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 8),
    _JnxIfOtnOCh2ODUkAPSPCC2_Type()
)
jnxIfOtnOCh2ODUkAPSPCC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkAPSPCC2.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkAPSPCC3_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkAPSPCC3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkAPSPCC3_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkAPSPCC3_Object = MibTableColumn
jnxIfOtnOCh2ODUkAPSPCC3 = _JnxIfOtnOCh2ODUkAPSPCC3_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 9),
    _JnxIfOtnOCh2ODUkAPSPCC3_Type()
)
jnxIfOtnOCh2ODUkAPSPCC3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkAPSPCC3.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkPayloadType_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkPayloadType_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkPayloadType_Object = MibTableColumn
jnxIfOtnOCh2ODUkPayloadType = _JnxIfOtnOCh2ODUkPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 10),
    _JnxIfOtnOCh2ODUkPayloadType_Type()
)
jnxIfOtnOCh2ODUkPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkPayloadType.setStatus("obsolete")
_JnxIfOtnOCh2ODUkTIMActEnabled_Type = TruthValue
_JnxIfOtnOCh2ODUkTIMActEnabled_Object = MibTableColumn
jnxIfOtnOCh2ODUkTIMActEnabled = _JnxIfOtnOCh2ODUkTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 11),
    _JnxIfOtnOCh2ODUkTIMActEnabled_Type()
)
jnxIfOtnOCh2ODUkTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkTIMActEnabled.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkTxTTI_Type(OctetString):
    """Custom type jnxIfOtnOCh2ODUkTxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxIfOtnOCh2ODUkTxTTI_Type.__name__ = "OctetString"
_JnxIfOtnOCh2ODUkTxTTI_Object = MibTableColumn
jnxIfOtnOCh2ODUkTxTTI = _JnxIfOtnOCh2ODUkTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 12),
    _JnxIfOtnOCh2ODUkTxTTI_Type()
)
jnxIfOtnOCh2ODUkTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkTxTTI.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkRxTTI_Type(OctetString):
    """Custom type jnxIfOtnOCh2ODUkRxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_JnxIfOtnOCh2ODUkRxTTI_Type.__name__ = "OctetString"
_JnxIfOtnOCh2ODUkRxTTI_Object = MibTableColumn
jnxIfOtnOCh2ODUkRxTTI = _JnxIfOtnOCh2ODUkRxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 13),
    _JnxIfOtnOCh2ODUkRxTTI_Type()
)
jnxIfOtnOCh2ODUkRxTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkRxTTI.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkExpectedRxSapi_Type(OctetString):
    """Custom type jnxIfOtnOCh2ODUkExpectedRxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnOCh2ODUkExpectedRxSapi_Type.__name__ = "OctetString"
_JnxIfOtnOCh2ODUkExpectedRxSapi_Object = MibTableColumn
jnxIfOtnOCh2ODUkExpectedRxSapi = _JnxIfOtnOCh2ODUkExpectedRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 14),
    _JnxIfOtnOCh2ODUkExpectedRxSapi_Type()
)
jnxIfOtnOCh2ODUkExpectedRxSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkExpectedRxSapi.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkExpectedRxDapi_Type(OctetString):
    """Custom type jnxIfOtnOCh2ODUkExpectedRxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnOCh2ODUkExpectedRxDapi_Type.__name__ = "OctetString"
_JnxIfOtnOCh2ODUkExpectedRxDapi_Object = MibTableColumn
jnxIfOtnOCh2ODUkExpectedRxDapi = _JnxIfOtnOCh2ODUkExpectedRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 15),
    _JnxIfOtnOCh2ODUkExpectedRxDapi_Type()
)
jnxIfOtnOCh2ODUkExpectedRxDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkExpectedRxDapi.setStatus("obsolete")


class _JnxIfOtnOCh2ODUkStatus_Type(Bits):
    """Custom type jnxIfOtnOCh2ODUkStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 0),
          ("bdi", 1),
          ("biae", 6),
          ("csf", 9),
          ("iae", 2),
          ("lck", 11),
          ("ltc", 12),
          ("oci", 10),
          ("ptm", 13),
          ("sd", 5),
          ("sf", 4),
          ("ssf", 8),
          ("tsf", 7),
          ("ttim", 3))
    )

_JnxIfOtnOCh2ODUkStatus_Type.__name__ = "Bits"
_JnxIfOtnOCh2ODUkStatus_Object = MibTableColumn
jnxIfOtnOCh2ODUkStatus = _JnxIfOtnOCh2ODUkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 16),
    _JnxIfOtnOCh2ODUkStatus_Type()
)
jnxIfOtnOCh2ODUkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkStatus.setStatus("current")


class _JnxIfOtnOCh2ODUkRxPayloadType_Type(Integer32):
    """Custom type jnxIfOtnOCh2ODUkRxPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2ODUkRxPayloadType_Type.__name__ = "Integer32"
_JnxIfOtnOCh2ODUkRxPayloadType_Object = MibTableColumn
jnxIfOtnOCh2ODUkRxPayloadType = _JnxIfOtnOCh2ODUkRxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 3, 1, 17),
    _JnxIfOtnOCh2ODUkRxPayloadType_Type()
)
jnxIfOtnOCh2ODUkRxPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2ODUkRxPayloadType.setStatus("obsolete")
_JnxIfOtnOCh2TcmCfgTable_Object = MibTable
jnxIfOtnOCh2TcmCfgTable = _JnxIfOtnOCh2TcmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmCfgTable.setStatus("obsolete")
_JnxIfOtnOCh2TcmCfgEntry_Object = MibTableRow
jnxIfOtnOCh2TcmCfgEntry = _JnxIfOtnOCh2TcmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1)
)
jnxIfOtnOCh2TcmCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2TcmCfgContIndx"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2TcmCfgL1Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2TcmCfgL2Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2TcmCfgL3Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2TcmCfgL4Index"),
    (0, "JUNIPER-IFOTN-MIB", "jnxIfOtnOCh2TcmCfgLevel"),
)
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmCfgEntry.setStatus("obsolete")


class _JnxIfOtnOCh2TcmCfgContIndx_Type(Integer32):
    """Custom type jnxIfOtnOCh2TcmCfgContIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2TcmCfgContIndx_Type.__name__ = "Integer32"
_JnxIfOtnOCh2TcmCfgContIndx_Object = MibTableColumn
jnxIfOtnOCh2TcmCfgContIndx = _JnxIfOtnOCh2TcmCfgContIndx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 1),
    _JnxIfOtnOCh2TcmCfgContIndx_Type()
)
jnxIfOtnOCh2TcmCfgContIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmCfgContIndx.setStatus("obsolete")


class _JnxIfOtnOCh2TcmCfgL1Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2TcmCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2TcmCfgL1Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2TcmCfgL1Index_Object = MibTableColumn
jnxIfOtnOCh2TcmCfgL1Index = _JnxIfOtnOCh2TcmCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 2),
    _JnxIfOtnOCh2TcmCfgL1Index_Type()
)
jnxIfOtnOCh2TcmCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmCfgL1Index.setStatus("obsolete")


class _JnxIfOtnOCh2TcmCfgL2Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2TcmCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2TcmCfgL2Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2TcmCfgL2Index_Object = MibTableColumn
jnxIfOtnOCh2TcmCfgL2Index = _JnxIfOtnOCh2TcmCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 3),
    _JnxIfOtnOCh2TcmCfgL2Index_Type()
)
jnxIfOtnOCh2TcmCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmCfgL2Index.setStatus("obsolete")


class _JnxIfOtnOCh2TcmCfgL3Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2TcmCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2TcmCfgL3Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2TcmCfgL3Index_Object = MibTableColumn
jnxIfOtnOCh2TcmCfgL3Index = _JnxIfOtnOCh2TcmCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 4),
    _JnxIfOtnOCh2TcmCfgL3Index_Type()
)
jnxIfOtnOCh2TcmCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmCfgL3Index.setStatus("obsolete")


class _JnxIfOtnOCh2TcmCfgL4Index_Type(Integer32):
    """Custom type jnxIfOtnOCh2TcmCfgL4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxIfOtnOCh2TcmCfgL4Index_Type.__name__ = "Integer32"
_JnxIfOtnOCh2TcmCfgL4Index_Object = MibTableColumn
jnxIfOtnOCh2TcmCfgL4Index = _JnxIfOtnOCh2TcmCfgL4Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 5),
    _JnxIfOtnOCh2TcmCfgL4Index_Type()
)
jnxIfOtnOCh2TcmCfgL4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmCfgL4Index.setStatus("obsolete")


class _JnxIfOtnOCh2TcmCfgLevel_Type(Integer32):
    """Custom type jnxIfOtnOCh2TcmCfgLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_JnxIfOtnOCh2TcmCfgLevel_Type.__name__ = "Integer32"
_JnxIfOtnOCh2TcmCfgLevel_Object = MibTableColumn
jnxIfOtnOCh2TcmCfgLevel = _JnxIfOtnOCh2TcmCfgLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 6),
    _JnxIfOtnOCh2TcmCfgLevel_Type()
)
jnxIfOtnOCh2TcmCfgLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmCfgLevel.setStatus("obsolete")
_JnxIfOtnOCh2TCMEnable_Type = TruthValue
_JnxIfOtnOCh2TCMEnable_Object = MibTableColumn
jnxIfOtnOCh2TCMEnable = _JnxIfOtnOCh2TCMEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 7),
    _JnxIfOtnOCh2TCMEnable_Type()
)
jnxIfOtnOCh2TCMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TCMEnable.setStatus("obsolete")


class _JnxIfOtnOCh2TcmTxTTI_Type(OctetString):
    """Custom type jnxIfOtnOCh2TcmTxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxIfOtnOCh2TcmTxTTI_Type.__name__ = "OctetString"
_JnxIfOtnOCh2TcmTxTTI_Object = MibTableColumn
jnxIfOtnOCh2TcmTxTTI = _JnxIfOtnOCh2TcmTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 8),
    _JnxIfOtnOCh2TcmTxTTI_Type()
)
jnxIfOtnOCh2TcmTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmTxTTI.setStatus("obsolete")


class _JnxIfOtnOCh2TcmRxTTI_Type(OctetString):
    """Custom type jnxIfOtnOCh2TcmRxTTI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_JnxIfOtnOCh2TcmRxTTI_Type.__name__ = "OctetString"
_JnxIfOtnOCh2TcmRxTTI_Object = MibTableColumn
jnxIfOtnOCh2TcmRxTTI = _JnxIfOtnOCh2TcmRxTTI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 9),
    _JnxIfOtnOCh2TcmRxTTI_Type()
)
jnxIfOtnOCh2TcmRxTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmRxTTI.setStatus("obsolete")


class _JnxIfOtnOCh2TcmExpectedRxSapi_Type(OctetString):
    """Custom type jnxIfOtnOCh2TcmExpectedRxSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnOCh2TcmExpectedRxSapi_Type.__name__ = "OctetString"
_JnxIfOtnOCh2TcmExpectedRxSapi_Object = MibTableColumn
jnxIfOtnOCh2TcmExpectedRxSapi = _JnxIfOtnOCh2TcmExpectedRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 10),
    _JnxIfOtnOCh2TcmExpectedRxSapi_Type()
)
jnxIfOtnOCh2TcmExpectedRxSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmExpectedRxSapi.setStatus("obsolete")


class _JnxIfOtnOCh2TcmExpectedRxDapi_Type(OctetString):
    """Custom type jnxIfOtnOCh2TcmExpectedRxDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxIfOtnOCh2TcmExpectedRxDapi_Type.__name__ = "OctetString"
_JnxIfOtnOCh2TcmExpectedRxDapi_Object = MibTableColumn
jnxIfOtnOCh2TcmExpectedRxDapi = _JnxIfOtnOCh2TcmExpectedRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 11),
    _JnxIfOtnOCh2TcmExpectedRxDapi_Type()
)
jnxIfOtnOCh2TcmExpectedRxDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmExpectedRxDapi.setStatus("obsolete")


class _JnxIfOtnOCh2TcmStatus_Type(Bits):
    """Custom type jnxIfOtnOCh2TcmStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 0),
          ("bdi", 1),
          ("biae", 6),
          ("iae", 2),
          ("ltc", 9),
          ("ssf", 8),
          ("tsf", 7),
          ("ttim", 3))
    )

_JnxIfOtnOCh2TcmStatus_Type.__name__ = "Bits"
_JnxIfOtnOCh2TcmStatus_Object = MibTableColumn
jnxIfOtnOCh2TcmStatus = _JnxIfOtnOCh2TcmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70, 1, 2, 4, 1, 12),
    _JnxIfOtnOCh2TcmStatus_Type()
)
jnxIfOtnOCh2TcmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOtnOCh2TcmStatus.setStatus("obsolete")
_JnxIfOtnNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxIfOtnNotificationPrefix = _JnxIfOtnNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 21, 0)
)

# Managed Objects groups


# Notification objects

jnxIfOtnNotificationAdminStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 21, 0, 1)
)
jnxIfOtnNotificationAdminStatus.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-IFOTN-MIB", "jnxIfOtnAdminState"))
)
if mibBuilder.loadTexts:
    jnxIfOtnNotificationAdminStatus.setStatus(
        "current"
    )

jnxIfOtnNotificationOperStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 21, 0, 2)
)
jnxIfOtnNotificationOperStatus.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-IFOTN-MIB", "jnxIfOtnOperState"))
)
if mibBuilder.loadTexts:
    jnxIfOtnNotificationOperStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IFOTN-MIB",
    **{"JnxIfAdminStates": JnxIfAdminStates,
       "JnxIfOperStates": JnxIfOperStates,
       "JnxIfOtnRate": JnxIfOtnRate,
       "JnxIfOtnFecType": JnxIfOtnFecType,
       "JnxIfOtnLayer": JnxIfOtnLayer,
       "JnxIfOtnType": JnxIfOtnType,
       "JnxIfOtnDirection": JnxIfOtnDirection,
       "JnxIfOtnSeverity": JnxIfOtnSeverity,
       "JnxIfOtnServiceStateAction": JnxIfOtnServiceStateAction,
       "jnxIfOtnMib": jnxIfOtnMib,
       "jnxIfOtn": jnxIfOtn,
       "jnxIfOtnOChCfgTable": jnxIfOtnOChCfgTable,
       "jnxIfOtnOChCfgEntry": jnxIfOtnOChCfgEntry,
       "jnxIfOtnOChCfgContainerIndex": jnxIfOtnOChCfgContainerIndex,
       "jnxIfOtnOChCfgL1Index": jnxIfOtnOChCfgL1Index,
       "jnxIfOtnOChCfgL2Index": jnxIfOtnOChCfgL2Index,
       "jnxIfOtnOChCfgL3Index": jnxIfOtnOChCfgL3Index,
       "jnxIfOtnLocalLoopback": jnxIfOtnLocalLoopback,
       "jnxIfOtnLineLoopback": jnxIfOtnLineLoopback,
       "jnxIfOtnPayloadLoopback": jnxIfOtnPayloadLoopback,
       "jnxIfOtnAdminState": jnxIfOtnAdminState,
       "jnxIfOtnOperState": jnxIfOtnOperState,
       "jnxIfOtnIndex": jnxIfOtnIndex,
       "jnxIfOtnOChStatus": jnxIfOtnOChStatus,
       "jnxIfOtnOChPortMode": jnxIfOtnOChPortMode,
       "jnxIfOtnOTUkCfgTable": jnxIfOtnOTUkCfgTable,
       "jnxIfOtnOTUkCfgEntry": jnxIfOtnOTUkCfgEntry,
       "jnxIfOtnOTUkCfgContainerIndex": jnxIfOtnOTUkCfgContainerIndex,
       "jnxIfOtnOTUkCfgL1Index": jnxIfOtnOTUkCfgL1Index,
       "jnxIfOtnOTUkCfgL2Index": jnxIfOtnOTUkCfgL2Index,
       "jnxIfOtnOTUkCfgL3Index": jnxIfOtnOTUkCfgL3Index,
       "jnxIfOtnOTUkCfgRate": jnxIfOtnOTUkCfgRate,
       "jnxIfOtnOTUkCfgFecMode": jnxIfOtnOTUkCfgFecMode,
       "jnxIfOtnOTUkEnableAutoFrrByteInsert": jnxIfOtnOTUkEnableAutoFrrByteInsert,
       "jnxIfOtnOTUkEnableBERFrrSupport": jnxIfOtnOTUkEnableBERFrrSupport,
       "jnxIfOtnOTUkPreFecBERThresholdMantissa": jnxIfOtnOTUkPreFecBERThresholdMantissa,
       "jnxIfOtnOTUkPreFecBERThresholdExponent": jnxIfOtnOTUkPreFecBERThresholdExponent,
       "jnxIfOtnOTUkPreFecBERThresholdTime": jnxIfOtnOTUkPreFecBERThresholdTime,
       "jnxIfOtnOTUkTIMActEnabled": jnxIfOtnOTUkTIMActEnabled,
       "jnxIfOtnOTUkTxTTI": jnxIfOtnOTUkTxTTI,
       "jnxIfOtnOTUkRxTTI": jnxIfOtnOTUkRxTTI,
       "jnxIfOtnOTUkExpectedRxSapi": jnxIfOtnOTUkExpectedRxSapi,
       "jnxIfOtnOTUkExpectedRxDapi": jnxIfOtnOTUkExpectedRxDapi,
       "jnxIfOtnOTUkStatus": jnxIfOtnOTUkStatus,
       "jnxIfOtnOTUkPreFecBERThresholdClearMantissa": jnxIfOtnOTUkPreFecBERThresholdClearMantissa,
       "jnxIfOtnOTUkPreFecBERThresholdClearExponent": jnxIfOtnOTUkPreFecBERThresholdClearExponent,
       "jnxIfOtnODUkCfgTable": jnxIfOtnODUkCfgTable,
       "jnxIfOtnODUkCfgEntry": jnxIfOtnODUkCfgEntry,
       "jnxIfOtnODUkCfgContainerIndex": jnxIfOtnODUkCfgContainerIndex,
       "jnxIfOtnODUkCfgL1Index": jnxIfOtnODUkCfgL1Index,
       "jnxIfOtnODUkCfgL2Index": jnxIfOtnODUkCfgL2Index,
       "jnxIfOtnODUkCfgL3Index": jnxIfOtnODUkCfgL3Index,
       "jnxIfOtnODUkAPSPCC0": jnxIfOtnODUkAPSPCC0,
       "jnxIfOtnODUkAPSPCC1": jnxIfOtnODUkAPSPCC1,
       "jnxIfOtnODUkAPSPCC2": jnxIfOtnODUkAPSPCC2,
       "jnxIfOtnODUkAPSPCC3": jnxIfOtnODUkAPSPCC3,
       "jnxIfOtnODUkPayloadType": jnxIfOtnODUkPayloadType,
       "jnxIfOtnODUkTIMActEnabled": jnxIfOtnODUkTIMActEnabled,
       "jnxIfOtnODUkTxTTI": jnxIfOtnODUkTxTTI,
       "jnxIfOtnODUkRxTTI": jnxIfOtnODUkRxTTI,
       "jnxIfOtnODUkExpectedRxSapi": jnxIfOtnODUkExpectedRxSapi,
       "jnxIfOtnODUkExpectedRxDapi": jnxIfOtnODUkExpectedRxDapi,
       "jnxIfOtnODUkStatus": jnxIfOtnODUkStatus,
       "jnxIfOtnODUkRxPayloadType": jnxIfOtnODUkRxPayloadType,
       "jnxIfOtnTcmCfgTable": jnxIfOtnTcmCfgTable,
       "jnxIfOtnTcmCfgEntry": jnxIfOtnTcmCfgEntry,
       "jnxIfOtnTcmCfgContainerIndex": jnxIfOtnTcmCfgContainerIndex,
       "jnxIfOtnTcmCfgL1Index": jnxIfOtnTcmCfgL1Index,
       "jnxIfOtnTcmCfgL2Index": jnxIfOtnTcmCfgL2Index,
       "jnxIfOtnTcmCfgL3Index": jnxIfOtnTcmCfgL3Index,
       "jnxIfOtnTcmCfgLevel": jnxIfOtnTcmCfgLevel,
       "jnxIfOtnTCMEnable": jnxIfOtnTCMEnable,
       "jnxIfOtnTcmTxTTI": jnxIfOtnTcmTxTTI,
       "jnxIfOtnTcmRxTTI": jnxIfOtnTcmRxTTI,
       "jnxIfOtnTcmExpectedRxSapi": jnxIfOtnTcmExpectedRxSapi,
       "jnxIfOtnTcmExpectedRxDapi": jnxIfOtnTcmExpectedRxDapi,
       "jnxIfOtnTcmStatus": jnxIfOtnTcmStatus,
       "jnxIfOtnODUkTcmTestTable": jnxIfOtnODUkTcmTestTable,
       "jnxIfOtnODUkTcmTestEntry": jnxIfOtnODUkTcmTestEntry,
       "jnxIfOtnODUkTcmTestLayer": jnxIfOtnODUkTcmTestLayer,
       "jnxIfOtnODUkTcmTestTCMLevel": jnxIfOtnODUkTcmTestTCMLevel,
       "jnxIfOtnODUkTcmInsertAis": jnxIfOtnODUkTcmInsertAis,
       "jnxIfOtnODUkTcmInsertLck": jnxIfOtnODUkTcmInsertLck,
       "jnxIfOtnODUkTcmInsertOci": jnxIfOtnODUkTcmInsertOci,
       "jnxIfOtnODUkPayloadPRBS": jnxIfOtnODUkPayloadPRBS,
       "jnxIfOtnODUkPayloadPRBSResult": jnxIfOtnODUkPayloadPRBSResult,
       "jnxIfOtnODUkTcmDMTable": jnxIfOtnODUkTcmDMTable,
       "jnxIfOtnODUkTcmDMEntry": jnxIfOtnODUkTcmDMEntry,
       "jnxIfOtnODUkTcmDMLayer": jnxIfOtnODUkTcmDMLayer,
       "jnxIfOtnODUkTcmDMLevel": jnxIfOtnODUkTcmDMLevel,
       "jnxIfOtnDMConnectionMonitoringEndpoint": jnxIfOtnDMConnectionMonitoringEndpoint,
       "jnxIfOtnDMBypass": jnxIfOtnDMBypass,
       "jnxIfOtnDMPersistFrames": jnxIfOtnDMPersistFrames,
       "jnxIfOtnDMEnable": jnxIfOtnDMEnable,
       "jnxIfOtnNotificationTrigDefaultHoldtimeUp": jnxIfOtnNotificationTrigDefaultHoldtimeUp,
       "jnxIfOtnNotificationTrigDefaultHoldtimeDown": jnxIfOtnNotificationTrigDefaultHoldtimeDown,
       "jnxIfOtnNotificationTrigTable": jnxIfOtnNotificationTrigTable,
       "jnxIfOtnNotificationTrigEntry": jnxIfOtnNotificationTrigEntry,
       "jnxIfOtnNotificationTrigContainerIndex": jnxIfOtnNotificationTrigContainerIndex,
       "jnxIfOtnNotificationTrigL1Index": jnxIfOtnNotificationTrigL1Index,
       "jnxIfOtnNotificationTrigL2Index": jnxIfOtnNotificationTrigL2Index,
       "jnxIfOtnNotificationTrigL3Index": jnxIfOtnNotificationTrigL3Index,
       "jnxIfOtnNotificationTrigLayer": jnxIfOtnNotificationTrigLayer,
       "jnxIfOtnNotificationTrigTCMLevel": jnxIfOtnNotificationTrigTCMLevel,
       "jnxIfOtnNotificationTrigAlmId": jnxIfOtnNotificationTrigAlmId,
       "jnxIfOtnNotificationTrigSeverity": jnxIfOtnNotificationTrigSeverity,
       "jnxIfOtnNotificationTrigIgnore": jnxIfOtnNotificationTrigIgnore,
       "jnxIfOtnNotificationTrigHoldtimeUp": jnxIfOtnNotificationTrigHoldtimeUp,
       "jnxIfOtnNotificationTrigHoldtimeDown": jnxIfOtnNotificationTrigHoldtimeDown,
       "jnxIfOtnTrigServiceStateAction": jnxIfOtnTrigServiceStateAction,
       "jnxOtnClearAllPMs": jnxOtnClearAllPMs,
       "jnxOtnClearInterfacePMs": jnxOtnClearInterfacePMs,
       "jnxOtnClearInterfaceCurrentPM": jnxOtnClearInterfaceCurrentPM,
       "jnxOtnClearIfPMsTable": jnxOtnClearIfPMsTable,
       "jnxOtnClearIfPMsEntry": jnxOtnClearIfPMsEntry,
       "jnxOtnClearCurrent": jnxOtnClearCurrent,
       "jnxOtnClearInterfaceInterval": jnxOtnClearInterfaceInterval,
       "jnxOtnClearInterfaceDay": jnxOtnClearInterfaceDay,
       "jnxOtnClearInterfaceAll": jnxOtnClearInterfaceAll,
       "jnxIfOtnOCh2": jnxIfOtnOCh2,
       "jnxIfOtnOCh2CfgTable": jnxIfOtnOCh2CfgTable,
       "jnxIfOtnOCh2CfgEntry": jnxIfOtnOCh2CfgEntry,
       "jnxIfOtnOCh2CfgContainerIndex": jnxIfOtnOCh2CfgContainerIndex,
       "jnxIfOtnOCh2CfgL1Index": jnxIfOtnOCh2CfgL1Index,
       "jnxIfOtnOCh2CfgL2Index": jnxIfOtnOCh2CfgL2Index,
       "jnxIfOtnOCh2CfgL3Index": jnxIfOtnOCh2CfgL3Index,
       "jnxIfOtnOCh2CfgL4Index": jnxIfOtnOCh2CfgL4Index,
       "jnxIfOtnOCh2LocalLoopback": jnxIfOtnOCh2LocalLoopback,
       "jnxIfOtnOCh2LineLoopback": jnxIfOtnOCh2LineLoopback,
       "jnxIfOtnOCh2PayloadLoopback": jnxIfOtnOCh2PayloadLoopback,
       "jnxIfOtnOCh2AdminState": jnxIfOtnOCh2AdminState,
       "jnxIfOtnOCh2OperState": jnxIfOtnOCh2OperState,
       "jnxIfOtnOCh2Index": jnxIfOtnOCh2Index,
       "jnxIfOtnOCh2Status": jnxIfOtnOCh2Status,
       "jnxIfOtnOCh2PortMode": jnxIfOtnOCh2PortMode,
       "jnxIfOtnOCh2OTUkCfgTable": jnxIfOtnOCh2OTUkCfgTable,
       "jnxIfOtnOCh2OTUkCfgEntry": jnxIfOtnOCh2OTUkCfgEntry,
       "jnxIfOtnOCh2OTUkCfgContIndx": jnxIfOtnOCh2OTUkCfgContIndx,
       "jnxIfOtnOCh2OTUkCfgL1Index": jnxIfOtnOCh2OTUkCfgL1Index,
       "jnxIfOtnOCh2OTUkCfgL2Index": jnxIfOtnOCh2OTUkCfgL2Index,
       "jnxIfOtnOCh2OTUkCfgL3Index": jnxIfOtnOCh2OTUkCfgL3Index,
       "jnxIfOtnOCh2OTUkCfgL4Index": jnxIfOtnOCh2OTUkCfgL4Index,
       "jnxIfOtnOCh2OTUkCfgRate": jnxIfOtnOCh2OTUkCfgRate,
       "jnxIfOtnOCh2OTUkCfgFecMode": jnxIfOtnOCh2OTUkCfgFecMode,
       "jnxIfOtnOCh2OTUkEnAutoFrrByteIns": jnxIfOtnOCh2OTUkEnAutoFrrByteIns,
       "jnxIfOtnOCh2OTUkEnBERFrrSupport": jnxIfOtnOCh2OTUkEnBERFrrSupport,
       "jnxIfOtnOCh2OTUkPreFecBERThMant": jnxIfOtnOCh2OTUkPreFecBERThMant,
       "jnxIfOtnOCh2OTUkPreFecBERThExpo": jnxIfOtnOCh2OTUkPreFecBERThExpo,
       "jnxIfOtnOCh2OTUkPreFecBERThTime": jnxIfOtnOCh2OTUkPreFecBERThTime,
       "jnxIfOtnOCh2OTUkTIMActEnabled": jnxIfOtnOCh2OTUkTIMActEnabled,
       "jnxIfOtnOCh2OTUkTxTTI": jnxIfOtnOCh2OTUkTxTTI,
       "jnxIfOtnOCh2OTUkRxTTI": jnxIfOtnOCh2OTUkRxTTI,
       "jnxIfOtnOCh2OTUkExpectedRxSapi": jnxIfOtnOCh2OTUkExpectedRxSapi,
       "jnxIfOtnOCh2OTUkExpectedRxDapi": jnxIfOtnOCh2OTUkExpectedRxDapi,
       "jnxIfOtnOCh2OTUkStatus": jnxIfOtnOCh2OTUkStatus,
       "jnxIfOtnOCh2OTUkPreFecBERThClrMn": jnxIfOtnOCh2OTUkPreFecBERThClrMn,
       "jnxIfOtnOCh2OTUkPreFecBERThClrEx": jnxIfOtnOCh2OTUkPreFecBERThClrEx,
       "jnxIfOtnOCh2ODUkCfgTable": jnxIfOtnOCh2ODUkCfgTable,
       "jnxIfOtnOCh2ODUkCfgEntry": jnxIfOtnOCh2ODUkCfgEntry,
       "jnxIfOtnOCh2ODUkCfgContIndx": jnxIfOtnOCh2ODUkCfgContIndx,
       "jnxIfOtnOCh2ODUkCfgL1Index": jnxIfOtnOCh2ODUkCfgL1Index,
       "jnxIfOtnOCh2ODUkCfgL2Index": jnxIfOtnOCh2ODUkCfgL2Index,
       "jnxIfOtnOCh2ODUkCfgL3Index": jnxIfOtnOCh2ODUkCfgL3Index,
       "jnxIfOtnOCh2ODUkCfgL4Index": jnxIfOtnOCh2ODUkCfgL4Index,
       "jnxIfOtnOCh2ODUkAPSPCC0": jnxIfOtnOCh2ODUkAPSPCC0,
       "jnxIfOtnOCh2ODUkAPSPCC1": jnxIfOtnOCh2ODUkAPSPCC1,
       "jnxIfOtnOCh2ODUkAPSPCC2": jnxIfOtnOCh2ODUkAPSPCC2,
       "jnxIfOtnOCh2ODUkAPSPCC3": jnxIfOtnOCh2ODUkAPSPCC3,
       "jnxIfOtnOCh2ODUkPayloadType": jnxIfOtnOCh2ODUkPayloadType,
       "jnxIfOtnOCh2ODUkTIMActEnabled": jnxIfOtnOCh2ODUkTIMActEnabled,
       "jnxIfOtnOCh2ODUkTxTTI": jnxIfOtnOCh2ODUkTxTTI,
       "jnxIfOtnOCh2ODUkRxTTI": jnxIfOtnOCh2ODUkRxTTI,
       "jnxIfOtnOCh2ODUkExpectedRxSapi": jnxIfOtnOCh2ODUkExpectedRxSapi,
       "jnxIfOtnOCh2ODUkExpectedRxDapi": jnxIfOtnOCh2ODUkExpectedRxDapi,
       "jnxIfOtnOCh2ODUkStatus": jnxIfOtnOCh2ODUkStatus,
       "jnxIfOtnOCh2ODUkRxPayloadType": jnxIfOtnOCh2ODUkRxPayloadType,
       "jnxIfOtnOCh2TcmCfgTable": jnxIfOtnOCh2TcmCfgTable,
       "jnxIfOtnOCh2TcmCfgEntry": jnxIfOtnOCh2TcmCfgEntry,
       "jnxIfOtnOCh2TcmCfgContIndx": jnxIfOtnOCh2TcmCfgContIndx,
       "jnxIfOtnOCh2TcmCfgL1Index": jnxIfOtnOCh2TcmCfgL1Index,
       "jnxIfOtnOCh2TcmCfgL2Index": jnxIfOtnOCh2TcmCfgL2Index,
       "jnxIfOtnOCh2TcmCfgL3Index": jnxIfOtnOCh2TcmCfgL3Index,
       "jnxIfOtnOCh2TcmCfgL4Index": jnxIfOtnOCh2TcmCfgL4Index,
       "jnxIfOtnOCh2TcmCfgLevel": jnxIfOtnOCh2TcmCfgLevel,
       "jnxIfOtnOCh2TCMEnable": jnxIfOtnOCh2TCMEnable,
       "jnxIfOtnOCh2TcmTxTTI": jnxIfOtnOCh2TcmTxTTI,
       "jnxIfOtnOCh2TcmRxTTI": jnxIfOtnOCh2TcmRxTTI,
       "jnxIfOtnOCh2TcmExpectedRxSapi": jnxIfOtnOCh2TcmExpectedRxSapi,
       "jnxIfOtnOCh2TcmExpectedRxDapi": jnxIfOtnOCh2TcmExpectedRxDapi,
       "jnxIfOtnOCh2TcmStatus": jnxIfOtnOCh2TcmStatus,
       "jnxIfOtnNotificationPrefix": jnxIfOtnNotificationPrefix,
       "jnxIfOtnNotificationAdminStatus": jnxIfOtnNotificationAdminStatus,
       "jnxIfOtnNotificationOperStatus": jnxIfOtnNotificationOperStatus}
)
