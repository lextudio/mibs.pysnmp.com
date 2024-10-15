# SNMP MIB module (Wellfleet-SYSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SYSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:13 2024
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

(wfSyslogGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSyslogGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSyslog_ObjectIdentity = ObjectIdentity
wfSyslog = _WfSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1)
)


class _WfSyslogDelete_Type(Integer32):
    """Custom type wfSyslogDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfSyslogDelete_Type.__name__ = "Integer32"
_WfSyslogDelete_Object = MibScalar
wfSyslogDelete = _WfSyslogDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 1),
    _WfSyslogDelete_Type()
)
wfSyslogDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogDelete.setStatus("mandatory")


class _WfSyslogDisable_Type(Integer32):
    """Custom type wfSyslogDisable based on Integer32"""
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


_WfSyslogDisable_Type.__name__ = "Integer32"
_WfSyslogDisable_Object = MibScalar
wfSyslogDisable = _WfSyslogDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 2),
    _WfSyslogDisable_Type()
)
wfSyslogDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogDisable.setStatus("mandatory")


class _WfSyslogOperState_Type(Integer32):
    """Custom type wfSyslogOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfSyslogOperState_Type.__name__ = "Integer32"
_WfSyslogOperState_Object = MibScalar
wfSyslogOperState = _WfSyslogOperState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 3),
    _WfSyslogOperState_Type()
)
wfSyslogOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogOperState.setStatus("mandatory")


class _WfSyslogMaxHosts_Type(Integer32):
    """Custom type wfSyslogMaxHosts based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfSyslogMaxHosts_Type.__name__ = "Integer32"
_WfSyslogMaxHosts_Object = MibScalar
wfSyslogMaxHosts = _WfSyslogMaxHosts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 4),
    _WfSyslogMaxHosts_Type()
)
wfSyslogMaxHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogMaxHosts.setStatus("mandatory")


class _WfSyslogPollTimer_Type(Integer32):
    """Custom type wfSyslogPollTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 610000),
    )


_WfSyslogPollTimer_Type.__name__ = "Integer32"
_WfSyslogPollTimer_Object = MibScalar
wfSyslogPollTimer = _WfSyslogPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 5),
    _WfSyslogPollTimer_Type()
)
wfSyslogPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogPollTimer.setStatus("mandatory")
_WfSyslogActTimeSeqHosts_Type = Integer32
_WfSyslogActTimeSeqHosts_Object = MibScalar
wfSyslogActTimeSeqHosts = _WfSyslogActTimeSeqHosts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 6),
    _WfSyslogActTimeSeqHosts_Type()
)
wfSyslogActTimeSeqHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogActTimeSeqHosts.setStatus("mandatory")
_WfSyslogActNonSeqHosts_Type = Integer32
_WfSyslogActNonSeqHosts_Object = MibScalar
wfSyslogActNonSeqHosts = _WfSyslogActNonSeqHosts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 7),
    _WfSyslogActNonSeqHosts_Type()
)
wfSyslogActNonSeqHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogActNonSeqHosts.setStatus("mandatory")
_WfSyslogTotalMsgFwds_Type = Counter32
_WfSyslogTotalMsgFwds_Object = MibScalar
wfSyslogTotalMsgFwds = _WfSyslogTotalMsgFwds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 8),
    _WfSyslogTotalMsgFwds_Type()
)
wfSyslogTotalMsgFwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogTotalMsgFwds.setStatus("mandatory")
_WfSyslogHostTable_Object = MibTable
wfSyslogHostTable = _WfSyslogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2)
)
if mibBuilder.loadTexts:
    wfSyslogHostTable.setStatus("mandatory")
_WfSyslogHostEntry_Object = MibTableRow
wfSyslogHostEntry = _WfSyslogHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1)
)
wfSyslogHostEntry.setIndexNames(
    (0, "Wellfleet-SYSL-MIB", "wfSyslogHostDest"),
)
if mibBuilder.loadTexts:
    wfSyslogHostEntry.setStatus("mandatory")


