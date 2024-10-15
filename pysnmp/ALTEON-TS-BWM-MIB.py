# SNMP MIB module (ALTEON-TS-BWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-TS-BWM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:59 2024
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

(switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "switch")

(information,
 operCmds,
 stats) = mibBuilder.importSymbols(
    "ALTEON-TIGON-SWITCH-MIB",
    "information",
    "operCmds",
    "stats")

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

_BwmStats_ObjectIdentity = ObjectIdentity
bwmStats = _BwmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15)
)
_BwmStatTcTable_Object = MibTable
bwmStatTcTable = _BwmStatTcTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1)
)
if mibBuilder.loadTexts:
    bwmStatTcTable.setStatus("mandatory")
_BwmStatTcEntry_Object = MibTableRow
bwmStatTcEntry = _BwmStatTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1)
)
bwmStatTcEntry.setIndexNames(
    (0, "ALTEON-TS-BWM-MIB", "bwmStatTcContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatTcEntry.setStatus("mandatory")
_BwmStatTcContractIndex_Type = Integer32
_BwmStatTcContractIndex_Object = MibTableColumn
bwmStatTcContractIndex = _BwmStatTcContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 1),
    _BwmStatTcContractIndex_Type()
)
bwmStatTcContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcContractIndex.setStatus("mandatory")


class _BwmStatTcName_Type(DisplayString):
    """Custom type bwmStatTcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BwmStatTcName_Type.__name__ = "DisplayString"
_BwmStatTcName_Object = MibTableColumn
bwmStatTcName = _BwmStatTcName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 2),
    _BwmStatTcName_Type()
)
bwmStatTcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcName.setStatus("mandatory")
_BwmStatTcOutoct_Type = Counter32
_BwmStatTcOutoct_Object = MibTableColumn
bwmStatTcOutoct = _BwmStatTcOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 3),
    _BwmStatTcOutoct_Type()
)
bwmStatTcOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcOutoct.setStatus("mandatory")
_BwmStatTcOutdisoct_Type = Counter32
_BwmStatTcOutdisoct_Object = MibTableColumn
bwmStatTcOutdisoct = _BwmStatTcOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 4),
    _BwmStatTcOutdisoct_Type()
)
bwmStatTcOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcOutdisoct.setStatus("mandatory")
_BwmStatTcBufferUsed_Type = Counter32
_BwmStatTcBufferUsed_Object = MibTableColumn
bwmStatTcBufferUsed = _BwmStatTcBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 5),
    _BwmStatTcBufferUsed_Type()
)
bwmStatTcBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcBufferUsed.setStatus("mandatory")
_BwmStatTcBufferMax_Type = Counter32
_BwmStatTcBufferMax_Object = MibTableColumn
bwmStatTcBufferMax = _BwmStatTcBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 1, 1, 6),
    _BwmStatTcBufferMax_Type()
)
bwmStatTcBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcBufferMax.setStatus("mandatory")
_BwmStatTcrTable_Object = MibTable
bwmStatTcrTable = _BwmStatTcrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2)
)
if mibBuilder.loadTexts:
    bwmStatTcrTable.setStatus("mandatory")
_BwmStatTcrEntry_Object = MibTableRow
bwmStatTcrEntry = _BwmStatTcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1)
)
bwmStatTcrEntry.setIndexNames(
    (0, "ALTEON-TS-BWM-MIB", "bwmStatTcrContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatTcrEntry.setStatus("mandatory")
_BwmStatTcrContractIndex_Type = Integer32
_BwmStatTcrContractIndex_Object = MibTableColumn
bwmStatTcrContractIndex = _BwmStatTcrContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 1),
    _BwmStatTcrContractIndex_Type()
)
bwmStatTcrContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrContractIndex.setStatus("mandatory")


class _BwmStatTcrName_Type(DisplayString):
    """Custom type bwmStatTcrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BwmStatTcrName_Type.__name__ = "DisplayString"
_BwmStatTcrName_Object = MibTableColumn
bwmStatTcrName = _BwmStatTcrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 2),
    _BwmStatTcrName_Type()
)
bwmStatTcrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrName.setStatus("mandatory")
_BwmStatTcrRate_Type = Integer32
_BwmStatTcrRate_Object = MibTableColumn
bwmStatTcrRate = _BwmStatTcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 3),
    _BwmStatTcrRate_Type()
)
bwmStatTcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrRate.setStatus("mandatory")
_BwmStatTcrOutoct_Type = Counter32
_BwmStatTcrOutoct_Object = MibTableColumn
bwmStatTcrOutoct = _BwmStatTcrOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 4),
    _BwmStatTcrOutoct_Type()
)
bwmStatTcrOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrOutoct.setStatus("mandatory")
_BwmStatTcrOutdisoct_Type = Counter32
_BwmStatTcrOutdisoct_Object = MibTableColumn
bwmStatTcrOutdisoct = _BwmStatTcrOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 5),
    _BwmStatTcrOutdisoct_Type()
)
bwmStatTcrOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrOutdisoct.setStatus("mandatory")
_BwmStatTcrBufferUsed_Type = Counter32
_BwmStatTcrBufferUsed_Object = MibTableColumn
bwmStatTcrBufferUsed = _BwmStatTcrBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 6),
    _BwmStatTcrBufferUsed_Type()
)
bwmStatTcrBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrBufferUsed.setStatus("mandatory")
_BwmStatTcrBufferMax_Type = Counter32
_BwmStatTcrBufferMax_Object = MibTableColumn
bwmStatTcrBufferMax = _BwmStatTcrBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 2, 1, 7),
    _BwmStatTcrBufferMax_Type()
)
bwmStatTcrBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrBufferMax.setStatus("mandatory")
_BwmStatSpTcTable_Object = MibTable
bwmStatSpTcTable = _BwmStatSpTcTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3)
)
if mibBuilder.loadTexts:
    bwmStatSpTcTable.setStatus("mandatory")
