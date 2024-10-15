# SNMP MIB module (SCSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:04 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

scspMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 2001)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScspPIDType(Integer32, TextualConvention):
    status = "current"
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
        *(("atmarp", 1),
          ("dhcp", 4),
          ("lnni", 5),
          ("mars", 3),
          ("nhrp", 2))
    )



class ScspHFSMStateType(Integer32, TextualConvention):
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
        *(("biConn", 4),
          ("down", 1),
          ("uniConn", 3),
          ("waiting", 2))
    )



class ScspCAFSMStateType(Integer32, TextualConvention):
    status = "current"
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
        *(("aligned", 5),
          ("cacheSumm", 3),
          ("cacheUpdate", 4),
          ("down", 1),
          ("msNego", 2))
    )



class SCSPVPIInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class SCSPVCIInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_ScspObjects_ObjectIdentity = ObjectIdentity
scspObjects = _ScspObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 2001, 1)
)
_ScspServerGroupTable_Object = MibTable
scspServerGroupTable = _ScspServerGroupTable_Object(
    (1, 3, 6, 1, 3, 2001, 1, 1)
)
if mibBuilder.loadTexts:
    scspServerGroupTable.setStatus("current")
_ScspServerGroupEntry_Object = MibTableRow
scspServerGroupEntry = _ScspServerGroupEntry_Object(
    (1, 3, 6, 1, 3, 2001, 1, 1, 1)
)
scspServerGroupEntry.setIndexNames(
    (0, "SCSP-MIB", "scspServerGroupID"),
    (0, "SCSP-MIB", "scspServerGroupPID"),
)
if mibBuilder.loadTexts:
    scspServerGroupEntry.setStatus("current")


class _ScspServerGroupID_Type(Integer32):
    """Custom type scspServerGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspServerGroupID_Type.__name__ = "Integer32"
_ScspServerGroupID_Object = MibTableColumn
scspServerGroupID = _ScspServerGroupID_Object(
    (1, 3, 6, 1, 3, 2001, 1, 1, 1, 1),
    _ScspServerGroupID_Type()
)
scspServerGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scspServerGroupID.setStatus("current")
_ScspServerGroupPID_Type = ScspPIDType
_ScspServerGroupPID_Object = MibTableColumn
scspServerGroupPID = _ScspServerGroupPID_Object(
    (1, 3, 6, 1, 3, 2001, 1, 1, 1, 2),
    _ScspServerGroupPID_Type()
)
scspServerGroupPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scspServerGroupPID.setStatus("current")
_ScspServerGroupRowStatus_Type = RowStatus
_ScspServerGroupRowStatus_Object = MibTableColumn
scspServerGroupRowStatus = _ScspServerGroupRowStatus_Object(
    (1, 3, 6, 1, 3, 2001, 1, 1, 1, 3),
    _ScspServerGroupRowStatus_Type()
)
scspServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspServerGroupRowStatus.setStatus("current")
_ScspLSTable_Object = MibTable
scspLSTable = _ScspLSTable_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2)
)
if mibBuilder.loadTexts:
    scspLSTable.setStatus("current")
_ScspLSEntry_Object = MibTableRow
scspLSEntry = _ScspLSEntry_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1)
)
scspLSEntry.setIndexNames(
    (0, "SCSP-MIB", "scspServerGroupID"),
    (0, "SCSP-MIB", "scspServerGroupPID"),
    (0, "SCSP-MIB", "scspLSID"),
)
if mibBuilder.loadTexts:
    scspLSEntry.setStatus("current")


class _ScspLSID_Type(OctetString):
    """Custom type scspLSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ScspLSID_Type.__name__ = "OctetString"
_ScspLSID_Object = MibTableColumn
scspLSID = _ScspLSID_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1, 1),
    _ScspLSID_Type()
)
scspLSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scspLSID.setStatus("current")


class _ScspLSHelloInterval_Type(Integer32):
    """Custom type scspLSHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspLSHelloInterval_Type.__name__ = "Integer32"
_ScspLSHelloInterval_Object = MibTableColumn
scspLSHelloInterval = _ScspLSHelloInterval_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1, 2),
    _ScspLSHelloInterval_Type()
)
scspLSHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspLSHelloInterval.setStatus("current")


class _ScspLSDeadFactor_Type(Integer32):
    """Custom type scspLSDeadFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspLSDeadFactor_Type.__name__ = "Integer32"