class _WfSyslogHostDelete_Type(Integer32):
    """Custom type wfSyslogHostDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfSyslogHostDelete_Type.__name__ = "Integer32"
_WfSyslogHostDelete_Object = MibTableColumn
wfSyslogHostDelete = _WfSyslogHostDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 1),
    _WfSyslogHostDelete_Type()
)
wfSyslogHostDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogHostDelete.setStatus("mandatory")


class _WfSyslogHostDisable_Type(Integer32):
    """Custom type wfSyslogHostDisable based on Integer32"""
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


_WfSyslogHostDisable_Type.__name__ = "Integer32"
_WfSyslogHostDisable_Object = MibTableColumn
wfSyslogHostDisable = _WfSyslogHostDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 2),
    _WfSyslogHostDisable_Type()
)
wfSyslogHostDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogHostDisable.setStatus("mandatory")
_WfSyslogHostDest_Type = IpAddress
_WfSyslogHostDest_Object = MibTableColumn
wfSyslogHostDest = _WfSyslogHostDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 3),
    _WfSyslogHostDest_Type()
)
wfSyslogHostDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogHostDest.setStatus("mandatory")


class _WfSyslogHostUDPPort_Type(Integer32):
    """Custom type wfSyslogHostUDPPort based on Integer32"""
    defaultValue = 514


_WfSyslogHostUDPPort_Object = MibTableColumn
wfSyslogHostUDPPort = _WfSyslogHostUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 4),
    _WfSyslogHostUDPPort_Type()
)
wfSyslogHostUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogHostUDPPort.setStatus("mandatory")


class _WfSyslogHostLogFacility_Type(Integer32):
    """Custom type wfSyslogHostLogFacility based on Integer32"""
    defaultValue = 184

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              136,
              144,
              152,
              160,
              168,
              176,
              184)
        )
    )
    namedValues = NamedValues(
        *(("local0", 128),
          ("local1", 136),
          ("local2", 144),
          ("local3", 152),
          ("local4", 160),
          ("local5", 168),
          ("local6", 176),
          ("local7", 184))
    )


_WfSyslogHostLogFacility_Type.__name__ = "Integer32"
_WfSyslogHostLogFacility_Object = MibTableColumn
wfSyslogHostLogFacility = _WfSyslogHostLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 5),
    _WfSyslogHostLogFacility_Type()
)
wfSyslogHostLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogHostLogFacility.setStatus("mandatory")


class _WfSyslogHostTimeSeqEnable_Type(Integer32):
    """Custom type wfSyslogHostTimeSeqEnable based on Integer32"""
    defaultValue = 2

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


_WfSyslogHostTimeSeqEnable_Type.__name__ = "Integer32"
_WfSyslogHostTimeSeqEnable_Object = MibTableColumn
wfSyslogHostTimeSeqEnable = _WfSyslogHostTimeSeqEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 6),
    _WfSyslogHostTimeSeqEnable_Type()
)
wfSyslogHostTimeSeqEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogHostTimeSeqEnable.setStatus("mandatory")


class _WfSyslogHostOperState_Type(Integer32):
    """Custom type wfSyslogHostOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WfSyslogHostOperState_Type.__name__ = "Integer32"
_WfSyslogHostOperState_Object = MibTableColumn
wfSyslogHostOperState = _WfSyslogHostOperState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 7),
    _WfSyslogHostOperState_Type()
)
wfSyslogHostOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogHostOperState.setStatus("mandatory")
_WfSyslogHostMsgFwds_Type = Counter32
_WfSyslogHostMsgFwds_Object = MibTableColumn
wfSyslogHostMsgFwds = _WfSyslogHostMsgFwds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 8),
    _WfSyslogHostMsgFwds_Type()
)
wfSyslogHostMsgFwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogHostMsgFwds.setStatus("mandatory")
_WfSyslogEntityFilterTable_Object = MibTable
wfSyslogEntityFilterTable = _WfSyslogEntityFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3)
)
if mibBuilder.loadTexts:
    wfSyslogEntityFilterTable.setStatus("mandatory")
