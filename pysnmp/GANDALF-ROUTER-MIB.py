# SNMP MIB module (GANDALF-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GANDALF-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:40 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
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
    "NotificationType",
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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gandalf_ObjectIdentity = ObjectIdentity
gandalf = _Gandalf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64)
)
_Gandalf_router_ObjectIdentity = ObjectIdentity
gandalf_router = _Gandalf_router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11)
)
_GrGenerationX_ObjectIdentity = ObjectIdentity
grGenerationX = _GrGenerationX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1)
)
_GrGeneral_ObjectIdentity = ObjectIdentity
grGeneral = _GrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1)
)


class _GrSerNum_Type(DisplayString):
    """Custom type grSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrSerNum_Type.__name__ = "DisplayString"
_GrSerNum_Object = MibScalar
grSerNum = _GrSerNum_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 1),
    _GrSerNum_Type()
)
grSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grSerNum.setStatus("mandatory")


class _GrSystemName_Type(DisplayString):
    """Custom type grSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_GrSystemName_Type.__name__ = "DisplayString"
_GrSystemName_Object = MibScalar
grSystemName = _GrSystemName_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 2),
    _GrSystemName_Type()
)
grSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grSystemName.setStatus("mandatory")


class _GrSystemPasswd_Type(DisplayString):
    """Custom type grSystemPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrSystemPasswd_Type.__name__ = "DisplayString"
_GrSystemPasswd_Object = MibScalar
grSystemPasswd = _GrSystemPasswd_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 3),
    _GrSystemPasswd_Type()
)
grSystemPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grSystemPasswd.setStatus("mandatory")


class _GrdBaseRev_Type(DisplayString):
    """Custom type grdBaseRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrdBaseRev_Type.__name__ = "DisplayString"
_GrdBaseRev_Object = MibScalar
grdBaseRev = _GrdBaseRev_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 4),
    _GrdBaseRev_Type()
)
grdBaseRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grdBaseRev.setStatus("mandatory")


class _GrSoftwareRev_Type(DisplayString):
    """Custom type grSoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrSoftwareRev_Type.__name__ = "DisplayString"
_GrSoftwareRev_Object = MibScalar
grSoftwareRev = _GrSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 5),
    _GrSoftwareRev_Type()
)
grSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grSoftwareRev.setStatus("mandatory")


class _GrFirmwareRev_Type(DisplayString):
    """Custom type grFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrFirmwareRev_Type.__name__ = "DisplayString"
_GrFirmwareRev_Object = MibScalar
grFirmwareRev = _GrFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 6),
    _GrFirmwareRev_Type()
)
grFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grFirmwareRev.setStatus("mandatory")


class _GrReset_Type(Integer32):
    """Custom type grReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("hardReset", 1)
    )


_GrReset_Type.__name__ = "Integer32"
_GrReset_Object = MibScalar
grReset = _GrReset_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 7),
    _GrReset_Type()
)
grReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grReset.setStatus("mandatory")


class _GrDateAndTime_Type(OctetString):
    """Custom type grDateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_GrDateAndTime_Type.__name__ = "OctetString"
_GrDateAndTime_Object = MibScalar
grDateAndTime = _GrDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 8),
    _GrDateAndTime_Type()
)
grDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grDateAndTime.setStatus("mandatory")


class _GrSwitchPosition_Type(Integer32):
    """Custom type grSwitchPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("wan", 2))
    )


_GrSwitchPosition_Type.__name__ = "Integer32"
_GrSwitchPosition_Object = MibScalar
grSwitchPosition = _GrSwitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 1, 9),
    _GrSwitchPosition_Type()
)
grSwitchPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grSwitchPosition.setStatus("mandatory")
_GrPhysPortGroup_ObjectIdentity = ObjectIdentity
grPhysPortGroup = _GrPhysPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2)
)
_GrPhysNameTable_Object = MibTable
grPhysNameTable = _GrPhysNameTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    grPhysNameTable.setStatus("mandatory")
_GrPhysNameEntry_Object = MibTableRow
grPhysNameEntry = _GrPhysNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 1, 1)
)
grPhysNameEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grPhysNameEntry.setStatus("mandatory")


class _GrPhysPortName_Type(DisplayString):
    """Custom type grPhysPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrPhysPortName_Type.__name__ = "DisplayString"
_GrPhysPortName_Object = MibTableColumn
grPhysPortName = _GrPhysPortName_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 1, 1, 1),
    _GrPhysPortName_Type()
)
grPhysPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysPortName.setStatus("mandatory")
_GrPhysPortTable_Object = MibTable
grPhysPortTable = _GrPhysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 2)
)
if mibBuilder.loadTexts:
    grPhysPortTable.setStatus("mandatory")
_GrPhysPortEntry_Object = MibTableRow
grPhysPortEntry = _GrPhysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 2, 1)
)
grPhysPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grPhysPortEntry.setStatus("mandatory")


class _GrPhysPortWanType_Type(Integer32):
    """Custom type grPhysPortWanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlSignal", 3),
          ("nonSwitched", 1),
          ("v25bis", 2))
    )


_GrPhysPortWanType_Type.__name__ = "Integer32"
_GrPhysPortWanType_Object = MibTableColumn
grPhysPortWanType = _GrPhysPortWanType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 2, 1, 1),
    _GrPhysPortWanType_Type()
)
grPhysPortWanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grPhysPortWanType.setStatus("mandatory")


class _GrPhysPortSignalling_Type(Integer32):
    """Custom type grPhysPortSignalling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 1),
          ("v11", 2),
          ("v35", 3))
    )


_GrPhysPortSignalling_Type.__name__ = "Integer32"
_GrPhysPortSignalling_Object = MibTableColumn
grPhysPortSignalling = _GrPhysPortSignalling_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 2, 1, 2),
    _GrPhysPortSignalling_Type()
)
grPhysPortSignalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysPortSignalling.setStatus("mandatory")
_GrPhysPortSpeed_Type = Integer32
_GrPhysPortSpeed_Object = MibTableColumn
grPhysPortSpeed = _GrPhysPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 2, 1, 3),
    _GrPhysPortSpeed_Type()
)
grPhysPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grPhysPortSpeed.setStatus("mandatory")


class _GrPhysPortCallType_Type(Integer32):
    """Custom type grPhysPortCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("both", 3),
          ("originate", 1))
    )


_GrPhysPortCallType_Type.__name__ = "Integer32"
_GrPhysPortCallType_Object = MibTableColumn
grPhysPortCallType = _GrPhysPortCallType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 2, 1, 4),
    _GrPhysPortCallType_Type()
)
grPhysPortCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grPhysPortCallType.setStatus("mandatory")


class _GrPhysPortHoldOff_Type(Integer32):
    """Custom type grPhysPortHoldOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GrPhysPortHoldOff_Type.__name__ = "Integer32"
_GrPhysPortHoldOff_Object = MibTableColumn
grPhysPortHoldOff = _GrPhysPortHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 2, 1, 5),
    _GrPhysPortHoldOff_Type()
)
grPhysPortHoldOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grPhysPortHoldOff.setStatus("mandatory")


class _GrPhysPortPool_Type(DisplayString):
    """Custom type grPhysPortPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrPhysPortPool_Type.__name__ = "DisplayString"
_GrPhysPortPool_Object = MibTableColumn
grPhysPortPool = _GrPhysPortPool_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 2, 1, 6),
    _GrPhysPortPool_Type()
)
grPhysPortPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grPhysPortPool.setStatus("mandatory")
_GrPhysWanStatsTable_Object = MibTable
grPhysWanStatsTable = _GrPhysWanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3)
)
if mibBuilder.loadTexts:
    grPhysWanStatsTable.setStatus("mandatory")
_GrPhysWanStatsEntry_Object = MibTableRow
grPhysWanStatsEntry = _GrPhysWanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1)
)
grPhysWanStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grPhysWanStatsEntry.setStatus("mandatory")
_GrPhysWanStRxCrcErrs_Type = Counter32
_GrPhysWanStRxCrcErrs_Object = MibTableColumn
grPhysWanStRxCrcErrs = _GrPhysWanStRxCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 1),
    _GrPhysWanStRxCrcErrs_Type()
)
grPhysWanStRxCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStRxCrcErrs.setStatus("mandatory")
_GrPhysWanStRxOverRunErrs_Type = Counter32
_GrPhysWanStRxOverRunErrs_Object = MibTableColumn
grPhysWanStRxOverRunErrs = _GrPhysWanStRxOverRunErrs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 2),
    _GrPhysWanStRxOverRunErrs_Type()
)
grPhysWanStRxOverRunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStRxOverRunErrs.setStatus("mandatory")
_GrPhysWanStTxUnderRunErrs_Type = Counter32
_GrPhysWanStTxUnderRunErrs_Object = MibTableColumn
grPhysWanStTxUnderRunErrs = _GrPhysWanStTxUnderRunErrs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 3),
    _GrPhysWanStTxUnderRunErrs_Type()
)
grPhysWanStTxUnderRunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStTxUnderRunErrs.setStatus("mandatory")
_GrPhysWanStRxAborts_Type = Counter32
_GrPhysWanStRxAborts_Object = MibTableColumn
grPhysWanStRxAborts = _GrPhysWanStRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 4),
    _GrPhysWanStRxAborts_Type()
)
grPhysWanStRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStRxAborts.setStatus("mandatory")
_GrPhysWanStTxAborts_Type = Counter32
_GrPhysWanStTxAborts_Object = MibTableColumn
grPhysWanStTxAborts = _GrPhysWanStTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 5),
    _GrPhysWanStTxAborts_Type()
)
grPhysWanStTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStTxAborts.setStatus("mandatory")
_GrPhysWanStRxOctetErrors_Type = Counter32
_GrPhysWanStRxOctetErrors_Object = MibTableColumn
grPhysWanStRxOctetErrors = _GrPhysWanStRxOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 6),
    _GrPhysWanStRxOctetErrors_Type()
)
grPhysWanStRxOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStRxOctetErrors.setStatus("mandatory")
_GrPhysWanStTxOctetErrors_Type = Counter32
_GrPhysWanStTxOctetErrors_Object = MibTableColumn
grPhysWanStTxOctetErrors = _GrPhysWanStTxOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 7),
    _GrPhysWanStTxOctetErrors_Type()
)
grPhysWanStTxOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStTxOctetErrors.setStatus("mandatory")
_GrPhysWanStLogicalIfIndex_Type = OctetString
_GrPhysWanStLogicalIfIndex_Object = MibTableColumn
grPhysWanStLogicalIfIndex = _GrPhysWanStLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 8),
    _GrPhysWanStLogicalIfIndex_Type()
)
grPhysWanStLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStLogicalIfIndex.setStatus("mandatory")
_GrPhysWanStInCalls_Type = Counter32
_GrPhysWanStInCalls_Object = MibTableColumn
grPhysWanStInCalls = _GrPhysWanStInCalls_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 9),
    _GrPhysWanStInCalls_Type()
)
grPhysWanStInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStInCalls.setStatus("mandatory")
_GrPhysWanStInFails_Type = Counter32
_GrPhysWanStInFails_Object = MibTableColumn
grPhysWanStInFails = _GrPhysWanStInFails_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 10),
    _GrPhysWanStInFails_Type()
)
grPhysWanStInFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStInFails.setStatus("mandatory")
_GrPhysWanStInSecurityFails_Type = Counter32
_GrPhysWanStInSecurityFails_Object = MibTableColumn
grPhysWanStInSecurityFails = _GrPhysWanStInSecurityFails_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 11),
    _GrPhysWanStInSecurityFails_Type()
)
grPhysWanStInSecurityFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStInSecurityFails.setStatus("mandatory")
_GrPhysWanStOutCalls_Type = Counter32
_GrPhysWanStOutCalls_Object = MibTableColumn
grPhysWanStOutCalls = _GrPhysWanStOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 12),
    _GrPhysWanStOutCalls_Type()
)
grPhysWanStOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStOutCalls.setStatus("mandatory")
_GrPhysWanStOutFails_Type = Counter32
_GrPhysWanStOutFails_Object = MibTableColumn
grPhysWanStOutFails = _GrPhysWanStOutFails_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 13),
    _GrPhysWanStOutFails_Type()
)
grPhysWanStOutFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStOutFails.setStatus("mandatory")
_GrPhysWanStOutSecurityFails_Type = Counter32
_GrPhysWanStOutSecurityFails_Object = MibTableColumn
grPhysWanStOutSecurityFails = _GrPhysWanStOutSecurityFails_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 2, 3, 1, 14),
    _GrPhysWanStOutSecurityFails_Type()
)
grPhysWanStOutSecurityFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPhysWanStOutSecurityFails.setStatus("mandatory")
_GrLogicalGroup_ObjectIdentity = ObjectIdentity
grLogicalGroup = _GrLogicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3)
)
_GrLogicalTable_Object = MibTable
grLogicalTable = _GrLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    grLogicalTable.setStatus("mandatory")
_GrLogicalEntry_Object = MibTableRow
grLogicalEntry = _GrLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 1, 1)
)
grLogicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grLogicalEntry.setStatus("mandatory")


class _GrLogicalDestName_Type(DisplayString):
    """Custom type grLogicalDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrLogicalDestName_Type.__name__ = "DisplayString"
_GrLogicalDestName_Object = MibTableColumn
grLogicalDestName = _GrLogicalDestName_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 1, 1, 1),
    _GrLogicalDestName_Type()
)
grLogicalDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogicalDestName.setStatus("mandatory")


class _GrLogicalTimeEnabled_Type(Integer32):
    """Custom type grLogicalTimeEnabled based on Integer32"""
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


_GrLogicalTimeEnabled_Type.__name__ = "Integer32"
_GrLogicalTimeEnabled_Object = MibTableColumn
grLogicalTimeEnabled = _GrLogicalTimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 1, 1, 2),
    _GrLogicalTimeEnabled_Type()
)
grLogicalTimeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogicalTimeEnabled.setStatus("mandatory")


class _GrLogicalTimeWindow_Type(OctetString):
    """Custom type grLogicalTimeWindow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(21, 21),
    )


_GrLogicalTimeWindow_Type.__name__ = "OctetString"
_GrLogicalTimeWindow_Object = MibTableColumn
grLogicalTimeWindow = _GrLogicalTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 1, 1, 3),
    _GrLogicalTimeWindow_Type()
)
grLogicalTimeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogicalTimeWindow.setStatus("mandatory")


class _GrLogicalType_Type(Integer32):
    """Custom type grLogicalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_GrLogicalType_Type.__name__ = "Integer32"
_GrLogicalType_Object = MibTableColumn
grLogicalType = _GrLogicalType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 1, 1, 4),
    _GrLogicalType_Type()
)
grLogicalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogicalType.setStatus("mandatory")
_GrLogicalStatus_Type = RowStatus
_GrLogicalStatus_Object = MibTableColumn
grLogicalStatus = _GrLogicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 1, 1, 5),
    _GrLogicalStatus_Type()
)
grLogicalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogicalStatus.setStatus("mandatory")
_GrLogWanTable_Object = MibTable
grLogWanTable = _GrLogWanTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    grLogWanTable.setStatus("mandatory")
_GrLogWanEntry_Object = MibTableRow
grLogWanEntry = _GrLogWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2, 1)
)
grLogWanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grLogWanEntry.setStatus("mandatory")