_ScspLSDeadFactor_Object = MibTableColumn
scspLSDeadFactor = _ScspLSDeadFactor_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1, 3),
    _ScspLSDeadFactor_Type()
)
scspLSDeadFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspLSDeadFactor.setStatus("current")


class _ScspLSCAReXmInterval_Type(Integer32):
    """Custom type scspLSCAReXmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspLSCAReXmInterval_Type.__name__ = "Integer32"
_ScspLSCAReXmInterval_Object = MibTableColumn
scspLSCAReXmInterval = _ScspLSCAReXmInterval_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1, 4),
    _ScspLSCAReXmInterval_Type()
)
scspLSCAReXmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspLSCAReXmInterval.setStatus("current")


class _ScspLSCSUSReXmtInterval_Type(Integer32):
    """Custom type scspLSCSUSReXmtInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspLSCSUSReXmtInterval_Type.__name__ = "Integer32"
_ScspLSCSUSReXmtInterval_Object = MibTableColumn
scspLSCSUSReXmtInterval = _ScspLSCSUSReXmtInterval_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1, 5),
    _ScspLSCSUSReXmtInterval_Type()
)
scspLSCSUSReXmtInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspLSCSUSReXmtInterval.setStatus("current")


class _ScspLSCSUReXmtInterval_Type(Integer32):
    """Custom type scspLSCSUReXmtInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspLSCSUReXmtInterval_Type.__name__ = "Integer32"
_ScspLSCSUReXmtInterval_Object = MibTableColumn
scspLSCSUReXmtInterval = _ScspLSCSUReXmtInterval_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1, 6),
    _ScspLSCSUReXmtInterval_Type()
)
scspLSCSUReXmtInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspLSCSUReXmtInterval.setStatus("current")


class _ScspLSCSAMaxReXmt_Type(Integer32):
    """Custom type scspLSCSAMaxReXmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspLSCSAMaxReXmt_Type.__name__ = "Integer32"
_ScspLSCSAMaxReXmt_Object = MibTableColumn
scspLSCSAMaxReXmt = _ScspLSCSAMaxReXmt_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1, 7),
    _ScspLSCSAMaxReXmt_Type()
)
scspLSCSAMaxReXmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspLSCSAMaxReXmt.setStatus("current")
_ScspLSRowStatus_Type = RowStatus
_ScspLSRowStatus_Object = MibTableColumn
scspLSRowStatus = _ScspLSRowStatus_Object(
    (1, 3, 6, 1, 3, 2001, 1, 2, 1, 8),
    _ScspLSRowStatus_Type()
)
scspLSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspLSRowStatus.setStatus("current")
_ScspDCSTable_Object = MibTable
scspDCSTable = _ScspDCSTable_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3)
)
if mibBuilder.loadTexts:
    scspDCSTable.setStatus("current")
_ScspDCSEntry_Object = MibTableRow
scspDCSEntry = _ScspDCSEntry_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1)
)
scspDCSEntry.setIndexNames(
    (0, "SCSP-MIB", "scspServerGroupID"),
    (0, "SCSP-MIB", "scspServerGroupPID"),
    (0, "SCSP-MIB", "scspDCSID"),
)
if mibBuilder.loadTexts:
    scspDCSEntry.setStatus("current")


class _ScspDCSID_Type(OctetString):
    """Custom type scspDCSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ScspDCSID_Type.__name__ = "OctetString"
_ScspDCSID_Object = MibTableColumn
scspDCSID = _ScspDCSID_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 1),
    _ScspDCSID_Type()
)
scspDCSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scspDCSID.setStatus("current")
_ScspDCSCAFSMState_Type = ScspCAFSMStateType
_ScspDCSCAFSMState_Object = MibTableColumn
scspDCSCAFSMState = _ScspDCSCAFSMState_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 2),
    _ScspDCSCAFSMState_Type()
)
scspDCSCAFSMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCAFSMState.setStatus("current")


class _ScspDCSCASequence_Type(Integer32):
    """Custom type scspDCSCASequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ScspDCSCASequence_Type.__name__ = "Integer32"