_BwmStatSpTcEntry_Object = MibTableRow
bwmStatSpTcEntry = _BwmStatSpTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1)
)
bwmStatSpTcEntry.setIndexNames(
    (0, "ALTEON-TS-BWM-MIB", "bwmStatSpTcPortIndex"),
    (0, "ALTEON-TS-BWM-MIB", "bwmStatSpTcContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatSpTcEntry.setStatus("mandatory")
_BwmStatSpTcPortIndex_Type = Integer32
_BwmStatSpTcPortIndex_Object = MibTableColumn
bwmStatSpTcPortIndex = _BwmStatSpTcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 1),
    _BwmStatSpTcPortIndex_Type()
)
bwmStatSpTcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcPortIndex.setStatus("mandatory")
_BwmStatSpTcContractIndex_Type = Integer32
_BwmStatSpTcContractIndex_Object = MibTableColumn
bwmStatSpTcContractIndex = _BwmStatSpTcContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 2),
    _BwmStatSpTcContractIndex_Type()
)
bwmStatSpTcContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcContractIndex.setStatus("mandatory")


class _BwmStatSpTcName_Type(DisplayString):
    """Custom type bwmStatSpTcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BwmStatSpTcName_Type.__name__ = "DisplayString"
_BwmStatSpTcName_Object = MibTableColumn
bwmStatSpTcName = _BwmStatSpTcName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 3),
    _BwmStatSpTcName_Type()
)
bwmStatSpTcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcName.setStatus("mandatory")
_BwmStatSpTcOutoct_Type = Counter32
_BwmStatSpTcOutoct_Object = MibTableColumn
bwmStatSpTcOutoct = _BwmStatSpTcOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 4),
    _BwmStatSpTcOutoct_Type()
)
bwmStatSpTcOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcOutoct.setStatus("mandatory")
_BwmStatSpTcOutdisoct_Type = Counter32
_BwmStatSpTcOutdisoct_Object = MibTableColumn
bwmStatSpTcOutdisoct = _BwmStatSpTcOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 5),
    _BwmStatSpTcOutdisoct_Type()
)
bwmStatSpTcOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcOutdisoct.setStatus("mandatory")
_BwmStatSpTcBufferUsed_Type = Counter32
_BwmStatSpTcBufferUsed_Object = MibTableColumn
bwmStatSpTcBufferUsed = _BwmStatSpTcBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 6),
    _BwmStatSpTcBufferUsed_Type()
)
bwmStatSpTcBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcBufferUsed.setStatus("mandatory")
_BwmStatSpTcBufferMax_Type = Counter32
_BwmStatSpTcBufferMax_Object = MibTableColumn
bwmStatSpTcBufferMax = _BwmStatSpTcBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 3, 1, 7),
    _BwmStatSpTcBufferMax_Type()
)
bwmStatSpTcBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcBufferMax.setStatus("mandatory")
_BwmStatSpTcrTable_Object = MibTable
bwmStatSpTcrTable = _BwmStatSpTcrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4)
)
if mibBuilder.loadTexts:
    bwmStatSpTcrTable.setStatus("mandatory")
_BwmStatSpTcrEntry_Object = MibTableRow
bwmStatSpTcrEntry = _BwmStatSpTcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1)
)
bwmStatSpTcrEntry.setIndexNames(
    (0, "ALTEON-TS-BWM-MIB", "bwmStatSpTcrPortIndex"),
    (0, "ALTEON-TS-BWM-MIB", "bwmStatSpTcrContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatSpTcrEntry.setStatus("mandatory")
_BwmStatSpTcrPortIndex_Type = Integer32
_BwmStatSpTcrPortIndex_Object = MibTableColumn
bwmStatSpTcrPortIndex = _BwmStatSpTcrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 1),
    _BwmStatSpTcrPortIndex_Type()
)
bwmStatSpTcrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrPortIndex.setStatus("mandatory")
_BwmStatSpTcrContractIndex_Type = Integer32
_BwmStatSpTcrContractIndex_Object = MibTableColumn
bwmStatSpTcrContractIndex = _BwmStatSpTcrContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 2),
    _BwmStatSpTcrContractIndex_Type()
)
bwmStatSpTcrContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrContractIndex.setStatus("mandatory")


class _BwmStatSpTcrName_Type(DisplayString):
    """Custom type bwmStatSpTcrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BwmStatSpTcrName_Type.__name__ = "DisplayString"