class _GrLogWanCmprsn_Type(Integer32):
    """Custom type grLogWanCmprsn based on Integer32"""
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


_GrLogWanCmprsn_Type.__name__ = "Integer32"
_GrLogWanCmprsn_Object = MibTableColumn
grLogWanCmprsn = _GrLogWanCmprsn_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2, 1, 1),
    _GrLogWanCmprsn_Type()
)
grLogWanCmprsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanCmprsn.setStatus("mandatory")


class _GrLogWanThshldOvrflw_Type(Integer32):
    """Custom type grLogWanThshldOvrflw based on Integer32"""
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


_GrLogWanThshldOvrflw_Type.__name__ = "Integer32"
_GrLogWanThshldOvrflw_Object = MibTableColumn
grLogWanThshldOvrflw = _GrLogWanThshldOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2, 1, 2),
    _GrLogWanThshldOvrflw_Type()
)
grLogWanThshldOvrflw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanThshldOvrflw.setStatus("mandatory")


class _GrLogWanThshld_Type(Integer32):
    """Custom type grLogWanThshld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GrLogWanThshld_Type.__name__ = "Integer32"
_GrLogWanThshld_Object = MibTableColumn
grLogWanThshld = _GrLogWanThshld_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2, 1, 3),
    _GrLogWanThshld_Type()
)
grLogWanThshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanThshld.setStatus("mandatory")


class _GrLogWanConnTimer_Type(Integer32):
    """Custom type grLogWanConnTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_GrLogWanConnTimer_Type.__name__ = "Integer32"
_GrLogWanConnTimer_Object = MibTableColumn
grLogWanConnTimer = _GrLogWanConnTimer_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2, 1, 4),
    _GrLogWanConnTimer_Type()
)
grLogWanConnTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanConnTimer.setStatus("mandatory")


class _GrLogWanDiscTimer_Type(Integer32):
    """Custom type grLogWanDiscTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_GrLogWanDiscTimer_Type.__name__ = "Integer32"
_GrLogWanDiscTimer_Object = MibTableColumn
grLogWanDiscTimer = _GrLogWanDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2, 1, 5),
    _GrLogWanDiscTimer_Type()
)
grLogWanDiscTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanDiscTimer.setStatus("mandatory")


class _GrLogWanSpoofing_Type(Integer32):
    """Custom type grLogWanSpoofing based on Integer32"""
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


_GrLogWanSpoofing_Type.__name__ = "Integer32"
_GrLogWanSpoofing_Object = MibTableColumn
grLogWanSpoofing = _GrLogWanSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2, 1, 6),
    _GrLogWanSpoofing_Type()
)
grLogWanSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanSpoofing.setStatus("mandatory")
_GrLogWanStatus_Type = RowStatus
_GrLogWanStatus_Object = MibTableColumn
grLogWanStatus = _GrLogWanStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 2, 1, 7),
    _GrLogWanStatus_Type()
)
grLogWanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanStatus.setStatus("mandatory")
_GrLogWanPortTable_Object = MibTable
grLogWanPortTable = _GrLogWanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3)
)
if mibBuilder.loadTexts:
    grLogWanPortTable.setStatus("mandatory")
_GrLogWanPortEntry_Object = MibTableRow
grLogWanPortEntry = _GrLogWanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1)
)
grLogWanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "GANDALF-ROUTER-MIB", "grLogWanPortIndex"),
)
if mibBuilder.loadTexts:
    grLogWanPortEntry.setStatus("mandatory")
_GrLogWanPortIndex_Type = Integer32
_GrLogWanPortIndex_Object = MibTableColumn
grLogWanPortIndex = _GrLogWanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 1),
    _GrLogWanPortIndex_Type()
)
grLogWanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanPortIndex.setStatus("mandatory")


class _GrLogWanPortWanType_Type(Integer32):
    """Custom type grLogWanPortWanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_GrLogWanPortWanType_Type.__name__ = "Integer32"
_GrLogWanPortWanType_Object = MibTableColumn
grLogWanPortWanType = _GrLogWanPortWanType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 2),
    _GrLogWanPortWanType_Type()
)
grLogWanPortWanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanPortWanType.setStatus("mandatory")
_GrLogWanPortPhysIfIndex_Type = Integer32
_GrLogWanPortPhysIfIndex_Object = MibTableColumn
grLogWanPortPhysIfIndex = _GrLogWanPortPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 3),
    _GrLogWanPortPhysIfIndex_Type()
)
grLogWanPortPhysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanPortPhysIfIndex.setStatus("mandatory")


class _GrLogWanPortPool_Type(DisplayString):
    """Custom type grLogWanPortPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrLogWanPortPool_Type.__name__ = "DisplayString"
_GrLogWanPortPool_Object = MibTableColumn
grLogWanPortPool = _GrLogWanPortPool_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 4),
    _GrLogWanPortPool_Type()
)
grLogWanPortPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanPortPool.setStatus("mandatory")


class _GrLogWanPortRetry_Type(Integer32):
    """Custom type grLogWanPortRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GrLogWanPortRetry_Type.__name__ = "Integer32"
_GrLogWanPortRetry_Object = MibTableColumn
grLogWanPortRetry = _GrLogWanPortRetry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 5),
    _GrLogWanPortRetry_Type()
)
grLogWanPortRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanPortRetry.setStatus("mandatory")


class _GrLogWanPortRetryPeriod_Type(Integer32):
    """Custom type grLogWanPortRetryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GrLogWanPortRetryPeriod_Type.__name__ = "Integer32"
_GrLogWanPortRetryPeriod_Object = MibTableColumn
grLogWanPortRetryPeriod = _GrLogWanPortRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 6),
    _GrLogWanPortRetryPeriod_Type()
)
grLogWanPortRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanPortRetryPeriod.setStatus("mandatory")


class _GrLogWanPortPrepend_Type(OctetString):
    """Custom type grLogWanPortPrepend based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_GrLogWanPortPrepend_Type.__name__ = "OctetString"
_GrLogWanPortPrepend_Object = MibTableColumn
grLogWanPortPrepend = _GrLogWanPortPrepend_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 7),
    _GrLogWanPortPrepend_Type()
)
grLogWanPortPrepend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanPortPrepend.setStatus("mandatory")


class _GrLogWanPortDestAddr_Type(DisplayString):
    """Custom type grLogWanPortDestAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GrLogWanPortDestAddr_Type.__name__ = "DisplayString"
_GrLogWanPortDestAddr_Object = MibTableColumn
grLogWanPortDestAddr = _GrLogWanPortDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 8),
    _GrLogWanPortDestAddr_Type()
)
grLogWanPortDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanPortDestAddr.setStatus("mandatory")


class _GrLogWanPortAdminStatus_Type(Integer32):
    """Custom type grLogWanPortAdminStatus based on Integer32"""
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


_GrLogWanPortAdminStatus_Type.__name__ = "Integer32"
_GrLogWanPortAdminStatus_Object = MibTableColumn
grLogWanPortAdminStatus = _GrLogWanPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 9),
    _GrLogWanPortAdminStatus_Type()
)
grLogWanPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanPortAdminStatus.setStatus("mandatory")


class _GrLogWanPortOperStatus_Type(Integer32):
    """Custom type grLogWanPortOperStatus based on Integer32"""
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
        *(("connected", 2),
          ("connecting", 1),
          ("disconnected", 4),
          ("disconnecting", 3),
          ("retryExhausted", 5))
    )


_GrLogWanPortOperStatus_Type.__name__ = "Integer32"
_GrLogWanPortOperStatus_Object = MibTableColumn
grLogWanPortOperStatus = _GrLogWanPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 10),
    _GrLogWanPortOperStatus_Type()
)
grLogWanPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanPortOperStatus.setStatus("mandatory")
_GrLogWanPortStatus_Type = RowStatus
_GrLogWanPortStatus_Object = MibTableColumn
grLogWanPortStatus = _GrLogWanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 3, 1, 11),
    _GrLogWanPortStatus_Type()
)
grLogWanPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grLogWanPortStatus.setStatus("mandatory")
_GrLogWanStatsTable_Object = MibTable
grLogWanStatsTable = _GrLogWanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4)
)
if mibBuilder.loadTexts:
    grLogWanStatsTable.setStatus("mandatory")
_GrLogWanStatsEntry_Object = MibTableRow
grLogWanStatsEntry = _GrLogWanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4, 1)
)
grLogWanStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grLogWanStatsEntry.setStatus("mandatory")
_GrLogWanStInUse_Type = OctetString
_GrLogWanStInUse_Object = MibTableColumn
grLogWanStInUse = _GrLogWanStInUse_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4, 1, 1),
    _GrLogWanStInUse_Type()
)
grLogWanStInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanStInUse.setStatus("mandatory")
_GrLogWanStUncmpsdRxOctets_Type = Counter32
_GrLogWanStUncmpsdRxOctets_Object = MibTableColumn
grLogWanStUncmpsdRxOctets = _GrLogWanStUncmpsdRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4, 1, 2),
    _GrLogWanStUncmpsdRxOctets_Type()
)
grLogWanStUncmpsdRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanStUncmpsdRxOctets.setStatus("mandatory")
_GrLogWanStCmpsdRxOctets_Type = Counter32
_GrLogWanStCmpsdRxOctets_Object = MibTableColumn
grLogWanStCmpsdRxOctets = _GrLogWanStCmpsdRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4, 1, 3),
    _GrLogWanStCmpsdRxOctets_Type()
)
grLogWanStCmpsdRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanStCmpsdRxOctets.setStatus("mandatory")
_GrLogWanStUncmpsdTxOctets_Type = Counter32
_GrLogWanStUncmpsdTxOctets_Object = MibTableColumn
grLogWanStUncmpsdTxOctets = _GrLogWanStUncmpsdTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4, 1, 4),
    _GrLogWanStUncmpsdTxOctets_Type()
)
grLogWanStUncmpsdTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanStUncmpsdTxOctets.setStatus("mandatory")
_GrLogWanStCmpsdTxOctets_Type = Counter32
_GrLogWanStCmpsdTxOctets_Object = MibTableColumn
grLogWanStCmpsdTxOctets = _GrLogWanStCmpsdTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4, 1, 5),
    _GrLogWanStCmpsdTxOctets_Type()
)
grLogWanStCmpsdTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanStCmpsdTxOctets.setStatus("mandatory")
_GrLogWanStConnects_Type = Counter32
_GrLogWanStConnects_Object = MibTableColumn
grLogWanStConnects = _GrLogWanStConnects_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4, 1, 6),
    _GrLogWanStConnects_Type()
)
grLogWanStConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanStConnects.setStatus("mandatory")
_GrLogWanStConnectFails_Type = Counter32
_GrLogWanStConnectFails_Object = MibTableColumn
grLogWanStConnectFails = _GrLogWanStConnectFails_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 4, 1, 7),
    _GrLogWanStConnectFails_Type()
)
grLogWanStConnectFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grLogWanStConnectFails.setStatus("mandatory")
_GrVirtualStatsTable_Object = MibTable
grVirtualStatsTable = _GrVirtualStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5)
)
if mibBuilder.loadTexts:
    grVirtualStatsTable.setStatus("mandatory")
_GrVirtualStatsEntry_Object = MibTableRow
grVirtualStatsEntry = _GrVirtualStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1)
)
grVirtualStatsEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grVSProtocolType"),
    (0, "GANDALF-ROUTER-MIB", "grVSNetAddr"),
)
if mibBuilder.loadTexts:
    grVirtualStatsEntry.setStatus("mandatory")


class _GrVSProtocolType_Type(Integer32):
    """Custom type grVSProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2))
    )


_GrVSProtocolType_Type.__name__ = "Integer32"
_GrVSProtocolType_Object = MibTableColumn
grVSProtocolType = _GrVSProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 1),
    _GrVSProtocolType_Type()
)
grVSProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSProtocolType.setStatus("mandatory")
_GrVSNetAddr_Type = OctetString
_GrVSNetAddr_Object = MibTableColumn
grVSNetAddr = _GrVSNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 2),
    _GrVSNetAddr_Type()
)
grVSNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSNetAddr.setStatus("mandatory")
_GrVSIfIndex_Type = Integer32
_GrVSIfIndex_Object = MibTableColumn
grVSIfIndex = _GrVSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 3),
    _GrVSIfIndex_Type()
)
grVSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSIfIndex.setStatus("mandatory")
_GrVSRxPkts_Type = Counter32
_GrVSRxPkts_Object = MibTableColumn
grVSRxPkts = _GrVSRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 4),
    _GrVSRxPkts_Type()
)
grVSRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSRxPkts.setStatus("mandatory")
_GrVSTxPkts_Type = Counter32
_GrVSTxPkts_Object = MibTableColumn
grVSTxPkts = _GrVSTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 5),
    _GrVSTxPkts_Type()
)
grVSTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSTxPkts.setStatus("mandatory")
_GrVSRxOctets_Type = Counter32
_GrVSRxOctets_Object = MibTableColumn
grVSRxOctets = _GrVSRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 6),
    _GrVSRxOctets_Type()
)
grVSRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSRxOctets.setStatus("mandatory")
_GrVSTxOctets_Type = Counter32
_GrVSTxOctets_Object = MibTableColumn
grVSTxOctets = _GrVSTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 7),
    _GrVSTxOctets_Type()
)
grVSTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSTxOctets.setStatus("mandatory")
_GrVSTTLDiscards_Type = Counter32
_GrVSTTLDiscards_Object = MibTableColumn
grVSTTLDiscards = _GrVSTTLDiscards_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 8),
    _GrVSTTLDiscards_Type()
)
grVSTTLDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSTTLDiscards.setStatus("mandatory")
_GrVSRxFilteredPkts_Type = Counter32
_GrVSRxFilteredPkts_Object = MibTableColumn
grVSRxFilteredPkts = _GrVSRxFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 9),
    _GrVSRxFilteredPkts_Type()
)
grVSRxFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSRxFilteredPkts.setStatus("mandatory")
_GrVSTxFilteredPkts_Type = Counter32
_GrVSTxFilteredPkts_Object = MibTableColumn
grVSTxFilteredPkts = _GrVSTxFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 3, 5, 1, 10),
    _GrVSTxFilteredPkts_Type()
)
grVSTxFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grVSTxFilteredPkts.setStatus("mandatory")
_GrBridgeGroup_ObjectIdentity = ObjectIdentity
grBridgeGroup = _GrBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4)
)


class _GrBridgingState_Type(Integer32):
    """Custom type grBridgingState based on Integer32"""
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


_GrBridgingState_Type.__name__ = "Integer32"
_GrBridgingState_Object = MibScalar
grBridgingState = _GrBridgingState_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 1),
    _GrBridgingState_Type()
)
grBridgingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grBridgingState.setStatus("mandatory")


