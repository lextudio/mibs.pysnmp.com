# SNMP MIB module (CISCO-QLLC01-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-QLLC01-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:19 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

snaqllc01 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 6)
)


# Types definitions



class IfIndexType(Integer32):
    """Custom type IfIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class X121Address(OctetString):
    """Custom type X121Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Qllc_ObjectIdentity = ObjectIdentity
qllc = _Qllc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1)
)
_QllcLSAdminTable_Object = MibTable
qllcLSAdminTable = _QllcLSAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1)
)
if mibBuilder.loadTexts:
    qllcLSAdminTable.setStatus("current")
_QllcLSAdminEntry_Object = MibTableRow
qllcLSAdminEntry = _QllcLSAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1)
)
qllcLSAdminEntry.setIndexNames(
    (0, "CISCO-QLLC01-MIB", "qllcLSAdminIfIndex"),
    (0, "CISCO-QLLC01-MIB", "qllcLSAdminLciVcIndex"),
)
if mibBuilder.loadTexts:
    qllcLSAdminEntry.setStatus("current")
_QllcLSAdminIfIndex_Type = IfIndexType
_QllcLSAdminIfIndex_Object = MibTableColumn
qllcLSAdminIfIndex = _QllcLSAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 1),
    _QllcLSAdminIfIndex_Type()
)
qllcLSAdminIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcLSAdminIfIndex.setStatus("current")
_QllcLSAdminLciVcIndex_Type = IfIndexType
_QllcLSAdminLciVcIndex_Object = MibTableColumn
qllcLSAdminLciVcIndex = _QllcLSAdminLciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 2),
    _QllcLSAdminLciVcIndex_Type()
)
qllcLSAdminLciVcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcLSAdminLciVcIndex.setStatus("current")


class _QllcLSAdminCircuitType_Type(Integer32):
    """Custom type qllcLSAdminCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanentVC", 2),
          ("switchedVC", 1))
    )


_QllcLSAdminCircuitType_Type.__name__ = "Integer32"
_QllcLSAdminCircuitType_Object = MibTableColumn
qllcLSAdminCircuitType = _QllcLSAdminCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 3),
    _QllcLSAdminCircuitType_Type()
)
qllcLSAdminCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcLSAdminCircuitType.setStatus("current")


class _QllcLSAdminRole_Type(Integer32):
    """Custom type qllcLSAdminRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("peerToPeer", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_QllcLSAdminRole_Type.__name__ = "Integer32"
_QllcLSAdminRole_Object = MibTableColumn
qllcLSAdminRole = _QllcLSAdminRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 4),
    _QllcLSAdminRole_Type()
)
qllcLSAdminRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcLSAdminRole.setStatus("current")
_QllcLSAdminX25Add_Type = X121Address
_QllcLSAdminX25Add_Object = MibTableColumn
qllcLSAdminX25Add = _QllcLSAdminX25Add_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 5),
    _QllcLSAdminX25Add_Type()
)
qllcLSAdminX25Add.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcLSAdminX25Add.setStatus("current")


class _QllcLSAdminModulo_Type(Integer32):
    """Custom type qllcLSAdminModulo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_QllcLSAdminModulo_Type.__name__ = "Integer32"
_QllcLSAdminModulo_Object = MibTableColumn
qllcLSAdminModulo = _QllcLSAdminModulo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 6),
    _QllcLSAdminModulo_Type()
)
qllcLSAdminModulo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcLSAdminModulo.setStatus("current")
_QllcLSAdminLgX25_Type = Integer32
_QllcLSAdminLgX25_Object = MibTableColumn
qllcLSAdminLgX25 = _QllcLSAdminLgX25_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 1, 1, 7),
    _QllcLSAdminLgX25_Type()
)
qllcLSAdminLgX25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcLSAdminLgX25.setStatus("current")
_QllcLSOperTable_Object = MibTable
qllcLSOperTable = _QllcLSOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2)
)
if mibBuilder.loadTexts:
    qllcLSOperTable.setStatus("current")
_QllcLSOperEntry_Object = MibTableRow
qllcLSOperEntry = _QllcLSOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1)
)
qllcLSOperEntry.setIndexNames(
    (0, "CISCO-QLLC01-MIB", "qllcLSOperIfIndex"),
    (0, "CISCO-QLLC01-MIB", "qllcLSOperLciVcIndex"),
)
if mibBuilder.loadTexts:
    qllcLSOperEntry.setStatus("current")
_QllcLSOperIfIndex_Type = IfIndexType
_QllcLSOperIfIndex_Object = MibTableColumn
qllcLSOperIfIndex = _QllcLSOperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 1),
    _QllcLSOperIfIndex_Type()
)
qllcLSOperIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSOperIfIndex.setStatus("current")
_QllcLSOperLciVcIndex_Type = IfIndexType
_QllcLSOperLciVcIndex_Object = MibTableColumn
qllcLSOperLciVcIndex = _QllcLSOperLciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 2),
    _QllcLSOperLciVcIndex_Type()
)
qllcLSOperLciVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSOperLciVcIndex.setStatus("current")


class _QllcLSOperCircuitType_Type(Integer32):
    """Custom type qllcLSOperCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanentVC", 2),
          ("switchedVC", 1))
    )


