# SNMP MIB module (APPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:30 2024
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

(snanauMIB,) = mibBuilder.importSymbols(
    "SNA-NAU-MIB",
    "snanauMIB")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 InstancePointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "InstancePointer",
    "TextualConvention")


# MODULE-IDENTITY

appcMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnaSenseData(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_AppcObjects_ObjectIdentity = ObjectIdentity
appcObjects = _AppcObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1)
)
_AppcGlobal_ObjectIdentity = ObjectIdentity
appcGlobal = _AppcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1)
)
_AppcCntrlAdminGroup_ObjectIdentity = ObjectIdentity
appcCntrlAdminGroup = _AppcCntrlAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 1)
)


class _AppcCntrlAdminStat_Type(Integer32):
    """Custom type appcCntrlAdminStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AppcCntrlAdminStat_Type.__name__ = "Integer32"
_AppcCntrlAdminStat_Object = MibScalar
appcCntrlAdminStat = _AppcCntrlAdminStat_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 1, 1),
    _AppcCntrlAdminStat_Type()
)
appcCntrlAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCntrlAdminStat.setStatus("current")


class _AppcCntrlAdminRscv_Type(Integer32):
    """Custom type appcCntrlAdminRscv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AppcCntrlAdminRscv_Type.__name__ = "Integer32"
_AppcCntrlAdminRscv_Object = MibScalar
appcCntrlAdminRscv = _AppcCntrlAdminRscv_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 1, 2),
    _AppcCntrlAdminRscv_Type()
)
appcCntrlAdminRscv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCntrlAdminRscv.setStatus("current")


class _AppcCntrlAdminTrace_Type(Integer32):
    """Custom type appcCntrlAdminTrace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AppcCntrlAdminTrace_Type.__name__ = "Integer32"
_AppcCntrlAdminTrace_Object = MibScalar
appcCntrlAdminTrace = _AppcCntrlAdminTrace_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 1, 3),
    _AppcCntrlAdminTrace_Type()
)
appcCntrlAdminTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCntrlAdminTrace.setStatus("current")


class _AppcCntrlAdminTraceParm_Type(DisplayString):
    """Custom type appcCntrlAdminTraceParm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AppcCntrlAdminTraceParm_Type.__name__ = "DisplayString"
_AppcCntrlAdminTraceParm_Object = MibScalar
appcCntrlAdminTraceParm = _AppcCntrlAdminTraceParm_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 1, 4),
    _AppcCntrlAdminTraceParm_Type()
)
appcCntrlAdminTraceParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCntrlAdminTraceParm.setStatus("current")
_AppcCntrlOperGroup_ObjectIdentity = ObjectIdentity
appcCntrlOperGroup = _AppcCntrlOperGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 2)
)


class _AppcCntrlOperStat_Type(Integer32):
    """Custom type appcCntrlOperStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AppcCntrlOperStat_Type.__name__ = "Integer32"
_AppcCntrlOperStat_Object = MibScalar
appcCntrlOperStat = _AppcCntrlOperStat_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 2, 1),
    _AppcCntrlOperStat_Type()
)
appcCntrlOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCntrlOperStat.setStatus("current")
_AppcCntrlOperStatTime_Type = TimeTicks
_AppcCntrlOperStatTime_Object = MibScalar
appcCntrlOperStatTime = _AppcCntrlOperStatTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 2, 2),
    _AppcCntrlOperStatTime_Type()
)
appcCntrlOperStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCntrlOperStatTime.setStatus("current")


class _AppcCntrlOperRscv_Type(Integer32):
    """Custom type appcCntrlOperRscv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AppcCntrlOperRscv_Type.__name__ = "Integer32"
_AppcCntrlOperRscv_Object = MibScalar
appcCntrlOperRscv = _AppcCntrlOperRscv_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 2, 3),
    _AppcCntrlOperRscv_Type()
)
appcCntrlOperRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCntrlOperRscv.setStatus("current")
_AppcCntrlOperRscvTime_Type = TimeTicks
_AppcCntrlOperRscvTime_Object = MibScalar
appcCntrlOperRscvTime = _AppcCntrlOperRscvTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 2, 4),
    _AppcCntrlOperRscvTime_Type()
)
appcCntrlOperRscvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCntrlOperRscvTime.setStatus("current")


class _AppcCntrlOperTrace_Type(Integer32):
    """Custom type appcCntrlOperTrace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AppcCntrlOperTrace_Type.__name__ = "Integer32"
_AppcCntrlOperTrace_Object = MibScalar
appcCntrlOperTrace = _AppcCntrlOperTrace_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 2, 5),
    _AppcCntrlOperTrace_Type()
)
appcCntrlOperTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCntrlOperTrace.setStatus("current")
_AppcCntrlOperTraceTime_Type = TimeTicks
_AppcCntrlOperTraceTime_Object = MibScalar
appcCntrlOperTraceTime = _AppcCntrlOperTraceTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 2, 6),
    _AppcCntrlOperTraceTime_Type()
)
appcCntrlOperTraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCntrlOperTraceTime.setStatus("current")


class _AppcCntrlOperTraceParm_Type(DisplayString):
    """Custom type appcCntrlOperTraceParm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AppcCntrlOperTraceParm_Type.__name__ = "DisplayString"
_AppcCntrlOperTraceParm_Object = MibScalar
appcCntrlOperTraceParm = _AppcCntrlOperTraceParm_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 2, 7),
    _AppcCntrlOperTraceParm_Type()
)
appcCntrlOperTraceParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCntrlOperTraceParm.setStatus("current")
_AppcGlobalObjects_ObjectIdentity = ObjectIdentity
appcGlobalObjects = _AppcGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3)
)
_AppcUpTime_Type = TimeTicks
_AppcUpTime_Object = MibScalar
appcUpTime = _AppcUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 1),
    _AppcUpTime_Type()
)
appcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcUpTime.setStatus("current")


class _AppcDefaultModeName_Type(DisplayString):
    """Custom type appcDefaultModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcDefaultModeName_Type.__name__ = "DisplayString"
_AppcDefaultModeName_Object = MibScalar
appcDefaultModeName = _AppcDefaultModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 2),
    _AppcDefaultModeName_Type()
)
appcDefaultModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcDefaultModeName.setStatus("current")


class _AppcDefaultLuName_Type(DisplayString):
    """Custom type appcDefaultLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcDefaultLuName_Type.__name__ = "DisplayString"
_AppcDefaultLuName_Object = MibScalar
appcDefaultLuName = _AppcDefaultLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 3),
    _AppcDefaultLuName_Type()
)
appcDefaultLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcDefaultLuName.setStatus("current")


class _AppcDefaultImplInbndPlu_Type(Integer32):
    """Custom type appcDefaultImplInbndPlu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcDefaultImplInbndPlu_Type.__name__ = "Integer32"
_AppcDefaultImplInbndPlu_Object = MibScalar
appcDefaultImplInbndPlu = _AppcDefaultImplInbndPlu_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 4),
    _AppcDefaultImplInbndPlu_Type()
)
appcDefaultImplInbndPlu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcDefaultImplInbndPlu.setStatus("current")
_AppcDefaultMaxMcLlSndSize_Type = Integer32
_AppcDefaultMaxMcLlSndSize_Object = MibScalar
appcDefaultMaxMcLlSndSize = _AppcDefaultMaxMcLlSndSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 5),
    _AppcDefaultMaxMcLlSndSize_Type()
)
appcDefaultMaxMcLlSndSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcDefaultMaxMcLlSndSize.setStatus("current")


class _AppcDefaultFileSpec_Type(DisplayString):
    """Custom type appcDefaultFileSpec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AppcDefaultFileSpec_Type.__name__ = "DisplayString"
_AppcDefaultFileSpec_Object = MibScalar
appcDefaultFileSpec = _AppcDefaultFileSpec_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 6),
    _AppcDefaultFileSpec_Type()
)
appcDefaultFileSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcDefaultFileSpec.setStatus("current")


class _AppcDefaultTpOperation_Type(Integer32):
    """Custom type appcDefaultTpOperation based on Integer32"""
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
        *(("nonqueuedAmStarted", 5),
          ("other", 1),
          ("queuedAmStarted", 4),
          ("queuedOperatorPreloaded", 3),
          ("queuedOperatorStarted", 2))
    )


_AppcDefaultTpOperation_Type.__name__ = "Integer32"
_AppcDefaultTpOperation_Object = MibScalar
appcDefaultTpOperation = _AppcDefaultTpOperation_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 7),
    _AppcDefaultTpOperation_Type()
)
appcDefaultTpOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcDefaultTpOperation.setStatus("current")


class _AppcDefaultTpConvSecRqd_Type(Integer32):
    """Custom type appcDefaultTpConvSecRqd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcDefaultTpConvSecRqd_Type.__name__ = "Integer32"
_AppcDefaultTpConvSecRqd_Object = MibScalar
appcDefaultTpConvSecRqd = _AppcDefaultTpConvSecRqd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 8),
    _AppcDefaultTpConvSecRqd_Type()
)
appcDefaultTpConvSecRqd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcDefaultTpConvSecRqd.setStatus("current")


class _AppcLocalCpName_Type(DisplayString):
    """Custom type appcLocalCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppcLocalCpName_Type.__name__ = "DisplayString"
_AppcLocalCpName_Object = MibScalar
appcLocalCpName = _AppcLocalCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 9),
    _AppcLocalCpName_Type()
)
appcLocalCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLocalCpName.setStatus("current")
_AppcActiveSessions_Type = Gauge32
_AppcActiveSessions_Object = MibScalar
appcActiveSessions = _AppcActiveSessions_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 10),
    _AppcActiveSessions_Type()
)
appcActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveSessions.setStatus("current")
_AppcActiveHprSessions_Type = Gauge32
_AppcActiveHprSessions_Object = MibScalar
appcActiveHprSessions = _AppcActiveHprSessions_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 3, 11),
    _AppcActiveHprSessions_Type()
)
appcActiveHprSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveHprSessions.setStatus("current")
_AppcCnosControl_ObjectIdentity = ObjectIdentity
appcCnosControl = _AppcCnosControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4)
)


class _AppcCnosCommand_Type(Integer32):
    """Custom type appcCnosCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("changeSesslimit", 2),
          ("initSesslimit", 1),
          ("resetSesslimit", 3))
    )


_AppcCnosCommand_Type.__name__ = "Integer32"
_AppcCnosCommand_Object = MibScalar
appcCnosCommand = _AppcCnosCommand_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 1),
    _AppcCnosCommand_Type()
)
appcCnosCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosCommand.setStatus("current")


class _AppcCnosMaxSessLimit_Type(Integer32):
    """Custom type appcCnosMaxSessLimit based on Integer32"""
    defaultValue = 0


_AppcCnosMaxSessLimit_Object = MibScalar
appcCnosMaxSessLimit = _AppcCnosMaxSessLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 2),
    _AppcCnosMaxSessLimit_Type()
)
appcCnosMaxSessLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosMaxSessLimit.setStatus("current")


class _AppcCnosMinCwinLimit_Type(Integer32):
    """Custom type appcCnosMinCwinLimit based on Integer32"""
    defaultValue = 0


_AppcCnosMinCwinLimit_Object = MibScalar
appcCnosMinCwinLimit = _AppcCnosMinCwinLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 3),
    _AppcCnosMinCwinLimit_Type()
)
appcCnosMinCwinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosMinCwinLimit.setStatus("current")


class _AppcCnosMinClosLimit_Type(Integer32):
    """Custom type appcCnosMinClosLimit based on Integer32"""
    defaultValue = 0


_AppcCnosMinClosLimit_Object = MibScalar
appcCnosMinClosLimit = _AppcCnosMinClosLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 4),
    _AppcCnosMinClosLimit_Type()
)
appcCnosMinClosLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosMinClosLimit.setStatus("current")


class _AppcCnosDrainSelf_Type(Integer32):
    """Custom type appcCnosDrainSelf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcCnosDrainSelf_Type.__name__ = "Integer32"
_AppcCnosDrainSelf_Object = MibScalar
appcCnosDrainSelf = _AppcCnosDrainSelf_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 5),
    _AppcCnosDrainSelf_Type()
)
appcCnosDrainSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosDrainSelf.setStatus("current")


class _AppcCnosDrainPart_Type(Integer32):
    """Custom type appcCnosDrainPart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcCnosDrainPart_Type.__name__ = "Integer32"
_AppcCnosDrainPart_Object = MibScalar
appcCnosDrainPart = _AppcCnosDrainPart_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 6),
    _AppcCnosDrainPart_Type()
)
appcCnosDrainPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosDrainPart.setStatus("current")


class _AppcCnosResponsible_Type(Integer32):
    """Custom type appcCnosResponsible based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("target", 2))
    )


_AppcCnosResponsible_Type.__name__ = "Integer32"
_AppcCnosResponsible_Object = MibScalar
appcCnosResponsible = _AppcCnosResponsible_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 7),
    _AppcCnosResponsible_Type()
)
appcCnosResponsible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosResponsible.setStatus("current")


class _AppcCnosForce_Type(Integer32):
    """Custom type appcCnosForce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcCnosForce_Type.__name__ = "Integer32"
_AppcCnosForce_Object = MibScalar
appcCnosForce = _AppcCnosForce_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 8),
    _AppcCnosForce_Type()
)
appcCnosForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosForce.setStatus("current")


class _AppcCnosTargetLocLuName_Type(DisplayString):
    """Custom type appcCnosTargetLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcCnosTargetLocLuName_Type.__name__ = "DisplayString"
_AppcCnosTargetLocLuName_Object = MibScalar
appcCnosTargetLocLuName = _AppcCnosTargetLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 9),
    _AppcCnosTargetLocLuName_Type()
)
appcCnosTargetLocLuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosTargetLocLuName.setStatus("current")


class _AppcCnosTargetParLuName_Type(DisplayString):
    """Custom type appcCnosTargetParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcCnosTargetParLuName_Type.__name__ = "DisplayString"
_AppcCnosTargetParLuName_Object = MibScalar
appcCnosTargetParLuName = _AppcCnosTargetParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 10),
    _AppcCnosTargetParLuName_Type()
)
appcCnosTargetParLuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosTargetParLuName.setStatus("current")


class _AppcCnosTargetModeName_Type(DisplayString):
    """Custom type appcCnosTargetModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcCnosTargetModeName_Type.__name__ = "DisplayString"
_AppcCnosTargetModeName_Object = MibScalar
appcCnosTargetModeName = _AppcCnosTargetModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 1, 4, 11),
    _AppcCnosTargetModeName_Type()
)
appcCnosTargetModeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcCnosTargetModeName.setStatus("current")
_AppcLu_ObjectIdentity = ObjectIdentity
appcLu = _AppcLu_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2)
)
_AppcLluAdminTable_Object = MibTable
appcLluAdminTable = _AppcLluAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    appcLluAdminTable.setStatus("current")
_AppcLluAdminEntry_Object = MibTableRow
appcLluAdminEntry = _AppcLluAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1)
)
appcLluAdminEntry.setIndexNames(
    (0, "APPC-MIB", "appcLluAdminName"),
)
if mibBuilder.loadTexts:
    appcLluAdminEntry.setStatus("current")


class _AppcLluAdminName_Type(DisplayString):
    """Custom type appcLluAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcLluAdminName_Type.__name__ = "DisplayString"
_AppcLluAdminName_Object = MibTableColumn
appcLluAdminName = _AppcLluAdminName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 1),
    _AppcLluAdminName_Type()
)
appcLluAdminName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcLluAdminName.setStatus("current")


class _AppcLluAdminDepType_Type(Integer32):
    """Custom type appcLluAdminDepType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dependent", 1),
          ("independent", 2))
    )


_AppcLluAdminDepType_Type.__name__ = "Integer32"
_AppcLluAdminDepType_Object = MibTableColumn
appcLluAdminDepType = _AppcLluAdminDepType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 2),
    _AppcLluAdminDepType_Type()
)
appcLluAdminDepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminDepType.setStatus("current")


class _AppcLluAdminLocalAddress_Type(OctetString):
    """Custom type appcLluAdminLocalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppcLluAdminLocalAddress_Type.__name__ = "OctetString"
_AppcLluAdminLocalAddress_Object = MibTableColumn
appcLluAdminLocalAddress = _AppcLluAdminLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 3),
    _AppcLluAdminLocalAddress_Type()
)
appcLluAdminLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminLocalAddress.setStatus("current")
_AppcLluAdminSessLimit_Type = Integer32
_AppcLluAdminSessLimit_Object = MibTableColumn
appcLluAdminSessLimit = _AppcLluAdminSessLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 4),
    _AppcLluAdminSessLimit_Type()
)
appcLluAdminSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminSessLimit.setStatus("current")


class _AppcLluAdminBindRspMayQ_Type(Integer32):
    """Custom type appcLluAdminBindRspMayQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcLluAdminBindRspMayQ_Type.__name__ = "Integer32"
_AppcLluAdminBindRspMayQ_Object = MibTableColumn
appcLluAdminBindRspMayQ = _AppcLluAdminBindRspMayQ_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 5),
    _AppcLluAdminBindRspMayQ_Type()
)
appcLluAdminBindRspMayQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminBindRspMayQ.setStatus("current")


class _AppcLluAdminCompression_Type(Integer32):
    """Custom type appcLluAdminCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("prohibited", 1),
          ("required", 2))
    )


_AppcLluAdminCompression_Type.__name__ = "Integer32"
_AppcLluAdminCompression_Object = MibTableColumn
appcLluAdminCompression = _AppcLluAdminCompression_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 6),
    _AppcLluAdminCompression_Type()
)
appcLluAdminCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminCompression.setStatus("current")


class _AppcLluAdminInBoundCompLevel_Type(Integer32):
    """Custom type appcLluAdminInBoundCompLevel based on Integer32"""
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
        *(("lz10", 4),
          ("lz12", 5),
          ("lz9", 3),
          ("none", 1),
          ("rle", 2))
    )


_AppcLluAdminInBoundCompLevel_Type.__name__ = "Integer32"
_AppcLluAdminInBoundCompLevel_Object = MibTableColumn
appcLluAdminInBoundCompLevel = _AppcLluAdminInBoundCompLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 7),
    _AppcLluAdminInBoundCompLevel_Type()
)
appcLluAdminInBoundCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminInBoundCompLevel.setStatus("current")


class _AppcLluAdminOutBoundCompLevel_Type(Integer32):
    """Custom type appcLluAdminOutBoundCompLevel based on Integer32"""
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
        *(("lz10", 4),
          ("lz12", 5),
          ("lz9", 3),
          ("none", 1),
          ("rle", 2))
    )


_AppcLluAdminOutBoundCompLevel_Type.__name__ = "Integer32"
_AppcLluAdminOutBoundCompLevel_Object = MibTableColumn
appcLluAdminOutBoundCompLevel = _AppcLluAdminOutBoundCompLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 8),
    _AppcLluAdminOutBoundCompLevel_Type()
)
appcLluAdminOutBoundCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminOutBoundCompLevel.setStatus("current")


class _AppcLluAdminCompRleBeforeLZ_Type(Integer32):
    """Custom type appcLluAdminCompRleBeforeLZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcLluAdminCompRleBeforeLZ_Type.__name__ = "Integer32"