_WfSyslogEntFltrEntry_Object = MibTableRow
wfSyslogEntFltrEntry = _WfSyslogEntFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1)
)
wfSyslogEntFltrEntry.setIndexNames(
    (0, "Wellfleet-SYSL-MIB", "wfSyslogEntFltrHostIndex"),
    (0, "Wellfleet-SYSL-MIB", "wfSyslogEntFltrNum"),
    (0, "Wellfleet-SYSL-MIB", "wfSyslogEntFltrIndex"),
)
if mibBuilder.loadTexts:
    wfSyslogEntFltrEntry.setStatus("mandatory")


class _WfSyslogEntFltrDelete_Type(Integer32):
    """Custom type wfSyslogEntFltrDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfSyslogEntFltrDelete_Type.__name__ = "Integer32"
_WfSyslogEntFltrDelete_Object = MibTableColumn
wfSyslogEntFltrDelete = _WfSyslogEntFltrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 1),
    _WfSyslogEntFltrDelete_Type()
)
wfSyslogEntFltrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrDelete.setStatus("mandatory")


class _WfSyslogEntFltrDisable_Type(Integer32):
    """Custom type wfSyslogEntFltrDisable based on Integer32"""
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


_WfSyslogEntFltrDisable_Type.__name__ = "Integer32"
_WfSyslogEntFltrDisable_Object = MibTableColumn
wfSyslogEntFltrDisable = _WfSyslogEntFltrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 2),
    _WfSyslogEntFltrDisable_Type()
)
wfSyslogEntFltrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrDisable.setStatus("mandatory")
_WfSyslogEntFltrHostIndex_Type = IpAddress
_WfSyslogEntFltrHostIndex_Object = MibTableColumn
wfSyslogEntFltrHostIndex = _WfSyslogEntFltrHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 3),
    _WfSyslogEntFltrHostIndex_Type()
)
wfSyslogEntFltrHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogEntFltrHostIndex.setStatus("mandatory")
_WfSyslogEntFltrNum_Type = Integer32
_WfSyslogEntFltrNum_Object = MibTableColumn
wfSyslogEntFltrNum = _WfSyslogEntFltrNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 4),
    _WfSyslogEntFltrNum_Type()
)
wfSyslogEntFltrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogEntFltrNum.setStatus("mandatory")
_WfSyslogEntFltrIndex_Type = Integer32
_WfSyslogEntFltrIndex_Object = MibTableColumn
wfSyslogEntFltrIndex = _WfSyslogEntFltrIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 5),
    _WfSyslogEntFltrIndex_Type()
)
wfSyslogEntFltrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogEntFltrIndex.setStatus("mandatory")


class _WfSyslogEntFltrOperState_Type(Integer32):
    """Custom type wfSyslogEntFltrOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WfSyslogEntFltrOperState_Type.__name__ = "Integer32"
_WfSyslogEntFltrOperState_Object = MibTableColumn
wfSyslogEntFltrOperState = _WfSyslogEntFltrOperState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 6),
    _WfSyslogEntFltrOperState_Type()
)
wfSyslogEntFltrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyslogEntFltrOperState.setStatus("mandatory")
_WfSyslogEntFltrLogEvtLowBnd_Type = Integer32
_WfSyslogEntFltrLogEvtLowBnd_Object = MibTableColumn
wfSyslogEntFltrLogEvtLowBnd = _WfSyslogEntFltrLogEvtLowBnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 7),
    _WfSyslogEntFltrLogEvtLowBnd_Type()
)
wfSyslogEntFltrLogEvtLowBnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrLogEvtLowBnd.setStatus("mandatory")


class _WfSyslogEntFltrLogEvtUppBnd_Type(Integer32):
    """Custom type wfSyslogEntFltrLogEvtUppBnd based on Integer32"""
    defaultValue = 255