class _GrBrMaxTransitDelay_Type(Integer32):
    """Custom type grBrMaxTransitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_GrBrMaxTransitDelay_Type.__name__ = "Integer32"
_GrBrMaxTransitDelay_Object = MibScalar
grBrMaxTransitDelay = _GrBrMaxTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 2),
    _GrBrMaxTransitDelay_Type()
)
grBrMaxTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grBrMaxTransitDelay.setStatus("mandatory")


class _GrBrFilterTestPackets_Type(Integer32):
    """Custom type grBrFilterTestPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2))
    )


_GrBrFilterTestPackets_Type.__name__ = "Integer32"
_GrBrFilterTestPackets_Object = MibScalar
grBrFilterTestPackets = _GrBrFilterTestPackets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 3),
    _GrBrFilterTestPackets_Type()
)
grBrFilterTestPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grBrFilterTestPackets.setStatus("mandatory")


class _GrProtFilterType_Type(Integer32):
    """Custom type grProtFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2))
    )


_GrProtFilterType_Type.__name__ = "Integer32"
_GrProtFilterType_Object = MibScalar
grProtFilterType = _GrProtFilterType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 4),
    _GrProtFilterType_Type()
)
grProtFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grProtFilterType.setStatus("mandatory")
_GrProtFilterTable_Object = MibTable
grProtFilterTable = _GrProtFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 5)
)
if mibBuilder.loadTexts:
    grProtFilterTable.setStatus("mandatory")
_GrProtFilterEntry_Object = MibTableRow
grProtFilterEntry = _GrProtFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 5, 1)
)
grProtFilterEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grProtFilterId"),
)
if mibBuilder.loadTexts:
    grProtFilterEntry.setStatus("mandatory")
_GrProtFilterId_Type = Integer32
_GrProtFilterId_Object = MibTableColumn
grProtFilterId = _GrProtFilterId_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 5, 1, 1),
    _GrProtFilterId_Type()
)
grProtFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grProtFilterId.setStatus("mandatory")
_GrProtFilterStatus_Type = RowStatus
_GrProtFilterStatus_Object = MibTableColumn
grProtFilterStatus = _GrProtFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 5, 1, 2),
    _GrProtFilterStatus_Type()
)
grProtFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grProtFilterStatus.setStatus("mandatory")
_GrProtPriorityTable_Object = MibTable
grProtPriorityTable = _GrProtPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 6)
)
if mibBuilder.loadTexts:
    grProtPriorityTable.setStatus("mandatory")
_GrProtPriorityEntry_Object = MibTableRow
grProtPriorityEntry = _GrProtPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 6, 1)
)
grProtPriorityEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grProtPriorityId"),
)
if mibBuilder.loadTexts:
    grProtPriorityEntry.setStatus("mandatory")
_GrProtPriorityId_Type = Integer32
_GrProtPriorityId_Object = MibTableColumn
grProtPriorityId = _GrProtPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 6, 1, 1),
    _GrProtPriorityId_Type()
)
grProtPriorityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grProtPriorityId.setStatus("mandatory")


class _GrProtPriorityLevel_Type(Integer32):
    """Custom type grProtPriorityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_GrProtPriorityLevel_Type.__name__ = "Integer32"
_GrProtPriorityLevel_Object = MibTableColumn
grProtPriorityLevel = _GrProtPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 6, 1, 2),
    _GrProtPriorityLevel_Type()
)
grProtPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grProtPriorityLevel.setStatus("mandatory")
_GrProtPriorityStatus_Type = RowStatus
_GrProtPriorityStatus_Object = MibTableColumn
grProtPriorityStatus = _GrProtPriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 6, 1, 3),
    _GrProtPriorityStatus_Type()
)
grProtPriorityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grProtPriorityStatus.setStatus("mandatory")
_GrBridgePortTable_Object = MibTable
grBridgePortTable = _GrBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 7)
)
if mibBuilder.loadTexts:
    grBridgePortTable.setStatus("mandatory")
_GrBridgePortEntry_Object = MibTableRow
grBridgePortEntry = _GrBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 7, 1)
)
grBridgePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grBridgePortEntry.setStatus("mandatory")


class _GrBrPortStpBpduFilter_Type(Integer32):
    """Custom type grBrPortStpBpduFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2))
    )


_GrBrPortStpBpduFilter_Type.__name__ = "Integer32"
_GrBrPortStpBpduFilter_Object = MibTableColumn
grBrPortStpBpduFilter = _GrBrPortStpBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 7, 1, 1),
    _GrBrPortStpBpduFilter_Type()
)
grBrPortStpBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grBrPortStpBpduFilter.setStatus("mandatory")
_GrBrPortAllowedToGoDef_Type = OctetString
_GrBrPortAllowedToGoDef_Object = MibTableColumn
grBrPortAllowedToGoDef = _GrBrPortAllowedToGoDef_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 7, 1, 2),
    _GrBrPortAllowedToGoDef_Type()
)
grBrPortAllowedToGoDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grBrPortAllowedToGoDef.setStatus("mandatory")
_GrBridgePortStatsTable_Object = MibTable
grBridgePortStatsTable = _GrBridgePortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 8)
)
if mibBuilder.loadTexts:
    grBridgePortStatsTable.setStatus("mandatory")
_GrBridgePortStatsEntry_Object = MibTableRow
grBridgePortStatsEntry = _GrBridgePortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 8, 1)
)
grBridgePortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grBridgePortStatsEntry.setStatus("mandatory")
_GrBrPortStRxOctets_Type = Counter32
_GrBrPortStRxOctets_Object = MibTableColumn
grBrPortStRxOctets = _GrBrPortStRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 8, 1, 1),
    _GrBrPortStRxOctets_Type()
)
grBrPortStRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grBrPortStRxOctets.setStatus("mandatory")
_GrBrPortStTxOctets_Type = Counter32
_GrBrPortStTxOctets_Object = MibTableColumn
grBrPortStTxOctets = _GrBrPortStTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 8, 1, 2),
    _GrBrPortStTxOctets_Type()
)
grBrPortStTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grBrPortStTxOctets.setStatus("mandatory")
_GrBrPortStRxFilteredPkts_Type = Counter32
_GrBrPortStRxFilteredPkts_Object = MibTableColumn
grBrPortStRxFilteredPkts = _GrBrPortStRxFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 8, 1, 3),
    _GrBrPortStRxFilteredPkts_Type()
)
grBrPortStRxFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grBrPortStRxFilteredPkts.setStatus("mandatory")
_GrBrPortStTxFilteredPkts_Type = Counter32
_GrBrPortStTxFilteredPkts_Object = MibTableColumn
grBrPortStTxFilteredPkts = _GrBrPortStTxFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 8, 1, 4),
    _GrBrPortStTxFilteredPkts_Type()
)
grBrPortStTxFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grBrPortStTxFilteredPkts.setStatus("mandatory")


class _GrSpanningTreeStatus_Type(Integer32):
    """Custom type grSpanningTreeStatus based on Integer32"""
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


_GrSpanningTreeStatus_Type.__name__ = "Integer32"
_GrSpanningTreeStatus_Object = MibScalar
grSpanningTreeStatus = _GrSpanningTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 4, 9),
    _GrSpanningTreeStatus_Type()
)
grSpanningTreeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grSpanningTreeStatus.setStatus("mandatory")
_GrIpxGroup_ObjectIdentity = ObjectIdentity
grIpxGroup = _GrIpxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5)
)


class _GrIpxRoutingEnable_Type(Integer32):
    """Custom type grIpxRoutingEnable based on Integer32"""
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


_GrIpxRoutingEnable_Type.__name__ = "Integer32"
_GrIpxRoutingEnable_Object = MibScalar
grIpxRoutingEnable = _GrIpxRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 1),
    _GrIpxRoutingEnable_Type()
)
grIpxRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxRoutingEnable.setStatus("mandatory")


class _GrIpxPrimaryNet_Type(OctetString):
    """Custom type grIpxPrimaryNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GrIpxPrimaryNet_Type.__name__ = "OctetString"
_GrIpxPrimaryNet_Object = MibScalar
grIpxPrimaryNet = _GrIpxPrimaryNet_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 2),
    _GrIpxPrimaryNet_Type()
)
grIpxPrimaryNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxPrimaryNet.setStatus("mandatory")


class _GrIpxRipEnable_Type(Integer32):
    """Custom type grIpxRipEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enabled", 1))
    )


_GrIpxRipEnable_Type.__name__ = "Integer32"
_GrIpxRipEnable_Object = MibScalar
grIpxRipEnable = _GrIpxRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 3),
    _GrIpxRipEnable_Type()
)
grIpxRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxRipEnable.setStatus("mandatory")


class _GrIpxSapEnable_Type(Integer32):
    """Custom type grIpxSapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enabled", 1))
    )


_GrIpxSapEnable_Type.__name__ = "Integer32"
_GrIpxSapEnable_Object = MibScalar
grIpxSapEnable = _GrIpxSapEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 4),
    _GrIpxSapEnable_Type()
)
grIpxSapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxSapEnable.setStatus("mandatory")


class _GrIpxAccessRestrictEnable_Type(Integer32):
    """Custom type grIpxAccessRestrictEnable based on Integer32"""
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


_GrIpxAccessRestrictEnable_Type.__name__ = "Integer32"
_GrIpxAccessRestrictEnable_Object = MibScalar
grIpxAccessRestrictEnable = _GrIpxAccessRestrictEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 5),
    _GrIpxAccessRestrictEnable_Type()
)
grIpxAccessRestrictEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccessRestrictEnable.setStatus("mandatory")
_GrIpxAccessRestrictTable_Object = MibTable
grIpxAccessRestrictTable = _GrIpxAccessRestrictTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6)
)
if mibBuilder.loadTexts:
    grIpxAccessRestrictTable.setStatus("mandatory")
_GrIpxAccessRestrictEntry_Object = MibTableRow
grIpxAccessRestrictEntry = _GrIpxAccessRestrictEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1)
)
grIpxAccessRestrictEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpxAccIndex"),
)
if mibBuilder.loadTexts:
    grIpxAccessRestrictEntry.setStatus("mandatory")
_GrIpxAccIndex_Type = Integer32
_GrIpxAccIndex_Object = MibTableColumn
grIpxAccIndex = _GrIpxAccIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 1),
    _GrIpxAccIndex_Type()
)
grIpxAccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxAccIndex.setStatus("mandatory")


class _GrIpxAccName_Type(DisplayString):
    """Custom type grIpxAccName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrIpxAccName_Type.__name__ = "DisplayString"
_GrIpxAccName_Object = MibTableColumn
grIpxAccName = _GrIpxAccName_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 2),
    _GrIpxAccName_Type()
)
grIpxAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccName.setStatus("mandatory")


class _GrIpxAccType_Type(Integer32):
    """Custom type grIpxAccType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2))
    )


_GrIpxAccType_Type.__name__ = "Integer32"
_GrIpxAccType_Object = MibTableColumn
grIpxAccType = _GrIpxAccType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 3),
    _GrIpxAccType_Type()
)
grIpxAccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccType.setStatus("mandatory")


class _GrIpxAccSrcNet_Type(OctetString):
    """Custom type grIpxAccSrcNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GrIpxAccSrcNet_Type.__name__ = "OctetString"
_GrIpxAccSrcNet_Object = MibTableColumn
grIpxAccSrcNet = _GrIpxAccSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 4),
    _GrIpxAccSrcNet_Type()
)
grIpxAccSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccSrcNet.setStatus("mandatory")


class _GrIpxAccSrcNode_Type(OctetString):
    """Custom type grIpxAccSrcNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GrIpxAccSrcNode_Type.__name__ = "OctetString"
_GrIpxAccSrcNode_Object = MibTableColumn
grIpxAccSrcNode = _GrIpxAccSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 5),
    _GrIpxAccSrcNode_Type()
)
grIpxAccSrcNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccSrcNode.setStatus("mandatory")


class _GrIpxAccSrcSocketFrom_Type(Integer32):
    """Custom type grIpxAccSrcSocketFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GrIpxAccSrcSocketFrom_Type.__name__ = "Integer32"
_GrIpxAccSrcSocketFrom_Object = MibTableColumn
grIpxAccSrcSocketFrom = _GrIpxAccSrcSocketFrom_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 6),
    _GrIpxAccSrcSocketFrom_Type()
)
grIpxAccSrcSocketFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccSrcSocketFrom.setStatus("mandatory")


class _GrIpxAccSrcSocketTo_Type(Integer32):
    """Custom type grIpxAccSrcSocketTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GrIpxAccSrcSocketTo_Type.__name__ = "Integer32"
_GrIpxAccSrcSocketTo_Object = MibTableColumn
grIpxAccSrcSocketTo = _GrIpxAccSrcSocketTo_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 7),
    _GrIpxAccSrcSocketTo_Type()
)
grIpxAccSrcSocketTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccSrcSocketTo.setStatus("mandatory")


class _GrIpxAccDstNet_Type(OctetString):
    """Custom type grIpxAccDstNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GrIpxAccDstNet_Type.__name__ = "OctetString"
_GrIpxAccDstNet_Object = MibTableColumn
grIpxAccDstNet = _GrIpxAccDstNet_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 8),
    _GrIpxAccDstNet_Type()
)
grIpxAccDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccDstNet.setStatus("mandatory")


class _GrIpxAccDstNode_Type(OctetString):
    """Custom type grIpxAccDstNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GrIpxAccDstNode_Type.__name__ = "OctetString"
_GrIpxAccDstNode_Object = MibTableColumn
grIpxAccDstNode = _GrIpxAccDstNode_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 9),
    _GrIpxAccDstNode_Type()
)
grIpxAccDstNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccDstNode.setStatus("mandatory")


class _GrIpxAccDstSocketFrom_Type(Integer32):
    """Custom type grIpxAccDstSocketFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GrIpxAccDstSocketFrom_Type.__name__ = "Integer32"
_GrIpxAccDstSocketFrom_Object = MibTableColumn
grIpxAccDstSocketFrom = _GrIpxAccDstSocketFrom_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 10),
    _GrIpxAccDstSocketFrom_Type()
)
grIpxAccDstSocketFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccDstSocketFrom.setStatus("mandatory")


class _GrIpxAccDstSocketTo_Type(Integer32):
    """Custom type grIpxAccDstSocketTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GrIpxAccDstSocketTo_Type.__name__ = "Integer32"
_GrIpxAccDstSocketTo_Object = MibTableColumn
grIpxAccDstSocketTo = _GrIpxAccDstSocketTo_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 11),
    _GrIpxAccDstSocketTo_Type()
)
grIpxAccDstSocketTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccDstSocketTo.setStatus("mandatory")
_GrIpxAccStatus_Type = RowStatus
_GrIpxAccStatus_Object = MibTableColumn
grIpxAccStatus = _GrIpxAccStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 6, 1, 12),
    _GrIpxAccStatus_Type()
)
grIpxAccStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxAccStatus.setStatus("mandatory")
_GrIpxRouteTable_Object = MibTable
grIpxRouteTable = _GrIpxRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7)
)
if mibBuilder.loadTexts:
    grIpxRouteTable.setStatus("mandatory")