_AppcLluAdminCompRleBeforeLZ_Object = MibTableColumn
appcLluAdminCompRleBeforeLZ = _AppcLluAdminCompRleBeforeLZ_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 9),
    _AppcLluAdminCompRleBeforeLZ_Type()
)
appcLluAdminCompRleBeforeLZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminCompRleBeforeLZ.setStatus("current")


class _AppcLluAdminAlias_Type(DisplayString):
    """Custom type appcLluAdminAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcLluAdminAlias_Type.__name__ = "DisplayString"
_AppcLluAdminAlias_Object = MibTableColumn
appcLluAdminAlias = _AppcLluAdminAlias_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 1, 1, 10),
    _AppcLluAdminAlias_Type()
)
appcLluAdminAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluAdminAlias.setStatus("current")
_AppcLluOperTable_Object = MibTable
appcLluOperTable = _AppcLluOperTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    appcLluOperTable.setStatus("current")
_AppcLluOperEntry_Object = MibTableRow
appcLluOperEntry = _AppcLluOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1)
)
appcLluOperEntry.setIndexNames(
    (0, "APPC-MIB", "appcLluOperName"),
)
if mibBuilder.loadTexts:
    appcLluOperEntry.setStatus("current")


class _AppcLluOperName_Type(DisplayString):
    """Custom type appcLluOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcLluOperName_Type.__name__ = "DisplayString"
_AppcLluOperName_Object = MibTableColumn
appcLluOperName = _AppcLluOperName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 1),
    _AppcLluOperName_Type()
)
appcLluOperName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcLluOperName.setStatus("current")


class _AppcLluOperDepType_Type(Integer32):
    """Custom type appcLluOperDepType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dependent", 1),
          ("independent", 2))
    )


_AppcLluOperDepType_Type.__name__ = "Integer32"
_AppcLluOperDepType_Object = MibTableColumn
appcLluOperDepType = _AppcLluOperDepType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 2),
    _AppcLluOperDepType_Type()
)
appcLluOperDepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperDepType.setStatus("current")


class _AppcLluOperLocalAddress_Type(OctetString):
    """Custom type appcLluOperLocalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppcLluOperLocalAddress_Type.__name__ = "OctetString"
_AppcLluOperLocalAddress_Object = MibTableColumn
appcLluOperLocalAddress = _AppcLluOperLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 3),
    _AppcLluOperLocalAddress_Type()
)
appcLluOperLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperLocalAddress.setStatus("current")
_AppcLluOperSessLimit_Type = Integer32
_AppcLluOperSessLimit_Object = MibTableColumn
appcLluOperSessLimit = _AppcLluOperSessLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 4),
    _AppcLluOperSessLimit_Type()
)
appcLluOperSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperSessLimit.setStatus("current")


class _AppcLluOperBindRspMayQ_Type(Integer32):
    """Custom type appcLluOperBindRspMayQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcLluOperBindRspMayQ_Type.__name__ = "Integer32"
_AppcLluOperBindRspMayQ_Object = MibTableColumn
appcLluOperBindRspMayQ = _AppcLluOperBindRspMayQ_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 5),
    _AppcLluOperBindRspMayQ_Type()
)
appcLluOperBindRspMayQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperBindRspMayQ.setStatus("current")


class _AppcLluOperCompression_Type(Integer32):
    """Custom type appcLluOperCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("prohibited", 1),
          ("required", 2))
    )


_AppcLluOperCompression_Type.__name__ = "Integer32"
_AppcLluOperCompression_Object = MibTableColumn
appcLluOperCompression = _AppcLluOperCompression_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 6),
    _AppcLluOperCompression_Type()
)
appcLluOperCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperCompression.setStatus("current")


class _AppcLluOperInBoundCompLevel_Type(Integer32):
    """Custom type appcLluOperInBoundCompLevel based on Integer32"""
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
        *(("lz10", 4),
          ("lz12", 5),
          ("lz9", 3),
          ("none", 1),
          ("rle", 2))
    )


_AppcLluOperInBoundCompLevel_Type.__name__ = "Integer32"
_AppcLluOperInBoundCompLevel_Object = MibTableColumn
appcLluOperInBoundCompLevel = _AppcLluOperInBoundCompLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 7),
    _AppcLluOperInBoundCompLevel_Type()
)
appcLluOperInBoundCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperInBoundCompLevel.setStatus("current")


class _AppcLluOperOutBoundCompLevel_Type(Integer32):
    """Custom type appcLluOperOutBoundCompLevel based on Integer32"""
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
        *(("lz10", 4),
          ("lz12", 5),
          ("lz9", 3),
          ("none", 1),
          ("rle", 2))
    )


_AppcLluOperOutBoundCompLevel_Type.__name__ = "Integer32"
_AppcLluOperOutBoundCompLevel_Object = MibTableColumn
appcLluOperOutBoundCompLevel = _AppcLluOperOutBoundCompLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 8),
    _AppcLluOperOutBoundCompLevel_Type()
)
appcLluOperOutBoundCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperOutBoundCompLevel.setStatus("current")


class _AppcLluOperCompRleBeforeLZ_Type(Integer32):
    """Custom type appcLluOperCompRleBeforeLZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcLluOperCompRleBeforeLZ_Type.__name__ = "Integer32"
_AppcLluOperCompRleBeforeLZ_Object = MibTableColumn
appcLluOperCompRleBeforeLZ = _AppcLluOperCompRleBeforeLZ_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 9),
    _AppcLluOperCompRleBeforeLZ_Type()
)
appcLluOperCompRleBeforeLZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperCompRleBeforeLZ.setStatus("current")


class _AppcLluOperAlias_Type(DisplayString):
    """Custom type appcLluOperAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcLluOperAlias_Type.__name__ = "DisplayString"
_AppcLluOperAlias_Object = MibTableColumn
appcLluOperAlias = _AppcLluOperAlias_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 10),
    _AppcLluOperAlias_Type()
)
appcLluOperAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperAlias.setStatus("current")
_AppcLluOperActiveSessions_Type = Gauge32
_AppcLluOperActiveSessions_Object = MibTableColumn
appcLluOperActiveSessions = _AppcLluOperActiveSessions_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 2, 1, 11),
    _AppcLluOperActiveSessions_Type()
)
appcLluOperActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLluOperActiveSessions.setStatus("current")
_AppcLuPairAdminTable_Object = MibTable
appcLuPairAdminTable = _AppcLuPairAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    appcLuPairAdminTable.setStatus("current")
_AppcLuPairAdminEntry_Object = MibTableRow
appcLuPairAdminEntry = _AppcLuPairAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1)
)
appcLuPairAdminEntry.setIndexNames(
    (0, "APPC-MIB", "appcLuPairAdminLocLuName"),
    (0, "APPC-MIB", "appcLuPairAdminParLuName"),
)
if mibBuilder.loadTexts:
    appcLuPairAdminEntry.setStatus("current")


class _AppcLuPairAdminLocLuName_Type(DisplayString):
    """Custom type appcLuPairAdminLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcLuPairAdminLocLuName_Type.__name__ = "DisplayString"
_AppcLuPairAdminLocLuName_Object = MibTableColumn
appcLuPairAdminLocLuName = _AppcLuPairAdminLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1, 1),
    _AppcLuPairAdminLocLuName_Type()
)
appcLuPairAdminLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcLuPairAdminLocLuName.setStatus("current")


class _AppcLuPairAdminParLuName_Type(DisplayString):
    """Custom type appcLuPairAdminParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcLuPairAdminParLuName_Type.__name__ = "DisplayString"
_AppcLuPairAdminParLuName_Object = MibTableColumn
appcLuPairAdminParLuName = _AppcLuPairAdminParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1, 2),
    _AppcLuPairAdminParLuName_Type()
)
appcLuPairAdminParLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcLuPairAdminParLuName.setStatus("current")


class _AppcLuPairAdminParLuAlias_Type(DisplayString):
    """Custom type appcLuPairAdminParLuAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcLuPairAdminParLuAlias_Type.__name__ = "DisplayString"
_AppcLuPairAdminParLuAlias_Object = MibTableColumn
appcLuPairAdminParLuAlias = _AppcLuPairAdminParLuAlias_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1, 3),
    _AppcLuPairAdminParLuAlias_Type()
)
appcLuPairAdminParLuAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairAdminParLuAlias.setStatus("current")
_AppcLuPairAdminSessLimit_Type = Integer32
_AppcLuPairAdminSessLimit_Object = MibTableColumn
appcLuPairAdminSessLimit = _AppcLuPairAdminSessLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1, 4),
    _AppcLuPairAdminSessLimit_Type()
)
appcLuPairAdminSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairAdminSessLimit.setStatus("current")


class _AppcLuPairAdminSessSec_Type(Integer32):
    """Custom type appcLuPairAdminSessSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 2),
          ("notAllowed", 3),
          ("required", 1))
    )


_AppcLuPairAdminSessSec_Type.__name__ = "Integer32"
_AppcLuPairAdminSessSec_Object = MibTableColumn
appcLuPairAdminSessSec = _AppcLuPairAdminSessSec_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1, 5),
    _AppcLuPairAdminSessSec_Type()
)
appcLuPairAdminSessSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairAdminSessSec.setStatus("current")


class _AppcLuPairAdminSecAccept_Type(Integer32):
    """Custom type appcLuPairAdminSecAccept based on Integer32"""
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
        *(("aVandpV", 5),
          ("alreadyVerified", 3),
          ("conversation", 2),
          ("none", 1),
          ("persistentVerification", 4))
    )


_AppcLuPairAdminSecAccept_Type.__name__ = "Integer32"
_AppcLuPairAdminSecAccept_Object = MibTableColumn
appcLuPairAdminSecAccept = _AppcLuPairAdminSecAccept_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1, 6),
    _AppcLuPairAdminSecAccept_Type()
)
appcLuPairAdminSecAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairAdminSecAccept.setStatus("current")
_AppcLuPairAdminLinkObjId_Type = InstancePointer
_AppcLuPairAdminLinkObjId_Object = MibTableColumn
appcLuPairAdminLinkObjId = _AppcLuPairAdminLinkObjId_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1, 7),
    _AppcLuPairAdminLinkObjId_Type()
)
appcLuPairAdminLinkObjId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairAdminLinkObjId.setStatus("current")


class _AppcLuPairAdminParaSessSup_Type(Integer32):
    """Custom type appcLuPairAdminParaSessSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcLuPairAdminParaSessSup_Type.__name__ = "Integer32"
_AppcLuPairAdminParaSessSup_Object = MibTableColumn
appcLuPairAdminParaSessSup = _AppcLuPairAdminParaSessSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 3, 1, 8),
    _AppcLuPairAdminParaSessSup_Type()
)
appcLuPairAdminParaSessSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairAdminParaSessSup.setStatus("current")
_AppcLuPairOperTable_Object = MibTable
appcLuPairOperTable = _AppcLuPairOperTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    appcLuPairOperTable.setStatus("current")
_AppcLuPairOperEntry_Object = MibTableRow
appcLuPairOperEntry = _AppcLuPairOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1)
)
appcLuPairOperEntry.setIndexNames(
    (0, "APPC-MIB", "appcLuPairOperLocLuName"),
    (0, "APPC-MIB", "appcLuPairOperParLuName"),
)
if mibBuilder.loadTexts:
    appcLuPairOperEntry.setStatus("current")


class _AppcLuPairOperLocLuName_Type(DisplayString):
    """Custom type appcLuPairOperLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcLuPairOperLocLuName_Type.__name__ = "DisplayString"
_AppcLuPairOperLocLuName_Object = MibTableColumn
appcLuPairOperLocLuName = _AppcLuPairOperLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 1),
    _AppcLuPairOperLocLuName_Type()
)
appcLuPairOperLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcLuPairOperLocLuName.setStatus("current")


class _AppcLuPairOperParLuName_Type(DisplayString):
    """Custom type appcLuPairOperParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcLuPairOperParLuName_Type.__name__ = "DisplayString"
_AppcLuPairOperParLuName_Object = MibTableColumn
appcLuPairOperParLuName = _AppcLuPairOperParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 2),
    _AppcLuPairOperParLuName_Type()
)
appcLuPairOperParLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcLuPairOperParLuName.setStatus("current")


class _AppcLuPairOperParLuAlias_Type(DisplayString):
    """Custom type appcLuPairOperParLuAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcLuPairOperParLuAlias_Type.__name__ = "DisplayString"
_AppcLuPairOperParLuAlias_Object = MibTableColumn
appcLuPairOperParLuAlias = _AppcLuPairOperParLuAlias_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 3),
    _AppcLuPairOperParLuAlias_Type()
)
appcLuPairOperParLuAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairOperParLuAlias.setStatus("current")
_AppcLuPairOperSessLimit_Type = Integer32
_AppcLuPairOperSessLimit_Object = MibTableColumn
appcLuPairOperSessLimit = _AppcLuPairOperSessLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 4),
    _AppcLuPairOperSessLimit_Type()
)
appcLuPairOperSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairOperSessLimit.setStatus("current")


class _AppcLuPairOperSessSec_Type(Integer32):
    """Custom type appcLuPairOperSessSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 2),
          ("notAllowed", 3),
          ("required", 1))
    )


_AppcLuPairOperSessSec_Type.__name__ = "Integer32"
_AppcLuPairOperSessSec_Object = MibTableColumn
appcLuPairOperSessSec = _AppcLuPairOperSessSec_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 5),
    _AppcLuPairOperSessSec_Type()
)
appcLuPairOperSessSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairOperSessSec.setStatus("current")


class _AppcLuPairOperSecAccept_Type(Integer32):
    """Custom type appcLuPairOperSecAccept based on Integer32"""
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
        *(("aVandpV", 5),
          ("alreadyVerified", 3),
          ("conversation", 2),
          ("none", 1),
          ("persistentVerification", 4))
    )


_AppcLuPairOperSecAccept_Type.__name__ = "Integer32"
_AppcLuPairOperSecAccept_Object = MibTableColumn
appcLuPairOperSecAccept = _AppcLuPairOperSecAccept_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 6),
    _AppcLuPairOperSecAccept_Type()
)
appcLuPairOperSecAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairOperSecAccept.setStatus("current")
_AppcLuPairOperLinkObjId_Type = InstancePointer
_AppcLuPairOperLinkObjId_Object = MibTableColumn
appcLuPairOperLinkObjId = _AppcLuPairOperLinkObjId_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 7),
    _AppcLuPairOperLinkObjId_Type()
)
appcLuPairOperLinkObjId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairOperLinkObjId.setStatus("current")


class _AppcLuPairOperParaSessSup_Type(Integer32):
    """Custom type appcLuPairOperParaSessSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcLuPairOperParaSessSup_Type.__name__ = "Integer32"
_AppcLuPairOperParaSessSup_Object = MibTableColumn
appcLuPairOperParaSessSup = _AppcLuPairOperParaSessSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 8),
    _AppcLuPairOperParaSessSup_Type()
)
appcLuPairOperParaSessSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairOperParaSessSup.setStatus("current")


class _AppcLuPairOperParaSessSupLS_Type(Integer32):
    """Custom type appcLuPairOperParaSessSupLS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcLuPairOperParaSessSupLS_Type.__name__ = "Integer32"
_AppcLuPairOperParaSessSupLS_Object = MibTableColumn
appcLuPairOperParaSessSupLS = _AppcLuPairOperParaSessSupLS_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 9),
    _AppcLuPairOperParaSessSupLS_Type()
)
appcLuPairOperParaSessSupLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairOperParaSessSupLS.setStatus("current")


class _AppcLuPairOperState_Type(Integer32):
    """Custom type appcLuPairOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_AppcLuPairOperState_Type.__name__ = "Integer32"
_AppcLuPairOperState_Object = MibTableColumn
appcLuPairOperState = _AppcLuPairOperState_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 4, 1, 10),
    _AppcLuPairOperState_Type()
)
appcLuPairOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcLuPairOperState.setStatus("current")
_AppcModeAdminTable_Object = MibTable
appcModeAdminTable = _AppcModeAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    appcModeAdminTable.setStatus("current")
_AppcModeAdminEntry_Object = MibTableRow
appcModeAdminEntry = _AppcModeAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1)
)
appcModeAdminEntry.setIndexNames(
    (0, "APPC-MIB", "appcModeAdminLocLuName"),
    (0, "APPC-MIB", "appcModeAdminParLuName"),
    (0, "APPC-MIB", "appcModeAdminModeName"),
)
if mibBuilder.loadTexts:
    appcModeAdminEntry.setStatus("current")


class _AppcModeAdminLocLuName_Type(DisplayString):
    """Custom type appcModeAdminLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcModeAdminLocLuName_Type.__name__ = "DisplayString"
_AppcModeAdminLocLuName_Object = MibTableColumn
appcModeAdminLocLuName = _AppcModeAdminLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 1),
    _AppcModeAdminLocLuName_Type()
)
appcModeAdminLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcModeAdminLocLuName.setStatus("current")


class _AppcModeAdminParLuName_Type(DisplayString):
    """Custom type appcModeAdminParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcModeAdminParLuName_Type.__name__ = "DisplayString"
_AppcModeAdminParLuName_Object = MibTableColumn
appcModeAdminParLuName = _AppcModeAdminParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 2),
    _AppcModeAdminParLuName_Type()
)
appcModeAdminParLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcModeAdminParLuName.setStatus("current")


class _AppcModeAdminModeName_Type(DisplayString):
    """Custom type appcModeAdminModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcModeAdminModeName_Type.__name__ = "DisplayString"
_AppcModeAdminModeName_Object = MibTableColumn
appcModeAdminModeName = _AppcModeAdminModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 3),
    _AppcModeAdminModeName_Type()
)
appcModeAdminModeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcModeAdminModeName.setStatus("current")


class _AppcModeAdminCosName_Type(DisplayString):
    """Custom type appcModeAdminCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcModeAdminCosName_Type.__name__ = "DisplayString"
_AppcModeAdminCosName_Object = MibTableColumn
appcModeAdminCosName = _AppcModeAdminCosName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 4),
    _AppcModeAdminCosName_Type()
)
appcModeAdminCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminCosName.setStatus("current")