_BwmStatSpTcrName_Object = MibTableColumn
bwmStatSpTcrName = _BwmStatSpTcrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 3),
    _BwmStatSpTcrName_Type()
)
bwmStatSpTcrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrName.setStatus("mandatory")
_BwmStatSpTcrRate_Type = Integer32
_BwmStatSpTcrRate_Object = MibTableColumn
bwmStatSpTcrRate = _BwmStatSpTcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 4),
    _BwmStatSpTcrRate_Type()
)
bwmStatSpTcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrRate.setStatus("mandatory")
_BwmStatSpTcrOutoct_Type = Counter32
_BwmStatSpTcrOutoct_Object = MibTableColumn
bwmStatSpTcrOutoct = _BwmStatSpTcrOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 5),
    _BwmStatSpTcrOutoct_Type()
)
bwmStatSpTcrOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrOutoct.setStatus("mandatory")
_BwmStatSpTcrOutdisoct_Type = Counter32
_BwmStatSpTcrOutdisoct_Object = MibTableColumn
bwmStatSpTcrOutdisoct = _BwmStatSpTcrOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 6),
    _BwmStatSpTcrOutdisoct_Type()
)
bwmStatSpTcrOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrOutdisoct.setStatus("mandatory")
_BwmStatSpTcrBufferUsed_Type = Counter32
_BwmStatSpTcrBufferUsed_Object = MibTableColumn
bwmStatSpTcrBufferUsed = _BwmStatSpTcrBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 7),
    _BwmStatSpTcrBufferUsed_Type()
)
bwmStatSpTcrBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrBufferUsed.setStatus("mandatory")
_BwmStatSpTcrBufferMax_Type = Counter32
_BwmStatSpTcrBufferMax_Object = MibTableColumn
bwmStatSpTcrBufferMax = _BwmStatSpTcrBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 15, 4, 1, 8),
    _BwmStatSpTcrBufferMax_Type()
)
bwmStatSpTcrBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatSpTcrBufferMax.setStatus("mandatory")
_BwmOper_ObjectIdentity = ObjectIdentity
bwmOper = _BwmOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 2)
)


class _BwmOperSendSMTP_Type(Integer32):
    """Custom type bwmOperSendSMTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("send", 2))
    )


_BwmOperSendSMTP_Type.__name__ = "Integer32"
_BwmOperSendSMTP_Object = MibScalar
bwmOperSendSMTP = _BwmOperSendSMTP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 2, 1),
    _BwmOperSendSMTP_Type()
)
bwmOperSendSMTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmOperSendSMTP.setStatus("mandatory")
_Bwm_ObjectIdentity = ObjectIdentity
bwm = _Bwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17)
)
_BwmGeneralConfig_ObjectIdentity = ObjectIdentity
bwmGeneralConfig = _BwmGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1)
)


class _BwmCurCfgGenState_Type(Integer32):
    """Custom type bwmCurCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_BwmCurCfgGenState_Type.__name__ = "Integer32"
_BwmCurCfgGenState_Object = MibScalar
bwmCurCfgGenState = _BwmCurCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 1),
    _BwmCurCfgGenState_Type()
)
bwmCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenState.setStatus("mandatory")


class _BwmNewCfgGenState_Type(Integer32):
    """Custom type bwmNewCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_BwmNewCfgGenState_Type.__name__ = "Integer32"
_BwmNewCfgGenState_Object = MibScalar
bwmNewCfgGenState = _BwmNewCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 2),
    _BwmNewCfgGenState_Type()
)
bwmNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenState.setStatus("mandatory")


class _BwmCurCfgGenEnforcePolicy_Type(Integer32):
    """Custom type bwmCurCfgGenEnforcePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgGenEnforcePolicy_Type.__name__ = "Integer32"
_BwmCurCfgGenEnforcePolicy_Object = MibScalar
bwmCurCfgGenEnforcePolicy = _BwmCurCfgGenEnforcePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 3),
    _BwmCurCfgGenEnforcePolicy_Type()
)
bwmCurCfgGenEnforcePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenEnforcePolicy.setStatus("mandatory")


class _BwmNewCfgGenEnforcePolicy_Type(Integer32):
    """Custom type bwmNewCfgGenEnforcePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgGenEnforcePolicy_Type.__name__ = "Integer32"
_BwmNewCfgGenEnforcePolicy_Object = MibScalar
bwmNewCfgGenEnforcePolicy = _BwmNewCfgGenEnforcePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 4),
    _BwmNewCfgGenEnforcePolicy_Type()
)
bwmNewCfgGenEnforcePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenEnforcePolicy.setStatus("mandatory")


class _BwmCurCfgGenSmtpUser_Type(DisplayString):
    """Custom type bwmCurCfgGenSmtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BwmCurCfgGenSmtpUser_Type.__name__ = "DisplayString"