_GrIpxRouteEntry_Object = MibTableRow
grIpxRouteEntry = _GrIpxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1)
)
grIpxRouteEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpxRouteDest"),
    (0, "GANDALF-ROUTER-MIB", "grIpxRouteType"),
    (0, "GANDALF-ROUTER-MIB", "grIpxRouteNextHopNet"),
    (0, "GANDALF-ROUTER-MIB", "grIpxRouteNextHopNode"),
)
if mibBuilder.loadTexts:
    grIpxRouteEntry.setStatus("mandatory")


class _GrIpxRouteDest_Type(OctetString):
    """Custom type grIpxRouteDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GrIpxRouteDest_Type.__name__ = "OctetString"
_GrIpxRouteDest_Object = MibTableColumn
grIpxRouteDest = _GrIpxRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 1),
    _GrIpxRouteDest_Type()
)
grIpxRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxRouteDest.setStatus("mandatory")


class _GrIpxRouteType_Type(Integer32):
    """Custom type grIpxRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learned", 1),
          ("local", 3),
          ("static", 2))
    )


_GrIpxRouteType_Type.__name__ = "Integer32"
_GrIpxRouteType_Object = MibTableColumn
grIpxRouteType = _GrIpxRouteType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 2),
    _GrIpxRouteType_Type()
)
grIpxRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxRouteType.setStatus("mandatory")
_GrIpxRouteHops_Type = Integer32
_GrIpxRouteHops_Object = MibTableColumn
grIpxRouteHops = _GrIpxRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 3),
    _GrIpxRouteHops_Type()
)
grIpxRouteHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxRouteHops.setStatus("mandatory")
_GrIpxRouteDelay_Type = Integer32
_GrIpxRouteDelay_Object = MibTableColumn
grIpxRouteDelay = _GrIpxRouteDelay_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 4),
    _GrIpxRouteDelay_Type()
)
grIpxRouteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxRouteDelay.setStatus("mandatory")
_GrIpxRouteAge_Type = TimeTicks
_GrIpxRouteAge_Object = MibTableColumn
grIpxRouteAge = _GrIpxRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 5),
    _GrIpxRouteAge_Type()
)
grIpxRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxRouteAge.setStatus("mandatory")


class _GrIpxRouteNextHopNet_Type(OctetString):
    """Custom type grIpxRouteNextHopNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GrIpxRouteNextHopNet_Type.__name__ = "OctetString"
_GrIpxRouteNextHopNet_Object = MibTableColumn
grIpxRouteNextHopNet = _GrIpxRouteNextHopNet_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 6),
    _GrIpxRouteNextHopNet_Type()
)
grIpxRouteNextHopNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxRouteNextHopNet.setStatus("mandatory")


class _GrIpxRouteNextHopNode_Type(OctetString):
    """Custom type grIpxRouteNextHopNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GrIpxRouteNextHopNode_Type.__name__ = "OctetString"
_GrIpxRouteNextHopNode_Object = MibTableColumn
grIpxRouteNextHopNode = _GrIpxRouteNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 7),
    _GrIpxRouteNextHopNode_Type()
)
grIpxRouteNextHopNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxRouteNextHopNode.setStatus("mandatory")
_GrIpxRouteIfIndex_Type = Integer32
_GrIpxRouteIfIndex_Object = MibTableColumn
grIpxRouteIfIndex = _GrIpxRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 8),
    _GrIpxRouteIfIndex_Type()
)
grIpxRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxRouteIfIndex.setStatus("mandatory")
_GrIpxRouteStatus_Type = RowStatus
_GrIpxRouteStatus_Object = MibTableColumn
grIpxRouteStatus = _GrIpxRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 7, 1, 9),
    _GrIpxRouteStatus_Type()
)
grIpxRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxRouteStatus.setStatus("mandatory")
_GrIpxServerTable_Object = MibTable
grIpxServerTable = _GrIpxServerTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8)
)
if mibBuilder.loadTexts:
    grIpxServerTable.setStatus("mandatory")
_GrIpxServerEntry_Object = MibTableRow
grIpxServerEntry = _GrIpxServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1)
)
grIpxServerEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpxServerType"),
    (0, "GANDALF-ROUTER-MIB", "grIpxServerSapType"),
    (0, "GANDALF-ROUTER-MIB", "grIpxServerName"),
)
if mibBuilder.loadTexts:
    grIpxServerEntry.setStatus("mandatory")
_GrIpxServerType_Type = Integer32
_GrIpxServerType_Object = MibTableColumn
grIpxServerType = _GrIpxServerType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1, 1),
    _GrIpxServerType_Type()
)
grIpxServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxServerType.setStatus("mandatory")


class _GrIpxServerSapType_Type(Integer32):
    """Custom type grIpxServerSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learned", 1),
          ("static", 2))
    )


_GrIpxServerSapType_Type.__name__ = "Integer32"
_GrIpxServerSapType_Object = MibTableColumn
grIpxServerSapType = _GrIpxServerSapType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1, 2),
    _GrIpxServerSapType_Type()
)
grIpxServerSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxServerSapType.setStatus("mandatory")


class _GrIpxServerName_Type(DisplayString):
    """Custom type grIpxServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_GrIpxServerName_Type.__name__ = "DisplayString"
_GrIpxServerName_Object = MibTableColumn
grIpxServerName = _GrIpxServerName_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1, 3),
    _GrIpxServerName_Type()
)
grIpxServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxServerName.setStatus("mandatory")
_GrIpxServerAge_Type = TimeTicks
_GrIpxServerAge_Object = MibTableColumn
grIpxServerAge = _GrIpxServerAge_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1, 4),
    _GrIpxServerAge_Type()
)
grIpxServerAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxServerAge.setStatus("mandatory")


class _GrIpxServerNet_Type(OctetString):
    """Custom type grIpxServerNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GrIpxServerNet_Type.__name__ = "OctetString"
_GrIpxServerNet_Object = MibTableColumn
grIpxServerNet = _GrIpxServerNet_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1, 5),
    _GrIpxServerNet_Type()
)
grIpxServerNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxServerNet.setStatus("mandatory")


class _GrIpxServerNode_Type(OctetString):
    """Custom type grIpxServerNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GrIpxServerNode_Type.__name__ = "OctetString"
_GrIpxServerNode_Object = MibTableColumn
grIpxServerNode = _GrIpxServerNode_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1, 6),
    _GrIpxServerNode_Type()
)
grIpxServerNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxServerNode.setStatus("mandatory")
_GrIpxServerSocket_Type = Integer32
_GrIpxServerSocket_Object = MibTableColumn
grIpxServerSocket = _GrIpxServerSocket_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1, 7),
    _GrIpxServerSocket_Type()
)
grIpxServerSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxServerSocket.setStatus("mandatory")
_GrIpxServerStatus_Type = RowStatus
_GrIpxServerStatus_Object = MibTableColumn
grIpxServerStatus = _GrIpxServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 8, 1, 8),
    _GrIpxServerStatus_Type()
)
grIpxServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxServerStatus.setStatus("mandatory")
_GrIpxInReceives_Type = Counter32
_GrIpxInReceives_Object = MibScalar
grIpxInReceives = _GrIpxInReceives_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 9),
    _GrIpxInReceives_Type()
)
grIpxInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxInReceives.setStatus("mandatory")
_GrIpxInHdrErrors_Type = Counter32
_GrIpxInHdrErrors_Object = MibScalar
grIpxInHdrErrors = _GrIpxInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 10),
    _GrIpxInHdrErrors_Type()
)
grIpxInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxInHdrErrors.setStatus("mandatory")
_GrIpxForwDatagrams_Type = Counter32
_GrIpxForwDatagrams_Object = MibScalar
grIpxForwDatagrams = _GrIpxForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 11),
    _GrIpxForwDatagrams_Type()
)
grIpxForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxForwDatagrams.setStatus("mandatory")
_GrIpxInUnknownSockets_Type = Counter32
_GrIpxInUnknownSockets_Object = MibScalar
grIpxInUnknownSockets = _GrIpxInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 12),
    _GrIpxInUnknownSockets_Type()
)
grIpxInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxInUnknownSockets.setStatus("mandatory")
_GrIpxInDiscards_Type = Counter32
_GrIpxInDiscards_Object = MibScalar
grIpxInDiscards = _GrIpxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 13),
    _GrIpxInDiscards_Type()
)
grIpxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxInDiscards.setStatus("mandatory")
_GrIpxInDelivers_Type = Counter32
_GrIpxInDelivers_Object = MibScalar
grIpxInDelivers = _GrIpxInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 14),
    _GrIpxInDelivers_Type()
)
grIpxInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxInDelivers.setStatus("mandatory")
_GrIpxOutRequests_Type = Counter32
_GrIpxOutRequests_Object = MibScalar
grIpxOutRequests = _GrIpxOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 15),
    _GrIpxOutRequests_Type()
)
grIpxOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxOutRequests.setStatus("mandatory")
_GrIpxOutDiscards_Type = Counter32
_GrIpxOutDiscards_Object = MibScalar
grIpxOutDiscards = _GrIpxOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 16),
    _GrIpxOutDiscards_Type()
)
grIpxOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxOutDiscards.setStatus("mandatory")
_GrIpxOutNoRoutes_Type = Counter32
_GrIpxOutNoRoutes_Object = MibScalar
grIpxOutNoRoutes = _GrIpxOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 17),
    _GrIpxOutNoRoutes_Type()
)
grIpxOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxOutNoRoutes.setStatus("mandatory")
_GrIpxLogicalTable_Object = MibTable
grIpxLogicalTable = _GrIpxLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 18)
)
if mibBuilder.loadTexts:
    grIpxLogicalTable.setStatus("mandatory")
_GrIpxLogicalEntry_Object = MibTableRow
grIpxLogicalEntry = _GrIpxLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 18, 1)
)
grIpxLogicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grIpxLogicalEntry.setStatus("mandatory")


class _GrIpxLAccessDef_Type(Integer32):
    """Custom type grIpxLAccessDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2))
    )


_GrIpxLAccessDef_Type.__name__ = "Integer32"
_GrIpxLAccessDef_Object = MibTableColumn
grIpxLAccessDef = _GrIpxLAccessDef_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 18, 1, 1),
    _GrIpxLAccessDef_Type()
)
grIpxLAccessDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxLAccessDef.setStatus("mandatory")
_GrIpxLRestrictions_Type = OctetString
_GrIpxLRestrictions_Object = MibTableColumn
grIpxLRestrictions = _GrIpxLRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 18, 1, 2),
    _GrIpxLRestrictions_Type()
)
grIpxLRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxLRestrictions.setStatus("mandatory")


class _GrIpxLTransport_Type(Integer32):
    """Custom type grIpxLTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bncp", 2),
          ("ipxcp", 1))
    )


_GrIpxLTransport_Type.__name__ = "Integer32"
_GrIpxLTransport_Object = MibTableColumn
grIpxLTransport = _GrIpxLTransport_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 18, 1, 3),
    _GrIpxLTransport_Type()
)
grIpxLTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxLTransport.setStatus("mandatory")
_GrIpxLStatus_Type = RowStatus
_GrIpxLStatus_Object = MibTableColumn
grIpxLStatus = _GrIpxLStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 18, 1, 4),
    _GrIpxLStatus_Type()
)
grIpxLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxLStatus.setStatus("mandatory")
_GrIpxVirtualTable_Object = MibTable
grIpxVirtualTable = _GrIpxVirtualTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19)
)
if mibBuilder.loadTexts:
    grIpxVirtualTable.setStatus("mandatory")
_GrIpxVirtualEntry_Object = MibTableRow
grIpxVirtualEntry = _GrIpxVirtualEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1)
)
grIpxVirtualEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpxVNetAddr"),
)
if mibBuilder.loadTexts:
    grIpxVirtualEntry.setStatus("mandatory")


class _GrIpxVNetAddr_Type(OctetString):
    """Custom type grIpxVNetAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GrIpxVNetAddr_Type.__name__ = "OctetString"
_GrIpxVNetAddr_Object = MibTableColumn
grIpxVNetAddr = _GrIpxVNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 1),
    _GrIpxVNetAddr_Type()
)
grIpxVNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVNetAddr.setStatus("mandatory")


class _GrIpxVNetEncap_Type(Integer32):
    """Custom type grIpxVNetEncap based on Integer32"""
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
        *(("ether2", 1),
          ("llc", 3),
          ("raw", 2),
          ("snap", 4))
    )


_GrIpxVNetEncap_Type.__name__ = "Integer32"
_GrIpxVNetEncap_Object = MibTableColumn
grIpxVNetEncap = _GrIpxVNetEncap_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 2),
    _GrIpxVNetEncap_Type()
)
grIpxVNetEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVNetEncap.setStatus("mandatory")


class _GrIpxVRipEnable_Type(Integer32):
    """Custom type grIpxVRipEnable based on Integer32"""
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


_GrIpxVRipEnable_Type.__name__ = "Integer32"
_GrIpxVRipEnable_Object = MibTableColumn
grIpxVRipEnable = _GrIpxVRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 3),
    _GrIpxVRipEnable_Type()
)
grIpxVRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVRipEnable.setStatus("mandatory")


class _GrIpxVRipMetric_Type(Integer32):
    """Custom type grIpxVRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GrIpxVRipMetric_Type.__name__ = "Integer32"
_GrIpxVRipMetric_Object = MibTableColumn
grIpxVRipMetric = _GrIpxVRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 4),
    _GrIpxVRipMetric_Type()
)
grIpxVRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVRipMetric.setStatus("mandatory")
_GrIpxVRipTxPeriod_Type = Integer32
_GrIpxVRipTxPeriod_Object = MibTableColumn
grIpxVRipTxPeriod = _GrIpxVRipTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 5),
    _GrIpxVRipTxPeriod_Type()
)
grIpxVRipTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVRipTxPeriod.setStatus("mandatory")
_GrIpxVRipAgeTimer_Type = Integer32
_GrIpxVRipAgeTimer_Object = MibTableColumn
grIpxVRipAgeTimer = _GrIpxVRipAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 6),
    _GrIpxVRipAgeTimer_Type()
)
grIpxVRipAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVRipAgeTimer.setStatus("mandatory")


class _GrIpxVSapEnable_Type(Integer32):
    """Custom type grIpxVSapEnable based on Integer32"""
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


_GrIpxVSapEnable_Type.__name__ = "Integer32"
_GrIpxVSapEnable_Object = MibTableColumn
grIpxVSapEnable = _GrIpxVSapEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 7),
    _GrIpxVSapEnable_Type()
)
grIpxVSapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVSapEnable.setStatus("mandatory")
_GrIpxVSapTxPeriod_Type = Integer32
_GrIpxVSapTxPeriod_Object = MibTableColumn
grIpxVSapTxPeriod = _GrIpxVSapTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 8),
    _GrIpxVSapTxPeriod_Type()
)
grIpxVSapTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVSapTxPeriod.setStatus("mandatory")
_GrIpxVSapAgeTimer_Type = Integer32
_GrIpxVSapAgeTimer_Object = MibTableColumn
grIpxVSapAgeTimer = _GrIpxVSapAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 9),
    _GrIpxVSapAgeTimer_Type()
)
grIpxVSapAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVSapAgeTimer.setStatus("mandatory")


class _GrIpxVWdogSpoof_Type(Integer32):
    """Custom type grIpxVWdogSpoof based on Integer32"""
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