class _AppcModeAdminSessEndTpName_Type(DisplayString):
    """Custom type appcModeAdminSessEndTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AppcModeAdminSessEndTpName_Type.__name__ = "DisplayString"
_AppcModeAdminSessEndTpName_Object = MibTableColumn
appcModeAdminSessEndTpName = _AppcModeAdminSessEndTpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 5),
    _AppcModeAdminSessEndTpName_Type()
)
appcModeAdminSessEndTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminSessEndTpName.setStatus("current")
_AppcModeAdminMaxSessLimit_Type = Integer32
_AppcModeAdminMaxSessLimit_Object = MibTableColumn
appcModeAdminMaxSessLimit = _AppcModeAdminMaxSessLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 6),
    _AppcModeAdminMaxSessLimit_Type()
)
appcModeAdminMaxSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminMaxSessLimit.setStatus("current")
_AppcModeAdminMinCwinLimit_Type = Integer32
_AppcModeAdminMinCwinLimit_Object = MibTableColumn
appcModeAdminMinCwinLimit = _AppcModeAdminMinCwinLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 7),
    _AppcModeAdminMinCwinLimit_Type()
)
appcModeAdminMinCwinLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminMinCwinLimit.setStatus("current")
_AppcModeAdminMinClosLimit_Type = Integer32
_AppcModeAdminMinClosLimit_Object = MibTableColumn
appcModeAdminMinClosLimit = _AppcModeAdminMinClosLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 8),
    _AppcModeAdminMinClosLimit_Type()
)
appcModeAdminMinClosLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminMinClosLimit.setStatus("current")
_AppcModeAdminConWinAutoActLmt_Type = Integer32
_AppcModeAdminConWinAutoActLmt_Object = MibTableColumn
appcModeAdminConWinAutoActLmt = _AppcModeAdminConWinAutoActLmt_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 9),
    _AppcModeAdminConWinAutoActLmt_Type()
)
appcModeAdminConWinAutoActLmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminConWinAutoActLmt.setStatus("current")
_AppcModeAdminRecvPacWinSz_Type = Integer32
_AppcModeAdminRecvPacWinSz_Object = MibTableColumn
appcModeAdminRecvPacWinSz = _AppcModeAdminRecvPacWinSz_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 10),
    _AppcModeAdminRecvPacWinSz_Type()
)
appcModeAdminRecvPacWinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminRecvPacWinSz.setStatus("current")
_AppcModeAdminSendPacWinSz_Type = Integer32
_AppcModeAdminSendPacWinSz_Object = MibTableColumn
appcModeAdminSendPacWinSz = _AppcModeAdminSendPacWinSz_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 11),
    _AppcModeAdminSendPacWinSz_Type()
)
appcModeAdminSendPacWinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminSendPacWinSz.setStatus("current")
_AppcModeAdminPrefRecvRuSz_Type = Integer32
_AppcModeAdminPrefRecvRuSz_Object = MibTableColumn
appcModeAdminPrefRecvRuSz = _AppcModeAdminPrefRecvRuSz_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 12),
    _AppcModeAdminPrefRecvRuSz_Type()
)
appcModeAdminPrefRecvRuSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminPrefRecvRuSz.setStatus("current")
_AppcModeAdminPrefSendRuSz_Type = Integer32
_AppcModeAdminPrefSendRuSz_Object = MibTableColumn
appcModeAdminPrefSendRuSz = _AppcModeAdminPrefSendRuSz_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 13),
    _AppcModeAdminPrefSendRuSz_Type()
)
appcModeAdminPrefSendRuSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminPrefSendRuSz.setStatus("current")
_AppcModeAdminRecvRuSzUpBnd_Type = Integer32
_AppcModeAdminRecvRuSzUpBnd_Object = MibTableColumn
appcModeAdminRecvRuSzUpBnd = _AppcModeAdminRecvRuSzUpBnd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 14),
    _AppcModeAdminRecvRuSzUpBnd_Type()
)
appcModeAdminRecvRuSzUpBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminRecvRuSzUpBnd.setStatus("current")
_AppcModeAdminSendRuSzUpBnd_Type = Integer32
_AppcModeAdminSendRuSzUpBnd_Object = MibTableColumn
appcModeAdminSendRuSzUpBnd = _AppcModeAdminSendRuSzUpBnd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 15),
    _AppcModeAdminSendRuSzUpBnd_Type()
)
appcModeAdminSendRuSzUpBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminSendRuSzUpBnd.setStatus("current")
_AppcModeAdminRecvRuSzLoBnd_Type = Integer32
_AppcModeAdminRecvRuSzLoBnd_Object = MibTableColumn
appcModeAdminRecvRuSzLoBnd = _AppcModeAdminRecvRuSzLoBnd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 16),
    _AppcModeAdminRecvRuSzLoBnd_Type()
)
appcModeAdminRecvRuSzLoBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminRecvRuSzLoBnd.setStatus("current")
_AppcModeAdminSendRuSzLoBnd_Type = Integer32
_AppcModeAdminSendRuSzLoBnd_Object = MibTableColumn
appcModeAdminSendRuSzLoBnd = _AppcModeAdminSendRuSzLoBnd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 17),
    _AppcModeAdminSendRuSzLoBnd_Type()
)
appcModeAdminSendRuSzLoBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminSendRuSzLoBnd.setStatus("current")


class _AppcModeAdminSingSessReinit_Type(Integer32):
    """Custom type appcModeAdminSingSessReinit based on Integer32"""
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
        *(("notApplicable", 1),
          ("operatorControlled", 2),
          ("primaryOnly", 3),
          ("primaryOrSecondary", 5),
          ("secondaryOnly", 4))
    )


_AppcModeAdminSingSessReinit_Type.__name__ = "Integer32"
_AppcModeAdminSingSessReinit_Object = MibTableColumn
appcModeAdminSingSessReinit = _AppcModeAdminSingSessReinit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 18),
    _AppcModeAdminSingSessReinit_Type()
)
appcModeAdminSingSessReinit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminSingSessReinit.setStatus("current")


class _AppcModeAdminCompression_Type(Integer32):
    """Custom type appcModeAdminCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("prohibited", 1),
          ("required", 2))
    )


_AppcModeAdminCompression_Type.__name__ = "Integer32"
_AppcModeAdminCompression_Object = MibTableColumn
appcModeAdminCompression = _AppcModeAdminCompression_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 19),
    _AppcModeAdminCompression_Type()
)
appcModeAdminCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminCompression.setStatus("current")


class _AppcModeAdminInBoundCompLevel_Type(Integer32):
    """Custom type appcModeAdminInBoundCompLevel based on Integer32"""
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
        *(("lz10", 4),
          ("lz12", 5),
          ("lz9", 3),
          ("none", 1),
          ("rle", 2))
    )


_AppcModeAdminInBoundCompLevel_Type.__name__ = "Integer32"
_AppcModeAdminInBoundCompLevel_Object = MibTableColumn
appcModeAdminInBoundCompLevel = _AppcModeAdminInBoundCompLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 20),
    _AppcModeAdminInBoundCompLevel_Type()
)
appcModeAdminInBoundCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminInBoundCompLevel.setStatus("current")


class _AppcModeAdminOutBoundCompLevel_Type(Integer32):
    """Custom type appcModeAdminOutBoundCompLevel based on Integer32"""
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
        *(("lz10", 4),
          ("lz12", 5),
          ("lz9", 3),
          ("none", 1),
          ("rle", 2))
    )


_AppcModeAdminOutBoundCompLevel_Type.__name__ = "Integer32"
_AppcModeAdminOutBoundCompLevel_Object = MibTableColumn
appcModeAdminOutBoundCompLevel = _AppcModeAdminOutBoundCompLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 21),
    _AppcModeAdminOutBoundCompLevel_Type()
)
appcModeAdminOutBoundCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminOutBoundCompLevel.setStatus("current")


class _AppcModeAdminCompRleBeforeLZ_Type(Integer32):
    """Custom type appcModeAdminCompRleBeforeLZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcModeAdminCompRleBeforeLZ_Type.__name__ = "Integer32"
_AppcModeAdminCompRleBeforeLZ_Object = MibTableColumn
appcModeAdminCompRleBeforeLZ = _AppcModeAdminCompRleBeforeLZ_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 22),
    _AppcModeAdminCompRleBeforeLZ_Type()
)
appcModeAdminCompRleBeforeLZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminCompRleBeforeLZ.setStatus("current")


class _AppcModeAdminSyncLvl_Type(Integer32):
    """Custom type appcModeAdminSyncLvl based on Integer32"""
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
          ("noneConfirm", 2),
          ("noneConfirmSyncPoint", 3))
    )


_AppcModeAdminSyncLvl_Type.__name__ = "Integer32"
_AppcModeAdminSyncLvl_Object = MibTableColumn
appcModeAdminSyncLvl = _AppcModeAdminSyncLvl_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 23),
    _AppcModeAdminSyncLvl_Type()
)
appcModeAdminSyncLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminSyncLvl.setStatus("current")


class _AppcModeAdminCrypto_Type(Integer32):
    """Custom type appcModeAdminCrypto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mandatory", 2),
          ("notSupported", 1),
          ("selective", 3))
    )


_AppcModeAdminCrypto_Type.__name__ = "Integer32"
_AppcModeAdminCrypto_Object = MibTableColumn
appcModeAdminCrypto = _AppcModeAdminCrypto_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 5, 1, 24),
    _AppcModeAdminCrypto_Type()
)
appcModeAdminCrypto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeAdminCrypto.setStatus("current")
_AppcModeOperTable_Object = MibTable
appcModeOperTable = _AppcModeOperTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    appcModeOperTable.setStatus("current")
_AppcModeOperEntry_Object = MibTableRow
appcModeOperEntry = _AppcModeOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1)
)
appcModeOperEntry.setIndexNames(
    (0, "APPC-MIB", "appcModeOperLocLuName"),
    (0, "APPC-MIB", "appcModeOperParLuName"),
    (0, "APPC-MIB", "appcModeOperModeName"),
)
if mibBuilder.loadTexts:
    appcModeOperEntry.setStatus("current")


class _AppcModeOperLocLuName_Type(DisplayString):
    """Custom type appcModeOperLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcModeOperLocLuName_Type.__name__ = "DisplayString"
_AppcModeOperLocLuName_Object = MibTableColumn
appcModeOperLocLuName = _AppcModeOperLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 1),
    _AppcModeOperLocLuName_Type()
)
appcModeOperLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcModeOperLocLuName.setStatus("current")


class _AppcModeOperParLuName_Type(DisplayString):
    """Custom type appcModeOperParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcModeOperParLuName_Type.__name__ = "DisplayString"
_AppcModeOperParLuName_Object = MibTableColumn
appcModeOperParLuName = _AppcModeOperParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 2),
    _AppcModeOperParLuName_Type()
)
appcModeOperParLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcModeOperParLuName.setStatus("current")


class _AppcModeOperModeName_Type(DisplayString):
    """Custom type appcModeOperModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcModeOperModeName_Type.__name__ = "DisplayString"
_AppcModeOperModeName_Object = MibTableColumn
appcModeOperModeName = _AppcModeOperModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 3),
    _AppcModeOperModeName_Type()
)
appcModeOperModeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcModeOperModeName.setStatus("current")


class _AppcModeOperCosName_Type(DisplayString):
    """Custom type appcModeOperCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcModeOperCosName_Type.__name__ = "DisplayString"
_AppcModeOperCosName_Object = MibTableColumn
appcModeOperCosName = _AppcModeOperCosName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 4),
    _AppcModeOperCosName_Type()
)
appcModeOperCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperCosName.setStatus("current")


class _AppcModeOperSessEndTpName_Type(DisplayString):
    """Custom type appcModeOperSessEndTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AppcModeOperSessEndTpName_Type.__name__ = "DisplayString"
_AppcModeOperSessEndTpName_Object = MibTableColumn
appcModeOperSessEndTpName = _AppcModeOperSessEndTpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 5),
    _AppcModeOperSessEndTpName_Type()
)
appcModeOperSessEndTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperSessEndTpName.setStatus("current")
_AppcModeOperSessLimit_Type = Integer32
_AppcModeOperSessLimit_Object = MibTableColumn
appcModeOperSessLimit = _AppcModeOperSessLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 6),
    _AppcModeOperSessLimit_Type()
)
appcModeOperSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperSessLimit.setStatus("current")
_AppcModeOperMaxSessLimit_Type = Integer32
_AppcModeOperMaxSessLimit_Object = MibTableColumn
appcModeOperMaxSessLimit = _AppcModeOperMaxSessLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 7),
    _AppcModeOperMaxSessLimit_Type()
)
appcModeOperMaxSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperMaxSessLimit.setStatus("current")
_AppcModeOperMinCwinLimit_Type = Integer32
_AppcModeOperMinCwinLimit_Object = MibTableColumn
appcModeOperMinCwinLimit = _AppcModeOperMinCwinLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 8),
    _AppcModeOperMinCwinLimit_Type()
)
appcModeOperMinCwinLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperMinCwinLimit.setStatus("current")
_AppcModeOperMinClosLimit_Type = Integer32
_AppcModeOperMinClosLimit_Object = MibTableColumn
appcModeOperMinClosLimit = _AppcModeOperMinClosLimit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 9),
    _AppcModeOperMinClosLimit_Type()
)
appcModeOperMinClosLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperMinClosLimit.setStatus("current")
_AppcModeOperConWinAutoActLmt_Type = Integer32
_AppcModeOperConWinAutoActLmt_Object = MibTableColumn
appcModeOperConWinAutoActLmt = _AppcModeOperConWinAutoActLmt_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 10),
    _AppcModeOperConWinAutoActLmt_Type()
)
appcModeOperConWinAutoActLmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperConWinAutoActLmt.setStatus("current")
_AppcModeOperRecvPacWinSz_Type = Integer32
_AppcModeOperRecvPacWinSz_Object = MibTableColumn
appcModeOperRecvPacWinSz = _AppcModeOperRecvPacWinSz_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 11),
    _AppcModeOperRecvPacWinSz_Type()
)
appcModeOperRecvPacWinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperRecvPacWinSz.setStatus("current")
_AppcModeOperSendPacWinSz_Type = Integer32
_AppcModeOperSendPacWinSz_Object = MibTableColumn
appcModeOperSendPacWinSz = _AppcModeOperSendPacWinSz_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 12),
    _AppcModeOperSendPacWinSz_Type()
)
appcModeOperSendPacWinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperSendPacWinSz.setStatus("current")
_AppcModeOperPrefRecvRuSz_Type = Integer32
_AppcModeOperPrefRecvRuSz_Object = MibTableColumn
appcModeOperPrefRecvRuSz = _AppcModeOperPrefRecvRuSz_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 13),
    _AppcModeOperPrefRecvRuSz_Type()
)
appcModeOperPrefRecvRuSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperPrefRecvRuSz.setStatus("current")
_AppcModeOperPrefSendRuSz_Type = Integer32
_AppcModeOperPrefSendRuSz_Object = MibTableColumn
appcModeOperPrefSendRuSz = _AppcModeOperPrefSendRuSz_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 14),
    _AppcModeOperPrefSendRuSz_Type()
)
appcModeOperPrefSendRuSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperPrefSendRuSz.setStatus("current")
_AppcModeOperRecvRuSzUpBnd_Type = Integer32
_AppcModeOperRecvRuSzUpBnd_Object = MibTableColumn
appcModeOperRecvRuSzUpBnd = _AppcModeOperRecvRuSzUpBnd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 15),
    _AppcModeOperRecvRuSzUpBnd_Type()
)
appcModeOperRecvRuSzUpBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperRecvRuSzUpBnd.setStatus("current")
_AppcModeOperSendRuSzUpBnd_Type = Integer32
_AppcModeOperSendRuSzUpBnd_Object = MibTableColumn
appcModeOperSendRuSzUpBnd = _AppcModeOperSendRuSzUpBnd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 16),
    _AppcModeOperSendRuSzUpBnd_Type()
)
appcModeOperSendRuSzUpBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperSendRuSzUpBnd.setStatus("current")
_AppcModeOperRecvRuSzLoBnd_Type = Integer32
_AppcModeOperRecvRuSzLoBnd_Object = MibTableColumn
appcModeOperRecvRuSzLoBnd = _AppcModeOperRecvRuSzLoBnd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 17),
    _AppcModeOperRecvRuSzLoBnd_Type()
)
appcModeOperRecvRuSzLoBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperRecvRuSzLoBnd.setStatus("current")
_AppcModeOperSendRuSzLoBnd_Type = Integer32
_AppcModeOperSendRuSzLoBnd_Object = MibTableColumn
appcModeOperSendRuSzLoBnd = _AppcModeOperSendRuSzLoBnd_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 18),
    _AppcModeOperSendRuSzLoBnd_Type()
)
appcModeOperSendRuSzLoBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperSendRuSzLoBnd.setStatus("current")


class _AppcModeOperSingSessReinit_Type(Integer32):
    """Custom type appcModeOperSingSessReinit based on Integer32"""
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
        *(("notApplicable", 1),
          ("operatorControlled", 2),
          ("primaryOnly", 3),
          ("primaryOrSecondary", 5),
          ("secondaryOnly", 4))
    )


_AppcModeOperSingSessReinit_Type.__name__ = "Integer32"
_AppcModeOperSingSessReinit_Object = MibTableColumn
appcModeOperSingSessReinit = _AppcModeOperSingSessReinit_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 19),
    _AppcModeOperSingSessReinit_Type()
)
appcModeOperSingSessReinit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperSingSessReinit.setStatus("current")


class _AppcModeOperCompression_Type(Integer32):
    """Custom type appcModeOperCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("prohibited", 1),
          ("required", 2))
    )


_AppcModeOperCompression_Type.__name__ = "Integer32"
_AppcModeOperCompression_Object = MibTableColumn
appcModeOperCompression = _AppcModeOperCompression_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 20),
    _AppcModeOperCompression_Type()
)
appcModeOperCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperCompression.setStatus("current")


class _AppcModeOperInBoundCompLevel_Type(Integer32):
    """Custom type appcModeOperInBoundCompLevel based on Integer32"""
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
        *(("lz10", 4),
          ("lz12", 5),
          ("lz9", 3),
          ("none", 1),
          ("rle", 2))
    )


_AppcModeOperInBoundCompLevel_Type.__name__ = "Integer32"
_AppcModeOperInBoundCompLevel_Object = MibTableColumn
appcModeOperInBoundCompLevel = _AppcModeOperInBoundCompLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 21),
    _AppcModeOperInBoundCompLevel_Type()
)
appcModeOperInBoundCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperInBoundCompLevel.setStatus("current")


class _AppcModeOperOutBoundCompLevel_Type(Integer32):
    """Custom type appcModeOperOutBoundCompLevel based on Integer32"""
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
        *(("lz10", 4),
          ("lz12", 5),
          ("lz9", 3),
          ("none", 1),
          ("rle", 2))
    )


_AppcModeOperOutBoundCompLevel_Type.__name__ = "Integer32"
_AppcModeOperOutBoundCompLevel_Object = MibTableColumn
appcModeOperOutBoundCompLevel = _AppcModeOperOutBoundCompLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 22),
    _AppcModeOperOutBoundCompLevel_Type()
)
appcModeOperOutBoundCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperOutBoundCompLevel.setStatus("current")


class _AppcModeOperCompRleBeforeLZ_Type(Integer32):
    """Custom type appcModeOperCompRleBeforeLZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcModeOperCompRleBeforeLZ_Type.__name__ = "Integer32"
_AppcModeOperCompRleBeforeLZ_Object = MibTableColumn
appcModeOperCompRleBeforeLZ = _AppcModeOperCompRleBeforeLZ_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 23),
    _AppcModeOperCompRleBeforeLZ_Type()
)
appcModeOperCompRleBeforeLZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperCompRleBeforeLZ.setStatus("current")


class _AppcModeOperSyncLvl_Type(Integer32):
    """Custom type appcModeOperSyncLvl based on Integer32"""
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
          ("noneConfirm", 2),
          ("noneConfirmSyncPoint", 3))
    )


_AppcModeOperSyncLvl_Type.__name__ = "Integer32"
_AppcModeOperSyncLvl_Object = MibTableColumn
appcModeOperSyncLvl = _AppcModeOperSyncLvl_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 24),
    _AppcModeOperSyncLvl_Type()
)
appcModeOperSyncLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperSyncLvl.setStatus("current")


class _AppcModeOperCrypto_Type(Integer32):
    """Custom type appcModeOperCrypto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mandatory", 2),
          ("notSupported", 1),
          ("selective", 3))
    )