_ScspDCSCASequence_Object = MibTableColumn
scspDCSCASequence = _ScspDCSCASequence_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 3),
    _ScspDCSCASequence_Type()
)
scspDCSCASequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCASequence.setStatus("current")
_ScspDCSCAIn_Type = Counter32
_ScspDCSCAIn_Object = MibTableColumn
scspDCSCAIn = _ScspDCSCAIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 4),
    _ScspDCSCAIn_Type()
)
scspDCSCAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCAIn.setStatus("current")
_ScspDCSCAOut_Type = Counter32
_ScspDCSCAOut_Object = MibTableColumn
scspDCSCAOut = _ScspDCSCAOut_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 5),
    _ScspDCSCAOut_Type()
)
scspDCSCAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCAOut.setStatus("current")
_ScspDCSCAInvalidIn_Type = Counter32
_ScspDCSCAInvalidIn_Object = MibTableColumn
scspDCSCAInvalidIn = _ScspDCSCAInvalidIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 6),
    _ScspDCSCAInvalidIn_Type()
)
scspDCSCAInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCAInvalidIn.setStatus("current")
_ScspDCSCADuplicateIn_Type = Counter32
_ScspDCSCADuplicateIn_Object = MibTableColumn
scspDCSCADuplicateIn = _ScspDCSCADuplicateIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 7),
    _ScspDCSCADuplicateIn_Type()
)
scspDCSCADuplicateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCADuplicateIn.setStatus("current")


class _ScspDCSMSState_Type(Integer32):
    """Custom type scspDCSMSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_ScspDCSMSState_Type.__name__ = "Integer32"
_ScspDCSMSState_Object = MibTableColumn
scspDCSMSState = _ScspDCSMSState_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 8),
    _ScspDCSMSState_Type()
)
scspDCSMSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSMSState.setStatus("current")
_ScspDCSCSUSIn_Type = Counter32
_ScspDCSCSUSIn_Object = MibTableColumn
scspDCSCSUSIn = _ScspDCSCSUSIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 9),
    _ScspDCSCSUSIn_Type()
)
scspDCSCSUSIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSUSIn.setStatus("current")
_ScspDCSCSUSOut_Type = Counter32
_ScspDCSCSUSOut_Object = MibTableColumn
scspDCSCSUSOut = _ScspDCSCSUSOut_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 10),
    _ScspDCSCSUSOut_Type()
)
scspDCSCSUSOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSUSOut.setStatus("current")
_ScspDCSCSUSInvalidIn_Type = Counter32
_ScspDCSCSUSInvalidIn_Object = MibTableColumn
scspDCSCSUSInvalidIn = _ScspDCSCSUSInvalidIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 11),
    _ScspDCSCSUSInvalidIn_Type()
)
scspDCSCSUSInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSUSInvalidIn.setStatus("current")
_ScspDCSCSURequestIn_Type = Counter32
_ScspDCSCSURequestIn_Object = MibTableColumn
scspDCSCSURequestIn = _ScspDCSCSURequestIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 12),
    _ScspDCSCSURequestIn_Type()
)
scspDCSCSURequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSURequestIn.setStatus("current")
_ScspDCSCSUReplyOut_Type = Counter32
_ScspDCSCSUReplyOut_Object = MibTableColumn
scspDCSCSUReplyOut = _ScspDCSCSUReplyOut_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 13),
    _ScspDCSCSUReplyOut_Type()
)
scspDCSCSUReplyOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSUReplyOut.setStatus("current")
_ScspDCSCSURequestOut_Type = Counter32
_ScspDCSCSURequestOut_Object = MibTableColumn
scspDCSCSURequestOut = _ScspDCSCSURequestOut_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 14),
    _ScspDCSCSURequestOut_Type()
)
scspDCSCSURequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSURequestOut.setStatus("current")
_ScspDCSCSUReplyIn_Type = Counter32
_ScspDCSCSUReplyIn_Object = MibTableColumn
scspDCSCSUReplyIn = _ScspDCSCSUReplyIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 15),
    _ScspDCSCSUReplyIn_Type()
)
scspDCSCSUReplyIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSUReplyIn.setStatus("current")
_ScspDCSCSUInvalidRequestIn_Type = Counter32
_ScspDCSCSUInvalidRequestIn_Object = MibTableColumn
scspDCSCSUInvalidRequestIn = _ScspDCSCSUInvalidRequestIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 16),
    _ScspDCSCSUInvalidRequestIn_Type()
)
scspDCSCSUInvalidRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSUInvalidRequestIn.setStatus("current")
_ScspDCSCSUInvalidReplyIn_Type = Counter32
_ScspDCSCSUInvalidReplyIn_Object = MibTableColumn
scspDCSCSUInvalidReplyIn = _ScspDCSCSUInvalidReplyIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 17),
    _ScspDCSCSUInvalidReplyIn_Type()
)
scspDCSCSUInvalidReplyIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSUInvalidReplyIn.setStatus("current")
_ScspDCSCSAIn_Type = Counter32
_ScspDCSCSAIn_Object = MibTableColumn
scspDCSCSAIn = _ScspDCSCSAIn_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 18),
    _ScspDCSCSAIn_Type()
)
scspDCSCSAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSAIn.setStatus("current")
_ScspDCSCSAOut_Type = Counter32
_ScspDCSCSAOut_Object = MibTableColumn
scspDCSCSAOut = _ScspDCSCSAOut_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 19),
    _ScspDCSCSAOut_Type()
)
scspDCSCSAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSAOut.setStatus("current")
_ScspDCSCSAReXmted_Type = Counter32
_ScspDCSCSAReXmted_Object = MibTableColumn
scspDCSCSAReXmted = _ScspDCSCSAReXmted_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 20),
    _ScspDCSCSAReXmted_Type()
)
scspDCSCSAReXmted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSAReXmted.setStatus("current")


class _ScspDCSCSAReXmtQDepth_Type(Integer32):
    """Custom type scspDCSCSAReXmtQDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspDCSCSAReXmtQDepth_Type.__name__ = "Integer32"
