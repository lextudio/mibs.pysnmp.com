# SNMP MIB module (FCTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FCTR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:26 2024
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



class RequestedFlowControlMode(Integer32):
    """Custom type RequestedFlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 1),
          ("enabled", 2))
    )





class GrantedFlowControlMode(Integer32):
    """Custom type GrantedFlowControlMode based on Integer32"""
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
        *(("backPressure", 3),
          ("disabled", 1),
          ("flowControl", 2),
          ("other", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbFctr_ObjectIdentity = ObjectIdentity
nbFctr = _NbFctr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2)
)
_NbFctrInfo_ObjectIdentity = ObjectIdentity
nbFctrInfo = _NbFctrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1)
)


class _NbFctrMgmtType_Type(Integer32):
    """Custom type nbFctrMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonControl", 1),
          ("perDeviceOnly", 2),
          ("perPort", 3))
    )


_NbFctrMgmtType_Type.__name__ = "Integer32"
_NbFctrMgmtType_Object = MibScalar
nbFctrMgmtType = _NbFctrMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 1),
    _NbFctrMgmtType_Type()
)
nbFctrMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbFctrMgmtType.setStatus("mandatory")
_NbFctrGlbReqRun_Type = RequestedFlowControlMode
_NbFctrGlbReqRun_Object = MibScalar
nbFctrGlbReqRun = _NbFctrGlbReqRun_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 2),
    _NbFctrGlbReqRun_Type()
)
nbFctrGlbReqRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbFctrGlbReqRun.setStatus("mandatory")
_NbFctrGlbGrntdRun_Type = GrantedFlowControlMode
_NbFctrGlbGrntdRun_Object = MibScalar
nbFctrGlbGrntdRun = _NbFctrGlbGrntdRun_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 3),
    _NbFctrGlbGrntdRun_Type()
)
nbFctrGlbGrntdRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbFctrGlbGrntdRun.setStatus("mandatory")
_NbFctrGlbReqPerm_Type = RequestedFlowControlMode
_NbFctrGlbReqPerm_Object = MibScalar
nbFctrGlbReqPerm = _NbFctrGlbReqPerm_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 4),
    _NbFctrGlbReqPerm_Type()
)
nbFctrGlbReqPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbFctrGlbReqPerm.setStatus("mandatory")
_NbFctrPortsTable_Object = MibTable
nbFctrPortsTable = _NbFctrPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2)
)
if mibBuilder.loadTexts:
    nbFctrPortsTable.setStatus("mandatory")
_NbFctrPortEntry_Object = MibTableRow
nbFctrPortEntry = _NbFctrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1)
)
nbFctrPortEntry.setIndexNames(
    (0, "FCTR-MIB", "nbFctrPort"),
)
if mibBuilder.loadTexts:
    nbFctrPortEntry.setStatus("mandatory")


class _NbFctrPort_Type(Integer32):
    """Custom type nbFctrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbFctrPort_Type.__name__ = "Integer32"
_NbFctrPort_Object = MibTableColumn
nbFctrPort = _NbFctrPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 1),
    _NbFctrPort_Type()
)
nbFctrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbFctrPort.setStatus("mandatory")
_NbFctrPortRunReqMode_Type = RequestedFlowControlMode
_NbFctrPortRunReqMode_Object = MibTableColumn
nbFctrPortRunReqMode = _NbFctrPortRunReqMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 2),
    _NbFctrPortRunReqMode_Type()
)
nbFctrPortRunReqMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbFctrPortRunReqMode.setStatus("mandatory")
_NbFctrPortRunGrntd_Type = GrantedFlowControlMode
_NbFctrPortRunGrntd_Object = MibTableColumn
nbFctrPortRunGrntd = _NbFctrPortRunGrntd_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 3),
    _NbFctrPortRunGrntd_Type()
)
nbFctrPortRunGrntd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbFctrPortRunGrntd.setStatus("mandatory")
_NbFctrPortPermReqMode_Type = RequestedFlowControlMode
_NbFctrPortPermReqMode_Object = MibTableColumn
nbFctrPortPermReqMode = _NbFctrPortPermReqMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 4),
    _NbFctrPortPermReqMode_Type()
)
nbFctrPortPermReqMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbFctrPortPermReqMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FCTR-MIB",
    **{"RequestedFlowControlMode": RequestedFlowControlMode,
       "GrantedFlowControlMode": GrantedFlowControlMode,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbFctr": nbFctr,
       "nbFctrInfo": nbFctrInfo,
       "nbFctrMgmtType": nbFctrMgmtType,
       "nbFctrGlbReqRun": nbFctrGlbReqRun,
       "nbFctrGlbGrntdRun": nbFctrGlbGrntdRun,
       "nbFctrGlbReqPerm": nbFctrGlbReqPerm,
       "nbFctrPortsTable": nbFctrPortsTable,
       "nbFctrPortEntry": nbFctrPortEntry,
       "nbFctrPort": nbFctrPort,
       "nbFctrPortRunReqMode": nbFctrPortRunReqMode,
       "nbFctrPortRunGrntd": nbFctrPortRunGrntd,
       "nbFctrPortPermReqMode": nbFctrPortPermReqMode}
)