_AppcModeOperCrypto_Type.__name__ = "Integer32"
_AppcModeOperCrypto_Object = MibTableColumn
appcModeOperCrypto = _AppcModeOperCrypto_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 25),
    _AppcModeOperCrypto_Type()
)
appcModeOperCrypto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperCrypto.setStatus("current")


class _AppcModeOperSyncLvlLastStart_Type(Integer32):
    """Custom type appcModeOperSyncLvlLastStart based on Integer32"""
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
          ("noneConfirm", 2),
          ("noneConfirmSyncPoint", 3))
    )


_AppcModeOperSyncLvlLastStart_Type.__name__ = "Integer32"
_AppcModeOperSyncLvlLastStart_Object = MibTableColumn
appcModeOperSyncLvlLastStart = _AppcModeOperSyncLvlLastStart_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 26),
    _AppcModeOperSyncLvlLastStart_Type()
)
appcModeOperSyncLvlLastStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperSyncLvlLastStart.setStatus("current")


class _AppcModeOperCryptoLastStart_Type(Integer32):
    """Custom type appcModeOperCryptoLastStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mandatory", 2),
          ("notSupported", 1),
          ("selective", 3))
    )


_AppcModeOperCryptoLastStart_Type.__name__ = "Integer32"
_AppcModeOperCryptoLastStart_Object = MibTableColumn
appcModeOperCryptoLastStart = _AppcModeOperCryptoLastStart_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 27),
    _AppcModeOperCryptoLastStart_Type()
)
appcModeOperCryptoLastStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperCryptoLastStart.setStatus("current")


class _AppcModeOperCNOSNeg_Type(Integer32):
    """Custom type appcModeOperCNOSNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcModeOperCNOSNeg_Type.__name__ = "Integer32"
_AppcModeOperCNOSNeg_Object = MibTableColumn
appcModeOperCNOSNeg = _AppcModeOperCNOSNeg_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 28),
    _AppcModeOperCNOSNeg_Type()
)
appcModeOperCNOSNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperCNOSNeg.setStatus("current")
_AppcModeOperActCwin_Type = Gauge32
_AppcModeOperActCwin_Object = MibTableColumn
appcModeOperActCwin = _AppcModeOperActCwin_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 29),
    _AppcModeOperActCwin_Type()
)
appcModeOperActCwin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperActCwin.setStatus("current")
_AppcModeOperActClos_Type = Gauge32
_AppcModeOperActClos_Object = MibTableColumn
appcModeOperActClos = _AppcModeOperActClos_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 30),
    _AppcModeOperActClos_Type()
)
appcModeOperActClos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperActClos.setStatus("current")
_AppcModeOperPndCwin_Type = Gauge32
_AppcModeOperPndCwin_Object = MibTableColumn
appcModeOperPndCwin = _AppcModeOperPndCwin_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 31),
    _AppcModeOperPndCwin_Type()
)
appcModeOperPndCwin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperPndCwin.setStatus("current")
_AppcModeOperPndClos_Type = Gauge32
_AppcModeOperPndClos_Object = MibTableColumn
appcModeOperPndClos = _AppcModeOperPndClos_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 32),
    _AppcModeOperPndClos_Type()
)
appcModeOperPndClos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperPndClos.setStatus("current")
_AppcModeOperPtmCwin_Type = Gauge32
_AppcModeOperPtmCwin_Object = MibTableColumn
appcModeOperPtmCwin = _AppcModeOperPtmCwin_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 33),
    _AppcModeOperPtmCwin_Type()
)
appcModeOperPtmCwin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperPtmCwin.setStatus("current")
_AppcModeOperPtmClos_Type = Gauge32
_AppcModeOperPtmClos_Object = MibTableColumn
appcModeOperPtmClos = _AppcModeOperPtmClos_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 34),
    _AppcModeOperPtmClos_Type()
)
appcModeOperPtmClos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperPtmClos.setStatus("current")


class _AppcModeOperDrainSelf_Type(Integer32):
    """Custom type appcModeOperDrainSelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcModeOperDrainSelf_Type.__name__ = "Integer32"
_AppcModeOperDrainSelf_Object = MibTableColumn
appcModeOperDrainSelf = _AppcModeOperDrainSelf_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 35),
    _AppcModeOperDrainSelf_Type()
)
appcModeOperDrainSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperDrainSelf.setStatus("current")


class _AppcModeOperDrainPart_Type(Integer32):
    """Custom type appcModeOperDrainPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcModeOperDrainPart_Type.__name__ = "Integer32"
_AppcModeOperDrainPart_Object = MibTableColumn
appcModeOperDrainPart = _AppcModeOperDrainPart_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 2, 6, 1, 36),
    _AppcModeOperDrainPart_Type()
)
appcModeOperDrainPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcModeOperDrainPart.setStatus("current")
_AppcTp_ObjectIdentity = ObjectIdentity
appcTp = _AppcTp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3)
)
_AppcTpAdminTable_Object = MibTable
appcTpAdminTable = _AppcTpAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    appcTpAdminTable.setStatus("current")
_AppcTpAdminEntry_Object = MibTableRow
appcTpAdminEntry = _AppcTpAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1)
)
appcTpAdminEntry.setIndexNames(
    (0, "APPC-MIB", "appcTpAdminLocLuName"),
    (0, "APPC-MIB", "appcTpAdminTpName"),
)
if mibBuilder.loadTexts:
    appcTpAdminEntry.setStatus("current")


class _AppcTpAdminLocLuName_Type(DisplayString):
    """Custom type appcTpAdminLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcTpAdminLocLuName_Type.__name__ = "DisplayString"
_AppcTpAdminLocLuName_Object = MibTableColumn
appcTpAdminLocLuName = _AppcTpAdminLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 1),
    _AppcTpAdminLocLuName_Type()
)
appcTpAdminLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcTpAdminLocLuName.setStatus("current")


class _AppcTpAdminTpName_Type(DisplayString):
    """Custom type appcTpAdminTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AppcTpAdminTpName_Type.__name__ = "DisplayString"
_AppcTpAdminTpName_Object = MibTableColumn
appcTpAdminTpName = _AppcTpAdminTpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 2),
    _AppcTpAdminTpName_Type()
)
appcTpAdminTpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcTpAdminTpName.setStatus("current")


class _AppcTpAdminFileSpec_Type(DisplayString):
    """Custom type appcTpAdminFileSpec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AppcTpAdminFileSpec_Type.__name__ = "DisplayString"
_AppcTpAdminFileSpec_Object = MibTableColumn
appcTpAdminFileSpec = _AppcTpAdminFileSpec_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 3),
    _AppcTpAdminFileSpec_Type()
)
appcTpAdminFileSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminFileSpec.setStatus("current")


class _AppcTpAdminStartParm_Type(DisplayString):
    """Custom type appcTpAdminStartParm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AppcTpAdminStartParm_Type.__name__ = "DisplayString"
_AppcTpAdminStartParm_Object = MibTableColumn
appcTpAdminStartParm = _AppcTpAdminStartParm_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 4),
    _AppcTpAdminStartParm_Type()
)
appcTpAdminStartParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminStartParm.setStatus("current")


class _AppcTpAdminTpOperation_Type(Integer32):
    """Custom type appcTpAdminTpOperation based on Integer32"""
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
        *(("nonqueuedAmStarted", 5),
          ("other", 1),
          ("queuedAmStarted", 4),
          ("queuedOperatorPreloaded", 3),
          ("queuedOperatorStarted", 2))
    )


_AppcTpAdminTpOperation_Type.__name__ = "Integer32"
_AppcTpAdminTpOperation_Object = MibTableColumn
appcTpAdminTpOperation = _AppcTpAdminTpOperation_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 5),
    _AppcTpAdminTpOperation_Type()
)
appcTpAdminTpOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminTpOperation.setStatus("current")
_AppcTpAdminInAttachTimeout_Type = Integer32
_AppcTpAdminInAttachTimeout_Object = MibTableColumn
appcTpAdminInAttachTimeout = _AppcTpAdminInAttachTimeout_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 6),
    _AppcTpAdminInAttachTimeout_Type()
)
appcTpAdminInAttachTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminInAttachTimeout.setStatus("current")
_AppcTpAdminRcvAllocTimeout_Type = Integer32
_AppcTpAdminRcvAllocTimeout_Object = MibTableColumn
appcTpAdminRcvAllocTimeout = _AppcTpAdminRcvAllocTimeout_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 7),
    _AppcTpAdminRcvAllocTimeout_Type()
)
appcTpAdminRcvAllocTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminRcvAllocTimeout.setStatus("current")


class _AppcTpAdminSyncLvl_Type(Integer32):
    """Custom type appcTpAdminSyncLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 7),
          ("confirm", 2),
          ("confirmAndSyncpoint", 6),
          ("none", 1),
          ("noneAndConfirm", 3),
          ("noneAndSyncpoint", 5),
          ("syncpoint", 4))
    )


_AppcTpAdminSyncLvl_Type.__name__ = "Integer32"
_AppcTpAdminSyncLvl_Object = MibTableColumn
appcTpAdminSyncLvl = _AppcTpAdminSyncLvl_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 8),
    _AppcTpAdminSyncLvl_Type()
)
appcTpAdminSyncLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminSyncLvl.setStatus("current")
_AppcTpAdminInstLmt_Type = Integer32
_AppcTpAdminInstLmt_Object = MibTableColumn
appcTpAdminInstLmt = _AppcTpAdminInstLmt_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 9),
    _AppcTpAdminInstLmt_Type()
)
appcTpAdminInstLmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminInstLmt.setStatus("current")


class _AppcTpAdminStatus_Type(Integer32):
    """Custom type appcTpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("permDisabled", 3),
          ("tempDisabled", 2))
    )


_AppcTpAdminStatus_Type.__name__ = "Integer32"
_AppcTpAdminStatus_Object = MibTableColumn
appcTpAdminStatus = _AppcTpAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 10),
    _AppcTpAdminStatus_Type()
)
appcTpAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminStatus.setStatus("current")


class _AppcTpAdminLongRun_Type(Integer32):
    """Custom type appcTpAdminLongRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcTpAdminLongRun_Type.__name__ = "Integer32"
_AppcTpAdminLongRun_Object = MibTableColumn
appcTpAdminLongRun = _AppcTpAdminLongRun_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 11),
    _AppcTpAdminLongRun_Type()
)
appcTpAdminLongRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminLongRun.setStatus("current")


class _AppcTpAdminConvType_Type(Integer32):
    """Custom type appcTpAdminConvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("basicOrMapped", 3),
          ("mapped", 2))
    )


_AppcTpAdminConvType_Type.__name__ = "Integer32"
_AppcTpAdminConvType_Object = MibTableColumn
appcTpAdminConvType = _AppcTpAdminConvType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 12),
    _AppcTpAdminConvType_Type()
)
appcTpAdminConvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminConvType.setStatus("current")


class _AppcTpAdminConvDuplex_Type(Integer32):
    """Custom type appcTpAdminConvDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("halfOrFull", 3))
    )


_AppcTpAdminConvDuplex_Type.__name__ = "Integer32"
_AppcTpAdminConvDuplex_Object = MibTableColumn
appcTpAdminConvDuplex = _AppcTpAdminConvDuplex_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 13),
    _AppcTpAdminConvDuplex_Type()
)
appcTpAdminConvDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminConvDuplex.setStatus("current")


class _AppcTpAdminConvSecReq_Type(Integer32):
    """Custom type appcTpAdminConvSecReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcTpAdminConvSecReq_Type.__name__ = "Integer32"
_AppcTpAdminConvSecReq_Object = MibTableColumn
appcTpAdminConvSecReq = _AppcTpAdminConvSecReq_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 14),
    _AppcTpAdminConvSecReq_Type()
)
appcTpAdminConvSecReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminConvSecReq.setStatus("current")


class _AppcTpAdminVerPip_Type(Integer32):
    """Custom type appcTpAdminVerPip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcTpAdminVerPip_Type.__name__ = "Integer32"
_AppcTpAdminVerPip_Object = MibTableColumn
appcTpAdminVerPip = _AppcTpAdminVerPip_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 15),
    _AppcTpAdminVerPip_Type()
)
appcTpAdminVerPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminVerPip.setStatus("current")
_AppcTpAdminPipSubNum_Type = Integer32
_AppcTpAdminPipSubNum_Object = MibTableColumn
appcTpAdminPipSubNum = _AppcTpAdminPipSubNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 3, 1, 1, 16),
    _AppcTpAdminPipSubNum_Type()
)
appcTpAdminPipSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcTpAdminPipSubNum.setStatus("current")
_AppcSession_ObjectIdentity = ObjectIdentity
appcSession = _AppcSession_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4)
)
_AppcActSessTable_Object = MibTable
appcActSessTable = _AppcActSessTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    appcActSessTable.setStatus("current")
_AppcActSessEntry_Object = MibTableRow
appcActSessEntry = _AppcActSessEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1)
)
appcActSessEntry.setIndexNames(
    (0, "APPC-MIB", "appcActSessLocLuName"),
    (0, "APPC-MIB", "appcActSessParLuName"),
    (0, "APPC-MIB", "appcActSessIndex"),
)
if mibBuilder.loadTexts:
    appcActSessEntry.setStatus("current")


class _AppcActSessLocLuName_Type(DisplayString):
    """Custom type appcActSessLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcActSessLocLuName_Type.__name__ = "DisplayString"
_AppcActSessLocLuName_Object = MibTableColumn
appcActSessLocLuName = _AppcActSessLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 1),
    _AppcActSessLocLuName_Type()
)
appcActSessLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcActSessLocLuName.setStatus("current")


class _AppcActSessParLuName_Type(DisplayString):
    """Custom type appcActSessParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcActSessParLuName_Type.__name__ = "DisplayString"
_AppcActSessParLuName_Object = MibTableColumn
appcActSessParLuName = _AppcActSessParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 2),
    _AppcActSessParLuName_Type()
)
appcActSessParLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcActSessParLuName.setStatus("current")
_AppcActSessIndex_Type = Integer32
_AppcActSessIndex_Object = MibTableColumn
appcActSessIndex = _AppcActSessIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 3),
    _AppcActSessIndex_Type()
)
appcActSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcActSessIndex.setStatus("current")


class _AppcActSessPcidCpName_Type(DisplayString):
    """Custom type appcActSessPcidCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_AppcActSessPcidCpName_Type.__name__ = "DisplayString"
_AppcActSessPcidCpName_Object = MibTableColumn
appcActSessPcidCpName = _AppcActSessPcidCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 4),
    _AppcActSessPcidCpName_Type()
)
appcActSessPcidCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessPcidCpName.setStatus("current")


class _AppcActSessPcid_Type(OctetString):
    """Custom type appcActSessPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_AppcActSessPcid_Type.__name__ = "OctetString"
_AppcActSessPcid_Object = MibTableColumn
appcActSessPcid = _AppcActSessPcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 5),
    _AppcActSessPcid_Type()
)
appcActSessPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessPcid.setStatus("current")


class _AppcActSessPluIndicator_Type(Integer32):
    """Custom type appcActSessPluIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localLuIsPlu", 1),
          ("partnerLuIsPlu", 2))
    )


_AppcActSessPluIndicator_Type.__name__ = "Integer32"
_AppcActSessPluIndicator_Object = MibTableColumn
appcActSessPluIndicator = _AppcActSessPluIndicator_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 6),
    _AppcActSessPluIndicator_Type()
)
appcActSessPluIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessPluIndicator.setStatus("current")


class _AppcActSessModeName_Type(DisplayString):
    """Custom type appcActSessModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcActSessModeName_Type.__name__ = "DisplayString"
_AppcActSessModeName_Object = MibTableColumn
appcActSessModeName = _AppcActSessModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 7),
    _AppcActSessModeName_Type()
)
appcActSessModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessModeName.setStatus("current")


class _AppcActSessCosName_Type(DisplayString):
    """Custom type appcActSessCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcActSessCosName_Type.__name__ = "DisplayString"
_AppcActSessCosName_Object = MibTableColumn
appcActSessCosName = _AppcActSessCosName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 8),
    _AppcActSessCosName_Type()
)
appcActSessCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessCosName.setStatus("current")


class _AppcActSessTransPriority_Type(Integer32):
    """Custom type appcActSessTransPriority based on Integer32"""
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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("network", 5),
          ("unknown", 1))
    )


_AppcActSessTransPriority_Type.__name__ = "Integer32"
_AppcActSessTransPriority_Object = MibTableColumn
appcActSessTransPriority = _AppcActSessTransPriority_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 9),
    _AppcActSessTransPriority_Type()
)
appcActSessTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessTransPriority.setStatus("current")


class _AppcActSessEnhanceSecSup_Type(Integer32):
    """Custom type appcActSessEnhanceSecSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 2),
          ("level2", 3),
          ("none", 1))
    )


_AppcActSessEnhanceSecSup_Type.__name__ = "Integer32"
_AppcActSessEnhanceSecSup_Object = MibTableColumn
appcActSessEnhanceSecSup = _AppcActSessEnhanceSecSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 10),
    _AppcActSessEnhanceSecSup_Type()
)
appcActSessEnhanceSecSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessEnhanceSecSup.setStatus("current")


class _AppcActSessSendPacingType_Type(Integer32):
    """Custom type appcActSessSendPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("fixed", 2),
          ("none", 1))
    )


_AppcActSessSendPacingType_Type.__name__ = "Integer32"
_AppcActSessSendPacingType_Object = MibTableColumn
appcActSessSendPacingType = _AppcActSessSendPacingType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 11),
    _AppcActSessSendPacingType_Type()
)
appcActSessSendPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessSendPacingType.setStatus("current")
_AppcActSessSendRpc_Type = Gauge32
_AppcActSessSendRpc_Object = MibTableColumn
appcActSessSendRpc = _AppcActSessSendRpc_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 12),
    _AppcActSessSendRpc_Type()
)
appcActSessSendRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessSendRpc.setStatus("current")
_AppcActSessSendNxWndwSize_Type = Gauge32
_AppcActSessSendNxWndwSize_Object = MibTableColumn
appcActSessSendNxWndwSize = _AppcActSessSendNxWndwSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 13),
    _AppcActSessSendNxWndwSize_Type()
)
appcActSessSendNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessSendNxWndwSize.setStatus("current")


class _AppcActSessRecvPacingType_Type(Integer32):
    """Custom type appcActSessRecvPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("fixed", 2),
          ("none", 1))
    )


_AppcActSessRecvPacingType_Type.__name__ = "Integer32"
_AppcActSessRecvPacingType_Object = MibTableColumn
appcActSessRecvPacingType = _AppcActSessRecvPacingType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 14),
    _AppcActSessRecvPacingType_Type()
)
appcActSessRecvPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessRecvPacingType.setStatus("current")
_AppcActSessRecvRpc_Type = Gauge32
_AppcActSessRecvRpc_Object = MibTableColumn
appcActSessRecvRpc = _AppcActSessRecvRpc_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 15),
    _AppcActSessRecvRpc_Type()
)
appcActSessRecvRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessRecvRpc.setStatus("current")
_AppcActSessRecvNxWndwSize_Type = Gauge32
_AppcActSessRecvNxWndwSize_Object = MibTableColumn
appcActSessRecvNxWndwSize = _AppcActSessRecvNxWndwSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 16),
    _AppcActSessRecvNxWndwSize_Type()
)
appcActSessRecvNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessRecvNxWndwSize.setStatus("current")


class _AppcActSessRscv_Type(OctetString):
    """Custom type appcActSessRscv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AppcActSessRscv_Type.__name__ = "OctetString"