_GrIpxVWdogSpoof_Type.__name__ = "Integer32"
_GrIpxVWdogSpoof_Object = MibTableColumn
grIpxVWdogSpoof = _GrIpxVWdogSpoof_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 10),
    _GrIpxVWdogSpoof_Type()
)
grIpxVWdogSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVWdogSpoof.setStatus("mandatory")
_GrIpxVIfIndex_Type = Integer32
_GrIpxVIfIndex_Object = MibTableColumn
grIpxVIfIndex = _GrIpxVIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 11),
    _GrIpxVIfIndex_Type()
)
grIpxVIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVIfIndex.setStatus("mandatory")
_GrIpxVStatus_Type = RowStatus
_GrIpxVStatus_Object = MibTableColumn
grIpxVStatus = _GrIpxVStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 19, 1, 12),
    _GrIpxVStatus_Type()
)
grIpxVStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpxVStatus.setStatus("mandatory")
_GrIpxVRipTable_Object = MibTable
grIpxVRipTable = _GrIpxVRipTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20)
)
if mibBuilder.loadTexts:
    grIpxVRipTable.setStatus("mandatory")
_GrIpxVRipEntry_Object = MibTableRow
grIpxVRipEntry = _GrIpxVRipEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1)
)
grIpxVRipEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpxVNetAddr"),
)
if mibBuilder.loadTexts:
    grIpxVRipEntry.setStatus("mandatory")
_GrIpxVRipRtePkts_Type = Counter32
_GrIpxVRipRtePkts_Object = MibTableColumn
grIpxVRipRtePkts = _GrIpxVRipRtePkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 1),
    _GrIpxVRipRtePkts_Type()
)
grIpxVRipRtePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRtePkts.setStatus("mandatory")
_GrIpxVRipHopCntExcs_Type = Counter32
_GrIpxVRipHopCntExcs_Object = MibTableColumn
grIpxVRipHopCntExcs = _GrIpxVRipHopCntExcs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 2),
    _GrIpxVRipHopCntExcs_Type()
)
grIpxVRipHopCntExcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipHopCntExcs.setStatus("mandatory")
_GrIpxVRipNetbHopCntExcs_Type = Counter32
_GrIpxVRipNetbHopCntExcs_Object = MibTableColumn
grIpxVRipNetbHopCntExcs = _GrIpxVRipNetbHopCntExcs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 3),
    _GrIpxVRipNetbHopCntExcs_Type()
)
grIpxVRipNetbHopCntExcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipNetbHopCntExcs.setStatus("mandatory")
_GrIpxVRipNoNetAddRcvs_Type = Counter32
_GrIpxVRipNoNetAddRcvs_Object = MibTableColumn
grIpxVRipNoNetAddRcvs = _GrIpxVRipNoNetAddRcvs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 4),
    _GrIpxVRipNoNetAddRcvs_Type()
)
grIpxVRipNoNetAddRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipNoNetAddRcvs.setStatus("mandatory")
_GrIpxVRipRxGenQs_Type = Counter32
_GrIpxVRipRxGenQs_Object = MibTableColumn
grIpxVRipRxGenQs = _GrIpxVRipRxGenQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 5),
    _GrIpxVRipRxGenQs_Type()
)
grIpxVRipRxGenQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRxGenQs.setStatus("mandatory")
_GrIpxVRipRxNearQs_Type = Counter32
_GrIpxVRipRxNearQs_Object = MibTableColumn
grIpxVRipRxNearQs = _GrIpxVRipRxNearQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 6),
    _GrIpxVRipRxNearQs_Type()
)
grIpxVRipRxNearQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRxNearQs.setStatus("mandatory")
_GrIpxVRipRxGenRs_Type = Counter32
_GrIpxVRipRxGenRs_Object = MibTableColumn
grIpxVRipRxGenRs = _GrIpxVRipRxGenRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 7),
    _GrIpxVRipRxGenRs_Type()
)
grIpxVRipRxGenRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRxGenRs.setStatus("mandatory")
_GrIpxVRipRxNearRs_Type = Counter32
_GrIpxVRipRxNearRs_Object = MibTableColumn
grIpxVRipRxNearRs = _GrIpxVRipRxNearRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 8),
    _GrIpxVRipRxNearRs_Type()
)
grIpxVRipRxNearRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRxNearRs.setStatus("mandatory")
_GrIpxVRipTxGenQs_Type = Counter32
_GrIpxVRipTxGenQs_Object = MibTableColumn
grIpxVRipTxGenQs = _GrIpxVRipTxGenQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 9),
    _GrIpxVRipTxGenQs_Type()
)
grIpxVRipTxGenQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipTxGenQs.setStatus("mandatory")
_GrIpxVRipTxNearQs_Type = Counter32
_GrIpxVRipTxNearQs_Object = MibTableColumn
grIpxVRipTxNearQs = _GrIpxVRipTxNearQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 10),
    _GrIpxVRipTxNearQs_Type()
)
grIpxVRipTxNearQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipTxNearQs.setStatus("mandatory")
_GrIpxVRipTxGenRs_Type = Counter32
_GrIpxVRipTxGenRs_Object = MibTableColumn
grIpxVRipTxGenRs = _GrIpxVRipTxGenRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 11),
    _GrIpxVRipTxGenRs_Type()
)
grIpxVRipTxGenRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipTxGenRs.setStatus("mandatory")
_GrIpxVRipTxNearRs_Type = Counter32
_GrIpxVRipTxNearRs_Object = MibTableColumn
grIpxVRipTxNearRs = _GrIpxVRipTxNearRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 12),
    _GrIpxVRipTxNearRs_Type()
)
grIpxVRipTxNearRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipTxNearRs.setStatus("mandatory")
_GrIpxVRipRxUnknGenQs_Type = Counter32
_GrIpxVRipRxUnknGenQs_Object = MibTableColumn
grIpxVRipRxUnknGenQs = _GrIpxVRipRxUnknGenQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 13),
    _GrIpxVRipRxUnknGenQs_Type()
)
grIpxVRipRxUnknGenQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRxUnknGenQs.setStatus("mandatory")
_GrIpxVRipRxUnknNearQs_Type = Counter32
_GrIpxVRipRxUnknNearQs_Object = MibTableColumn
grIpxVRipRxUnknNearQs = _GrIpxVRipRxUnknNearQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 14),
    _GrIpxVRipRxUnknNearQs_Type()
)
grIpxVRipRxUnknNearQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRxUnknNearQs.setStatus("mandatory")
_GrIpxVRipRxUnknGenRs_Type = Counter32
_GrIpxVRipRxUnknGenRs_Object = MibTableColumn
grIpxVRipRxUnknGenRs = _GrIpxVRipRxUnknGenRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 15),
    _GrIpxVRipRxUnknGenRs_Type()
)
grIpxVRipRxUnknGenRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRxUnknGenRs.setStatus("mandatory")
_GrIpxVRipRxUnknNearRs_Type = Counter32
_GrIpxVRipRxUnknNearRs_Object = MibTableColumn
grIpxVRipRxUnknNearRs = _GrIpxVRipRxUnknNearRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 16),
    _GrIpxVRipRxUnknNearRs_Type()
)
grIpxVRipRxUnknNearRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipRxUnknNearRs.setStatus("mandatory")
_GrIpxVRipAgedOuts_Type = Counter32
_GrIpxVRipAgedOuts_Object = MibTableColumn
grIpxVRipAgedOuts = _GrIpxVRipAgedOuts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 17),
    _GrIpxVRipAgedOuts_Type()
)
grIpxVRipAgedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipAgedOuts.setStatus("mandatory")
_GrIpxVRipPeriodics_Type = Counter32
_GrIpxVRipPeriodics_Object = MibTableColumn
grIpxVRipPeriodics = _GrIpxVRipPeriodics_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 18),
    _GrIpxVRipPeriodics_Type()
)
grIpxVRipPeriodics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipPeriodics.setStatus("mandatory")
_GrIpxVRipUpdates_Type = Counter32
_GrIpxVRipUpdates_Object = MibTableColumn
grIpxVRipUpdates = _GrIpxVRipUpdates_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 19),
    _GrIpxVRipUpdates_Type()
)
grIpxVRipUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipUpdates.setStatus("mandatory")
_GrIpxVRipWrongNets_Type = Counter32
_GrIpxVRipWrongNets_Object = MibTableColumn
grIpxVRipWrongNets = _GrIpxVRipWrongNets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 20),
    _GrIpxVRipWrongNets_Type()
)
grIpxVRipWrongNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipWrongNets.setStatus("mandatory")
_GrIpxVRipBadInfos_Type = Counter32
_GrIpxVRipBadInfos_Object = MibTableColumn
grIpxVRipBadInfos = _GrIpxVRipBadInfos_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 20, 1, 21),
    _GrIpxVRipBadInfos_Type()
)
grIpxVRipBadInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVRipBadInfos.setStatus("mandatory")
_GrIpxVSapTable_Object = MibTable
grIpxVSapTable = _GrIpxVSapTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21)
)
if mibBuilder.loadTexts:
    grIpxVSapTable.setStatus("mandatory")
_GrIpxVSapEntry_Object = MibTableRow
grIpxVSapEntry = _GrIpxVSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1)
)
grIpxVSapEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpxVNetAddr"),
)
if mibBuilder.loadTexts:
    grIpxVSapEntry.setStatus("mandatory")
_GrIpxVSapRxGenQs_Type = Counter32
_GrIpxVSapRxGenQs_Object = MibTableColumn
grIpxVSapRxGenQs = _GrIpxVSapRxGenQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 1),
    _GrIpxVSapRxGenQs_Type()
)
grIpxVSapRxGenQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapRxGenQs.setStatus("mandatory")
_GrIpxVSapRxNearQs_Type = Counter32
_GrIpxVSapRxNearQs_Object = MibTableColumn
grIpxVSapRxNearQs = _GrIpxVSapRxNearQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 2),
    _GrIpxVSapRxNearQs_Type()
)
grIpxVSapRxNearQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapRxNearQs.setStatus("mandatory")
_GrIpxVSapRxGenRs_Type = Counter32
_GrIpxVSapRxGenRs_Object = MibTableColumn
grIpxVSapRxGenRs = _GrIpxVSapRxGenRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 3),
    _GrIpxVSapRxGenRs_Type()
)
grIpxVSapRxGenRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapRxGenRs.setStatus("mandatory")
_GrIpxVSapRxNearRs_Type = Counter32
_GrIpxVSapRxNearRs_Object = MibTableColumn
grIpxVSapRxNearRs = _GrIpxVSapRxNearRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 4),
    _GrIpxVSapRxNearRs_Type()
)
grIpxVSapRxNearRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapRxNearRs.setStatus("mandatory")
_GrIpxVSapTxGenQs_Type = Counter32
_GrIpxVSapTxGenQs_Object = MibTableColumn
grIpxVSapTxGenQs = _GrIpxVSapTxGenQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 5),
    _GrIpxVSapTxGenQs_Type()
)
grIpxVSapTxGenQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapTxGenQs.setStatus("mandatory")
_GrIpxVSapTxNearQs_Type = Counter32
_GrIpxVSapTxNearQs_Object = MibTableColumn
grIpxVSapTxNearQs = _GrIpxVSapTxNearQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 6),
    _GrIpxVSapTxNearQs_Type()
)
grIpxVSapTxNearQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapTxNearQs.setStatus("mandatory")
_GrIpxVSapTxGenRs_Type = Counter32
_GrIpxVSapTxGenRs_Object = MibTableColumn
grIpxVSapTxGenRs = _GrIpxVSapTxGenRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 7),
    _GrIpxVSapTxGenRs_Type()
)
grIpxVSapTxGenRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapTxGenRs.setStatus("mandatory")
_GrIpxVSapTxNearRs_Type = Counter32
_GrIpxVSapTxNearRs_Object = MibTableColumn
grIpxVSapTxNearRs = _GrIpxVSapTxNearRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 8),
    _GrIpxVSapTxNearRs_Type()
)
grIpxVSapTxNearRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapTxNearRs.setStatus("mandatory")
_GrIpxVSapRxUnknGenQs_Type = Counter32
_GrIpxVSapRxUnknGenQs_Object = MibTableColumn
grIpxVSapRxUnknGenQs = _GrIpxVSapRxUnknGenQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 9),
    _GrIpxVSapRxUnknGenQs_Type()
)
grIpxVSapRxUnknGenQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapRxUnknGenQs.setStatus("mandatory")
_GrIpxVSapRxUnknNearQs_Type = Counter32
_GrIpxVSapRxUnknNearQs_Object = MibTableColumn
grIpxVSapRxUnknNearQs = _GrIpxVSapRxUnknNearQs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 10),
    _GrIpxVSapRxUnknNearQs_Type()
)
grIpxVSapRxUnknNearQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapRxUnknNearQs.setStatus("mandatory")
_GrIpxVSapRxUnknGenRs_Type = Counter32
_GrIpxVSapRxUnknGenRs_Object = MibTableColumn
grIpxVSapRxUnknGenRs = _GrIpxVSapRxUnknGenRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 11),
    _GrIpxVSapRxUnknGenRs_Type()
)
grIpxVSapRxUnknGenRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapRxUnknGenRs.setStatus("mandatory")
_GrIpxVSapRxUnknNearRs_Type = Counter32
_GrIpxVSapRxUnknNearRs_Object = MibTableColumn
grIpxVSapRxUnknNearRs = _GrIpxVSapRxUnknNearRs_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 12),
    _GrIpxVSapRxUnknNearRs_Type()
)
grIpxVSapRxUnknNearRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapRxUnknNearRs.setStatus("mandatory")
_GrIpxVSapAgedOuts_Type = Counter32
_GrIpxVSapAgedOuts_Object = MibTableColumn
grIpxVSapAgedOuts = _GrIpxVSapAgedOuts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 13),
    _GrIpxVSapAgedOuts_Type()
)
grIpxVSapAgedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapAgedOuts.setStatus("mandatory")
_GrIpxVSapPeriodics_Type = Counter32
_GrIpxVSapPeriodics_Object = MibTableColumn
grIpxVSapPeriodics = _GrIpxVSapPeriodics_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 14),
    _GrIpxVSapPeriodics_Type()
)
grIpxVSapPeriodics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapPeriodics.setStatus("mandatory")
_GrIpxVSapUpdates_Type = Counter32
_GrIpxVSapUpdates_Object = MibTableColumn
grIpxVSapUpdates = _GrIpxVSapUpdates_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 15),
    _GrIpxVSapUpdates_Type()
)
grIpxVSapUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapUpdates.setStatus("mandatory")
_GrIpxVSapWrongNets_Type = Counter32
_GrIpxVSapWrongNets_Object = MibTableColumn
grIpxVSapWrongNets = _GrIpxVSapWrongNets_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 16),
    _GrIpxVSapWrongNets_Type()
)
grIpxVSapWrongNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapWrongNets.setStatus("mandatory")
_GrIpxVSapBadInfos_Type = Counter32
_GrIpxVSapBadInfos_Object = MibTableColumn
grIpxVSapBadInfos = _GrIpxVSapBadInfos_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 5, 21, 1, 17),
    _GrIpxVSapBadInfos_Type()
)
grIpxVSapBadInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpxVSapBadInfos.setStatus("mandatory")
_GrIpGroup_ObjectIdentity = ObjectIdentity
grIpGroup = _GrIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6)
)