_WfSyslogEntFltrLogEvtUppBnd_Object = MibTableColumn
wfSyslogEntFltrLogEvtUppBnd = _WfSyslogEntFltrLogEvtUppBnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 8),
    _WfSyslogEntFltrLogEvtUppBnd_Type()
)
wfSyslogEntFltrLogEvtUppBnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrLogEvtUppBnd.setStatus("mandatory")
_WfSyslogEntFltrSevMask_Type = DisplayString
_WfSyslogEntFltrSevMask_Object = MibTableColumn
wfSyslogEntFltrSevMask = _WfSyslogEntFltrSevMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 9),
    _WfSyslogEntFltrSevMask_Type()
)
wfSyslogEntFltrSevMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrSevMask.setStatus("mandatory")
_WfSyslogEntFltrSlotLowBnd_Type = Integer32
_WfSyslogEntFltrSlotLowBnd_Object = MibTableColumn
wfSyslogEntFltrSlotLowBnd = _WfSyslogEntFltrSlotLowBnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 10),
    _WfSyslogEntFltrSlotLowBnd_Type()
)
wfSyslogEntFltrSlotLowBnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrSlotLowBnd.setStatus("mandatory")
_WfSyslogEntFltrSlotUppBnd_Type = Integer32
_WfSyslogEntFltrSlotUppBnd_Object = MibTableColumn
wfSyslogEntFltrSlotUppBnd = _WfSyslogEntFltrSlotUppBnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 11),
    _WfSyslogEntFltrSlotUppBnd_Type()
)
wfSyslogEntFltrSlotUppBnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrSlotUppBnd.setStatus("mandatory")


class _WfSyslogEntFltrFaultMap_Type(Integer32):
    """Custom type wfSyslogEntFltrFaultMap based on Integer32"""
    defaultValue = 3

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
        *(("alert", 2),
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_WfSyslogEntFltrFaultMap_Type.__name__ = "Integer32"
_WfSyslogEntFltrFaultMap_Object = MibTableColumn
wfSyslogEntFltrFaultMap = _WfSyslogEntFltrFaultMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 12),
    _WfSyslogEntFltrFaultMap_Type()
)
wfSyslogEntFltrFaultMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrFaultMap.setStatus("mandatory")


class _WfSyslogEntFltrWarningMap_Type(Integer32):
    """Custom type wfSyslogEntFltrWarningMap based on Integer32"""
    defaultValue = 5

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
        *(("alert", 2),
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_WfSyslogEntFltrWarningMap_Type.__name__ = "Integer32"
_WfSyslogEntFltrWarningMap_Object = MibTableColumn
wfSyslogEntFltrWarningMap = _WfSyslogEntFltrWarningMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 13),
    _WfSyslogEntFltrWarningMap_Type()
)
wfSyslogEntFltrWarningMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrWarningMap.setStatus("mandatory")


class _WfSyslogEntFltrInfoMap_Type(Integer32):
    """Custom type wfSyslogEntFltrInfoMap based on Integer32"""
    defaultValue = 7

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
        *(("alert", 2),
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_WfSyslogEntFltrInfoMap_Type.__name__ = "Integer32"
_WfSyslogEntFltrInfoMap_Object = MibTableColumn
wfSyslogEntFltrInfoMap = _WfSyslogEntFltrInfoMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 14),
    _WfSyslogEntFltrInfoMap_Type()
)
wfSyslogEntFltrInfoMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrInfoMap.setStatus("mandatory")


class _WfSyslogEntFltrTraceMap_Type(Integer32):
    """Custom type wfSyslogEntFltrTraceMap based on Integer32"""
    defaultValue = 8

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
        *(("alert", 2),
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_WfSyslogEntFltrTraceMap_Type.__name__ = "Integer32"
_WfSyslogEntFltrTraceMap_Object = MibTableColumn
wfSyslogEntFltrTraceMap = _WfSyslogEntFltrTraceMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 15),
    _WfSyslogEntFltrTraceMap_Type()
)
wfSyslogEntFltrTraceMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrTraceMap.setStatus("mandatory")