_BwmCurCfgGenSmtpUser_Object = MibScalar
bwmCurCfgGenSmtpUser = _BwmCurCfgGenSmtpUser_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 5),
    _BwmCurCfgGenSmtpUser_Type()
)
bwmCurCfgGenSmtpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenSmtpUser.setStatus("mandatory")


class _BwmNewCfgGenSmtpUser_Type(DisplayString):
    """Custom type bwmNewCfgGenSmtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BwmNewCfgGenSmtpUser_Type.__name__ = "DisplayString"
_BwmNewCfgGenSmtpUser_Object = MibScalar
bwmNewCfgGenSmtpUser = _BwmNewCfgGenSmtpUser_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 1, 6),
    _BwmNewCfgGenSmtpUser_Type()
)
bwmNewCfgGenSmtpUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenSmtpUser.setStatus("mandatory")
_BwmPolicyConfig_ObjectIdentity = ObjectIdentity
bwmPolicyConfig = _BwmPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2)
)
_BwmPolicyTableMaxEnt_Type = Integer32
_BwmPolicyTableMaxEnt_Object = MibScalar
bwmPolicyTableMaxEnt = _BwmPolicyTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 1),
    _BwmPolicyTableMaxEnt_Type()
)
bwmPolicyTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmPolicyTableMaxEnt.setStatus("mandatory")
_BwmCurCfgPolicyTable_Object = MibTable
bwmCurCfgPolicyTable = _BwmCurCfgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2)
)
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTable.setStatus("mandatory")
_BwmCurCfgPolicyTableEntry_Object = MibTableRow
bwmCurCfgPolicyTableEntry = _BwmCurCfgPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1)
)
bwmCurCfgPolicyTableEntry.setIndexNames(
    (0, "ALTEON-TS-BWM-MIB", "bwmCurCfgPolicyIndx"),
)
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTableEntry.setStatus("mandatory")
_BwmCurCfgPolicyIndx_Type = Integer32
_BwmCurCfgPolicyIndx_Object = MibTableColumn
bwmCurCfgPolicyIndx = _BwmCurCfgPolicyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 1),
    _BwmCurCfgPolicyIndx_Type()
)
bwmCurCfgPolicyIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyIndx.setStatus("mandatory")


class _BwmCurCfgPolicyTosIn_Type(Integer32):
    """Custom type bwmCurCfgPolicyTosIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmCurCfgPolicyTosIn_Type.__name__ = "Integer32"
_BwmCurCfgPolicyTosIn_Object = MibTableColumn
bwmCurCfgPolicyTosIn = _BwmCurCfgPolicyTosIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 2),
    _BwmCurCfgPolicyTosIn_Type()
)
bwmCurCfgPolicyTosIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTosIn.setStatus("mandatory")


class _BwmCurCfgPolicyTosOut_Type(Integer32):
    """Custom type bwmCurCfgPolicyTosOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmCurCfgPolicyTosOut_Type.__name__ = "Integer32"
_BwmCurCfgPolicyTosOut_Object = MibTableColumn
bwmCurCfgPolicyTosOut = _BwmCurCfgPolicyTosOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 3),
    _BwmCurCfgPolicyTosOut_Type()
)
bwmCurCfgPolicyTosOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTosOut.setStatus("mandatory")


class _BwmCurCfgPolicyHard_Type(DisplayString):
    """Custom type bwmCurCfgPolicyHard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmCurCfgPolicyHard_Type.__name__ = "DisplayString"
_BwmCurCfgPolicyHard_Object = MibTableColumn
bwmCurCfgPolicyHard = _BwmCurCfgPolicyHard_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 4),
    _BwmCurCfgPolicyHard_Type()
)
bwmCurCfgPolicyHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyHard.setStatus("mandatory")


class _BwmCurCfgPolicySoft_Type(DisplayString):
    """Custom type bwmCurCfgPolicySoft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmCurCfgPolicySoft_Type.__name__ = "DisplayString"
_BwmCurCfgPolicySoft_Object = MibTableColumn
bwmCurCfgPolicySoft = _BwmCurCfgPolicySoft_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 5),
    _BwmCurCfgPolicySoft_Type()
)
bwmCurCfgPolicySoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicySoft.setStatus("mandatory")


class _BwmCurCfgPolicyResv_Type(DisplayString):
    """Custom type bwmCurCfgPolicyResv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmCurCfgPolicyResv_Type.__name__ = "DisplayString"
_BwmCurCfgPolicyResv_Object = MibTableColumn
bwmCurCfgPolicyResv = _BwmCurCfgPolicyResv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 6),
    _BwmCurCfgPolicyResv_Type()
)
bwmCurCfgPolicyResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyResv.setStatus("mandatory")