_ScspDCSCSAReXmtQDepth_Object = MibTableColumn
scspDCSCSAReXmtQDepth = _ScspDCSCSAReXmtQDepth_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 21),
    _ScspDCSCSAReXmtQDepth_Type()
)
scspDCSCSAReXmtQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspDCSCSAReXmtQDepth.setStatus("current")
_ScspDCSRowStatus_Type = RowStatus
_ScspDCSRowStatus_Object = MibTableColumn
scspDCSRowStatus = _ScspDCSRowStatus_Object(
    (1, 3, 6, 1, 3, 2001, 1, 3, 1, 22),
    _ScspDCSRowStatus_Type()
)
scspDCSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspDCSRowStatus.setStatus("current")
_ScspNotifications_ObjectIdentity = ObjectIdentity
scspNotifications = _ScspNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 2001, 2)
)
_ScspConformance_ObjectIdentity = ObjectIdentity
scspConformance = _ScspConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 2001, 3)
)
_ScspCompliances_ObjectIdentity = ObjectIdentity
scspCompliances = _ScspCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 2001, 3, 1)
)
_ScspGroups_ObjectIdentity = ObjectIdentity
scspGroups = _ScspGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 2001, 3, 2)
)

# Managed Objects groups

scspLSGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 2001, 3, 2, 1)
)
scspLSGroup.setObjects(
      *(("SCSP-MIB", "scspServerGroupID"),
        ("SCSP-MIB", "scspServerGroupPID"),
        ("SCSP-MIB", "scspLSID"),
        ("SCSP-MIB", "scspLSHelloInterval"),
        ("SCSP-MIB", "scspLSCAReXmInterval"),
        ("SCSP-MIB", "scspLSCSUSReXmtInterval"),
        ("SCSP-MIB", "scspLSCSUReXmtInterval"),
        ("SCSP-MIB", "scspLSCSAMaxReXmt"),
        ("SCSP-MIB", "scspLSDeadFactor"))
)
if mibBuilder.loadTexts:
    scspLSGroup.setStatus("current")

scspDCSGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 2001, 3, 2, 2)
)
scspDCSGroup.setObjects(
      *(("SCSP-MIB", "scspDCSID"),
        ("SCSP-MIB", "scspDCSCAFSMState"),
        ("SCSP-MIB", "scspDCSCAIn"),
        ("SCSP-MIB", "scspDCSCAOut"),
        ("SCSP-MIB", "scspDCSCAInvalidIn"),
        ("SCSP-MIB", "scspDCSCADuplicateIn"),
        ("SCSP-MIB", "scspDCSMSState"),
        ("SCSP-MIB", "scspDCSCSUSIn"),
        ("SCSP-MIB", "scspDCSCSUSOut"),
        ("SCSP-MIB", "scspDCSCSURequestIn"),
        ("SCSP-MIB", "scspDCSCSURequestOut"),
        ("SCSP-MIB", "scspDCSCSUReplyOut"),
        ("SCSP-MIB", "scspDCSCSUReplyIn"),
        ("SCSP-MIB", "scspDCSCSUInvalidRequestIn"),
        ("SCSP-MIB", "scspDCSCSUInvalidReplyIn"),
        ("SCSP-MIB", "scspDCSCSAIn"),
        ("SCSP-MIB", "scspDCSCSAOut"),
        ("SCSP-MIB", "scspDCSCSAReXmted"),
        ("SCSP-MIB", "scspDCSCSAReXmtQDepth"))
)
if mibBuilder.loadTexts:
    scspDCSGroup.setStatus("current")