_AppcActSessRscv_Object = MibTableColumn
appcActSessRscv = _AppcActSessRscv_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 17),
    _AppcActSessRscv_Type()
)
appcActSessRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessRscv.setStatus("current")


class _AppcActSessInUse_Type(Integer32):
    """Custom type appcActSessInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AppcActSessInUse_Type.__name__ = "Integer32"
_AppcActSessInUse_Object = MibTableColumn
appcActSessInUse = _AppcActSessInUse_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 18),
    _AppcActSessInUse_Type()
)
appcActSessInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessInUse.setStatus("current")


class _AppcActSessMaxSndRuSize_Type(Integer32):
    """Custom type appcActSessMaxSndRuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_AppcActSessMaxSndRuSize_Type.__name__ = "Integer32"
_AppcActSessMaxSndRuSize_Object = MibTableColumn
appcActSessMaxSndRuSize = _AppcActSessMaxSndRuSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 19),
    _AppcActSessMaxSndRuSize_Type()
)
appcActSessMaxSndRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessMaxSndRuSize.setStatus("current")


class _AppcActSessMaxRcvRuSize_Type(Integer32):
    """Custom type appcActSessMaxRcvRuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_AppcActSessMaxRcvRuSize_Type.__name__ = "Integer32"
_AppcActSessMaxRcvRuSize_Object = MibTableColumn
appcActSessMaxRcvRuSize = _AppcActSessMaxRcvRuSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 20),
    _AppcActSessMaxRcvRuSize_Type()
)
appcActSessMaxRcvRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessMaxRcvRuSize.setStatus("current")


class _AppcActSessSndPacingSize_Type(Integer32):
    """Custom type appcActSessSndPacingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AppcActSessSndPacingSize_Type.__name__ = "Integer32"
_AppcActSessSndPacingSize_Object = MibTableColumn
appcActSessSndPacingSize = _AppcActSessSndPacingSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 21),
    _AppcActSessSndPacingSize_Type()
)
appcActSessSndPacingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessSndPacingSize.setStatus("current")


class _AppcActSessRcvPacingSize_Type(Integer32):
    """Custom type appcActSessRcvPacingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AppcActSessRcvPacingSize_Type.__name__ = "Integer32"
_AppcActSessRcvPacingSize_Object = MibTableColumn
appcActSessRcvPacingSize = _AppcActSessRcvPacingSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 22),
    _AppcActSessRcvPacingSize_Type()
)
appcActSessRcvPacingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessRcvPacingSize.setStatus("current")


class _AppcActSessOperState_Type(Integer32):
    """Custom type appcActSessOperState based on Integer32"""
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
        *(("bound", 3),
          ("pendingBind", 2),
          ("pendingUnbind", 4),
          ("unbound", 1))
    )


_AppcActSessOperState_Type.__name__ = "Integer32"
_AppcActSessOperState_Object = MibTableColumn
appcActSessOperState = _AppcActSessOperState_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 23),
    _AppcActSessOperState_Type()
)
appcActSessOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appcActSessOperState.setStatus("current")
_AppcActSessUpTime_Type = TimeTicks
_AppcActSessUpTime_Object = MibTableColumn
appcActSessUpTime = _AppcActSessUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 24),
    _AppcActSessUpTime_Type()
)
appcActSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessUpTime.setStatus("current")


class _AppcActSessRtpNceId_Type(OctetString):
    """Custom type appcActSessRtpNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcActSessRtpNceId_Type.__name__ = "OctetString"
_AppcActSessRtpNceId_Object = MibTableColumn
appcActSessRtpNceId = _AppcActSessRtpNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 25),
    _AppcActSessRtpNceId_Type()
)
appcActSessRtpNceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessRtpNceId.setStatus("current")


class _AppcActSessRtpTcid_Type(OctetString):
    """Custom type appcActSessRtpTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_AppcActSessRtpTcid_Type.__name__ = "OctetString"
_AppcActSessRtpTcid_Object = MibTableColumn
appcActSessRtpTcid = _AppcActSessRtpTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 26),
    _AppcActSessRtpTcid_Type()
)
appcActSessRtpTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessRtpTcid.setStatus("current")
_AppcActSessLinkIndex_Type = InstancePointer
_AppcActSessLinkIndex_Object = MibTableColumn
appcActSessLinkIndex = _AppcActSessLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 1, 1, 27),
    _AppcActSessLinkIndex_Type()
)
appcActSessLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActSessLinkIndex.setStatus("current")
_AppcSessStatsTable_Object = MibTable
appcSessStatsTable = _AppcSessStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    appcSessStatsTable.setStatus("current")
_AppcSessStatsEntry_Object = MibTableRow
appcSessStatsEntry = _AppcSessStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1)
)
appcSessStatsEntry.setIndexNames(
    (0, "APPC-MIB", "appcSessStatsLocLuName"),
    (0, "APPC-MIB", "appcSessStatsParLuName"),
    (0, "APPC-MIB", "appcSessStatsSessIndex"),
)
if mibBuilder.loadTexts:
    appcSessStatsEntry.setStatus("current")


class _AppcSessStatsLocLuName_Type(DisplayString):
    """Custom type appcSessStatsLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcSessStatsLocLuName_Type.__name__ = "DisplayString"
_AppcSessStatsLocLuName_Object = MibTableColumn
appcSessStatsLocLuName = _AppcSessStatsLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 1),
    _AppcSessStatsLocLuName_Type()
)
appcSessStatsLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcSessStatsLocLuName.setStatus("current")


class _AppcSessStatsParLuName_Type(DisplayString):
    """Custom type appcSessStatsParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcSessStatsParLuName_Type.__name__ = "DisplayString"
_AppcSessStatsParLuName_Object = MibTableColumn
appcSessStatsParLuName = _AppcSessStatsParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 2),
    _AppcSessStatsParLuName_Type()
)
appcSessStatsParLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcSessStatsParLuName.setStatus("current")
_AppcSessStatsSessIndex_Type = Integer32
_AppcSessStatsSessIndex_Object = MibTableColumn
appcSessStatsSessIndex = _AppcSessStatsSessIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 3),
    _AppcSessStatsSessIndex_Type()
)
appcSessStatsSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcSessStatsSessIndex.setStatus("current")
_AppcSessStatsSentFmdBytes_Type = Counter32
_AppcSessStatsSentFmdBytes_Object = MibTableColumn
appcSessStatsSentFmdBytes = _AppcSessStatsSentFmdBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 4),
    _AppcSessStatsSentFmdBytes_Type()
)
appcSessStatsSentFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsSentFmdBytes.setStatus("current")
_AppcSessStatsSentNonFmdBytes_Type = Counter32
_AppcSessStatsSentNonFmdBytes_Object = MibTableColumn
appcSessStatsSentNonFmdBytes = _AppcSessStatsSentNonFmdBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 5),
    _AppcSessStatsSentNonFmdBytes_Type()
)
appcSessStatsSentNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsSentNonFmdBytes.setStatus("current")
_AppcSessStatsRcvdFmdBytes_Type = Counter32
_AppcSessStatsRcvdFmdBytes_Object = MibTableColumn
appcSessStatsRcvdFmdBytes = _AppcSessStatsRcvdFmdBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 6),
    _AppcSessStatsRcvdFmdBytes_Type()
)
appcSessStatsRcvdFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsRcvdFmdBytes.setStatus("current")
_AppcSessStatsRcvdNonFmdBytes_Type = Counter32
_AppcSessStatsRcvdNonFmdBytes_Object = MibTableColumn
appcSessStatsRcvdNonFmdBytes = _AppcSessStatsRcvdNonFmdBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 7),
    _AppcSessStatsRcvdNonFmdBytes_Type()
)
appcSessStatsRcvdNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsRcvdNonFmdBytes.setStatus("current")
_AppcSessStatsSentFmdRus_Type = Counter32
_AppcSessStatsSentFmdRus_Object = MibTableColumn
appcSessStatsSentFmdRus = _AppcSessStatsSentFmdRus_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 8),
    _AppcSessStatsSentFmdRus_Type()
)
appcSessStatsSentFmdRus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsSentFmdRus.setStatus("current")
_AppcSessStatsSentNonFmdRus_Type = Counter32
_AppcSessStatsSentNonFmdRus_Object = MibTableColumn
appcSessStatsSentNonFmdRus = _AppcSessStatsSentNonFmdRus_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 9),
    _AppcSessStatsSentNonFmdRus_Type()
)
appcSessStatsSentNonFmdRus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsSentNonFmdRus.setStatus("current")
_AppcSessStatsRcvdFmdRus_Type = Counter32
_AppcSessStatsRcvdFmdRus_Object = MibTableColumn
appcSessStatsRcvdFmdRus = _AppcSessStatsRcvdFmdRus_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 10),
    _AppcSessStatsRcvdFmdRus_Type()
)
appcSessStatsRcvdFmdRus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsRcvdFmdRus.setStatus("current")
_AppcSessStatsRcvdNonFmdRus_Type = Counter32
_AppcSessStatsRcvdNonFmdRus_Object = MibTableColumn
appcSessStatsRcvdNonFmdRus = _AppcSessStatsRcvdNonFmdRus_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 11),
    _AppcSessStatsRcvdNonFmdRus_Type()
)
appcSessStatsRcvdNonFmdRus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsRcvdNonFmdRus.setStatus("current")
_AppcSessStatsCtrUpTime_Type = TimeTicks
_AppcSessStatsCtrUpTime_Object = MibTableColumn
appcSessStatsCtrUpTime = _AppcSessStatsCtrUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 2, 1, 12),
    _AppcSessStatsCtrUpTime_Type()
)
appcSessStatsCtrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessStatsCtrUpTime.setStatus("current")
_AppcHistSessTable_Object = MibTable
appcHistSessTable = _AppcHistSessTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    appcHistSessTable.setStatus("current")
_AppcHistSessEntry_Object = MibTableRow
appcHistSessEntry = _AppcHistSessEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1)
)
appcHistSessEntry.setIndexNames(
    (0, "APPC-MIB", "appcHistSessIndex"),
)
if mibBuilder.loadTexts:
    appcHistSessEntry.setStatus("current")


class _AppcHistSessIndex_Type(Integer32):
    """Custom type appcHistSessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AppcHistSessIndex_Type.__name__ = "Integer32"
_AppcHistSessIndex_Object = MibTableColumn
appcHistSessIndex = _AppcHistSessIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 1),
    _AppcHistSessIndex_Type()
)
appcHistSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcHistSessIndex.setStatus("current")
_AppcHistSessTime_Type = DateAndTime
_AppcHistSessTime_Object = MibTableColumn
appcHistSessTime = _AppcHistSessTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 2),
    _AppcHistSessTime_Type()
)
appcHistSessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessTime.setStatus("current")


class _AppcHistSessType_Type(Integer32):
    """Custom type appcHistSessType based on Integer32"""
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
        *(("recvNegBindRsp", 1),
          ("sendNegBindRsp", 2),
          ("sessActRejected", 3),
          ("unbindReceived", 5),
          ("unbindSent", 4))
    )


_AppcHistSessType_Type.__name__ = "Integer32"
_AppcHistSessType_Object = MibTableColumn
appcHistSessType = _AppcHistSessType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 3),
    _AppcHistSessType_Type()
)
appcHistSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessType.setStatus("current")


class _AppcHistSessLocLuName_Type(DisplayString):
    """Custom type appcHistSessLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcHistSessLocLuName_Type.__name__ = "DisplayString"
_AppcHistSessLocLuName_Object = MibTableColumn
appcHistSessLocLuName = _AppcHistSessLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 4),
    _AppcHistSessLocLuName_Type()
)
appcHistSessLocLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessLocLuName.setStatus("current")


class _AppcHistSessParLuName_Type(DisplayString):
    """Custom type appcHistSessParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppcHistSessParLuName_Type.__name__ = "DisplayString"
_AppcHistSessParLuName_Object = MibTableColumn
appcHistSessParLuName = _AppcHistSessParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 5),
    _AppcHistSessParLuName_Type()
)
appcHistSessParLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessParLuName.setStatus("current")


class _AppcHistSessModeName_Type(DisplayString):
    """Custom type appcHistSessModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcHistSessModeName_Type.__name__ = "DisplayString"
_AppcHistSessModeName_Object = MibTableColumn
appcHistSessModeName = _AppcHistSessModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 6),
    _AppcHistSessModeName_Type()
)
appcHistSessModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessModeName.setStatus("current")


class _AppcHistSessUnbindType_Type(OctetString):
    """Custom type appcHistSessUnbindType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppcHistSessUnbindType_Type.__name__ = "OctetString"
_AppcHistSessUnbindType_Object = MibTableColumn
appcHistSessUnbindType = _AppcHistSessUnbindType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 7),
    _AppcHistSessUnbindType_Type()
)
appcHistSessUnbindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessUnbindType.setStatus("current")
_AppcHistSessSenseData_Type = SnaSenseData
_AppcHistSessSenseData_Object = MibTableColumn
appcHistSessSenseData = _AppcHistSessSenseData_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 8),
    _AppcHistSessSenseData_Type()
)
appcHistSessSenseData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessSenseData.setStatus("current")


class _AppcHistSessComponentId_Type(DisplayString):
    """Custom type appcHistSessComponentId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppcHistSessComponentId_Type.__name__ = "DisplayString"
_AppcHistSessComponentId_Object = MibTableColumn
appcHistSessComponentId = _AppcHistSessComponentId_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 9),
    _AppcHistSessComponentId_Type()
)
appcHistSessComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessComponentId.setStatus("current")


class _AppcHistSessDetectModule_Type(DisplayString):
    """Custom type appcHistSessDetectModule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppcHistSessDetectModule_Type.__name__ = "DisplayString"
_AppcHistSessDetectModule_Object = MibTableColumn
appcHistSessDetectModule = _AppcHistSessDetectModule_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 3, 1, 10),
    _AppcHistSessDetectModule_Type()
)
appcHistSessDetectModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistSessDetectModule.setStatus("current")
_AppcSessRtpTable_Object = MibTable
appcSessRtpTable = _AppcSessRtpTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    appcSessRtpTable.setStatus("current")
_AppcSessRtpEntry_Object = MibTableRow
appcSessRtpEntry = _AppcSessRtpEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 4, 1)
)
appcSessRtpEntry.setIndexNames(
    (0, "APPC-MIB", "appcSessRtpNceId"),
    (0, "APPC-MIB", "appcSessRtpTcid"),
)
if mibBuilder.loadTexts:
    appcSessRtpEntry.setStatus("current")


class _AppcSessRtpNceId_Type(OctetString):
    """Custom type appcSessRtpNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcSessRtpNceId_Type.__name__ = "OctetString"
_AppcSessRtpNceId_Object = MibTableColumn
appcSessRtpNceId = _AppcSessRtpNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 4, 1, 1),
    _AppcSessRtpNceId_Type()
)
appcSessRtpNceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcSessRtpNceId.setStatus("current")


class _AppcSessRtpTcid_Type(OctetString):
    """Custom type appcSessRtpTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AppcSessRtpTcid_Type.__name__ = "OctetString"
_AppcSessRtpTcid_Object = MibTableColumn
appcSessRtpTcid = _AppcSessRtpTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 4, 1, 2),
    _AppcSessRtpTcid_Type()
)
appcSessRtpTcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcSessRtpTcid.setStatus("current")
_AppcSessRtpSessions_Type = Gauge32
_AppcSessRtpSessions_Object = MibTableColumn
appcSessRtpSessions = _AppcSessRtpSessions_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 4, 4, 1, 3),
    _AppcSessRtpSessions_Type()
)
appcSessRtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcSessRtpSessions.setStatus("current")
_AppcConversation_ObjectIdentity = ObjectIdentity
appcConversation = _AppcConversation_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5)
)
_AppcActiveConvTable_Object = MibTable
appcActiveConvTable = _AppcActiveConvTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    appcActiveConvTable.setStatus("current")
_AppcActiveConvEntry_Object = MibTableRow
appcActiveConvEntry = _AppcActiveConvEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1)
)
appcActiveConvEntry.setIndexNames(
    (0, "APPC-MIB", "appcActiveConvLocLuName"),
    (0, "APPC-MIB", "appcActiveConvParLuName"),
    (0, "APPC-MIB", "appcActiveConvSessIndex"),
)
if mibBuilder.loadTexts:
    appcActiveConvEntry.setStatus("current")


class _AppcActiveConvLocLuName_Type(DisplayString):
    """Custom type appcActiveConvLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcActiveConvLocLuName_Type.__name__ = "DisplayString"
_AppcActiveConvLocLuName_Object = MibTableColumn
appcActiveConvLocLuName = _AppcActiveConvLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 1),
    _AppcActiveConvLocLuName_Type()
)
appcActiveConvLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcActiveConvLocLuName.setStatus("current")


class _AppcActiveConvParLuName_Type(DisplayString):
    """Custom type appcActiveConvParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcActiveConvParLuName_Type.__name__ = "DisplayString"
_AppcActiveConvParLuName_Object = MibTableColumn
appcActiveConvParLuName = _AppcActiveConvParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 2),
    _AppcActiveConvParLuName_Type()
)
appcActiveConvParLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcActiveConvParLuName.setStatus("current")
_AppcActiveConvSessIndex_Type = Integer32
_AppcActiveConvSessIndex_Object = MibTableColumn
appcActiveConvSessIndex = _AppcActiveConvSessIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 3),
    _AppcActiveConvSessIndex_Type()
)
appcActiveConvSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcActiveConvSessIndex.setStatus("current")


class _AppcActiveConvId_Type(OctetString):
    """Custom type appcActiveConvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AppcActiveConvId_Type.__name__ = "OctetString"
_AppcActiveConvId_Object = MibTableColumn
appcActiveConvId = _AppcActiveConvId_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 4),
    _AppcActiveConvId_Type()
)
appcActiveConvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvId.setStatus("current")


class _AppcActiveConvState_Type(Integer32):
    """Custom type appcActiveConvState based on Integer32"""
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
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("backoutRequired", 17),
          ("confirm", 4),
          ("confirmDealloc", 6),
          ("confirmSend", 5),
          ("deferDeallocate", 13),
          ("deferReceive", 12),
          ("pendingDeallocate", 7),
          ("pendingPost", 8),
          ("receive", 3),
          ("receiveOnly", 11),
          ("reset", 1),
          ("send", 2),
          ("sendOnly", 10),
          ("sendReceive", 9),
          ("syncpoint", 14),
          ("syncpointDeallocate", 16),
          ("syncpointSend", 15))
    )


_AppcActiveConvState_Type.__name__ = "Integer32"
_AppcActiveConvState_Object = MibTableColumn
appcActiveConvState = _AppcActiveConvState_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 5),
    _AppcActiveConvState_Type()
)
appcActiveConvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvState.setStatus("current")


class _AppcActiveConvType_Type(Integer32):
    """Custom type appcActiveConvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("mapped", 2))
    )