class _GrIpRipEnable_Type(Integer32):
    """Custom type grIpRipEnable based on Integer32"""
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


_GrIpRipEnable_Type.__name__ = "Integer32"
_GrIpRipEnable_Object = MibScalar
grIpRipEnable = _GrIpRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 1),
    _GrIpRipEnable_Type()
)
grIpRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpRipEnable.setStatus("mandatory")


class _GrIpArpCacheAge_Type(Integer32):
    """Custom type grIpArpCacheAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_GrIpArpCacheAge_Type.__name__ = "Integer32"
_GrIpArpCacheAge_Object = MibScalar
grIpArpCacheAge = _GrIpArpCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 2),
    _GrIpArpCacheAge_Type()
)
grIpArpCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpArpCacheAge.setStatus("mandatory")


class _GrIpProxyArp_Type(Integer32):
    """Custom type grIpProxyArp based on Integer32"""
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


_GrIpProxyArp_Type.__name__ = "Integer32"
_GrIpProxyArp_Object = MibScalar
grIpProxyArp = _GrIpProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 3),
    _GrIpProxyArp_Type()
)
grIpProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpProxyArp.setStatus("mandatory")


class _GrIpTrustedGatewayEnable_Type(Integer32):
    """Custom type grIpTrustedGatewayEnable based on Integer32"""
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


_GrIpTrustedGatewayEnable_Type.__name__ = "Integer32"
_GrIpTrustedGatewayEnable_Object = MibScalar
grIpTrustedGatewayEnable = _GrIpTrustedGatewayEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 4),
    _GrIpTrustedGatewayEnable_Type()
)
grIpTrustedGatewayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpTrustedGatewayEnable.setStatus("mandatory")
_GrIpTrustedGatewayTable_Object = MibTable
grIpTrustedGatewayTable = _GrIpTrustedGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 5)
)
if mibBuilder.loadTexts:
    grIpTrustedGatewayTable.setStatus("mandatory")
_GrIpTrustedGatewayEntry_Object = MibTableRow
grIpTrustedGatewayEntry = _GrIpTrustedGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 5, 1)
)
grIpTrustedGatewayEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpGatewayAddr"),
)
if mibBuilder.loadTexts:
    grIpTrustedGatewayEntry.setStatus("mandatory")
_GrIpGatewayAddr_Type = IpAddress
_GrIpGatewayAddr_Object = MibTableColumn
grIpGatewayAddr = _GrIpGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 5, 1, 1),
    _GrIpGatewayAddr_Type()
)
grIpGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpGatewayAddr.setStatus("mandatory")


class _GrIpGatewayName_Type(DisplayString):
    """Custom type grIpGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrIpGatewayName_Type.__name__ = "DisplayString"
_GrIpGatewayName_Object = MibTableColumn
grIpGatewayName = _GrIpGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 5, 1, 2),
    _GrIpGatewayName_Type()
)
grIpGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpGatewayName.setStatus("mandatory")
_GrIpGatewayStatus_Type = RowStatus
_GrIpGatewayStatus_Object = MibTableColumn
grIpGatewayStatus = _GrIpGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 5, 1, 3),
    _GrIpGatewayStatus_Type()
)
grIpGatewayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpGatewayStatus.setStatus("mandatory")


class _GrIpAccessRestrictEnable_Type(Integer32):
    """Custom type grIpAccessRestrictEnable based on Integer32"""
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


_GrIpAccessRestrictEnable_Type.__name__ = "Integer32"
_GrIpAccessRestrictEnable_Object = MibScalar
grIpAccessRestrictEnable = _GrIpAccessRestrictEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 6),
    _GrIpAccessRestrictEnable_Type()
)
grIpAccessRestrictEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccessRestrictEnable.setStatus("mandatory")
_GrIpAccessRestrictTable_Object = MibTable
grIpAccessRestrictTable = _GrIpAccessRestrictTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7)
)
if mibBuilder.loadTexts:
    grIpAccessRestrictTable.setStatus("mandatory")
_GrIpAccessRestrictEntry_Object = MibTableRow
grIpAccessRestrictEntry = _GrIpAccessRestrictEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1)
)
grIpAccessRestrictEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpAccIndex"),
)
if mibBuilder.loadTexts:
    grIpAccessRestrictEntry.setStatus("mandatory")
_GrIpAccIndex_Type = Integer32
_GrIpAccIndex_Object = MibTableColumn
grIpAccIndex = _GrIpAccIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 1),
    _GrIpAccIndex_Type()
)
grIpAccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpAccIndex.setStatus("mandatory")


class _GrIpAccName_Type(DisplayString):
    """Custom type grIpAccName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrIpAccName_Type.__name__ = "DisplayString"
_GrIpAccName_Object = MibTableColumn
grIpAccName = _GrIpAccName_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 2),
    _GrIpAccName_Type()
)
grIpAccName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccName.setStatus("mandatory")


class _GrIpAccType_Type(Integer32):
    """Custom type grIpAccType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2))
    )


_GrIpAccType_Type.__name__ = "Integer32"
_GrIpAccType_Object = MibTableColumn
grIpAccType = _GrIpAccType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 3),
    _GrIpAccType_Type()
)
grIpAccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccType.setStatus("mandatory")
_GrIpAccSrcNet_Type = IpAddress
_GrIpAccSrcNet_Object = MibTableColumn
grIpAccSrcNet = _GrIpAccSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 4),
    _GrIpAccSrcNet_Type()
)
grIpAccSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccSrcNet.setStatus("mandatory")
_GrIpAccSrcMask_Type = IpAddress
_GrIpAccSrcMask_Object = MibTableColumn
grIpAccSrcMask = _GrIpAccSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 5),
    _GrIpAccSrcMask_Type()
)
grIpAccSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccSrcMask.setStatus("mandatory")
_GrIpAccDstNet_Type = IpAddress
_GrIpAccDstNet_Object = MibTableColumn
grIpAccDstNet = _GrIpAccDstNet_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 6),
    _GrIpAccDstNet_Type()
)
grIpAccDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccDstNet.setStatus("mandatory")
_GrIpAccDstMask_Type = IpAddress
_GrIpAccDstMask_Object = MibTableColumn
grIpAccDstMask = _GrIpAccDstMask_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 7),
    _GrIpAccDstMask_Type()
)
grIpAccDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccDstMask.setStatus("mandatory")


class _GrIpAccProtocolFrom_Type(Integer32):
    """Custom type grIpAccProtocolFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GrIpAccProtocolFrom_Type.__name__ = "Integer32"
_GrIpAccProtocolFrom_Object = MibTableColumn
grIpAccProtocolFrom = _GrIpAccProtocolFrom_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 8),
    _GrIpAccProtocolFrom_Type()
)
grIpAccProtocolFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccProtocolFrom.setStatus("mandatory")


class _GrIpAccProtocolTo_Type(Integer32):
    """Custom type grIpAccProtocolTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GrIpAccProtocolTo_Type.__name__ = "Integer32"
_GrIpAccProtocolTo_Object = MibTableColumn
grIpAccProtocolTo = _GrIpAccProtocolTo_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 9),
    _GrIpAccProtocolTo_Type()
)
grIpAccProtocolTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccProtocolTo.setStatus("mandatory")


class _GrIpAccPortFrom_Type(Integer32):
    """Custom type grIpAccPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GrIpAccPortFrom_Type.__name__ = "Integer32"
_GrIpAccPortFrom_Object = MibTableColumn
grIpAccPortFrom = _GrIpAccPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 10),
    _GrIpAccPortFrom_Type()
)
grIpAccPortFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccPortFrom.setStatus("mandatory")


class _GrIpAccPortTo_Type(Integer32):
    """Custom type grIpAccPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GrIpAccPortTo_Type.__name__ = "Integer32"
_GrIpAccPortTo_Object = MibTableColumn
grIpAccPortTo = _GrIpAccPortTo_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 11),
    _GrIpAccPortTo_Type()
)
grIpAccPortTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccPortTo.setStatus("mandatory")
_GrIpAccStatus_Type = RowStatus
_GrIpAccStatus_Object = MibTableColumn
grIpAccStatus = _GrIpAccStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 7, 1, 12),
    _GrIpAccStatus_Type()
)
grIpAccStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpAccStatus.setStatus("mandatory")
_GrIpLogicalTable_Object = MibTable
grIpLogicalTable = _GrIpLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 8)
)
if mibBuilder.loadTexts:
    grIpLogicalTable.setStatus("mandatory")
_GrIpLogicalEntry_Object = MibTableRow
grIpLogicalEntry = _GrIpLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 8, 1)
)
grIpLogicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grIpLogicalEntry.setStatus("mandatory")


class _GrIpLAccessDef_Type(Integer32):
    """Custom type grIpLAccessDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2))
    )


_GrIpLAccessDef_Type.__name__ = "Integer32"
_GrIpLAccessDef_Object = MibTableColumn
grIpLAccessDef = _GrIpLAccessDef_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 8, 1, 1),
    _GrIpLAccessDef_Type()
)
grIpLAccessDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpLAccessDef.setStatus("mandatory")
_GrIpLRestrictions_Type = OctetString
_GrIpLRestrictions_Object = MibTableColumn
grIpLRestrictions = _GrIpLRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 8, 1, 2),
    _GrIpLRestrictions_Type()
)
grIpLRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpLRestrictions.setStatus("mandatory")


class _GrIpLTransport_Type(Integer32):
    """Custom type grIpLTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bncp", 2),
          ("ipcp", 1))
    )


_GrIpLTransport_Type.__name__ = "Integer32"
_GrIpLTransport_Object = MibTableColumn
grIpLTransport = _GrIpLTransport_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 8, 1, 3),
    _GrIpLTransport_Type()
)
grIpLTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpLTransport.setStatus("mandatory")
_GrIpLStatus_Type = RowStatus
_GrIpLStatus_Object = MibTableColumn
grIpLStatus = _GrIpLStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 8, 1, 4),
    _GrIpLStatus_Type()
)
grIpLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpLStatus.setStatus("mandatory")
_GrIpVirtualTable_Object = MibTable
grIpVirtualTable = _GrIpVirtualTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9)
)
if mibBuilder.loadTexts:
    grIpVirtualTable.setStatus("mandatory")
_GrIpVirtualEntry_Object = MibTableRow
grIpVirtualEntry = _GrIpVirtualEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1)
)
grIpVirtualEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpVNetAddr"),
)
if mibBuilder.loadTexts:
    grIpVirtualEntry.setStatus("mandatory")
_GrIpVNetAddr_Type = IpAddress
_GrIpVNetAddr_Object = MibTableColumn
grIpVNetAddr = _GrIpVNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 1),
    _GrIpVNetAddr_Type()
)
grIpVNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpVNetAddr.setStatus("mandatory")
_GrIpVNetMask_Type = IpAddress
_GrIpVNetMask_Object = MibTableColumn
grIpVNetMask = _GrIpVNetMask_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 2),
    _GrIpVNetMask_Type()
)
grIpVNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVNetMask.setStatus("mandatory")


class _GrIpVNetEncap_Type(Integer32):
    """Custom type grIpVNetEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ether2", 1),
          ("snap", 2))
    )


_GrIpVNetEncap_Type.__name__ = "Integer32"
_GrIpVNetEncap_Object = MibTableColumn
grIpVNetEncap = _GrIpVNetEncap_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 3),
    _GrIpVNetEncap_Type()
)
grIpVNetEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVNetEncap.setStatus("mandatory")


class _GrIpVBcastAddr_Type(Integer32):
    """Custom type grIpVBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 1),
          ("allZeros", 2))
    )


_GrIpVBcastAddr_Type.__name__ = "Integer32"
_GrIpVBcastAddr_Object = MibTableColumn
grIpVBcastAddr = _GrIpVBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 4),
    _GrIpVBcastAddr_Type()
)
grIpVBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVBcastAddr.setStatus("mandatory")


class _GrIpVRipTx_Type(Integer32):
    """Custom type grIpVRipTx based on Integer32"""
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


_GrIpVRipTx_Type.__name__ = "Integer32"
_GrIpVRipTx_Object = MibTableColumn
grIpVRipTx = _GrIpVRipTx_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 5),
    _GrIpVRipTx_Type()
)
grIpVRipTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVRipTx.setStatus("mandatory")


class _GrIpVSendDefaultRoute_Type(Integer32):
    """Custom type grIpVSendDefaultRoute based on Integer32"""
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


_GrIpVSendDefaultRoute_Type.__name__ = "Integer32"
_GrIpVSendDefaultRoute_Object = MibTableColumn
grIpVSendDefaultRoute = _GrIpVSendDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 6),
    _GrIpVSendDefaultRoute_Type()
)
grIpVSendDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVSendDefaultRoute.setStatus("mandatory")


class _GrIpVSendStaticRoutes_Type(Integer32):
    """Custom type grIpVSendStaticRoutes based on Integer32"""
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


_GrIpVSendStaticRoutes_Type.__name__ = "Integer32"
_GrIpVSendStaticRoutes_Object = MibTableColumn
grIpVSendStaticRoutes = _GrIpVSendStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 7),
    _GrIpVSendStaticRoutes_Type()
)
grIpVSendStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVSendStaticRoutes.setStatus("mandatory")


class _GrIpVRipRx_Type(Integer32):
    """Custom type grIpVRipRx based on Integer32"""
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


_GrIpVRipRx_Type.__name__ = "Integer32"
_GrIpVRipRx_Object = MibTableColumn
grIpVRipRx = _GrIpVRipRx_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 8),
    _GrIpVRipRx_Type()
)
grIpVRipRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVRipRx.setStatus("mandatory")