_QllcLSOperCircuitType_Type.__name__ = "Integer32"
_QllcLSOperCircuitType_Object = MibTableColumn
qllcLSOperCircuitType = _QllcLSOperCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 3),
    _QllcLSOperCircuitType_Type()
)
qllcLSOperCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSOperCircuitType.setStatus("current")


class _QllcLSOperRole_Type(Integer32):
    """Custom type qllcLSOperRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("peerToPeer", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_QllcLSOperRole_Type.__name__ = "Integer32"
_QllcLSOperRole_Object = MibTableColumn
qllcLSOperRole = _QllcLSOperRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 4),
    _QllcLSOperRole_Type()
)
qllcLSOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSOperRole.setStatus("current")
_QllcLSOperX25Add_Type = X121Address
_QllcLSOperX25Add_Object = MibTableColumn
qllcLSOperX25Add = _QllcLSOperX25Add_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 5),
    _QllcLSOperX25Add_Type()
)
qllcLSOperX25Add.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSOperX25Add.setStatus("current")


class _QllcLSOperModulo_Type(Integer32):
    """Custom type qllcLSOperModulo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_QllcLSOperModulo_Type.__name__ = "Integer32"
_QllcLSOperModulo_Object = MibTableColumn
qllcLSOperModulo = _QllcLSOperModulo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 6),
    _QllcLSOperModulo_Type()
)
qllcLSOperModulo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSOperModulo.setStatus("current")