_AppcActiveConvType_Type.__name__ = "Integer32"
_AppcActiveConvType_Object = MibTableColumn
appcActiveConvType = _AppcActiveConvType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 6),
    _AppcActiveConvType_Type()
)
appcActiveConvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvType.setStatus("current")


class _AppcActiveConvCorrelator_Type(OctetString):
    """Custom type appcActiveConvCorrelator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcActiveConvCorrelator_Type.__name__ = "OctetString"
_AppcActiveConvCorrelator_Object = MibTableColumn
appcActiveConvCorrelator = _AppcActiveConvCorrelator_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 7),
    _AppcActiveConvCorrelator_Type()
)
appcActiveConvCorrelator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvCorrelator.setStatus("current")


class _AppcActiveConvSyncLvl_Type(Integer32):
    """Custom type appcActiveConvSyncLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("confirm", 2),
          ("none", 1),
          ("syncpt", 3))
    )


_AppcActiveConvSyncLvl_Type.__name__ = "Integer32"
_AppcActiveConvSyncLvl_Object = MibTableColumn
appcActiveConvSyncLvl = _AppcActiveConvSyncLvl_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 8),
    _AppcActiveConvSyncLvl_Type()
)
appcActiveConvSyncLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvSyncLvl.setStatus("current")


class _AppcActiveConvSource_Type(Integer32):
    """Custom type appcActiveConvSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localLu", 1),
          ("partnerLu", 2))
    )


_AppcActiveConvSource_Type.__name__ = "Integer32"
_AppcActiveConvSource_Object = MibTableColumn
appcActiveConvSource = _AppcActiveConvSource_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 9),
    _AppcActiveConvSource_Type()
)
appcActiveConvSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvSource.setStatus("current")


class _AppcActiveConvDuplex_Type(Integer32):
    """Custom type appcActiveConvDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_AppcActiveConvDuplex_Type.__name__ = "Integer32"
_AppcActiveConvDuplex_Object = MibTableColumn
appcActiveConvDuplex = _AppcActiveConvDuplex_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 10),
    _AppcActiveConvDuplex_Type()
)
appcActiveConvDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvDuplex.setStatus("current")
_AppcActiveConvUpTime_Type = TimeTicks
_AppcActiveConvUpTime_Object = MibTableColumn
appcActiveConvUpTime = _AppcActiveConvUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 11),
    _AppcActiveConvUpTime_Type()
)
appcActiveConvUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvUpTime.setStatus("current")
_AppcActiveConvSendBytes_Type = Counter32
_AppcActiveConvSendBytes_Object = MibTableColumn
appcActiveConvSendBytes = _AppcActiveConvSendBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 12),
    _AppcActiveConvSendBytes_Type()
)
appcActiveConvSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvSendBytes.setStatus("current")
_AppcActiveConvRcvBytes_Type = Counter32
_AppcActiveConvRcvBytes_Object = MibTableColumn
appcActiveConvRcvBytes = _AppcActiveConvRcvBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 13),
    _AppcActiveConvRcvBytes_Type()
)
appcActiveConvRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvRcvBytes.setStatus("current")


class _AppcActiveConvUserid_Type(DisplayString):
    """Custom type appcActiveConvUserid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AppcActiveConvUserid_Type.__name__ = "DisplayString"
_AppcActiveConvUserid_Object = MibTableColumn
appcActiveConvUserid = _AppcActiveConvUserid_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 14),
    _AppcActiveConvUserid_Type()
)
appcActiveConvUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvUserid.setStatus("current")


class _AppcActiveConvPcidNauName_Type(DisplayString):
    """Custom type appcActiveConvPcidNauName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_AppcActiveConvPcidNauName_Type.__name__ = "DisplayString"
_AppcActiveConvPcidNauName_Object = MibTableColumn
appcActiveConvPcidNauName = _AppcActiveConvPcidNauName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 15),
    _AppcActiveConvPcidNauName_Type()
)
appcActiveConvPcidNauName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvPcidNauName.setStatus("current")


class _AppcActiveConvPcid_Type(OctetString):
    """Custom type appcActiveConvPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_AppcActiveConvPcid_Type.__name__ = "OctetString"
_AppcActiveConvPcid_Object = MibTableColumn
appcActiveConvPcid = _AppcActiveConvPcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 16),
    _AppcActiveConvPcid_Type()
)
appcActiveConvPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvPcid.setStatus("current")


class _AppcActiveConvModeName_Type(DisplayString):
    """Custom type appcActiveConvModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcActiveConvModeName_Type.__name__ = "DisplayString"
_AppcActiveConvModeName_Object = MibTableColumn
appcActiveConvModeName = _AppcActiveConvModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 17),
    _AppcActiveConvModeName_Type()
)
appcActiveConvModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvModeName.setStatus("current")


class _AppcActiveConvLuwIdName_Type(DisplayString):
    """Custom type appcActiveConvLuwIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcActiveConvLuwIdName_Type.__name__ = "DisplayString"
_AppcActiveConvLuwIdName_Object = MibTableColumn
appcActiveConvLuwIdName = _AppcActiveConvLuwIdName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 18),
    _AppcActiveConvLuwIdName_Type()
)
appcActiveConvLuwIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvLuwIdName.setStatus("current")


class _AppcActiveConvLuwIdInstance_Type(OctetString):
    """Custom type appcActiveConvLuwIdInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AppcActiveConvLuwIdInstance_Type.__name__ = "OctetString"
_AppcActiveConvLuwIdInstance_Object = MibTableColumn
appcActiveConvLuwIdInstance = _AppcActiveConvLuwIdInstance_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 19),
    _AppcActiveConvLuwIdInstance_Type()
)
appcActiveConvLuwIdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvLuwIdInstance.setStatus("current")


class _AppcActiveConvLuwIdSequence_Type(OctetString):
    """Custom type appcActiveConvLuwIdSequence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_AppcActiveConvLuwIdSequence_Type.__name__ = "OctetString"
_AppcActiveConvLuwIdSequence_Object = MibTableColumn
appcActiveConvLuwIdSequence = _AppcActiveConvLuwIdSequence_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 20),
    _AppcActiveConvLuwIdSequence_Type()
)
appcActiveConvLuwIdSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvLuwIdSequence.setStatus("current")


class _AppcActiveConvTpName_Type(DisplayString):
    """Custom type appcActiveConvTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AppcActiveConvTpName_Type.__name__ = "DisplayString"
_AppcActiveConvTpName_Object = MibTableColumn
appcActiveConvTpName = _AppcActiveConvTpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 1, 1, 21),
    _AppcActiveConvTpName_Type()
)
appcActiveConvTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcActiveConvTpName.setStatus("current")
_AppcHistConvTable_Object = MibTable
appcHistConvTable = _AppcHistConvTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    appcHistConvTable.setStatus("current")
_AppcHistConvEntry_Object = MibTableRow
appcHistConvEntry = _AppcHistConvEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1)
)
appcHistConvEntry.setIndexNames(
    (0, "APPC-MIB", "appcHistConvIndex"),
)
if mibBuilder.loadTexts:
    appcHistConvEntry.setStatus("current")
_AppcHistConvIndex_Type = Integer32
_AppcHistConvIndex_Object = MibTableColumn
appcHistConvIndex = _AppcHistConvIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 1),
    _AppcHistConvIndex_Type()
)
appcHistConvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcHistConvIndex.setStatus("current")
_AppcHistConvEndTime_Type = DateAndTime
_AppcHistConvEndTime_Object = MibTableColumn
appcHistConvEndTime = _AppcHistConvEndTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 2),
    _AppcHistConvEndTime_Type()
)
appcHistConvEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvEndTime.setStatus("current")


class _AppcHistConvLocLuName_Type(DisplayString):
    """Custom type appcHistConvLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcHistConvLocLuName_Type.__name__ = "DisplayString"
_AppcHistConvLocLuName_Object = MibTableColumn
appcHistConvLocLuName = _AppcHistConvLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 3),
    _AppcHistConvLocLuName_Type()
)
appcHistConvLocLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvLocLuName.setStatus("current")


class _AppcHistConvParLuName_Type(DisplayString):
    """Custom type appcHistConvParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcHistConvParLuName_Type.__name__ = "DisplayString"
_AppcHistConvParLuName_Object = MibTableColumn
appcHistConvParLuName = _AppcHistConvParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 4),
    _AppcHistConvParLuName_Type()
)
appcHistConvParLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvParLuName.setStatus("current")


class _AppcHistConvTpName_Type(DisplayString):
    """Custom type appcHistConvTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AppcHistConvTpName_Type.__name__ = "DisplayString"
_AppcHistConvTpName_Object = MibTableColumn
appcHistConvTpName = _AppcHistConvTpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 5),
    _AppcHistConvTpName_Type()
)
appcHistConvTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvTpName.setStatus("current")


class _AppcHistConvPcidNauName_Type(DisplayString):
    """Custom type appcHistConvPcidNauName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_AppcHistConvPcidNauName_Type.__name__ = "DisplayString"
_AppcHistConvPcidNauName_Object = MibTableColumn
appcHistConvPcidNauName = _AppcHistConvPcidNauName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 6),
    _AppcHistConvPcidNauName_Type()
)
appcHistConvPcidNauName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvPcidNauName.setStatus("current")


class _AppcHistConvPcid_Type(OctetString):
    """Custom type appcHistConvPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_AppcHistConvPcid_Type.__name__ = "OctetString"
_AppcHistConvPcid_Object = MibTableColumn
appcHistConvPcid = _AppcHistConvPcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 7),
    _AppcHistConvPcid_Type()
)
appcHistConvPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvPcid.setStatus("current")
_AppcHistConvSenseData_Type = SnaSenseData
_AppcHistConvSenseData_Object = MibTableColumn
appcHistConvSenseData = _AppcHistConvSenseData_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 8),
    _AppcHistConvSenseData_Type()
)
appcHistConvSenseData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvSenseData.setStatus("current")


class _AppcHistConvLogData_Type(OctetString):
    """Custom type appcHistConvLogData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppcHistConvLogData_Type.__name__ = "OctetString"
_AppcHistConvLogData_Object = MibTableColumn
appcHistConvLogData = _AppcHistConvLogData_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 9),
    _AppcHistConvLogData_Type()
)
appcHistConvLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvLogData.setStatus("current")


class _AppcHistConvEndedBy_Type(Integer32):
    """Custom type appcHistConvEndedBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localLu", 1),
          ("partnerLu", 2))
    )


_AppcHistConvEndedBy_Type.__name__ = "Integer32"
_AppcHistConvEndedBy_Object = MibTableColumn
appcHistConvEndedBy = _AppcHistConvEndedBy_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 5, 2, 1, 10),
    _AppcHistConvEndedBy_Type()
)
appcHistConvEndedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcHistConvEndedBy.setStatus("current")
_AppcCPIC_ObjectIdentity = ObjectIdentity
appcCPIC = _AppcCPIC_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6)
)
_AppcCpicAdminTable_Object = MibTable
appcCpicAdminTable = _AppcCpicAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    appcCpicAdminTable.setStatus("current")
_AppcCpicAdminEntry_Object = MibTableRow
appcCpicAdminEntry = _AppcCpicAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1)
)
appcCpicAdminEntry.setIndexNames(
    (0, "APPC-MIB", "appcCpicAdminLocLuName"),
    (0, "APPC-MIB", "appcCpicAdminSymbDestName"),
)
if mibBuilder.loadTexts:
    appcCpicAdminEntry.setStatus("current")


class _AppcCpicAdminLocLuName_Type(DisplayString):
    """Custom type appcCpicAdminLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcCpicAdminLocLuName_Type.__name__ = "DisplayString"
_AppcCpicAdminLocLuName_Object = MibTableColumn
appcCpicAdminLocLuName = _AppcCpicAdminLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 1),
    _AppcCpicAdminLocLuName_Type()
)
appcCpicAdminLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcCpicAdminLocLuName.setStatus("current")


class _AppcCpicAdminSymbDestName_Type(DisplayString):
    """Custom type appcCpicAdminSymbDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcCpicAdminSymbDestName_Type.__name__ = "DisplayString"
_AppcCpicAdminSymbDestName_Object = MibTableColumn
appcCpicAdminSymbDestName = _AppcCpicAdminSymbDestName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 2),
    _AppcCpicAdminSymbDestName_Type()
)
appcCpicAdminSymbDestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcCpicAdminSymbDestName.setStatus("current")


class _AppcCpicAdminParLuAlias_Type(DisplayString):
    """Custom type appcCpicAdminParLuAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcCpicAdminParLuAlias_Type.__name__ = "DisplayString"
_AppcCpicAdminParLuAlias_Object = MibTableColumn
appcCpicAdminParLuAlias = _AppcCpicAdminParLuAlias_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 3),
    _AppcCpicAdminParLuAlias_Type()
)
appcCpicAdminParLuAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicAdminParLuAlias.setStatus("current")


class _AppcCpicAdminParLuName_Type(DisplayString):
    """Custom type appcCpicAdminParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcCpicAdminParLuName_Type.__name__ = "DisplayString"
_AppcCpicAdminParLuName_Object = MibTableColumn
appcCpicAdminParLuName = _AppcCpicAdminParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 4),
    _AppcCpicAdminParLuName_Type()
)
appcCpicAdminParLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicAdminParLuName.setStatus("current")


class _AppcCpicAdminModeName_Type(DisplayString):
    """Custom type appcCpicAdminModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcCpicAdminModeName_Type.__name__ = "DisplayString"
_AppcCpicAdminModeName_Object = MibTableColumn
appcCpicAdminModeName = _AppcCpicAdminModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 5),
    _AppcCpicAdminModeName_Type()
)
appcCpicAdminModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicAdminModeName.setStatus("current")


class _AppcCpicAdminTpNameType_Type(Integer32):
    """Custom type appcCpicAdminTpNameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("snaServiceTp", 2))
    )


_AppcCpicAdminTpNameType_Type.__name__ = "Integer32"
_AppcCpicAdminTpNameType_Object = MibTableColumn
appcCpicAdminTpNameType = _AppcCpicAdminTpNameType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 6),
    _AppcCpicAdminTpNameType_Type()
)
appcCpicAdminTpNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicAdminTpNameType.setStatus("current")


class _AppcCpicAdminTpName_Type(DisplayString):
    """Custom type appcCpicAdminTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AppcCpicAdminTpName_Type.__name__ = "DisplayString"
_AppcCpicAdminTpName_Object = MibTableColumn
appcCpicAdminTpName = _AppcCpicAdminTpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 7),
    _AppcCpicAdminTpName_Type()
)
appcCpicAdminTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicAdminTpName.setStatus("current")


class _AppcCpicAdminUserid_Type(DisplayString):
    """Custom type appcCpicAdminUserid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AppcCpicAdminUserid_Type.__name__ = "DisplayString"
_AppcCpicAdminUserid_Object = MibTableColumn
appcCpicAdminUserid = _AppcCpicAdminUserid_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 8),
    _AppcCpicAdminUserid_Type()
)
appcCpicAdminUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicAdminUserid.setStatus("current")


class _AppcCpicAdminSecurity_Type(Integer32):
    """Custom type appcCpicAdminSecurity based on Integer32"""
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
        *(("distributed", 5),
          ("mutual", 6),
          ("none", 1),
          ("pgm", 3),
          ("pgmStrong", 4),
          ("same", 2))
    )


_AppcCpicAdminSecurity_Type.__name__ = "Integer32"
_AppcCpicAdminSecurity_Object = MibTableColumn
appcCpicAdminSecurity = _AppcCpicAdminSecurity_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 1, 1, 9),
    _AppcCpicAdminSecurity_Type()
)
appcCpicAdminSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicAdminSecurity.setStatus("current")
_AppcCpicOperTable_Object = MibTable
appcCpicOperTable = _AppcCpicOperTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    appcCpicOperTable.setStatus("current")
_AppcCpicOperEntry_Object = MibTableRow
appcCpicOperEntry = _AppcCpicOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1)
)
appcCpicOperEntry.setIndexNames(
    (0, "APPC-MIB", "appcCpicOperLocLuName"),
    (0, "APPC-MIB", "appcCpicOperSymbDestName"),
)
if mibBuilder.loadTexts:
    appcCpicOperEntry.setStatus("current")


class _AppcCpicOperLocLuName_Type(DisplayString):
    """Custom type appcCpicOperLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcCpicOperLocLuName_Type.__name__ = "DisplayString"
_AppcCpicOperLocLuName_Object = MibTableColumn
appcCpicOperLocLuName = _AppcCpicOperLocLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 1),
    _AppcCpicOperLocLuName_Type()
)
appcCpicOperLocLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcCpicOperLocLuName.setStatus("current")


class _AppcCpicOperSymbDestName_Type(DisplayString):
    """Custom type appcCpicOperSymbDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcCpicOperSymbDestName_Type.__name__ = "DisplayString"
_AppcCpicOperSymbDestName_Object = MibTableColumn
appcCpicOperSymbDestName = _AppcCpicOperSymbDestName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 2),
    _AppcCpicOperSymbDestName_Type()
)
appcCpicOperSymbDestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appcCpicOperSymbDestName.setStatus("current")


class _AppcCpicOperParLuAlias_Type(DisplayString):
    """Custom type appcCpicOperParLuAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppcCpicOperParLuAlias_Type.__name__ = "DisplayString"
_AppcCpicOperParLuAlias_Object = MibTableColumn
appcCpicOperParLuAlias = _AppcCpicOperParLuAlias_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 3),
    _AppcCpicOperParLuAlias_Type()
)
appcCpicOperParLuAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicOperParLuAlias.setStatus("current")


class _AppcCpicOperParLuName_Type(DisplayString):
    """Custom type appcCpicOperParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppcCpicOperParLuName_Type.__name__ = "DisplayString"
_AppcCpicOperParLuName_Object = MibTableColumn
appcCpicOperParLuName = _AppcCpicOperParLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 4),
    _AppcCpicOperParLuName_Type()
)
appcCpicOperParLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicOperParLuName.setStatus("current")


class _AppcCpicOperModeName_Type(DisplayString):
    """Custom type appcCpicOperModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppcCpicOperModeName_Type.__name__ = "DisplayString"
_AppcCpicOperModeName_Object = MibTableColumn
appcCpicOperModeName = _AppcCpicOperModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 5),
    _AppcCpicOperModeName_Type()
)
appcCpicOperModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicOperModeName.setStatus("current")


class _AppcCpicOperTpNameType_Type(Integer32):
    """Custom type appcCpicOperTpNameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("snaServiceTp", 2))
    )


_AppcCpicOperTpNameType_Type.__name__ = "Integer32"
_AppcCpicOperTpNameType_Object = MibTableColumn
appcCpicOperTpNameType = _AppcCpicOperTpNameType_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 6),
    _AppcCpicOperTpNameType_Type()
)
appcCpicOperTpNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicOperTpNameType.setStatus("current")


class _AppcCpicOperTpName_Type(DisplayString):
    """Custom type appcCpicOperTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AppcCpicOperTpName_Type.__name__ = "DisplayString"
_AppcCpicOperTpName_Object = MibTableColumn
appcCpicOperTpName = _AppcCpicOperTpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 7),
    _AppcCpicOperTpName_Type()
)
appcCpicOperTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicOperTpName.setStatus("current")