# Notification objects

scspCSAReXmExceed = NotificationType(
    (1, 3, 6, 1, 3, 2001, 2, 1)
)
scspCSAReXmExceed.setObjects(
      *(("SCSP-MIB", "scspServerGroupID"),
        ("SCSP-MIB", "scspServerGroupPID"),
        ("SCSP-MIB", "scspDCSID"))
)
if mibBuilder.loadTexts:
    scspCSAReXmExceed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

scspCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 2001, 3, 1, 1)
)
if mibBuilder.loadTexts:
    scspCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCSP-MIB",
    **{"ScspPIDType": ScspPIDType,
       "ScspHFSMStateType": ScspHFSMStateType,
       "ScspCAFSMStateType": ScspCAFSMStateType,
       "SCSPVPIInteger": SCSPVPIInteger,
       "SCSPVCIInteger": SCSPVCIInteger,
       "scspMIB": scspMIB,
       "scspObjects": scspObjects,
       "scspServerGroupTable": scspServerGroupTable,
       "scspServerGroupEntry": scspServerGroupEntry,
       "scspServerGroupID": scspServerGroupID,
       "scspServerGroupPID": scspServerGroupPID,
       "scspServerGroupRowStatus": scspServerGroupRowStatus,
       "scspLSTable": scspLSTable,
       "scspLSEntry": scspLSEntry,
       "scspLSID": scspLSID,
       "scspLSHelloInterval": scspLSHelloInterval,
       "scspLSDeadFactor": scspLSDeadFactor,
       "scspLSCAReXmInterval": scspLSCAReXmInterval,
       "scspLSCSUSReXmtInterval": scspLSCSUSReXmtInterval,
       "scspLSCSUReXmtInterval": scspLSCSUReXmtInterval,
       "scspLSCSAMaxReXmt": scspLSCSAMaxReXmt,
       "scspLSRowStatus": scspLSRowStatus,
       "scspDCSTable": scspDCSTable,
       "scspDCSEntry": scspDCSEntry,
       "scspDCSID": scspDCSID,
       "scspDCSCAFSMState": scspDCSCAFSMState,
       "scspDCSCASequence": scspDCSCASequence,
       "scspDCSCAIn": scspDCSCAIn,
       "scspDCSCAOut": scspDCSCAOut,
       "scspDCSCAInvalidIn": scspDCSCAInvalidIn,
       "scspDCSCADuplicateIn": scspDCSCADuplicateIn,
       "scspDCSMSState": scspDCSMSState,
       "scspDCSCSUSIn": scspDCSCSUSIn,
       "scspDCSCSUSOut": scspDCSCSUSOut,
       "scspDCSCSUSInvalidIn": scspDCSCSUSInvalidIn,
       "scspDCSCSURequestIn": scspDCSCSURequestIn,
       "scspDCSCSUReplyOut": scspDCSCSUReplyOut,
       "scspDCSCSURequestOut": scspDCSCSURequestOut,
       "scspDCSCSUReplyIn": scspDCSCSUReplyIn,
       "scspDCSCSUInvalidRequestIn": scspDCSCSUInvalidRequestIn,
       "scspDCSCSUInvalidReplyIn": scspDCSCSUInvalidReplyIn,
       "scspDCSCSAIn": scspDCSCSAIn,
       "scspDCSCSAOut": scspDCSCSAOut,
       "scspDCSCSAReXmted": scspDCSCSAReXmted,
       "scspDCSCSAReXmtQDepth": scspDCSCSAReXmtQDepth,
       "scspDCSRowStatus": scspDCSRowStatus,
       "scspNotifications": scspNotifications,
       "scspCSAReXmExceed": scspCSAReXmExceed,
       "scspConformance": scspConformance,
       "scspCompliances": scspCompliances,
       "scspCompliance": scspCompliance,
       "scspGroups": scspGroups,
       "scspLSGroup": scspLSGroup,
       "scspDCSGroup": scspDCSGroup}
)