class _QllcLSOperState_Type(Integer32):
    """Custom type qllcLSOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lsStateClosed", 2),
          ("lsStateClosing", 4),
          ("lsStateInop", 1),
          ("lsStateOpened", 6),
          ("lsStateOpening", 3),
          ("lsStateRecovery", 5))
    )


_QllcLSOperState_Type.__name__ = "Integer32"
_QllcLSOperState_Object = MibTableColumn
qllcLSOperState = _QllcLSOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 7),
    _QllcLSOperState_Type()
)
qllcLSOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSOperState.setStatus("current")
_QllcLSOperLgX25_Type = Integer32
_QllcLSOperLgX25_Object = MibTableColumn
qllcLSOperLgX25 = _QllcLSOperLgX25_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 2, 1, 8),
    _QllcLSOperLgX25_Type()
)
qllcLSOperLgX25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSOperLgX25.setStatus("current")
_QllcLSStatsTable_Object = MibTable
qllcLSStatsTable = _QllcLSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3)
)
if mibBuilder.loadTexts:
    qllcLSStatsTable.setStatus("current")
_QllcLSStatsEntry_Object = MibTableRow
qllcLSStatsEntry = _QllcLSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1)
)
qllcLSStatsEntry.setIndexNames(
    (0, "CISCO-QLLC01-MIB", "qllcLSStatsIfIndex"),
    (0, "CISCO-QLLC01-MIB", "qllcLSStatsLciVcIndex"),
)
if mibBuilder.loadTexts:
    qllcLSStatsEntry.setStatus("current")
_QllcLSStatsIfIndex_Type = IfIndexType
_QllcLSStatsIfIndex_Object = MibTableColumn
qllcLSStatsIfIndex = _QllcLSStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 1),
    _QllcLSStatsIfIndex_Type()
)
qllcLSStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsIfIndex.setStatus("current")
_QllcLSStatsLciVcIndex_Type = IfIndexType
_QllcLSStatsLciVcIndex_Object = MibTableColumn
qllcLSStatsLciVcIndex = _QllcLSStatsLciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 2),
    _QllcLSStatsLciVcIndex_Type()
)
qllcLSStatsLciVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsLciVcIndex.setStatus("current")
_QllcLSStatsXidIn_Type = Counter32
_QllcLSStatsXidIn_Object = MibTableColumn
qllcLSStatsXidIn = _QllcLSStatsXidIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 3),
    _QllcLSStatsXidIn_Type()
)
qllcLSStatsXidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsXidIn.setStatus("current")
_QllcLSStatsXidOut_Type = Counter32
_QllcLSStatsXidOut_Object = MibTableColumn
qllcLSStatsXidOut = _QllcLSStatsXidOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 4),
    _QllcLSStatsXidOut_Type()
)
qllcLSStatsXidOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsXidOut.setStatus("current")
_QllcLSStatsTestIn_Type = Counter32
_QllcLSStatsTestIn_Object = MibTableColumn
qllcLSStatsTestIn = _QllcLSStatsTestIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 5),
    _QllcLSStatsTestIn_Type()
)
qllcLSStatsTestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsTestIn.setStatus("current")
_QllcLSStatsTestOut_Type = Counter32
_QllcLSStatsTestOut_Object = MibTableColumn
qllcLSStatsTestOut = _QllcLSStatsTestOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 6),
    _QllcLSStatsTestOut_Type()
)
qllcLSStatsTestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsTestOut.setStatus("current")
_QllcLSStatsQuenchOff_Type = Counter32
_QllcLSStatsQuenchOff_Object = MibTableColumn
qllcLSStatsQuenchOff = _QllcLSStatsQuenchOff_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 7),
    _QllcLSStatsQuenchOff_Type()
)
qllcLSStatsQuenchOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsQuenchOff.setStatus("current")
_QllcLSStatsQuenchOn_Type = Counter32
_QllcLSStatsQuenchOn_Object = MibTableColumn
qllcLSStatsQuenchOn = _QllcLSStatsQuenchOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 8),
    _QllcLSStatsQuenchOn_Type()
)
qllcLSStatsQuenchOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsQuenchOn.setStatus("current")
_QllcLSStatsInPaks_Type = Counter32
_QllcLSStatsInPaks_Object = MibTableColumn
qllcLSStatsInPaks = _QllcLSStatsInPaks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 9),
    _QllcLSStatsInPaks_Type()
)
qllcLSStatsInPaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsInPaks.setStatus("current")
_QllcLSStatsOutPaks_Type = Counter32
_QllcLSStatsOutPaks_Object = MibTableColumn
qllcLSStatsOutPaks = _QllcLSStatsOutPaks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 10),
    _QllcLSStatsOutPaks_Type()
)
qllcLSStatsOutPaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsOutPaks.setStatus("current")
_QllcLSStatsInBytes_Type = Counter32
_QllcLSStatsInBytes_Object = MibTableColumn
qllcLSStatsInBytes = _QllcLSStatsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 11),
    _QllcLSStatsInBytes_Type()
)
qllcLSStatsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsInBytes.setStatus("current")
_QllcLSStatsOutBytes_Type = Counter32
_QllcLSStatsOutBytes_Object = MibTableColumn
qllcLSStatsOutBytes = _QllcLSStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 12),
    _QllcLSStatsOutBytes_Type()
)
qllcLSStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsOutBytes.setStatus("current")
_QllcLSStatsNumRcvQsms_Type = Counter32
_QllcLSStatsNumRcvQsms_Object = MibTableColumn
qllcLSStatsNumRcvQsms = _QllcLSStatsNumRcvQsms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 13),
    _QllcLSStatsNumRcvQsms_Type()
)
qllcLSStatsNumRcvQsms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumRcvQsms.setStatus("current")
_QllcLSStatsNumSndQsms_Type = Counter32
_QllcLSStatsNumSndQsms_Object = MibTableColumn
qllcLSStatsNumSndQsms = _QllcLSStatsNumSndQsms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 14),
    _QllcLSStatsNumSndQsms_Type()
)
qllcLSStatsNumSndQsms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumSndQsms.setStatus("current")
_QllcLSStatsNumRcvDiscs_Type = Counter32
_QllcLSStatsNumRcvDiscs_Object = MibTableColumn
qllcLSStatsNumRcvDiscs = _QllcLSStatsNumRcvDiscs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 15),
    _QllcLSStatsNumRcvDiscs_Type()
)
qllcLSStatsNumRcvDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumRcvDiscs.setStatus("current")
_QllcLSStatsNumSndDiscs_Type = Counter32
_QllcLSStatsNumSndDiscs_Object = MibTableColumn
qllcLSStatsNumSndDiscs = _QllcLSStatsNumSndDiscs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 16),
    _QllcLSStatsNumSndDiscs_Type()
)
qllcLSStatsNumSndDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumSndDiscs.setStatus("current")
_QllcLSStatsNumRcvDms_Type = Counter32
_QllcLSStatsNumRcvDms_Object = MibTableColumn
qllcLSStatsNumRcvDms = _QllcLSStatsNumRcvDms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 17),
    _QllcLSStatsNumRcvDms_Type()
)
qllcLSStatsNumRcvDms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumRcvDms.setStatus("current")
_QllcLSStatsNumSndDms_Type = Counter32
_QllcLSStatsNumSndDms_Object = MibTableColumn
qllcLSStatsNumSndDms = _QllcLSStatsNumSndDms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 18),
    _QllcLSStatsNumSndDms_Type()
)
qllcLSStatsNumSndDms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumSndDms.setStatus("current")
_QllcLSStatsNumRcvFrmrs_Type = Counter32
_QllcLSStatsNumRcvFrmrs_Object = MibTableColumn
qllcLSStatsNumRcvFrmrs = _QllcLSStatsNumRcvFrmrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 19),
    _QllcLSStatsNumRcvFrmrs_Type()
)
qllcLSStatsNumRcvFrmrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumRcvFrmrs.setStatus("current")
_QllcLSStatsNumSndFrmrs_Type = Counter32
_QllcLSStatsNumSndFrmrs_Object = MibTableColumn
qllcLSStatsNumSndFrmrs = _QllcLSStatsNumSndFrmrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 20),
    _QllcLSStatsNumSndFrmrs_Type()
)
qllcLSStatsNumSndFrmrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumSndFrmrs.setStatus("current")
_QllcLSStatsNumDrops_Type = Counter32
_QllcLSStatsNumDrops_Object = MibTableColumn
qllcLSStatsNumDrops = _QllcLSStatsNumDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 21),
    _QllcLSStatsNumDrops_Type()
)
qllcLSStatsNumDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumDrops.setStatus("current")
_QllcLSStatsNumErrs_Type = Counter32
_QllcLSStatsNumErrs_Object = MibTableColumn
qllcLSStatsNumErrs = _QllcLSStatsNumErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 1, 3, 1, 22),
    _QllcLSStatsNumErrs_Type()
)
qllcLSStatsNumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcLSStatsNumErrs.setStatus("current")
_QllcMibConformance_ObjectIdentity = ObjectIdentity
qllcMibConformance = _QllcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 2)
)
_QllcMibCompliances_ObjectIdentity = ObjectIdentity
qllcMibCompliances = _QllcMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 1)
)
_QllcMibGroups_ObjectIdentity = ObjectIdentity
qllcMibGroups = _QllcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 2)
)

# Managed Objects groups

qllcLSAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 2, 1)
)
qllcLSAdminGroup.setObjects(
      *(("CISCO-QLLC01-MIB", "qllcLSAdminIfIndex"),
        ("CISCO-QLLC01-MIB", "qllcLSAdminLciVcIndex"),
        ("CISCO-QLLC01-MIB", "qllcLSAdminRole"),
        ("CISCO-QLLC01-MIB", "qllcLSAdminCircuitType"),
        ("CISCO-QLLC01-MIB", "qllcLSAdminX25Add"),
        ("CISCO-QLLC01-MIB", "qllcLSAdminModulo"),
        ("CISCO-QLLC01-MIB", "qllcLSAdminLgX25"))
)
if mibBuilder.loadTexts:
    qllcLSAdminGroup.setStatus("current")

qllcLSOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 2, 2)
)
qllcLSOperGroup.setObjects(
      *(("CISCO-QLLC01-MIB", "qllcLSOperIfIndex"),
        ("CISCO-QLLC01-MIB", "qllcLSOperLciVcIndex"),
        ("CISCO-QLLC01-MIB", "qllcLSOperCircuitType"),
        ("CISCO-QLLC01-MIB", "qllcLSOperRole"),
        ("CISCO-QLLC01-MIB", "qllcLSOperX25Add"),
        ("CISCO-QLLC01-MIB", "qllcLSOperModulo"),
        ("CISCO-QLLC01-MIB", "qllcLSOperState"),
        ("CISCO-QLLC01-MIB", "qllcLSOperLgX25"))
)
if mibBuilder.loadTexts:
    qllcLSOperGroup.setStatus("current")

qllcLSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 2, 3)
)
qllcLSStatsGroup.setObjects(
      *(("CISCO-QLLC01-MIB", "qllcLSStatsIfIndex"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsLciVcIndex"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsXidIn"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsXidOut"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsTestIn"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsTestOut"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsQuenchOff"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsQuenchOn"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsInPaks"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsOutPaks"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsInBytes"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsOutBytes"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumRcvQsms"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumSndQsms"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumRcvDiscs"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumSndDiscs"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumRcvDms"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumSndDms"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumRcvFrmrs"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumSndFrmrs"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumDrops"),
        ("CISCO-QLLC01-MIB", "qllcLSStatsNumErrs"))
)
if mibBuilder.loadTexts:
    qllcLSStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qllcMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qllcMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-QLLC01-MIB",
    **{"IfIndexType": IfIndexType,
       "X121Address": X121Address,
       "snaqllc01": snaqllc01,
       "qllc": qllc,
       "qllcLSAdminTable": qllcLSAdminTable,
       "qllcLSAdminEntry": qllcLSAdminEntry,
       "qllcLSAdminIfIndex": qllcLSAdminIfIndex,
       "qllcLSAdminLciVcIndex": qllcLSAdminLciVcIndex,
       "qllcLSAdminCircuitType": qllcLSAdminCircuitType,
       "qllcLSAdminRole": qllcLSAdminRole,
       "qllcLSAdminX25Add": qllcLSAdminX25Add,
       "qllcLSAdminModulo": qllcLSAdminModulo,
       "qllcLSAdminLgX25": qllcLSAdminLgX25,
       "qllcLSOperTable": qllcLSOperTable,
       "qllcLSOperEntry": qllcLSOperEntry,
       "qllcLSOperIfIndex": qllcLSOperIfIndex,
       "qllcLSOperLciVcIndex": qllcLSOperLciVcIndex,
       "qllcLSOperCircuitType": qllcLSOperCircuitType,
       "qllcLSOperRole": qllcLSOperRole,
       "qllcLSOperX25Add": qllcLSOperX25Add,
       "qllcLSOperModulo": qllcLSOperModulo,
       "qllcLSOperState": qllcLSOperState,
       "qllcLSOperLgX25": qllcLSOperLgX25,
       "qllcLSStatsTable": qllcLSStatsTable,
       "qllcLSStatsEntry": qllcLSStatsEntry,
       "qllcLSStatsIfIndex": qllcLSStatsIfIndex,
       "qllcLSStatsLciVcIndex": qllcLSStatsLciVcIndex,
       "qllcLSStatsXidIn": qllcLSStatsXidIn,
       "qllcLSStatsXidOut": qllcLSStatsXidOut,
       "qllcLSStatsTestIn": qllcLSStatsTestIn,
       "qllcLSStatsTestOut": qllcLSStatsTestOut,
       "qllcLSStatsQuenchOff": qllcLSStatsQuenchOff,
       "qllcLSStatsQuenchOn": qllcLSStatsQuenchOn,
       "qllcLSStatsInPaks": qllcLSStatsInPaks,
       "qllcLSStatsOutPaks": qllcLSStatsOutPaks,
       "qllcLSStatsInBytes": qllcLSStatsInBytes,
       "qllcLSStatsOutBytes": qllcLSStatsOutBytes,
       "qllcLSStatsNumRcvQsms": qllcLSStatsNumRcvQsms,
       "qllcLSStatsNumSndQsms": qllcLSStatsNumSndQsms,
       "qllcLSStatsNumRcvDiscs": qllcLSStatsNumRcvDiscs,
       "qllcLSStatsNumSndDiscs": qllcLSStatsNumSndDiscs,
       "qllcLSStatsNumRcvDms": qllcLSStatsNumRcvDms,
       "qllcLSStatsNumSndDms": qllcLSStatsNumSndDms,
       "qllcLSStatsNumRcvFrmrs": qllcLSStatsNumRcvFrmrs,
       "qllcLSStatsNumSndFrmrs": qllcLSStatsNumSndFrmrs,
       "qllcLSStatsNumDrops": qllcLSStatsNumDrops,
       "qllcLSStatsNumErrs": qllcLSStatsNumErrs,
       "qllcMibConformance": qllcMibConformance,
       "qllcMibCompliances": qllcMibCompliances,
       "qllcMibCompliance": qllcMibCompliance,
       "qllcMibGroups": qllcMibGroups,
       "qllcLSAdminGroup": qllcLSAdminGroup,
       "qllcLSOperGroup": qllcLSOperGroup,
       "qllcLSStatsGroup": qllcLSStatsGroup}
)