class _BwmCurCfgPolicyBuffer_Type(Integer32):
    """Custom type bwmCurCfgPolicyBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 128000),
    )


_BwmCurCfgPolicyBuffer_Type.__name__ = "Integer32"
_BwmCurCfgPolicyBuffer_Object = MibTableColumn
bwmCurCfgPolicyBuffer = _BwmCurCfgPolicyBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 2, 1, 7),
    _BwmCurCfgPolicyBuffer_Type()
)
bwmCurCfgPolicyBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyBuffer.setStatus("mandatory")
_BwmNewCfgPolicyTable_Object = MibTable
bwmNewCfgPolicyTable = _BwmNewCfgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3)
)
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTable.setStatus("mandatory")
_BwmNewCfgPolicyTableEntry_Object = MibTableRow
bwmNewCfgPolicyTableEntry = _BwmNewCfgPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1)
)
bwmNewCfgPolicyTableEntry.setIndexNames(
    (0, "ALTEON-TS-BWM-MIB", "bwmNewCfgPolicyIndx"),
)
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTableEntry.setStatus("mandatory")
_BwmNewCfgPolicyIndx_Type = Integer32
_BwmNewCfgPolicyIndx_Object = MibTableColumn
bwmNewCfgPolicyIndx = _BwmNewCfgPolicyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 1),
    _BwmNewCfgPolicyIndx_Type()
)
bwmNewCfgPolicyIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyIndx.setStatus("mandatory")


class _BwmNewCfgPolicyTosIn_Type(Integer32):
    """Custom type bwmNewCfgPolicyTosIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmNewCfgPolicyTosIn_Type.__name__ = "Integer32"
_BwmNewCfgPolicyTosIn_Object = MibTableColumn
bwmNewCfgPolicyTosIn = _BwmNewCfgPolicyTosIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 2),
    _BwmNewCfgPolicyTosIn_Type()
)
bwmNewCfgPolicyTosIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTosIn.setStatus("mandatory")


class _BwmNewCfgPolicyTosOut_Type(Integer32):
    """Custom type bwmNewCfgPolicyTosOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmNewCfgPolicyTosOut_Type.__name__ = "Integer32"
_BwmNewCfgPolicyTosOut_Object = MibTableColumn
bwmNewCfgPolicyTosOut = _BwmNewCfgPolicyTosOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 3),
    _BwmNewCfgPolicyTosOut_Type()
)
bwmNewCfgPolicyTosOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTosOut.setStatus("mandatory")


class _BwmNewCfgPolicyHard_Type(DisplayString):
    """Custom type bwmNewCfgPolicyHard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicyHard_Type.__name__ = "DisplayString"
_BwmNewCfgPolicyHard_Object = MibTableColumn
bwmNewCfgPolicyHard = _BwmNewCfgPolicyHard_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 4),
    _BwmNewCfgPolicyHard_Type()
)
bwmNewCfgPolicyHard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyHard.setStatus("mandatory")


class _BwmNewCfgPolicySoft_Type(DisplayString):
    """Custom type bwmNewCfgPolicySoft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicySoft_Type.__name__ = "DisplayString"
_BwmNewCfgPolicySoft_Object = MibTableColumn
bwmNewCfgPolicySoft = _BwmNewCfgPolicySoft_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 5),
    _BwmNewCfgPolicySoft_Type()
)
bwmNewCfgPolicySoft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicySoft.setStatus("mandatory")


class _BwmNewCfgPolicyResv_Type(DisplayString):
    """Custom type bwmNewCfgPolicyResv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicyResv_Type.__name__ = "DisplayString"
_BwmNewCfgPolicyResv_Object = MibTableColumn
bwmNewCfgPolicyResv = _BwmNewCfgPolicyResv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 6),
    _BwmNewCfgPolicyResv_Type()
)
bwmNewCfgPolicyResv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyResv.setStatus("mandatory")


class _BwmNewCfgPolicyBuffer_Type(Integer32):
    """Custom type bwmNewCfgPolicyBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 128000),
    )


_BwmNewCfgPolicyBuffer_Type.__name__ = "Integer32"
_BwmNewCfgPolicyBuffer_Object = MibTableColumn
bwmNewCfgPolicyBuffer = _BwmNewCfgPolicyBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 7),
    _BwmNewCfgPolicyBuffer_Type()
)
bwmNewCfgPolicyBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyBuffer.setStatus("mandatory")


class _BwmNewCfgPolicyDelete_Type(Integer32):
    """Custom type bwmNewCfgPolicyDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_BwmNewCfgPolicyDelete_Type.__name__ = "Integer32"