class _GrIpVRipMetric_Type(Integer32):
    """Custom type grIpVRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GrIpVRipMetric_Type.__name__ = "Integer32"
_GrIpVRipMetric_Object = MibTableColumn
grIpVRipMetric = _GrIpVRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 9),
    _GrIpVRipMetric_Type()
)
grIpVRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVRipMetric.setStatus("mandatory")


class _GrIpVOverrideDefaultRoute_Type(Integer32):
    """Custom type grIpVOverrideDefaultRoute based on Integer32"""
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


_GrIpVOverrideDefaultRoute_Type.__name__ = "Integer32"
_GrIpVOverrideDefaultRoute_Object = MibTableColumn
grIpVOverrideDefaultRoute = _GrIpVOverrideDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 10),
    _GrIpVOverrideDefaultRoute_Type()
)
grIpVOverrideDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVOverrideDefaultRoute.setStatus("mandatory")
_GrIpVIfIndex_Type = Integer32
_GrIpVIfIndex_Object = MibTableColumn
grIpVIfIndex = _GrIpVIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 11),
    _GrIpVIfIndex_Type()
)
grIpVIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVIfIndex.setStatus("mandatory")
_GrIpVStatus_Type = RowStatus
_GrIpVStatus_Object = MibTableColumn
grIpVStatus = _GrIpVStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 9, 1, 12),
    _GrIpVStatus_Type()
)
grIpVStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grIpVStatus.setStatus("mandatory")
_GrIpVRipTable_Object = MibTable
grIpVRipTable = _GrIpVRipTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 10)
)
if mibBuilder.loadTexts:
    grIpVRipTable.setStatus("mandatory")
_GrIpVRipEntry_Object = MibTableRow
grIpVRipEntry = _GrIpVRipEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 10, 1)
)
grIpVRipEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grIpVNetAddr"),
)
if mibBuilder.loadTexts:
    grIpVRipEntry.setStatus("mandatory")
_GrIpVRipRxPkts_Type = Counter32
_GrIpVRipRxPkts_Object = MibTableColumn
grIpVRipRxPkts = _GrIpVRipRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 10, 1, 1),
    _GrIpVRipRxPkts_Type()
)
grIpVRipRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpVRipRxPkts.setStatus("mandatory")
_GrIpVRipRxBadPkts_Type = Counter32
_GrIpVRipRxBadPkts_Object = MibTableColumn
grIpVRipRxBadPkts = _GrIpVRipRxBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 10, 1, 2),
    _GrIpVRipRxBadPkts_Type()
)
grIpVRipRxBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpVRipRxBadPkts.setStatus("mandatory")
_GrIpVRipRxBadRtes_Type = Counter32
_GrIpVRipRxBadRtes_Object = MibTableColumn
grIpVRipRxBadRtes = _GrIpVRipRxBadRtes_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 10, 1, 3),
    _GrIpVRipRxBadRtes_Type()
)
grIpVRipRxBadRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpVRipRxBadRtes.setStatus("mandatory")
_GrIpVRipTxUpdates_Type = Counter32
_GrIpVRipTxUpdates_Object = MibTableColumn
grIpVRipTxUpdates = _GrIpVRipTxUpdates_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 6, 10, 1, 4),
    _GrIpVRipTxUpdates_Type()
)
grIpVRipTxUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grIpVRipTxUpdates.setStatus("mandatory")
_GrSnmpGroup_ObjectIdentity = ObjectIdentity
grSnmpGroup = _GrSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7)
)


class _GrSnmpNetworkSet_Type(Integer32):
    """Custom type grSnmpNetworkSet based on Integer32"""
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


_GrSnmpNetworkSet_Type.__name__ = "Integer32"
_GrSnmpNetworkSet_Object = MibScalar
grSnmpNetworkSet = _GrSnmpNetworkSet_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 1),
    _GrSnmpNetworkSet_Type()
)
grSnmpNetworkSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grSnmpNetworkSet.setStatus("mandatory")
_GrSnmpCommunityTable_Object = MibTable
grSnmpCommunityTable = _GrSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2)
)
if mibBuilder.loadTexts:
    grSnmpCommunityTable.setStatus("mandatory")
_GrSnmpCommunityEntry_Object = MibTableRow
grSnmpCommunityEntry = _GrSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2, 1)
)
grSnmpCommunityEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grCommunityIndex"),
)
if mibBuilder.loadTexts:
    grSnmpCommunityEntry.setStatus("mandatory")
_GrCommunityIndex_Type = Integer32
_GrCommunityIndex_Object = MibTableColumn
grCommunityIndex = _GrCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2, 1, 1),
    _GrCommunityIndex_Type()
)
grCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grCommunityIndex.setStatus("mandatory")


class _GrCommunityName_Type(DisplayString):
    """Custom type grCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GrCommunityName_Type.__name__ = "DisplayString"
_GrCommunityName_Object = MibTableColumn
grCommunityName = _GrCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2, 1, 2),
    _GrCommunityName_Type()
)
grCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grCommunityName.setStatus("mandatory")


class _GrCommunityType_Type(Integer32):
    """Custom type grCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("public", 1),
          ("restricted", 2))
    )


_GrCommunityType_Type.__name__ = "Integer32"
_GrCommunityType_Object = MibTableColumn
grCommunityType = _GrCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2, 1, 3),
    _GrCommunityType_Type()
)
grCommunityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grCommunityType.setStatus("mandatory")


class _GrCommunityPriv_Type(Integer32):
    """Custom type grCommunityPriv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("readonly", 2),
          ("readwrite", 3))
    )


_GrCommunityPriv_Type.__name__ = "Integer32"
_GrCommunityPriv_Object = MibTableColumn
grCommunityPriv = _GrCommunityPriv_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2, 1, 4),
    _GrCommunityPriv_Type()
)
grCommunityPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grCommunityPriv.setStatus("mandatory")


class _GrCommunityTrapGeneration_Type(Integer32):
    """Custom type grCommunityTrapGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("none", 1))
    )


_GrCommunityTrapGeneration_Type.__name__ = "Integer32"
_GrCommunityTrapGeneration_Object = MibTableColumn
grCommunityTrapGeneration = _GrCommunityTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2, 1, 5),
    _GrCommunityTrapGeneration_Type()
)
grCommunityTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grCommunityTrapGeneration.setStatus("mandatory")
_GrCommunityTrapPort_Type = Integer32
_GrCommunityTrapPort_Object = MibTableColumn
grCommunityTrapPort = _GrCommunityTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2, 1, 6),
    _GrCommunityTrapPort_Type()
)
grCommunityTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grCommunityTrapPort.setStatus("mandatory")
_GrCommunityStatus_Type = RowStatus
_GrCommunityStatus_Object = MibTableColumn
grCommunityStatus = _GrCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 2, 1, 7),
    _GrCommunityStatus_Type()
)
grCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grCommunityStatus.setStatus("mandatory")
_GrSnmpCommMemberTable_Object = MibTable
grSnmpCommMemberTable = _GrSnmpCommMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 3)
)
if mibBuilder.loadTexts:
    grSnmpCommMemberTable.setStatus("mandatory")
_GrSnmpCommMemberEntry_Object = MibTableRow
grSnmpCommMemberEntry = _GrSnmpCommMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 3, 1)
)
grSnmpCommMemberEntry.setIndexNames(
    (0, "GANDALF-ROUTER-MIB", "grCommunityIndex"),
    (0, "GANDALF-ROUTER-MIB", "grCommMemberIpAddr"),
)
if mibBuilder.loadTexts:
    grSnmpCommMemberEntry.setStatus("mandatory")
_GrCommMemberIpAddr_Type = IpAddress
_GrCommMemberIpAddr_Object = MibTableColumn
grCommMemberIpAddr = _GrCommMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 3, 1, 1),
    _GrCommMemberIpAddr_Type()
)
grCommMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grCommMemberIpAddr.setStatus("mandatory")
_GrCommMemberStatus_Type = RowStatus
_GrCommMemberStatus_Object = MibTableColumn
grCommMemberStatus = _GrCommMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 7, 3, 1, 2),
    _GrCommMemberStatus_Type()
)
grCommMemberStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grCommMemberStatus.setStatus("mandatory")
_GrPppGroup_ObjectIdentity = ObjectIdentity
grPppGroup = _GrPppGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8)
)
_GrPppLinkStatusTable_Object = MibTable
grPppLinkStatusTable = _GrPppLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8, 1)
)
if mibBuilder.loadTexts:
    grPppLinkStatusTable.setStatus("mandatory")
_GrPppLinkStatusEntry_Object = MibTableRow
grPppLinkStatusEntry = _GrPppLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8, 1, 1)
)
grPppLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grPppLinkStatusEntry.setStatus("mandatory")


class _GrPppLinkStatusMultilink_Type(Integer32):
    """Custom type grPppLinkStatusMultilink based on Integer32"""
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


_GrPppLinkStatusMultilink_Type.__name__ = "Integer32"
_GrPppLinkStatusMultilink_Object = MibTableColumn
grPppLinkStatusMultilink = _GrPppLinkStatusMultilink_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8, 1, 1, 1),
    _GrPppLinkStatusMultilink_Type()
)
grPppLinkStatusMultilink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPppLinkStatusMultilink.setStatus("mandatory")


class _GrPppLinkStatusLapB_Type(Integer32):
    """Custom type grPppLinkStatusLapB based on Integer32"""
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


_GrPppLinkStatusLapB_Type.__name__ = "Integer32"
_GrPppLinkStatusLapB_Object = MibTableColumn
grPppLinkStatusLapB = _GrPppLinkStatusLapB_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8, 1, 1, 2),
    _GrPppLinkStatusLapB_Type()
)
grPppLinkStatusLapB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPppLinkStatusLapB.setStatus("mandatory")
_GrPppIpxTable_Object = MibTable
grPppIpxTable = _GrPppIpxTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8, 2)
)
if mibBuilder.loadTexts:
    grPppIpxTable.setStatus("mandatory")
_GrPppIpxEntry_Object = MibTableRow
grPppIpxEntry = _GrPppIpxEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8, 2, 1)
)
grPppIpxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    grPppIpxEntry.setStatus("mandatory")


class _GrPppIpxAdminStatus_Type(Integer32):
    """Custom type grPppIpxAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_GrPppIpxAdminStatus_Type.__name__ = "Integer32"
_GrPppIpxAdminStatus_Object = MibTableColumn
grPppIpxAdminStatus = _GrPppIpxAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8, 2, 1, 1),
    _GrPppIpxAdminStatus_Type()
)
grPppIpxAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    grPppIpxAdminStatus.setStatus("mandatory")