class _AppcCpicOperUserid_Type(DisplayString):
    """Custom type appcCpicOperUserid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AppcCpicOperUserid_Type.__name__ = "DisplayString"
_AppcCpicOperUserid_Object = MibTableColumn
appcCpicOperUserid = _AppcCpicOperUserid_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 8),
    _AppcCpicOperUserid_Type()
)
appcCpicOperUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicOperUserid.setStatus("current")


class _AppcCpicOperSecurity_Type(Integer32):
    """Custom type appcCpicOperSecurity based on Integer32"""
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
        *(("distributed", 5),
          ("mutual", 6),
          ("none", 1),
          ("pgm", 3),
          ("pgmStrong", 4),
          ("same", 2))
    )


_AppcCpicOperSecurity_Type.__name__ = "Integer32"
_AppcCpicOperSecurity_Object = MibTableColumn
appcCpicOperSecurity = _AppcCpicOperSecurity_Object(
    (1, 3, 6, 1, 2, 1, 34, 3, 1, 6, 2, 1, 9),
    _AppcCpicOperSecurity_Type()
)
appcCpicOperSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appcCpicOperSecurity.setStatus("current")
_AppcConformance_ObjectIdentity = ObjectIdentity
appcConformance = _AppcConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 2)
)
_AppcCompliances_ObjectIdentity = ObjectIdentity
appcCompliances = _AppcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 1)
)
_AppcGroups_ObjectIdentity = ObjectIdentity
appcGroups = _AppcGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2)
)

# Managed Objects groups

appcGlobalConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 1)
)
appcGlobalConfGroup.setObjects(
      *(("APPC-MIB", "appcUpTime"),
        ("APPC-MIB", "appcDefaultModeName"),
        ("APPC-MIB", "appcDefaultLuName"),
        ("APPC-MIB", "appcDefaultImplInbndPlu"),
        ("APPC-MIB", "appcDefaultMaxMcLlSndSize"),
        ("APPC-MIB", "appcDefaultFileSpec"),
        ("APPC-MIB", "appcDefaultTpOperation"),
        ("APPC-MIB", "appcDefaultTpConvSecRqd"),
        ("APPC-MIB", "appcLocalCpName"),
        ("APPC-MIB", "appcActiveSessions"),
        ("APPC-MIB", "appcActiveHprSessions"))
)
if mibBuilder.loadTexts:
    appcGlobalConfGroup.setStatus("current")

appcLluConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 2)
)
appcLluConfGroup.setObjects(
      *(("APPC-MIB", "appcLluAdminDepType"),
        ("APPC-MIB", "appcLluAdminLocalAddress"),
        ("APPC-MIB", "appcLluAdminSessLimit"),
        ("APPC-MIB", "appcLluAdminBindRspMayQ"),
        ("APPC-MIB", "appcLluAdminCompression"),
        ("APPC-MIB", "appcLluAdminInBoundCompLevel"),
        ("APPC-MIB", "appcLluAdminOutBoundCompLevel"),
        ("APPC-MIB", "appcLluAdminCompRleBeforeLZ"),
        ("APPC-MIB", "appcLluAdminAlias"),
        ("APPC-MIB", "appcLluOperDepType"),
        ("APPC-MIB", "appcLluOperLocalAddress"),
        ("APPC-MIB", "appcLluOperSessLimit"),
        ("APPC-MIB", "appcLluOperBindRspMayQ"),
        ("APPC-MIB", "appcLluOperCompression"),
        ("APPC-MIB", "appcLluOperInBoundCompLevel"),
        ("APPC-MIB", "appcLluOperOutBoundCompLevel"),
        ("APPC-MIB", "appcLluOperCompRleBeforeLZ"),
        ("APPC-MIB", "appcLluOperAlias"),
        ("APPC-MIB", "appcLluOperActiveSessions"))
)
if mibBuilder.loadTexts:
    appcLluConfGroup.setStatus("current")

appcParLuConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 3)
)
appcParLuConfGroup.setObjects(
      *(("APPC-MIB", "appcLuPairAdminParLuAlias"),
        ("APPC-MIB", "appcLuPairAdminSessLimit"),
        ("APPC-MIB", "appcLuPairAdminSessSec"),
        ("APPC-MIB", "appcLuPairAdminSecAccept"),
        ("APPC-MIB", "appcLuPairAdminLinkObjId"),
        ("APPC-MIB", "appcLuPairAdminParaSessSup"),
        ("APPC-MIB", "appcLuPairOperParLuAlias"),
        ("APPC-MIB", "appcLuPairOperSessLimit"),
        ("APPC-MIB", "appcLuPairOperSessSec"),
        ("APPC-MIB", "appcLuPairOperSecAccept"),
        ("APPC-MIB", "appcLuPairOperLinkObjId"),
        ("APPC-MIB", "appcLuPairOperParaSessSup"),
        ("APPC-MIB", "appcLuPairOperParaSessSupLS"),
        ("APPC-MIB", "appcLuPairOperState"))
)
if mibBuilder.loadTexts:
    appcParLuConfGroup.setStatus("current")

appcModeConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 4)
)
appcModeConfGroup.setObjects(
      *(("APPC-MIB", "appcModeAdminCosName"),
        ("APPC-MIB", "appcModeAdminSessEndTpName"),
        ("APPC-MIB", "appcModeAdminMaxSessLimit"),
        ("APPC-MIB", "appcModeAdminMinCwinLimit"),
        ("APPC-MIB", "appcModeAdminMinClosLimit"),
        ("APPC-MIB", "appcModeAdminConWinAutoActLmt"),
        ("APPC-MIB", "appcModeAdminRecvPacWinSz"),
        ("APPC-MIB", "appcModeAdminSendPacWinSz"),
        ("APPC-MIB", "appcModeAdminPrefRecvRuSz"),
        ("APPC-MIB", "appcModeAdminPrefSendRuSz"),
        ("APPC-MIB", "appcModeAdminRecvRuSzUpBnd"),
        ("APPC-MIB", "appcModeAdminSendRuSzUpBnd"),
        ("APPC-MIB", "appcModeAdminRecvRuSzLoBnd"),
        ("APPC-MIB", "appcModeAdminSendRuSzLoBnd"),
        ("APPC-MIB", "appcModeAdminSingSessReinit"),
        ("APPC-MIB", "appcModeAdminCompression"),
        ("APPC-MIB", "appcModeAdminInBoundCompLevel"),
        ("APPC-MIB", "appcModeAdminOutBoundCompLevel"),
        ("APPC-MIB", "appcModeAdminCompRleBeforeLZ"),
        ("APPC-MIB", "appcModeAdminSyncLvl"),
        ("APPC-MIB", "appcModeAdminCrypto"),
        ("APPC-MIB", "appcModeOperCosName"),
        ("APPC-MIB", "appcModeOperSessEndTpName"),
        ("APPC-MIB", "appcModeOperSessLimit"),
        ("APPC-MIB", "appcModeOperMaxSessLimit"),
        ("APPC-MIB", "appcModeOperMinCwinLimit"),
        ("APPC-MIB", "appcModeOperMinClosLimit"),
        ("APPC-MIB", "appcModeOperConWinAutoActLmt"),
        ("APPC-MIB", "appcModeOperRecvPacWinSz"),
        ("APPC-MIB", "appcModeOperSendPacWinSz"),
        ("APPC-MIB", "appcModeOperPrefRecvRuSz"),
        ("APPC-MIB", "appcModeOperPrefSendRuSz"),
        ("APPC-MIB", "appcModeOperRecvRuSzUpBnd"),
        ("APPC-MIB", "appcModeOperSendRuSzUpBnd"),
        ("APPC-MIB", "appcModeOperRecvRuSzLoBnd"),
        ("APPC-MIB", "appcModeOperSendRuSzLoBnd"),
        ("APPC-MIB", "appcModeOperSingSessReinit"),
        ("APPC-MIB", "appcModeOperCompression"),
        ("APPC-MIB", "appcModeOperInBoundCompLevel"),
        ("APPC-MIB", "appcModeOperOutBoundCompLevel"),
        ("APPC-MIB", "appcModeOperCompRleBeforeLZ"),
        ("APPC-MIB", "appcModeOperSyncLvl"),
        ("APPC-MIB", "appcModeOperCrypto"),
        ("APPC-MIB", "appcModeOperSyncLvlLastStart"),
        ("APPC-MIB", "appcModeOperCryptoLastStart"),
        ("APPC-MIB", "appcModeOperCNOSNeg"),
        ("APPC-MIB", "appcModeOperActCwin"),
        ("APPC-MIB", "appcModeOperActClos"),
        ("APPC-MIB", "appcModeOperPndCwin"),
        ("APPC-MIB", "appcModeOperPndClos"),
        ("APPC-MIB", "appcModeOperPtmCwin"),
        ("APPC-MIB", "appcModeOperPtmClos"),
        ("APPC-MIB", "appcModeOperDrainSelf"),
        ("APPC-MIB", "appcModeOperDrainPart"))
)
if mibBuilder.loadTexts:
    appcModeConfGroup.setStatus("current")

appcTpConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 5)
)
appcTpConfGroup.setObjects(
      *(("APPC-MIB", "appcTpAdminFileSpec"),
        ("APPC-MIB", "appcTpAdminStartParm"),
        ("APPC-MIB", "appcTpAdminTpOperation"),
        ("APPC-MIB", "appcTpAdminInAttachTimeout"),
        ("APPC-MIB", "appcTpAdminRcvAllocTimeout"),
        ("APPC-MIB", "appcTpAdminSyncLvl"),
        ("APPC-MIB", "appcTpAdminInstLmt"),
        ("APPC-MIB", "appcTpAdminStatus"),
        ("APPC-MIB", "appcTpAdminLongRun"),
        ("APPC-MIB", "appcTpAdminConvType"),
        ("APPC-MIB", "appcTpAdminConvDuplex"),
        ("APPC-MIB", "appcTpAdminConvSecReq"),
        ("APPC-MIB", "appcTpAdminVerPip"),
        ("APPC-MIB", "appcTpAdminPipSubNum"))
)
if mibBuilder.loadTexts:
    appcTpConfGroup.setStatus("current")

appcSessionConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 6)
)
appcSessionConfGroup.setObjects(
      *(("APPC-MIB", "appcActSessPcidCpName"),
        ("APPC-MIB", "appcActSessPcid"),
        ("APPC-MIB", "appcActSessPluIndicator"),
        ("APPC-MIB", "appcActSessModeName"),
        ("APPC-MIB", "appcActSessCosName"),
        ("APPC-MIB", "appcActSessTransPriority"),
        ("APPC-MIB", "appcActSessEnhanceSecSup"),
        ("APPC-MIB", "appcActSessSendPacingType"),
        ("APPC-MIB", "appcActSessSendRpc"),
        ("APPC-MIB", "appcActSessSendNxWndwSize"),
        ("APPC-MIB", "appcActSessRecvPacingType"),
        ("APPC-MIB", "appcActSessRecvRpc"),
        ("APPC-MIB", "appcActSessRecvNxWndwSize"),
        ("APPC-MIB", "appcActSessRscv"),
        ("APPC-MIB", "appcActSessInUse"),
        ("APPC-MIB", "appcActSessMaxSndRuSize"),
        ("APPC-MIB", "appcActSessMaxRcvRuSize"),
        ("APPC-MIB", "appcActSessSndPacingSize"),
        ("APPC-MIB", "appcActSessRcvPacingSize"),
        ("APPC-MIB", "appcActSessOperState"),
        ("APPC-MIB", "appcActSessUpTime"),
        ("APPC-MIB", "appcActSessRtpNceId"),
        ("APPC-MIB", "appcActSessRtpTcid"),
        ("APPC-MIB", "appcActSessLinkIndex"),
        ("APPC-MIB", "appcSessStatsSentFmdBytes"),
        ("APPC-MIB", "appcSessStatsSentNonFmdBytes"),
        ("APPC-MIB", "appcSessStatsRcvdFmdBytes"),
        ("APPC-MIB", "appcSessStatsRcvdNonFmdBytes"),
        ("APPC-MIB", "appcSessStatsSentFmdRus"),
        ("APPC-MIB", "appcSessStatsSentNonFmdRus"),
        ("APPC-MIB", "appcSessStatsRcvdFmdRus"),
        ("APPC-MIB", "appcSessStatsRcvdNonFmdRus"),
        ("APPC-MIB", "appcSessStatsCtrUpTime"),
        ("APPC-MIB", "appcHistSessTime"),
        ("APPC-MIB", "appcHistSessType"),
        ("APPC-MIB", "appcHistSessLocLuName"),
        ("APPC-MIB", "appcHistSessParLuName"),
        ("APPC-MIB", "appcHistSessModeName"),
        ("APPC-MIB", "appcHistSessUnbindType"),
        ("APPC-MIB", "appcHistSessSenseData"),
        ("APPC-MIB", "appcHistSessComponentId"),
        ("APPC-MIB", "appcHistSessDetectModule"),
        ("APPC-MIB", "appcSessRtpSessions"))
)
if mibBuilder.loadTexts:
    appcSessionConfGroup.setStatus("current")

appcControlConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 7)
)
appcControlConfGroup.setObjects(
      *(("APPC-MIB", "appcCntrlAdminStat"),
        ("APPC-MIB", "appcCntrlAdminRscv"),
        ("APPC-MIB", "appcCntrlAdminTrace"),
        ("APPC-MIB", "appcCntrlAdminTraceParm"),
        ("APPC-MIB", "appcCntrlOperStat"),
        ("APPC-MIB", "appcCntrlOperStatTime"),
        ("APPC-MIB", "appcCntrlOperRscv"),
        ("APPC-MIB", "appcCntrlOperRscvTime"),
        ("APPC-MIB", "appcCntrlOperTrace"),
        ("APPC-MIB", "appcCntrlOperTraceTime"),
        ("APPC-MIB", "appcCntrlOperTraceParm"))
)
if mibBuilder.loadTexts:
    appcControlConfGroup.setStatus("current")

appcCnosConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 8)
)
appcCnosConfGroup.setObjects(
      *(("APPC-MIB", "appcCnosCommand"),
        ("APPC-MIB", "appcCnosMaxSessLimit"),
        ("APPC-MIB", "appcCnosMinCwinLimit"),
        ("APPC-MIB", "appcCnosMinClosLimit"),
        ("APPC-MIB", "appcCnosDrainSelf"),
        ("APPC-MIB", "appcCnosDrainPart"),
        ("APPC-MIB", "appcCnosResponsible"),
        ("APPC-MIB", "appcCnosForce"),
        ("APPC-MIB", "appcCnosTargetLocLuName"),
        ("APPC-MIB", "appcCnosTargetParLuName"),
        ("APPC-MIB", "appcCnosTargetModeName"))
)
if mibBuilder.loadTexts:
    appcCnosConfGroup.setStatus("current")

appcCpicConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 9)
)
appcCpicConfGroup.setObjects(
      *(("APPC-MIB", "appcCpicAdminParLuAlias"),
        ("APPC-MIB", "appcCpicAdminParLuName"),
        ("APPC-MIB", "appcCpicAdminModeName"),
        ("APPC-MIB", "appcCpicAdminTpNameType"),
        ("APPC-MIB", "appcCpicAdminTpName"),
        ("APPC-MIB", "appcCpicAdminUserid"),
        ("APPC-MIB", "appcCpicAdminSecurity"),
        ("APPC-MIB", "appcCpicOperParLuAlias"),
        ("APPC-MIB", "appcCpicOperParLuName"),
        ("APPC-MIB", "appcCpicOperModeName"),
        ("APPC-MIB", "appcCpicOperTpNameType"),
        ("APPC-MIB", "appcCpicOperTpName"),
        ("APPC-MIB", "appcCpicOperUserid"),
        ("APPC-MIB", "appcCpicOperSecurity"))
)
if mibBuilder.loadTexts:
    appcCpicConfGroup.setStatus("current")

appcConversationConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 2, 10)
)
appcConversationConfGroup.setObjects(
      *(("APPC-MIB", "appcActiveConvId"),
        ("APPC-MIB", "appcActiveConvState"),
        ("APPC-MIB", "appcActiveConvType"),
        ("APPC-MIB", "appcActiveConvCorrelator"),
        ("APPC-MIB", "appcActiveConvSyncLvl"),
        ("APPC-MIB", "appcActiveConvSource"),
        ("APPC-MIB", "appcActiveConvDuplex"),
        ("APPC-MIB", "appcActiveConvUpTime"),
        ("APPC-MIB", "appcActiveConvSendBytes"),
        ("APPC-MIB", "appcActiveConvRcvBytes"),
        ("APPC-MIB", "appcActiveConvUserid"),
        ("APPC-MIB", "appcActiveConvPcidNauName"),
        ("APPC-MIB", "appcActiveConvPcid"),
        ("APPC-MIB", "appcActiveConvModeName"),
        ("APPC-MIB", "appcActiveConvLuwIdName"),
        ("APPC-MIB", "appcActiveConvLuwIdInstance"),
        ("APPC-MIB", "appcActiveConvLuwIdSequence"),
        ("APPC-MIB", "appcActiveConvTpName"),
        ("APPC-MIB", "appcHistConvEndTime"),
        ("APPC-MIB", "appcHistConvLocLuName"),
        ("APPC-MIB", "appcHistConvParLuName"),
        ("APPC-MIB", "appcHistConvTpName"),
        ("APPC-MIB", "appcHistConvPcidNauName"),
        ("APPC-MIB", "appcHistConvPcid"),
        ("APPC-MIB", "appcHistConvSenseData"),
        ("APPC-MIB", "appcHistConvLogData"),
        ("APPC-MIB", "appcHistConvEndedBy"))
)
if mibBuilder.loadTexts:
    appcConversationConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

appcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    appcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPC-MIB",
    **{"SnaSenseData": SnaSenseData,
       "appcMIB": appcMIB,
       "appcObjects": appcObjects,
       "appcGlobal": appcGlobal,
       "appcCntrlAdminGroup": appcCntrlAdminGroup,
       "appcCntrlAdminStat": appcCntrlAdminStat,
       "appcCntrlAdminRscv": appcCntrlAdminRscv,
       "appcCntrlAdminTrace": appcCntrlAdminTrace,
       "appcCntrlAdminTraceParm": appcCntrlAdminTraceParm,
       "appcCntrlOperGroup": appcCntrlOperGroup,
       "appcCntrlOperStat": appcCntrlOperStat,
       "appcCntrlOperStatTime": appcCntrlOperStatTime,
       "appcCntrlOperRscv": appcCntrlOperRscv,
       "appcCntrlOperRscvTime": appcCntrlOperRscvTime,
       "appcCntrlOperTrace": appcCntrlOperTrace,
       "appcCntrlOperTraceTime": appcCntrlOperTraceTime,
       "appcCntrlOperTraceParm": appcCntrlOperTraceParm,
       "appcGlobalObjects": appcGlobalObjects,
       "appcUpTime": appcUpTime,
       "appcDefaultModeName": appcDefaultModeName,
       "appcDefaultLuName": appcDefaultLuName,
       "appcDefaultImplInbndPlu": appcDefaultImplInbndPlu,
       "appcDefaultMaxMcLlSndSize": appcDefaultMaxMcLlSndSize,
       "appcDefaultFileSpec": appcDefaultFileSpec,
       "appcDefaultTpOperation": appcDefaultTpOperation,
       "appcDefaultTpConvSecRqd": appcDefaultTpConvSecRqd,
       "appcLocalCpName": appcLocalCpName,
       "appcActiveSessions": appcActiveSessions,
       "appcActiveHprSessions": appcActiveHprSessions,
       "appcCnosControl": appcCnosControl,
       "appcCnosCommand": appcCnosCommand,
       "appcCnosMaxSessLimit": appcCnosMaxSessLimit,
       "appcCnosMinCwinLimit": appcCnosMinCwinLimit,
       "appcCnosMinClosLimit": appcCnosMinClosLimit,
       "appcCnosDrainSelf": appcCnosDrainSelf,
       "appcCnosDrainPart": appcCnosDrainPart,
       "appcCnosResponsible": appcCnosResponsible,
       "appcCnosForce": appcCnosForce,
       "appcCnosTargetLocLuName": appcCnosTargetLocLuName,
       "appcCnosTargetParLuName": appcCnosTargetParLuName,
       "appcCnosTargetModeName": appcCnosTargetModeName,
       "appcLu": appcLu,
       "appcLluAdminTable": appcLluAdminTable,
       "appcLluAdminEntry": appcLluAdminEntry,
       "appcLluAdminName": appcLluAdminName,
       "appcLluAdminDepType": appcLluAdminDepType,
       "appcLluAdminLocalAddress": appcLluAdminLocalAddress,
       "appcLluAdminSessLimit": appcLluAdminSessLimit,
       "appcLluAdminBindRspMayQ": appcLluAdminBindRspMayQ,
       "appcLluAdminCompression": appcLluAdminCompression,
       "appcLluAdminInBoundCompLevel": appcLluAdminInBoundCompLevel,
       "appcLluAdminOutBoundCompLevel": appcLluAdminOutBoundCompLevel,
       "appcLluAdminCompRleBeforeLZ": appcLluAdminCompRleBeforeLZ,
       "appcLluAdminAlias": appcLluAdminAlias,
       "appcLluOperTable": appcLluOperTable,
       "appcLluOperEntry": appcLluOperEntry,
       "appcLluOperName": appcLluOperName,
       "appcLluOperDepType": appcLluOperDepType,
       "appcLluOperLocalAddress": appcLluOperLocalAddress,
       "appcLluOperSessLimit": appcLluOperSessLimit,
       "appcLluOperBindRspMayQ": appcLluOperBindRspMayQ,
       "appcLluOperCompression": appcLluOperCompression,
       "appcLluOperInBoundCompLevel": appcLluOperInBoundCompLevel,
       "appcLluOperOutBoundCompLevel": appcLluOperOutBoundCompLevel,
       "appcLluOperCompRleBeforeLZ": appcLluOperCompRleBeforeLZ,
       "appcLluOperAlias": appcLluOperAlias,
       "appcLluOperActiveSessions": appcLluOperActiveSessions,
       "appcLuPairAdminTable": appcLuPairAdminTable,
       "appcLuPairAdminEntry": appcLuPairAdminEntry,
       "appcLuPairAdminLocLuName": appcLuPairAdminLocLuName,
       "appcLuPairAdminParLuName": appcLuPairAdminParLuName,
       "appcLuPairAdminParLuAlias": appcLuPairAdminParLuAlias,
       "appcLuPairAdminSessLimit": appcLuPairAdminSessLimit,
       "appcLuPairAdminSessSec": appcLuPairAdminSessSec,
       "appcLuPairAdminSecAccept": appcLuPairAdminSecAccept,
       "appcLuPairAdminLinkObjId": appcLuPairAdminLinkObjId,
       "appcLuPairAdminParaSessSup": appcLuPairAdminParaSessSup,
       "appcLuPairOperTable": appcLuPairOperTable,
       "appcLuPairOperEntry": appcLuPairOperEntry,
       "appcLuPairOperLocLuName": appcLuPairOperLocLuName,
       "appcLuPairOperParLuName": appcLuPairOperParLuName,
       "appcLuPairOperParLuAlias": appcLuPairOperParLuAlias,
       "appcLuPairOperSessLimit": appcLuPairOperSessLimit,
       "appcLuPairOperSessSec": appcLuPairOperSessSec,
       "appcLuPairOperSecAccept": appcLuPairOperSecAccept,
       "appcLuPairOperLinkObjId": appcLuPairOperLinkObjId,
       "appcLuPairOperParaSessSup": appcLuPairOperParaSessSup,
       "appcLuPairOperParaSessSupLS": appcLuPairOperParaSessSupLS,
       "appcLuPairOperState": appcLuPairOperState,
       "appcModeAdminTable": appcModeAdminTable,
       "appcModeAdminEntry": appcModeAdminEntry,
       "appcModeAdminLocLuName": appcModeAdminLocLuName,
       "appcModeAdminParLuName": appcModeAdminParLuName,
       "appcModeAdminModeName": appcModeAdminModeName,
       "appcModeAdminCosName": appcModeAdminCosName,
       "appcModeAdminSessEndTpName": appcModeAdminSessEndTpName,
       "appcModeAdminMaxSessLimit": appcModeAdminMaxSessLimit,
       "appcModeAdminMinCwinLimit": appcModeAdminMinCwinLimit,
       "appcModeAdminMinClosLimit": appcModeAdminMinClosLimit,
       "appcModeAdminConWinAutoActLmt": appcModeAdminConWinAutoActLmt,
       "appcModeAdminRecvPacWinSz": appcModeAdminRecvPacWinSz,
       "appcModeAdminSendPacWinSz": appcModeAdminSendPacWinSz,
       "appcModeAdminPrefRecvRuSz": appcModeAdminPrefRecvRuSz,
       "appcModeAdminPrefSendRuSz": appcModeAdminPrefSendRuSz,
       "appcModeAdminRecvRuSzUpBnd": appcModeAdminRecvRuSzUpBnd,
       "appcModeAdminSendRuSzUpBnd": appcModeAdminSendRuSzUpBnd,
       "appcModeAdminRecvRuSzLoBnd": appcModeAdminRecvRuSzLoBnd,
       "appcModeAdminSendRuSzLoBnd": appcModeAdminSendRuSzLoBnd,
       "appcModeAdminSingSessReinit": appcModeAdminSingSessReinit,
       "appcModeAdminCompression": appcModeAdminCompression,
       "appcModeAdminInBoundCompLevel": appcModeAdminInBoundCompLevel,
       "appcModeAdminOutBoundCompLevel": appcModeAdminOutBoundCompLevel,
       "appcModeAdminCompRleBeforeLZ": appcModeAdminCompRleBeforeLZ,
       "appcModeAdminSyncLvl": appcModeAdminSyncLvl,
       "appcModeAdminCrypto": appcModeAdminCrypto,
       "appcModeOperTable": appcModeOperTable,
       "appcModeOperEntry": appcModeOperEntry,
       "appcModeOperLocLuName": appcModeOperLocLuName,
       "appcModeOperParLuName": appcModeOperParLuName,
       "appcModeOperModeName": appcModeOperModeName,
       "appcModeOperCosName": appcModeOperCosName,
       "appcModeOperSessEndTpName": appcModeOperSessEndTpName,
       "appcModeOperSessLimit": appcModeOperSessLimit,
       "appcModeOperMaxSessLimit": appcModeOperMaxSessLimit,
       "appcModeOperMinCwinLimit": appcModeOperMinCwinLimit,
       "appcModeOperMinClosLimit": appcModeOperMinClosLimit,
       "appcModeOperConWinAutoActLmt": appcModeOperConWinAutoActLmt,
       "appcModeOperRecvPacWinSz": appcModeOperRecvPacWinSz,
       "appcModeOperSendPacWinSz": appcModeOperSendPacWinSz,
       "appcModeOperPrefRecvRuSz": appcModeOperPrefRecvRuSz,
       "appcModeOperPrefSendRuSz": appcModeOperPrefSendRuSz,
       "appcModeOperRecvRuSzUpBnd": appcModeOperRecvRuSzUpBnd,
       "appcModeOperSendRuSzUpBnd": appcModeOperSendRuSzUpBnd,
       "appcModeOperRecvRuSzLoBnd": appcModeOperRecvRuSzLoBnd,
       "appcModeOperSendRuSzLoBnd": appcModeOperSendRuSzLoBnd,
       "appcModeOperSingSessReinit": appcModeOperSingSessReinit,
       "appcModeOperCompression": appcModeOperCompression,
       "appcModeOperInBoundCompLevel": appcModeOperInBoundCompLevel,
       "appcModeOperOutBoundCompLevel": appcModeOperOutBoundCompLevel,
       "appcModeOperCompRleBeforeLZ": appcModeOperCompRleBeforeLZ,
       "appcModeOperSyncLvl": appcModeOperSyncLvl,
       "appcModeOperCrypto": appcModeOperCrypto,
       "appcModeOperSyncLvlLastStart": appcModeOperSyncLvlLastStart,
       "appcModeOperCryptoLastStart": appcModeOperCryptoLastStart,
       "appcModeOperCNOSNeg": appcModeOperCNOSNeg,
       "appcModeOperActCwin": appcModeOperActCwin,
       "appcModeOperActClos": appcModeOperActClos,
       "appcModeOperPndCwin": appcModeOperPndCwin,
       "appcModeOperPndClos": appcModeOperPndClos,
       "appcModeOperPtmCwin": appcModeOperPtmCwin,
       "appcModeOperPtmClos": appcModeOperPtmClos,
       "appcModeOperDrainSelf": appcModeOperDrainSelf,
       "appcModeOperDrainPart": appcModeOperDrainPart,
       "appcTp": appcTp,
       "appcTpAdminTable": appcTpAdminTable,
       "appcTpAdminEntry": appcTpAdminEntry,
       "appcTpAdminLocLuName": appcTpAdminLocLuName,
       "appcTpAdminTpName": appcTpAdminTpName,
       "appcTpAdminFileSpec": appcTpAdminFileSpec,
       "appcTpAdminStartParm": appcTpAdminStartParm,
       "appcTpAdminTpOperation": appcTpAdminTpOperation,
       "appcTpAdminInAttachTimeout": appcTpAdminInAttachTimeout,
       "appcTpAdminRcvAllocTimeout": appcTpAdminRcvAllocTimeout,
       "appcTpAdminSyncLvl": appcTpAdminSyncLvl,
       "appcTpAdminInstLmt": appcTpAdminInstLmt,
       "appcTpAdminStatus": appcTpAdminStatus,
       "appcTpAdminLongRun": appcTpAdminLongRun,
       "appcTpAdminConvType": appcTpAdminConvType,
       "appcTpAdminConvDuplex": appcTpAdminConvDuplex,
       "appcTpAdminConvSecReq": appcTpAdminConvSecReq,
       "appcTpAdminVerPip": appcTpAdminVerPip,
       "appcTpAdminPipSubNum": appcTpAdminPipSubNum,
       "appcSession": appcSession,
       "appcActSessTable": appcActSessTable,
       "appcActSessEntry": appcActSessEntry,
       "appcActSessLocLuName": appcActSessLocLuName,
       "appcActSessParLuName": appcActSessParLuName,
       "appcActSessIndex": appcActSessIndex,
       "appcActSessPcidCpName": appcActSessPcidCpName,
       "appcActSessPcid": appcActSessPcid,
       "appcActSessPluIndicator": appcActSessPluIndicator,
       "appcActSessModeName": appcActSessModeName,
       "appcActSessCosName": appcActSessCosName,
       "appcActSessTransPriority": appcActSessTransPriority,
       "appcActSessEnhanceSecSup": appcActSessEnhanceSecSup,
       "appcActSessSendPacingType": appcActSessSendPacingType,
       "appcActSessSendRpc": appcActSessSendRpc,
       "appcActSessSendNxWndwSize": appcActSessSendNxWndwSize,
       "appcActSessRecvPacingType": appcActSessRecvPacingType,
       "appcActSessRecvRpc": appcActSessRecvRpc,
       "appcActSessRecvNxWndwSize": appcActSessRecvNxWndwSize,
       "appcActSessRscv": appcActSessRscv,
       "appcActSessInUse": appcActSessInUse,
       "appcActSessMaxSndRuSize": appcActSessMaxSndRuSize,
       "appcActSessMaxRcvRuSize": appcActSessMaxRcvRuSize,
       "appcActSessSndPacingSize": appcActSessSndPacingSize,
       "appcActSessRcvPacingSize": appcActSessRcvPacingSize,
       "appcActSessOperState": appcActSessOperState,
       "appcActSessUpTime": appcActSessUpTime,
       "appcActSessRtpNceId": appcActSessRtpNceId,
       "appcActSessRtpTcid": appcActSessRtpTcid,
       "appcActSessLinkIndex": appcActSessLinkIndex,
       "appcSessStatsTable": appcSessStatsTable,
       "appcSessStatsEntry": appcSessStatsEntry,
       "appcSessStatsLocLuName": appcSessStatsLocLuName,
       "appcSessStatsParLuName": appcSessStatsParLuName,
       "appcSessStatsSessIndex": appcSessStatsSessIndex,
       "appcSessStatsSentFmdBytes": appcSessStatsSentFmdBytes,
       "appcSessStatsSentNonFmdBytes": appcSessStatsSentNonFmdBytes,
       "appcSessStatsRcvdFmdBytes": appcSessStatsRcvdFmdBytes,
       "appcSessStatsRcvdNonFmdBytes": appcSessStatsRcvdNonFmdBytes,
       "appcSessStatsSentFmdRus": appcSessStatsSentFmdRus,
       "appcSessStatsSentNonFmdRus": appcSessStatsSentNonFmdRus,
       "appcSessStatsRcvdFmdRus": appcSessStatsRcvdFmdRus,
       "appcSessStatsRcvdNonFmdRus": appcSessStatsRcvdNonFmdRus,
       "appcSessStatsCtrUpTime": appcSessStatsCtrUpTime,
       "appcHistSessTable": appcHistSessTable,
       "appcHistSessEntry": appcHistSessEntry,
       "appcHistSessIndex": appcHistSessIndex,
       "appcHistSessTime": appcHistSessTime,
       "appcHistSessType": appcHistSessType,
       "appcHistSessLocLuName": appcHistSessLocLuName,
       "appcHistSessParLuName": appcHistSessParLuName,
       "appcHistSessModeName": appcHistSessModeName,
       "appcHistSessUnbindType": appcHistSessUnbindType,
       "appcHistSessSenseData": appcHistSessSenseData,
       "appcHistSessComponentId": appcHistSessComponentId,
       "appcHistSessDetectModule": appcHistSessDetectModule,
       "appcSessRtpTable": appcSessRtpTable,
       "appcSessRtpEntry": appcSessRtpEntry,
       "appcSessRtpNceId": appcSessRtpNceId,
       "appcSessRtpTcid": appcSessRtpTcid,
       "appcSessRtpSessions": appcSessRtpSessions,
       "appcConversation": appcConversation,
       "appcActiveConvTable": appcActiveConvTable,
       "appcActiveConvEntry": appcActiveConvEntry,
       "appcActiveConvLocLuName": appcActiveConvLocLuName,
       "appcActiveConvParLuName": appcActiveConvParLuName,
       "appcActiveConvSessIndex": appcActiveConvSessIndex,
       "appcActiveConvId": appcActiveConvId,
       "appcActiveConvState": appcActiveConvState,
       "appcActiveConvType": appcActiveConvType,
       "appcActiveConvCorrelator": appcActiveConvCorrelator,
       "appcActiveConvSyncLvl": appcActiveConvSyncLvl,
       "appcActiveConvSource": appcActiveConvSource,
       "appcActiveConvDuplex": appcActiveConvDuplex,
       "appcActiveConvUpTime": appcActiveConvUpTime,
       "appcActiveConvSendBytes": appcActiveConvSendBytes,
       "appcActiveConvRcvBytes": appcActiveConvRcvBytes,
       "appcActiveConvUserid": appcActiveConvUserid,
       "appcActiveConvPcidNauName": appcActiveConvPcidNauName,
       "appcActiveConvPcid": appcActiveConvPcid,
       "appcActiveConvModeName": appcActiveConvModeName,
       "appcActiveConvLuwIdName": appcActiveConvLuwIdName,
       "appcActiveConvLuwIdInstance": appcActiveConvLuwIdInstance,
       "appcActiveConvLuwIdSequence": appcActiveConvLuwIdSequence,
       "appcActiveConvTpName": appcActiveConvTpName,
       "appcHistConvTable": appcHistConvTable,
       "appcHistConvEntry": appcHistConvEntry,
       "appcHistConvIndex": appcHistConvIndex,
       "appcHistConvEndTime": appcHistConvEndTime,
       "appcHistConvLocLuName": appcHistConvLocLuName,
       "appcHistConvParLuName": appcHistConvParLuName,
       "appcHistConvTpName": appcHistConvTpName,
       "appcHistConvPcidNauName": appcHistConvPcidNauName,
       "appcHistConvPcid": appcHistConvPcid,
       "appcHistConvSenseData": appcHistConvSenseData,
       "appcHistConvLogData": appcHistConvLogData,
       "appcHistConvEndedBy": appcHistConvEndedBy,
       "appcCPIC": appcCPIC,
       "appcCpicAdminTable": appcCpicAdminTable,
       "appcCpicAdminEntry": appcCpicAdminEntry,
       "appcCpicAdminLocLuName": appcCpicAdminLocLuName,
       "appcCpicAdminSymbDestName": appcCpicAdminSymbDestName,
       "appcCpicAdminParLuAlias": appcCpicAdminParLuAlias,
       "appcCpicAdminParLuName": appcCpicAdminParLuName,
       "appcCpicAdminModeName": appcCpicAdminModeName,
       "appcCpicAdminTpNameType": appcCpicAdminTpNameType,
       "appcCpicAdminTpName": appcCpicAdminTpName,
       "appcCpicAdminUserid": appcCpicAdminUserid,
       "appcCpicAdminSecurity": appcCpicAdminSecurity,
       "appcCpicOperTable": appcCpicOperTable,
       "appcCpicOperEntry": appcCpicOperEntry,
       "appcCpicOperLocLuName": appcCpicOperLocLuName,
       "appcCpicOperSymbDestName": appcCpicOperSymbDestName,
       "appcCpicOperParLuAlias": appcCpicOperParLuAlias,
       "appcCpicOperParLuName": appcCpicOperParLuName,
       "appcCpicOperModeName": appcCpicOperModeName,
       "appcCpicOperTpNameType": appcCpicOperTpNameType,
       "appcCpicOperTpName": appcCpicOperTpName,
       "appcCpicOperUserid": appcCpicOperUserid,
       "appcCpicOperSecurity": appcCpicOperSecurity,
       "appcConformance": appcConformance,
       "appcCompliances": appcCompliances,
       "appcCompliance": appcCompliance,
       "appcGroups": appcGroups,
       "appcGlobalConfGroup": appcGlobalConfGroup,
       "appcLluConfGroup": appcLluConfGroup,
       "appcParLuConfGroup": appcParLuConfGroup,
       "appcModeConfGroup": appcModeConfGroup,
       "appcTpConfGroup": appcTpConfGroup,
       "appcSessionConfGroup": appcSessionConfGroup,
       "appcControlConfGroup": appcControlConfGroup,
       "appcCnosConfGroup": appcCnosConfGroup,
       "appcCpicConfGroup": appcCpicConfGroup,
       "appcConversationConfGroup": appcConversationConfGroup}
)