_BwmNewCfgPolicyDelete_Object = MibTableColumn
bwmNewCfgPolicyDelete = _BwmNewCfgPolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 2, 3, 1, 8),
    _BwmNewCfgPolicyDelete_Type()
)
bwmNewCfgPolicyDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyDelete.setStatus("mandatory")
_BwmContractConfig_ObjectIdentity = ObjectIdentity
bwmContractConfig = _BwmContractConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3)
)
_BwmContractTableMaxEnt_Type = Integer32
_BwmContractTableMaxEnt_Object = MibScalar
bwmContractTableMaxEnt = _BwmContractTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 1),
    _BwmContractTableMaxEnt_Type()
)
bwmContractTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContractTableMaxEnt.setStatus("mandatory")
_BwmCurCfgContractTable_Object = MibTable
bwmCurCfgContractTable = _BwmCurCfgContractTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2)
)
if mibBuilder.loadTexts:
    bwmCurCfgContractTable.setStatus("mandatory")
_BwmCurCfgContractTableEntry_Object = MibTableRow
bwmCurCfgContractTableEntry = _BwmCurCfgContractTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1)
)
bwmCurCfgContractTableEntry.setIndexNames(
    (0, "ALTEON-TS-BWM-MIB", "bwmCurCfgContractIndx"),
)
if mibBuilder.loadTexts:
    bwmCurCfgContractTableEntry.setStatus("mandatory")
_BwmCurCfgContractIndx_Type = Integer32
_BwmCurCfgContractIndx_Object = MibTableColumn
bwmCurCfgContractIndx = _BwmCurCfgContractIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 1),
    _BwmCurCfgContractIndx_Type()
)
bwmCurCfgContractIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractIndx.setStatus("mandatory")


class _BwmCurCfgContractName_Type(DisplayString):
    """Custom type bwmCurCfgContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BwmCurCfgContractName_Type.__name__ = "DisplayString"
_BwmCurCfgContractName_Object = MibTableColumn
bwmCurCfgContractName = _BwmCurCfgContractName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 2),
    _BwmCurCfgContractName_Type()
)
bwmCurCfgContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractName.setStatus("mandatory")


class _BwmCurCfgContractState_Type(Integer32):
    """Custom type bwmCurCfgContractState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgContractState_Type.__name__ = "Integer32"
_BwmCurCfgContractState_Object = MibTableColumn
bwmCurCfgContractState = _BwmCurCfgContractState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 3),
    _BwmCurCfgContractState_Type()
)
bwmCurCfgContractState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractState.setStatus("mandatory")


class _BwmCurCfgContractPolicy_Type(Integer32):
    """Custom type bwmCurCfgContractPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BwmCurCfgContractPolicy_Type.__name__ = "Integer32"
_BwmCurCfgContractPolicy_Object = MibTableColumn
bwmCurCfgContractPolicy = _BwmCurCfgContractPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 4),
    _BwmCurCfgContractPolicy_Type()
)
bwmCurCfgContractPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractPolicy.setStatus("mandatory")


class _BwmCurCfgContractPrec_Type(Integer32):
    """Custom type bwmCurCfgContractPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwmCurCfgContractPrec_Type.__name__ = "Integer32"
_BwmCurCfgContractPrec_Object = MibTableColumn
bwmCurCfgContractPrec = _BwmCurCfgContractPrec_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 5),
    _BwmCurCfgContractPrec_Type()
)
bwmCurCfgContractPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractPrec.setStatus("mandatory")


class _BwmCurCfgContractUseTos_Type(Integer32):
    """Custom type bwmCurCfgContractUseTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgContractUseTos_Type.__name__ = "Integer32"
_BwmCurCfgContractUseTos_Object = MibTableColumn
bwmCurCfgContractUseTos = _BwmCurCfgContractUseTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 6),
    _BwmCurCfgContractUseTos_Type()
)
bwmCurCfgContractUseTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractUseTos.setStatus("mandatory")


class _BwmCurCfgContractHistory_Type(Integer32):
    """Custom type bwmCurCfgContractHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgContractHistory_Type.__name__ = "Integer32"
_BwmCurCfgContractHistory_Object = MibTableColumn
bwmCurCfgContractHistory = _BwmCurCfgContractHistory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 2, 1, 7),
    _BwmCurCfgContractHistory_Type()
)
bwmCurCfgContractHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractHistory.setStatus("mandatory")
_BwmNewCfgContractTable_Object = MibTable
bwmNewCfgContractTable = _BwmNewCfgContractTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3)
)
if mibBuilder.loadTexts:
    bwmNewCfgContractTable.setStatus("mandatory")
_BwmNewCfgContractTableEntry_Object = MibTableRow
bwmNewCfgContractTableEntry = _BwmNewCfgContractTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1)
)
bwmNewCfgContractTableEntry.setIndexNames(
    (0, "ALTEON-TS-BWM-MIB", "bwmNewCfgContractIndx"),
)
if mibBuilder.loadTexts:
    bwmNewCfgContractTableEntry.setStatus("mandatory")
_BwmNewCfgContractIndx_Type = Integer32
_BwmNewCfgContractIndx_Object = MibTableColumn
bwmNewCfgContractIndx = _BwmNewCfgContractIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 1),
    _BwmNewCfgContractIndx_Type()
)
bwmNewCfgContractIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContractIndx.setStatus("mandatory")