class _WfSyslogEntFltrDebugMap_Type(Integer32):
    """Custom type wfSyslogEntFltrDebugMap based on Integer32"""
    defaultValue = 8

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
        *(("alert", 2),
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_WfSyslogEntFltrDebugMap_Type.__name__ = "Integer32"
_WfSyslogEntFltrDebugMap_Object = MibTableColumn
wfSyslogEntFltrDebugMap = _WfSyslogEntFltrDebugMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 16),
    _WfSyslogEntFltrDebugMap_Type()
)
wfSyslogEntFltrDebugMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrDebugMap.setStatus("mandatory")
_WfSyslogEntFltrName_Type = DisplayString
_WfSyslogEntFltrName_Object = MibTableColumn
wfSyslogEntFltrName = _WfSyslogEntFltrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 17),
    _WfSyslogEntFltrName_Type()
)
wfSyslogEntFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyslogEntFltrName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SYSL-MIB",
    **{"wfSyslog": wfSyslog,
       "wfSyslogDelete": wfSyslogDelete,
       "wfSyslogDisable": wfSyslogDisable,
       "wfSyslogOperState": wfSyslogOperState,
       "wfSyslogMaxHosts": wfSyslogMaxHosts,
       "wfSyslogPollTimer": wfSyslogPollTimer,
       "wfSyslogActTimeSeqHosts": wfSyslogActTimeSeqHosts,
       "wfSyslogActNonSeqHosts": wfSyslogActNonSeqHosts,
       "wfSyslogTotalMsgFwds": wfSyslogTotalMsgFwds,
       "wfSyslogHostTable": wfSyslogHostTable,
       "wfSyslogHostEntry": wfSyslogHostEntry,
       "wfSyslogHostDelete": wfSyslogHostDelete,
       "wfSyslogHostDisable": wfSyslogHostDisable,
       "wfSyslogHostDest": wfSyslogHostDest,
       "wfSyslogHostUDPPort": wfSyslogHostUDPPort,
       "wfSyslogHostLogFacility": wfSyslogHostLogFacility,
       "wfSyslogHostTimeSeqEnable": wfSyslogHostTimeSeqEnable,
       "wfSyslogHostOperState": wfSyslogHostOperState,
       "wfSyslogHostMsgFwds": wfSyslogHostMsgFwds,
       "wfSyslogEntityFilterTable": wfSyslogEntityFilterTable,
       "wfSyslogEntFltrEntry": wfSyslogEntFltrEntry,
       "wfSyslogEntFltrDelete": wfSyslogEntFltrDelete,
       "wfSyslogEntFltrDisable": wfSyslogEntFltrDisable,
       "wfSyslogEntFltrHostIndex": wfSyslogEntFltrHostIndex,
       "wfSyslogEntFltrNum": wfSyslogEntFltrNum,
       "wfSyslogEntFltrIndex": wfSyslogEntFltrIndex,
       "wfSyslogEntFltrOperState": wfSyslogEntFltrOperState,
       "wfSyslogEntFltrLogEvtLowBnd": wfSyslogEntFltrLogEvtLowBnd,
       "wfSyslogEntFltrLogEvtUppBnd": wfSyslogEntFltrLogEvtUppBnd,
       "wfSyslogEntFltrSevMask": wfSyslogEntFltrSevMask,
       "wfSyslogEntFltrSlotLowBnd": wfSyslogEntFltrSlotLowBnd,
       "wfSyslogEntFltrSlotUppBnd": wfSyslogEntFltrSlotUppBnd,
       "wfSyslogEntFltrFaultMap": wfSyslogEntFltrFaultMap,
       "wfSyslogEntFltrWarningMap": wfSyslogEntFltrWarningMap,
       "wfSyslogEntFltrInfoMap": wfSyslogEntFltrInfoMap,
       "wfSyslogEntFltrTraceMap": wfSyslogEntFltrTraceMap,
       "wfSyslogEntFltrDebugMap": wfSyslogEntFltrDebugMap,
       "wfSyslogEntFltrName": wfSyslogEntFltrName}
)