class _GrPppIpxOperStatus_Type(Integer32):
    """Custom type grPppIpxOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_GrPppIpxOperStatus_Type.__name__ = "Integer32"
_GrPppIpxOperStatus_Object = MibTableColumn
grPppIpxOperStatus = _GrPppIpxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 11, 1, 8, 2, 1, 2),
    _GrPppIpxOperStatus_Type()
)
grPppIpxOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grPppIpxOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

grNewIpDefaultGateway = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 1200)
)
if mibBuilder.loadTexts:
    grNewIpDefaultGateway.setStatus(
        ""
    )

grIpStaticRouteOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 1201)
)
if mibBuilder.loadTexts:
    grIpStaticRouteOverride.setStatus(
        ""
    )

grIpxStaticRouteOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 1202)
)
if mibBuilder.loadTexts:
    grIpxStaticRouteOverride.setStatus(
        ""
    )

grPppLqmFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 1203)
)
if mibBuilder.loadTexts:
    grPppLqmFailed.setStatus(
        ""
    )

grWanRetryThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 1204)
)
if mibBuilder.loadTexts:
    grWanRetryThreshold.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GANDALF-ROUTER-MIB",
    **{"RowStatus": RowStatus,
       "gandalf": gandalf,
       "grNewIpDefaultGateway": grNewIpDefaultGateway,
       "grIpStaticRouteOverride": grIpStaticRouteOverride,
       "grIpxStaticRouteOverride": grIpxStaticRouteOverride,
       "grPppLqmFailed": grPppLqmFailed,
       "grWanRetryThreshold": grWanRetryThreshold,
       "gandalf-router": gandalf_router,
       "grGenerationX": grGenerationX,
       "grGeneral": grGeneral,
       "grSerNum": grSerNum,
       "grSystemName": grSystemName,
       "grSystemPasswd": grSystemPasswd,
       "grdBaseRev": grdBaseRev,
       "grSoftwareRev": grSoftwareRev,
       "grFirmwareRev": grFirmwareRev,
       "grReset": grReset,
       "grDateAndTime": grDateAndTime,
       "grSwitchPosition": grSwitchPosition,
       "grPhysPortGroup": grPhysPortGroup,
       "grPhysNameTable": grPhysNameTable,
       "grPhysNameEntry": grPhysNameEntry,
       "grPhysPortName": grPhysPortName,
       "grPhysPortTable": grPhysPortTable,
       "grPhysPortEntry": grPhysPortEntry,
       "grPhysPortWanType": grPhysPortWanType,
       "grPhysPortSignalling": grPhysPortSignalling,
       "grPhysPortSpeed": grPhysPortSpeed,
       "grPhysPortCallType": grPhysPortCallType,
       "grPhysPortHoldOff": grPhysPortHoldOff,
       "grPhysPortPool": grPhysPortPool,
       "grPhysWanStatsTable": grPhysWanStatsTable,
       "grPhysWanStatsEntry": grPhysWanStatsEntry,
       "grPhysWanStRxCrcErrs": grPhysWanStRxCrcErrs,
       "grPhysWanStRxOverRunErrs": grPhysWanStRxOverRunErrs,
       "grPhysWanStTxUnderRunErrs": grPhysWanStTxUnderRunErrs,
       "grPhysWanStRxAborts": grPhysWanStRxAborts,
       "grPhysWanStTxAborts": grPhysWanStTxAborts,
       "grPhysWanStRxOctetErrors": grPhysWanStRxOctetErrors,
       "grPhysWanStTxOctetErrors": grPhysWanStTxOctetErrors,
       "grPhysWanStLogicalIfIndex": grPhysWanStLogicalIfIndex,
       "grPhysWanStInCalls": grPhysWanStInCalls,
       "grPhysWanStInFails": grPhysWanStInFails,
       "grPhysWanStInSecurityFails": grPhysWanStInSecurityFails,
       "grPhysWanStOutCalls": grPhysWanStOutCalls,
       "grPhysWanStOutFails": grPhysWanStOutFails,
       "grPhysWanStOutSecurityFails": grPhysWanStOutSecurityFails,
       "grLogicalGroup": grLogicalGroup,
       "grLogicalTable": grLogicalTable,
       "grLogicalEntry": grLogicalEntry,
       "grLogicalDestName": grLogicalDestName,
       "grLogicalTimeEnabled": grLogicalTimeEnabled,
       "grLogicalTimeWindow": grLogicalTimeWindow,
       "grLogicalType": grLogicalType,
       "grLogicalStatus": grLogicalStatus,
       "grLogWanTable": grLogWanTable,
       "grLogWanEntry": grLogWanEntry,
       "grLogWanCmprsn": grLogWanCmprsn,
       "grLogWanThshldOvrflw": grLogWanThshldOvrflw,
       "grLogWanThshld": grLogWanThshld,
       "grLogWanConnTimer": grLogWanConnTimer,
       "grLogWanDiscTimer": grLogWanDiscTimer,
       "grLogWanSpoofing": grLogWanSpoofing,
       "grLogWanStatus": grLogWanStatus,
       "grLogWanPortTable": grLogWanPortTable,
       "grLogWanPortEntry": grLogWanPortEntry,
       "grLogWanPortIndex": grLogWanPortIndex,
       "grLogWanPortWanType": grLogWanPortWanType,
       "grLogWanPortPhysIfIndex": grLogWanPortPhysIfIndex,
       "grLogWanPortPool": grLogWanPortPool,
       "grLogWanPortRetry": grLogWanPortRetry,
       "grLogWanPortRetryPeriod": grLogWanPortRetryPeriod,
       "grLogWanPortPrepend": grLogWanPortPrepend,
       "grLogWanPortDestAddr": grLogWanPortDestAddr,
       "grLogWanPortAdminStatus": grLogWanPortAdminStatus,
       "grLogWanPortOperStatus": grLogWanPortOperStatus,
       "grLogWanPortStatus": grLogWanPortStatus,
       "grLogWanStatsTable": grLogWanStatsTable,
       "grLogWanStatsEntry": grLogWanStatsEntry,
       "grLogWanStInUse": grLogWanStInUse,
       "grLogWanStUncmpsdRxOctets": grLogWanStUncmpsdRxOctets,
       "grLogWanStCmpsdRxOctets": grLogWanStCmpsdRxOctets,
       "grLogWanStUncmpsdTxOctets": grLogWanStUncmpsdTxOctets,
       "grLogWanStCmpsdTxOctets": grLogWanStCmpsdTxOctets,
       "grLogWanStConnects": grLogWanStConnects,
       "grLogWanStConnectFails": grLogWanStConnectFails,
       "grVirtualStatsTable": grVirtualStatsTable,
       "grVirtualStatsEntry": grVirtualStatsEntry,
       "grVSProtocolType": grVSProtocolType,
       "grVSNetAddr": grVSNetAddr,
       "grVSIfIndex": grVSIfIndex,
       "grVSRxPkts": grVSRxPkts,
       "grVSTxPkts": grVSTxPkts,
       "grVSRxOctets": grVSRxOctets,
       "grVSTxOctets": grVSTxOctets,
       "grVSTTLDiscards": grVSTTLDiscards,
       "grVSRxFilteredPkts": grVSRxFilteredPkts,
       "grVSTxFilteredPkts": grVSTxFilteredPkts,
       "grBridgeGroup": grBridgeGroup,
       "grBridgingState": grBridgingState,
       "grBrMaxTransitDelay": grBrMaxTransitDelay,
       "grBrFilterTestPackets": grBrFilterTestPackets,
       "grProtFilterType": grProtFilterType,
       "grProtFilterTable": grProtFilterTable,
       "grProtFilterEntry": grProtFilterEntry,
       "grProtFilterId": grProtFilterId,
       "grProtFilterStatus": grProtFilterStatus,
       "grProtPriorityTable": grProtPriorityTable,
       "grProtPriorityEntry": grProtPriorityEntry,
       "grProtPriorityId": grProtPriorityId,
       "grProtPriorityLevel": grProtPriorityLevel,
       "grProtPriorityStatus": grProtPriorityStatus,
       "grBridgePortTable": grBridgePortTable,
       "grBridgePortEntry": grBridgePortEntry,
       "grBrPortStpBpduFilter": grBrPortStpBpduFilter,
       "grBrPortAllowedToGoDef": grBrPortAllowedToGoDef,
       "grBridgePortStatsTable": grBridgePortStatsTable,
       "grBridgePortStatsEntry": grBridgePortStatsEntry,
       "grBrPortStRxOctets": grBrPortStRxOctets,
       "grBrPortStTxOctets": grBrPortStTxOctets,
       "grBrPortStRxFilteredPkts": grBrPortStRxFilteredPkts,
       "grBrPortStTxFilteredPkts": grBrPortStTxFilteredPkts,
       "grSpanningTreeStatus": grSpanningTreeStatus,
       "grIpxGroup": grIpxGroup,
       "grIpxRoutingEnable": grIpxRoutingEnable,
       "grIpxPrimaryNet": grIpxPrimaryNet,
       "grIpxRipEnable": grIpxRipEnable,
       "grIpxSapEnable": grIpxSapEnable,
       "grIpxAccessRestrictEnable": grIpxAccessRestrictEnable,
       "grIpxAccessRestrictTable": grIpxAccessRestrictTable,
       "grIpxAccessRestrictEntry": grIpxAccessRestrictEntry,
       "grIpxAccIndex": grIpxAccIndex,
       "grIpxAccName": grIpxAccName,
       "grIpxAccType": grIpxAccType,
       "grIpxAccSrcNet": grIpxAccSrcNet,
       "grIpxAccSrcNode": grIpxAccSrcNode,
       "grIpxAccSrcSocketFrom": grIpxAccSrcSocketFrom,
       "grIpxAccSrcSocketTo": grIpxAccSrcSocketTo,
       "grIpxAccDstNet": grIpxAccDstNet,
       "grIpxAccDstNode": grIpxAccDstNode,
       "grIpxAccDstSocketFrom": grIpxAccDstSocketFrom,
       "grIpxAccDstSocketTo": grIpxAccDstSocketTo,
       "grIpxAccStatus": grIpxAccStatus,
       "grIpxRouteTable": grIpxRouteTable,
       "grIpxRouteEntry": grIpxRouteEntry,
       "grIpxRouteDest": grIpxRouteDest,
       "grIpxRouteType": grIpxRouteType,
       "grIpxRouteHops": grIpxRouteHops,
       "grIpxRouteDelay": grIpxRouteDelay,
       "grIpxRouteAge": grIpxRouteAge,
       "grIpxRouteNextHopNet": grIpxRouteNextHopNet,
       "grIpxRouteNextHopNode": grIpxRouteNextHopNode,
       "grIpxRouteIfIndex": grIpxRouteIfIndex,
       "grIpxRouteStatus": grIpxRouteStatus,
       "grIpxServerTable": grIpxServerTable,
       "grIpxServerEntry": grIpxServerEntry,
       "grIpxServerType": grIpxServerType,
       "grIpxServerSapType": grIpxServerSapType,
       "grIpxServerName": grIpxServerName,
       "grIpxServerAge": grIpxServerAge,
       "grIpxServerNet": grIpxServerNet,
       "grIpxServerNode": grIpxServerNode,
       "grIpxServerSocket": grIpxServerSocket,
       "grIpxServerStatus": grIpxServerStatus,
       "grIpxInReceives": grIpxInReceives,
       "grIpxInHdrErrors": grIpxInHdrErrors,
       "grIpxForwDatagrams": grIpxForwDatagrams,
       "grIpxInUnknownSockets": grIpxInUnknownSockets,
       "grIpxInDiscards": grIpxInDiscards,
       "grIpxInDelivers": grIpxInDelivers,
       "grIpxOutRequests": grIpxOutRequests,
       "grIpxOutDiscards": grIpxOutDiscards,
       "grIpxOutNoRoutes": grIpxOutNoRoutes,
       "grIpxLogicalTable": grIpxLogicalTable,
       "grIpxLogicalEntry": grIpxLogicalEntry,
       "grIpxLAccessDef": grIpxLAccessDef,
       "grIpxLRestrictions": grIpxLRestrictions,
       "grIpxLTransport": grIpxLTransport,
       "grIpxLStatus": grIpxLStatus,
       "grIpxVirtualTable": grIpxVirtualTable,
       "grIpxVirtualEntry": grIpxVirtualEntry,
       "grIpxVNetAddr": grIpxVNetAddr,
       "grIpxVNetEncap": grIpxVNetEncap,
       "grIpxVRipEnable": grIpxVRipEnable,
       "grIpxVRipMetric": grIpxVRipMetric,
       "grIpxVRipTxPeriod": grIpxVRipTxPeriod,
       "grIpxVRipAgeTimer": grIpxVRipAgeTimer,
       "grIpxVSapEnable": grIpxVSapEnable,
       "grIpxVSapTxPeriod": grIpxVSapTxPeriod,
       "grIpxVSapAgeTimer": grIpxVSapAgeTimer,
       "grIpxVWdogSpoof": grIpxVWdogSpoof,
       "grIpxVIfIndex": grIpxVIfIndex,
       "grIpxVStatus": grIpxVStatus,
       "grIpxVRipTable": grIpxVRipTable,
       "grIpxVRipEntry": grIpxVRipEntry,
       "grIpxVRipRtePkts": grIpxVRipRtePkts,
       "grIpxVRipHopCntExcs": grIpxVRipHopCntExcs,
       "grIpxVRipNetbHopCntExcs": grIpxVRipNetbHopCntExcs,
       "grIpxVRipNoNetAddRcvs": grIpxVRipNoNetAddRcvs,
       "grIpxVRipRxGenQs": grIpxVRipRxGenQs,
       "grIpxVRipRxNearQs": grIpxVRipRxNearQs,
       "grIpxVRipRxGenRs": grIpxVRipRxGenRs,
       "grIpxVRipRxNearRs": grIpxVRipRxNearRs,
       "grIpxVRipTxGenQs": grIpxVRipTxGenQs,
       "grIpxVRipTxNearQs": grIpxVRipTxNearQs,
       "grIpxVRipTxGenRs": grIpxVRipTxGenRs,
       "grIpxVRipTxNearRs": grIpxVRipTxNearRs,
       "grIpxVRipRxUnknGenQs": grIpxVRipRxUnknGenQs,
       "grIpxVRipRxUnknNearQs": grIpxVRipRxUnknNearQs,
       "grIpxVRipRxUnknGenRs": grIpxVRipRxUnknGenRs,
       "grIpxVRipRxUnknNearRs": grIpxVRipRxUnknNearRs,
       "grIpxVRipAgedOuts": grIpxVRipAgedOuts,
       "grIpxVRipPeriodics": grIpxVRipPeriodics,
       "grIpxVRipUpdates": grIpxVRipUpdates,
       "grIpxVRipWrongNets": grIpxVRipWrongNets,
       "grIpxVRipBadInfos": grIpxVRipBadInfos,
       "grIpxVSapTable": grIpxVSapTable,
       "grIpxVSapEntry": grIpxVSapEntry,
       "grIpxVSapRxGenQs": grIpxVSapRxGenQs,
       "grIpxVSapRxNearQs": grIpxVSapRxNearQs,
       "grIpxVSapRxGenRs": grIpxVSapRxGenRs,
       "grIpxVSapRxNearRs": grIpxVSapRxNearRs,
       "grIpxVSapTxGenQs": grIpxVSapTxGenQs,
       "grIpxVSapTxNearQs": grIpxVSapTxNearQs,
       "grIpxVSapTxGenRs": grIpxVSapTxGenRs,
       "grIpxVSapTxNearRs": grIpxVSapTxNearRs,
       "grIpxVSapRxUnknGenQs": grIpxVSapRxUnknGenQs,
       "grIpxVSapRxUnknNearQs": grIpxVSapRxUnknNearQs,
       "grIpxVSapRxUnknGenRs": grIpxVSapRxUnknGenRs,
       "grIpxVSapRxUnknNearRs": grIpxVSapRxUnknNearRs,
       "grIpxVSapAgedOuts": grIpxVSapAgedOuts,
       "grIpxVSapPeriodics": grIpxVSapPeriodics,
       "grIpxVSapUpdates": grIpxVSapUpdates,
       "grIpxVSapWrongNets": grIpxVSapWrongNets,
       "grIpxVSapBadInfos": grIpxVSapBadInfos,
       "grIpGroup": grIpGroup,
       "grIpRipEnable": grIpRipEnable,
       "grIpArpCacheAge": grIpArpCacheAge,
       "grIpProxyArp": grIpProxyArp,
       "grIpTrustedGatewayEnable": grIpTrustedGatewayEnable,
       "grIpTrustedGatewayTable": grIpTrustedGatewayTable,
       "grIpTrustedGatewayEntry": grIpTrustedGatewayEntry,
       "grIpGatewayAddr": grIpGatewayAddr,
       "grIpGatewayName": grIpGatewayName,
       "grIpGatewayStatus": grIpGatewayStatus,
       "grIpAccessRestrictEnable": grIpAccessRestrictEnable,
       "grIpAccessRestrictTable": grIpAccessRestrictTable,
       "grIpAccessRestrictEntry": grIpAccessRestrictEntry,
       "grIpAccIndex": grIpAccIndex,
       "grIpAccName": grIpAccName,
       "grIpAccType": grIpAccType,
       "grIpAccSrcNet": grIpAccSrcNet,
       "grIpAccSrcMask": grIpAccSrcMask,
       "grIpAccDstNet": grIpAccDstNet,
       "grIpAccDstMask": grIpAccDstMask,
       "grIpAccProtocolFrom": grIpAccProtocolFrom,
       "grIpAccProtocolTo": grIpAccProtocolTo,
       "grIpAccPortFrom": grIpAccPortFrom,
       "grIpAccPortTo": grIpAccPortTo,
       "grIpAccStatus": grIpAccStatus,
       "grIpLogicalTable": grIpLogicalTable,
       "grIpLogicalEntry": grIpLogicalEntry,
       "grIpLAccessDef": grIpLAccessDef,
       "grIpLRestrictions": grIpLRestrictions,
       "grIpLTransport": grIpLTransport,
       "grIpLStatus": grIpLStatus,
       "grIpVirtualTable": grIpVirtualTable,
       "grIpVirtualEntry": grIpVirtualEntry,
       "grIpVNetAddr": grIpVNetAddr,
       "grIpVNetMask": grIpVNetMask,
       "grIpVNetEncap": grIpVNetEncap,
       "grIpVBcastAddr": grIpVBcastAddr,
       "grIpVRipTx": grIpVRipTx,
       "grIpVSendDefaultRoute": grIpVSendDefaultRoute,
       "grIpVSendStaticRoutes": grIpVSendStaticRoutes,
       "grIpVRipRx": grIpVRipRx,
       "grIpVRipMetric": grIpVRipMetric,
       "grIpVOverrideDefaultRoute": grIpVOverrideDefaultRoute,
       "grIpVIfIndex": grIpVIfIndex,
       "grIpVStatus": grIpVStatus,
       "grIpVRipTable": grIpVRipTable,
       "grIpVRipEntry": grIpVRipEntry,
       "grIpVRipRxPkts": grIpVRipRxPkts,
       "grIpVRipRxBadPkts": grIpVRipRxBadPkts,
       "grIpVRipRxBadRtes": grIpVRipRxBadRtes,
       "grIpVRipTxUpdates": grIpVRipTxUpdates,
       "grSnmpGroup": grSnmpGroup,
       "grSnmpNetworkSet": grSnmpNetworkSet,
       "grSnmpCommunityTable": grSnmpCommunityTable,
       "grSnmpCommunityEntry": grSnmpCommunityEntry,
       "grCommunityIndex": grCommunityIndex,
       "grCommunityName": grCommunityName,
       "grCommunityType": grCommunityType,
       "grCommunityPriv": grCommunityPriv,
       "grCommunityTrapGeneration": grCommunityTrapGeneration,
       "grCommunityTrapPort": grCommunityTrapPort,
       "grCommunityStatus": grCommunityStatus,
       "grSnmpCommMemberTable": grSnmpCommMemberTable,
       "grSnmpCommMemberEntry": grSnmpCommMemberEntry,
       "grCommMemberIpAddr": grCommMemberIpAddr,
       "grCommMemberStatus": grCommMemberStatus,
       "grPppGroup": grPppGroup,
       "grPppLinkStatusTable": grPppLinkStatusTable,
       "grPppLinkStatusEntry": grPppLinkStatusEntry,
       "grPppLinkStatusMultilink": grPppLinkStatusMultilink,
       "grPppLinkStatusLapB": grPppLinkStatusLapB,
       "grPppIpxTable": grPppIpxTable,
       "grPppIpxEntry": grPppIpxEntry,
       "grPppIpxAdminStatus": grPppIpxAdminStatus,
       "grPppIpxOperStatus": grPppIpxOperStatus}
)