class _BwmNewCfgContractName_Type(DisplayString):
    """Custom type bwmNewCfgContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BwmNewCfgContractName_Type.__name__ = "DisplayString"
_BwmNewCfgContractName_Object = MibTableColumn
bwmNewCfgContractName = _BwmNewCfgContractName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 2),
    _BwmNewCfgContractName_Type()
)
bwmNewCfgContractName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractName.setStatus("mandatory")


class _BwmNewCfgContractState_Type(Integer32):
    """Custom type bwmNewCfgContractState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgContractState_Type.__name__ = "Integer32"
_BwmNewCfgContractState_Object = MibTableColumn
bwmNewCfgContractState = _BwmNewCfgContractState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 3),
    _BwmNewCfgContractState_Type()
)
bwmNewCfgContractState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractState.setStatus("mandatory")


class _BwmNewCfgContractPolicy_Type(Integer32):
    """Custom type bwmNewCfgContractPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BwmNewCfgContractPolicy_Type.__name__ = "Integer32"
_BwmNewCfgContractPolicy_Object = MibTableColumn
bwmNewCfgContractPolicy = _BwmNewCfgContractPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 4),
    _BwmNewCfgContractPolicy_Type()
)
bwmNewCfgContractPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractPolicy.setStatus("mandatory")


class _BwmNewCfgContractDelete_Type(Integer32):
    """Custom type bwmNewCfgContractDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_BwmNewCfgContractDelete_Type.__name__ = "Integer32"
_BwmNewCfgContractDelete_Object = MibTableColumn
bwmNewCfgContractDelete = _BwmNewCfgContractDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 5),
    _BwmNewCfgContractDelete_Type()
)
bwmNewCfgContractDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractDelete.setStatus("mandatory")


class _BwmNewCfgContractPrec_Type(Integer32):
    """Custom type bwmNewCfgContractPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwmNewCfgContractPrec_Type.__name__ = "Integer32"
_BwmNewCfgContractPrec_Object = MibTableColumn
bwmNewCfgContractPrec = _BwmNewCfgContractPrec_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 6),
    _BwmNewCfgContractPrec_Type()
)
bwmNewCfgContractPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractPrec.setStatus("mandatory")


class _BwmNewCfgContractUseTos_Type(Integer32):
    """Custom type bwmNewCfgContractUseTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgContractUseTos_Type.__name__ = "Integer32"
_BwmNewCfgContractUseTos_Object = MibTableColumn
bwmNewCfgContractUseTos = _BwmNewCfgContractUseTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 7),
    _BwmNewCfgContractUseTos_Type()
)
bwmNewCfgContractUseTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractUseTos.setStatus("mandatory")


class _BwmNewCfgContractHistory_Type(Integer32):
    """Custom type bwmNewCfgContractHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgContractHistory_Type.__name__ = "Integer32"
_BwmNewCfgContractHistory_Object = MibTableColumn
bwmNewCfgContractHistory = _BwmNewCfgContractHistory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 17, 3, 3, 1, 8),
    _BwmNewCfgContractHistory_Type()
)
bwmNewCfgContractHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgContractHistory.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-TS-BWM-MIB",
    **{"bwmStats": bwmStats,
       "bwmStatTcTable": bwmStatTcTable,
       "bwmStatTcEntry": bwmStatTcEntry,
       "bwmStatTcContractIndex": bwmStatTcContractIndex,
       "bwmStatTcName": bwmStatTcName,
       "bwmStatTcOutoct": bwmStatTcOutoct,
       "bwmStatTcOutdisoct": bwmStatTcOutdisoct,
       "bwmStatTcBufferUsed": bwmStatTcBufferUsed,
       "bwmStatTcBufferMax": bwmStatTcBufferMax,
       "bwmStatTcrTable": bwmStatTcrTable,
       "bwmStatTcrEntry": bwmStatTcrEntry,
       "bwmStatTcrContractIndex": bwmStatTcrContractIndex,
       "bwmStatTcrName": bwmStatTcrName,
       "bwmStatTcrRate": bwmStatTcrRate,
       "bwmStatTcrOutoct": bwmStatTcrOutoct,
       "bwmStatTcrOutdisoct": bwmStatTcrOutdisoct,
       "bwmStatTcrBufferUsed": bwmStatTcrBufferUsed,
       "bwmStatTcrBufferMax": bwmStatTcrBufferMax,
       "bwmStatSpTcTable": bwmStatSpTcTable,
       "bwmStatSpTcEntry": bwmStatSpTcEntry,
       "bwmStatSpTcPortIndex": bwmStatSpTcPortIndex,
       "bwmStatSpTcContractIndex": bwmStatSpTcContractIndex,
       "bwmStatSpTcName": bwmStatSpTcName,
       "bwmStatSpTcOutoct": bwmStatSpTcOutoct,
       "bwmStatSpTcOutdisoct": bwmStatSpTcOutdisoct,
       "bwmStatSpTcBufferUsed": bwmStatSpTcBufferUsed,
       "bwmStatSpTcBufferMax": bwmStatSpTcBufferMax,
       "bwmStatSpTcrTable": bwmStatSpTcrTable,
       "bwmStatSpTcrEntry": bwmStatSpTcrEntry,
       "bwmStatSpTcrPortIndex": bwmStatSpTcrPortIndex,
       "bwmStatSpTcrContractIndex": bwmStatSpTcrContractIndex,
       "bwmStatSpTcrName": bwmStatSpTcrName,
       "bwmStatSpTcrRate": bwmStatSpTcrRate,
       "bwmStatSpTcrOutoct": bwmStatSpTcrOutoct,
       "bwmStatSpTcrOutdisoct": bwmStatSpTcrOutdisoct,
       "bwmStatSpTcrBufferUsed": bwmStatSpTcrBufferUsed,
       "bwmStatSpTcrBufferMax": bwmStatSpTcrBufferMax,
       "bwmOper": bwmOper,
       "bwmOperSendSMTP": bwmOperSendSMTP,
       "bwm": bwm,
       "bwmGeneralConfig": bwmGeneralConfig,
       "bwmCurCfgGenState": bwmCurCfgGenState,
       "bwmNewCfgGenState": bwmNewCfgGenState,
       "bwmCurCfgGenEnforcePolicy": bwmCurCfgGenEnforcePolicy,
       "bwmNewCfgGenEnforcePolicy": bwmNewCfgGenEnforcePolicy,
       "bwmCurCfgGenSmtpUser": bwmCurCfgGenSmtpUser,
       "bwmNewCfgGenSmtpUser": bwmNewCfgGenSmtpUser,
       "bwmPolicyConfig": bwmPolicyConfig,
       "bwmPolicyTableMaxEnt": bwmPolicyTableMaxEnt,
       "bwmCurCfgPolicyTable": bwmCurCfgPolicyTable,
       "bwmCurCfgPolicyTableEntry": bwmCurCfgPolicyTableEntry,
       "bwmCurCfgPolicyIndx": bwmCurCfgPolicyIndx,
       "bwmCurCfgPolicyTosIn": bwmCurCfgPolicyTosIn,
       "bwmCurCfgPolicyTosOut": bwmCurCfgPolicyTosOut,
       "bwmCurCfgPolicyHard": bwmCurCfgPolicyHard,
       "bwmCurCfgPolicySoft": bwmCurCfgPolicySoft,
       "bwmCurCfgPolicyResv": bwmCurCfgPolicyResv,
       "bwmCurCfgPolicyBuffer": bwmCurCfgPolicyBuffer,
       "bwmNewCfgPolicyTable": bwmNewCfgPolicyTable,
       "bwmNewCfgPolicyTableEntry": bwmNewCfgPolicyTableEntry,
       "bwmNewCfgPolicyIndx": bwmNewCfgPolicyIndx,
       "bwmNewCfgPolicyTosIn": bwmNewCfgPolicyTosIn,
       "bwmNewCfgPolicyTosOut": bwmNewCfgPolicyTosOut,
       "bwmNewCfgPolicyHard": bwmNewCfgPolicyHard,
       "bwmNewCfgPolicySoft": bwmNewCfgPolicySoft,
       "bwmNewCfgPolicyResv": bwmNewCfgPolicyResv,
       "bwmNewCfgPolicyBuffer": bwmNewCfgPolicyBuffer,
       "bwmNewCfgPolicyDelete": bwmNewCfgPolicyDelete,
       "bwmContractConfig": bwmContractConfig,
       "bwmContractTableMaxEnt": bwmContractTableMaxEnt,
       "bwmCurCfgContractTable": bwmCurCfgContractTable,
       "bwmCurCfgContractTableEntry": bwmCurCfgContractTableEntry,
       "bwmCurCfgContractIndx": bwmCurCfgContractIndx,
       "bwmCurCfgContractName": bwmCurCfgContractName,
       "bwmCurCfgContractState": bwmCurCfgContractState,
       "bwmCurCfgContractPolicy": bwmCurCfgContractPolicy,
       "bwmCurCfgContractPrec": bwmCurCfgContractPrec,
       "bwmCurCfgContractUseTos": bwmCurCfgContractUseTos,
       "bwmCurCfgContractHistory": bwmCurCfgContractHistory,
       "bwmNewCfgContractTable": bwmNewCfgContractTable,
       "bwmNewCfgContractTableEntry": bwmNewCfgContractTableEntry,
       "bwmNewCfgContractIndx": bwmNewCfgContractIndx,
       "bwmNewCfgContractName": bwmNewCfgContractName,
       "bwmNewCfgContractState": bwmNewCfgContractState,
       "bwmNewCfgContractPolicy": bwmNewCfgContractPolicy,
       "bwmNewCfgContractDelete": bwmNewCfgContractDelete,
       "bwmNewCfgContractPrec": bwmNewCfgContractPrec,
       "bwmNewCfgContractUseTos": bwmNewCfgContractUseTos,
       "bwmNewCfgContractHistory": bwmNewCfgContractHistory}
)
